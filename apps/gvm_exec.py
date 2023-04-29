import subprocess
import xml.etree.ElementTree as et

# 執行 docker compose; PIPE代表等待讀取/寫入指令
command = 'docker-compose -f C:/greenbone-community-container/docker-compose.yml -p greenbone-community-edition run --rm gvm-tools'
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

# 指令設定
gvm_default = "gvm-cli --gmp-username admin --gmp-password admin socket --pretty --xml "

# 輸入 gvm-cli 指令
while True:
    # 使用者輸入
    user_input = str(input("Enter gvm-cli command: "))
    
    # 查看process狀態
    print(process.poll())

    # 結束程式
    if user_input == "exit":
        process.stdin.close()
        process.wait()
        print("Exit")
        break
    
    # 將指令傳送給gvm-cli
    result = gvm_default + f"'{user_input}'\n"  # '\n'代表傳送
    process.stdin.write(result.encode())        # 使用write寫入; encode表示字串轉換成二進位
    process.stdin.flush()                       # 清除buffer，避免進入deadlock


    output = ''
    # 讀取回傳值
    while True:
        # 屬於file object，使用readline讀取; decode代表二進位轉換成字串
        line = process.stdout.readline().decode()

        line = line.replace('\n', '<br>')

        # repr印出所有資訊包括跳脫字元
        print(repr(line))

        # 印出回傳值
        output += line

        # 印出長長的字串
        print(output)

        # 此file object，沒有EOF，觀察XML的最後標籤，判斷break
        if line[0] == '<' and line[1] == '/':
            break

print('he',type(output))