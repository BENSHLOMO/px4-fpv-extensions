# Validation record

## Independently executed in this review

See `evidence/HOST_TEST_RESULTS.txt` and `evidence/REVIEW_TOOL_TESTS.txt`.

The C++ tests are retained from the supplied prior B8 test package. The runner was added for this review so they compile against new-file contents extracted and hash-checked from **the uploaded patch**, rather than a reconstructed replacement controller.

Host suite results: RC zero-secondary-timestamp regression; 25 controller scenarios across six callback intervals; 44 phase/fault cases; 1,000 recovery/release cycles; 285,120 corner/slot mapping combinations; interlock guard lifetimes and 200,000 concurrent reservation attempts. The hardware-independent headers were compiled using g++ C++14 with warnings-as-errors and UBSan.

These callback intervals are simulated calls, not measured target scheduling rates. The interlock test uses host threads, not the target RTOS. The runner does not compile the complete modified DShot.cpp, Commander.cpp or mixer, and does not reproduce the full PX4 build.

Two additional Python packaging tests exercised temporary patch application/target hashes, preservation of the original test repository index/HEAD/worktree, patch checksum rejection and unsafe-path rejection.

## Existing hardware/build evidence

The user supplied successful ARM build logs and explicitly reported real-world recovery working on Dragonfly. Those results are retained as operator evidence and are not re-described as reviewer-performed tests.

## Pending release reproducibility

Run the supplied read-only pinned-base verifier using the existing local PX4 repository. A separate clean-checkout board build, with a documented board configuration, remains a release-reproducibility step. The full-aircraft board/OSD profile is not in this core patch.

## Evidence capture template

Record exact source/firmware hashes, board target, ESC firmware version, battery/propeller configuration, case tested, result, and a brief log or video reference when available. Keep private locations and aircraft calibration files out of the public repository.
