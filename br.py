# -*- coding: utf-8 -*-
import sys
import tkinter as tk
from tkinter import ttk
import time , json , os , csv

#print(sys.getdefaultencoding())

# 定義一個計算用的函數
def Enter(*args):
    if sender.get() == '' or receiver.get() == '' or date.get() == '' or content.get() == '' :
        text = "資料填寫不齊全，請完整填寫後再按儲存!"
    elif "," in sender.get()+receiver.get()+date.get()+content.get() :
        text = "資料內容不可含有英式鍵盤的逗號「,」，請更正後再按儲存!"
    else :
        # 使用 csv writer 時須注意以下
        # newlines embedded inside quoted fields will not be interpreted correctly,
        # and on platforms that use \r\n linendings on write an extra \r will be added.
        # It should always be safe to specify newline='' in open(),
        # since the csv module does its own (universal) newline handling.
        f = open('record.br', 'a+', encoding='utf8', newline='')
        datalist = [sender.get(),receiver.get(),date.get(),content.get()]
        csv.writer(f).writerow(datalist)
        #f.write(",".join([sender.get(),receiver.get(),date.get(),content.get()]) + "\n")
        f.close()
        text = "儲存成功!!\n" + sender.get() + "\n" + receiver.get() + "\n" + date.get() + "\n" + content.get() + "\n"
        if boolean1.get() or boolean2.get() or boolean4.get() :
            f = open('defalt.br', 'r', encoding='utf8')
            defalt = json.load(f)
            f.close()
            if boolean1.get() :
                defalt[1] = sender.get()
                text += sender.get() + " 已成為預設值\n"
            if boolean2.get() :
                defalt[2] = receiver.get()
                text += receiver.get() + " 已成為預設值\n"
            if boolean4.get() :
                defalt[4] = content.get()
                text += content.get() + " 已成為預設值\n"
            f = open('defalt.br', 'w', encoding='utf8')
            json.dump(defalt,f,ensure_ascii=False)
            f.close()
    message.set(text)
    content.set('')


# 創建視窗
root = tk.Tk()
root.title("外送早餐紀錄器")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# 宣告變數
sender = tk.StringVar()
receiver = tk.StringVar()
date = tk.StringVar()
content = tk.StringVar()
boolean1 = tk.BooleanVar()
boolean2 = tk.BooleanVar()
boolean3 = tk.BooleanVar()
boolean4 = tk.BooleanVar()
message = tk.StringVar()
# 設定變數預設值(初始值)
date.set(time.strftime("%x"))
if os.path.isfile('defalt.br') :
    f = open('defalt.br', 'r', encoding='utf8')
    defalt = json.load(f)
    f.close()
    sender.set(defalt[1])
    receiver.set(defalt[2])
    content.set(defalt[4])
else :
    f = open('defalt.br', 'w+', encoding='utf8')
    json.dump(['','','','',''],f)
    f.close()


# 創建GUI面板
# 第 0 行
ttk.Label(mainframe, text="標題", font=12).grid(column=0, row=0)
ttk.Label(mainframe, text="送餐人 :").grid(column=0, row=1, sticky=tk.W)
ttk.Label(mainframe, text="收取人 :").grid(column=0, row=2, sticky=tk.W)
ttk.Label(mainframe, text="日期 :").grid(column=0, row=3, sticky=tk.W)
ttk.Label(mainframe, text="早餐內容 :").grid(column=0, row=4, sticky=tk.W)
# 第 1 行
ttk.Label(mainframe, text="輸入欄位", font=12).grid(column=1, row=0)
ttk.Entry(mainframe, width=20, textvariable=sender).grid(column=1, row=1)
ttk.Entry(mainframe, width=20, textvariable=receiver).grid(column=1, row=2)
ttk.Entry(mainframe, width=20, exportselection=0, textvariable=date).grid(column=1, row=3)
ttk.Entry(mainframe, width=20, textvariable=content).grid(column=1, row=4)
# 第 2 行
ttk.Label(mainframe, text="附加功能", font=12).grid(column=2, row=0)
ttk.Checkbutton(mainframe, text="將此值存成預設值", variable=boolean1, onvalue=True, offvalue=False).grid(column=2, row=1, sticky=tk.W)
ttk.Checkbutton(mainframe, text="將此值存成預設值", variable=boolean2, onvalue=True, offvalue=False).grid(column=2, row=2, sticky=tk.W)
ttk.Label(mainframe, text="預設值為當天日期").grid(column=2, row=3, sticky=tk.W)
ttk.Checkbutton(mainframe, text="將此值存成預設值", variable=boolean4, onvalue=True, offvalue=False).grid(column=2, row=4, sticky=tk.W)
# 第 3 行
ttk.Label(mainframe, text="備註", font=12).grid(column=3, row=0)
ttk.Label(mainframe, text="送早餐來的人(學生)").grid(column=3, row=1, sticky=tk.W)
ttk.Label(mainframe, text="吃早餐的人(自己)").grid(column=3, row=2, sticky=tk.W)
ttk.Label(mainframe, text="格式: 月/日/年").grid(column=3, row=3, sticky=tk.W)
ttk.Label(mainframe, text="可自行填寫").grid(column=3, row=4, sticky=tk.W)
# 第 5 列
ttk.Label(mainframe, textvariable=message, foreground="red").grid(column=1, row=5, columnspan=2)
ttk.Button(mainframe, text="儲存", command=Enter).grid(column=3, row=5)


"""
# 創建輸入欄位
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

# 創建文字標籤 & 按鈕
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(tk.W, tk.E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=tk.W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W)


# 將游標關注設定在輸入欄位
feet_entry.focus()
"""
# 綁定 Enter 鍵為執行函數
root.bind('<Return>', Enter)
# 將每一個 grid 內的欄位格都設定 padding
for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=5)

# 執行
root.mainloop()
