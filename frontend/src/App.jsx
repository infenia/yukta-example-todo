import { useEffect, useState } from "react";
import { summary } from "./todos.js";

const send = (path, method, body) =>
  fetch(`/api/todos${path}`, {
    method,
    headers: { "Content-Type": "application/json" },
    body: body && JSON.stringify(body),
  });

const load = (set) =>
  fetch("/api/todos")
    .then((response) => response.json())
    .then(set);

export default function App() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");

  useEffect(() => {
    load(setTodos);
  }, []);

  const act = (request) => request.then(() => load(setTodos));

  return (
    <main style={{ maxWidth: 420, margin: "3rem auto", fontFamily: "system-ui" }}>
      <h1>Todo</h1>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          act(send("", "POST", { title })).then(() => setTitle(""));
        }}
      >
        <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="What next?" />
        <button type="submit">Add</button>
      </form>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {todos.map((todo) => (
          <li key={todo.id}>
            <label style={{ textDecoration: todo.done ? "line-through" : "none" }}>
              <input
                type="checkbox"
                checked={todo.done}
                onChange={() => act(send(`/${todo.id}`, "PATCH"))}
              />{" "}
              {todo.title}
            </label>{" "}
            <button type="button" onClick={() => act(send(`/${todo.id}`, "DELETE"))}>
              x
            </button>
          </li>
        ))}
      </ul>
      <p>{summary(todos)}</p>
    </main>
  );
}
