import tkinter as tk
from tkinter import messagebox
import os

class CSVFileCleanerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CSVファイルのクリア")
        self.master.geometry("300x150")

        # ラベルの作成
        self.label = tk.Label(master, text="timetable.csv と userdata.csv の中身をクリアします")
        self.label.pack(pady=10)

        # ボタンの作成
        self.clear_button = tk.Button(master, text="クリア", command=self.clear_csv_files)
        self.clear_button.pack(pady=20)

    def clear_csv_files(self):
        files_to_clear = ['timetable.csv', 'userdata.csv']
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

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVFileCleanerApp(root)
    root.mainloop()
