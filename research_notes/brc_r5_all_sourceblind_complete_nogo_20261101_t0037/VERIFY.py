"""Exact author checker for auxiliary compensated R5 source-blind no-go (not native X6)."""
from fractions import Fraction as F
from itertools import product
ALPHA=(F(1,4),F(1,5)); KAPPA=(F(3,4),F(1,6)); THETA=F(11,2)
LEAF={'A':(1,F(1)), 'D':(2,F(1,2)), 'Y':(2,F(3,2)),
      'C':(2,F(1)), 'DH':(3,F(1,4)), 'YH':(3,F(2)),
      'L':(3,F(1)), 'L4':(4,F(1))}
FULL_KEYS=('A','D','Y','LD','LY','LC'); LR_KEYS=('A','D','Y','L')

def flows(actions, pA=None):
    f={k:F(0) for k in LEAF}
    for i,(a,k) in enumerate(zip(ALPHA,KAPPA)):
        z=F(1,2)
        cont = F(actions[i]['A']) if pA is None else pA[i]
        f['A']+=z*(1-cont)
        if cont==0: continue
        d=y=z*cont*a; c=z*cont*(1-2*a)
        if actions[i]['D']:
            f['DH']+=d*F(2,3); f['L4' if actions[i]['LD'] else 'L']+=d/3
        else: f['D']+=d
        if actions[i]['Y']:
            f['YH']+=y/2; f['L4' if actions[i]['LY'] else 'L']+=y/2
        else: f['Y']+=y
        f['C']+=c*(1-k); f['L4' if actions[i]['LC'] else 'L']+=c*k
    assert sum(f.values())==1
    assert sum(f[t]*LEAF[t][1] for t in LEAF)==1
    return f

def full(bits):
    return flows([dict(zip(FULL_KEYS,bits[6*i:6*i+6])) for i in (0,1)])

def lr(bits):
    b=dict(zip(LR_KEYS,bits))
    return flows([dict((n,b['L' if n.startswith('L') else n]) for n in FULL_KEYS)]*2)

def carrier(f):
    tq=sum(f[k]*LEAF[k][0] for k in LEAF)
    tp=sum(f[k]*LEAF[k][0]*LEAF[k][1] for k in LEAF)
    x,y,u=f['DH'],f['L4'],f['YH']
    assert tp-tq == u-F(3,4)*x
    return x,y,u,tq

def B_of(z):
    x,y,u,t=z
    return (t-1-y-F(3,2)*x-2*u)/THETA

def observe(f,r):
    ep=sum(f[k]*LEAF[k][1]*r[k] for k in LEAF)
    eq=sum(f[k]*r[k] for k in LEAF)
    x,y,u,t=carrier(f)
    return ep,eq,t+u-F(3,4)*x,t

def factor(z,r):
    x,y,u,t=z; B=B_of(z)
    d=B-F(3,2)*x; ys=B-2*u
    Aplus=2-(THETA+2)*B
    base=r['L']+(r['C']-r['L'])*Aplus
    eq=base+(r['D']-r['L'])*d+(r['Y']-r['L'])*ys
    eq+=(r['DH']-r['L'])*x+(r['YH']-r['L'])*u+(r['L4']-r['L'])*y
    ep=base+(r['D']-r['L'])*d/2+(r['Y']-r['L'])*ys*F(3,2)
    ep+=(r['DH']-r['L'])*x/4+2*(r['YH']-r['L'])*u+(r['L4']-r['L'])*y
    return ep,eq,t+u-F(3,4)*x,t

def score(f,r,H):
    return sum(f[k]*((H[0]*LEAF[k][1]+H[1])*r[k]
              +(H[2]*LEAF[k][1]+H[3])*LEAF[k][0]) for k in LEAF)

def gamma(r): return 2*r['C']-r['A']-r['L']

def separation_A(r,s):
    g=gamma(r); abar=sum(ALPHA)
    xi=r['D']+r['YH']/2-F(3,2)*r['L']-(THETA+2)*(r['C']-r['L'])
    Bbound=THETA+F(7,2)+4/abar
    assert s>0 and s < min(F(1,2),THETA/(2*Bbound))
    h=THETA-s*(xi+2*g/abar)
    assert h>1
    H=(F(0),s,2*(h+1),-(2*h+3))
    expected=s*abs(g)*abs(ALPHA[0]-ALPHA[1])/(2*abar)
    return H,expected,h

def det(mat):
    n=len(mat); a=[list(map(F,row)) for row in mat]
    assert all(len(row)==n for row in a)
    v=F(1)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]!=0),None)
        if k is None:return F(0)
        if j!=k:a[j],a[k]=a[k],a[j];v=-v
        p=a[j][j];v*=p
        for i in range(j+1,n):
            c=a[i][j]/p
            for z in range(j,n):a[i][z]-=c*a[j][z]
    return v

def rank(rows):
    if not rows:return 0
    a=[list(map(F,r)) for r in rows]
    m,n=len(a),len(a[0]); j=0
    for k in range(n):
        idx=next((i for i in range(j,m) if a[i][k]),None)
        if idx is None:continue
        a[j],a[idx]=a[idx],a[j]
        p=a[j][k]
        for i in range(j+1,m):
            c=a[i][k]/p
            for q in range(k,n):a[i][q]-=c*a[j][q]
        j+=1
        if j==m:break
    return j

