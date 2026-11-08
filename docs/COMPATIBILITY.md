# Compatibility and validation scope

## Tested development configuration

| Item | Recorded configuration or result |
|---|---|
| Aircraft | Guarded 2.5-inch Dragonfly quad |
| Controller/build target | MicoAir H743 V2 / `micoair_h743-v2_default` |
| Flight stack | Custom PX4 v1.16.1, pinned source base in the manifest |
| ESC | AM32; exact firmware version and target not recorded |
| RC | RadioMaster TX16S, physical RC path, recovery channel 9 |
| TRTL build size | 1,674,240 bytes; 160,768 bytes remaining in the board's reported flash region |
| Recovery | Successful real-world recovery reported by the aircraft operator |
| Driver status | One recorded attempt stopped for UPRIGHT after 440 ms of DRIVE; restore sequences were sent |

Build logs, driver output and operator reports are the basis of these results. Individual fault scenarios require their own recorded hardware tests.

## Supported software configuration

The controller requires four distinct PX4 logical motors (1..4) in X-like corners, fixed near-vertical thrust axes, non-VTOL rotary-wing geometry, and one DShot driver instance controlling all recovery motors. The ESC firmware must support verified temporary relative-direction command semantics 21/20. Configuration is opt-in.

The geometry checker validates corner positions in the corresponding body-frame quadrants. Motor selection uses corner pairs or a single corner; it does not weight torque by frame dimensions. Deadcat and stretched frames need propulsion and recovery tuning for their geometry.

## Configurations outside the current scope

- PWM, OneShot, CAN or mixed motor-output backends;
- plus, coaxial, tilting, VTOL, hexa or octa configurations;
- 3D/reversible-throttle setups;
- multiple selectable RC inputs.

Each additional flight controller requires its own board target, sufficient memory and build validation. Each ESC/aircraft combination requires hardware validation.

## Additional validation work

Record the exact ESC firmware version and target, normal-direction verification, cancellation/link-loss/reacquisition results, FC-only reset behavior while ESCs remain powered, and ESC brownout/reset behavior during a recovery transaction. Perform fault testing in a controlled bench setup.

See [Hardware validation matrix](HARDWARE_MATRIX.md) for the current evidence and the fields needed to document another platform.
