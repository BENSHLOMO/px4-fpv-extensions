# DJI O4 / MSP OSD integration

Dragonfly uses DJI O4 with PX4's existing MSP OSD implementation. This is a separate aircraft integration from the turtle-recovery extension.

The turtle-core patch contains no OSD driver changes, board definitions, serial-port configuration or wiring guide. The full Dragonfly OSD setup is therefore outside the patch's installation scope.

A reproducible OSD integration profile is planned separately. It will document the board build flags, wiring, serial-port assignments and parameters used on the test aircraft, with attribution to the existing PX4 MSP OSD implementation.
