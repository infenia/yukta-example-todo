export const remaining = (todos) => todos.filter((todo) => !todo.done).length;

export const summary = (todos) =>
  todos.length === 0 ? "Nothing to do" : `${remaining(todos)} of ${todos.length} left`;
