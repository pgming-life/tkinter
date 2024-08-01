from tkinter import *
from tkinter import ttk
from glob import *
import subprocess

print("ロード中...")

# 選択プログラム実行
def show_selection():
    for i in lb.curselection():
        try:
            print("\n「{}」を開きます...".format(lb.get(i)))
            subprocess.check_output(['start', r'{}'.format(lb.get(i))], shell=True)
        except subprocess.CalledProcessError:
            print("\nファイルを開けません！！！")

# ウィンドウ設定
root = Tk()
root.title('Tkinter')
root.minsize(700, 500)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# フレーム設定
frame = ttk.Frame(root, padding=10)
frame.grid(sticky=(E, W, S, N))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# リストボックス設定
list_txt = glob("**/*.txt", recursive=True)
currencies = tuple(list_txt)
v1 = StringVar(value=currencies)
lb = Listbox(frame, listvariable=v1, height=3)
lb.grid(row=0, column=0, sticky=(E, W, S, N))

# スクロールバー設定
scrollbar = ttk.Scrollbar(
    frame,
    orient=VERTICAL,
    command=lb.yview)
lb['yscrollcommand'] = scrollbar.set
scrollbar.grid(row=0, column=1, sticky=(N, S))

# ボタン設定
button1 = ttk.Button(
    frame, text='OK',
    command=lambda: show_selection())
button1.grid(
    row=1, column=0, columnspan=2,
    pady=5, sticky=(S))

# メイン実行
root.mainloop()
