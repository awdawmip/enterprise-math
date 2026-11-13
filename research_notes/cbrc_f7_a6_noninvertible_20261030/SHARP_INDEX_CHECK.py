from itertools import permutations, product
from fractions import Fraction

D=((1,1,0,0),(1,-1,0,0),(0,0,1,1),(0,0,1,-1))
def matmul(A,B):
    return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in zip(*B)) for row in A)

def transpose(A):return tuple(zip(*A))
def det(A):
    n=len(A)
    res=0
    for p in permutations(range(n)):
        s=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=s
        for i in range(n):t*=A[i][p[i]]
        res+=t
    return res

def supp(v): return sum(x!=0 for x in v)
Pcount=0
Acount=0
for p in permutations(range(4)):
    # P acts on input channel i by sending to output channel p[i]
    split= (p[0]//2 != p[1]//2)
    if not split: continue
    assert p[2]//2 != p[3]//2
    Pcount+=1
    P=tuple(tuple(int(r==p[c]) for c in range(4)) for r in range(4))
    for kvals in product((-2,-1,1,2),repeat=4):
        Lam=tuple(tuple(2*kvals[i] if i==j else 0 for j in range(4)) for i in range(4))
        # D^-1 = D/2 ; A=(D P Lambda D)/2
        B=matmul(matmul(matmul(D,P),Lam),D)
        assert all(v%2==0 for row in B for v in row)
        A=tuple(tuple(v//2 for v in row) for row in B)
        assert det(A)==(1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0 else -1)*16*__import__('math').prod(kvals)
        if all(abs(k)==1 for k in kvals): assert abs(det(A))==16
        for w in product((-2,-1,0,1,2),repeat=4):
            h=tuple(sum(D[i][j]*w[j] for j in range(4)) for i in range(4))
            out=tuple(sum(A[i][j]*w[j] for j in range(4)) for i in range(4))
            ho=tuple(sum(D[i][j]*out[j] for j in range(4)) for i in range(4))
            assert supp(ho)==supp(h)
        h=tuple(sum(A[i][0] for _ in range(1)) for i in range(4))
        out=tuple(sum(D[i][j]*h[j] for j in range(4)) for i in range(4))
        assert supp(out[:2])==supp(out[2:])==1
        for i in (0,2):
            for j in (0,2):
                block=[A[i+a][j+b] for a in range(2) for b in range(2)]
                assert all(x!=0 for x in block)
                assert A[i][j]*A[i+1][j+1]==A[i][j+1]*A[i+1][j]
        Acount+=1
print(f'PASS split permutations={Pcount}; example matrices={Acount}; fixed test inputs=625 each; total free tests={Acount*625}; minimal index=16')
