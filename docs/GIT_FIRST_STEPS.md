# Working with this repository

Git records local source history. GitHub hosts the shared repository, review discussions and releases. Keep this extension repository separate from the PX4 checkout used to build aircraft firmware.

## Clone and create a branch

```bash
git clone https://github.com/BENSHLOMO/px4-fpv-extensions.git
cd px4-fpv-extensions
git switch -c docs/my-update
```

Use a short branch name that describes the change.

## Author identity

Set your name and email in this checkout before committing. Repository-local settings apply only here. GitHub provides a no-reply email option for contributors who prefer it.

```bash
git config user.name "Your Name"
git config user.email "your-github-noreply-address"
```

Replace both example values with your own identity.

## Review and commit

```bash
git status --short
git diff
```

Stage only the intended files with `git add`, then create a local snapshot with `git commit`. Update the relevant checksum entries in `SHA256SUMS` when changing listed files. Run the checks in [Contributing](../CONTRIBUTING.md) before submitting the branch.

Push to a repository where you have write access, or use a fork and open a pull request. Review the staged diff before pushing. Keep aircraft-specific parameter exports, firmware backups and credentials outside this repository.

## Preserving release history

Existing baseline and release tags identify reproducible source checkpoints. Make fixes in new commits and record functional changes and validation in the pull request. The tested aircraft's firmware and settings are separate from the extension repository.

References:

- [GitHub repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
- [Contributing](../CONTRIBUTING.md)
