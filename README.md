# PX4 Turtle Recovery

**Developed by [Yisrael Ben-Shlomo](https://github.com/yisrael-benshlomo) at [BENSHLOMO | Advanced Systems](https://github.com/BENSHLOMO)**

Configurable turtle mode (crash-flip recovery) for Quad-X aircraft running PX4.

Turtle mode lets a pilot recover a quadcopter that has tipped over by temporarily reversing motor direction and driving the motors selected with the roll/pitch stick to turn it upright. It is particularly useful for indoor flying and operation near obstacles, where a collision can leave an aircraft overturned and difficult to reach.

We developed this extension for Dragonfly, a 2.5-inch guarded quad, and released the source for other PX4 builders. Motor mapping, radio input, power, timing and recovery angles are configurable through 21 native `TRTL_*` parameters in QGroundControl.

**Release:** experimental source patch for PX4 v1.16.1. Hardware validation currently covers the Dragonfly configuration below. Additional builds require configuration and validation for their airframe and ESC firmware.

## Recovery demonstration

Dragonfly recovers from inverted and near-vertical starting positions, completes repeated attempts, and returns to normal arming and flight. The video includes the setup workflow and live attitude/RC telemetry alongside the aircraft.

https://github.com/user-attachments/assets/52dea387-f7dd-4787-bfcc-19a3bb74b075

Recorded on the MicoAir H743 V2 / AM32 configuration described below.

## Recovery controls

- Configurable logical FL/FR/RL/RR motor mapping and recovery switch channel/polarity.
- Roll/pitch stick selection with proportional power, minimum/maximum output and ramp time.
- Separate entry and near-upright exit angles.
- Stop → temporary reverse → drive → stop → restore sequencing.
- Switch-OFF qualification between attempts and startup direction normalization.
- Commander/DShot ownership interlock, recovery timeout, cancellation conditions and configuration checks.

Recovery commands selected motors while PX4 is disarmed. The feature defaults disabled and requires explicit configuration before use.

## Tested hardware and results

| Component | Tested configuration |
| --- | --- |
| Aircraft | Dragonfly, 2.5-inch guarded Quad-X |
| Flight controller | MicoAir H743 V2 |
| Flight stack | Custom PX4 v1.16.1 |
| ESC firmware family | AM32; exact version pending documentation |

The TRTL build compiled for the MicoAir H743 V2, loaded its parameters in QGroundControl and completed real-world recovery on Dragonfly. Testing included motor mapping, the configured upright exit threshold, direction-restoration sequencing and return to the switch-OFF reset state.

Host tests cover controller transitions, RC validation, motor-mapping permutations, fault/cancellation cases, repeated attempts and the Commander/DShot interlock. See [validation results](docs/VALIDATION.md) and the [hardware matrix](docs/HARDWARE_MATRIX.md) for the recorded scope.

## Compatibility and setup

The patch targets this PX4-Autopilot revision:

```text
94cb2012792b2ae89f0b147cfee53ee31ae550be
```

Other PX4 revisions require a separate port and validation. The supported software scope is conventional four-motor X-like geometry using compatible DShot ESC firmware.

ESC firmware must support **temporary relative DShot direction commands 21/20**. The `restores_sent` and `synced=1` diagnostics report completion of the software sequence; physical direction is not acknowledged by the ESCs. Verify mapping, direction, cancellation, restoration and arming on a secured propeller-free bench before recovery tests with propellers.

Start with the [installation guide](docs/INSTALL.md), [compatibility requirements](docs/COMPATIBILITY.md) and [operating procedure](docs/OPERATION.md). This release provides a source patch to build for your target board.

## Source, documentation and tests

| Resource | Contents |
| --- | --- |
| [Source patch](patches/dragonfly-b8-trtl.patch) | Tested checkpoint with the documented comment/SPDX cleanup |
| [Parameters](docs/PARAMETERS.md) | All 21 `TRTL_*` settings |
| [Architecture](docs/ARCHITECTURE.md) | DShot recovery controller and arming coordination |
| [Release status](docs/PUBLICATION_STATUS.md) | Validation scope and next development steps |
| [Source history](docs/SOURCE_HYGIENE.md) | Publication changes relative to the tested checkpoint |
| [Host tests](tests/) | Tests against the exported source headers |
| [Evidence](evidence/) | Recorded host-test and patch-review results |

Run the host tests:

```bash
python3 tests/run_host_tests.py
python3 tests/test_review_tools.py
```

Verify the patch against the pinned base in a local PX4 checkout:

```bash
python3 tools/verify_pinned_base.py ~/PX4-Autopilot
```

The verifier uses a temporary directory and leaves the supplied checkout unchanged.

## DJI O4 / MSP OSD

Dragonfly uses DJI O4 with PX4's existing MSP OSD support. Integration notes are tracked [separately](docs/DJI_OSD_SCOPE.md); the turtle patch covers recovery control.

## Development and license

Yisrael Ben-Shlomo led the requirements, systems integration and hardware validation. Development used AI assistance for software, debugging, documentation and review.

Released under the **BSD 3-Clause License**, with PX4 attribution retained. See [LICENSE](LICENSE), [NOTICE](NOTICE.md) and [licensing details](docs/LICENSING.md).

[Project resource](https://benshlomosystems.com/resources/px4-turtle-mode/) · [Contributing](CONTRIBUTING.md)
