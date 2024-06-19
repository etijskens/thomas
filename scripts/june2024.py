import numpy as np
import random

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

################################################################################

if __name__ == '__main__':
    # run_collage()
    # run_verschillende_karakters()
    # run_waarde()
    l = [(1, 'aaa'), (2, 'b'), (-1, 'cccc'), (1, 'd'), (3, 'aa')]
    print(sorted(l, key=lambda t: len(t[1])))
    # [(2, 'b'), (1, 'd'), (3, 'aa'), (1, 'aaa'), (-1, 'cccc’)]
    print('-*# completed #*-')