from sanic import Sanic, response
from sanic.response import json, text

app = Sanic()

app.config.REQUEST_TIMEOUT = 600
app.config.RESPONSE_TIMEOUT = 600


# sanic-apline project's code
@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route('/post', methods=['POST'])
async def post_handler(request):
    # print("PRINT:", request.json)
    # obj = request.json
    # modelAssemblyService(obj)
    return text('New model is at this addreess: <a href=/.api/mas/model target=_blank>Click Here</a>')
    # return text('New model is at this addreess: <a href=http://130.216.216.219:8000/model target=_blank>Click Here</a>')


@app.route('/model')
async def handle_request(request):
    return await response.file('model.xml')


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=8000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)

