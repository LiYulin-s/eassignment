from sanic import Sanic
from sqlalchemy

app = Sanic("BackEnd")

@app.route("/api")
async def api():
    return "hello world."