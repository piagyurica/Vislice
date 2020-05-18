import random 

STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'Z'

# Konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

# Konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open("besede.txt") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:
    def __init__(self, geslo, crke=None): #nikol ne sme biti tukaj [], ker ce nardis vec objektov oz vec ljudi igra igro, se bo vsem potem spremenil takoj ko bo nekdo naredil spremembo
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke]

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        # return all(c in self.crke for c in self.geslo)
        for c in self.geslo:
            if c not in self.crke:
                return False

        return True

    def pravilni_del_gesla(self):
        trenutno = ""
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += "_"

        return trenutno

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(ugibana_crka)

        if ugibana_crka in self.geslo: #uganil je crko, ali je ze zmagal
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)

class Vislice: # to bo nas container
    """
    Skrbi za trenutno stanje več iger (imel bo več objektov tipa Igra)
    """
    def __init__(self):
        # Slovar, ki ID-ju priredi objekt njegove igre
        self.igre = {} # int/vrednosti -> (Igra, stanje)

    def prost_id_igre(self):
        """Vrne nek id, ki ga ne uporablja nobena igra"""
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1 #boljse kot return len(self.igre.keys()) ker lahko brisemo igre

    def nova_igra(self): # to si predstavljaj kot da na banki odpres nov racun
        # dobimo svez id
        nov_id = self.prost_id_igre()
        # naredimo novo igro
        sveza_igra = nova_igra()
        # vse to shranimo v self.igre
        self.igre[nov_id] = (sveza_igra, ZACETEK)
        # vrnemo nov id
        return nov_id

    def ugibaj(self, id_igre, crka):
        # dobimo staro igro ven
        trenutna_igra, _ = self.igre[id_igre]
        # ugibamo crko, dobimo novo stanje
        novo_stanje = trenutna_igra.ugibaj(crka)
        # zapisemo posodobljeno stanje in igro nazaj v "bazo"
        self.igre[id_igre] = (trenutna_igra, novo_stanje)







