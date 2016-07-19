import pyttsx, thread, unicodedata
import Tkinter as tk
from sys import exit

# A function to update the text box. I will run it in a new thread
# because it would be faster that way and will not delay the
# pyttsx engine to speak next line.
def update(new):
    global w
    w.insert(1.0, new)      # Adds new thing to the beginning.
                                      # You can use tk.END to add to end.
    root.update_idletasks()

# A funtion to open the file, send each line to update and speak it
def speak():
    global start, engine
    start['state']='disabled'
    text= open("text.txt")
    for line in text:
        #line=unicode(line)      # Converting to unicode
        #line = unicodedata.normalize('NFKD', line).encode('ascii','ignore')   # Converting to ASCII correctly.
        thread.start_new(update, (line,))
        engine.say(line, name=line)
        engine.runAndWait()

# A function to exit everything. It's fucked up by the way.
# Doesn't work for some unknown reasons.
def finish():
    global engine, root
    engine.stop()
    root.destroy()
    exit()

# Setting up pyttsx engine
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+0)      # Change the rate from here
# Uncomment the below two lines to change to a female voice.
#hazel="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_10.0"
#engine.setProperty('voice', hazel)

# For Tkinter
root = tk.Tk()
root.title("Listen my dear")

# Let's make the buttons
start = tk.Button(text='Start', command=speak)
start.pack()
stop = tk.Button(text='Exit', command=finish)
stop.pack()

# Setting up the text frame to display the lines
frameLabel = tk.Frame( root, padx=20, pady=20 )
frameLabel.pack()
w = tk.Text( frameLabel, wrap='word', font='Arial 12 italic' )
w.insert( 1.0, "Welcome! Click on start to begin." )
w.pack()
w.configure( bg=root.cget('bg'), relief='flat' )

root.mainloop()     # ...Finally! :-)
