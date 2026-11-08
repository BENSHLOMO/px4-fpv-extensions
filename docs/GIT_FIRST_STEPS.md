# First Git/GitHub steps for this project

Git is already installed on the Lubuntu machine used for development. It records local source history. GitHub will host a separate publication repository; it is not where we need to move the full private PX4 checkout or aircraft backup.

## Create an empty private repository

On GitHub, create **px4-fpv-extensions**, visibility **Private**. Do not auto-add a README, license or gitignore when importing this prepared folder. These files should have one deliberate starting point.

Use a new directory for this review package. Do not run `git remote add` or publish commands inside the working `PX4-Autopilot` checkout.

## Local identity

Inside the new publication directory, set `user.name` and `user.email` only for that repository. Use your chosen public identity and the GitHub-provided no-reply email when desired. Do not use the development placeholder `Dragonfly Local` as if it were your public identity.

## The first commands, once the remote URL and identity are known

```bash
git init -b main
git status
```

Review files before staging. `git add` selects content for a snapshot; `git commit` creates the snapshot locally; `git push` uploads it. `git status` is the check before and after each step. A remote URL is not an authentication token. Never paste private keys or access tokens into a public README.

At this stage, send the private repository URL to continue setup. This package neither creates a repository nor publishes anything.

## Keeping the working aircraft intact

The historical full backup and exact source tag remain the rollback point. The public project starts with the immutable exported patch. Any cleanup belongs in later commits with its own checks, not silent edits to the frozen patch.

Before making the repository public, inspect its history as well as the current files. Never add the full aircraft parameter dump or the frozen ZIP. `.gitignore` is a precaution, not a substitute for reviewing staged files.

References:
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
