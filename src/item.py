class Item:
    def __init__(self, name, description, adjective="simple"):
        self.name = name
        self.description = description
        self.adjectives = adjective

    def on_take(self):
        print(
            f'Acquired {self.name}, You have picked up {self.name} - {self.description}')

    def on_drop(self):
        print(f'Rid of {self.name} from inventory')


class Treasure(Item):
    def __init__(self, name, description, adjective):
        super().__init__(name, description, adjective)


class LightSource(Item):
    def __init__(self, name, description, adjective):
        super().__init__(name, description, adjective)

    def on_drop(self):
      print("\nIt's not wise to drop your source of light - the darkness lingers")
