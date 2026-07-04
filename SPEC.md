# Postgram: build spec

A high-level spec for the app we build together in the session. It says WHAT to build, not HOW.
We build it live with Claude Code, and we layer in the Claude memory setup as we go
(see `docs/memory-plan.md`).

## What we are building

Postgram: a small photo-sharing app. A feed of posts, each with an image and a caption. People can
like a post and comment on it. Think of the smallest useful slice of Instagram.

## Scope for the session (v1)

- List the feed of posts (newest first, paginated).
- Create a post (image URL + caption).
- Like and unlike a post (a second like from the same person is a no-op).
- Add a comment to a post, and list a post's comments.

Out of scope for now: accounts and login, image uploads (we use an image URL), following, and search.

## Stack

- **Backend:** Python, FastAPI, SQLModel, SQLite. A REST API under `/api`.
- **Frontend:** React, Vite, TypeScript, Tailwind, TanStack Query for data fetching.

## Data model

- **Post:** `id` (uuid), `image_url`, `caption`, `created_at` (UTC).
- **Comment:** `id`, `post_id`, `author`, `body`, `created_at`.
- **Like:** `id`, `post_id`, `user`. A `(post_id, user)` pair is unique.

## API sketch

| Method | Path | Does |
|---|---|---|
| GET | `/api/posts` | List posts, newest first. Query: `limit` (default 20, max 100). |
| POST | `/api/posts` | Create a post from `image_url` + `caption`. |
| GET | `/api/posts/{id}` | Get one post. |
| DELETE | `/api/posts/{id}` | Delete a post. |
| GET | `/api/posts/{id}/comments` | List a post's comments (paginated). |
| POST | `/api/posts/{id}/comments` | Add a comment. |
| GET | `/api/posts/{id}/likes` | Get the like count. |
| POST | `/api/posts/{id}/likes` | Like the post (idempotent). |
| DELETE | `/api/posts/{id}/likes` | Unlike the post. |

## Rules the finished app should follow

These become our `CLAUDE.md` files and rules during the build:

- Timestamps are UTC and ISO-8601. Ids are UUID strings.
- API errors use the shape `{"detail": "..."}`. List endpoints paginate.
- Backend endpoints are `async`, use Pydantic v2 schemas, and never return ORM models directly.
- Frontend uses function components, no `any`, Tailwind for styling, and renders a loading and an
  error state for every data fetch.

## Definition of done

A running backend at `http://localhost:8000/docs`, a running frontend that shows the feed and lets
you post, like, and comment, a passing test suite, and a memory setup that matches the plan in
`docs/memory-plan.md`.
