from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="/static/"), name="static")

@app.get("/", response_class=HTMLResponse)
async def elmer():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
            <script src="/static/Main.js"></script>
        </head>
        <body>
            <main></main>
              <script>
                var app = Elm.Main.init({
                    node: document.querySelector('main')
                      });
            </script>
        </body>
    </html>
    """
