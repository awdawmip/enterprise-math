# PREFIX-1144: Precision-budget separation with two coupled moments

Date: 2026-11-28. Continuing EM-DIRECT-780BBE / TASK_RESEARCH, original own managed registration MCP-f6d93209fc8e4c5bb2c3b44f69a47174 verified nonrevoked/not closed by recovery_status; no formal CLAIM or shared task mutation. Status AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Inputs and scope

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d; joint observer and Heartbeat contracts at same pin. Current account main 99475e82dae37753630c9ee46dfaba87bcbf104f verified; current portable and normative rules read. Predecessor 367595a950c0cc3a3c95ebc3545236e0a64d2d2f:research_notes/portable_direct/2026-11-28_r6_prefix1143_thirteen_observer_section.md. Reuse its eight exact lattice relations (full 1460 tuple enumeration rerun), 9600-order shared anchor, 301-term Frobenius basis, and Stage46 analytic conditions. Predecessor archive PREFIX1143_SHA256SUMS verified. Frozen raw moments1142.txt SHA256 788ff109086da94026658a5fe77ecf835a023a6531affd5574855662f9d0ecde matches PREFIX-1142 at a3ede9ce612c4f08d420937b56559812ea62ca32, which also records the exact five raw integers. No new original moment or anchor calculation. Auxiliary rational observer coordinates, not native spatial dimensions or a native simulation.

Owner query r6-20261128-0651-owner-read-v1 SUCCEEDED/error=null, source 024ba558f0bb509a5be04ad8cce5b8ae97f0aec9, snapshot 2026-11-27T22:52:42.242576Z, 547 tasks, LEASED filter empty. No formal claim.

## First experiment: adding two coupled rows without tightening

The pending k=14400 channels j=1,2 were actually constructed using the inherited recurrence (coupled1142.py). With its original 10^-120 per-term flooring both new row radii are 120600014 units at G=10^125. All eight PREFIX-1143 witnesses extend exactly: for an old witness v set each new independent coordinate to -(m_new+C_new*v_shared)/e_new. Their absolute values are at most 0.611 for channel 1 and 0.460 for channel 2, verified by evaluating the old exact rational coefficients. Thus merely adding the two rows at the old arithmetic budget fails to exclude any of these eight in the enlarged affine outer model. This is local to those witnesses, not a general redundancy assertion.

## Lemma: decouple moment quantization from observer-row arithmetic

Let raw moment integer y=floor(H*Y), H=10^120, so Y belongs to [y/H,(y+1)/H]. Use its midpoint (2y+1)/(2H), with observation radius 1/(2H). Compute the observer basis row separately: floor each certified term at J=10^155, after proving its outward interval gives the same floor at both endpoints. For the exact anchor coefficients alpha_i, the full shared anchor satisfies |alpha_i|<1, checked using |center_i|+sum_l|W_il|+dr_i<1 for every i. The 4(N+1)+1=1205 possible nonzero terms, N=300, have total row arithmetic error at most 1205/J when paired with these coefficients. This separates the error due to the raw readout from the artificial arithmetic grid, without changing the scientific moments.

For a radial row the inherited analytic tail payment is (35/36)^k + sum of the four basis tail bounds. For coupled channel j=1,2 use 6^(j+1)/(j+1)*(35/36)^k plus the same basis tail sum, as in the inherited coupled construction. Keep this analytic envelope unchanged. Let E be that analytic payment plus 1/(2H)+1205/J. The integer row center and all twelve shared coefficients are separately floored at G; each rounding can cost at most one grid unit because the shared coefficients lie in [-1,1]. Hence e=ceil(G*E)+13 is sufficient. This establishes the new joint enclosure given the inherited analytic tails; it is not an independent reproof of the inherited anchor enclosure.

Actual basis tail display: 5.45499e-185, 7.04818e-185, 2.73309e-184, 1.38864e-183. Actual integer e=50014 for each of five rows (radial 14400,16000,20000; coupled 14400 j=1,2). Old e=120600014, improvement about 2411.32-fold. All same-floor tests passed at J. The original raw moment values remain identical. Reproduction: use replay_9600_n300_gmp.py and anchor_compact.json from PREFIX-1143 archive; keep integ(k,i,N+5) (outward 10^-260 integral recurrence) and basis unchanged. For radial use sum floor(c[0]*ints[half][off+n]*J)/J; for coupled use sum floor(c*ints[half][off+n+1]*J)/J from h[j-1] and row[3+j]=floor(ints[0][j]*J)/J. Row center = dot(row,cc)-(2*y+1)/(2*H), common columns = row*W followed by row_i*dr_i. The exact row construction scripts radial1144_tight.py and coupled1144_tight.py and outputs are in the execution bundle. The earlier loose and partially tightened trials are retained.

## Fifteen-observer result

Replace the three high radial rows of PREFIX-1143 with their tighter versions; append the two tighter coupled rows. Retain all ten earlier rows and all twelve shared columns. At L0=10^114 use the inherited affine transfer:
a=-G*(n[0]*aj+n[1]*dj), b=G*n[1]*am, z=n.m, S=sum_j|n.C_j|+sum_i|n_i|e_i.
For x=p/q-r, y=h/q-u, let v=a*x+b*y-z. Necessarily
v <= S+max(0,-a)*K/L0^2+max(0,b)*Hscale/L0,
-v <= S+max(0,a)*K/L0^2+max(0,-b)*Hscale/L0.
These conditions hold for every L>=L0 by monotonicity. Here Hscale is the inherited Stage46 error constant, distinct from raw quantization H above.

