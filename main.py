from quart import Quart, redirect, render_template

app = Quart(__name__)

@app.route('/')
async def redir():
    return redirect('/loading')

@app.route('/loading')
async def load():
    return await render_template('loading.html')

@app.route('/index')
async def index():
    return await render_template('index.html')

app.run()