from tkinter import *
import sys
sys.path.insert(0,'P:/PlanetsideSoftware/RPC/terragen_rpc-0.9.0/terragen_rpc-0.9.0')
import terragen_rpc as tg

gui = Tk()
gui.title("TG_Sunlight01_HeadingElevation")
gui.geometry("450x300")

gui.grid_rowconfigure(0,weight=1)
gui.grid_columnconfigure(0,weight=1)

frame1 = LabelFrame(gui,text="Set Sunlight01 heading in degrees ",padx=37,pady=10)
frame2 = LabelFrame(gui,text="Offset XZ clipboard coordinates with Transform shader node",padx=5,pady=5)
frame3 = LabelFrame(gui,relief=FLAT,bg="#FFF9EC") # Errors and messages

frame1.grid(row=1,column = 0,padx=5)
frame2.grid(row=3,column = 0,padx=5)
frame3.grid(row=4,column = 0,columnspan=4,sticky='nsew')

def rpc_sun_heading(heading):
    try:
        project = tg.root()
        node = tg.node_by_path('/Sunlight 01')    
        node.set_param('heading',str(heading))
        rpc_error.set(False)
    except ConnectionError as e:
        formatted_error_message = format_message("Terragen RPC connection error: " + str(e))
        #show_error("Terragen RPC connection error: " + str(e))
        show_error(formatted_error_message)
        rpc_error.set(True)
        show_message(" ")
    except TimeoutError as e:
        show_error("Terragen RPC timeout error: " + str(e))
        rpc_error.set(True)
    except tg.ReplyError as e:
        show_error("Terragen RPC server reply error: " + str(e))
        rpc_error.set(True)
    except tg.ApiError:
        show_error("Terragen RPC API error")
        rpc_error.set(True)
        raise

def rpc_sun_elevation(elevation):
    try:
        project = tg.root()
        node = tg.node_by_path('/Sunlight 01')    
        node.set_param('elevation',str(elevation))
        rpc_error.set(False)
    except ConnectionError as e:
        formatted_error_message = format_message("Terragen RPC connection error: " + str(e))
        # show_error("Terragen RPC connection error: " + str(e))
        show_error(formatted_error_message)
        rpc_error.set(True)
        show_message(" ")
    except TimeoutError as e:
        show_error("Terragen RPC timeout error: " + str(e))
        rpc_error.set(True)
    except tg.ReplyError as e:
        show_error("Terragen RPC server reply error: " + str(e))
        rpc_error.set(True)
    except tg.ApiError:
        show_error("Terragen RPC API error")
        rpc_error.set(True)
        raise

def set_sun_heading(heading):
    # print("heading is ",heading)
    rpc_sun_heading(heading)
    if rpc_error.get() == False:
        info_message.set("Sunlight 01 heading set to "+ str(heading))
        error_message.set(" ")

def set_sun_elevation():
    rpc_sun_elevation(sun_elevation.get())
    if rpc_error.get() == False:
        info_message.set("Sunlight 01 elevation set to " + str(sun_elevation.get()))
        error_message.set(" ")

def show_error(text):    
    error_message.set(text)

def show_message(text):
    info_message.set(text)

# Splits a very long error message across two lines of the label widget
def format_message(text):    
    formatted_text = text    
    if len(text) >= 80:
        n = int(len(text) / 2)
        formatted_text = text[:n] + " \n" + text[n:]    
    return(formatted_text)

# Variables
error_message = StringVar()
info_message = StringVar()
rpc_error = BooleanVar(gui,False)
sun_elevation = IntVar()


# Set sunlight heading section -----
button1 = Button(frame1,text="0",command=lambda: set_sun_heading(0)).grid(row=0,column=0,padx=10,pady=5)
button2 = Button(frame1,text="45",command=lambda: set_sun_heading(45)).grid(row=0,column=1,padx=10,pady=5)
button3 = Button(frame1,text="60",command=lambda: set_sun_heading(60)).grid(row=0,column=2,padx=10,pady=5)
button4 = Button(frame1,text="90",command=lambda: set_sun_heading(90)).grid(row=0,column=3,padx=10,pady=5)
button5 = Button(frame1,text="130",bg='cyan',command=lambda: set_sun_heading(130)).grid(row=0,column=4,padx=10,pady=5)
button6 = Button(frame1,text="180",command=lambda: set_sun_heading(180)).grid(row=0,column=5,padx=10,pady=5)
button7 = Button(frame1,text="270",command=lambda: set_sun_heading(270)).grid(row=0,column=6,padx=10,pady=5)
button8 = Button(frame1,text="300",command=lambda: set_sun_heading(300)).grid(row=0,column=7,padx=10,pady=5)
# new_line = Label(frame1,text=" ").grid(row=1,column=0)

# Set sunlight elevation section -----
slider1 = Scale(frame2,from_= -90, to = 90, variable=sun_elevation,orient=HORIZONTAL,showvalue=0,length=360).grid(row=0,column=0,padx=10,pady=5)
e1 = Entry(frame2,textvariable=sun_elevation,width=6).grid(row=0,column=1)
button9 = Button(frame2,text="Apply Elevation",bg='yellow',command=set_sun_elevation).grid(row=1,column=0,padx=5,pady=5)

# Message section -----
label3 = Label(frame3,text="Error messages: ",bg="#FFF9EC").grid(row=0,column=0,pady=5,sticky='w')
Label4 = Label(frame3,textvariable=error_message,fg='red',bg="#FFF9EC").grid(row=1,column=0,stick='w',)
Label5 = Label (frame3,text="Info messages: ",bg="#FFF9EC").grid(row=2,column=0,pady=5,sticky='w')
Label6 = Label(frame3,textvariable=info_message,bg="#FFF9EC").grid(row=3,column=0,pady=5,sticky='w')



gui.mainloop()
