from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<center><h1>Te amo morin e to morrendo de saudades! ♥</h1></center>"

if __name__ == '__main__':
    app.run()