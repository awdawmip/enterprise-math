# PREFIX-1136 — Coupled BRC moment separates the last primitive relation

Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.
Date: 2026-11-27. Source read and computation in the continuing R6 conversation. Current owner inventory request r6-20261127-2246-leased-read SUCCEEDED, error=null, as_of 2026-11-27T14:49:03.573820Z, Source c14aa20b88301b25f372d955b9db7414640e3a2d, LEASED tasks=[], next_cursor=null. Prior own registration r6-20261123-2358-session-start-own-v1 SUCCEEDED and custody metadata read; no claim or protected Activity mutation. Global entry blobs verified at 379f693786b90f8f5d00b822d1da7140e9d0a0f7.

## Scope

Continue PREFIX-1135 at 3b05acc11534008c25b08b7ab228902a89ac22e2:research_notes/portable_direct/2026-11-27_r6_prefix1135_three_moment_fixed_point.md, and PREFIX-1134 at 1be6afaab6e3bd6682feffc7ca067d96f32cf18c:research_notes/portable_direct/2026-11-27_r6_prefix1134_affine_section_transport.md. Preserve frozen P000 V5 and companions f42f2906d77f24085c123f3ccfe9667d41caa96d, signed reversal -5, 5q cover, O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. These are auxiliary algebraic observers of the inherited signed X6 BRC carrier; inherited Stage46 native correspondence and analytic boundary conditions and historical 8400/8800 exit uncertainty remain. No new native CT or physical attribution. Reuse 9600 shared anchor, 301-term Frobenius basis and old full parameter rectangle L0=10^100, not just candidate center. Prior complete PREFIX-1134 enumeration re-executed locally: 2 integer coordinates, unique primitive line as below, q<=10^62. The prior five-observer relaxed feasibility is preserved at its stated scope; this work adds new information.

## 1. Select a different moment channel, not only a larger order

Write the shared six-coefficient enclosure as a=a0+Wz[0:6]+diag(dr)z[6:12], |z_i|<=1. Ordinary radial moment rows have form (M0,M1,M2,M3,0,0). This is an exact structural absence of the two integration-constant coordinates in this observer family; it is not a claim of redundancy of the whole BRC carrier or of all radial moments. More radial rows may refine the first four coordinates. The coupled channel j=1 instead has fifth coordinate nonzero and sixth zero; j=2 has sixth coordinate nonzero and fifth zero. The already validated anchor_dual implementation uses both coupled channels at the original first anchor order. Raising their order rather than merely repeating the first channel can shrink a different shared uncertainty direction.

Use frozen recurrence from PREFIX-1126, 80430d242c6809ed9c61ee137c7913bdea9daaef:research_notes/portable_direct/2026-11-27_r6_prefix1126_anchor_moments.cpp. Its exact GMP moment recurrence gives v_l for each of the typed shift multisets (0,0,0,0,0,0), (0,0,0,0,1,1), (0,0,0,0,1,2). For channel j=1,2 the observer is
y_(k,j)=36^(-k) sum_{l=0}^k (-1)^l binom(k,l)36^(k-l) v_l/(l+j+1).
The original code first multiplies by j, makes the exact integer division, and divides the entire result by j. For channel zero use v_l without the extra denominator. Horner recurrence is the existing BRC-derived exact observer recurrence, not a new classical reference or native physical simulation. Run the inherited C++ program with 11200 11600 12000; the last two output lines are the coupled observers at 11200. All assertions passed.

In the Frobenius basis tuple (a,z,h,err,T), define the j-th coupled row for the first four coefficients as
M_(k,j,i)=sum_{n=0}^{300} floor_H(h_i[j-1][n] I_(k,half_i,off_i+n+1)),
and M_(k,j,3+j)=floor_H(I_(k,0,j)), other constant coordinate zero. Here off_i=int(a_i), half_i=int(2(a_i-off_i)); I is the inherited outward integer integral recurrence integ; floor_H=floor(H*x)/H, H=10^120. Every interval floor was checked equal at both endpoints. This is exactly the coupled-row construction in the inherited anchor_dual, applied without recomputing its inverse. Inherit the original tail and basis enclosure: eps_(k,j)=6^(j+1)/(j+1)*(35/36)^k+1/H+eb, eb=sum_i basis[i].err+(4*(N+1)+1)/H. With G=10^125, round center and twelve shared column contributions down at G, and set error=ceil(G*eps)+13 to pay all 13 rounding errors. Thus the true coupled residual lies in the shared rounded affine row plus this independent error interval. All statements are conditional on the inherited integral/analytic error bounds; no new native correspondence asserted.

