# Backend proxy (Gemini)

`server.mjs` is a dependency-free Node proxy: it holds the system prompt + sample catalog, adds a budget hint, rate-limits per IP, restricts CORS to the GitHub Pages origin and calls Gemini with the key from the **server environment** (`GEMINI_API_KEY`).
The key is never in this repo or in the page. Deploy with `deploy_hf.py` (Hugging Face Docker Space, key stored as a Space secret).
After deploy, set `smart/config.json` to `{ "api": "https://<user>-ms-store-smart-bot.hf.space" }`.
