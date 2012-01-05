#coding: utf-8

import gtk 
import webkit 

def start_event_loop(url,
    title=None,
    size=None):        
    view = webkit.WebView() 
    
    sw = gtk.ScrolledWindow() 
    sw.add(view) 
    
    win = gtk.Window(gtk.WINDOW_TOPLEVEL) 
    win.add(sw) 
    
    if title:
        win.set_title(title)
    if size:
        if 0 <= size[0] <= 1 and 0 <= size[1] <= 1:
            screen = win.get_screen()
            size = (int(size[0] * screen.get_width()), int(size[1] * screen.get_height()))
        win.set_size_request(*size)
    
    win.connect("destroy", lambda w: gtk.main_quit())    
    win.show_all()
    view.open(url)
    gtk.main()

def error_dialog(message):
    dialog = gtk.MessageDialog(None,
        flags = gtk.DIALOG_MODAL,
        type = gtk.MESSAGE_ERROR,
        buttons = gtk.BUTTONS_CLOSE,
        message_format = message)
    dialog.run()
    dialog.destroy()
