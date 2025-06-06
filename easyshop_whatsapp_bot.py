# EASYSHOP - Módulo 1: Integración WhatsApp con Python usando Twilio

from flask import Flask, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    # Lógica básica para responder
    if "hola" in incoming_msg:
        msg.body("Hola, soy EASYSHOP. Puedes registrar ventas o pedir tu balance. Ejemplo: 'Vendí 3 arroz a 2000'")
    elif "balance" in incoming_msg:
        msg.body("Tus ventas hoy fueron $30.000. Gastos: $10.000. Ganancia: $20.000")
    elif "vendi" in incoming_msg:
        msg.body("Venta registrada correctamente ✅")
    else:
        msg.body("Lo siento, no entendí tu mensaje. Puedes decir 'balance' o 'vendí arroz a 2000'")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
