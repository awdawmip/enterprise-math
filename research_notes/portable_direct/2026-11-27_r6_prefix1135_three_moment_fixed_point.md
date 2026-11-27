# PREFIX-1135 — Robust three-moment fiber and self-consistent inverse-scale fixed point

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / COMPACT_ANCHOR_THREE_MOMENT_RELAXATION / NOT_REVIEWED.

## Scope and immutable inputs
Continue PREFIX-1134 at 1be6afaab6e3bd6682feffc7ca067d96f32cf18c:research_notes/portable_direct/2026-11-27_r6_prefix1134_affine_section_transport.md, with its sole surviving line and the three nominal moment inequalities of PREFIX-1131 at a20dc66d0703778cc5825b015da539398a5ae4a2. Reuse the 9600 compact anchor and 301-term Frobenius basis, frozen P000 V5 and companions f42f2906d77f24085c123f3ccfe9667d41caa96d, signed reversal -5, 5q cover, O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. All coordinates here are auxiliary algebraic readouts of the existing signed X6 carrier. No new native CT, anchor inverse, raw moment computation or formal Task mutation. Inherited Stage46 correspondence, analytic boundary and historical 8400/8800 exit uncertainty remain conditions. The compact anchor and moment inequalities are relaxations, not the exact original carrier.

Global entries read at immutable 92a452f6ee60b4bc2e1be49df78271a3f79e9a1f. Current LEASED inventory r6-20261127-2153-leased-read SUCCEEDED/error=null; as_of 2026-11-27T13:54:02.540253Z, Source d44dbbe27b2f2e7f0b741259ac246c28fc8687af, tasks=[], next_cursor=null. Historical registration r6-20261123-2358-session-start-own-v1 SUCCEEDED (EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 / TASK_RESEARCH); current private session binding unconfirmed; independent continuation, no borrowed identity or new CLAIM.

## 1. Direct candidate test and positive robust inner certificate
Write the compact anchor as a(z)=a0+W z[0:6]+diag(dr) z[6:12], z in [-1,1]^12. For fixed rho,c with t=sqrt(36/(1+rho)), use the two real density observers F_a(t), G_c(a,t) from PREFIX-1134 and the three nominal moment residuals M_k a - yhat_k (k=10000,10400,10800). Here M_k and yhat_k are the rational row and floor-observation of PREFIX-1131, not the exact untruncated moments. These residuals being zero suffices for the three published inequalities |M_k a-yhat_k|<=eps_k.

Using the same full necessary candidate rectangle as PREFIX-1134, L0=10^100, K=d_u+2E/q0, H=2d_u+4E/q0, E=400000, q0=544447235321021556325566186117974922693:
rho in [p/q,p/q+K/L0^2], c in [h/q-H/L0,h/q].
Evaluate the two density rows with exact interval Horner, tail payments, and shared columns. Append the three moment rows. In integer units 10^-125, uniformly in rho,c,z, the actual continuous five-vector is m+Cz+e_actual, |e_actual_i|<=e_i. The published moment payment e_i is a conservative upper bound for the rounding error even if the nominal equations rather than true raw moments are used. The full 12 shared columns are retained.

For all nonzero primitive cofactor normals n of four independent columns of C, verify
S=sum_j |n dot C_j| > |n dot m|+sum_i |n_i|e_i.
This implies [-e,e] lies inside the nominal zonotope m+C[-1,1]^12 by the facet characterization of a full-rank zonotope. The actual exact test enumerated 495 four-column subsets, with 420 nonzero support normals, and the minimum (S-|n dot m|-sum |n_i|e_i)/S is 0.02630317215895356 > 0.0263. In particular all five equations can be imposed together for every parameter pair in the rectangle. This is a positive inner test, strictly stronger than failure to find an outer separator. The two-moment outer ratio is 0.973685251066349, three-moment ratio 0.9736943161685981. Adding the sixth (d) observer with d ranging over the old interval gives the same outer maximum ratio to displayed precision. Direct fixed-d six-row inner test at L0=10^114 gave margin -6.410070951375324, inconclusive. These negative attempts are retained.

## 2. Fixed-point lemma: avoid a fixed d six-row inner test
Let Z=[-1,1]^N, D=[dl,du], and h:Z x D -> R^m continuous with h(z,d)=m+Cz+u(z,d), |u_i|<=e_i. Suppose [-e,e] is contained in m+CZ. Let v:Z x D -> D be continuous. Then there exists (z*,d*) such that h(z*,d*)=0 and v(z*,d*)=d*.

