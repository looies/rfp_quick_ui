import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, messagebox
from tkinter import font
from tkinter import StringVar
from tkinter import filedialog
from ftplib import FTP
import os
import re
from rfp_ui import mas_parse as ms


#
# 規劃的想法：
# 先做欄位table ， 再弄整個RFP的系統
# RFP系統也包含欄位table但size有點不一樣
# 所以在最底層的ButtomRoot上可以選擇要用哪一種Frame???



g_font = ('Arial', 12)




class ConnectError(Exception):
    pass


# 最底層的root
class ButtomRoot(tk.Tk):
   def __init__(self):
       tk.Tk.__init__(self)
#       固定整個畫面就是1180x780
       self.geometry('1180x780+150+10')

class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, master = parent)

        filmenu = tk.Menu(parent, tearoff=0)
        subfilemenu = tk.Menu(filmenu, tearoff=0)
        subfilemenu.add_command(label=" RFP專案")
        filmenu.add_cascade(label="新增", menu=subfilemenu)


        filmenu.add_command(label="開啟舊檔")
        filmenu.add_command(label="儲存")
        filmenu.add_command(label="另存新檔")
        filmenu.add_separator()
        filmenu.add_command(label="輸出")
        filmenu.add_separator()
        filmenu.add_command(label="結束")



        self.add_cascade(label="檔案", menu=filmenu)


        edimenu = tk.Menu(parent, tearoff=0)
        edimenu.add_command(label="複製")
        edimenu.add_command(label="剪下")
        edimenu.add_command(label="貼上")
        edimenu.add_separator()
        edimenu.add_command(label="字型")
        edimenu.add_separator()
        edimenu.add_command(label="復原")
        edimenu.add_command(label="取消復原")
        edimenu.add_separator()
        edimenu.add_command(label="轉換Table Format")
        self.add_cascade(label="編輯", menu=edimenu)

        loadingmenu = tk.Menu(parent, tearoff = 0)
        loadingmenu.add_command(label="從 FOC", command = LoadFocData)
        loadingmenu.add_command(label="從 NDB")
        self.add_cascade(label = '讀資料庫', menu = loadingmenu )

        parent.config(menu=self)


class ConnectionPm:
    def __init__(self):
        self._server_ip = None
    @property
    def server_ip(self):
        return self._server_ip

    @server_ip.setter
    def set_server_ip(self, value):
        try:
            self._server_ip = str(value)
        except:
            print('Type Error')








class LoadFocData:
    def __init__(self):
        self.ask_info_ui()



    def ask_info_ui(self):
        g_font = ('Arial', 12)
        self.root = tk.Tk()

        # 連線使用的變數
        # self.spath = tk.StringVar()

        self.ip_label = tk.Label(self.root, text='IP', font=g_font)
        self.ip_label.grid(row=0, column=0)

        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.grid(row=0, column=1)

        self.path_label = tk.Label(self.root, text='FOC 位置:', font=g_font)
        self.path_label.grid(row=1, column=0)

        self.path_entry = tk.Entry(self.root)
        self.path_entry.grid(row=1, column=1)

        self.user_label = tk.Label(self.root, text='user', font=g_font)
        self.user_label.grid(row=2, column=0)

        self.user_entry = tk.Entry(self.root)
        self.user_entry.grid(row=2, column=1)

        self.psw_label = tk.Label(self.root, text='password', font=g_font)
        self.psw_label.grid(row=3, column=0)

        self.psw_entry = tk.Entry(self.root)
        self.psw_entry.grid(row=3, column=1)

        # self.savepath_label = tk.Label(self.root, text='存檔位置', font=g_font)
        # self.savepath_label.grid(row=4, column=0)
        #
        # self.savepath_entry = tk.Entry(self.root)
        # self.savepath_entry.grid(row=4, column=1)
        #
        # self.browse_btn = tk.Button(self.root, text='瀏覽', command=self.ask_file_save_path)
        # self.browse_btn.grid(row=4, column=2)

        self.ok_button = tk.Button(self.root, text='OK', font=g_font, command = self.get_mas)
        self.ok_button.grid(row=5, columnspan=2)

        root.mainloop()

    # def ask_file_save_path(self):
    #     ask = filedialog.asksaveasfilename(initialdir=r"Desktop",
    #                                        filetypes=(("Mas File", "*.mas"), ("All File", "*.*")), title="請選擇本機存檔路徑")
    #     self.spath.set(ask)
    #     print(ask)




    def get_mas(self):
        def connect_error():
            tk.messagebox.showerror(title= 'Error', message='連線錯誤，請重新確認您輸入的IP或帳密')
        def mas_path_error():
            tk.messagebox.showerror(title= 'Error', message='MAS 路徑有誤，請以「/home*」為開頭')
        def file_error():
            tk.messagebox.showerror(title= 'Error', message='此路徑下沒有您指定的檔案，請重新輸入')

        # 先確認連線
        # try:
        ftp = FTP(self.ip_entry.get(), timeout =5)
        ftp.login(str.lower(self.user_entry.get()),self.psw_entry.get())


        # 連線OK，確認路徑
        if str(self.path_entry.get())[:5] == '/home':
            ftp.cwd(str.lower('/'.join(self.path_entry.get().split('/')[:-1])))


            filelst = []
            ftp.retrlines('LIST' , filelst.append)
            flag = False
            for f in filelst:
                if f.split()[-1] == self.path_entry.get().split('/')[-1]:
                    flag = True
                    break
                else:
                    flag = False

            if flag == True:
                file = open(os.path.expanduser("~\桌面") + '\\' + self.path_entry.get().split('/')[-1], 'wb')
                ftp.retrbinary('RETR ' + str(self.path_entry.get().split('/')[-1]), file.write)
                file.close()

                tmp = []
                aa  = ms.showcol(os.path.expanduser("~\桌面") + '\\' + self.path_entry.get().split('/')[-1], 1)
                for i in aa:
                    tmp.append([aa[4],aa[3],aa[5],aa[6]])

                MasData.data = tmp
                print(MasData.data)





                self.root.destroy()

            else:
                file_error()
        else:
            ConnectError()
            mas_path_error()
        # except:
        #     ConnectError()
        #     connect_error()


