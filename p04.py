import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from datetime import datetime
import csv
import os

class Userdata:
    def __init__(self, root):
        self.root = root
        self.root.title("ユーザー情報登録画面")

        # 名前のレーベル＆エントリー作成
        self.username_label = tk.Label(root, text="名前:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # メールアドレスのレーベル＆エントリー作成
        self.email_label = tk.Label(root, text="メールアドレス:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        # 保存ボタン
        self.save_button = tk.Button(root, text="保存", command=self.save_info)
        self.save_button.grid(row=2, columnspan=2, pady=10)

    def save_info(self):
        username = self.username_entry.get()
        email = self.email_entry.get()

        if not username or not email:
            messagebox.showwarning("エラー！", "正しく入力してください")
            return

        file_exists = os.path.isfile("userdata.csv")

        with open("userdata.csv", "a", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Username", "Email"])
            writer.writerow([username, email])

        messagebox.showinfo("保存成功！", "保存しました！")
        self.username_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

        root = tk.Tk()
        app = TimetableApp(root)
        root.mainloop()

class Timetable:
    def __init__(self):
        self.reset_schedule()

    def reset_schedule(self):
        self.schedule = {day: {period: None for period in range(1, 7)} for day in ["月", "火", "水", "木", "金"]}

    def add_class(self, subject, day, period):
        if day in self.schedule and period in self.schedule[day]:
            self.schedule[day][period] = subject

    def get_schedule(self):
        return self.schedule

    def save_to_file(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["曜日", "時限", "科目"])
            for day, periods in self.schedule.items():
                for period, subject in periods.items():
                    writer.writerow([day, period, subject if subject else ""])

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                day, period, subject = row
                period = int(period)
                self.add_class(subject, day, period)

class TimetableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timetable Manager")

        self.timetable = Timetable()

        # Main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Widgets for adding classes
        self.subject_label = tk.Label(self.main_frame, text="Subject")
        self.subject_entry = tk.Entry(self.main_frame)
        self.day_label = tk.Label(self.main_frame, text="Day (月, 火, 水, 木, 金)")
        self.day_entry = tk.Entry(self.main_frame)
        self.period_label = tk.Label(self.main_frame, text="Period (1, 2, 3, 4, 5, 6)")
        self.period_entry = tk.Entry(self.main_frame)
        self.add_button = tk.Button(self.main_frame, text="Add Class", command=self.add_class)

        # Treeview for displaying timetable
        self.tree = ttk.Treeview(self.main_frame, columns=("月", "火", "水", "木", "金"), show="headings")
        self.tree.heading("月", text="月")
        self.tree.heading("火", text="火")
        self.tree.heading("水", text="水")
        self.tree.heading("木", text="木")
        self.tree.heading("金", text="金")

        self.tree.column("月", width=100, anchor="center")
        self.tree.column("火", width=100, anchor="center")
        self.tree.column("水", width=100, anchor="center")
        self.tree.column("木", width=100, anchor="center")
        self.tree.column("金", width=100, anchor="center")

        for i in range(1, 7):
            self.tree.insert("", "end", text=f"{i}時間目", values=("", "", "", "", ""))

        # Layout for adding classes
        self.subject_label.grid(row=0, column=0, padx=5, pady=5)
        self.subject_entry.grid(row=0, column=1, padx=5, pady=5)
        self.day_label.grid(row=1, column=0, padx=5, pady=5)
        self.day_entry.grid(row=1, column=1, padx=5, pady=5)
        self.period_label.grid(row=2, column=0, padx=5, pady=5)
        self.period_entry.grid(row=2, column=1, padx=5, pady=5)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Buttons for saving, loading, and resetting timetable
        self.save_button = tk.Button(self.main_frame, text="Save Timetable", command=self.save_timetable)
        self.load_button = tk.Button(self.main_frame, text="Load Timetable", command=self.load_timetable)
        self.reset_button = tk.Button(self.main_frame, text="Reset Timetable", command=self.show_reset_screen)
        self.save_button.grid(row=4, column=0, padx=5, pady=5)
        self.load_button.grid(row=4, column=1, padx=5, pady=5)
        self.reset_button.grid(row=4, column=2, padx=5, pady=5)

        # Treeview layout
        self.tree.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        # Configure the treeview style
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
        style.configure("Treeview", rowheight=30)

        # Add alternating row colors
        self.tree.tag_configure('odd', background='#f0f0ff')
        self.tree.tag_configure('even', background='#ffffff')

        # Reset frame

        # Load timetable on startup
        self.default_file_path = "timetable.csv"
        if os.path.exists(self.default_file_path):
            self.timetable.load_from_file(self.default_file_path)
            self.update_treeview()

        self.update_treeview()

    def add_class(self):
        subject = self.subject_entry.get()
        day = self.day_entry.get()
        period = int(self.period_entry.get())

        if not subject or not day or not period:
            messagebox.showerror("Input Error", "All fields are required")
            return

        if day not in ["月", "火", "水", "木", "金"] or period not in [1, 2, 3, 4, 5, 6]:
            messagebox.showerror("Input Error", "Invalid day or period")
            return

        self.timetable.add_class(subject, day, period)
        self.subject_entry.delete(0, tk.END)
        self.day_entry.delete(0, tk.END)
        self.period_entry.delete(0, tk.END)
        self.update_treeview()
        self.save_timetable()  # 自動保存

    def update_treeview(self):
        # Clear current content
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert updated content
        schedule = self.timetable.get_schedule()
        for period in range(1, 7):
            values = []
            for day in ["月", "火", "水", "木", "金"]:
                subject = schedule[day][period]
                values.append(subject if subject else "")
            tag = 'even' if period % 2 == 0 else 'odd'
            self.tree.insert("", "end", text=f"{period}時間目", values=tuple(values), tags=(tag,))

    def save_timetable(self):
        self.timetable.save_to_file(self.default_file_path)
        messagebox.showinfo("Save Timetable", "Timetable saved successfully!")

    def load_timetable(self):
        self.timetable.load_from_file(self.default_file_path)
        self.update_treeview()
        messagebox.showinfo("Load Timetable", "Timetable loaded successfully!")

    def show_reset_screen(self):
        self.main_frame.grid_forget()
        root = tk.Tk()
        app = Reset(root)
        root.mainloop()

class Homework:
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

class Reset:
    def __init__(self, root):
        self.root = root
        self.root.title("CSVファイルのクリア")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="timetable.csv と userdata.csv の中身をクリアします")
        self.label.pack(pady=10)

        self.clear_button = tk.Button(root, text="クリア", command=self.clear_csv_files)
        self.clear_button.pack(pady=20)

        self.clear_button = tk.Button(root, text="戻る", command=self.show_main_screen)
        self.clear_button.pack(pady=30)

    def clear_csv_files(self):
        files_to_clear = ['timetable.csv', 'userdata.csv', 'homework.csv']
        cleared_files = []
        missing_files = []

        for file_path in files_to_clear:
            if os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    pass  # 空の状態でファイルを閉じる
                cleared_files.append(file_path)
            else:
                missing_files.append(file_path)

        if cleared_files:
            messagebox.showinfo("Success", f"{', '.join(cleared_files)} の中身をクリアしました。")
        if missing_files:
            messagebox.showerror("Error", f"{', '.join(missing_files)} は存在しません。")

    def show_main_screen(self):
        self.root.grid_forget()
        root = tk.Tk()
        app = TimetableApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()

    def is_csv_empty(file_path):
        if not os.path.exists(file_path):
            return True
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # ファイルに一つでも行があれば
                    return False
        return True
    
    def check_csv_and_display():
        file_path = 'userdata.csv'  # チェックしたいCSVファイルのパスを指定
        if is_csv_empty(file_path):
            app = Userdata(root)
            root.mainloop()
        else:
            TimetableApp(root)
            root.mainloop()

    check_csv_and_display()