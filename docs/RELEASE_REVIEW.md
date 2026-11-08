# Release review of the exported working patch

Reviewed 8 November 2026. Input: `dragonfly_turtle_core.patch`.

SHA-256: `2f4933719c71876fea964ea87c48cdb550f9c8f21d87fae6f8171fe2d1cbe913`  
Size: 73,391 bytes; 1,516 lines; 14 touched paths; 9 new files; 1,346 inserted lines and no deleted lines (Git numstat).

## Verdict

**Suitable as the unchanged baseline in a private review repository. Not yet presented as a polished upstream pull request or universal release.** Nothing in this review modifies the uploaded firmware patch or the user's frozen backups. The working hardware result remains valid as the operator's observation.

## Findings

| ID | Finding in the supplied patch | Action before presenting a polished release |
|---|---|---|
| P1 | DShot.cpp contains a stale comment saying motor output is compile-disabled (patch lines 76-81), although the active B8 path can issue throttle. | Correct explanatory comments in a separate cleanup commit. Do not describe the current firmware as simulation-only. |
| P2 | DShot.h retains old RecoveryTimer/Sequencer/Frame instances, parameter members and B1 diagnostic counters alongside the active `_trtl_core` (patch lines 358-429). | Remove proven-unused members/includes/helpers in a separate refactor, with a build and the same host tests. Not removed from this snapshot. |
| P3 | Legacy helper policies disagree with active B8: old angle helper minimum 85 degrees vs active minimum 60; legacy RC `off()` uses `<0.3`, active B8 requires `<-0.3`. Old motor helper has different waits and drive limits. | Make the active controller authoritative in docs; remove or clearly isolate unused helpers. The active B8 path does not use these old helpers to decide its OFF threshold. |
| P4 | Four new headers have no SPDX marker: driver ArmingInterlock forwarding header, Angle, Motor and Rc. Others declare BSD-3-Clause. The patch is not a complete license/notice bundle. | Finalize consistent notices and retain exact upstream notices before public distribution. See LICENSING.md. |
| P5 | This code-only diff includes no tests, README or install instructions. | Supplied review scaffold adds tests/docs without altering patch bytes. Host tests are not a substitute for target/hardware evidence. |
| P6 | The patch names exact base/target Git blob IDs but does not itself specify the base commit. It depends on older PX4 Commander, mixer and DShot interfaces. | Keep the manifest and pinned-base check. Do not advertise compatibility with arbitrary PX4 releases. |
| P7 | No board files, OSD driver changes or legacy probe module are included. | Keep the turtle-core patch separate from the tested full-aircraft configuration. A clean stock build may differ in size/features from the user's custom build. |
| P8 | Defaults are disabled, unconfigured ESC profile and zero corner mappings. Power defaults 850/1500 retain Dragonfly tuning. | Make opt-in setup explicit; do not tell other pilots to copy Dragonfly motor order or assume these are universal propulsion values. |
| P9 | Real command acceptance, direction restoration and ESC reset behavior are not proved by counters. Exact AM32 firmware version was not supplied here. | Retain this boundary in README and hardware matrix; record the exact version before claiming support for it. |

P1-P5 are mainly source hygiene, reproducibility and release packaging. They do not justify replacing the already-working aircraft firmware during this step. No new functional failure was reproduced by the five host suites run for this review. This is not a proof that no functional bugs exist.

## Checks actually performed here

1. Read all 14 diff sections and active input, controller, mapping and interlock code.
2. Verified the new-file payloads against all nine target Git blob hashes.
3. Verified 21 short-name parameter definitions with no old `DF_TRTL_`/`DF_TURT_` names in the uploaded patch.
4. Re-ran five existing B8 host suites against **headers extracted from this exact uploaded patch**, with `-Wall -Wextra -Werror` and undefined-behavior sanitizer.
5. Tested the added read-only base verifier on a synthetic Git repository; checked original index bytes/HEAD/worktree preservation and checksum/path refusal.
6. Reviewed paths and content for obvious private material. No aircraft parameter dump, firmware image, private key, access token, password, home-directory path or client material was found. This is a scoped content review, not a formal secret-scan certification.

## Not independently performed here

A complete clean PX4 checkout could not be retrieved in this environment. No complete clean-base application, GCC ARM/NuttX build, board scheduler test or hardware test was run here. `tools/verify_pinned_base.py` is provided to perform the apply/blob checks using the user's existing local Git objects, without changing that checkout.

The earlier full firmware build, real recovery and frozen commit identity are reported evidence from the conversation. The host tests do not authenticate that a particular firmware is installed on the flight controller.

## Release recommendation

Archive this exact snapshot privately, complete the publication cleanup in separate commits, and publish as an **experimental, source-level extension for a pinned PX4 version**. An upstream PR is a subsequent activity. No first-ever, upstream-accepted, production-ready, universal, independently watchdog-protected or direction-acknowledged claim is supported.
