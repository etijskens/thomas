import numpy as np
import random
import string

# OEFENING 1 ###################################################################
def collage(l:list,M:int,N:int) -> list:
    # Result matrix
    ABCD = np.zeros((M,N),dtype=float)
    # overlap matrix
    vrlp = np.zeros((M,N),dtype=float)
    #   0 implies the element is not overlapped by A B C or D
    #   1 implies the element is overlapped by one of A B C  D
    #   2 implies the element is overlapped by two of A B C D
    #   3 implies the element is overlapped by three of A B C D
    #   4 implies the element is overlapped by all four of A B C D

    A = l[0]
    MA,NA = A.shape
    # Update the result matrix
    ABCD[0:MA,0:NA] += A
    # Update overlap matrix
    vrlp[0:MA,0:NA] += np.ones_like(A)

    B = l[1]
    MB,NB = B.shape
    # Update the result matrix
    ABCD[0:MB, N-NB:N] += B
    # Update overlap matrix
    vrlp[0:MB, N-NB:N] += np.ones_like(B)

    C = l[2]
    MC,NC = C.shape
    # Update the result matrix
    ABCD[M-MC:M, 0:NC] += C
    # Update overlap matrix
    vrlp[M-MC:M, 0:NC] += np.ones_like(C)

    D = l[3]
    MD,ND = D.shape
    # Update the result matrix
    ABCD[M-MD:M, N-ND:N] += D
    # Update overlap matrix
    vrlp[M-MD:M, N-ND:N] += np.ones_like(D)
    # print(ABCD)
    # print(vrlp)

    # avoid division by 0
    vrlp = np.maximum(vrlp, np.ones_like(vrlp))
    # print(vrlp)
    # Scale the result matrix by the overlap count
    ABCD /= vrlp

    # Convert result to integer and return
    return np.int_(ABCD)

def random_pixel() -> int:
    """Generate a random integer between """
    return random.randint(0, 255)

def run_collage():
    """a test"""
    A = random_pixel()*np.ones((3,3),dtype=int)
    B = random_pixel()*np.ones((2,2),dtype=int)
    C = random_pixel()*np.ones((2,2),dtype=int)
    D = random_pixel()*np.ones((2,2),dtype=int)
    ABCD = collage([A,B,C,D],4,4)
    print(ABCD)

# OEFENING 2 ###################################################################

def unique_characters(s:str) -> str:
    """return a string of unique characters"""
    return ''.join(set(s))
def verschillende_karakters(a:str, b:str,na=0, nb=0)-> tuple[int,int]:
    """"""
    na = verschillende_karakters_a_in_b(unique_characters(a),b)
    nb = verschillende_karakters_a_in_b(unique_characters(b),a)
    return na,nb

def verschillende_karakters_a_in_b(a,b,ainb=0):
    """"""
    if not a[0] in b:
        ainb += 1
    if len(a) == 1:
        return ainb
    return verschillende_karakters_a_in_b(a[1:], b, ainb)

def run_verschillende_karakters():
    a = 'aaa'
    b = 'abc'
    print(verschillende_karakters(a, b))

# OEFENING 3 ###################################################################

KAARTEN = '234567890JQKA' # 0 staat voor 10
def kaartwaarde(k:str) -> int:
    """bereken de waarde(n) van 1 kaart."""
    pos = KAARTEN.find(k)
    waarde = pos + 2
    if waarde == 14:
        # een aas geeft waarde 1.
        waarde = 1

    return waarde

def waarde(kaarten:list)->list:
    # Het resultaat is vanzelf geordend, maar kan dezelfde waarde meermaals bevatten
    # in het geval van meerdere azen. dat lossen we op met np.unique
    return list(np.unique(voeg_toe(kaarten, np.zeros(1, dtype=int))))

def voeg_toe(kaarten, w)->list:
    w0 = kaartwaarde(kaarten[0])
    w += w0
    if w0 == 1: # aas
        # Hou er rekening mee dat een aas ook voor 11 kan tellen
        # maak de lijst dubbel zo lang
        ww = w + 10 # in deze lijst telt de aas voor 11
        # concatenate w and ww
        w = np.concatenate((w, ww))

    # w is vanzelf geordend, maar bevat dezelfde waarde meermaals in het geval van meerdere azen.
    if len(kaarten) == 1:
        return w
    return voeg_toe(kaarten[1:], w)


