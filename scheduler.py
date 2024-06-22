#User（ユーザー）クラスはユーザー名、メールアドレスを持つ
class User:
    def __init__(self, name, mailaddress):
        self.name = name
        self.mailaddress = mailaddress
#Schedule（時間割）クラスは授業名、曜日、何限目、色を持つ
class Schedule:
    def __init__(self, name, dayofweek, time, color):
        self.name = name
        self.dayofweek = dayofweek
        self.time = time
        self.time = color
#Homework（課題）クラスは名前、説明文、締め切り、進捗情報を持つ
class Homework:
    def __init__(self, name, description, deadline, progress):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.progress = progress
#Mail（メール）クラスは名前、メールアドレス、文章を持つ
class Mail:
    def __init__(self, name, mailaddress, text):
        self.name = name
        self.mailaddress = mailaddress
        self.text = text
#Reset（リセット）クラスは確認を持つ
class Reset:
    def __init__(self, confirm = False):
        self.confirm = confirm

#以下、データ永続化機構
import csv

#以下、tkinterのウィンドウ操作
import tkinter as tk
import tkinter.ttk as ttk

def change_app(window):
    window.tkraise()

if __name__ == "__main__":
    #rootメインウィンドウの設定
    root = tk.Tk()
    root.title("scheduler")
    root.geometry("600x600")
    # rootメインウィンドウのグリッドを 1x1 にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # 時間割表示画面の作成と設置
    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text="時間割表示画面")
    entry1_frame = ttk.Entry(frame)
    button_change = ttk.Button(frame, text="時間割登録画面に移動", command=lambda: change_app(frame_app))
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change.pack()

    # 時間割登録画面の作成と設置
    frame_app = ttk.Frame(root)
    frame_app.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame_app = ttk.Label(frame_app, text="時間割登録画面")
    entry1_frame_app = ttk.Entry(frame_app)
    button_change_frame_app = ttk.Button(frame_app, text="時間割表示画面に移動", command=lambda: change_app(frame))
    # 各種ウィジェットの設置
    label1_frame_app.pack()
    entry1_frame_app.pack()
    button_change_frame_app.pack()

    # frameを前面にする
    frame.tkraise()
    root.mainloop()