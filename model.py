
class Phoneme:
    def __init__(self, id, ipa, ipa_dot=None, x=None, y=None):
        self.id = id
        self.ipa = ipa
        self.ipa_dot = ipa_dot
        self.id_dot = self.id.upper() if self.ipa_dot else None
        self.ipa_dot = ipa_dot
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
        Phoneme(id='P', ipa='P', ipa_dot='Ṗ', x=600, y=100),
        Phoneme(id='t', ipa='T', ipa_dot='Ṫ', x=650, y=100),
        Phoneme(id='k', ipa='K', ipa_dot='K̇̇', x=700, y=100),
        Phoneme(id='b', ipa='B', ipa_dot='Ḃ', x=600, y=175),
        Phoneme(id='d', ipa='D', ipa_dot='Ḋ', x=650, y=175),
        Phoneme(id='g', ipa='G', ipa_dot='Ġ̇̇̇', x=700, y=175),
        Phoneme(id='m', ipa='M', ipa_dot='Ṁ', x=600, y=250),
        Phoneme(id='n', ipa='N', ipa_dot='Ṅ', x=650, y=250),
        Phoneme(id='5', ipa='Ŋ', ipa_dot='Ŋ', x=700, y=250),
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