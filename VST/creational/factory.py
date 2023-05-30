class EQsFactory: # Абстрактная фабрика эквалайзеров
    def __init__(self):
        self._eqsfactory = [FabFilter(5, "Pro Q"), UAD(4, "UAD"), Waves(10, "Waves")]

    @property
    def eqs(self):
        return self._eqsfactory

class GuitarsFactory: # Абстрактная фабрика эквалайзеров
    def __init__(self):
        self._guitarsfactory = [ToneLib(5, "ToneLib"), GuitarRIG(4, "GuitarRIG")]

    @property
    def guitars(self):
        return self._guitarsfactory

class EQ:
    def __init__(self, bands, name):
        self.bands = bands
        self.name = name

    def getBands(self):
        return self.bands
class FabFilter(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()
class Waves(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()
class UAD(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()   
     
class Guitar:
    def __init__(self, bands, name):
        self.bands = bands
        self.name = name

    def getBands(self):
        return self.bands
class ToneLib(Guitar):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()
class GuitarRIG(Guitar):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()