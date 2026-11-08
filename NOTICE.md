# Notice and provenance

This repository contains an experimental source-level extension derived from and intended to patch a pinned PX4-Autopilot revision.

## PX4 provenance

Pinned base:

```text
94cb2012792b2ae89f0b147cfee53ee31ae550be
```

The repository's top-level `LICENSE` is the BSD 3-Clause license text retrieved from that exact pinned PX4 base. Existing notices in patched PX4 source files must be preserved.

PX4 and the names of its contributors are referenced descriptively and do not imply endorsement of BENSHLOMO or this extension.

## BENSHLOMO extension

The turtle-recovery extension was developed as part of the personal Dragonfly FPV/UAV development project at **BENSHLOMO | Advanced Systems**, led and hardware-tested by **Yisrael Ben-Shlomo**.

Development used AI assistance for portions of code generation, debugging, documentation, and review. Hardware integration, configuration, iterative bench testing, real-aircraft testing, and release decisions were performed by Yisrael Ben-Shlomo.

## Tested baseline

The private repository preserves the exact exported working patch as a traceable baseline. Documentation cleanup does not imply that every supported-looking hardware combination has been physically validated.

No aircraft parameter export, prebuilt firmware, SSH private key, access token, password, confidential client material, or full private aircraft backup is intended to be published in this repository.

References to MicoAir, AM32 and DJI describe hardware used during development and do not imply endorsement.
