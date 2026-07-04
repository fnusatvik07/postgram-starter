# Postgram (starter): build this live

This is the starting point for the workshop. It has a spec and a plan, and no code yet. We build the
app together from `SPEC.md` and set up Claude Code's memory as we go, following `docs/memory-plan.md`.

The finished answer key is the **`postgram-complete`** repo. If you get stuck, copy the file we are
discussing from there.

## Start here

1. Read **`docs/where-we-are-heading.md`** to see the destination.
2. Read **`SPEC.md`** for what we are building.
3. Open this folder with Claude Code and run `/init` to create the first `CLAUDE.md`.
4. Follow **`docs/memory-plan.md`** as we build: add each memory file at the step where it helps.

## What is in this repo

```
postgram-starter/
├── README.md                     you are here
├── SPEC.md                       the high-level build spec (what to build)
├── docs/
│   ├── where-we-are-heading.md   the goal and why the memory setup matters
│   └── memory-plan.md            the order we add CLAUDE.md files and rules
└── .gitignore
```

There is no `backend/` or `frontend/` yet. That is the point. We create them from the spec, and we
add memory files as the project grows.

## Push it to GitHub

After the session, this becomes your own project:

```bash
git add -A
git commit -m "postgram: workshop build"
gh repo create postgram --public --source=. --push
# or, without the gh cli:
# git remote add origin https://github.com/<you>/postgram.git
# git push -u origin main
```

Remember: `CLAUDE.md` and the `.claude/rules/` files get committed and shared. `CLAUDE.local.md` and
`.claude/settings.local.json` stay out of git (already in `.gitignore`).
