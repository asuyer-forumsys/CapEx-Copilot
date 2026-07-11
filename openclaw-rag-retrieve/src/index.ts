import { Type } from "typebox";
import { defineToolPlugin } from "openclaw/plugin-sdk/tool-plugin";

import { spawn } from "node:child_process";
import path from "node:path";

const PROJECT_ROOT = "/Users/andrewsuyer/Documents/CapEx-Copilot"

const PYTHON =
  process.platform === "win32"
    ? path.join(PROJECT_ROOT, ".venv", "Scripts", "python.exe")
    : path.join(PROJECT_ROOT, ".venv", "bin", "python");


export default defineToolPlugin({
  id: "openclaw-rag-retrieve",
  name: "RAG retrieve",
  description: "Add RAG retrieve tools to OpenClaw.",
  tools: (tool) => [
    tool({
      name: "rag_retrieve",
      description: "Search the knowledge base for chunks relevant to a query. Use this before answering questions that depend on indexed documents.",
      parameters: Type.Object({
        query: Type.String({ description: "The search query" }),
        top_k: Type.Integer({ description: "Number of chunks to return", default: 3 }),
      }),
      execute: async ({ query, top_k }) => {
        return new Promise((resolve, reject) => { 
          // Fill these in however your CLI works.
          const args = [
            "-m",
            "capex_copilot.retriever",
            query,
            top_k.toString(),
          ];

          const child = spawn(PYTHON, args, {
            cwd: PROJECT_ROOT,
          });

          let stdout = "";
          let stderr = "";

          child.stdout.on("data", (data) => {
            stdout += data.toString();
          });

          child.stderr.on("data", (data) => {
            stderr += data.toString();
          });

          child.on("error", reject);

          child.on("close", (code) => {
            if (code !== 0) {
              reject(
                new Error(
                  `Retriever exited with code ${code}\n${stderr}`
                )
              );
              return;
            }

            resolve(JSON.parse(stdout));
          });
        });
      },
    }),
  ],
});
