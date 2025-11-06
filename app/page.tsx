"use client";

import TodoForm from "@/app/components/TodoForms";
import TodoItem from "@/app/components/TodoItem";
import { useStore } from "@/app/store";
import { useEffect } from "react";

const Home: React.FC = () => {
  const todos = useStore((state) => state.todos);
  const fetchTodos = useStore((state) => state.fetchTodos);

  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div className="container mx-auto max-w-md p-4">
      <TodoForm />
      <h1 className="text-2x1 font-bold mb4"> Todo List</h1>
      {todos.length === 0 ? (
        <p className="text-center">No Todos Found</p>
      ) : (
        todos.map((todo) => <TodoItem key={todo.id} todo={todo} />)
      )}
    </div>
  );
};

export default Home;
