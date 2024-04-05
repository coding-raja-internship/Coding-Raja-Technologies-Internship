from tkinter import *

class ToDo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150') 

        self.label = Label(self.root, text='To-Do-List-App',
             font='ariel, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
             font='ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
             font='ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)
        
        # Add text
        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        # Delete text
        def delete():
            selected_index = self.main_text.curselection()
            if selected_index:
                self.main_text.delete(selected_index)
                with open('data.txt', 'r') as f:
                    lines = f.readlines()
                with open('data.txt', 'w') as f:
                    for line in lines:
                        if line.strip() != self.main_text.get(selected_index):
                            f.write(line)

        # Check if file exists, if not create it
        try:
            with open('data.txt', 'r'):
                pass
        except FileNotFoundError:
            with open('data.txt', 'w'):
                pass

        # Read from file
        with open('data.txt', 'r') as file:
            for line in file:
                self.main_text.insert(END, line.strip())

        # Buttons
        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                 width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                 width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=30, y=280)

def main():
    root = Tk()
    ui = ToDo(root)
    root.mainloop()

if __name__ == "__main__":
    main()




