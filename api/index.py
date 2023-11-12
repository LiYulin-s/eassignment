from sanic import Sanic

app = Sanic("BackEnd")

@app.route("/api")
async def api():
    return "hello world."