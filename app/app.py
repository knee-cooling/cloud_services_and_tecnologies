from flask import Flask, render_template

from decorator import (
    Hostname,
    CPU,
    Memory
)

from visitor import (
    TestVisitorHome,
    TestVisitorCommercial
)

app = Flask(__name__)


def html(text: str) -> str:
    return text.replace("\n", "<br/>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")


@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/visitor')
def visitor():

    home = TestVisitorHome()
    home.setProduct()
    visitor1 = f"Всего к оплате (для домашнего использования): {home.GetCost()}"
    print(visitor1)

    comm = TestVisitorCommercial()
    comm.setProduct()
    visitor2 = f"Всего к оплате (для коммерческого использования): {comm.GetCost()}"
    print(visitor2)

    return render_template(
        'visitor.html',
        visitor1=html(visitor1),
        visitor2=html(visitor2)
    )


@app.route('/decorator')
def decorator():
    hostname: Hostname = Hostname()
    cpu: CPU = CPU(hostname)
    memory: Memory = Memory(cpu)

    return render_template(
        'decorator.html',
        decorator=html(memory.show())
    )


if __name__ == "__main__":
    app.run('127.0.0.1', debug=True)
