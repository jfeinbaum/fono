
class Fon:
    def __init__(self, id, ipa, parent_id=None, x=None, y=None):
        self.id = id
        self.ipa = ipa
        self.parent_id = parent_id
        self.x = x
        self.y = y


def initialize_fonz():
    return [
        Fon(id='y', ipa='Y', x=300, y=100),
        Fon(id='i', ipa='I', x=350, y=135),
        Fon(id='=', ipa='⋂', x=400, y=175),
        Fon(id='0', ipa='Ǝ', x=450, y=215),
        Fon(id='9', ipa='Ɐ', x=500, y=250),
        Fon(id='a', ipa='A', x=500, y=100),
        Fon(id='e', ipa='E', x=450, y=135),
        Fon(id='o', ipa='O', x=350, y=215),
        Fon(id='u', ipa='U', x=300, y=250),
        Fon(id='l', ipa='L', x=400, y=100),
        Fon(id='r', ipa='R', x=400, y=250),
        Fon(id='p', ipa='P', x=600, y=100),
        Fon(id='P', ipa='Ṗ̇', parent_id='p'),
        Fon(id='t', ipa='T', x=650, y=100),
        Fon(id='T', ipa='Ṫ', parent_id='t'),
        Fon(id='k', ipa='K', x=700, y=100),
        Fon(id='K', ipa='K̇', parent_id='k'),
        Fon(id='b', ipa='B', x=600, y=175),
        Fon(id='B', ipa='Ḃ', parent_id='b'),
        Fon(id='d', ipa='D', x=650, y=175),
        Fon(id='D', ipa='Ḋ', parent_id='d'),
        Fon(id='g', ipa='G', x=700, y=175),
        Fon(id='G', ipa='Ġ', parent_id='g'),
        Fon(id='m', ipa='M', x=600, y=250),
        Fon(id='M', ipa='Ṁ', parent_id='m'),
        Fon(id='n', ipa='N', x=650, y=250),
        Fon(id='N', ipa='Ṅ', parent_id='n'),
        Fon(id='5', ipa='Ŋ', x=700, y=250),
        Fon(id='%', ipa='Ŋ̇', parent_id='5'),
        Fon(id='h', ipa='H', x=875, y=40),
        Fon(id='f', ipa='F', x=800, y=100),
        Fon(id='7', ipa='Φ', x=850, y=100),
        Fon(id='s', ipa='S', x=900, y=100),
        Fon(id='8', ipa='Ƨ', x=950, y=100),
        Fon(id='v', ipa='V', x=800, y=175),
        Fon(id='6', ipa='θ', x=850, y=175),
        Fon(id='z', ipa='Z', x=900, y=175),
        Fon(id='j', ipa='J', x=950, y=175)
    ]

def initialize_edges():
    return [
    ("Y", "I"),
    ("I", "⋂"),
    ("⋂", "Ǝ"),
    ("Ǝ", "Ɐ"),
    ("A", "E"),
    ("E", "⋂"),
    ("⋂", "O"),
    ("O", "U"),
    ("L", "⋂"),
    ("⋂", "R"),
    ("Ɐ", "M"),
    ("P", "T"),
    ("T", "K"),
    ("B", "M"),
    ("D", "N"),
    ("G", "Ŋ"),
    ("B", "D"),
    ("D", "G"),
    ("M", "N"),
    ("N", "Ŋ"),
    ("Ŋ", "V"),
    ("F", "Φ"),
    ("Φ", "S"),
    ("S", "Ƨ"),
    ("V", "θ"),
    ("θ", "Z"),
    ("Z", "J"),
]