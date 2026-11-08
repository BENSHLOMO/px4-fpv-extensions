# Validation record

## Host tests

See `evidence/HOST_TEST_RESULTS.txt` and `evidence/REVIEW_TOOL_TESTS.txt`.

The test runner extracts the new-file headers from the exported patch and verifies their Git blob hashes before compiling the B8 host suites.

Recorded results:

- RC zero-secondary-timestamp regression checks;
- 25 controller scenarios across six callback intervals;
- 44 phase and fault cases;
- 1,000 recovery/release cycles;
- 285,120 motor-corner/output-slot combinations;
- interlock guard lifetimes and 200,000 concurrent reservation attempts.

The hardware-independent headers were compiled with g++ C++14, warnings-as-errors and UBSan. Callback intervals are simulated calls, and concurrency checks use host threads. These suites test the extracted headers; they do not compile the complete DShot, Commander or mixer implementation or measure target RTOS scheduling.

Two Python tests exercise temporary patch application, target hashes, preservation of the test repository's index/HEAD/worktree, checksum rejection and unsafe-path rejection.

## Target build and hardware results

The development record includes successful ARM build logs and operator-reported real-world recovery on Dragonfly. These results apply to the preserved hardware-tested checkpoint and its aircraft configuration.

The later comment/SPDX cleanup passed the host suites and temporary pinned-base application with target-blob verification. It has not been built and hardware-tested as a separate firmware. See [Source hygiene](SOURCE_HYGIENE.md).

## Reproducible target builds

A separate clean-checkout board build with a documented board configuration remains to be recorded. The core patch excludes the full Dragonfly board/OSD profile.

The read-only pinned-base check is available for a local PX4 repository:

```bash
python3 tools/verify_pinned_base.py /path/to/PX4-Autopilot
```

This verifies patch application and source blobs. Firmware installation on the flight controller is verified separately.

## Recording another result

Record source and firmware hashes, board target, ESC firmware version, battery/propeller configuration, the case tested, result, and a log or video reference. Use the [Hardware validation matrix](HARDWARE_MATRIX.md) checklist for a new platform.
