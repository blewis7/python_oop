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

    def __init__(self, start=0):
        self.start = self.next = start
    
    def __repr__(self):
        '''Represents the starting point of the serial generator'''
        return f"start = {self.start} next = {self.next}"
    
    def generate(self):
        '''Takes the current serial number and adds 1 to it'''
        self.next += 1
        return self.next - 1
    
    def reset(self):
        '''Reset the value of next to start'''
        self.next = self.start


