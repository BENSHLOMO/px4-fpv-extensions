# Notice and provenance

This repository contains an experimental source extension for a pinned PX4-Autopilot revision.

## PX4 provenance

Pinned base:

```text
94cb2012792b2ae89f0b147cfee53ee31ae550be
```

The repository's top-level `LICENSE` contains the BSD 3-Clause license from that PX4 revision. Preserve existing notices in patched PX4 source files.

## BENSHLOMO extension

The turtle-recovery extension was developed at **BENSHLOMO | Advanced Systems** for the Dragonfly aircraft project. **Yisrael Ben-Shlomo** led the project, systems integration and hardware validation.

Development used AI assistance for code generation, debugging, documentation and review. Yisrael Ben-Shlomo performed hardware integration, configuration, bench testing, real-aircraft testing and release decisions.

## Source and validation records

The `private-baseline-b8-trtl` tag preserves the original exported patch from the hardware-tested checkpoint. Subsequent comment and SPDX updates are documented in [Source hygiene](docs/SOURCE_HYGIENE.md). Hardware results apply to the Dragonfly development configuration; the current hardware matrix records the scope of that validation.

The repository distributes source, tests and documentation. Aircraft-specific configuration and firmware are managed separately.

## Project and product names

PX4, MicoAir, AM32 and DJI identify upstream software and hardware used during development. Their names do not imply endorsement of BENSHLOMO or this extension.
