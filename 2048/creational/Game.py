from tkinter import messagebox
<<<<<<< HEAD
=======

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
class Game:
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False
<<<<<<< HEAD
=======

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
    def start(self):
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()
<<<<<<< HEAD
    def link_keys(self,event):
        if self.end or self.won:
            return
        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False
        presed_key=event.keysym
=======
    
    def link_keys(self,event):
        if self.end or self.won:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False

        presed_key=event.keysym

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
        if presed_key=='Up':
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()
<<<<<<< HEAD
=======

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
        elif presed_key=='Down':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()
<<<<<<< HEAD
=======

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
        elif presed_key=='Left':
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
<<<<<<< HEAD
=======

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
        elif presed_key=='Right':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
        else:
            pass
<<<<<<< HEAD
        self.gamepanel.paintGrid()
=======

        self.gamepanel.paintGrid()

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
        flag=0
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break
<<<<<<< HEAD
        if(flag==1): #found 2048
            self.won=True
            messagebox.showinfo('2048', message='You Won!')
            return
=======

        if(flag==1): #found 2048
            self.won=True
            messagebox.showinfo('2048', message='You Wonnn!!')
            
            return

>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break
<<<<<<< HEAD
        if not (flag or self.gamepanel.can_merge()):
            self.end=True
            messagebox.showinfo('2048','Game Over!!!')
        if self.gamepanel.moved:
            self.gamepanel.random_cell()      
        self.gamepanel.paintGrid()
=======

        if not (flag or self.gamepanel.can_merge()):
            self.end=True
            messagebox.showinfo('2048','Game Over!!!')
            

        if self.gamepanel.moved:
            self.gamepanel.random_cell()
        
        self.gamepanel.paintGrid()
    
>>>>>>> 25bd3471e57fe338fc60f32fe1fd5553da7ca86b
