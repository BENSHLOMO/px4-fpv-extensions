# Installation on the pinned PX4 base

## Scope

The patch is currently prepared for PX4-Autopilot commit:

```text
94cb2012792b2ae89f0b147cfee53ee31ae550be
```

This is a source patch for the pinned revision. Other PX4 revisions require a separate port and build validation.

## 1. Obtain a clean PX4 checkout

Example:

```bash
git clone https://github.com/PX4/PX4-Autopilot.git
cd PX4-Autopilot
git checkout 94cb2012792b2ae89f0b147cfee53ee31ae550be
```

Install the build dependencies required by that PX4 revision using PX4's own documentation.

## 2. Verify the patch before applying it

From this repository:

```bash
python3 tools/verify_pinned_base.py /path/to/PX4-Autopilot
```

Then, from the PX4 checkout:

```bash
git apply --check /path/to/px4-fpv-extensions/patches/dragonfly-b8-trtl.patch
```

This step verifies patch applicability; step 4 builds the target firmware.

## 3. Apply the patch

```bash
git apply /path/to/px4-fpv-extensions/patches/dragonfly-b8-trtl.patch
```

Review the resulting diff before building:

```bash
git diff --stat
git diff -- src/drivers/dshot src/lib/dragonfly_turtle src/modules/commander
```

## 4. Build for your own controller

Use the PX4 board target appropriate to the flight controller. The Dragonfly development aircraft used:

```bash
make micoair_h743-v2_default
```

Select the matching board target for each additional controller. Board-specific OSD configuration and aircraft parameters are configured separately from the core patch.

## 5. Configure before enabling

The extension defaults disabled/unconfigured. Read `PARAMETERS.md`, `COMPATIBILITY.md`, and `OPERATION.md` before setting `TRTL_EN=1`.

At minimum, validate:

- actual logical motor-to-corner mapping;
- all four motors are served by the expected DShot instance;
- normal motor directions before recovery;
- exact ESC firmware support for temporary commands 21/20;
- selected RC channel and polarity;
- entry/exit angles;
- recovery power/timing for the actual propulsion system;
- cancellation, restoration and return-to-normal-arming behavior.

Do initial motor/direction testing with propellers removed.

## 6. Tune for the propulsion system

Dragonfly's documented mapping and 850/1500 command values describe the tested aircraft. Select and validate values for the actual motor, propeller, battery, guard geometry and ESC firmware on each build.
