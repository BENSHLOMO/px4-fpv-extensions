# Compatibility and evidence

## Hardware evidence supplied in this conversation

| Item | Evidence |
|---|---|
| Aircraft | Personal guarded 2.5-inch Dragonfly quad |
| Controller/build target | MicoAir H743 V2 / `micoair_h743-v2_default` |
| Flight stack | Custom PX4 v1.16.1, pinned source base in manifest |
| ESC | AM32; exact firmware version and target not supplied |
| RC | TX16S/physical RC path, recovery channel 9 |
| Short-name target build | User log: 1,674,240 bytes; 160,768 bytes remaining in this board's reported flash region |
| Real recovery | Operator explicitly reported the short-name version worked in real use |
| Driver telemetry | One supplied attempt stopped for UPRIGHT after 440 ms of DRIVE; restore sequences were sent |

These are reported/observed conversation results, not independent flights by the reviewer. A generic successful-use statement is not converted into a pass for every distinct fault scenario.

## Intended software scope

Four PX4 logical motors (1..4), distinct X-like corners, fixed near-vertical thrust axes, supported non-VTOL rotary-wing geometry, one DShot driver instance controlling all recovery motors, and verified temporary relative-direction command semantics 21/20. Configuration is opt-in.

The geometry checker requires corner positions in the appropriate body-frame quadrants. It is not a geometry-weighted torque controller and does not promise equal performance for every deadcat or stretched frame.

Unsupported here: PWM, OneShot, CAN/mixed output backends, plus/coaxial/tilting/VTOL/hexa/octa configurations, 3D/reversible-throttle setups and multiple selectable RC inputs. Another board also needs its own build target and sufficient memory.

## Boundaries still needing evidence

Exact ESC version/target; independent normal-direction verification; cancellation/link-loss/reacquisition cases on this exact revision; FC-only reset with ESCs still powered; ESC brownout/reset during an attempt; other FC/ESC combinations. Do not deliberately inject hazardous faults in flight to fill a table.

The existing working aircraft needs no repeat flight solely to create the private repository. Future compatibility claims should grow only with recorded evidence.
