# TRTL parameter reference

Reference for the patch's `module.yaml` parameter definitions. The table lists source defaults; aircraft-specific tuning is configured separately. All 21 values are int32.

| Name | Default | Bounds | Unit | Purpose |
|---|---:|---|---|---|
| `TRTL_EN` | 0 | 0..1 |  | Enable experimental Quad-X turtle recovery |
| `TRTL_ESC` | 0 | 0..1 |  | Verified temporary-direction ESC profile |
| `TRTL_CH` | 9 | 1..18 |  | Turtle receiver channel |
| `TRTL_POL` | 1 | -1..1 |  | Turtle switch polarity |
| `TRTL_ANGLE` | 120 | 60..175 | deg | Minimum tilt to START recovery |
| `TRTL_EXIT` | 35 | 5..80 | deg | Tilt at which recovery STOPS |
| `TRTL_MIN` | 850 | 1..1999 |  | Starting recovery motor command |
| `TRTL_MAX` | 1500 | 1..1999 |  | Maximum recovery motor command |
| `TRTL_RAMP` | 250 | 0..1500 | ms | Recovery upward ramp time |
| `TRTL_TIME` | 1000 | 100..3000 | ms | Maximum DRIVE phase duration |
| `TRTL_PRE` | 800 | 100..5000 | ms | Stop time before reverse commands |
| `TRTL_POST` | 1000 | 200..5000 | ms | Stop time before restore commands |
| `TRTL_SETTLE` | 200 | 100..1000 | ms | Stop time after reversal commands |
| `TRTL_COOL` | 300 | 100..2000 | ms | Cooldown after restore commands |
| `TRTL_DB` | 20 | 5..60 | % | Recovery roll/pitch deadband |
| `TRTL_PWR` | 1 | 0..1 |  | Use proportional stick power |
| `TRTL_HOLD` | 400 | 100..1000 | ms | Deliberate activation hold |
| `TRTL_FL` | 0 | 0..4 |  | Front-left logical motor |
| `TRTL_FR` | 0 | 0..4 |  | Front-right logical motor |
| `TRTL_RL` | 0 | 0..4 |  | Rear-left logical motor |
| `TRTL_RR` | 0 | 0..4 |  | Rear-right logical motor |

## Original long descriptions

### `TRTL_EN`

Enable only after mapping and verifying the ESC profile. Commander rejects arming until startup restoration is sent and the switch has been released. This feature intentionally permits motor output while disarmed.

### `TRTL_ESC`

0 unconfigured. Set 1 only after verifying your exact ESC firmware supports temporary relative DShot 21 reverse and 20 normal, including repeated commands while stopped. No ESC settings are saved. This is an acknowledgement by the operator, not automatic ESC detection.

### `TRTL_CH`

One-based calibrated receiver channel. It must not share roll, pitch, yaw, throttle, arm, kill, flight mode, parameter tuning or other critical functions. Generic AUX sharing is allowed. RC source only.

### `TRTL_POL`

Use 1 for high=ON or -1 for low=ON. Zero is invalid. After polarity, ON is above 0.7 and OFF is below -0.3; center stops recovery but does not reset the switch handshake.

### `TRTL_ANGLE`

Degrees away from upright. Entry needs a fresh OFF to ON request followed by a hold. 85 allows a nominal 90-degree side-on start. Must be at least EXIT plus 10 degrees. This is not proof that the aircraft is on the ground.

### `TRTL_EXIT`

Separate threshold from ANGLE. Once started, a flip can continue through the entry angle until it reaches this near-upright tilt or another stop condition. Must be at least 10 degrees below ANGLE.

### `TRTL_MIN`

PX4 non-stop DShot command units, not measured RPM, thrust or percent power. Must not exceed MAX. Defaults retain the Dragonfly development profile and are not universal recommendations.

### `TRTL_MAX`

PX4 DShot command units. Full stick reaches this target in proportional mode. Verify reverse thrust, motor start, current and heating for the actual propulsion system.

### `TRTL_RAMP`

Ramps the output cap from MIN to MAX. Reset when the selected motor set changes or the stick is centered. Must not exceed TIME. Zero disables the ramp.

### `TRTL_TIME`

Starts when the motor-driving phase begins, not during reverse or settling. Motor stopping and restore phases have a separate derived transaction budget.

### `TRTL_PRE`

Time spent transmitting stop before temporary reversal. Choose from measured coast-down on the actual motor and propeller; this is not RPM confirmation.

### `TRTL_POST`

Time spent transmitting stop before normal-direction restore. Increase for slower-stopping propulsion. A fixed delay does not prove the motor stopped.

### `TRTL_SETTLE`

Stopped interval after a reverse command train, before drive.

### `TRTL_COOL`

Stopped interval after restore, before requiring switch OFF for release.

### `TRTL_DB`

Percent of normalized roll or pitch. Diagonal deflection selects a single corner; axis-only input selects a pair.

### `TRTL_PWR`

1 maps stick magnitude above deadband to MIN..MAX with the ramp cap. 0 retains a timed ramp to MAX regardless of stick magnitude.

### `TRTL_HOLD`

Continuous eligibility after a fresh OFF-to-ON request while disarmed. Switch OFF for at least 300 ms is required between attempts and after RC loss.

### `TRTL_FL`

PX4 logical Motor 1..4 at the front-left corner, looking down with the quad upright and nose forward. Not a connector number. All four must be distinct; 0 is unconfigured. Allocation positions and axes must agree.

### `TRTL_FR`

PX4 logical Motor 1..4 at the front-right corner, looking down with the quad upright and nose forward. Not a connector number. All four must be distinct; 0 is unconfigured. Allocation positions and axes must agree.

### `TRTL_RL`

PX4 logical Motor 1..4 at the rear-left corner, looking down with the quad upright and nose forward. Not a connector number. All four must be distinct; 0 is unconfigured. Allocation positions and axes must agree.

### `TRTL_RR`

PX4 logical Motor 1..4 at the rear-right corner, looking down with the quad upright and nose forward. Not a connector number. All four must be distinct; 0 is unconfigured. Allocation positions and axes must agree.

## Cross-validation and active settings

The active Core also rejects MIN > MAX, RAMP > TIME and EXIT + 10 > ANGLE. A valid mapping contains four distinct supported motor assignments. POL=0 is invalid even though it lies inside the metadata min/max interval. Configuration is accepted only under the allowed idle/disarmed/OFF conditions; it is not guaranteed to apply during a recovery.
