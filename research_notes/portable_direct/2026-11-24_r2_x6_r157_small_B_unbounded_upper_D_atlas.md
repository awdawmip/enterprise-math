# X6 R157 — Complete small-B upper-D fan, including the unbounded tail

2026-11-24. Author analytic proof and exact finite certificate, NOT_REVIEWED. Independent informed portable research continuing R156@994068e27c1031956bac257482d3360dd45ad9a3. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@0687aa24f5402da3b35f914dd6907967a9805b94. The static conditional six-gap observer on the selected signed three-axis restriction of X6 is used unchanged; all six joint channels are retained. No native physical evolution or residual attribution is claimed.

## Statement
For 0<B<=20, D>=528, w=(136,B,176,D), use q(v)=max(sum positive coordinates, sum absolute negative coordinates), Port 10, one sign representative per nonzero triple. h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), g=absolute pair differences in order 01,02,03,12,13,23. s=(136+B,312,136+D,B+176,B+D,D+176), F=max_j g_j/s_j, eta=min F, N={v:2F<3eta}.

The exact optimum is
- 6/(B+D) for 528<=D<=528+2B;
- 2/(B+176) for 528+2B<=D<=1056+5B;
- 12/(B+D) for D>=1056+5B.

All seams agree. The complete strict near set is described by the following six rows:
- A=(1,0,0), C=(5,-4,1): D<1584+8B.
- K=(5,-1,0): D<1224+8B.
- H=(9,-5,1): D<528+2B.
- J=(4,-1,0): 704+3B<D<2448+17B.
- E=(6,-4,1): D>704+3B.

Thus the successive strict near counts are 4,3,5,4,2,1. At the entry wall itself J,E are excluded; at each exit wall its exiting rows are excluded. The order is strict for every 0<B<=20: 528+2B<704+3B<1224+8B<1584+8B<2448+17B. In particular A,C exit together well before the conservative R148 tail boundary 1872-B (difference 288-9B>=108). This proves the exact earlier two-direction onset and closes the entire small-B high-D continuation, not merely the bounded bridge. R156 supplies the full lower-D part, with exact agreement at 528.

## Proof
Use the finite direction generator of R121/R156, covering all 1935 sign representatives. The three regions have vertices or lower edge:
I: (0,528),(20,528),(20,568), candidate n/L=6/(B+D), witness A.
II: (0,528),(20,568),(20,1156),(0,1056), n/L=2/(B+176), witness A.
III: lower edge (0,1056),(20,1156) plus the positive D recession ray, n/L=12/(B+D), witness E.
B=0 is used only to certify affine inequalities, not to expand the claimed positive-weight domain.

For r=2 or 3 define slack_j=2*g_j*L-r*n*s_j. For every direction the attached finite certificate finds one channel nonnegative at all vertices for r=2. For r=3 it does the same for every direction outside W={A,C,K,H,J,E}. In III it additionally checks the nonnegative D slope 2*g_j-r*n*1_{j in {03,13,23}}. These are affine functions, so vertex and recession tests prove the inequalities over the whole corresponding real region, including unbounded D. For the listed witness all r=2 slacks are nonpositive, with equality in channel 13,12,13 respectively, including the slope check in III. Consequently eta=n/L and outsiders cannot be strictly near.

The six retained gap rows are A=(1,3,7,2,6,4), C=(1,3,5,2,6,8), K=(2,3,4,1,6,7), H=(0,3,6,3,6,3), J=(1,0,11,1,12,11), E=(0,0,12,0,12,12).
In I the near condition is g_j*(B+D)<9*s_j. A,C,K satisfy it on the whole triangle for positive B; H's channel 12 is D<528+2B and its other channels are strict. J,E fail channel 13 (12>9). In II the condition is g_j*(B+176)<3*s_j. H fails by equality in 12. A,C,K satisfy all channels throughout (check affine slacks at the four vertices). J,E need D>704+3B from channel 13; their other D-dependent bounds are weaker since B<=20<136<176 and g_03,g_23<=12. The fixed channels of both are strict. In III the condition is g_j*(B+D)<18*s_j. H fails channel 12 throughout. The upper bounds for A,C from 01,02,12 respectively are 2448+17B,1872-B,1584+8B, with the last smallest for B<=20; their other channels are strict because g<=18 and B<136,176. For K the corresponding upper bounds are 1224+8B,1872-B,3168+17B; the first is smallest. For J the nonzero fixed channels 01 and 12 give D<2448+17B and D<3168+17B, with the first controlling. E always satisfies all six. The strict endpoints and all joins follow directly. The R156 lower region and this result together classify every positive real D at 0<B<=20.

