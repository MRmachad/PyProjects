from flask import Flask, request
from smtpConnect import SmtpConnect

app = Flask(__name__)


@app.route('/envio', methods=['POST'])
def webhook():

    data = request.get_json(force=True)
    v_key = sorted(list(data))
    print(v_key)

    obj_smtp = SmtpConnect()
    obj_smtp.Envia_email(para_email = "leonardo.silva@tsea.com.br", assunto = "Alarme", msg_texto = ("Alerta de temperatura alta: " + data["AD_esp"] + " | " + data["AD_DS"]))
    obj_smtp.Serv_quit()

    print("Entrou")

    return "OK", 200

if __name__ == "__main__":
    app.run("0.0.0.0", 3040, debug=True)
