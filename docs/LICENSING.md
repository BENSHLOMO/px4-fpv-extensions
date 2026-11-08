# Licensing review before public release

**Proposed project license: BSD-3-Clause, matching PX4's contribution policy.** This private starter does not declare missing provenance resolved.

Several new headers already use `SPDX-License-Identifier: BSD-3-Clause`. Four do not: the driver forwarding ArmingInterlock header and the Angle, Motor and Rc helpers. Add consistent notices in a separate reviewed cleanup, identifying actual copyright holders rather than inventing ownership. Preserve original notices in the patched upstream files. A unified diff normally omits most unchanged license headers, so their absence in a hunk is not proof that the full source lacks them.

The PX4 license reference included under LICENSES was retrieved from upstream main during this review. Retrieve the exact pinned-base LICENSE from the user's repository before public distribution, for example with the read-only command:

```bash
git -C ~/PX4-Autopilot show 94cb2012792b2ae89f0b147cfee53ee31ae550be:LICENSE
```

Do not represent this reference copy as independently verified against the pinned base. Finalize the top-level LICENSE and appropriate notices before changing the repository to Public. The unchanged snapshot remains traceable by its original hash.

AI assistance does not replace authorship/provenance review. Do not claim upstream endorsement or ownership of the pre-existing PX4 MSP OSD implementation.

References:
- https://raw.githubusercontent.com/PX4/PX4-Autopilot/main/LICENSE
- https://docs.px4.io/main/en/contribute/licenses
- https://docs.px4.io/main/en/contribute/ai_assistants
