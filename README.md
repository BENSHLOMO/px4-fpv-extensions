# PX4 FPV Extensions: Dragonfly turtle recovery

**BENSHLOMO | Advanced Systems**  
**Private release-review starter, 8 November 2026. Not published, not an upstream release.**

Experimental, configurable turtle recovery for supported conventional Quad-X layouts, developed on a personal 2.5-inch guarded Dragonfly quad. This repository keeps the exported working patch unchanged and adds reproducible host checks and release documentation around it.

## Status

The operator reported successful real-world recovery on **MicoAir H743 V2 with AM32 ESCs and custom PX4 v1.16.1**. The conversation includes a successful target build and a short-name recovery status showing `reason=UPRIGHT`, 440 ms of DRIVE and restoration commands sent. Broader hardware coverage and unobserved interruption cases are not claimed.

This review independently ran host suites against the actual new headers extracted from the uploaded patch. It did **not** build PX4/NuttX, access the flight controller, verify physical ESC direction or establish universal Quad-X compatibility.

## What's included

- `patches/dragonfly-b8-trtl.patch`: the exact uploaded core patch, unchanged.
- `docs/PARAMETERS.md`: all 21 definitions extracted from that patch.
- `docs/RELEASE_REVIEW.md`: cleanup findings and publication boundaries.
- `docs/ARCHITECTURE.md`, `docs/COMPATIBILITY.md`, `docs/OPERATION.md`.
- `tests/`: runnable host tests retained from the prior B8 package, run against this exact snapshot.
- `tools/verify_pinned_base.py`: read-only check against the pinned base in a local PX4 repository; patch application occurs only in a temporary folder.
- `evidence/`: patch manifest and actual review test outputs.
- `docs/GIT_FIRST_STEPS.md`: beginner guide for the separate publication repository.

No aircraft parameter export, prebuilt firmware, flight logs, confidential client documents or credentials are included.

## Core capabilities

Logical motor-to-corner mapping; channel/polarity selection; distinct entry and exit tilt thresholds; proportional stick power with a bounded ramp; stop/reverse/drive/stop/restore sequencing; Commander/DShot arming ownership; switch-OFF qualification and startup normal-direction commands. These are code features, not claims that every path is hardware-validated.

**The feature deliberately allows selected motors to run while the aircraft is disarmed.** It defaults disabled and unmapped. ESC profile selection acknowledges compatibility; it does not detect it. Command counters and `synced=1` are not ESC acknowledgements.

## Version and provenance

Pinned PX4 base: `94cb2012792b2ae89f0b147cfee53ee31ae550be`.

Reported frozen source tag: `dragonfly-b8-trtl-tested-20261107T225810Z`.  
Reported snapshot commit: `ccfc0f53587c139b8d7afdecf374732665037612`.

These source identifiers came from the user's freeze-tool output. The patch's exact SHA-256 is recorded in `evidence/PATCH_MANIFEST.json`. A unified diff is not itself cryptographic proof of the reported commit identity.

## Read-only checks

From this repository folder, on a machine with Python 3 and g++:

```bash
python3 tests/run_host_tests.py
python3 tests/test_review_tools.py
python3 tools/verify_pinned_base.py ~/PX4-Autopilot
```

The last command needs the pinned commit's Git objects already present locally. It does not change the PX4 worktree, index, HEAD or tags. It does not compile or flash.

## Before a public experimental release

Read `docs/RELEASE_REVIEW.md` and `docs/LICENSING.md`. Preserve the frozen source artifact; make any cleanup in a separate reviewed commit. Confirm clean-base application and document the build/profile used. Finalize copyright/license notices. Keep the current source labelled experimental and hardware-specific evidence explicit.

The patch contains **no DJI OSD changes**. A reproducible O4/MSP OSD integration guide and board profile are a separate publication item, not something supplied by this core patch.
