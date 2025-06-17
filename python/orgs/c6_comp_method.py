#+begin_src python
import tkinter as tk
import tkinter.messagebox as tmsg

import random

def setup_window():
    global rirekibox, editbox1
    root.geometry("600x800")
    root.title("数あてゲーム")
    root.bind('<Return>', ButtonClick) # here is a trick!!!

    rirekibox = tk.Text(root, font=(("Helvetica", 14)))
    rirekibox.place(x=400, y=0, width=200, height=800)

    label1 = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
    label1.place(x=20, y=20)

    editbox1 = tk.Entry(width=4, font=("Helvetica", 28))
    editbox1.place(x=120, y=60)

    button1 = tk.Button(root, text="チェック", 
                        font=("Helvetica", 14), 
                        command=ButtonClick)
    button1.place(x=220, y=60)
def mk_four_digit_number():
    a = [random.randint(0, 9), 
         random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9)]
    
    print(a)
    return a
def check_input_number():
    b = editbox1.get()
    if len(b) != 4:
        tmsg.showerror("エラー", "4桁の数字をいれてね")
        return
    for i in range(4):
        if (b[i] < "0") or (b[i] > "9"):
            tmsg.showerror("エラー", "b["+str(i)+"]は数字ではありません．")
            return
    return [int(b[0]),int(b[1]), int(b[2]), int(b[3])]

def check_hit_and_blow(answer, trial):
    blow, hit = 0, 0
    if trial is None:
        return 0,0
    answer = answer[:] # 浅いコピー
    trial = trial[:] # 浅いコピー
    for i in range(len(trial)):
        if trial[i] == answer[i]:
            answer[i] = trial[i] = None
            hit +=1
    for i in range(len(answer)): 
        for j in range(len(trial)):
            if (answer[i] == None) or (trial[j] == None):
                continue
            if answer[i] == trial[j] :
                answer[i] = trial[j] = None
                blow+=1
    return hit, blow
def ButtonClick(event=None):
    b = check_input_number()
    hit, blow = check_hit_and_blow(a,b)
    rirekibox.insert(tk.END, str(b) + " h:"+str(hit)+" b:"+str(blow)+"\n")

    if hit == 4:
        tmsg.showinfo("あたり", "おめでとうさん．あたりでっせ．")
        root.destroy()

a = mk_four_digit_number()

root = tk.Tk()
setup_window()

root.mainloop()
#+end_src
