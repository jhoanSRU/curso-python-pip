import store
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
app = FastAPI()

#se agrega un recuzo que se llama decorador 
@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/Contact', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>First time </title>
        </head>
        <body>
            <h1> First time using FastAPI and web server</h1>
            <p> this is just a test </p>
        </body>
    </html>
    """
def run():
    store.get_categories()

if __name__ == '__main__':
    run()