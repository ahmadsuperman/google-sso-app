from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

LOGIN_FORM = """
<html>
    <body>
        <form action="" method="post">
            <p><input type=text name=username placeholder=username></p>
            <p><input type=password name=password placeholder=password></p>
            <p><input type=submit value=Login></p>
        </form>
    </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Placeholder for authentication logic
        return redirect(url_for('home'))
    return render_template_string(LOGIN_FORM)

@app.route('/home')
def home():
    return 'Home Page - Login Successful'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
