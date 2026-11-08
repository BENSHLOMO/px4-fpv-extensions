# Architecture of the uploaded B8 patch

## Active path

`DShot::Run()` polls configuration and input topics, invokes the normal mixer update, and provides a recovery-only fallback output callback when needed. While active, the existing DShot driver remains the physical output owner; a separate module is not used to compete with it.

`update_turtle_parameters()` caches configuration, resolves logical motor corner assignments to active output bits, checks allocator geometry and radio conflicts, and accepts changes only in the permitted idle/disarmed/OFF conditions. Parameter values shown in QGroundControl can therefore differ temporarily from the active driver snapshot. Center switch position does not qualify as OFF.

`update_turtle_inputs()` separately checks RC channel health, manual-control freshness/source, arming/safety state, attitude, motor assignments and stick deflection.

`DragonflyTurtleCore.hpp` executes:

```text
IDLE -> HOLD -> PRESTOP -> REVERSE -> SETTLE -> DRIVE
                                     cancellation / cutoff / timeout
                      -> POSTSTOP -> RESTORE -> COOLDOWN -> WAIT_OFF -> IDLE
```

Startup uses POSTSTOP/RESTORE/COOLDOWN/WAIT_OFF before readiness. Certain unrecoverable conditions latch FAULT. RESTORE represents transmitted temporary normal-direction commands, not acknowledgements.

`src/lib/dragonfly_turtle/ArmingInterlock.hpp` is shared by Commander and DShot in the monolithic build. Atomic ownership separates FLIGHT and RECOVERY. Commander denies new arm requests when recovery owns the outputs or required readiness is absent. This is software coordination, not an independent hardware watchdog.

`DragonflyTurtleMapping.hpp` maps distinct logical motors 1..4 to local DShot output bits. Cardinal roll/pitch selects a side or end pair. Combined deflection selects the intersecting corner. Motor order is configurable, not hard-coded to the first four connectors.

## Development leftovers

The exported snapshot also retains the earlier Motor/Timer/Angle helpers and unused driver members. They are not the active B8 state machine. Do not read their older thresholds as B8 policy or assume the legacy compile-enable macro governs the active controller. See the release review before cleanup.

## Configuration and telemetry limitations

Only one physical RC path is handled. Live settings are latched between attempts, not promised to apply immediately during a burst. Output assignment changes are not a supported recovery control. The interlock/status labels do not assert ground contact or successful ESC direction command acceptance.
