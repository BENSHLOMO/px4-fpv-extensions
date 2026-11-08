# Licensing and attribution

## Repository license

The repository uses the **BSD 3-Clause License**. The top-level `LICENSE` contains the license from the exact pinned PX4 base:

```text
PX4-Autopilot 94cb2012792b2ae89f0b147cfee53ee31ae550be
```

Redistribution of modified PX4 source must preserve the required copyright notice, license conditions and disclaimer.

## Patched upstream files

The patch modifies existing PX4 files and adds extension headers. Preserve the upstream copyright and license notices in the complete source files; unchanged notice blocks may be absent from the unified diff.

## New extension files

Extension headers use BSD-3-Clause SPDX identifiers. The original tested patch is preserved by the `private-baseline-b8-trtl` tag. Subsequent comment and license-notice updates are recorded in [Source hygiene](SOURCE_HYGIENE.md), with their own patch and target-blob hashes.

## Attribution

The extension was developed at **BENSHLOMO | Advanced Systems**, led and hardware-tested by **Yisrael Ben-Shlomo**.

Development used AI assistance for code generation, debugging, documentation and review. Upstream PX4 code retains its existing authorship and licensing.

## Project and product names

PX4, MicoAir, AM32 and DJI names identify software and hardware used by the project. The extension is maintained separately from upstream PX4; these references do not imply endorsement by those projects or manufacturers.
