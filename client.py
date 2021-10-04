from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from PIL import Image, ImageTk

host_address = input('Enter the IP address here: ')
username = input("Choose a username: ")

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf8")
            message_list.insert(tkinter.END, message)
            if message == 'USER':
                client_socket.send(username.encode('ascii'))
        except:
            print("An error occured")
            break

def send(event=None):  
    message = client_message.get()
    client_message.set("{}: ".format(username))  
    client_socket.send(bytes(message, "utf8"))
    split_message = message.split()
    if split_message[-1] == "/quit":
        client_socket.close()
        chat_title.quit()


def close_chat(event=None):
    client_message.set("/quit")
    send()

#chat frame
chat_title = tkinter.Tk()
chat_title.title("EC Chatroom")


#Background image using PIL
image1 = Image.open("image.png")
image1 = image1.resize((1500,800 ), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

chat_frame = tkinter.Frame(chat_title)
client_message = tkinter.StringVar() 
client_message.set("{}: ".format(username))

# Scroll bar and list box using tkinter
scrollbar = tkinter.Scrollbar(chat_frame)
scrollbar2 = tkinter.Scrollbar(chat_frame, orient='horizontal')
message_list = tkinter.Listbox(chat_frame, height=15, width=80, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set, bg='gray82', fg='gray5', font=("Helvetica",12))
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scrollbar2.pack(side=tkinter.BOTTOM, fill=tkinter.X)
scrollbar.config(command=message_list.yview)
scrollbar2.config(command=message_list.xview)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.place(x=100,y=200)
message_list.pack()
chat_frame.pack()

#Entry field using tkinter
entry_field = tkinter.Entry(chat_title, textvariable=client_message)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(chat_title, text="Send", command=send)
send_button.pack()

chat_title.protocol("WM_DELETE_WINDOW", close_chat)


port_number = 8080

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host_address, port_number))

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()