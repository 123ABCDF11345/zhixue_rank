import zhixuewang
#student = zhixuewang.login(input('UserID: '),input('Password: '))
#print(student.get_clazz()) #学生信息
#print(student.get_exams()) #返回所有的考试
from flask import Flask, escape, url_for ,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    try:
        student = zhixuewang.login(request.args.get('accountId', ''),request.args.get('passwd', ''))
    except zhixuewang.exceptions.UserOrPassError:
        return '<html><meta http-equiv="refresh" content="3;URL=/">账号或密码异常<br>3秒后将返回主页</html>'
    return str(student.get_clazz())

if __name__ == '__main__':
    app.run(debug=True)