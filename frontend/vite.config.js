import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react()],
  // the browser talks to this server only; /api goes on to the Python backend
  server: { proxy: { "/api": process.env.BACKEND_URL ?? "http://127.0.0.1:8000" } },
});
