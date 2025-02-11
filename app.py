from flask import Flask, render_template_string, request

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Um Jogo para Você!</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        button { font-size: 18px; padding: 10px; margin: 10px; cursor: pointer; }
    </style>
    <script>
        function fugir() {
            var btnNao = document.getElementById("nao");
            btnNao.style.position = "absolute";
            btnNao.style.left = (Math.random() * window.innerWidth) + "px";
            btnNao.style.top = (Math.random() * window.innerHeight) + "px";
        }
    </script>
</head>
<body>
    <h1>Olá, Camila! Tenho algo para te perguntar 😊</h1>
    <p>Você aceitaria sair comigo um dia desses?</p>
    <form action="/" method="post">
        <button type="submit" name="resposta" value="sim">Sim 😍</button>
        <button type="button" id="nao" onmouseover="fugir()">Não 🤨</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return "<h1>YES! 😍 Eu sabia que programação funcionava! Vou te chamar então! 💙</h1>"
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)