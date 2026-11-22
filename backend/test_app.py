import json
import threading
import urllib.error
import urllib.request

import pytest

import app


@pytest.fixture
def base():
    app.todos.clear()
    server = app.serve(0)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{server.server_port}/api/todos"
    server.shutdown()


def call(method, url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(request) as response:
            raw = response.read()
            return response.status, json.loads(raw) if raw else None
    except urllib.error.HTTPError as error:
        return error.code, None


def test_add_toggle_and_delete(base):
    status, todo = call("POST", base, {"title": "write an example"})
    assert status == 201 and todo["done"] is False

    assert call("PATCH", f"{base}/{todo['id']}")[1]["done"] is True
    assert call("GET", base)[1] == [{**todo, "done": True}]

    assert call("DELETE", f"{base}/{todo['id']}")[0] == 204
    assert call("GET", base)[1] == []


def test_a_todo_needs_a_title(base):
    assert call("POST", base, {"title": "  "})[0] == 400
