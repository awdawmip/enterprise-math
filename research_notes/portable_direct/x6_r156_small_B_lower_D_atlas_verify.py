from itertools import product
from fractions import Fraction as Q
G={}
for v in product(range(-10,11),repeat=3):
    if not any(v) or next(z for z in v if z)<0 or max(sum(max(z,0) for z in v),sum(max(-z,0) for z in v))>10:continue
    x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    G[v]=tuple(abs(h[j]-h[i]) for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
assert len(G)==1935
U=(4,-4,1);V=(6,-1,0);A=(1,0,0);C=(5,-4,1);K=(5,-1,0);H=(9,-5,1);P=(1,3,-1);R=(7,-1,0)
F={U,V,A,C,K,H,P,R}
S=lambda B,D:(136+B,312,136+D,B+176,B+D,D+176)
regions=[([(0,0),(20,0),(20,20)],3,lambda B,D:136+D,V,{U,V},2), ([(0,0),(20,20),(20,292),(0,272)],3,lambda B,D:136+B,V,F,0), ([(0,272),(20,292),(20,528),(0,528)],6,lambda B,D:B+D,A,F,4)]
for vertices,n,L,w,family,active in regions:
    def slack(g,j,B,D,r):return g[j]*L(B,D)-r*n*S(B,D)[j]
    for r,exclude in [(Q(1),set()),(Q(3,2),family)]:
        hist=[0]*6
        for v,g in G.items():
            if v in exclude:continue
            js=[j for j in range(6) if all(slack(g,j,B,D,r)>=0 for B,D in vertices)]
            assert js,(vertices,r,v)
            hist[js[0]]+=1
        print(r,hist,sum(hist))
    assert all(all(slack(G[w],j,B,D,1)<=0 for j in range(6)) and slack(G[w],active,B,D,1)==0 for B,D in vertices)
    if family=={U,V}:
        for v in family:
            for j in range(6):
                assert all(slack(G[v],j,B,D,Q(3,2))<0 or (j==4 and B==D==0 and G[v][j]==0) for B,D in vertices)
print('CERTIFICATE PASS')
def predict(B,D):
    if D<=B:return {U,V}
    if D<=272+B:
        T=(B+544)/3
        out={U,V}
        if D>T:out|={A,C,K,H}
        if B<20 and D>max(T,(1408+22*B)/9):out.add(P)
        if B<20 and D>max(T,(1496+20*B)/9):out.add(R)
        return out
    out={A,C,K,H}
    if D<396+5*B/4:out.add(U)
    if D<408+2*B:out.add(V)
    if D<min(306+5*B/4,312-B):out|={P,R}
    return out
Bs=list(map(Q,[1,2,8,12,19,20]))+[Q(1,100),Q(8,3),Q(224,19),Q(199,10)]
c=0
for B in Bs:
    cuts={Q(0),B,(B+544)/3,(1408+22*B)/9,(1496+20*B)/9,272+B,306+5*B/4,312-B,396+5*B/4,408+2*B,Q(528)}
    cuts=sorted(d for d in cuts if 0<=d<=528)
    ds=set(cuts)|{(a+b)/2 for a,b in zip(cuts,cuts[1:])}
    for D in sorted(ds-{0}):
        scores={v:max(Q(g,s) for g,s in zip(gs,S(B,D))) for v,gs in G.items()}
        eta=min(scores.values());expected=min(max(Q(3,136+B),Q(3,136+D)),Q(6,B+D))
        assert eta==expected,(B,D,eta,expected)
        near={v for v,s in scores.items() if 2*s<3*eta}
        assert near==predict(B,D),(B,D,near,predict(B,D))
        c+=1
print('FULL DIRECTION CHECK PASS',c)
