import assert from "node:assert/strict";
import { test } from "node:test";
import { remaining, summary } from "./todos.js";

const todos = [
  { id: 1, title: "a", done: true },
  { id: 2, title: "b", done: false },
];

test("counts the todos that are not done", () => {
  assert.equal(remaining(todos), 1);
});

test("summarises the list", () => {
  assert.equal(summary([]), "Nothing to do");
  assert.equal(summary(todos), "1 of 2 left");
});
