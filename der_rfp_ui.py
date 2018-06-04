import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import font
from tkinter import StringVar



#
# 規劃的想法：
# 先做欄位table ， 再弄整個RFP的系統
# RFP系統也包含欄位table但size有點不一樣
# 所以在最底層的ButtomRoot上可以選擇要用哪一種Frame???



g_font = ('Arial', 12)


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
        loadingmenu.add_command(label="從 FOC")
        loadingmenu.add_command(label="從 NDB")
        self.add_cascade(label = '讀資料庫', menu = loadingmenu )








        parent.config(menu=self)










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

       dataCol = ('column','pk', 'title')
       t = Tree(addframe, dataCol, 'headings')


       # set frame resize priorities
       addframe.rowconfigure(0, weight=1)
       addframe.columnconfigure(0, weight=1)




       data = [[ 'WRNT_ID', 'Y', '證券碼'], [ 'WRNT_ID1', 'N', '證券碼(出貨碼)'], [ 'WRNT_OID', 'N', '證券碼(舊碼)'], [ 'WRNT_ID2', 'N', '交易所原始碼'], [ 'ISIN', 'N', '國際證券辯識號碼'], [ 'SEDOL', 'N', 'SEDOL'], [ 'ERASE', 'N', '失敗與否'], [ 'KEYIN1', 'N', '修改日期'], [ 'KEY_HR', 'N', '修改時間'], [ 'CKEYIN', 'N', '更改日期'], [ 'CKEY_HR', 'N', '更改時間'], [ 'BKEYIN', 'N', '更改日期(EVENT_TYPE)'], [ 'BKEY_HR', 'N', '更改時間(EVENT_TYPE)'], [ 'STK_NAME', 'N', 'TSE簡稱'], [ 'STK_NAME1', 'N', 'TSE簡稱1'], [ 'TSE_ENG', 'N', 'TSE英文簡稱'], [ 'TEJ_F_NAME', 'N', '權證名稱'], [ 'TEJ_NM', 'N', 'TEJ簡稱'], [ 'STK_ENG', 'N', '英文名稱'], [ 'STK_NAME_NEW', 'N', 'TSE簡稱(建檔用)'], [ 'STK_NAME1_NEW', 'N', 'TSE簡稱1(建檔用)'], [ 'TSE_ENG_NEW', 'N', 'TSE英文簡稱(建檔'], [ 'TEJ_F_NAME_N', 'N', '權證名稱(建檔用)'], [ 'TEJ_NM_NEW', 'N', 'TEJ簡稱(建檔用)'], [ 'STK_ENG_NEW', 'N', '英文名稱(建檔用)'], [ 'MKT', 'N', '市場別'], [ 'IND_BAN', 'N', '發行券商統編'], [ 'DATA_D', 'N', '發行公告日'], [ 'ZISS_D', 'N', '發行日'], [ 'ZMAT_D', 'N', '到期日'], [ 'TERM_M', 'N', '存續期間(月)'], [ 'ZLST_D_N', 'N', '上市公告日'], [ 'ZLST_D', 'N', '上市日期'], [ 'ALST_D', 'N', '實際上市日'], [ 'DLIST_D', 'N', '下市日'], [ 'ZPRE_D', 'N', '預計到期日'], [ 'ZLTRADE_D', 'N', '最後交易日'], [ 'ZLTRADE_D1', 'N', '預計最後交易日'], [ 'ZBEGIN_D', 'N', '履約開始日'], [ 'ZEND_D', 'N', '履約結束日'], [ 'TMAT_D', 'N', '到期日YT'], [ 'TDLIST_D', 'N', '下市日YT'], [ 'TPRE_D', 'N', '預計到期日YT'], [ 'TLTRADE_D', 'N', '最後交易日YT'], [ 'TLTRADE_D1', 'N', '預計最後交易日YT'], [ 'TBEGIN_D', 'N', '履約開始日YT'], [ 'TEND_D', 'N', '履約結束日YT'], [ 'YESNO', 'N', '是否已上市'], [ 'WAR_TYPE', 'N', '認購權證種類'], [ 'WAR_DER', 'N', '權證衍生種類'], [ 'WAR_DERD', 'N', '權證細種類'], [ 'C_P_TYPE', 'N', '認購(售)權證'], [ 'ST_PTF', 'N', '個股/組合'], [ 'SCNT', 'N', '標的數'], [ 'SETTLE', 'N', '履約方式'], [ 'ISS_CUR', 'N', '發行掛牌幣別'], [ 'ISS_EX', 'N', '發行匯率'], [ 'ISS_SIZE', 'N', '發行單位(千股)'], [ 'ISS_AMT', 'N', '發行總額(千元)'], [ 'X_ISSAMT', 'N', '發行總額(元)元大'], [ 'ISS_PRC', 'N', '發行價格(元)'], [ 'LST_PRC', 'N', '上市掛牌價(元)'], [ 'EX_CUR', 'N', '履約幣別'], [ 'ST_EX', 'N', '結算匯率'], [ 'PERCENT', 'N', '發行溢價'], [ 'EX_PRICE', 'N', '發行時履約價(元)'], [ 'EX_PCT', 'N', '價外發行%'], [ 'P_UP', 'N', '上限價格'], [ 'P_DOWN', 'N', '下限價格'], [ 'UP%', 'N', '上下限價履約價比'], [ 'P_SEC', 'N', '流動量提供券商'], [ 'P_WAY', 'N', '履行報價方式'], [ 'MAX_SIZE', 'N', '最大升降單位'], [ 'MIN_PRC', 'N', '履行責任最低價格'], [ 'PREDUE', 'N', '是否提前下市'], [ 'DUEREASON', 'N', '提前下市理由'], [ 'FOREIGN', 'N', '外資可否投資'], [ 'FOREIGN1', 'N', '外資採證券給付'], [ 'BROKCODE', 'N', '發行人委任券商'], [ 'INTEREST_R', 'N', '發行日利率'], [ 'FINANCE_R', 'N', '財務費用率'], [ 'FINANCE_C', 'N', '發行財務費用'], [ 'ISSVOLT', 'N', '發行日定價波動率'], [ 'ISSVOLT1', 'N', 'ISSVOLT1_TEJ'], [ 'RESETBEG', 'N', '重設期間起日'], [ 'RESETEND', 'N', '重設期間迄日'], [ 'RESETAVG', 'N', '重設計算均價日數'], [ 'RESET_UP', 'N', '重設百分比上限'], [ 'RESET_LO', 'N', '重設百分比下限'], [ 'RESETDAY', 'N', '重設生效日'], [ 'RE_BD', 'N', '上市幾日重設起日'], [ 'RE_ED', 'N', '上市幾日重設迄日'], [ 'RE_DATE', 'N', '上市幾日重設生效'], [ 'RESETFG', 'N', '有無重設'], [ 'RMK', 'N', '備註說明'], [ 'PAR', 'N', '面額'], [ 'STK_TYPE', 'N', '證券別'], [ 'TRADE_P', 'N', '標的證券市場'], [ 'CURR', 'N', '幣別'], [ 'CHGDATE', 'N', '換市場/換碼日'], [ 'DOER', 'N', '建檔者'], [ 'DOER1', 'N', '修改者'], [ 'WRSET', 'N', '權證結算價'], [ 'WRSETD', 'N', '權證交割日'], [ 'TEJ_FP_ID', 'N', 'NDB金融商品碼'], [ 'FPID_NKEYIN', 'N', 'NDB金融商品碼新增日'], [ 'FPID_NKEYHR', 'N', 'NDB金融商品碼新增時間'], [ 'FPID_KEYIN', 'N', 'NDB金融商品碼異動日'], [ 'FPID_KEYHR', 'N', 'NDB金融商品碼異動時間'], [ 'TYPE', 'Y', '事件別'], [ 'ZCVT_DD', 'N', '日期'], [ 'CO_ID16', 'N', '證券碼16'], [ 'CO_ID', 'N', '證券碼'], [ 'STK_CUR', 'N', '標的幣別'], [ 'ZEND_DD', 'N', '標的股價日期'], [ 'CL_PRC', 'N', '標的股價'], [ 'SHARE', 'N', '行使比例(股數)'], [ 'EXX_CUR', 'N', '履約幣別'], [ 'L_EX_PRC', 'N', '履約價格'], [ 'L_P_UP', 'N', '上限價格'], [ 'L_P_DOWN', 'N', '下限價格'], [ 'REASON', 'N', '調整原因'], [ 'DATA_D2', 'N', '事件公告日'], [ 'K_EVENT2', 'N', '資料日期'], [ 'KEY_HR2', 'N', '資料時間'], [ 'DOER2', 'N', '建檔者'], [ 'DOER3', 'N', '修改者'], [ 'OD1', 'Y', '次序'], [ 'TXT', 'N', '說明'], [ 'EVENT_TYPE', 'Y', '事件別'], [ 'BCO_ID16', 'N', '證券碼16'], [ 'BCO_ID', 'N', '證券碼'], [ 'BK_TRADE1', 'N', '交易起日'], [ 'BK_TRADE2', 'N', '交易迄日'], [ 'KEYIN3', 'N', '異動日'], [ 'KEY_HR3', 'N', '異動時'], [ 'ISSOD', 'Y', '發行次數'], [ 'AISS_D', 'N', '增發日期'], [ 'AISS_SIZE', 'N', '增發數量（千股）'], [ 'AISS_AMT', 'N', '增發金額（千元）'], [ 'AISS_PRC', 'N', '增發價格(元)'], [ 'KEYIN4', 'N', '異動日'], [ 'KEY_HR4', 'N', '異動時'],['','','']]

       # 填入data
       for item in data:
           k = 0
           t.insert('', 'end', values=item)
           k+=1
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

