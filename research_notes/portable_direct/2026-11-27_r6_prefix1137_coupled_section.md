# PREFIX-1137 — Two coupled BRC moments and global seven-observer section

Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. Date: 2026-11-27 (research batch R6). Own original researcher EM-DIRECT-780BBE / TASK_RESEARCH registration r6-20261123-2358-session-start-own-v1 SUCCEEDED; own managed-session recovery metadata verified, underlying session not closed, no runs, execution_authorized=false. Current owner inventory r6-20261127-2352-leased-read SUCCEEDED/error=null, as_of 2026-11-27T15:53:47.906205Z, Source f34fc13a7fff1fe43ba0de68dd794163695f09b3, LEASED tasks=[], next_cursor=null. No new CLAIM or protected shared-state write. Global main entry bytes verified at 05c90a85be128762eacb9c89bbe3217b444e0ce9.

## Scope and inherited inputs
Continue PREFIX-1136 at 5398060227764faceb139720385c09dc87578bb1:research_notes/portable_direct/2026-11-27_r6_prefix1136_coupled_moment_exclusion.md, PREFIX-1135 at 3b05acc11534008c25b08b7ab228902a89ac22e2 and PREFIX-1134 at 1be6afaab6e3bd6682feffc7ca067d96f32cf18c. Reuse frozen P000 V5 and joint/world/residual companions f42f2906d77f24085c123f3ccfe9667d41caa96d, 9600 shared anchor, signed reversal -5, 5q cover, O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. Conditional on inherited Stage46 carrier/analytic and integral-tail bounds; historic 8400/8800 exit uncertainty remains. The following are auxiliary algebraic observers and integer relation coordinates, not new native spatial axes. No new native computation, classical comparison, high-order anchor inverse or moment generation. Both coupled observations at order 11200 were already computed in PREFIX-1136; reuse the archived second row (SHA256 manifest verified). The two coupled rows were separately checked against the archived exact moment floors, nominal row and all twelve shared anchor contributions.

## 1. Global transport with two coupled channels
Let r=p/q, u=h/q be the excluded PREFIX-1134 line, x=sqrt(36/(1+r)), t* the true root. Write t*-x=J(t*,x)(rho-r), J=-x^2 t*^2/(36(t*+x)); its range lies in [-T_hi^3/72,-T_lo^3/72] when x,t* in T. Set A enclosing F', D enclosing G'_{c0}-sF', DG=D+sA, AJ=A J, DJ=DG J; am,aj,dj are respective midpoints of A,AJ,DJ. With G_{u}=G_{c0}+(c0-u)F', the mean value theorem gives
F(x)=-AJ_actual (rho-r),
G_u(x)=(c-c0)F'(t*)-(u-c0)F'(x)-DJ_actual(rho-r).
The three radial moment residuals and two coupled moment residuals have true values bounded by their existing payments. Thus the affine target in observer units is
L=(-aj*(rho-r), am*(c-u)-dj*(rho-r), 0,0,0,0,0).
Replace products by midpoint products with errors E1=mag(AJ-aj)mag(R-r), E2=mag(A-am)(mag(C-c0)+abs(u-c0))+mag(DJ-dj)mag(R-r). With G=10^125, both ceil(G*Ei)=1, even using the wider PREFIX-1132 marginal box in the independent replay. Preserve all twelve shared coefficient columns and add these two payments to the already rounded error coordinates. Then G L belongs to m+sum[-1,1]C_j+[-e,e], a seven-observer outer enclosure. Every integer direction n gives |G*n.L-n.m|<=sum_j|n.C_j|+sum_i|n_i|e_i. Each inequality alone is necessary; we do not assert complete facet enumeration or inner feasibility.

