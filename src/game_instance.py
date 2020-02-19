from item import Item, LightSource
from room import Room

item = {
    'key': Item('key', 'A reqular key covered in dried blood'),
    'dagger':   Item('dagger', 'A dull dagger that has a cloth wrapped around its handle'),
    'orb':  Item('orb', 'A darken orb with a hole in it'),
    'shard':  Item('shard', 'A shard of multicolored glass'),
    'marble':  Item('marble', 'A small glass marble with a red and orange swirls'),
    'chalice':  Item('chalice', 'A golden chalice with jewels encrusted'),
    'journal':  Item('journal', 'A leather bound journal - a ripped out paper slips out as you open it: "A flame will marry glass to their dark cage to to illuminate the path to eternity"'),
    'lamp':  LightSource('lamp', 'A silver oil lamp with only a small amount of oil left', "shiny"),
    'glow_orb': Item('orb', 'An orb that is illuminated with a warm orange', "glowing")
}


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['marble'], item['lamp'], item['shard']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['key']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['journal']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['orb']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
    'coffin': Room("Child's Coffin", """A soft wind breezes by with a faint whisper of your name,
    dusty and half burnt children toys spread over the floor \na coffin with a well on the cover, looks like you can pour something into it""", [item['dagger']]),
    'throne': Room("Throne Room", """Cold stone floors with a high cieling surrounds a throne in
    the long room - a faded ripped potrait hands behind the throne. It looks like a family with
    only the small eyes on a child's face is recognizable""", [item['chalice']]),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['narrow'].e_to = room['coffin']
room['narrow'].s_to = room['throne']
room['coffin'].w_to = room['narrow']
room['throne'].n_to = room['narrow']