# PREFIX-1142: High radial moment joint exclusion beyond the full bounded fiber

Date: 2026-11-28. Continuation of EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322 (historical identity; own original managed registration status SUCCEEDED, nonrevoked, unexpired and not closed; no formal execution authority or CLAIM asserted). Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Inputs and scope
Frozen P000 V5: f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessor 9f2dda4631b22dc23ec8963dc8ea6aca5752323f:research_notes/portable_direct/2026-11-28_r6_prefix1141_full_observer_fiber.md. All 151 entries of the predecessor execution manifest were verified in the local extraction; the compact independent verifier was actually rerun. Reuse its immutable fixture fd5b29757feda778fdc120f85ecb32c1b67cb847:research_notes/portable_direct/prefix1141/fixture1141.json and verifier 9514c30135e1d76bdb5581e2b4d1fccdaf491f3f:research_notes/portable_direct/prefix1141/verify1141_compact.py. The predecessor proved eight primitive relations in the finite domain q<=2*10^69, L>=10^114, one excluded and seven interior witnesses in the ten-observer affine outer model. This work tightens that model without changing the frozen spectrum, anchor, or Stage46 assumptions. It is an auxiliary exact integer/rational observer calculation, not a new native world computation or a formal task result.

## New observations
Reuse the inherited integer moment recurrence in anchor_moments.cpp from PREFIX-1141 execution archive, compiled with g++ -O3 -lgmpxx -lgmp. Command: ./anchor_moments 14400 16000 20000. Actual output (floor on grid 10^-120):
```
416564040236936803113376722851344511944266272700142033332693855886238119671642785168616243068140179713333358924794087
375114346717930298502489731039914577088539543579484453935388541689102726588789368476139375191752808451063172536830881
300414171868423160687796749897683349191420736702466724671406351795708151004628468610972116167888722129715197049516908
208166878737484809363127838972732086266906373988310398092486250816067158229106332983845295199090389939720509789893
88838862534540679822505669816199891416113133108555357979906730328378290833388999415250698371218029303814453220
```
First three lines are radial k=14400,16000,20000; last two are the k=14400 coupled moment outputs, not used in the result. SHA256 of the raw output: 788ff109086da94026658a5fe77ecf835a023a6531affd5574855662f9d0ecde.

Reproduce radial observer rows using predecessor extra_moment_1136.py with input moments1142.txt, ks=[14400,16000,20000], output extra_radial1142.json. Its inherited basis reconstruction is replay_9600_n300_gmp.py and anchor_compact.json. The radial moment row uses the same four Frobenius columns, two zero integration-constant entries, beta integrals, 10^-120 floor enclosure, and the same twelve common weighted and rounding directions. For each k the inherited error bound is (35/36)^k+10^-120+sum(b[3] for b in basis)+(4*(N+1)+1)*10^-120; pay ceil(10^125*bound)+13, including one center and twelve column grid-rounding errors. All three row constructions actually completed. Independent support-certificate replay below verifies the consequence from these rows; no independent recomputation of the analytic anchor or moment-row enclosure is claimed. The attempted new coupled-row construction timed out before its basis initialization finished; no new coupled row is used.

## Joint separation
Append these three rows to the existing ten observations, retaining all twelve shared columns and thirteen independent error axes. For n in Z^13, write a=-G(n[0]*aj+n[1]*dj), b=G*n[1]*am, z=n.m, S=sum_j|n.C_j|+sum_i|n_i|e_i, G=10^125. The affine target for (rho,c) has first two coordinates -G*aj*(rho-r), G*(am*(c-u)-dj*(rho-r)) and all other coordinates zero. Therefore |a(rho-r)+b(c-u)-z|<=S. With inherited 0<=rho-p/q<=K/L^2 and 0<=h/q-c<=H/L, v=a(p/q-r)+b(h/q-u)-z must satisfy
v<=S+max(0,-a)K/L^2+max(0,b)H/L,
-v<=S+max(0,a)K/L^2+max(0,-b)H/L.
Both payments decrease for L>=10^114. A strict failure at the starting L excludes throughout that tail. Exact integer support arithmetic checks the same single normal for all seven remaining relations; floating LP was used only to propose it (old ten pivots plus three new error axes). Ratios in increasing q order: 40.67192930156569, 33.41880905813896, 27.44042571229668, 22.42787175118752, 18.16459013126597, 14.494263079942682, 11.30122819231634. All strictly >11 by rational comparisons. The prior eight-candidate enumeration and first exclusion remain unchanged. Consequently under the inherited certificates every genuine relevant pair has b-a>=q>2*10^69 for all L>=10^114. Dyadic three-anomaly first unexcluded window 3.384606560206073e133; close-pair first unexcluded window 4.436271510593304e138 (base 10^8, dyadic steps). Both derived by the exact threshold loops in the verifier. No claim that these new bounds are sharp. Continuous integer endpoint 4.72478e43 unchanged; unbounded strict separation and B_fix,odd(32) open.

