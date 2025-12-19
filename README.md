# Trunk-Based Development Pattern Demo

This repository demonstrates the **Trunk-Based Development** strategy.

## Philosophy
Trunk-Based Development is a source-control branching model where developers collaborate on code in a single branch called "trunk" (or `main`), resisting any pressure to create other long-lived development branches.

## Key Concepts
- **Trunk (main)**: The single source of truth.
- **Short-lived branches**: Branches live for a few hours or days at most.
- **Feature Flags**: Used to toggle unfinished features in production so code can be merged frequently without breaking the build.

## How to Interact
1. **Pull Latest**: Always start with the latest code from `main`.
2. **Small Changes**: Make small, incremental changes.
3. **Feature Flags**: Wrap new features in flags (see `flags.json`) if they are not ready for users.
4. **Merge Often**: Merge back to `main` frequently (at least daily).
