import tkinter as tk
import tkinter.messagebox as tmsg

import random


def ButtonClick(event=None):
    b = editbox1.get()
    isok = False
    while isok == False:
        #b = input("数を入れてね>")
        if len(b) != 4:
            tmsg.showerror("エラー", "4桁の数字をいれてね")
            return
        else:
            kazuok = True
            for i in range(4):
                if ((b[i] < "0") or (b[i] > "9")):
                    tmsg.showerror("b["+str(i)+"]は数字ではありません．")
                    kazuok = False
                    return
                else:
                    isok = True

    hit = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit = hit + 1

    blow = 0
    blow = 0
    a1 = sorted(a)
    b1 = sorted(b)
    i = 0
    j = 0
    while True:
        if int(b1[j])==int(a1[i]):
            blow += 1
            i +=1
            j +=1
        else:
            if int(b1[j])>int(a1[i]):
                i+=1
            else:
                j+=1
        if i==4 or j==4:
            break
                    
                

    rirekibox.insert(tk.END, b + " h:"+str(hit)+"b:"+str(blow-hit)+"\n")

    if hit == 4:
        tmsg.showinfo("あたり", "おめでとうさん．あたりでっせ．")
    #    print("当たり")
        root.destroy()


# random.seed(0)
a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]
print(a)
# print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

root = tk.Tk()
root.geometry("600x800")
root.title("数あてゲーム")
root.bind('<Return>', ButtonClick)

rirekibox = tk.Text(root, font=(("Helvetica", 14)))
rirekibox.place(x=400, y=0, width=200, height=800)

label1 = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
label1.place(x=20, y=20)

editbox1 = tk.Entry(width=4, font=("Helvetica", 28))
editbox1.place(x=120, y=60)

button1 = tk.Button(root, text="チェック", font=(
    "Helvetica", 14), command=ButtonClick)
button1.place(x=220, y=60)
root.mainloop()
