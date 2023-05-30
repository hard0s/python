from abc import ABC, abstractmethod

class Audio(ABC):
    @abstractmethod
    def audioRecord(self):
        pass

class MIDI(ABC):
    @abstractmethod
    def midiTrack(self):
        pass

class MIDITrack(MIDI):
    @abstractmethod
    def midiTrack(self):
        print("midiTrack")

class AudioTrack(Audio):
    @abstractmethod
    def audioTrack(self):
        print("audioTrack")

class AudioToMidi(Audio):
    def __init__(self):
        self.midi = MIDITrack()

    def audioRecord(self):
        self.midi.midiTrack()