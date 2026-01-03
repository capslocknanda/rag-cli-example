# Qdrant (quadrant-db) Docker Compose

This folder runs a Qdrant vector database and includes a one-shot `restore` helper that will run any `restore.sh` found in the `backups/` directory.

Files
- `docker-compose.yml` - starts `qdrant` and a `restore` job which will execute `/backups/restore.sh` if present.
- `restore.sh` - example helper (in repo root) that tries to import NDJSON/JSON files into Qdrant collections via the HTTP API. Adjust it to your export format or replace it with a custom script inside `backups/`.

Usage
1. Put your backup files and optionally a `restore.sh` into `./backups`.
2. Start Qdrant and run restore job:

   docker compose up -d qdrant
   docker compose run --rm restore

   Or start both (the restore job will exit after running):

   docker compose up --build

Notes
- The provided `restore.sh` is a simple example and uses a heuristic to find a `collection` in the first line of an input file. Modify it to match your data export format.
- To re-run restore, simply run `docker compose run --rm restore` again.
