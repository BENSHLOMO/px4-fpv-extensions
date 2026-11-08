# Release status

## Current release

The project distributes an experimental source extension for PX4 v1.16.1, with configurable turtle recovery for conventional Quad-X layouts using verified compatible temporary-direction DShot ESC commands.

Hardware validation currently covers the Dragonfly development aircraft. Ports to other PX4 revisions and additional hardware profiles require separate builds and validation.

## Source history

The original exported hardware-tested checkpoint is preserved by the tag:

```text
private-baseline-b8-trtl
```

The published patch includes a subsequent comment and SPDX cleanup. This cleanup changes no executable statements and has passed host tests and pinned-base patch checks. It has not been flashed and hardware-tested as a separate firmware build. See [Source hygiene](SOURCE_HYGIENE.md) for both patch hashes and the scope of the change.

## Validation record

- Successful ARM target build for the Dragonfly MicoAir H743 V2 configuration.
- Real-world recovery success reported by the Dragonfly operator.
- Host tests covering controller state logic, motor mapping, RC validation and Commander/DShot ownership.
- Temporary application of the cleaned patch to the pinned base, with base and target Git blob verification.
- Preserved PX4 BSD-3-Clause license and source notices.

See [Validation](VALIDATION.md) and [Hardware validation matrix](HARDWARE_MATRIX.md) for details.

## Compatibility and operational limits

- The exact AM32 firmware version and target remain to be recorded.
- Additional flight controllers, ESC versions and propulsion configurations require hardware testing.
- ESC command counters record transmitted sequences; the implementation has no physical direction acknowledgement.
- Arming coordination is implemented in software and is separate from an independent hardware watchdog.
- The release is maintained separately from upstream PX4 and has experimental status.

## Further work

- Document additional hardware profiles and fault-case results.
- Record a clean-checkout target build with its complete board configuration.
- Publish the DJI O4 / PX4 MSP OSD integration profile separately.
- Prepare an upstream technical discussion and port against the requested PX4 revision.
