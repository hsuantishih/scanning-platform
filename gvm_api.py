import subprocess

# 執行 docker compose
command = 'docker-compose -f C:/greenbone-community-container/docker-compose.yml -p greenbone-community-edition run --rm gvm-tools'
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

# 測試 gvm-cli 指令
gvm_cli_command = 'gvm-cli --version'
process.stdin.write(gvm_cli_command.encode())
process.stdin.flush()

# 等待程式完成，讀取回傳值
output, error = process.communicate()
print(output.decode())