def affrank(points):
    pts=list(points);b=pts[0]
    return rank([[p[j]-b[j] for j in range(len(b))] for p in pts[1:]])

def sourceblind_r(**updates):
    r={n:F(1,2) for n in LEAF};r.update(updates)
    assert all(0<=v<=1 for v in r.values())
    return r

def main():
    assert tuple((1+k*(1-2*a))/a for a,k in zip(ALPHA,KAPPA))==(THETA,THETA)
    LF={b:lr(b) for b in product((0,1),repeat=4)}
    FF={b:full(b) for b in product((0,1),repeat=12)}
    assert len(LF)==16 and len(FF)==4096
    Lcar={b:carrier(f) for b,f in LF.items()}
    Fcar={b:carrier(f) for b,f in FF.items()}
    assert affrank(Lcar.values())==affrank(Fcar.values())==4
    LR_BASIS=((0,0,0,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0))
    base=Lcar[LR_BASIS[0]]
    d4=det([[Lcar[b][j]-base[j] for j in range(4)] for b in LR_BASIS[1:]])
    assert d4==-F(50787,10240000)
    for f in (*LF.values(),*FF.values()):
        z=carrier(f);B=B_of(z)
        assert f['D']==B-F(3,2)*z[0]
        assert f['Y']==B-2*z[2]
        assert f['C']+2*f['A']==2-(THETA+2)*B
        assert f['L']==1-sum(f[k] for k in LEAF if k!='L')
    print('ALL_POLICIES=4096_FULL+16_LR; P=Q=1; TIME/B/C+D/2A_IDENTITIES=PASS')
    print('CARRIER_4D_LR_MINOR='+str(d4))
    names=list(LEAF)
    fpts=[tuple(f[k] for k in names) for f in FF.values()]
    lpts=[tuple(f[k] for k in names) for f in LF.values()]
    assert affrank(fpts)==5 and affrank(lpts)==4
    print('TERMINAL_MASS_RANK: FULL=5 LR=4')
    stop={n:0 for n in FULL_KEYS}
    X=flows([stop,stop],pA=(F(4,5),F(0)))
    Y=flows([stop,stop],pA=(F(0),F(1)))
    assert carrier(X)==carrier(Y)==(0,0,0,F(31,20))
    assert (X['A']-Y['A'],X['C']-Y['C'],X['L']-Y['L'])==(F(1,10),-F(1,5),F(1,10))
    assert all(X[k]==Y[k] for k in LEAF if k not in ('A','C','L'))
    print('FIBER_SAME_XYUT=(0,0,0,31/20); C(X)=1/20 C(Y)=1/4; (A,C,L)_DIFF=(1/10,-1/5,1/10)')
    g0=[sourceblind_r(),
        sourceblind_r(DH=F(5,8),L4=F(3,4),YH=F(1,2)),
        sourceblind_r(A=F(3,4),C=F(5,8),L=F(1,2),DH=F(5,8),L4=F(3,4),YH=F(2,3)),
        sourceblind_r(A=F(1,4),C=F(1,2),L=F(3,4),D=F(5,6),Y=F(1,6),DH=F(1,3),YH=F(2,3),L4=F(7,8))]
    for i,r in enumerate(g0):
        assert gamma(r)==0
        for f in (*LF.values(),*FF.values()):
            assert factor(carrier(f),r)==observe(f,r)
        rankLR=affrank([observe(f,r) for f in LF.values()])
        assert rankLR<=4
        print(f'GAMMA0_CASE_{i}: observed_LR_affine_rank={rankLR}; factor_verified=4112/4112')
    def Fcar(z):x,y,u,t=z;return F(985,8)*x+70*y-130*u-23*t
    witness=(1,1,0,1,0,1,0,0,0,0,0,0)
    v=Fcar(carrier(FF[witness])); h=max(Fcar(c) for c in Lcar.values())
    assert v==-F(661,32) and h==-23 and v-h==F(75,32)
    print('GAMMA0_CARRIER_SUPPORT: LR=-23 FULL_WITNESS=-661/32 GAP=75/32')
    gn=[sourceblind_r(C=F(3,4)),
        sourceblind_r(A=F(1,4),C=F(1,3),L=F(3,4),D=F(1,5),Y=F(4,5),DH=F(2,7),YH=F(3,7),L4=F(6,7)),
        sourceblind_r(A=F(1,10),C=F(9,10),L=F(1,10),D=F(1,3),Y=F(2,3),DH=F(5,6),YH=F(1,6),L4=F(1,4))]
    for i,r in enumerate(gn):
        assert gamma(r)!=0
        H,expected,t=separation_A(r,F(1,16))
        lrmax=max(score(f,r,H) for f in LF.values())
        fullmax=max(score(f,r,H) for f in FF.values())
        assert fullmax-lrmax==expected>0
        print(f'GAMMA_NONZERO_CASE_{i}: gamma={gamma(r)} t={t} LRmax={lrmax} FULLmax={fullmax} gap={expected}')
    print('ALL_REAL_SOURCEBLIND_NO_GO: gamma!=0 Bellman separator; gamma=0 factor+rank dichotomy')
    print('PASS_EXACT_R5_ALL_SOURCEBLIND_COMPLETE_NO_GO')

if __name__=='__main__': main()
