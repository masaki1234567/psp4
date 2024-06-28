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

        days = ["月", "火", "水", "木", "金"]
        times = ["1", "2", "3", "4", "5", "6"]

        # 表の見出しを作成
        for i, day in enumerate(["時限/曜日"] + days):
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
        Schedule("Math", "月", "1", "lightblue"),
        Schedule("Science", "月", "2", "lightgreen"),
        Schedule("History", "火", "1", "lightcoral"),
        Schedule("PE", "火", "2", "lightskyblue"),
        Schedule("Art", "水", "1", "lightyellow"),
        Schedule("Music", "水", "2", "lightpink"),
        Schedule("Math", "木", "1", "lightblue"),
        Schedule("Science", "木", "2", "lightgreen"),
        Schedule("History", "金", "1", "lightcoral"),
        Schedule("PE", "金", "2", "lightskyblue")
    ]

    app = Timetable(schedule_list)
    app.mainloop()
