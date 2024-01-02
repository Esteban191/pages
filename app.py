
from flask import Flask, render_template

app = Flask(__name__, static_folder='templates', static_url_path='/templates')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

"""    

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__, static_folder='templates', static_url_path='/templates')

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'aealzate91@gmail.com'  # Replace with your email server
app.config['MAIL_PORT'] = 587  # Replace with your email server's port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'aealzate91@gmail.com'  # Replace with your email address
app.config['MAIL_PASSWORD'] = '1017191214ae'  # Replace with your email password

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a message object
        msg = Message(subject='New Contact Form Submission',
                      sender=email,
                      recipients=['aealzate91@gmail.com'])  # Replace with your email address

        # Customize the email body
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Send the email
        mail.send(msg)

        return render_template('index.html', success=True)

    return render_template('index.html', success=False)


if __name__ == '__main__':
    app.run(debug=True)

"""