class BolaHelado:
    def __init__(self, color, sabor):
        self.color = color
        self.sabor = sabor

    def comer(self):
        print("Delicioso Helado de color", self.color, "sabor a", self.sabor)