First, tightening only the two new coupled rows gives exact separation of two of eight (candidate 2 ratio 1.00539395, candidate 8 ratio 1.05968087); six still have exact affine witnesses. Tightening the three high radial rows as well gives one common integer normal excluding all eight, with ratios in increasing q order 251.17720324, 571.06104843, 968.05579380, 608.30399256, 94.46369577, 336.40600068, 624.91226211, 905.55874768. Floating LP was used only to propose normals; exact arithmetic decides the result.

The prior complete lattice enumeration plus these exclusions establishes q>10^70 and b-a>=q for all L>=10^114 under the inherited Stage46 and anchor assumptions. First unexcluded dyadic windows (base 10^8): triple 1.0830740992659433e135, close pair 1.4196068833898572e140, each 16 times the prior boundary. Continuous integer endpoint 4.72478e43 unchanged; unbounded strict separation and B_fix,odd(32) open. The inherited analytic anchor and Stage46 were not independently revalidated.

## Compact exact certificate and replay

The following code contains the exact new rows and one normal (sign may be reversed); use the PREFIX-1143 compact verifier extracted from its paper, together with the fixed predecessor fixtures and verifiers named there. The local execution verify1144.py used the same JSON row and normal inputs, reran the PREFIX-1143 verifier, and checked all eight strict rational inequalities >94. No floating LP is needed for replay.

```python
from fractions import Fraction as F
import runpy
D=runpy.run_path('verify1143_compact.py')
G,L,K,H,aj,am,dj,r,u=[D[k] for k in ('G','L','K','H','aj','am','dj','r','u')]
A=D['A']
# A is the PREFIX-1141 verifier dictionary (ten rows).
m0,e0,C0=A['m'],A['e'],A['cols']
rows=[
[-537378197081296272832,-989602582095486220662295,47458609622835095805,-757675616387427,17760413241,0,0,46,-8,-1,0,0,0],
[-837787403044792739637,-1542816606340676775418698,72876196576253439392,-1143655813704068,26286777131,0,0,41,-7,-1,0,0,0],
[-1550395940623921188059,-2855109202824325639444683,132263626931599235587,-2031957495680465,45626599285,0,0,33,-5,-1,0,0,0],
[363735132893106646,-500733329985880975000,23778323876840065,-379616673653,8897716,104168595143626652328856,0,-1,-1,-1,0,0,0],
[32342963584203631,-5873715889882419523,283505208906910,-4451040583,100668,0,243096217452445879567399,-1,0,0,-1,0,0]]
m=m0+[v[0] for v in rows];e=e0+[50014]*5
C=[v+[w[j+1] for w in rows] for j,v in enumerate(C0)]
n=[
52077316508130615150553571438066357907348438994919376633268500247708534881432544329231861793019124574319082070093509986908258651837412919623618,
2225227147629894679583613689262131503708090585589210564583073349662454678464334717203167381966123463511280414197318198393566581476128156939315,
543117845963749277162927477651194342660912653306636112047447485735116036363010447987441222665960318678483290344020704938285022761830015536820477074948,0,0,
1048845719700701998271880083621357703524632677628904684688253535282081722510752941860664385031922380419980858375268661133241420007672883403288351118169,
1116437196870532012804035237611691649883809017954966248334148396056097280855396396355308182985351597994262956855266514017419027458833510869849213395470,0,0,
-3207092162418406559735600686697020525668723900030631822688230010726262944238964051123216464083948299631759691621230167388635065700834331299119694219590,
2613823848655689823364676266136534942939808781641037214021718014177017824545922235072966702215660152149096835643711084585879521012756198037011344226327399745680300,
-4387561051029332704712249761504153447173883467281095694696457925963330074615924666355304394484411692122017504630116313724746274913544681513823241857949679799755250,
1854146487117352400194520911625594201834885831473554249267103958073329585694190662772089830577080945609109415791291168842305568975923403244937484323586940585084900,
1055558410891942323485501633913681837973726613473549522768669824767664379070890194220615387617997592011634869480657841740727278963135577342904033756595830928325,
-269379020942142522089758668374664787064690037764064417813739378882965112599259281694003954039257246627341039939808257177558228264035979717753804794973109317107425]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
assert len(m)==len(e)==len(n)==15 and len(C)==12
a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;z=dot(n,m)
S=sum(abs(dot(n,c)) for c in C)+sum(abs(v)*d for v,d in zip(n,e))
assert S>0 and len(D['lines'])==8
for q,p,h in D['lines']:
 v=a*(F(p,q)-r)+b*(F(h,q)-u)-z
 ratio=max(v/(S+max(0,-a)*K/L**2+max(0,b)*H/L),-v/(S+max(0,a)*K/L**2+max(0,-b)*H/L))
 assert ratio>94
 print(q,float(ratio))
Q=10**70;L3=L2=10**8
while L3<=A['d0']*Q*Q/(4*400000):L3*=2
while L2<=Q*Q:L2*=2
print('PASS',Q,float(L3),float(L2))
```

## Next
Build global section from the tightened fifteen-observer rows, not the old coarse ones. Extend q search beyond 10^70 with exact unimodular enumeration. Prioritize quantization/row arithmetic separation on earlier rows if needed, retaining all shared directions and the actual raw floor enclosures. New original moments are not needed merely to reproduce the present result. Independent review and inherited anchor exit confirmation remain pending.
