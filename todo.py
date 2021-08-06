import tkinter
import threading
from tkinter import messagebox
import sys

tasks = []
timer = threading
real_timer = threading
ok_thread = True

def get_tasks(event=""):
    work = todo.get()
    hour = int(time.get())
    todo.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    todo.focus_set()
    add_record(work, hour)
    if 0 < hour < 9999:
        update_record()

def add_record(work, hrs):
    tasks.append([work, hrs])
    clock = threading.Timer(hrs, proceed_time, [work])
    clock.start()

def update_record():
    if WorkingList.size() > 0:
        WorkingList.delete(0, "end")
    for task in tasks:
        WorkingList.insert("end", "" + task[0] + "=======>>> Time left: " + str(task[1]) + " seconds" )

def proceed_time(task):
    tkinter.messagebox.showinfo("Notification", "It`s Now the time for : " + task)

def actual_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, actual_time)
        real_timer.start()
        for task in tasks:
            if task[1] == 0:
                tasks.remove(task)
                task[1] -= 1
                update_record()

if __name__ == '__main__':

    root = tkinter.Tk()
    root.geometry("460x480")
    root.title("Todo list")
    root.rowconfigure(0, weight=1)
    root.config(bg="blue")

frame = tkinter.Frame(root)
frame.pack()

lbl = tkinter.Label(root, text="Завдання", fg="white", bg="blue",
font=('Arial', 12), wraplength=200)
lbl_hrs = tkinter.Label(root, text="Час", fg="white",
bg="blue", font=('Arial', 12), wraplength=200)
todo = tkinter.Entry(root, width=30, font=('Arial', 12))
time = tkinter.Entry(root, width=15, font=('Arial', 12))
post = tkinter.Button(root, text='Таск', fg="white", bg='green',
font=('Arial', 12), relief="ridge", bd=5, height=3, width=30, command=get_tasks)
Exit = tkinter.Button(root, text='Вихід', fg="white", bg='red', height=3,
font=('Arial Bold', 12), relief="ridge", bd=5, width=30, command=root.destroy)
WorkingList = tkinter.Listbox(root, font=('Arial', 12))

if tasks != "":
    actual_time()

root.bind('>Return>', get_tasks)


lbl.place(x=0, y=10, width=200, height=25)
lbl_hrs.place(x=235, y=10, width=200, height=25)
todo.place(x=20, y=40, width=160, height=25)
time.place(x=245, y=40, width=170, height=25)
post.place(x=62, y=80, width=100, height=25)
Exit.place(x=302, y=80, width=50, height=25)
WorkingList.place(x=20, y=120, width=395, height=300)


root.mainloop()
ok_thread = False
sys.exit("FINISHED")
