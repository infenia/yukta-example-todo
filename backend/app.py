"""A tiny todo API on the standard library: no framework, todos kept in memory."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

todos = []
next_id = 1


class Handler(BaseHTTPRequestHandler):
    def reply(self, code, body=None):
        data = json.dumps(body).encode() if body is not None else b""
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def find(self):
        todo_id = self.path.rsplit("/", 1)[-1]
        return next((t for t in todos if str(t["id"]) == todo_id), None)

    def do_GET(self):
        if self.path == "/api/todos":
            self.reply(200, todos)
        else:
            self.reply(404, {"error": "not found"})

    def do_POST(self):
        global next_id
        size = int(self.headers.get("Content-Length", 0))
        title = str(json.loads(self.rfile.read(size) or b"{}").get("title", "")).strip()
        if self.path != "/api/todos" or not title:
            return self.reply(400, {"error": "title is required"})
        todo = {"id": next_id, "title": title, "done": False}
        next_id += 1
        todos.append(todo)
        self.reply(201, todo)

    def do_PATCH(self):
        todo = self.find()
        if todo is None:
            return self.reply(404, {"error": "not found"})
        todo["done"] = not todo["done"]
        self.reply(200, todo)

    def do_DELETE(self):
        todo = self.find()
        if todo is None:
            return self.reply(404, {"error": "not found"})
        todos.remove(todo)
        self.reply(204)

    def log_message(self, format, *args):  # noqa: A002 - signature set by the base class
        print(f"{self.command} {self.path} -> {args[1]}", flush=True)


def serve(port):
    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"backend listening on http://127.0.0.1:{port}", flush=True)
    serve(port).serve_forever()
