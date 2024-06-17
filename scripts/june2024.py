import numpy as np
import random

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

if __name__ == '__main__':
    run_collage()
    print('-*# completed #*-')