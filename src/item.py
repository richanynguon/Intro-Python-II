class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
      print(f'Acquired {self.name}, You have picked up {self.name} - {self.description}')
    def on_drop(self):
      print(f'Rid of {self.name} from inventory')
