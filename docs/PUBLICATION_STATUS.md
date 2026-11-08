# Publication status

## Preserved tested baseline

The private repository baseline is tagged:

```text
private-baseline-b8-trtl
```

The underlying working aircraft checkpoint was separately frozen before publication work. The baseline patch remains unchanged in this documentation cleanup.

## Current release posture

Appropriate description:

> Experimental configurable PX4 v1.16.1 turtle recovery for supported conventional Quad-X layouts with verified compatible temporary-direction DShot ESC behavior on the Dragonfly development aircraft.

Do **not** describe it as:

- universal;
- production-ready;
- validated on most quads;
- compatible with every AM32/BLHeli/Bluejay/DShot ESC;
- upstream PX4 functionality;
- independently watchdog-protected;
- capable of confirming physical ESC direction from software counters alone.

## Evidence available

- successful target build on the Dragonfly MicoAir H743 V2 development target;
- real-world operator-reported recovery success on Dragonfly;
- exported working patch;
- host tests for state logic, mapping, RC validation and arming/recovery ownership;
- exact PX4 BSD-3-Clause license from the pinned base.

## Before changing repository visibility to Public

1. Review the README and installation instructions.
2. Record the exact AM32 firmware version used on Dragonfly if available.
3. Keep the repository's tested-baseline tag.
4. Ensure no private parameter export, firmware backup, private keys, tokens or client material are present.
5. Decide whether to publish the tested patch unchanged first or make a separate source-hygiene patch and retest it.
6. Add the BENSHLOMO website URL and project media only after those destinations are ready.

## Planned follow-on content

- DJI O4 / PX4 MSP OSD integration guide, clearly identified as integration of existing PX4 support;
- website engineering case study;
- LinkedIn launch post;
- optional upstream discussion after the experimental release is reproducible.
