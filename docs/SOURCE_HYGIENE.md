# Source hygiene: release/v0.1-cleanup

This is a **comment and license-notice-only** change to the exported PX4 patch.
It does not change executable statements, parameters, ESC commands, radio logic,
or the tested aircraft firmware. The frozen hardware-tested source is preserved
by the Git tag `private-baseline-b8-trtl` and the separate private B8 backup.

## Changes

- Added `SPDX-License-Identifier: BSD-3-Clause` to four newly introduced headers
  that previously lacked a file-level identifier.
- Corrected the old Stage 2B1 statement that recovery motor output was
  compile-disabled. The active B8 path is motor-enabled.
- Recomputed the Git target blob IDs and patch SHA-256 from the **pinned PX4
  base** in a temporary directory. No modifications to that PX4 checkout.
- Regenerated `evidence/PATCH_MANIFEST.json` and the root `SHA256SUMS` so the
  publication repository reflects its current content.

The older diagnostic structures and helper headers remain in the patch.
Removing them is a true refactor, **not part of this comment-only change**.
That refactor requires a clean target PX4 build and tests before merging.

Original preserved patch SHA-256: `2f4933719c71876fea964ea87c48cdb550f9c8f21d87fae6f8171fe2d1cbe913`.
Comment-cleaned patch SHA-256: `9d8f3086b242762c951e8aace4c5b99cece3b5920256bfa344dbd139ec1725a8`.

## Evidence and limits

Host tests and a clean temporary patch apply confirm source-format consistency,
but do not substitute for a complete PX4/NuttX/ARM build or physical flight tests.
Do not label the cleaned patch as a separately hardware-tested firmware build.
The recorded real-world recovery results refer to the preserved baseline.

## Attribution

Retain the upstream PX4 BSD-3-Clause LICENSE and notices. The added SPDX
identifiers document the intended source license and are not an assertion
of upstream authorship or endorsement.
