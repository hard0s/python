from mainwindow import Window

if __name__ == '__main__':
    handle = Window()
    handle.title('Daw')
    handle.geometry('1280x720')
    
    handle2 = Window()
    handle2.title('Daw2')
    handle2.geometry('1280x720')
    

    handle3 = Window()
    handle3.title('Daw3')
    handle3.geometry('1280x720')

    handle.mainloop()
    handle2.mainloop()
    handle3.mainloop()