## 2. Targeted support directions
A full cofactor enumeration attempt timed out before output. Instead take the PREFIX-1136 separator padded by zero, the cofactor normal of the first six shared columns, and normals from any five of those six columns together with one of the seven independent error-axis columns. Canonicalize by gcd and sign, omit zero, deduplicate. This yields 43 distinct directions. The cofactor of six leading columns is valid because each column is annihilated by the alternating-minor identity; no heuristic basis choice enters the validity of any inequality. Clipping the old 28-vertex joint outer section by the two halfspaces of each direction gives 16 effective cuts and 16 final vertices. Independent replay starts from a wider outward-rounded PREFIX-1132 rectangular enclosure, uses recursive Laplace determinants rather than Bareiss, clips in sorted normal order and reproduces the same section widths and integer search result. Thus previous section vertices are not a load-bearing input to that replay.

rho width 4.101624829506882e-101 (old PREFIX-1134 3.46257e-92, ~8.44e8 improvement).
c width 1.5216386212196777e-98 (old 1.04457e-91, ~6.86e6 improvement).
A positive-slope band chosen from section edges has width 1.501955192620779e-98, slope 4.7990592501510525. This is a useful direction for the integer basis, not a universal optimized normalized width. All widths displayed approximately; exact fractions retained in the execution evidence.

## 3. Complete arithmetic enumeration
For all L>=L0=10^100 inherit delta=rho-p/q in [0,K/L^2], eta=h/q-c in [0,H/L], q>=q0=544447235321021556325566186117974922693, E=400000, K=d_hi+2E/q0, H=2d_hi+4E/q0. Add [-K/L0^2,0]x[0,H/L0] to the whole affine section by exact convex hull of its vertices plus rectangle corners. For each row (a,b,e) of the unimodular V below, the range of a q+b p+e h equals the extrema bound obtained from q in {q0,Q} and the hull vertices: linear in the hull point for fixed q and affine in q for fixed hull point. Enumerate every integer in the resulting box, invert V (det +/-1), test q range, gcd(p,q)=1 and every convex hull inequality. Thus no relation is omitted, regardless of the heuristic used to select V.

Q=10^66: [(0,0),(0,0),(-1,-1)], one integer point, zero survivors.
Q=3*10^66: [(0,1),(0,2),(-4,-1)], 24 integer points, five survivors; exact minimum q=1842587604597899205836070659413418778049462046290172681472044737135.
Hence any two true anomalies in an inherited dyadic window with L>=10^100 have b-a>=q>=q_min. The five lines are survivors of necessary conditions, not witnesses of actual anomalies. Combining q^2<4EL/d for the triple case, q<=sqrt(L) for close pairs, and the previously covered smaller windows, gives first not-excluded dyadic starts (10^8*2^j):
L3=32278123476086357370698989650037648429121322410365293910383241956758095275210514932870566916001722892948789649659343667200000000 (~3.22781234761e127)
L2=4230758200257591033292257971409734654901789970971399803421752289756197063912392613281210946814177823024583756960149493147238400000000 (~4.23075820026e132).
Both are 2^28 times the PREFIX-1136 endpoints. No sharpness claim; continuous integer endpoint remains 4.72478e43, remaining endpoint candidate and fixed-spectrum unbounded separation, B_fix,odd(32) open.

## 4. Compact input certificate
All integers serialized as decimal strings to retain exactness. First six rows from the immutable PREFIX-1136 paper; seventh from archive extra_coupled_1136.json, actual verified nominal floor, columns and observation floor. e here excludes the two new unit payments. The prior derivative bounds and helpers are in the immutable PREFIX-1134 verifier a26d0589bb05b8c5fb07371840976426b27aa512:research_notes/portable_direct/2026-11-27_r6_prefix1134_verify_section.py. No new tail or native correspondence proof asserted.

