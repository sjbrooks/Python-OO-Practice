"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 100):
        "Initialize with a start number"
        self.start = start
        self.current_serial = start - 1
    
    def generate(self):
        "Return the next sequential serial"
        self.current_serial = self.current_serial + 1
        return self.current_serial

    def reset(self):
        "Resets value of serial to starting number"
        self.current_serial = self.start - 1

