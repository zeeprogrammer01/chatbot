from tkinter import *

root = Tk()

root.title('Chatbot')

root.geometry('400x500')

main_menu = Menu(root)



main_menu.add_command(label='Quit')

chatWindow = Text(root, bd=1, bg='light blue', width=50,height=8)
chatWindow.place(x=6, y=6,height = 385, width=370)

messageWindow = Text(root, bg='white', highlightbackground='#f0d8ef',width=30,height=4,)
messageWindow.place(x=128, y=400, height=88,width=260)

Button = Button(root, text='Send', bg='blue',activebackground='light blue',width = 12,height=5, font=('Arial',20))
Button.place(x=6,y=400,height=88, width= 120)
root.config(menu=main_menu)

scrollbar = Scrollbar(root, command = chatWindow.yview())
scrollbar.place(x=375, y=5, height = 385)

root.mainloop()