```json
{"line":["39842427926119417299262046818826239782916070158838139476777507","854223117766075752740545225414351655926157527291751525026511332","3950018562885944348193743729715096500004840471989124645725608269"],"m":["1578749725436294200191847058759791294255121","-8016680709457034915696742911950186983902114","-5125943210844204295","-17950719237217173155","-39478465139117230238","1001163861891333451","74181271838224845"],"C":[["3744138645775498910841297928701976010966640315","-87125244309961656188605995439254644350120196792","-9439727292964913715644","-33057192159364659829729","-72701511035128092066755","-91220000364952284887","-2448023579049005246"],["-161039656349520894471888359937205864380223","3746573643488776666579887859681069553495355","563814399574156417","1850874067992514339","3907417520264524189","4344473217818122","146091831130612"],["2298254077145580893797380295013148626","-53458267472769732129352373972486955517","-12547204637116","-36609963069810","-72451756015164","-77348963365","-2621002235"],["-47952155714854405058160188075338","1115182088175091721930947313324566","543387970","1189019200","2091474020","2091906","65022"],["970258271083964521363312982548236062773","-72120495286988764488827521413216860724180","0","0","0","172186817276751308897194","0"],["-466583415180187615239670236197498944780635","40347985749191228916185797857499750580988601","0","0","0","0","516606560948510513646727"],["-4422552409729","-14544658619171738","66","64","61","-1","-1"],["-30551863247001164","2239318452415096038","-14","-13","-13","-1","0"],["-36535640931316125","2363560184834305474","-1","-1","-1","-1","0"],["814480300480595744","-19198820539636586492","0","0","0","0","-1"],["5395617291183169","-401062895330366980","0","0","0","0","0"],["-1525853534519761","131948789140695908","0","0","0","0","0"]],"e":["778398383415451143","7186278565963893173986745928764695745","120600466","120600014","120600014","120600014","120600014"],"normal6":["-13080203160992911088329295334758188735877473315329159902961449684069601241446922502419816500372952339274064982850089228","-151259245010244209386279251388273530096304258830003232825978912617163961903162467498052891451885490206564754282791780","-15149794751240068993211826331977397196625533413814857399776976763088027530477147265497524081246488770667150912642804915131414613963743950614198","16710421614617855830236655250213739062726915355980433739946510629583989420811048700273599245743036474966492005974094267579211630758468001955885","-6123466713672218932803955940673651265970619640785789446081834397682359374440390214158736673843712619806112168035072050904704437663816885578185","10350871604023994439141032481296877146400610656621516895770865310014952020965063228890792927564039339648624284673685377657930919049726"],"row2":{"k":11200,"channel":2,"m":"74181271838224845","cols":["-2448023579049005246","146091831130612","-2621002235","65022","0","516606560948510513646727","-1","0","0","-1","0","0"],"error":"120600014","observation_floor":"189048166976163685859175999109378674750763053669692844297727135888057394751533498506042089131985362482891635964"},"V":[["373579431436543501937698643266114888","-17396852651425369601182052411051616","-5953860747523108004924389269041"],["-113212095101368799340418613077541322","5460490004045610266768042818319529","-38944641372185653846695585041524"],["80512086630290408821117731873270125","-3637154578019681883554311829869459","-25532914266107527130269343011013"]],"qmin":"1842587604597899205836070659413418778049462046290172681472044737135"}
```

## 5. Replay
Save the JSON as cert1137.json; download PREFIX-1134 verify_section.py at its pinned path above. The following reproduces the independent section and arithmetic algorithm using the compact input instead of the separate parent archive files. The actual local independent run used the identical archived rows, the wider prior marginal rectangle and the same fixed V, with the original source data split across the files in the evidence bundle. Full source and logs: coupled_section_1137.py/log, extended_1137.py/log/json, verify_coupled_1137.py/log, verify_rows_1137.log. The full-enumeration attempt timed out and produced no usable result; only the targeted-direction calculation is claimed.

