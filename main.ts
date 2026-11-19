// Entry point for the gta6-meme-x-01 bounty.
//
// The meme itself lives on X: the house reads the post directly from the
// public post named in POST.json. This program has one job — deliver that
// POST.json into the grader's output directory, byte for byte, so every
// run completes identically.
//
// Run it the way the grader does:
//   MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
//
// Standard library only, no network.

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

function scriptDir() {
  return path.dirname(fileURLToPath(import.meta.url));
}

function outputDir() {
  return process.env.MAKEFUN_OUTPUT_DIR || "/output";
}

function findPostFile() {
  const places = [process.env.MAKEFUN_BOT_DIR, scriptDir(), process.cwd()];
  for (const dir of places) {
    if (!dir) continue;
    const candidate = path.join(dir, "POST.json");
    if (existsSync(candidate)) return candidate;
  }
  throw new Error("POST.json not found: expected it next to main.ts");
}

const source = findPostFile();
const destDir = outputDir();
mkdirSync(destDir, { recursive: true });
const dest = path.join(destDir, "POST.json");
copyFileSync(source, dest);
console.log(`POST.json delivered to ${dest}`);
