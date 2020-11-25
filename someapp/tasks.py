from testlooptask.celery import app


@app.task(name='print_hello_world')
def print_hello_world():
    print('Hello world')