class MasData:
    def __init__(self, data):
        self.data = data

    # @property
    # def data(self):
    #     return self._data
    #
    # @data.setter
    # def data(self, new_data):
    #     self._data = new_data






# 欄位的notebook 兩個frame都會用，只是差在size
class ColumnNotebook(ttk.Notebook):

   def __init__(self, parent):
       # 設定讓tab往左靠，預設都放在中間很醜
       style = ttk.Style(parent)
       style.configure('toptab.TNotebook', tabposition='nw')

       # photo = tk.PhotoImage(file='1460226110-X.gif')
       # TODO:目前用按鈕來控制新增跟刪除，ICON沒解決！


       ttk.Notebook.__init__(self, master=parent, width =1000, height = 200, style = 'toptab.TNotebook')
       self.bind("<Double-Button-1>", self.addtab)


       addframe = tk.Frame(self)

       dataCol = ('column','pk', 'title', 'format')
       t = Tree(addframe, dataCol, 'headings')


       # set frame resize priorities
       addframe.rowconfigure(0, weight=1)
       addframe.columnconfigure(0, weight=1)






       # 填入data

       MasData.data = []
       idata = MasData.data
       for item in idata:
           t.insert('', 'end', values=item)




       t.bind("<<TreeviewSelect>>", t.get_selection_value)




       # addframe.pack()
       self.add(addframe, text = '+')
       self.pack(side = tk.TOP)

       f2 = tk.Frame(parent)
       f2.pack(side = tk.TOP)



       global fieldname
       fieldname = tk.StringVar()

       global pk
       pk = tk.StringVar()

       global title
       title = tk.StringVar()

       L1 = tk.Label(f2, text='欄位:', font = g_font)
       L1.grid(row = 0, column = 0)

       E1 = tk.Entry(f2, textvariable=fieldname, font = g_font)
       E1.grid(row = 0, column = 1)

       L2 = tk.Label(f2, text='PK', font=g_font)
       L2.grid(row=1, column=0)

       E2 = tk.Entry(f2, textvariable=pk, font=g_font)
       E2.grid(row=1, column=1)

       L3 = tk.Label(f2, text='中文名稱', font=g_font)
       L3.grid(row=2, column=0)

       E3 = tk.Entry(f2, textvariable=title, font=g_font)
       E3.grid(row=2, column=1)




   def addtab(self,event= None):

       # self.unbind("<Double-Button-1>")
       k = tk.Frame(self)
       self.add(k, text='tab2')
       tk.Button(k, text='tt', command=self.addtab).pack(side=tk.BOTTOM)






class Tree(ttk.Treeview):
    def __init__(self, parent, columns, show):
        ttk.Treeview.__init__(self, parent, columns = columns, show = show)
        self.grid(in_=parent, row=0, column=0, sticky=tk.NSEW)


        # 設定x軸y軸捲軸
        self.setxscr(parent)
        self.setyscr(parent)

        # 設定表頭
        self.setheader(columns)

    def setxscr(self,parent):
        self.xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.xview)
        self['xscroll'] = self.xsb.set
        self.xsb.grid(in_=parent, row=1, column=0, sticky=tk.EW)

    def setyscr(self, parent):
        self.ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.yview)
        self['yscroll'] = self.ysb.set
        self.ysb.grid(in_= parent, row=0, column=1, sticky=tk.NS)

    def setheader(self, columns):
        for c in columns:
            self.heading(c, text=c.title())
            self.column(c)

    def get_selection_value(self, event):
        global fieldname
        fieldname.set(self.set(self.selection())['column'])

        global pk
        pk.set(self.set(self.selection())['pk'])

        global title
        title.set(self.set(self.selection())['title'])





        # print()




        # for item in self.selection():
        #     item_text = self.item(item, 'text')
        #     print(item_text)


# 應該要做一個add 的function
# 需要update嗎？
# 那刪除呢？



# 欄位table 的 Frame





if __name__ == '__main__':
   root = ButtomRoot()
   ColumnNotebook(root)
   Menu(root)
   root.config()
   root.mainloop()

