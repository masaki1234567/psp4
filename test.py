import tkinter as tk

def save_data():
    data = entry.get()  # 入力データを取得する
    with open('userdata.txt', 'w') as f:
        f.write(data)  # テキストファイルにデータを書き込む

root = tk.Tk()
root.title("データ保存アプリ")

label = tk.Label(root, text="データを入力してください:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="保存", command=save_data)
button.pack(pady=10)

root.mainloop()