Three extra ordinary radial rows at 11200, 11600, 12000 separately appended to the five-observer system produced maximum abs(center)/support ratios 0.9736943189623221, 0.9736943197708059, 0.9736943200763494, respectively (6237 nonzero cofactor directions each); inconclusive as exclusion tests, not positive inner feasibility proofs. Channel 1 at order 11200 instead separates the entire parameter rectangle by factor 181.20789547661693. Channel 2 also computed and retained locally for next use, not needed for current exclusion.

## 2. Exact common-coefficient separator

Append the channel-1 row to the 5-dimensional outer enclosure from PREFIX-1135, retaining all 12 shared directions and all independent payments. With integer unit 10^-125 and m,C,e defined in the certificate, the six-vector belongs to m+sum_i[-1,1]C_i+[-e,e]. A true candidate requires zero in this set. For every normal n this implies |n dot m|<=sum_i|n dot C_i|+sum_j |n_j|e_j. One exact integer normal with strict reverse inequality excludes every coefficient and every parameter in the whole candidate rectangle. Cofactor search examined 6912 nonzero directions for the channel-1 extension. The stored normal directly verifies |n dot m|>181*support>0. The local independent verifier checked the new row against exact nominal observations and all compact anchor columns; a separate BigInt check read the previous paper's immutable certificate and independently recomputed the same support. No assumption of independent shared column errors.

## 3. Consequences

Under inherited Stage46 conditions and PREFIX-1134 complete lattice enumeration, no primitive relation with q<=10^62 survives for any L>=10^100, hence b-a>=q>10^62 for all such dyadic windows. The finite smaller windows retain earlier evidence. Combining q^2<4EL/d (E=400000, d>0 from frozen certificate) and q<=sqrt(L) for the close-pair case gives first not-excluded starts on 10^8*2^j:
L3=120245380238020261267941406555614055801634946504105977380213297742449102085867952305341388717300157595235070771200000000 (~1.20245380238e119);
L2=15760802478557791684911616040057445522031895708186178667179317361698288708598884244565706501953966256322651196122726400000000 (~1.57608024786e124).
Each is eight times the PREFIX-1134/1135 start. No claim these new endpoints are sharp or that the fixed true BRC parameters ever produce an anomaly. Continuous endpoint certification unchanged; fixed-spectrum unbounded strict separation and B_fix,odd(32) remain open.

## 4. Compact exact verification

The following certificate is sufficient for exact support and dyadic arithmetic verification. The parent five rows are copied directly from the immutable PREFIX-1135 paper. The new compact row is from the actual local execution; unrounded row, coupled channel 2, source inputs and original output remain in the execution archive.

```json
{"line":["39842427926119417299262046818826239782916070158838139476777507","854223117766075752740545225414351655926157527291751525026511332","3950018562885944348193743729715096500004840471989124645725608269"],"m":["1578749725436294200191847058759791294255121","-8016680709457034915696742911950186983902114","-5125943210844204295","-17950719237217173155","-39478465139117230238","1001163861891333451"],"C":[["3744138645775498910841297928701976010966640315","-87125244309961656188605995439254644350120196792","-9439727292964913715644","-33057192159364659829729","-72701511035128092066755","-91220000364952284887"],["-161039656349520894471888359937205864380223","3746573643488776666579887859681069553495355","563814399574156417","1850874067992514339","3907417520264524189","4344473217818122"],["2298254077145580893797380295013148626","-53458267472769732129352373972486955517","-12547204637116","-36609963069810","-72451756015164","-77348963365"],["-47952155714854405058160188075338","1115182088175091721930947313324566","543387970","1189019200","2091474020","2091906"],["970258271083964521363312982548236062773","-72120495286988764488827521413216860724180","0","0","0","172186817276751308897194"],["-466583415180187615239670236197498944780635","40347985749191228916185797857499750580988601","0","0","0","0"],["-4422552409729","-14544658619171738","66","64","61","-1"],["-30551863247001164","2239318452415096038","-14","-13","-13","-1"],["-36535640931316125","2363560184834305474","-1","-1","-1","-1"],["814480300480595744","-19198820539636586492","0","0","0","0"],["5395617291183169","-401062895330366980","0","0","0","0"],["-1525853534519761","131948789140695908","0","0","0","0"]],"e":["778398383415451143","7186278565963893173986745928764695745","120600466","120600014","120600014","120600014"],"normal":["-13080203160992911088329295334758188735877473315329159902961449684069601241446922502419816500372952339274064982850089228","-151259245010244209386279251388273530096304258830003232825978912617163961903162467498052891451885490206564754282791780","-15149794751240068993211826331977397196625533413814857399776976763088027530477147265497524081246488770667150912642804915131414613963743950614198","16710421614617855830236655250213739062726915355980433739946510629583989420811048700273599245743036474966492005974094267579211630758468001955885","-6123466713672218932803955940673651265970619640785789446081834397682359374440390214158736673843712619806112168035072050904704437663816885578185","10350871604023994439141032481296877146400610656621516895770865310014952020965063228890792927564039339648624284673685377657930919049726"],"center_abs":"197930420310487770120261912238255481633525361973957456759182131092163434974585714633725637280612326123279659528580095022344471235217653902674852234952542023","support":"1092283643545922258469063818973987074859457201440173567594945370685112024168735739560161810984952013921368838709575503675139689937574273463751956903874645","gap":"196838136666941847861792848419281494558665904772517283191587185721478322950416978894165475469627374109358290689870519518669331545280079629211100278048667378","new_row":{"k":11200,"channel":1,"m":"1001163861891333451","cols":["-91220000364952284887","4344473217818122","-77348963365","2091906","172186817276751308897194","0","-1","-1","-1","0","0","0"],"error":"120600014","observation_floor":"343563320336064353108621240784591080944946563130887918835918143494619283778718876276074080441585261786849611797009"},"old_d_lower":"96908626596415488199625924806903600960651737707918479478269855625061455284941067578033/10000000000000000000000000000000000000000000000000000000000000000000000000000000000000"}
```

