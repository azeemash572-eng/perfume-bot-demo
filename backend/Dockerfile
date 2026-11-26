FROM node:22-slim
WORKDIR /app
COPY server.mjs catalog.json ./
ENV PORT=7860
EXPOSE 7860
# GEMINI_API_KEY is injected at runtime from the Space secret. It is never in this image or repo.
CMD ["node", "server.mjs"]