Proof: at every vertex w of the box [-e,e] choose a preimage z_w in Z with m+C z_w=w. Multi-affine interpolation of the vertex preimages gives a continuous S(w) in Z and m+C S(w)=w throughout the box (zero-width coordinates may be omitted). The map (z,d) -> (S(-u(z,d)),v(z,d)) is a continuous self-map of the compact convex product Z x D. Brouwer yields a fixed point; substitution proves both identities. The lemma only needs uniform outer error for the actual continuous equations and a robust inner inclusion for the nominal system, not independence of errors or exact realizability of an enclosing error box. It preserves the same shared coefficient z in every equation.

Apply it with the inherited density derivative ratio for d from PREFIX-1130. Put b=t^2/36, v0=b(1-b), ell=1-2b, A=1-b(c+2), B=-(c+2)A-A/v0*(A ell-(c+3)v0+A^2), C3=v0(2ell+3A)/6, C4=v0^2/8. Define the continuous extension
d_actual=B+(C3 D3+C4 D4)/D1
on the entire compact anchor and parameter rectangle, using the density derivative rows with the F contribution dropped (the formula agrees with the intended density derivatives when F=0). D1 is nonzero on the entire declared domain. On F=G_c=0, the inherited constant relation r2=-2A/v0 holds, so d_actual is precisely the inherited inverse-scale coefficient. This extension does not impose a false relation off the root fiber.

For L>=10^114, uniform exact interval arithmetic in the narrower necessary rectangle with K,H unchanged gives D1 strictly negative (near -1.3687866813e7). With d0=(dl+du)/2, enclose H3=(B-d0)D1+C3D3+C4D4 using all shared columns, and divide by D1. The resulting d0+H3/D1 is strictly inside the old [dl,du] for ALL z and parameter pairs in that narrower rectangle; width about 9.95753446125e-88, old width 9.8998790324e-75. This is a candidate-fiber bound, not a new global true-spectrum d certificate. It supplies v(z,d) in the fixed-point lemma. No assumption of continuous choices of exact true coefficients as a function of scale is needed.

## 3. Sharpness of the PREFIX-1134 bounds in the strengthened relaxation
Use the sole surviving primitive q,p,h in the compact certificate below. For every integer L>=10^114 choose zpos the largest integer <2L satisfying p*zpos+h=0 mod q. Set a=zpos-q for a pair. For d in [dl,du], define rho(d)=p/q+d/(a*zpos), c(d)=h/q-d*(1/a+1/zpos). These satisfy the narrower necessary rectangle since a,zpos>=L. The five equations at these continuously varying parameters and the continuous extension d_actual meet the fixed-point lemma. Hence for each L there exists a common anchor coefficient vector with three nominal moment residuals zero, F=G=0 and d_actual=d, producing two exact integer values of rho*m+c+d/m at a and zpos.

For a triple take a=zpos-2q, bpos=a+q, lambda=d*q^2/(2*a*bpos*zpos), add lambda to c(d), and otherwise use the same rho(d). The residuals at a,bpos,zpos are +lambda,-lambda,+lambda by direct subtraction. The narrower rectangle still holds (lambda<d*(1/a+1/zpos)). At the first PREFIX-1134 not-excluded triple dyadic start, exact rational tests at du give lambda*zpos^2/E=0.6396694863804486<1, so all d in D satisfy the three budgets. At the first not-excluded close-pair start, q^2/L=0.8057554506923958<1, with both residuals zero. Affine dependence on d proves the parameter and budget tests throughout D. Thus both dyadic exclusion endpoints and q_min are attained in the compact anchor relaxation strengthened by all three published moment inequalities and self-consistent rho,c,d. The coefficients may vary with L. No claim of a fixed true BRC anomaly, exact raw-moment realization, or actual native carrier realization.

## 4. Compact exact input and verifier
Integer arrays m,C,e in 10^-125; H3,D1 are outward endpoints in 10^-110; d0,old are exact fractions. These data are generated by candidate_1135.py and d_bound_1135.py from the inherited verified bundle. All five-row normal checks and d interval arithmetic were independently rechecked in verify_1135.py using Fraction; cofactor integer determinant routine inherited from check_extra_core.py. The raw execution bundle additionally retains the failed fixed-d inner attempt, all source inputs and outputs. The compact arrays below support the strict claims without regenerating the Frobenius polynomials.

