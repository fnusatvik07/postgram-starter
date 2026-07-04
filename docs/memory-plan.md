# Memory plan

The order we add the Claude Code memory files as we build. Each step is small. Copy the matching file
from the `postgram-complete` repo, or write it live.

| Step | Add this | Where | Scope | What it does |
|---|---|---|---|---|
| 1 | `CLAUDE.md` | repo root | project | Run `/init` to draft it, then add the error shape, the UTC rule, and "never push to main". |
| 2 | `backend/CLAUDE.md` | `backend/` | project (nested) | The API team's rules. Loads only when Claude reads a backend file. |
| 3 | `frontend/CLAUDE.md` | `frontend/` | project (nested) | The UI team's rules. Loads only when Claude reads a frontend file. |
| 4 | `CLAUDE.local.md` | repo root | local | Your machine-only notes (port, seed command). Add it to `.gitignore`. |
| 5 | `.claude/rules/api-design.md` | `.claude/rules/` | project (path-scoped) | Applies to `backend/app/api/**`. Then add an endpoint and watch it paginate on its own. |
| 6 | (nothing to add) | | auto memory | Build a feature. Claude hits a gotcha, fixes it, and writes memory. Open `/memory` to read it. |
| 7 | (nothing to add) | | payoff | A backend person edits a frontend file. `frontend/CLAUDE.md` + `react.md` load automatically. |

## The one rule for deciding scope

Ask "who is this true for?"

- True for the repo, it is **project** scope (`CLAUDE.md`, `.claude/rules/`).
- True for you on every project, it is **user** scope (`~/.claude/CLAUDE.md`).
- True for your machine only, it is **local** scope (`CLAUDE.local.md`).
- Something Claude worked out, let **auto memory** keep it.

## Useful commands

- `/init` writes a first `CLAUDE.md` by reading the codebase.
- `/memory` lists every memory file loaded this session and opens the auto-memory folder.
- If Claude is not following an instruction, run `/memory` first. If the file is not in the list,
  Claude cannot see it.
