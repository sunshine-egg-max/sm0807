from flask import Flask # flask是工具箱(model模組), Flask是工具(class類別)
from flask import abort, redirect, url_for, render_template

app = Flask(__name__) # 製作出一個由Flask類別生成的物件 (object)

@app.route("/")
@app.route("/<string:username>") 
def say_hello_world(username=""): # function
    return render_template("hello.html", name = username)

@app.route("/tell_me_a_joke") # 裝飾器  # / -> 根目錄  # 根目錄要做啥事
def tell_me_a_joke():
    return "<p>ha ha ha ha</p>"

@app.route("/eat/<string:what_fruit>")
def eat_fruit(what_fruit):
    return redirect(url_for('say_fruit_is_gone', fruit = what_fruit))

@app.route("/eat_<string:fruit>")
def say_fruit_is_gone(fruit):
    return "<p>" + fruit + " is gone.</p>"

# 如果我直接執行這個檔案，那__name__就等於__main__
#if __name__ == '__main__':
    # 或在command_line下: flask --app flask_linebot.py --debug run
    #app.run(debug=True)

#@app.route('/login')
#ef login():
    #abort(401)
    #this_is_never_executed()
