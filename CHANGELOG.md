# Changelog

## v0.1.0 Experimental

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

### Limitations

Experimental source release only. Other flight controllers,
ESC implementations and Quad-X configurations require
independent testing. No universal prebuilt firmware is supplied.

Software development involved substantial AI assistance.
Project direction, hardware integration and real-world testing
were led by Yisrael Ben-Shlomo.
