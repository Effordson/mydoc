

# 功能菜单及全局变量定义

```
import tkinter as tk

window = tk.Tk(className='spinbox test')
window.geometry('300x100+600+300')


pw = tk.PanedWindow(window, orient='horizontal', width=10,bg='green')
pw.pack(fill='y', expand='no', side='left')

def b_call():
    change_bg(b)
def b1_call():
    change_bg(b1)
b = tk.Button(pw, text='选择文件aa', state='normal', background='white', command=b_call)
b.pack(side='top', expand=1)
b1 = tk.Button(pw, text='my button', background='white', command=b1_call)
b1.pack(side='top', expand=1)

var_dict = {'active': b}
def change_bg(v):
    var_dict['active'].config(background='white')
    var_dict['active'] = v
    var_dict['active'].config(background='red')


window.mainloop()
```



# 功能切换

```
import tkinter as tk

window = tk.Tk(className='spinbox test')
window.geometry('300x100+600+300')

# b = tk.Button(window, text='my button', font=('Arial', 12), bg='green')
# b.pack()

# t = tk.Text(window, background='gray', width=20, height=4, wrap='none')
# t.pack()
# t.insert('insert', 'hello world\n')

pw = tk.PanedWindow(window, orient='vertical', width=10,bg='green')
pw.pack(fill='y', expand='no', side='left')

pw1 = tk.Frame(window, bg='red')
pw1.pack(fill='x')
w = pw1
# pw1 = tk.PanedWindow(window, background='red', orient='horizontal')
# pw1.pack(fill='x', expand='no')
b3 = tk.Button(pw1, text='选择文件', background='blue', state='disabled')
b3.pack(expand='no')
b4 = tk.Button(pw1, text='选择文件', background='blue', state='disabled')
b4.pack(expand='no')

pw2 = tk.Frame(window, bg='red')
# pw2.pack(fill='x')
# pw1 = tk.PanedWindow(window, background='red', orient='horizontal')
# pw1.pack(fill='x', expand='no')
b4 = tk.Button(pw2, text='new pw', background='blue', state='disabled')
b4.pack(expand='no')
b5 = tk.Button(pw2, text='new pw', background='blue', state='disabled')
b5.pack(expand='no')

def callback():
    global w
    print('call callback')
    w.pack_forget()
    w = pw2
    pw2.pack(fill='x')
def active_b():
    global w
    print('call callback 11')
    w.pack_forget()
    w = pw1
    pw1.pack(fill='x')
b = tk.Button(pw, text='选择文件', background='blue', state='active', command=callback)
b.pack(side='top', expand=1)
b1 = tk.Button(pw, text='my button', background='blue', command=active_b)
b1.pack(side='top', expand=1)
# b2 = tk.Button(pw, text='my button', background='blue')
# b2.pack(side='left')

window.mainloop()
```

