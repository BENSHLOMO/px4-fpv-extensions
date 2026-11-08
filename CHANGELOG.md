# Changelog

## v0.1.0-experimental.1

**Developed by Yisrael Ben-Shlomo at BENSHLOMO | Advanced Systems**

### Initial release

- Experimental PX4 Quad-X turtle/crash-flip recovery
- Temporary DShot motor reversal for compatible ESCs
- Configurable logical-to-physical motor mapping
- 21 native TRTL_* parameters in QGroundControl
- Configurable RC channel, switch polarity and recovery angles
- Proportional stick control and adjustable power
- Repeatable recovery and direction-restoration sequencing
- Commander/DShot arming interlock
- Automated host tests through GitHub Actions

### Validation

- Successfully built and demonstrated on Project Dragonfly
- MicoAir H743 V2 running custom PX4 v1.16.1
- AM32 ESC firmware family
- Host testing and pinned-base patch verification passed

### Compatibility

Experimental source patch for the pinned PX4 v1.16.1 revision.
Build for the target board and validate its motor mapping, geometry and
ESC direction-command behavior. Hardware validation covers Dragonfly;
additional configurations require independent testing.

Development used AI assistance. Yisrael Ben-Shlomo led the requirements,
hardware integration and real-world testing.
