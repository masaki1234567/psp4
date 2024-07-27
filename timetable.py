import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import csv
import os

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
            writer.writerow(["Day", "Period", "Subject"])
            for day, periods in self.schedule.items():
                for period, subject in periods.items():
                    writer.writerow([day, period, subject if subject else ""])

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
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
        self.reset_frame = tk.Frame(root)

        self.reset_label = tk.Label(self.reset_frame, text="Are you sure you want to reset the timetable?")
        self.confirm_reset_button = tk.Button(self.reset_frame, text="Yes, Reset", command=self.reset_timetable)
        self.cancel_reset_button = tk.Button(self.reset_frame, text="Cancel", command=self.show_main_screen)

        self.reset_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.confirm_reset_button.grid(row=1, column=0, padx=5, pady=5)
        self.cancel_reset_button.grid(row=1, column=1, padx=5, pady=5)

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

    def reset_timetable(self):
        self.timetable.reset_schedule()
        self.update_treeview()
        self.save_timetable()
        messagebox.showinfo("Reset Timetable", "Timetable reset successfully!")
        self.show_main_screen()

    def show_main_screen(self):
        self.reset_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky="nsew")

    def show_reset_screen(self):
        self.main_frame.grid_forget()
        self.reset_frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimetableApp(root)
    root.mainloop()
