# Contributing

Contributions to the turtle-recovery extension and its documentation are welcome. The patch targets a pinned PX4 revision; proposed ports should identify their target revision and build configuration.

## Changes and reports

Submit focused, reviewable changes with a description of the problem, resulting behavior and validation. Keep extension changes separate from aircraft-specific configuration and firmware binaries.

For a bug report, include the PX4 revision, board target, ESC model and firmware, relevant parameters, steps to reproduce, and available logs. For a hardware compatibility result, use the checklist in [Hardware validation matrix](docs/HARDWARE_MATRIX.md).

## Validation

Run the host suites:

```bash
python3 tests/run_host_tests.py
python3 tests/test_review_tools.py
```

Identify host tests, target builds and hardware tests separately in the result. Changes to executable firmware require a target build and appropriate bench or hardware validation. Preserve baseline tags and document functional changes in separate commits.

## Licensing and development

Preserve upstream copyright and license notices. Use the repository's BSD-3-Clause licensing for new extension files.

Development uses AI assistance. Contributors remain responsible for understanding, reviewing and validating submitted changes. An upstream PX4 submission must follow PX4's current contribution policy, including its AI-assistance and sign-off requirements.

References:

- [PX4 contribution policy](https://github.com/PX4/PX4-Autopilot/blob/main/CONTRIBUTING.md)
- [PX4 AI assistance guidance](https://docs.px4.io/main/en/contribute/ai_assistants)