def random_kaarten(n:int)->list:
    return random.choices(KAARTEN, k=n)


def run_waarde():
    hand = random_kaarten(5)
    hand = ['A', 'A', '7', '3', '5']

    kaartwaarden = []
    for kaart in hand:
        kaartwaarden.append(kaartwaarde(kaart))
    print(hand, kaartwaarden)
    print(waarde(hand))

# examen #######################################################################

def b_from_a(a):
    # The sum of neighbours is subject to boundary special cases. They are
    # annoying and prone to errors.
    # However, if we surround a with zeros in every direction, we can get rid of
    # those.

    # list comprehension to generate a shape which is larger by 2 in each
    # dimension, and turn into tuple
    shape_surrounded = tuple([d+2 for d in a.shape])
    a_surrounded = np.zeros(shape_surrounded, dtype=int)
    # Add a to the central part of a_surrounded
    a_surrounded[1:-1,1:-1] = a
    print(a)
    print(a_surrounded)

    # Compute the neighbour sums
    # the neighbour sum  is np.sum(a_surrounded[i-1:i+2,j-1:j+2]) - a_surrounded[i,j]
    neighbour_sum = -a_surrounded
    for i in range(1,a_surrounded.shape[0]):
        for j in range(1,a_surrounded.shape[1]):
            neighbour_sum[i,j] += np.sum(a_surrounded[i-1:i+1,j-1:j+1])
    # remove the surroundings, as they ar no longer needed
    neighbour_sum = neighbour_sum[1:-1,1:-1]
    print(neighbour_sum)
    # Compute b
    # Indien a[i,j] == 1 en som van de buren van a[i,j] is 2 of 3, dan b[i,j] = 1, anders 0.
    # Indien a[i,j] == 0 en som van de buren van a[i,j] is 1, dan b[i,j] = 1, anders 0.
    # de conditie van de eerste regel kan element-wise geschreven worden als
    cond1 = np.logical_and(a == 1, np.logical_or(neighbour_sum==2, neighbour_sum==3))
    # op dezelfde manier is de conditie van de tweede regel:
    cond2 = np.logical_and(a == 0, neighbour_sum == 1)
    # beide condities zijn wederzijds exclusief (ze kunnen niet gelijktijdig waar zijn)
    # Maw, b wordt op 1 gezet als np.logical_or(cond1, cond2) waar is
    # Noteer vervolgens dat True en False intern in Python weergegeven worden als 1 en 0.
    # Het resultaat is dus de conditie np.logical_or(cond1, cond2) omgezet naar int waarden.
    b = np.int_(np.logical_or(cond1, cond2))
    return b

def run_b_from_a():
    a = np.random.randint(0, 2, size=(5,5) )
    b = b_from_a(a)

################################################################################
class Groep:
    def __init__(self, l:list[tuple[str,str]]):
        self.l = l
        self.w = {}
        self.personen = set()
        for t in self.l:
            if t[0] != t[1]:
                self.personen.add(t[0])
                self.personen.add(t[1])
                if t[0] not in self.w:
                    self.w[t[0]] = set()
                if t[1] not in self.w:
                    self.w[t[1]] = set()
                self.w[t[0]].add(t[1])
                self.w[t[1]].add(t[0])

    def __str__(self):
        t = [[e, sorted(list(self.w[e]))] for e in self.w]
        t_sort = sorted(t, key=lambda x: x[0])
        r = [e[0] + '->' + ''.join(e[1]) for e in t_sort]
        join_r = ':'.join(r)
        return f'[{join_r}]'

    def geef_personen(self):
        return self.personen

    def vriend_van_vriend_0(self, p:str, n:int):
        if p not in self.w:
            return set()

        vrienden = list(self.w[p])
        l = list(self.w[p])
        t = 1

        while t <= n:
            if t != 1:
                vrienden = nieuwe_v
            nieuwe_v = []
            for v in vrienden:
                for e in self.w[v]:
                    if e != p:
                        nieuwe_v.append(e)  # lijst maken met de volgende vrienden
            l.extend(nieuwe_v)
            t += 1  # nadat je alle tussenpersonen hebt overlopen, begin je met de volgende
        return set(l)

    def vriend_van_vriend(self, p:str, n:int=0):
        if p not in self.w:
            return set()

        else:
            vrienden = set(self.w[p]) # directe vrienden
            for i in range(n):
                nieuwe_vrienden = set()
                for v in vrienden:
                    nieuwe_vrienden.update(self.w[v])
                vrienden.update(nieuwe_vrienden)
            return vrienden

    def zijn_bevriend(self,p1,p2):
        return p1 == p2 or p2 in self.w[p1]
    def vind_groepjes(self):
        for p1 in self.w:
            pv = list(self.w[p1])
            n = len(pv)
            is_groepje = True
            for i in range(n):
                for j in range(i+1,n):
                    if not self.zijn_bevriend(pv[i], pv[j]):
                        is_groepje = False
                        break
            if is_groepje:
                # eerste voorwaarde is voldaan, alle personen kennen elkaar
                # tweede voorwaarde is niemand kent iemand anders
                for p2 in pv:
                    p2v = list(self.w[p2])
                    for p3 in p2v:
                        if not self.zijn_bevriend(p3,p1):
                            # p2 kent p3, maar die kent p1 niet, voorwaarde twee geldt niet
                            is_groepje = False
                            break
                if is_groepje:
                    # maak een lijst met het groepje, p1 + zijn vrienden, en print ze
                    l = [p1]
                    l.extend(pv)
                    print(l)

