import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.course_label = tk.Label(root, text="授業名:")
        self.course_label.grid(row=0, column=0)
        self.course_entry = tk.Entry(root)
        self.course_entry.grid(row=0, column=1)

        self.assignment_label = tk.Label(root, text="課題名:")
        self.assignment_label.grid(row=1, column=0)
        self.assignment_entry = tk.Entry(root)
        self.assignment_entry.grid(row=1, column=1)

        self.description_label = tk.Label(root, text="課題概要:")
        self.description_label.grid(row=2, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=2, column=1)

        self.deadline_label = tk.Label(root, text="締め切り日 (YYYY-MM-DD):")
        self.deadline_label.grid(row=3, column=0)
        self.deadline_entry = tk.Entry(root)
        self.deadline_entry.grid(row=3, column=1)

        self.progress_label = tk.Label(root, text="進捗情報:")
        self.progress_label.grid(row=4, column=0)
        self.progress_entry = tk.Entry(root)
        self.progress_entry.grid(row=4, column=1)

        self.save_button = tk.Button(root, text="保存", command=self.save_task)
        self.save_button.grid(row=5, column=1)

        self.tasks_listbox = tk.Listbox(root, width=50)
        self.tasks_listbox.grid(row=6, column=0, columnspan=2)

        self.load_tasks()

    def save_task(self):
        course = self.course_entry.get()
        assignment = self.assignment_entry.get()
        description = self.description_entry.get()
        deadline = self.deadline_entry.get()
        progress = self.progress_entry.get()

        if not course or not assignment or not description or not deadline or not progress:
            messagebox.showwarning("入力エラー", "すべてのフィールドを入力してください")
            return

        try:
            datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            messagebox.showwarning("日付エラー", "締め切り日はYYYY-MM-DD形式で入力してください")
            return

        task_info = [course, assignment, description, deadline, progress]
        self.save_to_csv(task_info)

        self.tasks_listbox.insert(tk.END, f"授業名: {course}, 課題名: {assignment}, 概要: {description}, 締め切り日: {deadline}, 進捗: {progress}")

        self.clear_entries()

    def save_to_csv(self, task_info):
        file_exists = os.path.isfile('homework.csv')

        with open('homework.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["授業名", "課題名", "課題概要", "締め切り日", "進捗情報"])
            writer.writerow(task_info)

    def load_tasks(self):
        if os.path.isfile('homework.csv'):
            with open('homework.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    self.tasks_listbox.insert(tk.END, f"授業名: {row[0]}, 課題名: {row[1]}, 概要: {row[2]}, 締め切り日: {row[3]}, 進捗: {row[4]}")

    def clear_entries(self):
        self.course_entry.delete(0, tk.END)
        self.assignment_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.progress_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
