# fastapi + elm
..hot reloading.

Use `docker-compose up` and go to http://localhost:8081. Then, when you do a change in `src/Main.elm`,
the elm app is rebuilt and the server is restarted.

For production, the same server can be used (maybe without `--reload`, can be done by env as in squad).
