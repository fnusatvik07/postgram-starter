# Where we are heading

Read this at the start so everyone can see the destination before we write a line of code.

## By the end of the session you will have

1. **A working app.** Postgram running locally: a photo feed you can post to, like, and comment on.
   A FastAPI backend and a React frontend, with tests that pass.

2. **A complete memory setup.** The reason we are here. Claude Code will know this project the way a
   teammate who has worked on it for months would, because we give it the right files in the right
   folders:

   - A project `CLAUDE.md` at the root that everyone shares.
   - A `backend/CLAUDE.md` and a `frontend/CLAUDE.md` so each area carries its own rules.
   - Path-scoped rules in `.claude/rules/` that only load when Claude touches matching files.
   - A personal `CLAUDE.local.md` for the things true only on your machine.
   - Auto memory that Claude writes itself as we work.

## Why this matters

Without it, every session starts from zero. You re-explain the build command, the conventions, and
the gotchas again and again. A new person cannot touch the backend without asking the backend author.

With it, the context lives in the repo. Claude follows the conventions on the first try, a frontend
person can safely edit the backend, and Claude gets a little better every session because it keeps
notes for itself. A few files in the right folders is the whole trick.

## How we get there

We build the app from `SPEC.md` and add the memory files in the order laid out in
`docs/memory-plan.md`. The finished answer key is the `postgram-complete` repo: if you get stuck,
copy the file we are discussing from there.