def run_vriend_van_vriend():
    n = random.randint(10,20)
    input = set()
    for i in range(n):
        t = (random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase) )
        input.add(t)
    g = Groep(input)
    print(g.personen)
    print(g.w)
    for p in g.personen:
        print(p, g.vriend_van_vriend(p))
        print(p, g.vriend_van_vriend(p,1))
        print(p, g.vriend_van_vriend(p,2))

def run_vind_groepjes():
    n = random.randint(5, 7)
    input = set()
    for i in range(n):
        t = (random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase))
        input.add(t)
    g = Groep(input)
    print(g.personen)
    print(g.w)
    g.vind_groepjes()
################################################################################
"""
Programmeer de klasse FlipLijst, waarbij elk object van deze klasse een lijst l van gehele getallen bijhoudt (deze lijst kan dubbels bevatten).
Programmeer in deze klasse:
een constructor met 1 argument, namelijk de lijst gehele getallen waarvan hierboven sprake
de operator *= met als rechterargument een natuurlijk getal (eventueel 0). De werking van de operator is als volgt:
indien het rechteroperand een geldige index i in de lijst l voorstelt, dan wordt de getallenlijst van het object als volgt aangepast:
de kop van de lijst tot net voor index i blijft ongewijzigd
de staart van de lijst vanaf index i (inbegrepen) wordt omgekeerd
Indien het rechteroperand dus de waarde 0 heeft, wordt de volledige lijst omgekeerd.
indien het rechteroperand geen geldige index in l voorstelt, dan blijft het object ongewijzigd (en heeft de operator dus geen effect)
de methode __str__() levert de stringgedaante van elk element van de getallenlijst op, gescheiden door dubbele punten (dus door :) en het geheel tussen vierkante haakjes.
 
Herneem je oplossing uit deel A. Programmeer bijkomend de methode sorteer_sequentie() (zonder argumenten). Deze methode geeft een lijst van gehele getallen r terug, maar laat de lijst van het object ongewijzigd.
Deze lijst r moet zodanig geconstrueerd zijn dat na uitvoering van onderstaand code-fragment
flips = f.sorteer_sequentie()
for e in flips:
    f *= e
de lijst van de FlipLijst f van klein naar groot gesorteerd is.
Zorg hierbij dat je algoritme voldoende efficiënt is om binnen de tijdslimiet door Dodona opgelegd tot een resultaat te komen (alle mogelijke sequenties van alle mogelijke flips aflopen is dus geen goed idee).
"""
class FlipLijst:
    def __init__(self, l:list[int]):
        self.l = l


################################################################################
if __name__ == '__main__':
    # run_collage()
    # run_verschillende_karakters()
    # run_waarde()

    # l = [(1, 'aaa'), (2, 'b'), (-1, 'cccc'), (1, 'd'), (3, 'aa')]
    # print(sorted(l, key=lambda t: len(t[1])))
    # # [(2, 'b'), (1, 'd'), (3, 'aa'), (1, 'aaa'), (-1, 'cccc’)]
    # print('-*# completed #*-')

    # run_b_from_a()
    # run_vriend_van_vriend()
    run_vind_groepjes()