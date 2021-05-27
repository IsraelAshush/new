import socket

input_word = input("enter word: ")

my_socket = socket.socket()
my_socket.connect(("127.0.0.1",8820))

my_socket.send(input_word.encode())
data = ''
while data == '':
    data = my_socket.recv(1024).decode()
print("The server send: {}".format(data))

my_socket.close()


def main():
        print("i")


if __name__ == '__main__':
    main()
#test2