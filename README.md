# yukta-example-todo

A deliberately tiny todo app (Python backend, React frontend) that the [Yukta](https://github.com/infenia/yukta) examples
`18-todo-run` and `19-todo-ci` check out and run. It is useful on its own as something small to point a workflow at.

| Part | What | Tools |
|---|---|---|
| `backend/` | JSON API on the standard library, todos kept in memory, port 8000 | [uv](https://docs.astral.sh/uv/), ruff, pytest |
| `frontend/` | React (Vite) page, port 5173, proxies `/api` to the backend | [bun](https://bun.sh), Biome, `bun test` |

## Run it

```bash
# terminal 1
cd backend && uv run --no-dev app.py
# terminal 2
cd frontend && bun install && bun run dev      # then open http://127.0.0.1:5173
```

## Check it

```bash
cd backend  && uv run ruff check . && uv run ruff format --check . && uv run pytest -q
cd frontend && bun install && bun run lint && bun run format:check && bun run test
```

Apache-2.0.
