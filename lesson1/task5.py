import subprocess

args_ya = ['ping', 'yandex.ru']
args_yt = ['ping', 'youtube.com']
subproc_ping_ya = subprocess.Popen(args_ya, stdout=subprocess.PIPE)
subproc_ping_yt = subprocess.Popen(args_yt, stdout=subprocess.PIPE)

for line in subproc_ping_ya.stdout:             # пинг яндекс
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

for line in subproc_ping_yt.stdout:             # пинг ютуб
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
