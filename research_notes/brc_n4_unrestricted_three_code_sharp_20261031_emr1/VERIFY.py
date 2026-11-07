"""Exact checks for BRC N=4 unrestricted stochastic 3-code sharp minimax."""
from fractions import Fraction as F
from itertools import product
M20=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
M40=tuple(tuple(2*x for x in r) for r in M20)
D40=((19,21,0,0,0,0),(0,0,0,12,28,0),(0,0,20,0,0,20))
ENC=(0,0,2,1,1,2)
def observed(p40,mask,err):
    out=[0]*6
    for cls,mass in enumerate(p40):
        d=(mask>>cls)&1
        if cls in (3,4):
            j=cls-3
            for z in (0,1):
                out[2+2*z+d]+=mass*(8-err if z==j else err)
        else:out[d]+=mass*8
    assert sum(out)==320
    return out
def tv(a,b):
    return F(sum(abs(x-y) for x,y in zip(a,b)),2*sum(a))
def nullvector(rows):
    a=[[F(x) for x in row] for row in rows]
    m,n=len(a),6
    piv=[];rank=0
    for c in range(n):
        p=next((r for r in range(rank,m) if a[r][c]),None)
        if p is None:continue
        a[rank],a[p]=a[p],a[rank]
        lead=a[rank][c];a[rank]=[v/lead for v in a[rank]]
        for r in range(m):
            if r!=rank and a[r][c]:
                factor=a[r][c]
                a[r]=[a[r][k]-factor*a[rank][k] for k in range(n)]
        piv.append(c);rank+=1
        if rank==m:break
    free=next(c for c in range(n) if c not in piv)
    w=[F(0)]*n;w[free]=F(1)
    for r,c in enumerate(piv):w[c]=-a[r][free]
    assert any(w)
    assert all(sum(row[i]*w[i] for i in range(n))==0 for row in rows)
    return w
def witness(E):
    assert len(E)==6 and all(len(r)==3 and all(v>=0 for v in r) and sum(r)==1 for r in E)
    rows=[[E[i][j] for i in range(6)] for j in range(3)]
    rows += [[F(1),F(-1),F(0),F(0),F(0),F(0)],
             [F(0),F(0),F(0),F(1),F(-1),F(0)]]
    w=nullvector(rows)
    assert w[0]==w[1] and w[3]==w[4] and sum(w)==0
    v=[sum(w[i]*F(M20[i][j],20) for i in range(6)) for j in range(6)]
    assert sum(abs(x) for x in v)==sum(abs(x) for x in w) and sum(v)==0
    mask=sum(1<<j for j,x in enumerate(v) if x>0)
    assert abs(sum(v[j] for j in range(6) if mask&(1<<j)))==sum(abs(x) for x in w)/2
def verify():
    raw={'AU':{'P':(9,11),'Q':(10,10)},
         'AV':{'P':(5,5),'Q':(20,20)},
         'BU':{'P':(3,27),'Q':(15,15)},
         'BV':{'P':(30,30),'Q':(15,15)}}
    for law in ('P','Q'):
        weights=[v for s in raw.values() for v in s[law] for _ in range(2)]
        assert len(weights)==16 and all(x>0 for x in weights) and sum(weights)==240
    assert all(sum(r)==20 for r in M20) and all(sum(r)==40 for r in D40)
    errors=[tv(M40[i],D40[ENC[i]]) for i in range(6)]
    assert errors==[F(1,40),F(1,40),F(1,2),F(1,5),F(1,5),F(1,2)]
    count=0;worst=F(0)
    for e in (0,1,2,4):
        for mask in range(64):
            for i in range(6):
                dist=tv(observed(M40[i],mask,e),observed(D40[ENC[i]],mask,e))
                assert dist<=F(1,2)
                worst=max(worst,dist);count+=1
    assert count==1536 and worst==F(1,2)
    for lab in product(range(3),repeat=6):
        E=[[F(int(lab[i]==j)) for j in range(3)] for i in range(6)]
        witness(E)
    seed=20261031
    for _ in range(256):
        E=[]
        for i in range(6):
            v=[]
            for j in range(3):
                seed=(1664525*seed+1013904223)%(2**32)
                v.append(1+seed%31)
            E.append([F(x,sum(v)) for x in v])
        witness(E)
    print('PASS_BRC_N4_UNRESTRICTED_THREE_CODE_SHARP_20261031')
    print('P/Q: 16 strictly positive leaves each, 240/240.')
    print('Six-row M20 normalized; 3-code future errors: '+','.join(str(x) for x in errors))
    print('1536 exact public-record checks (64 masks x 6 states x 4 epsilon); worst TV=1/2.')
    print('Kernel certificate examples: all 729 deterministic E and 256 rational stochastic E.')
    print('General stochastic, continuum epsilon and all lawful adaptive policies: analytic proof in PROOF.md.')
if __name__=='__main__':verify()
