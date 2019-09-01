# Tkinter パッケージ を インポート
import tkinter

# ウィンドウを作成
window = tkinter.Tk()

# タイトルを設定
window.title("Welcome to LikeGeeks app")

# geometry関数を使って、ウィンドウサイズを設定
window.geometry('350x200')

# ラベルを作成
lbl = tkinter.Label(window, text="Hello", font=("Arial Bold", 50))

# grid関数を使って、表示位置を指定
lbl.grid(column=0, row=0)

# mainloop関数を呼び出し、ユーザーの操作を待ちます。
window.mainloop()