```python
# Save the JSON block as cert1136.json; Python standard library.
import json
from fractions import Fraction as F
r=json.load(open("cert1136.json"))
n=list(map(int,r["normal"])); m=list(map(int,r["m"]))
C=[list(map(int,c)) for c in r["C"]]; e=list(map(int,r["e"]))
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
v=abs(dot(n,m)); s=sum(abs(dot(n,c)) for c in C)+dot(list(map(abs,n)),e)
assert v==int(r["center_abs"]) and s==int(r["support"]) and v-s==int(r["gap"])
assert v>181*s>0
Q=10**62; d=F(r["old_d_lower"]); E=400000
L3=L2=10**8
while L3<=d*Q*Q/(4*E): L3*=2
while L2<=Q*Q: L2*=2
assert F(L3,2)<=d*Q*Q/(4*E)<L3 and L2//2<=Q*Q<L2
print(float(F(v,s)),L3,L2)
```

New coupled row generator (reuse archived replay_9600_n300_gmp.py, anchor_compact.json, original exact moment C++ and output new_moments_1136.txt; no new anchor inverse):

```python
from replay_9600_n300_gmp import *
from math import floor,ceil
H=10**120; G=10**125
pkt=json.load(open('anchor_compact.json'))
cc=[F(int(x),H) for x in pkt['center']]
W=[[F(int(x),10**140) for x in row] for row in pkt['weighted_columns_rows']]
dr=[F(int(x),10**140) for x in pkt['rounding_radii']]
vals=list(map(int,open('new_moments_1136.txt').read().split())); k=11200
assert len(vals)==5
eb=sum(b[3] for b in basis)+F(4*(N+1)+1,H)
def down(x):
    if isinstance(x,IV): x=x*1
    a,b=x; v=floor(a*H); assert v==floor(b*H); return F(v,H)
ints={i:integ(k,i,N+5) for i in (0,1)}
rows=[]
for j in (1,2):
    rr=[]
    for a,z,h,err,T in basis:
        off=int(a); half=int(2*(a-off))
        rr.append(sum(down(c*ints[half][off+n+1]) for n,c in enumerate(h[j-1])))
    row=rr+[F(0)]*2; row[3+j]=down(ints[0][j]); val=vals[2+j]
    center=sum(a*b for a,b in zip(row,cc))-F(val,H)
    cols=[sum(row[i]*W[i][l] for i in range(6)) for l in range(6)]+[row[i]*dr[i] for i in range(6)]
    err=F(6**(j+1),j+1)*F(35,36)**k+F(1,H)+eb
    rows.append(dict(k=k,channel=j,row=list(map(str,row)),observation=str(F(val,H)),m=floor(center*G),cols=[floor(x*G) for x in cols],error=ceil(err*G)+13))
json.dump(rows,open('extra_coupled_1136.json','w'))
```

Actual five GMP floor values (H=10^120):
```text
534811686137250751111727753892950408019877855360782158915649213931199627484026046644290286289016750041150241125753835
516479514746103467645875125997812025475364723406858452744093125919873483440528640340123093028847852850213654058626464
499364140598644459369808083671986036570599068725805952349451508659668944079684359354444062319312552484633307815223654
343563320336064353108621240784591080944946563130887918835918143494619283778718876276074080441585261786849611797009
189048166976163685859175999109378674750763053669692844297727135888057394751533498506042089131985362482891635964
```

## Next

Use the channel-1 separating normal as a sixth affine observer in PREFIX-1134's global section transfer. Channel 2 may provide a transverse direction; both have actually been computed at order 11200. Extend lattice search beyond 10^62 without recomputing 9600 anchor. Keep all retained observer directions and separate finite search limits from the unresolved mother objective. Activity association and independent review pending; no formal Task completion.
