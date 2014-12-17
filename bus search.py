from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('{}x{}'.format(1000, 600))

FilePtt = '001.png'
imgptt = ImageTk.PhotoImage(Image.open(FilePtt))

FileTpi = '002.png'
imgtpi = ImageTk.PhotoImage(Image.open(FileTpi))

FileProm = '003.png'
imgprom = ImageTk.PhotoImage(Image.open(FileProm))

FilePrawet = '004.png'
imgprawet = ImageTk.PhotoImage(Image.open(FilePrawet))

FileIvory = '005.png'
imgivory = ImageTk.PhotoImage(Image.open(FileIvory))

FileCon = '006.png'
imgcon = ImageTk.PhotoImage(Image.open(FileCon))

FilePhoe = '007.png'
imgphoe = ImageTk.PhotoImage(Image.open(FilePhoe))

FileKriss = '008.png'
imgkriss = ImageTk.PhotoImage(Image.open(FileKriss))

FileKmitl = '009.png'
imgkmitl = ImageTk.PhotoImage(Image.open(FileKmitl))

FileLad = '010.png'
imglad = ImageTk.PhotoImage(Image.open(FileLad))

FileJura = '011.png'
imgjura = ImageTk.PhotoImage(Image.open(FileJura))

FilePaseo = '012.png'
imgpaseo = ImageTk.PhotoImage(Image.open(FilePaseo))

FilePark = '013.png'
imgpark = ImageTk.PhotoImage(Image.open(FilePark))

FilePolice = '014.png'
imgpolice = ImageTk.PhotoImage(Image.open(FilePolice))

FileManage = '015.png'
imgmanage = ImageTk.PhotoImage(Image.open(FileManage))

FileMail = '016.png'
imgmail = ImageTk.PhotoImage(Image.open(FileMail))

FileTax = '017.png'
imgtax = ImageTk.PhotoImage(Image.open(FileTax))

FileTemp = '018.png'
imgtemp = ImageTk.PhotoImage(Image.open(FileTemp))

FileMarket = '019.png'
imgmarket = ImageTk.PhotoImage(Image.open(FileMarket))

FileTrain = '020.png'
imgtrain = ImageTk.PhotoImage(Image.open(FileTrain))

list_img = ['imgblank' , imgptt, imgtpi, imgprom, imgprawet, imgivory,\
            imgcon, imgphoe, imgkriss, imgkmitl, imglad, imgjura,\
            imgpaseo, imgpark, imgpolice, imgmanage, imgmail, imgtax,\
            imgtemp, imgmarket, imgtrain]

list_text = ['Do you want to set this place as your starting point?', \
             'Do you want to set this place as your destination?']

dict_bus = {1013:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],\
            553:[1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19],\
            517:[1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19],\
            92:[20,1,2,5,12,3,4,6],550:[7,8,14,1,2,5,12,3,4,6]}}

collect = 0
def increase(delete):
    global collect
    collect += 1

    delete.destroy()

def pop_img(num):
    topimg = Toplevel()

    tempframe = Frame(topimg)
    tempcanvas = Canvas(tempframe, height=410, width=410)

    tempcanvas.create_image(0,0,image=list_img[num],anchor='nw')
    
    tempcanvas.pack()
    tempframe.pack()

    global collect
    if collect < 2:
        yes = Button(topimg, text='Confirm', command=lambda x = topimg: increase(topimg))
        no = Button(topimg, text='Cancel', command=topimg.destroy)
        ask = Message(topimg, text=list_text[collect])

        ask.pack()
        yes.pack(side=LEFT, ipadx=50)
        no.pack(side=RIGHT, ipadx=50)
    else:
        nope = Message(topimg, text=\
                       'You have already selected starting and destination point!?')
        no = Button(topimg, text='Cancel', command=topimg.destroy)
        nope.pack()
        no.pack(ipadx=50)

def topplace():
    top = Toplevel()
    top.title('List of Places')

    ptt = Button(top, text='PTT NGV Gas Station', command=lambda x = 1: pop_img(x))
    ptt.pack()

    tpi = Button(top, text='TPI Oil Station', command=lambda x = 2: pop_img(x))
    tpi.pack()

    prom = Button(top, text='Prom School', command=lambda x = 3: pop_img(x))
    prom.pack()

    prawet = Button(top, text='Prawet Pitthayakarn School', command=lambda x = 4: pop_img(x))
    prawet.pack()

    ivory = Button(top, text='Ivory Bangkok Hotel', command=lambda x = 5: pop_img(x))
    ivory.pack()

    con = Button(top, text='Convenient Resort Hotel', command=lambda x = 6: pop_img(x))
    con.pack()

    phoe = Button(top, text='Phoenix hotel Bangkok', command=lambda x = 7: pop_img(x))
    phoe.pack()

    kriss = Button(top, text='Kriss Residence Hotel', command=lambda x = 8: pop_img(x))
    kriss.pack()

    kmitl = Button(top, text='King Mongkut Institute of Technology Ladkrabang', command=lambda x = 9: pop_img(x))
    kmitl.pack()

    lad = Button(top, text='Lad Krabang Bangkok Hospital', command=lambda x = 10: pop_img(x))
    lad.pack()

    jura = Button(top, text='Jurarat 8 Hospital', command=lambda x = 11: pop_img(x))
    jura.pack()

    paseo = Button(top, text='The Paseo Lad Krabang', command=lambda x = 12: pop_img(x))
    paseo.pack()

    park = Button(top, text='Pranakorn Park', command=lambda x = 13: pop_img(x))
    park.pack()

    police = Button(top, text='Lad Krabang Police Station', command=lambda x = 14: pop_img(x))
    police.pack()

    manage = Button(top, text='Lad Krabang District Office', command=lambda x = 15: pop_img(x))
    manage.pack()

    mail = Button(top, text='Lad Krabang Post Office', command=lambda x = 16: pop_img(x))
    mail.pack()

    tax = Button(top, text='Lad Krabang Area Revenue Branch Office', command=lambda x = 17: pop_img(x))
    tax.pack()

    temp = Button(top, text='Wat Sam', command=lambda x = 18: pop_img(x))
    temp.pack()

    market = Button(top, text='Suwannabhumi Market', command=lambda x = 19: pop_img(x))
    market.pack()

    train = Button(top, text='Airport Rail Link & Train Station Lad Krabang', command=lambda x = 20: pop_img(x))
    train.pack()
    
menubar = Menu(root)
menubar.add_command(label="Quit!", command=root.quit)

root.config(menu=menubar)

frame = Frame(root,width=2900,height=600,bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=100)
frame.grid_columnconfigure(0, weight=100)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

canvas = Canvas(frame, bd=0, width=2900, height=600, xscrollcommand=xscrollbar.set)
canvas.grid(row=0, column=0, sticky=E+W)

FileMap = 'home.png'
img = ImageTk.PhotoImage(Image.open(FileMap))
canvas.create_image(0,0,image=img,anchor='nw')

xscrollbar.config(command=canvas.xview)
canvas.config(scrollregion=canvas.bbox(ALL))

frame.pack()

FileList = 'p list.png'
imglist = ImageTk.PhotoImage(Image.open(FileList))

listing = Button(root, image=imglist, command=topplace)
listing.place(x=25, y=25)

mainloop()
