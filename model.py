
class Phoneme:
    def __init__(self, id, ipa, dot=False, x=None, y=None):
        self.id = id
        self.ipa = ipa
        self.dot = dot
        self.id_dot = self.id.upper() if self.dot else None
        self.x = x
        self.y = y








if __name__ == '__main__':


    phonemes = [
        Phoneme(id='y', ipa='Y', dot=False, x=300, y=100),
        Phoneme(id='i', ipa='I', dot=False, x=350, y=135),
        Phoneme(id='=', ipa='⋂', dot=False, x=400, y=175),
        Phoneme(id='0', ipa='Ǝ', dot=False, x=450, y=215),
        Phoneme(id='', ipa='Ɐ', dot=False, x=500, y=250),
        Phoneme(id='9', ipa='A', dot=False, x=500, y=100),
        Phoneme(id='e', ipa='E', dot=False, x=450, y=135),
        Phoneme(id='o', ipa='O', dot=False, x=350, y=215),
        Phoneme(id='u', ipa='U', dot=False, x=300, y=250),
        Phoneme(id='l', ipa='L', dot=False, x=400, y=100),
        Phoneme(id='r', ipa='R', dot=False, x=400, y=250),
        Phoneme(id='P', ipa='P', dot=True, x=600, y=100),
        Phoneme(id='t', ipa='T', dot=True, x=650, y=100),
        Phoneme(id='k', ipa='K', dot=True, x=700, y=100),
        Phoneme(id='b', ipa='B', dot=True, x=600, y=175),
        Phoneme(id='d', ipa='D', dot=True, x=650, y=175),
        Phoneme(id='g', ipa='G', dot=True, x=700, y=175),
        Phoneme(id='m', ipa='M', dot=True, x=600, y=250),
        Phoneme(id='n', ipa='N', dot=True, x=650, y=250),
        Phoneme(id='5', ipa='Ŋ', dot=True, x=700, y=250),
        Phoneme(id='h', ipa='H', dot=False, x=875, y=40),
        Phoneme(id='f', ipa='F', dot=False, x=800, y=100),
        Phoneme(id='7', ipa='Φ', dot=False, x=850, y=100),
        Phoneme(id='s', ipa='S', dot=False, x=900, y=100),
        Phoneme(id='8', ipa='Ƨ', dot=False, x=950, y=100),
        Phoneme(id='v', ipa='V', dot=False, x=800, y=175),
        Phoneme(id='6', ipa='θ', dot=False, x=850, y=175),
        Phoneme(id='z', ipa='Z', dot=False, x=900, y=175),
        Phoneme(id='j', ipa='J', dot=False, x=950, y=175)
    ]

    pass