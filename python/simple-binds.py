# File: simple-binds.py (Oct 2012)

# learning from the Tkinter tutorial for python .. 

from Tkinter import *

root = Tk()

global lastconnect , lastclick

lastconnect = [ ] 
lastclick = [ ] 

def clickCallback(event):
	global lastclick
	lastclick = [ event.x, event.y ]
	print "clicked at", event.x, event.y 

def dragCallback(event):
	global lastconnect
	lastconnect = [ event.x, event.y ]
	print "connecting at", event.x, event.y 

def doConnect (event):
	global lastconnect, lastclick
	print "xy " , event.x, event.y
	# If current event's x,y is not the same as lastclick then this isn't a "drag & drop" but a single click
	if [ event.x, event.y ] != lastclick:
		print "Connecting %s -> %s" % ( lastconnect , lastclick)
	

frame = Frame(root, width=400, height=400)
frame.bind("<B1-Motion>", dragCallback)
frame.bind("<Button-1>", clickCallback)
frame.bind("<ButtonRelease-1>", doConnect)
frame.pack()

root.mainloop()

