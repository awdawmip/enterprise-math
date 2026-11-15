"""Exact Burnside verification of signed-letter word orbits under H=(C2)^6 ⋊ A6."""
from itertools import permutations, product

def stirling(n,k):
    t=[[0]*(k+1) for _ in range(n+1)]
    t[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            t[i][j]=t[i-1][j-1]+j*t[i-1][j]
    return t[n][k]

def parity(p):
    return sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2

def orbit_formula(n):
    return sum((1+int(k>=5))*stirling(n,k)*2**(n-k)
               for k in range(1,min(6,n)+1)) if n else 1

def orbit_B(n):
    return sum(stirling(n,k)*2**(n-k)
               for k in range(1,min(6,n)+1)) if n else 1

def burnside(n):
    total=0
    order=0
    for p in permutations(range(6)):
        if parity(p): continue
        fixed=[i for i in range(6) if p[i]==i]
        for signs in product((-1,1),repeat=6):
            f=2*sum(signs[i]==1 for i in fixed)
            total+=f**n
            order+=1
    assert order==23040 and total%order==0
    return total//order

def run():
    return {n:{"H_orbits":orbit_formula(n),
               "B6_orbits":orbit_B(n),
               "H_B_gap":orbit_formula(n)-orbit_B(n),
               "burnside":burnside(n)}
            for n in range(0,9)}

if __name__=="__main__":
    result=run()
    assert all(v["H_orbits"]==v["burnside"] for v in result.values())
    print("PASS; 23040 signed monomial actions checked per N")
    for n,v in result.items():print(n,v)
