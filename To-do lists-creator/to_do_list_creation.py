import os
import time
from fpdf import FPDF
import calendar
from datetime import datetime

class ToDoPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'To-Do List', 0, 1, 'C')

    def add_task(self, task, priority, due_date):
        self.set_font('Arial', '', 10)
        if priority == 'h':
            priority = "High"
        elif priority == 'm':
            priority = "Medium"
        elif priority == 'l':
            priority = "Low"
        self.cell(0, 10, f"Task: {task} | Priority: {priority} | Due: {due_date}", 0, 1)

def create_todo_pdf(tasks, filepath):
    pdf = ToDoPDF()
    pdf.add_page()

    for task in tasks:
        title, priority, due_date = task

        # Check if due date is just the day of the month
        # if len(due_date.split('-')) == 1:
        #     # Use current month and year
        current_date = datetime.now()
        due_date = f"{current_date.year}-{current_date.month}-{due_date}"

        pdf.add_task(title, priority, due_date)

    pdf.output(filepath)
    print(f"PDF saved as {filepath}")

class CalendarPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'To-Do List', 0, 1, 'C')

    def add_task_to_calendar(self, task, priority, due_date):

        current_date = datetime.now()
        cal = calendar.monthcalendar(current_date.year, current_date.month)
        self.cell(0, 10, f"Calendar for {current_date.month}-{current_date.year}", 0, 1)

        tasks = [(task, priority, due_date)]

        for week in cal:
            for day in week:
                if day != 0:
                    #due_date_text = ""
                    for task in tasks:
                        task, priority, due_date = tasks
                        if len(due_date.split('-')) == 1:
                            current_date = datetime.now()
                            due_date = f"{current_date.year}-{current_date.month}-{due_date}"
                        #int_due_date = int(due_date.split('-')[-1])
                        # if day == int_due_date:
                        #     due_date_text += " " + task
                        #     if due_date_text == due_date_text and priority.lower() == "h":
                        #         self.set_text_color(255, 0, 0)
                        #         self.cell(25, 40, txt=str(day) + " " + str(task), border=1, align='L')
                        #         self.set_text_color(0, 0, 0)
                        #     elif due_date_text == due_date_text and priority.lower() == "m":
                        #         self.set_text_color(255, 165, 0)
                        #         self.cell(25, 40, txt=str(day) + " " + str(task), border=1, align='L')
                        #         self.set_text_color(0, 0, 0)
                        #     elif due_date_text == due_date_text and priority.lower() == "l":
                        #         self.set_text_color(0, 255, 0)
                        #         self.cell(25, 40, txt=str(day) + " " + str(task), border=1, align='L')
                        #         self.set_text_color(0, 0, 0)
                        #     break
                else:
                    self.cell(25, 40, txt="", border=1, align='L')
            self.ln(40)

def create_Calendar(tasks, calfilepath):
   
    for task in tasks:
        task, priority, due_date = task

    pdf1 = CalendarPDF()
    pdf1.add_page()

    pdf1.ln(10)  # Add a line break between the task list and the calendar
    pdf1.set_font('Arial', 'B', 10)
    pdf1.cell(0, 10, "Calendar", 0, 1, 'C')  # Add a header for the calendar
    pdf1.set_font('Arial', '', 10)

    pdf1.add_task_to_calendar(task, priority, due_date)
    #int_due_date = int(due_date)

    pdf1.output(calfilepath)
    print(f"Calendar saved as {calfilepath}")


def main(task, priority, due_date):
    # Makes and empty list
    tasks = []
    # Adds the task to the list
    tasks.append((task, priority, due_date))

    current_date = time.strftime("%d-%m-%Y")
    second_date = str(current_date)

    # Define the full file path (including the filename)
    folder_name_path = "/Users/willwalker/Desktop/Homework/CS 111/To-do lists-creator/To-do-lists/"
    folder_name = f"To-do-list-for-{current_date}"
    full_folder_path = f"{folder_name_path}{folder_name}"

    try:
        os.mkdir(full_folder_path)
    except FileExistsError:
        pass

    # Sets the default folder path
    file_name_path = f"{folder_name_path}To-do-list-for-{second_date}"
    calendar_name_path = f"{folder_name_path}Calendar-for-{second_date}"

    # Define the file name
    file_name = f"the_todo_list.pdf"
    filepath = os.path.join(file_name_path, file_name)

    calendarname = f"calendar.pdf"
    calendarpath = os.path.join(calendar_name_path, calendarname)

    # Creates the PDF with the tasks and saves it
    create_todo_pdf(tasks, filepath)

    # Creates the Calendar
    create_Calendar(tasks, calendarpath)

if __name__ == "__main__":
    task = "CS"
    priority = "h"
    due_date = "10"
    main(task, priority, due_date)