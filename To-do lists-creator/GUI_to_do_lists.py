import to_do_list_creation
import tkinter as tk

def firstwindow():
    window = tk.Tk()
    window.title("To-do Lists")

    label = tk.Label(window, text="To-Do Lists Maker:")
    label.pack()

    labeloftasks = tk.Label(window, text="The amount of tasks you want:")
    labeloftasks.pack()
    tasks = tk.Entry(window, width=100)
    tasks.pack()

    def get_tasks():
        tasks_amount = int(tasks.get())
        secondwindow(tasks_amount)
        window.destroy()

    button = tk.Button(window, text="Submit", command=get_tasks)
    button.pack()

    window.mainloop()

def secondwindow(tasks_amount):
    window = tk.Tk()
    window.title("To-do Lists Items")

    for i in range(tasks_amount):
        labeloftasks = tk.Label(window, text="Enter your task title below:")
        labeloftasks.pack()
        task = tk.Entry(window, width=100)
        task.pack()

        labbelofpriority = tk.Label(window, text="Enter the priority of the task (l/m/h):")
        labbelofpriority.pack()
        priority = tk.Entry(window, width=100)
        priority.pack()

        labelofdue_date = tk.Label(window, text="Enter the due date of the task:")
        labelofdue_date.pack()
        due_date = tk.Entry(window, width=100)
        due_date.pack()

    def submit_tasks():
        task1 = task.get()
        priority1 = priority.get()   
        due_date1 = due_date.get()
        to_do_list_creation.main(task1, priority1, due_date1)
        #window.destroy()

    button2 = tk.Button(window, text="Submit", command=submit_tasks)
    button2.pack()

    window.mainloop()

firstwindow()
