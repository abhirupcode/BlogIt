import os
import threading

from flask import *

blog = Flask(__name__)


@blog.route("/")
def home():
    return render_template("home.html")


@blog.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            emailOpen = str(email) + ".txt"
            passOpen = str(email) + ".info.txt"
            email1 = open(emailOpen, 'r+')
            email2Con = email1.read()
            email1.close()
            password2 = open(passOpen, 'r+')
            password2Con = password2.read()
            password2.close()
        except:
            return render_template("login.html")

        if password == email2Con:
            return redirect(url_for("dashboard", username=password2Con))
        else:
            pass

    return render_template("login.html")


@blog.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        usr = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        usrFile = str(email) + ".txt"
        usrNameFile = str(email) + ".info.txt"
        isExist = os.path.exists("D:\\Coding\\Blog\\" + usrFile)
        isExist1 = os.path.exists("D:\\Coding\\Blog\\" + usrNameFile)
        if isExist == False and isExist1 == False:
            userPass = open(str(usrFile), 'x')
            userPass.write(str(password))
            userPass.close()

            userName = open(str(usrNameFile), 'x')
            userName.write(str(usr))
            userName.close()

            return redirect(url_for("login"))
        else:
            pass

        return render_template("signup.html")

    else:

        return render_template("signup.html")


@blog.route("/dash/", methods=['GET', 'POST'])
def dashboard():
    try:
        username = request.args['username']
        if request.method == "POST":
            email = request.form.get('email')
            oldpassword = request.form.get('oldpassword')
            newpassword = request.form.get('password')

            repass1Open = str(email) + ".txt"
            path = "D:\\Coding\\Blog\\" + repass1Open
            isExist2 = os.path.exists(path)

            if isExist2 == True:
                repass2Open = open(path, 'r+')
                repassword = repass2Open.read()
                repass2Open.close()
                if repassword == oldpassword:
                    os.remove(path)
                    repass2Open = open(path, 'x')
                    repass2Open.write(str(newpassword))
                    repass2Open.close()
                else:
                    pass

            else:
                pass

        return render_template("dash.html", name=username)
    except:
        return redirect(url_for("home"))


@blog.route("/dash/delete/", methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        email1 = request.form.get('EMAIL')
        print(email1)
        usrFile = str(email1) + ".txt"
        usrNameFile = str(email1) + ".info.txt"
        isExist = os.path.exists("D:\\Coding\\Blog\\" + usrFile)
        isExist1 = os.path.exists("D:\\Coding\\Blog\\" + usrNameFile)

        if isExist and isExist1:
            os.remove(usrFile)
            os.remove(usrNameFile)
            return redirect(url_for('home'))

    return render_template("delete.html")


if __name__ == "__main__":
    blog.run()
