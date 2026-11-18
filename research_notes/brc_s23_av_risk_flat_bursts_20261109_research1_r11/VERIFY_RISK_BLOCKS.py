#!/usr/bin/env python3
"""Complete exact rational-interval certificate for S23/AV R(128,L), 0<=L<=1142.

Model and strict theta enclosure inherited from the cited frozen-source studies.
No floating point is used for any assertion or comparison.
"""
P = 262204504569236716045286
Q = 10**24
M = 128
LMAX = 1142
# Each row: inclusive first/last horizon, exact affine first difference A+B*theta.
BLOCKS = (
    (1, 36, (16, -61)),
    (37, 164, (-43, 164)),
    (165, 200, (0, 0)),
    (201, 328, (-43, 164)),
    (329, 364, (0, 0)),
    (365, 425, (-43, 164)),
    (426, 492, (145, -553)),
    (493, 528, (0, 0)),
    (529, 589, (145, -553)),
    (590, 978, (0, 0)),
    (979, 1045, (-188, 717)),
    (1046, 1081, (0, 0)),
    (1082, 1142, (-188, 717)),
)

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(k,x): return (k*x[0],k*x[1])
def lo(x): return min(Q*x[0]+P*x[1],Q*x[0]+(P+1)*x[1])
def hi(x): return max(Q*x[0]+P*x[1],Q*x[0]+(P+1)*x[1])
def phase(j):
    if j == 0: return (0,0)
    z = j*P//Q
    assert z == j*(P+1)//Q, ("ambiguous floor",j)
    p=(z+1,-j)
    assert 0 < lo(p) <= hi(p) < Q
    return p

def direct_risk(n):
    assert n>=M
    cuts=sorted(((lo(phase(j)),j) for j in range(n)))
    phases=[phase(j) for _,j in cuts]
    # The complete circular order is the same for EVERY theta in the strict bracket.
    for x,y in zip(phases,phases[1:]):
        assert hi(x)<lo(y), ("ambiguous order",n,x,y)
    gaps=[]
    for i in range(n):
        gap=sub(phases[(i+1)%n],phases[i])
        if i==n-1:gap=add(gap,(1,0))
        assert lo(gap)>0
        gaps.append(gap)
    old=[i for i,(_,j) in enumerate(cuts) if j<M]
    assert len(old)==M
    wins=(0,0)
    for u,k in enumerate(old):
        stop=old[(u+1)%M]
        if stop<=k:stop+=n
        gs=[gaps[z%n] for z in range(k,stop)]
        best=max(gs,key=lo)
        assert all(g==best or hi(g)<lo(best) for g in gs), ("ambiguous max",n,gs)
        wins=add(wins,best)
    risk=sub((1,0),wins)
    assert 0<=lo(risk)<=hi(risk)<=Q
    return risk

def main():
    rows={}
    for first,last,slope in BLOCKS:
        assert 1<=first<=last<=LMAX
        for L in range(first,last+1):
            assert L not in rows
            rows[L]=slope
    assert set(rows)==set(range(1,LMAX+1))
    prev=direct_risk(M)
    assert prev==(0,0)
    selected={0:prev}
    for L in range(1,LMAX+1):
        new=direct_risk(M+L)
        got=sub(new,prev)
        assert got==rows[L], ("wrong step",L,got,rows[L])
        assert lo(got)>=0
        if L in (36,37,164,165,200,201,328,329,364,365,425,426,492,493,528,529,589,590,978,979,1045,1046,1081,1082,1142):
            selected[L]=new
        prev=new
    print("CERTIFIED_RISK_CUTS",M+LMAX,"CERTIFIED_HORIZONS",LMAX,"SYMBOLIC_BLOCKS",len(BLOCKS))
    for a,b,slope in BLOCKS:
        print("BLOCK",a,b,"INCREMENT",slope[0],slope[1],"COUNT",b-a+1)
    for L,expr in sorted(selected.items()):
        print("R",L,expr[0],expr[1])
    assert rows[165]==(0,0) and rows[201]==(-43,164)
    assert lo(rows[201])>0
    print("PASS_EXACT_S23_AV_NONMONOTONE_RISK_128_1142")
if __name__=='__main__':main()
