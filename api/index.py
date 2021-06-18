from sanic import Sanic
from sanic.response import json
app = Sanic()


@app.route('/api/yanick')
async def index(request, path=""):
    return json({'god': 'yanick', 'hello': path})
