import time
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
#gives width and height of our main screen
stream=cv2.VideoCapture("runout.mp4")
flag=True
def play(speed):
    global flag
    print(f"you clicked on play.Speed is {speed}")

    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(140,24,fill="red",font="Times 20 italic bold",text="DECISION PENDING")
    flag= not flag


def pending(decision):
    frame=cv2.cvtColor(cv2.imread("te.jpg"),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    time.sleep(1)
    frame = cv2.cvtColor(cv2.imread("coke.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(1)
    if decision=="out":
        decisionimg="o.jpg"
    elif decision=="notout":
        decisionimg="not.png"
    frame = cv2.cvtColor(cv2.imread(decisionimg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)



    pass
def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("player is out")

def notout():
    thread = threading.Thread(target=pending, args=("notout",))
    thread.daemon = 1
    thread.start()
    print("player is not out")


SET_WIDTH=650
SET_HEIGHT=368

# tkinter starts here
window=tkinter.Tk()
window.title("codewithsuvan third umpire decision review kit")
cv_image=cv2.cvtColor(cv2.imread("nwz.jpg"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


# buttons to cotrol

btn=tkinter.Button(window,text="<< Previous(fast)",width=50,command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<< Previous(slow)",width=50,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text=" Next(slow)>>",width=50,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text=" Next(fast)>>",width=50,command=partial(play,25))
btn.pack()
btn=tkinter.Button(window,text=" GIVE OUT",width=50,command=lambda:out())
btn.pack()
btn=tkinter.Button(window,text="GIVE NOTOUT",width=50,command=lambda:notout())
btn.pack()




window.mainloop()
1
