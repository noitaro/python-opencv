import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk

# ウィンドウを作成
window = tkinter.Tk()

# タイトルを設定
window.title("Welcome to LikeGeeks app")

# geometry関数を使って、ウィンドウサイズを設定
window.geometry('800x600')

# 画像読み込み
img = Image.open('python-logo.png')
img = ImageTk.PhotoImage(img)

# キャンバスの作成
canvas = tkinter.Canvas(width=800, height=600)
canvas.place(x=0, y=0)

# キャンバスに画像を設定
canvas.create_image(10, 10, image=img, anchor=tkinter.NW)

# mainloop関数を呼び出し、ユーザーの操作を待ちます。
window.mainloop()
