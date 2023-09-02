class ItemDeLista:
    def __init__(self):
        self.Nombre=None
        self.Imagen=None
        self.Descripcion=None
        self.id=None
        self.indice=0
    def acortarDescricion(self):
        max=40
        if len(self.Descripcion)>max:
            self.Descripcion=self.Descripcion[:max]+"..."