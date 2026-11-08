# DJI O4 / MSP OSD publication scope

The supplied turtle-core patch modifies no OSD driver, board definition, serial-port configuration or wiring guide. It cannot by itself reproduce the full Dragonfly aircraft firmware, including the reported DJI O4/MSP OSD setup.

Publish that as a separately documented integration profile using the existing PX4 MSP OSD implementation. Do not credit this turtle patch with introducing upstream DJI OSD support. Pin the board build flags, wiring and parameters from actual evidence before providing a reproducible guide. No such details are invented in this review package.

The website case study can describe both engineering activities, while the code repository clearly separates the turtle extension from the aircraft/OSD integration work.
