# Baseline source review

Initial review: 8 November 2026. Input: the original `dragonfly_turtle_core.patch` export preserved in the baseline history.

SHA-256: `2f4933719c71876fea964ea87c48cdb550f9c8f21d87fae6f8171fe2d1cbe913`  
Size: 73,391 bytes; 1,516 lines; 14 touched paths; 9 new files; 1,346 inserted lines and no deleted lines (Git numstat).

The current published patch has subsequent comment and SPDX updates. See [Source hygiene](SOURCE_HYGIENE.md) for its hash and validation record.

## Findings and disposition

| ID | Baseline finding | Disposition |
|---|---|---|
| P1 | DShot.cpp retained a Stage 2B1 comment saying motor output was compile-disabled, although the active B8 path can issue throttle. | Corrected in the comment/SPDX cleanup. The B8 controller is motor-enabled. |
| P2 | DShot.h retained earlier RecoveryTimer/Sequencer/Frame instances, parameter members and B1 diagnostic counters alongside the active `_trtl_core`. | Retained. Removal is a separate refactor requiring a target build and host tests. |
| P3 | Earlier helper thresholds differ from active B8 behavior, including angle, switch-OFF, wait and drive limits. | Documentation uses the active B8 controller. Legacy helper removal remains separate work. |
| P4 | Four new headers lacked SPDX markers: driver ArmingInterlock forwarding header, Angle, Motor and Rc. | BSD-3-Clause identifiers added in the source cleanup; upstream notices retained. |
| P5 | The original code-only diff contained no tests, README or installation guide. | The repository includes documentation and host tests against extracted patch headers. |
| P6 | The diff carried exact Git blob IDs but depended on a specific PX4 Commander, mixer and DShot interface revision. | Base commit pinned in the manifest; the supplied verifier checks application and target blobs in a temporary directory. |
| P7 | The core patch contains no board files, OSD changes or legacy probe module. | Aircraft/OSD configuration remains separate; a stock board build can differ from the development aircraft's build. |
| P8 | Defaults are disabled, with an unconfigured ESC profile and zero corner mappings. Power defaults 850/1500 retain Dragonfly tuning. | Installation requires explicit motor mapping, ESC verification and propulsion-specific tuning. |
| P9 | Transmitted command counters do not establish physical ESC direction or reset behavior. The exact AM32 version was not recorded. | Retained as a technical validation limit in the hardware matrix and operation guide. |

## Initial review checks

1. Read all 14 diff sections, including the active input, controller, mapping and interlock paths.
2. Verified all nine new-file payloads against their target Git blob hashes.
3. Verified 21 short-name parameter definitions, with no legacy `DF_TRTL_` or `DF_TURT_` names.
4. Ran five B8 host suites against headers extracted from the exact baseline patch, using `-Wall -Wextra -Werror` and undefined-behavior sanitizer.
5. Tested temporary patch application, repository index/HEAD/worktree preservation, and checksum/path rejection on a synthetic Git repository.
6. Reviewed repository content for aircraft backups, credentials and client material; none were found in that scoped inspection.

## Validation scope

The initial source review covered extracted headers and review tooling. Pinned-base patch application and blob checks were subsequently completed during source cleanup. The review did not perform a complete ARM/NuttX build, target scheduler test or hardware test.

Successful target-build logs and real-world recovery reports belong to the preserved Dragonfly development checkpoint. The comment-cleaned patch has not been separately flashed and hardware-tested. A clean-checkout target build with a documented board configuration remains to be recorded.

## Release scope

The release is an experimental source extension for the pinned PX4 revision. Hardware evidence covers the Dragonfly configuration. Additional platforms and an upstream PX4 port require their own review and validation.
