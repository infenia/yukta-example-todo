import { expect, test } from "bun:test";
import { remaining, summary } from "./todos.js";

const todos = [
  { id: 1, title: "a", done: true },
  { id: 2, title: "b", done: false },
];

test("counts the todos that are not done", () => {
  expect(remaining(todos)).toBe(1);
});

test("summarises the list", () => {
  expect(summary([])).toBe("Nothing to do");
  expect(summary(todos)).toBe("1 of 2 left");
});
