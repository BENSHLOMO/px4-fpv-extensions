# Hardware validation matrix

The matrix records hardware results. Software test coverage is listed separately below.

| Platform | Flight controller | ESC / firmware | Frame | Result | Evidence boundary |
|---|---|---|---|---|---|
| Dragonfly development aircraft | MicoAir H743 V2 | AM32; exact firmware version not yet recorded | guarded 2.5-inch Quad-X-like | **Successful recovery (operator report)** | Development reference. Exact ESC version and motor/propeller/battery details remain to be recorded for a reproducible hardware profile. |

## Dragonfly observed configuration

- PX4 base: `94cb2012792b2ae89f0b147cfee53ee31ae550be`
- Recovery channel: CH9 in the tested transmitter setup
- Logical-to-physical mapping observed in status:
  - Front left: logical Motor 3 → physical DShot output 2
  - Front right: logical Motor 1 → physical DShot output 3
  - Rear left: logical Motor 2 → physical DShot output 4
  - Rear right: logical Motor 4 → physical DShot output 1
- Documented tuning during the successful TRTL checkpoint: entry 85°, exit 35°, start command 850, peak command 1500, ramp 250 ms, drive 1000 ms.

These values describe the tested Dragonfly aircraft. Configure and validate propulsion and recovery settings for each additional build.

## Software-tested scope

Host tests exercise conventional four-corner motor mapping, controller transitions, cancellation/fault cases, RC validation, repeated recovery/release cycles, and the shared arming/recovery interlock.

Physical compatibility of additional ESCs, flight controllers, propulsion systems, frames and PX4 revisions requires separate hardware and target-build results.

## Configurations outside the current scope

- plus-frame control logic;
- coaxial, hex, octo or VTOL layouts;
- tilted/tilting motors;
- PWM, OneShot, DroneCAN or mixed motor-output backends;
- PX4 reversible/3D throttle configurations;
- unverified ESC firmwares that merely support ordinary DShot;
- arbitrary PX4 releases or current `main` without a separate port and build/test cycle.

## Adding another hardware result

Record:

1. exact FC and board target;
2. exact PX4 commit/release;
3. exact ESC model and firmware version;
4. motor, propeller, battery and frame;
5. logical motor mapping and physical outputs;
6. parameter profile;
7. normal-direction verification;
8. recovery, cancellation, restore and return-to-flight result;
9. log/video reference where appropriate.

Add a separate matrix entry for each hardware configuration with recorded validation.