```json
{"line":["39842427926119417299262046818826239782916070158838139476777507","854223117766075752740545225414351655926157527291751525026511332","3950018562885944348193743729715096500004840471989124645725608269"],"m":["1578749725436294200191847058759791294255121","-8016680709457034915696742911950186983902114","-5125943210844204295","-17950719237217173155","-39478465139117230238"],"C":[["3744138645775498910841297928701976010966640315","-87125244309961656188605995439254644350120196792","-9439727292964913715644","-33057192159364659829729","-72701511035128092066755"],["-161039656349520894471888359937205864380223","3746573643488776666579887859681069553495355","563814399574156417","1850874067992514339","3907417520264524189"],["2298254077145580893797380295013148626","-53458267472769732129352373972486955517","-12547204637116","-36609963069810","-72451756015164"],["-47952155714854405058160188075338","1115182088175091721930947313324566","543387970","1189019200","2091474020"],["970258271083964521363312982548236062773","-72120495286988764488827521413216860724180","0","0","0"],["-466583415180187615239670236197498944780635","40347985749191228916185797857499750580988601","0","0","0"],["-4422552409729","-14544658619171738","66","64","61"],["-30551863247001164","2239318452415096038","-14","-13","-13"],["-36535640931316125","2363560184834305474","-1","-1","-1"],["814480300480595744","-19198820539636586492","0","0","0"],["5395617291183169","-401062895330366980","0","0","0"],["-1525853534519761","131948789140695908","0","0","0"]],"e":["778398383415451143","7186278565963893173986745928764695745","120600466","120600014","120600014"],"H3":["520495298938795335826695840081111188","520496661912850240935299344376396043"],"D1":["-1368786681290847096476201583917176569095811213042556424560414506091256342211917053398160696811322784263853785016118518","-1368786681290847096476201583917176569095811213042556424560414506091256342211917053398160689495212986718557760713408114"],"d0":"19381725319283097639925184961380720192130347541583695895653971125012291056998113394639/2000000000000000000000000000000000000000000000000000000000000000000000000000000000000","old":["96908626596415488199625924806903600960651737707918479478269855625061455284941067578033/10000000000000000000000000000000000000000000000000000000000000000000000000000000000000","96908626596415488199625924806903600960651737707918479478269855625061455285040066368357/10000000000000000000000000000000000000000000000000000000000000000000000000000000000000"]}
```

```python
# Python standard library; parse the JSON block as compact_1135.json.
import json,itertools,math
from fractions import Fraction as F
r=json.load(open("compact_1135.json"))
m=list(map(int,r["m"])); C=[list(map(int,z)) for z in r["C"]]; e=list(map(int,r["e"]))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def det(A):
    if len(A)==1: return A[0][0]
    return sum((-1)**i*v*det([row[:i]+row[i+1:] for row in A[1:]]) for i,v in enumerate(A[0]))
scores=[]
for rows in itertools.combinations(C,4):
    n=[(-1)**i*det([row[:i]+row[i+1:] for row in rows]) for i in range(5)]
    if not any(n): continue
    S=sum(abs(dot(n,z)) for z in C)
    if not S: continue
    scores.append(F(S-abs(dot(n,m))-dot(list(map(abs,n)),e),S))
assert len(scores)==420 and min(scores)>F(263,10000)
D=[F(int(x),10**110) for x in r["D1"]]; H=[F(int(x),10**110) for x in r["H3"]]
dl,du=map(F,r["old"]); d0=F(r["d0"])
assert D[1]<0 and dl<min(d0+x/y for x,y in itertools.product(H,D))<=max(d0+x/y for x,y in itertools.product(H,D))<du
q,p,h=map(int,r["line"]); assert math.gcd(p,q)==1
L3=15030672529752532658492675819451756975204368313013247172526662217806137760733494038167673589662519699404383846400000000
L2=1970100309819723960613952005007180690253986963523272333397414670212286088574860530570713312744245782040331399515340800000000
for L,triple in [(L3,True),(L2,False)]:
    z=2*L-1-((2*L-1+pow(p,-1,q)*h)%q); a=z-(2 if triple else 1)*q; b=a+q
    xs=[a,b,z] if triple else [a,z]
    assert L<=a<z<2*L and all((p*x+h)%q==0 for x in xs)
    if triple: assert du*q*q*z*z/(2*a*b*z)<=400000
    else: assert q*q<=L
    for d in (dl,du):
        lam=d*q*q/(2*a*b*z) if triple else F(0)
        rho=F(p,q)+d/(a*z); c=F(h,q)-d*(F(1,a)+F(1,z))+lam
        assert F(p,q)<=rho<=F(p,q)+du/F(10**228)
        assert F(h,q)-2*du/F(10**114)<=c<=F(h,q)
        assert [rho*x+c+d/x-F(p*x+h,q) for x in xs]==([lam,-lam,lam] if triple else [0,0])
print("exact checks passed",len(scores),float(min(scores)))
```

## Next
The old exclusion boundaries remain 1.50306725297525e118 (triple) and 1.97010030981972e123 (close pair). The strengthened relaxation is now provably attainable. Choose an extra genuinely discriminating BRC original moment, or reduce the existing nominal moment truncation errors; do not repeat the five-observer or same fixed-d inner search. The single integer endpoint m=47247757565973207955345875119021762026915609, fixed-spectrum unbounded separation, and B_fix,odd(32) remain open. Independent review pending. No new formal Task/Result or Activity association claimed.
