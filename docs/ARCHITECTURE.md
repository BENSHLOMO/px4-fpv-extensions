# Turtle recovery architecture

## Active path

`DShot::Run()` polls configuration and input topics, invokes the normal mixer update, and provides a recovery-only fallback output callback when needed. The existing DShot driver owns physical motor output throughout recovery.

`update_turtle_parameters()` caches configuration, resolves logical motor corner assignments to active output bits, checks allocator geometry and radio conflicts, and accepts changes only in the permitted idle/disarmed/OFF conditions. Parameter values shown in QGroundControl can therefore differ temporarily from the active driver snapshot. Center switch position does not qualify as OFF.

`update_turtle_inputs()` separately checks RC channel health, manual-control freshness/source, arming/safety state, attitude, motor assignments and stick deflection.

`DragonflyTurtleCore.hpp` executes:

```text
IDLE -> HOLD -> PRESTOP -> REVERSE -> SETTLE -> DRIVE
                                     cancellation / cutoff / timeout
                      -> POSTSTOP -> RESTORE -> COOLDOWN -> WAIT_OFF -> IDLE
```

Startup uses POSTSTOP/RESTORE/COOLDOWN/WAIT_OFF before readiness. Certain unrecoverable conditions latch FAULT. RESTORE represents transmitted temporary normal-direction commands, not acknowledgements.

`src/lib/dragonfly_turtle/ArmingInterlock.hpp` is shared by Commander and DShot in the monolithic build. Atomic ownership separates FLIGHT and RECOVERY. Commander denies new arm requests when recovery owns the outputs or required readiness is absent. This interlock coordinates software ownership; an independent hardware watchdog is outside its scope.

`DragonflyTurtleMapping.hpp` maps distinct logical motors 1..4 to local DShot output bits. Cardinal roll/pitch selects a side or end pair. Combined deflection selects the intersecting corner. Motor order is configurable, not hard-coded to the first four connectors.

## Legacy helpers

The patch retains earlier Motor/Timer/Angle helpers and unused driver members. The active B8 state machine is `DragonflyTurtleCore.hpp`; its thresholds and enable logic govern recovery. Legacy-helper removal is tracked in [Release review](RELEASE_REVIEW.md) as a separate refactor.

## Configuration and telemetry limitations

One physical RC path is supported. Settings are latched between attempts under the permitted idle/disarmed/OFF conditions. Output assignments remain fixed during recovery. Ground contact and physical ESC direction acknowledgement are outside the reported interlock/status information.
