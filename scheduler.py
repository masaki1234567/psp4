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

#以下、データ保存機構
import tkinter as tk
import tkinter.ttk as ttk
userdata = "userdata.txt"
data = "data.csv"

def save_userdata():
    data = entry_username_frame.get() 
    with open(userdata, 'r') as f:
        lines = f.readlines()
    # 1行目にデータを挿入または置き換える
    if len(lines) == 0:
        lines.append(data + '\n')
    else:
        lines[0] = data + '\n'
    # ファイルに書き込む
    with open(userdata, 'w') as f:
        f.writelines(lines)

def save_mailaddress():
    data = entry_mailaddress_frame.get() 
    with open(userdata, 'r') as f:
        lines = f.readlines()
    # 2行目にデータを挿入または置き換える
    if len(lines) < 2:
        # 2行目が存在しない場合、新しい行を追加する
        while len(lines) < 1:
            lines.append('\n')  # 1行目が存在しない場合の対策
        lines.append(data + '\n')
    else:
        lines[1] = data + '\n'
    # ファイルに書き込む
    with open(userdata, 'w') as f:
        f.writelines(lines)

def save_userdata_mailaddress():
    save_userdata()
    save_mailaddress()

#以下、tkinterのウィンドウ操作
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

    # ユーザー情報登録画面の作成と設置
    frame_userinformation = ttk.Frame(root)
    frame_userinformation.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame_userinformation, text="ユーザー情報登録画面")
    label2_frame = ttk.Label(frame_userinformation, text="名前を入力してください")
    entry_username_frame = ttk.Entry(frame_userinformation)
    label3_frame = ttk.Label(frame_userinformation, text="メールアドレスを入力してください")
    entry_mailaddress_frame = ttk.Entry(frame_userinformation)
    button1_change_frame = tk.Button(frame_userinformation, text="保存", command=save_userdata_mailaddress)
    button2_change_frame = ttk.Button(frame_userinformation, text="時間割登録画面に移動", command=lambda: change_app(frame_schedule))
    # 各種ウィジェットの設置
    label1_frame.pack()
    label2_frame.pack()
    entry_username_frame.pack()
    label3_frame.pack()
    entry_mailaddress_frame.pack()
    button1_change_frame.pack()
    button2_change_frame.pack()

    # 時間割表示画面の作成と設置
    frame_schedule = ttk.Frame(root)
    frame_schedule.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame_schedule, text="時間割表示画面")
    entry1_frame = ttk.Entry(frame_schedule)
    button1_change = ttk.Button(frame_schedule, text="時間割登録画面に移動", command=lambda: change_app(frame_schedule_registration))
    entry2_frame = ttk.Entry(frame_schedule)
    button2_change = ttk.Button(frame_schedule, text="時間割編集画面に移動", command=lambda: change_app(frame_schedule_edit))
    entry3_frame = ttk.Entry(frame_schedule)
    button3_change = ttk.Button(frame_schedule, text="システムリセット確認画面に移動", command=lambda: change_app(frame_reset))
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button1_change.pack()
    entry2_frame.pack()
    button2_change.pack()
    entry3_frame.pack()
    button3_change.pack()

    # 時間割登録画面の作成と設置
    frame_schedule_registration = ttk.Frame(root)
    frame_schedule_registration.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame_schedule_registration, text="時間割登録画面")
    entry1_frame = ttk.Entry(frame_schedule_registration)
    button_change_frame = ttk.Button(frame_schedule_registration, text="時間割表示画面に移動", command=lambda: change_app(frame_schedule))
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change_frame.pack()

    # 時間割編集画面の作成と設置
    frame_schedule_edit = ttk.Frame(root)
    frame_schedule_edit.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame_schedule_edit, text="時間割編集画面")
    entry1_frame = ttk.Entry(frame_schedule_edit)
    button1_change_frame = ttk.Button(frame_schedule_edit, text="時間割表示画面に移動", command=lambda: change_app(frame_schedule))
    entry2_frame = ttk.Entry(frame_schedule_edit)
    button2_change_frame = ttk.Button(frame_schedule_edit, text="課題登録画面に移動", command=lambda: change_app(frame_hw_registration))
    entry3_frame = ttk.Entry(frame_schedule_edit)
    button3_change_frame = ttk.Button(frame_schedule_edit, text="課題進捗画面に移動", command=lambda: change_app(frame_hw_progress))
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button1_change_frame.pack()
    entry2_frame.pack()
    button2_change_frame.pack()
    entry3_frame.pack()
    button3_change_frame.pack()

    # 課題登録画面の作成と設置
    frame_hw_registration = ttk.Frame(root)
    frame_hw_registration.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame_hw_registration, text="課題登録画面")
    entry1_frame = ttk.Entry(frame_hw_registration)
    button_change_frame = ttk.Button(frame_hw_registration, text="時間割編集画面に移動", command=lambda: change_app(frame_schedule_edit))
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change_frame.pack()

    # 課題進捗画面の作成と設置
    frame_hw_progress = ttk.Frame(root)
    frame_hw_progress.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame_hw_progress, text="課題進捗画面")
    entry1_frame = ttk.Entry(frame_hw_progress)
    button_change_frame = ttk.Button(frame_hw_progress, text="時間割編集画面に移動", command=lambda: change_app(frame_schedule_edit))
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change_frame.pack()

    # システムリセット確認画面の作成と設置
    frame_reset = ttk.Frame(root)
    frame_reset.grid(row=0, column=0, sticky="nsew", pady=20)
    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame_reset, text="システムリセット確認画面")
    entry1_frame = ttk.Entry(frame_reset)
    button_change_frame = ttk.Button(frame_reset, text="時間割表示画面に移動", command=lambda: change_app(frame_schedule))
    entry2_frame = ttk.Entry(frame_reset)
    button2_change_frame = ttk.Button(frame_reset, text="ユーザー情報登録画面に移動", command=lambda: change_app(frame_userinformation))
    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change_frame.pack()
    entry2_frame.pack()
    button2_change_frame.pack()

    # frameを前面にする
    frame_userinformation.tkraise()
    root.mainloop()