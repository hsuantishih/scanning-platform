from flask import Flask, render_template, request, redirect, url_for, session
import subprocess, xml.etree.ElementTree as ET

app = Flask(__name__)

# SECRET_KEY
app.config['SECRET_KEY'] = 'JOIJPOJOPHIJOoijpjoij'.encode()

# 執行docker compose; PIPE代表等待讀取/寫入指令
command = 'docker-compose -f C:/greenbone-community-container/docker-compose.yml -p greenbone-community-edition run --rm gvm-tools'
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

# 寫入指令/讀取回傳值
def send_command(command):
    config = "gvm-cli --gmp-username admin --gmp-password admin socket --pretty --xml "
    command = config + f"'{command}'\n"
    process.stdin.write(command.encode())   # 使用write寫入; encode表示字串轉換成二進位
    process.stdin.flush()

    # 取得結果
    response = ''
    # 讀取回傳值
    while True:
        # 屬於file object，使用readline讀取; decode代表二進位轉換成字串
        line = process.stdout.readline().decode()

        # 儲存回傳值
        response += line

        # 此file object，沒有EOF，觀察XML的最後標籤，判斷break
        if line[0] == '<' and line[1] == '/':
            break
        elif line[-2] == '>' and line[-3] == '/':
            break

    return response

@app.route('/', methods=['GET', 'POST'])
def get_version():
    if request.method == 'GET':
        version = '<get_version/>'
        response = send_command(version)
        return render_template("version.html", response=response)
    
    elif request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        hosts = request.form['hosts']
        ports_min = request.form['ports_min']
        ports_max = request.form['ports_max']
        port_range = f'T:{str(ports_min)}-{str(ports_max)}'
        target = "<create_target><name>{}</name><comment>{}</comment><hosts>{}</hosts><port_range>{}</port_range></create_target>".format(name, comment, hosts, port_range)
        session['target'] = target
        return redirect(url_for("create_target"))


@app.route('/create_target', methods=['GET', 'POST'])
def create_target():
    if request.method == 'GET':
        target = session['target']
        session.pop('target', None)
        session['target_response'] = send_command(target)
        root = ET.fromstring(session['target_response'])
        session['target_id'] = root.get('id')
        return render_template("create_target.html", target_response=session['target_response'], id=session['target_id'])
    elif request.method == 'POST':
        name = request.form['name']
        target_id = request.form['target_id']
        config_id = request.form['config_id']
        task = "<create_task><name>{}</name><target id=\"{}\"></target><config id=\"{}\"></config></create_task>".format(name, target_id, config_id)
        session['task'] = task
        return redirect(url_for("create_task"))

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    if request.method == 'GET':
        task = session['task']
        session.pop('task', None)
        session['task_response'] = send_command(task)
        root = ET.fromstring(session['task_response'])
        session['id'] = root.get('id')
        return render_template('create_task.html', task_response=session['task_response'], id=session['id'])
    elif request.method == 'POST':
        task_id = request.form['task_id']
        start_task = "<start_task task_id=\"{}\"/>".format(task_id)
        session['start_task'] = start_task
        return redirect(url_for("start_task"))
    
@app.route('/start_task', methods=['GET', 'POST'])
def start_task():
    start_task = session['start_task']
    session.pop('start_task', None)
    session['start_task_response'] = send_command(start_task)
    return render_template('start_task.html', response=session['start_task_response'])

# get_tasks

# get_reports

if __name__ == '__main__':
    app.run()