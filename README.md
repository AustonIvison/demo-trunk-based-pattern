# Trunk-Based Development Pattern Demo

This repository demonstrates the **Trunk-Based Development** strategy.

## Philosophy & In-Depth Explanation
Trunk-Based Development is a source-control branching model where developers collaborate on code in a single branch called "trunk" (or `main`), resisting any pressure to create other long-lived development branches.

The goal is to avoid "merge hell" and long-lived feature branches that drift far from the main codebase. Developers commit small batches of code to `main` multiple times a day. To ensure the application remains stable even with unfinished features, **Feature Flags** (toggles) are used. This allows code to be deployed to production while keeping the new feature hidden from users until it is ready.

## Comparison with Other Patterns

| Pattern | Best For | Key Difference |
| :--- | :--- | :--- |
| [**Gitflow**](https://github.com/AustonIvison/demo-gitflow-pattern) | Scheduled releases, strict control. | Relies on long-lived branches which can lead to difficult merges if not managed carefully. |
| [**GitHub Flow**](https://github.com/AustonIvison/demo-github-flow-pattern) | Continuous deployment, PR-centric. | Still uses feature branches that might live for days. Trunk-based encourages merging hours or minutes after starting. |
| **Trunk-Based** (This Repo) | High-velocity teams, CI/CD. | Commits go directly to `main`. Feature Flags are essential. |

## Key Concepts
- **Trunk (main)**: The single source of truth.
- **Short-lived branches**: Branches live for a few hours or days at most.
- **Feature Flags**: Used to toggle unfinished features in production so code can be merged frequently without breaking the build.

## How to Interact
1. **Pull Latest**: Always start with the latest code from `main`.
2. **Small Changes**: Make small, incremental changes.
3. **Feature Flags**: Wrap new features in flags (see `flags.json`) if they are not ready for users.
4. **Merge Often**: Merge back to `main` frequently (at least daily).