## Compact exact verifier
Save the following code as verify1142_compact.py beside the two immutable predecessor files. It uses no numerical LP and replays complete predecessor enumeration and exact new support inequalities. The local actual execution used the same rows, normal and assertions read from JSON rather than embedded (verify1142.py); its log ended PASS. Reproduction archive also contains the full new radial rows, raw recurrence output, LP proposal code, and exact verifier.

```python
from fractions import Fraction as F
from pathlib import Path
import runpy
D=runpy.run_path(str(Path(__file__).with_name('verify1141_compact.py')))
G,L,K,H,aj,am,dj,r,u=[D[k] for k in ('G','L','K','H','aj','am','dj','r','u')]
rows=[
(-537378197081301477868,[-989602582095486220662295,47458609622835095805,-757675616387427,17760413241,0,0,46,-8,-1,0,0,0],120600014),
(-837787403044797986152,[-1542816606340676775418698,72876196576253439392,-1143655813704068,26286777131,0,0,41,-7,-1,0,0,0],120600014),
(-1550395940623926518380,[-2855109202824325639444683,132263626931599235587,-2031957495680465,45626599285,0,0,33,-5,-1,0,0,0],120600014)]
m=D['m']+[v[0] for v in rows]
e=D['e']+[v[2] for v in rows]
C=[v+[w[1][j] for w in rows] for j,v in enumerate(D['cols'])]
n=[
-269053851363234464890791408940147772567701067414117507995598488305743466568279883322848790197933416845206940660383929639836826005500732188519244,
-11514005515759551890230976122062602002344232641072254019602050702860049003496077111571005268237353076270809030558410450279132063517347337807455,
-902022059430400519593799780967529572960599733076614815710413118226208038542979808993673378891394024177461955149575751640467129047297147744094296309079,
0,0,
-3306548462223062889951480213135657489503104979540539010664757734283945813307677159991737186530471342732866938209973758829940986656997183123916453818835611059352,
656265117901446561928360969736268248913836885343541765712271453290025502369910952036612644854407669558984589792535604557781314237956481528879333501258962928381445,
0,0,
-3481337880564683052573326927587406230589060673690932610082487807756703266424163933369045683765447310540466996940650797870894415287727195935136888894530,
3072357503846484701485393125782692902016947766082783217288427157557696071150452216204938421152430551403981618082174052663906335628064538309186093129160635605080920,
0,
-2540986297023077666225605978359975928390014674270872017725923254255006470730884638585511943128924073801345086474690314857191718230067019120005086379330607741891460]
dot=lambda x,y:sum(a*b for a,b in zip(x,y))
a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;z=dot(n,m)
S=sum(abs(dot(n,v)) for v in C)+sum(abs(v)*w for v,w in zip(n,e))
assert S>0 and len(D['lines'])==8
for q,p,h in D['lines'][1:]:
    v=a*(F(p,q)-r)+b*(F(h,q)-u)-z
    ratio=max(v/(S+max(0,-a)*K/L**2+max(0,b)*H/L),
              -v/(S+max(0,a)*K/L**2+max(0,-b)*H/L))
    assert ratio>11
    print(q,float(ratio))
Q=2*10**69;L3=L2=10**8
while L3<=D['d0']*Q*Q/(4*400000):L3*=2
while L2<=Q*Q:L2*=2
print('PASS',Q,L3,L2)
```

## Next
Transport the one separating direction and further sparse normals into a 13-observer global affine section, then re-enumerate to 10^70. The three new radial rows have demonstrable joint information gain even though the two integration-constant coordinates were not directly changed. Determine the remaining fiber before adding the two k=14400 coupled rows; their integer raw moment values are saved but their row enclosures have not completed. Review of inherited anchor exit and independent mathematical review remain pending.

## Provenance
Global entries read at main and their blobs matched immutable 5f073f50b470c398e492c038ba798f5e2e0e3c4e; current portable protocol, method, P000 frozen source, joint-preservation and worldview read. Owner read r6-20261128-0450-owner-read-v1 SUCCEEDED/error=null, snapshot 2026-11-28 04:50:30.985431+08, Source f712aea5da8337ccb84e0b1dd50ffe0ce8412e9b, 547 tasks, LEASED filter empty, cursor null. No formal claim or shared task-state mutation. Activity association separate.
