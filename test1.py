#色付きの時間割表を作る

import tkinter as tk

class Schedule:
    def __init__(self, name, day, time, color):
        self.name = name
        self.day = day
        self.time = time
        self.color = color


class ColorfulTable(tk.Tk):
    def __init__(self, schedules):
        super().__init__()
        self.title("Schedule Table")

        # 表の見出し
        headers = ["Name", "Day", "Time", "Color"]
        for j, header in enumerate(headers):
            label = tk.Label(self, text=header, relief=tk.RIDGE, width=15, bg="lightgrey")
            label.grid(row=0, column=j, padx=1, pady=1)

        # スケジュールデータを表に追加
        for i, schedule in enumerate(schedules, start=1):
            label_name = tk.Label(self, text=schedule.name, relief=tk.RIDGE, width=15, bg=schedule.color)
            label_name.grid(row=i, column=0, padx=1, pady=1)
            
            label_day = tk.Label(self, text=schedule.day, relief=tk.RIDGE, width=15, bg=schedule.color)
            label_day.grid(row=i, column=1, padx=1, pady=1)
            
            label_time = tk.Label(self, text=schedule.time, relief=tk.RIDGE, width=15, bg=schedule.color)
            label_time.grid(row=i, column=2, padx=1, pady=1)
            
            label_color = tk.Label(self, text=schedule.color, relief=tk.RIDGE, width=15, bg=schedule.color)
            label_color.grid(row=i, column=3, padx=1, pady=1)

if __name__ == "__main__":
    # Scheduleリストの定義
    schedule_list = [
        Schedule("Meeting", "Monday", "10:00", "lightblue"),
        Schedule("Lunch", "Tuesday", "12:00", "lightgreen"),
        Schedule("Workout", "Wednesday", "18:00", "lightcoral"),
        Schedule("Study", "Thursday", "20:00", "lightskyblue")
    ]

    app = ColorfulTable(schedule_list)
    app.mainloop()
