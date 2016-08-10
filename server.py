#Модуль socket для сетевого программирования
from socket import *

#данные сервера
host = 'localhost'
port = 777
addr = (host,port)

#socket - функция создания сокета 
#первый параметр socket_family может быть AF_INET или AF_UNIX
#второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
tcp_socket = socket(AF_INET, SOCK_STREAM)
#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)
#listen - запускает прием TCP
tcp_socket.listen(1)
fp = open("file.jpg", "wb")
#Бесконечный цикл работы программы
while True:
    
    #Если мы захотели выйти из программы
    question = input('Do you want to quit? y\\n: ')
    if question == 'y': break
    
    print('wait connection...')
    
    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    #устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)
    
    #recv - получает сообщение TCP
   
    while True:
     data = tcp_socket.resv(4096)
     if not data: break
     fp.write(data)
    fp.close()

    #если ничего не прислали, завершим программу
    if not data:
        conn.close()
        break
    else:
        # print(data)
        #send - передает сообщение TCP
        conn.send(b'Hello from server!')
        #close - закрывает сокет
        conn.close()
    
tcp_socket.close()