```python
from fractions import Fraction as F
from itertools import product
from math import ceil,floor,gcd
from pathlib import Path
import json
ns={};exec(Path('verify_section.py').read_text().split('assert A[1]<0')[0],ns)
T,R,C,A,D,s,c0,d=[ns[k] for k in ('T','R','C','A','D','s','c0','d')];G=10**125
mul,mid,mag,sub,clip,det,normal,dot=[ns[k] for k in ('mul','mid','mag','sub','clip','det','normal','dot')]
DG=tuple(x+y for x,y in zip(D,mul(s,A)));J=(-T[1]**3/72,-T[0]**3/72)
AJ=mul(A,J);DJ=mul(DG,J);am=mid(A);aj=mid(AJ);dj=mid(DJ)
c=json.load(open('cert1137.json'));q,p,h=map(int,c['line']);r0,u=F(p,q),F(h,q)
assert T[0]**2<=36/(1+r0)<=T[1]**2 and A[1]<0
P=[(R[0]-r0,C[0]-u),(R[1]-r0,C[0]-u),(R[1]-r0,C[1]-u),(R[0]-r0,C[1]-u)]
er=[ceil(G*mag(sub(AJ,aj))*mag(sub(R,r0))),ceil(G*(mag(sub(A,am))*(mag(sub(C,c0))+abs(u-c0))+mag(sub(DJ,dj))*mag(sub(R,r0))))]
assert er==[1,1]
m=list(map(int,c['m']));cols=[list(map(int,v)) for v in c['C']];e=list(map(int,c['e']));e[0]+=1;e[1]+=1
U=cols+[[e[i] if i==j else 0 for i in range(7)] for j in range(7)]
norms=[tuple(map(int,c['normal6']))+(0,),normal(U[:6])]
for omitted in range(6):
    for axis in U[-7:]:norms.append(normal([U[j] for j in range(6) if j!=omitted]+[axis]))
norms={tuple(-x for x in n) if next(x for x in n if x)<0 else n for n in norms if n}
assert len(norms)==43
for n in sorted(norms):
    v=dot(n,m);sp=sum(abs(dot(n,w)) for w in U)
    a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am
    P=clip(P,a,b,v+sp);P=clip(P,-a,-b,sp-v);assert P
print('widths',float(max(x for x,y in P)-min(x for x,y in P)),float(max(y for x,y in P)-min(y for x,y in P)))
V=[list(map(int,v)) for v in c['V']];D0=det(V);assert abs(D0)==1
W=[[(-1)**(i+j)*det([r[:i]+r[i+1:] for k,r in enumerate(V) if k!=j])*D0 for j in range(3)] for i in range(3)]
assert [[dot(v,w) for w in zip(*W)] for v in V]==[[1,0,0],[0,1,0],[0,0,1]]
q0=544447235321021556325566186117974922693;E=400000;L=10**100;K=d[1]+F(2*E,q0);H=2*d[1]+F(4*E,q0)
hullns={};exec('def hull(pts):'+Path('verify_section.py').read_text().split('def hull(pts):')[1].split('P=hull(pts)')[0],hullns)
HP=hullns['hull']([(r+r0-x,y+u+z) for (r,y),x,z in product(P,(0,K/L**2),(0,H/L))])
ineq=[]
for (x,y),(v,w) in zip(HP,HP[1:]+HP[:1]):
    a=w-y;b=x-v;z=a*x+b*y
    assert all(a*r+b*t<=z for r,t in HP);ineq.append((a,b,z))
for Q in (10**66,3*10**66):
    box=[]
    for a,b,f in V:
        vv=[q*(a+b*r+f*t) for q,(r,t) in product((q0,Q),HP)]
        box.append((ceil(min(vv)),floor(max(vv))))
    ans=[]
    for n in product(*(range(a,b+1) for a,b in box)):
        q,p,h=(dot(w,n) for w in W)
        if q0<=q<=Q and gcd(p,q)==1 and all(a*p+b*h<=z*q for a,b,z in ineq):ans.append((q,p,h))
    ans.sort();print(Q,box,len(ans),ans[:1])
    assert box==([(0,0),(0,0),(-1,-1)] if Q==10**66 else [(0,1),(0,2),(-4,-1)])
    assert len(ans)==(0 if Q==10**66 else 5)
q=ans[0][0];assert q==int(c['qmin'])
L3=L2=10**8
while L3<=d[0]*q*q/(4*E):L3*=2
while L2<q*q:L2*=2
print(L3,L2)
```

## Next
Test the five surviving relations with the same seven-observer shared coefficient enclosure and actual scale-dependent conditions, then add the d relation or a targeted additional BRC moment only if the current information is proved insufficient. Keep earlier failed full enumeration as a resource result, not as impossibility. Activity association and independent review pending; no Task completion or new native attribution.
