from flask import Flask, render_template, request, url_for

from flask_mail import Mail, Message
import os
app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "ak475885@gmail.com"
app.config['MAIL_PASSWORD'] = "idayzwkxttcfaztv"
# app.config['DEFAULT_MAIL_SENDER'] = 'ak475885@gmail.com'
mail = Mail(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        user_message = request.form.get('message')
        workOnProject = False
        if request.form.get('workOnProject'):
            workOnProject = True
        title = f'{name}--webClient--workOnProject--{workOnProject}'
        message = Message(title, sender=email , recipients=['hk264603@gmail.com'])
        message.body = user_message
        mail.send(message)

    return render_template('contact.html')


@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/skill")
def skill():
    return render_template('skill.html')


if __name__ == '__main__':
    app.run(debug=True)

