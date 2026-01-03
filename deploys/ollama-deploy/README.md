# Ollama Server Docker Compose

This folder includes a `docker-compose.yml` that runs the `ollama` model server and a one-shot `init-model` job that pulls models into a persistent volume.

Quick start
1. Start the stack (models will be persisted in the `ollama-models` volume):

   docker compose up --build

2. The server will be available on port `11434`. The `init-model` job will run after the server is healthy and pull the models configured in the compose file.

GPU notes
- The compose contains examples for NVIDIA and AMD GPU setups. Use the approach appropriate for your host (NVIDIA Container Toolkit or ROCm). If Compose ignores `deploy` settings, consider running the container with `--gpus all`.

Troubleshooting
- Check `docker compose logs ollama` for server startup issues.
- To manually pull models after the server is running:

   docker compose run --rm init-model
