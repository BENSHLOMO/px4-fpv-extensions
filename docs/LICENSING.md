# Licensing and attribution

## Repository license

The repository uses the **BSD 3-Clause License**. The top-level `LICENSE` file was retrieved from the exact pinned PX4 base used by this extension:

```text
PX4-Autopilot 94cb2012792b2ae89f0b147cfee53ee31ae550be
```

Redistribution of modified PX4 source must preserve the required copyright notice, license conditions, and disclaimer.

## Patched upstream files

The patch modifies existing PX4 files as well as adding extension headers. Existing upstream copyright/license notices in the full source files must be retained. The unified diff may not show unchanged notice blocks.

## New extension files

New source files should use consistent BSD-3-Clause SPDX identifiers where appropriate. The exact tested baseline patch is retained unchanged for traceability; source-hygiene changes should be made in separate commits and retested rather than silently rewriting the hardware-tested checkpoint.

## Attribution

The extension was developed under **BENSHLOMO | Advanced Systems**, led and hardware-tested by **Yisrael Ben-Shlomo**.

Development used AI assistance for portions of code generation, debugging, documentation, and review. AI assistance does not imply authorship of upstream PX4 code and does not replace source-license obligations.

## No endorsement

PX4, MicoAir, AM32 and DJI names are used descriptively. This repository is not an upstream PX4 release and does not imply endorsement by those projects or manufacturers.
