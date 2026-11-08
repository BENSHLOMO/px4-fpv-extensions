# Operator-facing behavior from this source

This is documentation of the exported code, not permission to enable it blindly on an unverified aircraft. Initial motor mapping/direction/cancellation validation belongs on a propeller-free bench with battery access.

1. Configure distinct logical FL/FR/RL/RR motors for the actual aircraft, not connector numbers. Verify normal flight configuration independently.
2. Select a calibrated RC channel without critical function conflicts. Choose polarity. With POL=1, below -0.3 is OFF and above 0.7 is ON. Center cancels a drive but does not reset the handshake.
3. Select ESC profile only after confirming compatible stopped-motor temporary commands. Power ESCs during the startup direction sequence; USB-only FC activity cannot establish command receipt by unpowered ESCs.
4. The controller waits for valid radio input and fully OFF before accepting settings. It may show initial mapping/angles until that happens.
5. Enable intentionally. Startup sends stop/normal-direction commands before readiness. `synced=1` means the software sequence completed, not that the ESCs acknowledged it.
6. While disarmed and sufficiently tilted, a fresh OFF-to-ON request begins HOLD/PRESTOP/REVERSE/SETTLE. With default timings, DRIVE does not begin immediately.
7. Roll/pitch selects motors; stick magnitude sets power when PWR=1. Entry ANGLE is separate from EXIT cutoff. DRIVE is time-bounded.
8. Turn fully OFF after an attempt. WAIT_OFF is not a permanent fault: a valid OFF dwell lets restoration release the arming interlock. FAULT is different and must be investigated without bypassing the interlock.

Use `param show TRTL*` and `dshot status`. Do not use the legacy probe's fixed-map output as the authoritative B8 status. Normal direction must be physically validated; transmitted frame counts alone are insufficient.

The one-aircraft reported map is FL logical 3 -> physical output 2, FR 1 -> 3, RL 2 -> 4, RR 4 -> 1. This is reference evidence, not an auto-loaded generic profile.
