from turtle import *
import turtle
from freegames import square, vector
from random import randrange
from random import *
from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import mysql.connector as msc

root = Tk()
root.title("PROMETHEUS")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")
img = ImageTk.PhotoImage(Image.open("D:\chrome downloads\\img.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#========================================VARIABLES AND ARRAYS========================================
LIST=[]
ILIST=[0]
USERNAME = StringVar()
PASSWORD = StringVar()
USER = StringVar()
PASS = StringVar()
HANG = StringVar()
SEARCH = StringVar()

#========================================METHODS==========================================
def Database():
    global conn, cursor
    connection_config_dict = {
    'user': 'root',
    'password': 'DragonKing29',
    'host': '127.0.0.1',
    'database': 'Prometheus',
    'raise_on_warnings': True,
    'autocommit': True
    }
    conn= msc.connect(**connection_config_dict)
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT username,password FROM `admin`")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('PROMETHEUS', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('PROMETHEUS', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("PROMETHEUS/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=3, pady=20)
    btn_login.bind('<Return>', Login)
    
def Home():
    global home
    home = Toplevel()
    home.title("PROMETHEUS/Home")
    width = 1024
    height = 520
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    home.resizable(0, 0)
    MainHome = Frame(home, width=1024, height = 520)
    MainHome.pack(side="top")
    imgh = ImageTk.PhotoImage(Image.open("D:\chrome downloads\\img(Home).png"))
    panelh = Label(MainHome, image = imgh)
    panelh.image = imgh
    panelh.pack(side = "bottom", fill = "both", expand = "yes")
    Title = Frame(home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="PROMETHEUS", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(home)
    filemenu1 = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu1.add_command(label="Logout", command=Logout)
    filemenu1.add_command(label="Add new",command=ShowAddNew)
    filemenu1.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Snake", command=ShowView)
    filemenu2.add_command(label="HangMan", command=ShowHangView)
    filemenu3.add_command(label="Snake",command=Snake)
    filemenu3.add_command(label="Hangman",command=ShowMainHang)
    menubar.add_cascade(label="Account", menu=filemenu1)
    menubar.add_cascade(label="HighScores", menu=filemenu2)
    menubar.add_cascade(label="Games" , menu=filemenu3)
    home.config(menu=menubar)
    home.config(bg="#6666ff")
    
def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("PROMETHEUS/Add new account")
    width = 600
    height = 500
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Account", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_username = Label(MidAddNew, text="USERNAME:", font=('arial', 25), bd=10)
    lbl_username.grid(row=0, sticky=W)
    lbl_password = Label(MidAddNew, text="PASSWORD:", font=('arial', 25), bd=10)
    lbl_password.grid(row=1, sticky=W)
    username = Entry(MidAddNew, textvariable=USER, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidAddNew, textvariable=PASS, font=('arial', 25), width=15)
    password.grid(row=1, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=20)

def AddNew():
    Database()
    cursor.execute("INSERT INTO `admin` (username, password) VALUES('%s','%s')" % (str(USER.get()), str(PASS.get())))
    conn.commit()
    USER.set("")
    PASS.set("")
    cursor.close()
    conn.close()
        
def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("PROMETHEUS/View Scores (Snake)")
    width = 600
    height = 400
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Scores", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("S_no", "Score","Account"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('S_no', text='Game_no',anchor=W)
    tree.heading('Score', text="Score",anchor=W)
    tree.heading('Account', text="Player",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `HighScores` ORDER BY score DESC;")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `Highscores` WHERE `account` LIKE '%s'"%(str(SEARCH.get())))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('PROMETHEUS', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `Highscores` WHERE `S_no` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
        
def ShowHangView():
    global hviewform
    hviewform = Toplevel()
    hviewform.title("PROMETHEUS/View Scores (HangMan)")
    width = 600
    height = 400
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    hviewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    hviewform.resizable(0, 0)
    HangViewForm()

def HangViewForm():
    global hangtree
    TopHangView = Frame(hviewform, width=600, bd=1, relief=SOLID)
    TopHangView.pack(side=TOP, fill=X)
    LeftHangView = Frame(hviewform, width=600)
    LeftHangView.pack(side=LEFT, fill=Y)
    MidHangView = Frame(hviewform, width=600)
    MidHangView.pack(side=RIGHT)
    lbl_text = Label(TopHangView, text="View Scores", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftHangView, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftHangView, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftHangView, text="Search", command=HSearch)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftHangView, text="Reset", command=HReset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftHangView, text="Delete", command=HDelete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidHangView, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidHangView, orient=VERTICAL)
    hangtree = ttk.Treeview(MidHangView, columns=("S_no", "Score","Account"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=hangtree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=hangtree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    hangtree.heading('S_no', text="Game_no",anchor=W)
    hangtree.heading('Score', text="Score",anchor=W)
    hangtree.heading('Account', text="Player",anchor=W)
    hangtree.column('#0', stretch=NO, minwidth=0, width=0)
    hangtree.column('#1', stretch=NO, minwidth=0, width=200)
    hangtree.column('#2', stretch=NO, minwidth=0, width=120)
    hangtree.column('#3', stretch=NO, minwidth=0, width=120)
    hangtree.pack()
    DisplayHangData()

def DisplayHangData():
    Database()
    cursor.execute("SELECT * FROM `HHighScores` ORDER BY score ASC;")
    fetch = cursor.fetchall()
    for data in fetch:
        hangtree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def HSearch():
    if SEARCH.get() != "":
        hangtree.delete(*hangtree.get_children())
        Database()
        cursor.execute("SELECT * FROM `HHighscores` WHERE `account` LIKE '%s'"%(str(SEARCH.get())))
        fetch = cursor.fetchall()
        SEARCH.set("")
        for data in fetch:
            hangtree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def HReset():
    hangtree.delete(*hangtree.get_children())
    DisplayHangData()
    SEARCH.set("")

def HDelete():
    if not hangtree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('PROMETHEUS', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = hangtree.focus()
            contents =(hangtree.item(curItem))
            selecteditem = contents['values']
            hangtree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `HHighscores` WHERE `S_no` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def ShowHighForm():
    global highform
    highform = Toplevel()
    highform.title("PROMETHEUS/Score Entry Form (Snake)")
    width = 600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    highform.resizable(0, 0)
    highform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    HighForm()
    
def HighForm():
    TopHighForm = Frame(highform, width=600, height=100, bd=1, relief=SOLID)
    TopHighForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopHighForm, text="Score Card", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidHighForm = Frame(highform, width=600)
    MidHighForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidHighForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_FScore = Label(MidHighForm, text="Score:", font=('arial', 25), bd=18)
    lbl_FScore.grid(row=1)
    lbl_Score = Label(MidHighForm, text=len(snake), font=('arial', 25), bd=18)
    lbl_Score.grid(row=1, column=1)
    username = Entry(MidHighForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    btn_entry = Button(MidHighForm, text="Enter", font=('arial', 18), width=30, command=Entrye)
    btn_retry = Button(MidHighForm, text="Retry", font=('arial', 18), width=30, command=Retry)
    btn_quit = Button(MidHighForm, text="Quit Game", font=('arial', 18), width=30, command=Quit)
    btn_entry.grid(row=2, columnspan=2, pady=20)
    btn_retry.grid(row=3, columnspan=2, pady=20)
    btn_quit.grid(row=4, columnspan=2, pady=20)
    btn_entry.bind('<Return>', Entrye)
    btn_retry.bind('<Return>', Retry)
    btn_quit.bind('<Return>', Quit)

def Quit():
    result = tkMessageBox.askquestion('Snake', 'Do you want to exit?', icon="warning")
    if result == 'yes':
        bye()
        highform.destroy()

def Retry():
    highform.destroy()
    Snake()

def Entrye():
    Database()
    cursor.execute("INSERT INTO `Highscores` (score, account) VALUES(%i,'%s')" % (len(snake),USERNAME.get()))
    USERNAME.set("")
    conn.commit()
    cursor.close()
    conn.close()
    result = tkMessageBox.askquestion('PROMETHEUS', 'Do you want to retry the game ?', icon="warning")
    if result == 'yes':
        highform.destroy()
        Snake()
    elif result == 'no':
        bye()
    highform.destroy()

def Snake():
    global snake
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)

    def change(x, y):
        "Change snake direction."
        aim.x = x
        aim.y = y

    def inside(head):
        "Return True if head inside boundaries."
        return -200 < head.x < 190 and -200 < head.y < 190

    def move():
        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)
        if not inside(head) or head in snake:
            square(head.x, head.y, 9, 'red')
            update()
            ShowHighForm()
            return
        snake.append(head)
        if head == food:
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)
        clear()
        for body in snake:
            square(body.x, body.y, 9, 'black')
        square(food.x, food.y, 9, 'green')
        update()
        ontimer(move, 100)
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()

def ShowMainHang():
    global mhangform
    mhangform = Toplevel()
    mhangform.title("PROMETHEUS/HangMan")
    width = 600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    mhangform.resizable(0, 0)
    mhangform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    MainHang()

def MainHang():
    TopMainHang = Frame ( mhangform, width=600, height=100, bd=1, relief=SOLID)
    TopMainHang.pack(side=TOP, pady=20)
    lbl_text = Label(TopMainHang, text="HangMan", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidMainHang = Frame(mhangform, width=600)
    MidMainHang.pack(side=TOP, pady=50)
    btn_anime = Button(MidMainHang, text="Anime", font=('arial', 18), width=30, command=Anime)
    btn_auto = Button(MidMainHang, text="Automobile Companies", font=('arial', 18), width=30, command=Autom)
    btn_marvel = Button(MidMainHang, text="Marvel Characters", font=('arial', 18), width=30, command=Marvel)
    btn_dawg = Button(MidMainHang, text="Dog Breeds", font=('arial', 18), width=30, command=Dawg)
    btn_quit = Button(MidMainHang, text="Quit Game", font=('arial', 18), width=30, command=HQuit)
    btn_anime.grid(row=2, columnspan=2, pady=20)
    btn_auto.grid(row=3, columnspan=2, pady=20)
    btn_marvel.grid(row=4, columnspan=2, pady=20)
    btn_dawg.grid(row=5, columnspan=2, pady=20)
    btn_quit.grid(row=6, columnspan=2, pady=20)
    btn_anime.bind('<Return>', Anime)
    btn_auto.bind('<Return>', Autom)
    btn_marvel.bind('<Return>', Marvel)
    btn_dawg.bind('<Return>', Dawg)
    btn_quit.bind('<Return>', HQuit)

def ShowHangForm():
    global hangform
    hangform = Toplevel()
    hangform.title("PROMETHEUS/HangMan")
    width = 600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    hangform.resizable(0, 0)
    hangform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    HangForm()

def HangForm():
    global lbl_res,lbl_word,SWORD
    TopHangForm = Frame(hangform, width=600, height=100, bd=1, relief=SOLID)
    TopHangForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopHangForm, text="HangMan", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidHangForm = Frame(hangform, width=600)
    MidHangForm.pack(side=TOP, pady=50)
    lbl_Letter= Label(MidHangForm, text="Please enter a letter:", font=('arial', 25), bd=18)
    lbl_Letter.grid(row=0)
    Letter = Entry(MidHangForm, textvariable=HANG, font=('arial', 25), width=15)
    Letter.grid(row=0, column=1)
    lbl_word = Label(MidHangForm, text=SWORD, font=('arial', 18))
    lbl_word.grid(row=3, columnspan=2)
    lbl_res = Label(MidHangForm, text="", font=('arial', 18))
    lbl_res.grid(row=5, columnspan=2)
    Sbt = Button (MidHangForm, text="SUBMIT", font=('arial', 18), width=30, command=Submit)
    Sbt.grid(row=4, columnspan=2)
    Sbt.bind("<Return>", Submit)

def chk (a,b,c=0):
    
    if ( c < len(b)):
        if (b[c].isspace() == False):
            if ( b[c].lower() not in a ):
                return False
            else:
                return chk (a,b,c+1)
        else:
            return chk (a,b,c+1)
    else:
        return True
    
def Submit(event=None):

    global incorrect
    a=HANG.get().lower()
    LIST.append(a)
    incorrect=ILIST[len(ILIST)-1]
    lbl_res.config(text="")
    k=list(word)
    if ( chk(LIST,k) == False):
        if a == "" or a == " " :
            lbl_res.config(text="Please complete the required field!", fg="red")
            HANG.set("")
        else:
            HANG.set("")
            SWORD = ""
            if a in word.lower():
                for j in word :
                    if ( j.isspace() == True ):
                        SWORD +=" "
                    else:
                        SWORD +="*"
                wl=list(SWORD)
                l=len(word)
                for i in range (l):
                    z=word[i]
                    for k in LIST:
                        if (z.lower() == k):
                            wl[i] = z
                SWORD = "".join(wl)
                lbl_word.config(text=SWORD)
                
            else:
                incorrect+=1
                ILIST.append(incorrect)
                lbl_res.config(text="Letter is not a part of the word", fg="red")
                DrawHangMan(incorrect)
                HANG.set("")
    else:
        HANG.set("")
        ShowEHangForm()

def Anime():
    global word,SWORD
    SWORD=""
    mhangform.destroy()
    Database()
    cursor.execute("SELECT name FROM Anime where S_no=%i" % (randint(1,20)))
    a=cursor.fetchall()
    for i in a :
        word=i[0]
        for j in word :
            if (j.isspace() == True ):
                SWORD +=" "
            else:
                SWORD +="*"
        ShowHangForm()
        DrawGallow()
        
def Autom():    
    global word,SWORD
    SWORD=""
    mhangform.destroy()
    Database()
    cursor.execute("SELECT name FROM Auto where S_no=%i" % (randint(1,20)))
    a=cursor.fetchall()
    for i in a :
        word=i[0]
        for j in word :
            if (j.isspace() == True ):
                SWORD +=" "
            else:
                SWORD +="*"
        ShowHangForm()
        DrawGallow()
        
def Marvel():
    global word,SWORD
    SWORD=""
    mhangform.destroy()
    Database()
    cursor.execute("SELECT name FROM Marvel where S_no=%i" % (randint(1,20)))
    a=cursor.fetchall()
    for i in a :
        word=i[0]
        for j in word :
            if (j.isspace() == True ):
                SWORD +=" "
            else:
                SWORD +="*"
        ShowHangForm()
        DrawGallow()

def Dawg():
    global word,SWORD
    SWORD=""
    mhangform.destroy()
    Database()
    cursor.execute("SELECT name FROM Dawg where S_no=%i" % (randint(1,17)))
    a=cursor.fetchall()
    for i in a :
        word=i[0]
        for j in word :
            if (j.isspace() == True ):
                SWORD +=" "
            else:
                SWORD +="*"
        ShowHangForm()
        DrawGallow()

def HQuit():
    result = tkMessageBox.askquestion('Snake', 'Do you want to exit?', icon="warning")
    if result == 'yes':
        mhangform.destroy()

def DrawGallow():
    global t
    t =Turtle()
    t.pu()
    t.setx(-250)
    t.sety(80)
    t.pd()
    t.speed(50)
    t.fd(100)
    t.rt(180)
    t.fd(50)
    t.rt(90)
    t.fd(170)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.ht()

def DrawHangMan(incorrect):
    if incorrect == 1:
      t.pu()
      t.setx(-120)
      t.sety(180)
      t.pd()
      t.circle(20)
      t.ht()
    elif incorrect == 2:
      t.pu()
      t.setx(-100)
      t.sety(160)
      t.pd()
      t.fd(50)
      t.ht()
    elif incorrect == 3:
      t.rt(45)
      t.fd(30)
      t.ht()
    elif incorrect == 4:
      t.pu()
      t.rt(-90)
      t.setx(-100)
      t.sety(110)
      t.pd()
      t.fd(30)
      t.ht()
    elif incorrect == 5:
      t.pu()
      t.rt(-45)
      t.setx(-100)
      t.sety(135)
      t.pd()
      t.fd(30)
      t.ht()
    elif incorrect == 6:
      t.pu()
      t.rt(180)
      t.setx(-100)
      t.sety(135)
      t.pd()
      t.fd(30)
      t.pu()
      t.ht()
      ShowNHangForm()

def ShowEHangForm():    
    global ehangform
    hangform.destroy()
    t.clear()
    ehangform = Toplevel()
    ehangform.title("PROMETHEUS/Score Entry Form (HangMan)")
    width = 600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    ehangform.resizable(0, 0)
    ehangform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    EndHangForm()
    
def EndHangForm():
    TopEHangForm = Frame(ehangform, width=600, height=100, bd=1, relief=SOLID)
    TopEHangForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopEHangForm, text="Score Card", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidEHangForm = Frame(ehangform, width=600)
    MidEHangForm.pack(side=TOP, pady=50)
    lbl_name = Label(MidEHangForm, text="Player Name:", font=('arial', 25), bd=18)
    lbl_name.grid(row=2)
    lbl_FScore = Label(MidEHangForm, text="SCORE :", font=('arial', 25), bd=18)
    lbl_FScore.grid(row=0)
    lbl_Score = Label(MidEHangForm, text=str(incorrect), font=('arial', 25), bd=18)
    lbl_Score.grid(row=0, column=1)
    username = Entry(MidEHangForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=2, column=1)
    btn_entry = Button(MidEHangForm, text="Enter", font=('arial', 18), width=30, command=EEntrye)
    btn_retry = Button(MidEHangForm, text="Retry", font=('arial', 18), width=30, command=HRetry)
    btn_quit = Button(MidEHangForm, text="Quit Game", font=('arial', 18), width=30, command=EQuit)
    btn_entry.grid(row=3, columnspan=2, pady=20)
    btn_retry.grid(row=4, columnspan=2, pady=20)
    btn_quit.grid(row=5, columnspan=2, pady=20)
    btn_entry.bind('<Return>', EEntrye)
    btn_retry.bind('<Return>', HRetry)
    btn_quit.bind('<Return>', EQuit)

def ShowNHangForm():    
    global nhangform
    hangform.destroy()
    t.clear()
    nhangform = Toplevel()
    nhangform.title("PROMETHEUS/GAME OVER (HangMan)")
    width = 600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    nhangform.resizable(0, 0)
    nhangform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    NoHangForm()
    
def NoHangForm():
    TopNHangForm = Frame(nhangform, width=600, height=100, bd=1, relief=SOLID)
    TopNHangForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopNHangForm, text="Score Card", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidNHangForm = Frame(nhangform, width=600)
    MidNHangForm.pack(side=TOP, pady=50)
    lbl_end = Label(MidNHangForm, text="GAME OVER", font=('arial', 25), bd=18)
    lbl_end.grid(row=0)
    btn_retry = Button(MidNHangForm, text="Retry", font=('arial', 18), width=30, command=NRetry)
    btn_quit = Button(MidNHangForm, text="Quit Game", font=('arial', 18), width=30, command=NQuit)
    btn_retry.grid(row=1, columnspan=2, pady=20)
    btn_quit.grid(row=2, columnspan=2, pady=20)
    btn_retry.bind('<Return>', NRetry)
    btn_quit.bind('<Return>', NQuit)

def HRetry():
    ehangform.destroy()
    ShowMainHang()
    del LIST[:len(LIST)]
    del ILIST[:len(ILIST)]
    ILIST.append(0)
    
def EEntrye():
    Database()
    cursor.execute("INSERT INTO `HHighscores` (score, account) VALUES(%i,'%s')" % (incorrect,USERNAME.get()))
    USERNAME.set("")
    conn.commit()
    cursor.close()
    conn.close()
    result = tkMessageBox.askquestion('PROMETHEUS', 'Do you want to retry the game ?', icon="warning")
    if result == 'yes':
        ehangform.destroy()
        ShowMainHang()
        del LIST[:len(LIST)]
        del ILIST[:len(ILIST)]
        ILIST.append(0)
    elif result == 'no':
        del LIST[:len(LIST)]
        del ILIST[:len(ILIST)]
        ILIST.append(0)
        ehangform.destroy()
        bye()

def EQuit():
    result = tkMessageBox.askquestion('Hangman', 'Do you want to exit?', icon="warning")
    if result == 'yes':
        del LIST[:len(LIST)]
        del ILIST[:len(ILIST)]
        ILIST.append(0)
        bye()
        ehangform.destroy()

def NRetry():
    nhangform.destroy()
    ShowMainHang()
    del LIST[:len(LIST)]
    del ILIST[:len(ILIST)]
    ILIST.append(0)

def NQuit():
    result = tkMessageBox.askquestion('Hangman', 'Do you want to exit?', icon="warning")
    if result == 'yes':
        del LIST[:len(LIST)]
        del ILIST[:len(ILIST)]
        ILIST.append(0)
        bye()
        nhangform.destroy()

def Logout():
    result = tkMessageBox.askquestion('PROMETHEUS', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        home.withdraw()
  
def Login(event=None):
    
    global admin_id
    Database()
    if (USERNAME.get() == "") or (PASSWORD.get() == "") :
        ShowHome()
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM admin WHERE username = '%s' AND password = '%s'" % (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM admin WHERE username = '%s' AND password = '%s'" % (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


#========================================MENUBAR WIDGETS================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="PROMETHEUS", font=('arial', 45))
lbl_display.pack()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()

