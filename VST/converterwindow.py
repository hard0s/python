from tkinter import *
from structural.adapter import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Converter")
        self.geometry("640x420")

        self.button = Button(self, text="Midi", command=self.midi)
        self.button.pack(expand=True)

        self.button = Button(self, text="Audio", command=self.audio)
        self.button.pack(expand=True)


        def audio(self):
            track = AudioTrack()
            track.audioTrack()

        def midi(self):
            track = AudioToMidi()
            track.audioRecord()