from sanic import Sanic, response
from sanic.response import json, text

from run_model import run_model

app = Sanic(name="opencor_run_model")

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

@app.route("/test_request_args")
async def test_request_args(request):
    return json({
        "parsed": True,
        "url": request.url,
        "query_string": request.query_string,
        "args": request.args,
        "raw_args": request.raw_args,
        "query_args": request.query_args,
    })

@app.route('/run_model')
async def run_handler(request):
    print(request.args)
    stim_mode = int(request.args['stim_mode'][0])
    stim_level = float(request.args['stim_level'][0])
    print("stim_mode = " + str(stim_mode) + "; stim_level = " + str(stim_level))
    result = run_model(stim_mode, stim_level)
    return json(result)

@app.route('/model')
async def handle_request(request):
    return await response.file('model.xml')


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=8000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4, debug=True)

