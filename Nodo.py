class Nodo:
    def __init__(self, label):
        self.left = None
        self.right = None
        self.label = label

    def isEmpty(self):
        return self.left is None and self.right is None
