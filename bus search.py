from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('{}x{}'.format(1000, 600))

list_img = [imgblank , imgptt, imgtpi, imgprom, imgprom, imgprawet, imgivory/
            imgcon, imgphoe, imgkriss, imgkmitl, imglad, imgjura,/
            imgpaseo, imgpark, imgpolice, imgmanage, imgmail, imgtax,/
            imgtemp, imgmarket, imgtrain]

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
imgTemp = ImageTk.PhotoImage(Image.open(FileTemp))

FileMarket = '019.png'
imgmarket = ImageTk.PhotoImage(Image.open(FileMarket))

FileTrain = '020.png'
imgtrain = ImageTk.PhotoImage(Image.open(FileTrain))

def pop_img():
    topimg = Toplevel()

    tempframe = Frame(topimg)
    tempcanvas = Canvas(tempframe, height=404, width=404)

    tempcanvas.create_image(0,0,image=tempimg,anchor='nw')
    
    tempcanvas.pack()
    tempframe.pack()

def topplace():
    top = Toplevel()
    top.title('List of Places')

    ptt = Button(top, text='Lat Krabang Bangkok Hospital', command=lambda x = )
    ptt.pack()

    tpi = Button(top, text='Lat Krabang Bangkok Hospital', command=lambda x = )
    tpi.pack()

    prom = Button(top, text='Lat Krabang Bangkok Hospital', command=lambda x = )
    prom.pack()

    prawet = Button(top, text='Lat Krabang Bangkok Hospital', command=lambda x = )
    prawet.pack()

    hospit = Button(top, text='Lat Krabang Bangkok Hospital', command=lambda x = )    
    hospit.pack()
    
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
