class Simplon:
    def __init__(self, threshold, cooldown):
        self.connections_in = []
        self.connections_out = []
        self.threshold = 1
        self.cooldown = 1

        self.potential = 0
        self.temp = 0

    def tick(self):
        if self.potential > self.threshold:
            for neuron in self.connections_out:
                neuron.temp += 1
    
    def update(self):
        