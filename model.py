
class Phoneme:
    def __init__(self, id, ipa, parent_id=None, x=None, y=None):
        self.id = id
        self.ipa = ipa
        self.parent_id = parent_id
        self.x = x
        self.y = y


def initialize_phonemes():
    return [
        Phoneme(id='y', ipa='Y', x=300, y=100),
        Phoneme(id='i', ipa='I', x=350, y=135),
        Phoneme(id='=', ipa='⋂', x=400, y=175),
        Phoneme(id='0', ipa='Ǝ', x=450, y=215),
        Phoneme(id='9', ipa='Ɐ', x=500, y=250),
        Phoneme(id='a', ipa='A', x=500, y=100),
        Phoneme(id='e', ipa='E', x=450, y=135),
        Phoneme(id='o', ipa='O', x=350, y=215),
        Phoneme(id='u', ipa='U', x=300, y=250),
        Phoneme(id='l', ipa='L', x=400, y=100),
        Phoneme(id='r', ipa='R', x=400, y=250),
        Phoneme(id='p', ipa='P', x=600, y=100),
        Phoneme(id='P', ipa='Ṗ̇', parent_id='p'),
        Phoneme(id='t', ipa='T', x=650, y=100),
        Phoneme(id='T', ipa='Ṫ', parent_id='t'),
        Phoneme(id='k', ipa='K', x=700, y=100),
        Phoneme(id='K', ipa='K̇', parent_id='k'),
        Phoneme(id='b', ipa='B', x=600, y=175),
        Phoneme(id='B', ipa='Ḃ', parent_id='b'),
        Phoneme(id='d', ipa='D', x=650, y=175),
        Phoneme(id='D', ipa='Ḋ', parent_id='d'),
        Phoneme(id='g', ipa='G', x=700, y=175),
        Phoneme(id='G', ipa='Ġ', parent_id='g'),
        Phoneme(id='m', ipa='M', x=600, y=250),
        Phoneme(id='M', ipa='Ṁ', parent_id='m'),
        Phoneme(id='n', ipa='N', x=650, y=250),
        Phoneme(id='N', ipa='Ṅ', parent_id='n'),
        Phoneme(id='5', ipa='Ŋ', x=700, y=250),
        Phoneme(id='%', ipa='Ŋ̇', parent_id='5'),
        Phoneme(id='h', ipa='H', x=875, y=40),
        Phoneme(id='f', ipa='F', x=800, y=100),
        Phoneme(id='7', ipa='Φ', x=850, y=100),
        Phoneme(id='s', ipa='S', x=900, y=100),
        Phoneme(id='8', ipa='Ƨ', x=950, y=100),
        Phoneme(id='v', ipa='V', x=800, y=175),
        Phoneme(id='6', ipa='θ', x=850, y=175),
        Phoneme(id='z', ipa='Z', x=900, y=175),
        Phoneme(id='j', ipa='J', x=950, y=175)
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