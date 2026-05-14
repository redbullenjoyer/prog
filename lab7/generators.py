class RepeatApplyGenerator:
    def __init__(self, sequence, func, times):
        self.sequence = sequence
        self.func = func
        self.times = times
        self.index = 0
        self.current_element = None
        self.apply_count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.index >= len(self.sequence):
                raise StopIteration
            
            if self.current_element is None:
                self.current_element = self.sequence[self.index]
                self.apply_count = 0
            
            if self.apply_count < self.times:
                self.current_element = self.func(self.current_element)
                self.apply_count += 1
                return self.current_element
            else:
                self.index += 1
                self.current_element = None


class SquareGenerator(RepeatApplyGenerator):
    def __init__(self, sequence):
        super().__init__(sequence, self.square, 2)
    
    @staticmethod
    def square(x):
        return x ** 2