# PX4 FPV Extensions

**Experimental PX4 extensions and integration notes from BENSHLOMO | Advanced Systems.**

This repository currently contains a configurable **Quad-X turtle / crash-flip recovery extension** for a pinned PX4 v1.16.1 source revision. It was developed and hardware-tested on the personal **Dragonfly** 2.5-inch guarded quad, then generalized in software for supported conventional four-motor X-like layouts.

> **Status:** experimental source-level extension. It is not an upstream PX4 feature, not production-ready, and not claimed to work on every DShot ESC or airframe.

## What has actually been demonstrated

On the Dragonfly test aircraft, the current TRTL build:

- compiled successfully for **MicoAir H743 V2**;
- loaded configurable `TRTL_*` parameters in QGroundControl;
- resolved the tested logical-to-physical motor mapping correctly;
- performed real-world turtle recovery successfully;
- stopped recovery on reaching the configured upright threshold;
- restored the recovery sequence and returned to the operator-controlled reset state.

The test aircraft uses **AM32 ESC firmware** with temporary direction commands that were verified during development. The exact AM32 firmware version still needs to be recorded before this is advertised as a reusable hardware profile.

Host-side tests also cover recovery state transitions, RC validation, motor mapping permutations, fault/cancellation cases, repeated attempts, and the Commander/DShot ownership interlock. See [`docs/VALIDATION.md`](docs/VALIDATION.md).

## Repository contents

- [`patches/dragonfly-b8-trtl.patch`](patches/dragonfly-b8-trtl.patch) — exact exported patch from the tested development checkpoint.
- [`docs/INSTALL.md`](docs/INSTALL.md) — applying the patch to the pinned PX4 source revision.
- [`docs/PARAMETERS.md`](docs/PARAMETERS.md) — all 21 `TRTL_*` parameters.
- [`docs/OPERATION.md`](docs/OPERATION.md) — controller behavior and operator workflow.
- [`docs/COMPATIBILITY.md`](docs/COMPATIBILITY.md) — supported scope and exclusions.
- [`docs/HARDWARE_MATRIX.md`](docs/HARDWARE_MATRIX.md) — hardware evidence and what has not yet been tested.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — DShot recovery architecture.
- [`tests/`](tests/) — host-side tests against the exported source headers.
- [`tools/verify_pinned_base.py`](tools/verify_pinned_base.py) — read-only patch/base verification tool.
- [`evidence/`](evidence/) — host-test and patch-review evidence.

The repository intentionally does **not** include the aircraft's private parameter dump, prebuilt firmware, SSH credentials, client material, or the full Dragonfly aircraft configuration.

## Pinned PX4 base

The exported patch targets:

```text
PX4-Autopilot commit 94cb2012792b2ae89f0b147cfee53ee31ae550be
```

Do not assume the patch applies to PX4 `main` or another release. Port and test separately.

## Core behavior

The extension adds:

- configurable logical FL/FR/RL/RR motor mapping;
- configurable RC channel and polarity;
- separate recovery-entry and near-upright exit angles;
- proportional stick power with configurable minimum, maximum and ramp;
- bounded stop → temporary reverse → drive → stop → restore sequencing;
- explicit switch-OFF qualification between attempts;
- startup normal-direction normalization;
- Commander/DShot ownership interlock to avoid normal arming while recovery owns motor output;
- configuration, geometry and RC-conflict validation.

The feature intentionally permits selected DShot motor output while PX4 is disarmed. It therefore defaults disabled/unconfigured and requires explicit setup.

## Important hardware limitation

The implementation relies on **temporary relative DShot direction commands 21/20**. A DShot-capable ESC is not automatically compatible. `restores_sent` and `synced=1` mean the software transmitted/completed its sequence; they are **not ESC acknowledgements of physical direction**.

Initial mapping, direction, cancellation, restoration and arming checks belong on a secured propeller-free bench before attempting recovery with propellers installed.

## Quick start

Read [`docs/INSTALL.md`](docs/INSTALL.md), [`docs/COMPATIBILITY.md`](docs/COMPATIBILITY.md), and [`docs/OPERATION.md`](docs/OPERATION.md) before applying the patch.

For host tests in this repository:

```bash
python3 tests/run_host_tests.py
python3 tests/test_review_tools.py
```

To verify that the patch matches the pinned base already present in a local PX4 repository:

```bash
python3 tools/verify_pinned_base.py ~/PX4-Autopilot
```

That verifier works in a temporary directory and does not modify the supplied PX4 checkout.

## DJI O4 / MSP OSD

Dragonfly also uses DJI O4 with PX4's existing MSP OSD support. That is **integration work, not a newly invented OSD protocol or driver**, and it is intentionally separate from this turtle-recovery patch. A reproducible integration guide is planned as a separate part of this repository.

## Development disclosure

Development used AI assistance for portions of code generation, debugging, documentation, and review. Hardware integration, configuration, iterative bench testing, real-aircraft testing, and release ownership were performed by **Yisrael Ben-Shlomo / BENSHLOMO Advanced Systems**.

## License

This repository uses the **BSD 3-Clause License**, matching the pinned PX4 base. See [`LICENSE`](LICENSE), [`NOTICE.md`](NOTICE.md), and [`docs/LICENSING.md`](docs/LICENSING.md).

PX4 is a project of its respective contributors. BENSHLOMO is not claiming upstream endorsement or acceptance of this extension.
