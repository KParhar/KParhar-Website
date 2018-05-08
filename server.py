from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'coderk2001@gmail.com'
app.config['MAIL_PASSWORD'] = 'Kush2001'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/email', methods = ['POST'])
def email():
	senderName = request.form['contact-name']
	senderEmail = request.form['contact-email']
	senderSubject = request.form['contact-subject']
	senderMsg = request.form['contact-msg']
	
	msg = Message(senderSubject, sender = 'coderk2001@gmail.com', recipients = ['coderk2001@gmail.com'])
	msg.body = ""
	msg.body += "Sender Name:" + senderName + "\n"
	msg.body += "Sender Email:" + senderEmail + "\n"
	msg.body += "\nSender Message:\n" + senderMsg
	mail.send(msg)
	return redirect("http://localhost:5000")
	
if __name__ == '__main__':
    app.run(debug=True)