## Actual execution evidence
Local Python exact run of the embedded checker below returned:
```
2 [1861, 61, 10, 1, 2, 0]
3 [1809, 104, 16, 0, 0, 0]
2 [1861, 61, 8, 3, 2, 0]
3 [1809, 104, 13, 1, 2, 0]
2 [1861, 61, 8, 3, 2, 0]
3 [1809, 104, 13, 1, 2, 0]
UNBOUNDED CERTIFICATE PASS
FULL DIRECTION CROSSCHECK PASS 166
```
Each r=2 histogram totals 1935, each r=3 totals 1929. The continuous proof is the finite affine/recession certificate, not the 166 rational sample cross-checks. Exact integers/Fraction implement the frozen six-gap static observer, without pi/trigonometry or external model evolution. Independent review remains pending.

## Reproduction (standalone Python 3)
```python
from itertools import product
from fractions import Fraction as Q
G={}
for v in product(range(-10,11),repeat=3):
    if not any(v) or next(z for z in v if z)<0 or max(sum(max(z,0) for z in v),sum(max(-z,0) for z in v))>10:continue
    x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    G[v]=tuple(abs(h[j]-h[i]) for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
assert len(G)==1935
S=lambda B,D:(136+B,312,136+D,B+176,B+D,D+176)
A=(1,0,0);C=(5,-4,1);K=(5,-1,0);H=(9,-5,1);J=(4,-1,0);E=(6,-4,1)
W={A,C,K,H,J,E}
regions=[([(0,528),(20,528),(20,568)],6,lambda B,D:B+D,A,4,False), ([(0,528),(20,568),(20,1156),(0,1056)],2,lambda B,D:B+176,A,3,False), ([(0,1056),(20,1156)],12,lambda B,D:B+D,E,4,True)]
for vertices,n,L,w,active,ray in regions:
    def slack(g,j,B,D,r):return 2*g[j]*L(B,D)-r*n*S(B,D)[j]
    def slope(g,j,r):return 2*g[j]-r*n*(j in (2,4,5))
    for r,exclude in [(2,set()),(3,W)]:
        hist=[0]*6
        for v,g in G.items():
            if v in exclude:continue
            js=[j for j in range(6) if all(slack(g,j,B,D,r)>=0 for B,D in vertices) and (not ray or slope(g,j,r)>=0)]
            assert js,(r,v);hist[js[0]]+=1
        print(r,hist)
    assert all(all(slack(G[w],j,B,D,2)<=0 for j in range(6)) and slack(G[w],active,B,D,2)==0 for B,D in vertices)
    if ray:assert all(slope(G[w],j,2)<=0 for j in range(6)) and slope(G[w],active,2)==0
print('UNBOUNDED CERTIFICATE PASS')
def predicted(B,D):
    n={E} if D>704+3*B else set()
    if 704+3*B<D<2448+17*B:n.add(J)
    if D<1584+8*B:n|={A,C}
    if D<1224+8*B:n.add(K)
    if D<528+2*B:n.add(H)
    eta=min(max(Q(6,B+D),Q(2,B+176)),Q(12,B+D))
    return eta,n
count=0
for B in [Q(1,1000),Q(1),Q(8,3),Q(8),Q(10),Q(224,19),Q(19),Q(20)]:
    cuts=sorted({Q(528),528+2*B,528+4*B,704+3*B,1056+5*B,1224+8*B,1584+8*B,1632+11*B,1872-B,2448+17*B,Q(10**6)})
    for D in sorted(set(cuts)|{(a+b)/2 for a,b in zip(cuts,cuts[1:])}):
        scores={v:max(Q(g,s) for g,s in zip(gs,S(B,D))) for v,gs in G.items()}
        eta=min(scores.values());near={v for v,f in scores.items() if 2*f<3*eta}
        assert (eta,near)==predicted(B,D),(B,D,eta,near,predicted(B,D));count+=1
print('FULL DIRECTION CROSSCHECK PASS',count)
```

## Next
Complete B>20, D<528 with the same affine/recession approach; in particular R155's loss of synchronization at B=304/3. Then unify all positive (B,D) without changing the conditional observer. Original current task read request r2-20261124-0510-x6-task-read was RUNNING when proof was prepared; no formal CLAIM or Result. Previous lane's Researcher EM-DIRECT-AE5AD5 and Activity RA-B60559848FD879270DCA6317 were recovered as metadata only (registration original r2-20261124-0310-r155-own-session-v1); activity association requires actual authorized update, not implied by this file.
