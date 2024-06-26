class Schedule:
    def __init__(self, name, day, time, color):
        self.name = name
        self.day = day
        self.time = time
        self.color = color

import tkinter as tk

class Timetable(tk.Tk):
    def __init__(self, schedules):
        super().__init__()
        self.title("Timetable")

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        times = ["9:00", "10:00"]

        # 表の見出しを作成
        for i, day in enumerate(["Time/Day"] + days):
            label = tk.Label(self, text=day, relief=tk.RIDGE, width=15, bg="lightgrey")
            label.grid(row=0, column=i, padx=1, pady=1)

        for j, time in enumerate(times):
            label = tk.Label(self, text=time, relief=tk.RIDGE, width=15, bg="lightgrey")
            label.grid(row=j+1, column=0, padx=1, pady=1)

        # 時間割データを表に追加
        for schedule in schedules:
            row = times.index(schedule.time) + 1
            column = days.index(schedule.day) + 1

            label = tk.Label(self, text=schedule.name, relief=tk.RIDGE, width=15, bg=schedule.color)
            label.grid(row=row, column=column, padx=1, pady=1)

if __name__ == "__main__":
    # Scheduleリストの定義
    schedule_list = [
        Schedule("Math", "Monday", "9:00", "lightblue"),
        Schedule("Science", "Monday", "10:00", "lightgreen"),
        Schedule("History", "Tuesday", "9:00", "lightcoral"),
        Schedule("PE", "Tuesday", "10:00", "lightskyblue"),
        Schedule("Art", "Wednesday", "9:00", "lightyellow"),
        Schedule("Music", "Wednesday", "10:00", "lightpink"),
        Schedule("Math", "Thursday", "9:00", "lightblue"),
        Schedule("Science", "Thursday", "10:00", "lightgreen"),
        Schedule("History", "Friday", "9:00", "lightcoral"),
        Schedule("PE", "Friday", "10:00", "lightskyblue")
    ]

    app = Timetable(schedule_list)
    app.mainloop()
