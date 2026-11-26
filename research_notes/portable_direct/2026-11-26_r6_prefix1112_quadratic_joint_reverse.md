# PREFIX-1112: three-point quadratic reverse observation and correlated coefficient strips

Date 2026-11-26. EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / NOT_REVIEWED.
Frozen model: same Stage46 X6 chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link{O,e1} blocked without renormalization, exactly two negatives. P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d, joint/time companions. Full Cell, port, signed phase, ordered branch multiplicity retained in parent BRC carrier; use only the paired auxiliary radial observer D_m(k)=L[x^m(1-x)^k]. No new native propagation, external comparison or residual attribution. Mother B_fix,odd(32) open.

## Sources
- PREFIX-1096 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md
- PREFIX-1105 04ca670bf23a2b37e9182921376cb28e87992658:research_notes/portable_direct/2026-11-26_r6_prefix1105_effective_integer_edge_band.md (explicit B2 polynomial)
- PREFIX-1107 7e95625df3a8c21b6d370246065d51469afa6345:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.md (620/m^3 remainder BEFORE absorbing B2 into 1000|e|/m^2; B2(0)=0 and |B2'|<1000)
- PREFIX-1107b bd6e81d3baba1aa8bcea7caec629814475fe5ab6:research_notes/portable_direct/2026-11-26_r6_prefix1107b_real_window_sieve.md (c,d boxes)
- PREFIX-1111 e4ebedecb64b01b33e832d4e7779b3b91fa26097:research_notes/portable_direct/2026-11-26_r6_prefix1111_exact_replay_quintillion_window.md
- 308fe4a28beb9dfadaccc1171514035cb95bc4d0:research_notes/portable_direct/2026-11-26_r6_prefix1111_replay_refine.py (parent reconstruction). Actual local parent replay.py SHA256 a905181441adf83cedf6f2bf296fd55b16691fe142168e20c9ce74140bd72f1f; sieve_result.json c83a6758977a94782dbffd94d28c99bffd521e67e4bc3e6164fdf2339cefdf46 both verified equal to 1111 evidence manifest from attached ZIP.

## 1. Quadratic reverse lemma

Write f(m)=rho*m+c+d/m, W(k)=D_m(k)/(K*Beta(m+1,k+1)), K>0 the fixed oracle normalization. alpha=-g'(b)/K>0. 1107's proof and 1105 section 4 give
 W(k)=alpha*(b^2*(k-f)/m - B2(k-f)/m^2)+r(k), |r(k)|<=620*alpha/m^3
for m>=10^8, integer k, |k-f|<=2, b>=0.044. B2 is a polynomial in e of degree at most 2, B2(0)=0, |B2'(e)|<1000 on [-2,2]. Explicitly B2(e)/b^2 =
 -[d+(c+e+2)A_e] + r2/2*[A_e L0-(c+e+3)v+A_e^2] +r3*v/6*(2L0+3A_e)+r4*v^2/8,
where A_e=1-b(c+e+2), v=b(1-b), L0=1-2b and rj=g^(j)(b)/g'(b). Each summand has degree <=2. This retains the signed second-order term that the earlier two-point inverse paid by a first-order error.

Choose integer k0 with certified |f-k0|<=1; write x*=f-k0. Obtain three certified W(k0+j) intervals for j=-1,0,1 with rational centers y_j and errors <=R. Let
 delta=(y_1-y_-1)/2, q=(y_1+y_-1-2y_0)/2,
 P(x)=y_0+delta*x+q*x^2.
The model quadratic Q(x)=alpha*[b^2*(x-x*)/m-B2(x-x*)/m^2] vanishes exactly at x*. Its derivative on [-1,1] is >=alpha*(b0^2-1000/m)/m, b0=.044. At the three nodes, |y_j-Q(j)|<=R+620*alpha/m^3. Therefore
 delta+R >= (alpha/m)*(b0^2-1000/m-620/m^2).
Use H=(delta+R)/(b0^2-1000/m-620/m^2) as an observable upper bound for alpha/m; denominator positive at m>=10^8. Lagrange interpolation is exact for Q. On [-1,1] the sum of absolute cardinal polynomials is 1+|x|-x^2<=5/4. Hence
 |P(x*)| <= E=(5/4)*(R+620*H/m^2).
If delta>2|q|, P is strictly increasing on [-1,1]. Exact bisection of levels -E,+E, clipped to the domain if necessary, yields an enclosure [x_l,x_u] of x*. If both levels occur inside, width <=2E/(delta-2|q|). These are purely auxiliary operations on the existing BRC observations, not a different physical computation. The unknown scale alpha cancels via its observable bound. With adequate oracle precision (R/delta=O(m^-2)), interpolation payment is O(m^-2), versus the inherited secant payment O(m^-1). No exact-zero test is needed to obtain the strip. The actual run verified |f-k0|<=1, delta>2|q| and both levels interior for all four scales.

## 2. Joint reverse polytope

Each strip k0+x_l <= m*rho+c+d/m <= k0+x_u is a pair of affine inequalities in the same unknown triple. Intersect all with prior certified coefficient boxes. This preserves cross-scale information, rather than replacing c,d by independent worst cases in each slope update. A nonempty bounded polytope has extrema of each linear coordinate at vertices. At a vertex the active normals span R^3 (otherwise a small nonzero perturbation in their common nullspace gives a segment through the point, contradicting extremality). Enumerate every triple of independent active boundary planes by exact Cramer determinants, retain only points satisfying all inequalities. This yields the exact extrema for the specified polytope; even a lower-dimensional bounded polytope has vertices of full active-normal rank in the ambient space. This does not establish that every feasible triple is a physically realizable observer.

For three distinct scales m1,m2,m3, multiply strip values by m to interpolate rho*m^2+c*m+d. With s_i=f(m_i) and |s_i-s_i_hat|<=epsilon_i, the Lagrange coefficient errors are bounded by
 |Delta rho|<=sum m_i*epsilon_i/|D_i|,
 |Delta c|<=sum m_i*(m_j+m_k)*epsilon_i/|D_i|,
 |Delta d|<=sum m_i*m_j*m_k*epsilon_i/|D_i|,
 D_i=(m_i-m_j)*(m_i-m_k), {i,j,k}={1,2,3}.
For scales comparable to M and pairwise separated by a fixed fraction of M, errors are O(epsilon/M), O(epsilon), O(M*epsilon). With epsilon=O(M^-2) these become O(M^-3), O(M^-2), O(M^-1). A fixed absolute oracle radius eta with slope of order 1/M instead contributes O(eta), O(M*eta), O(M^2*eta); for d this competes with O(1/M). Increasing scale alone cannot shrink all parameters with fixed precision. This explains the present unresolved d bottleneck. These are sufficient error bounds, not lower bounds for arbitrary correlated or stronger methods.

## 3. Actual new computation

Reused replay.py from 1111 evidence archive (hash verified above), and the exact floor-grid anchor recovery. Recomputed 66-term signed carrier, matrix hash 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312, four 201-term Frobenius bases and exact grouped occupation divisions through 6400. New anchor [5200,5600,6000,6400], cut=150, digits=90, J=7, R0=160427545/10^8, degree=358. All anchor floors recovered, all old box containment assertions passed. Local radius about 2.26000635e-45; total normalized radius <=1.329e-37 for each of 12 calls. No high-scale native CT. Initial streaming launch failed (StreamingExecNotEnabledContainerError); direct local execution succeeded. The raw 90-decimal outward rows were used in the actual joint.py computation. Compact 60-decimal outward rows below retain all observations at a negligible extra radius; the compact verifier is supplied for reconstruction, not represented as separately executed in this run.

For reproduction from the actual parent replay.py, invoke anchor_dual([5200,5600,6000,6400]); oracle,loc,degree=make_oracle(anchor,cut=150,digits=90). For each m below and given k0, query k0-1,k0,k0+1. For result tuple a, a[0] is center, a[1] total radius. Floor/ceil a[0]*10^90 and ceil a[1]*10^90, then run the joint strip calculation. The exact source of the preceding parent is 1111 execution archive replay.py; its hash verified, not a new external model.

Compact certificate: columns m,k,L,U,R, all center endpoints and radii divided by 10^60:
```csv
1000000000000000000,21440036720404644081,-10088596944488399403603548670038042885026413814921101,-10088596944488399403603548670038042885026413814921100,132895326144236277600031
1000000000000000000,21440036720404644082,-2962880010823022326079009069445337528141573096094148,-2962880010823022326079009069445337528141573096094147,132895326144236277574251
1000000000000000000,21440036720404644083,4162836922842354748479187014745797399220228362515214,4162836922842354748479187014745797399220228362515215,132895326144236277548471
100000000000000000000,2144003672040464398426,-44183979764809500371008994496493324079822811192298,-44183979764809500371008994496493324079822811192297,132895326144236278579973
100000000000000000000,2144003672040464398427,27073189571844271176370587911023247603438736817439,27073189571844271176370587911023247603438736817440,132895326144236278579715
100000000000000000000,2144003672040464398428,98330358908498042723453535966899662239244725002912,98330358908498042723453535966899662239244725002913,132895326144236278579458
1000000000000000000000,21440036720404643983373,-6637907857706528492588922956035833289155968811768,-6637907857706528492588922956035833289155968811767,132895326144236278589247
1000000000000000000000,21440036720404643983374,487809075958848662873357864341026206143434947421,487809075958848662873357864341026206143434947422,132895326144236278589221
1000000000000000000000,21440036720404643983375,7613526009624225818332672341201484130967864894912,7613526009624225818332672341201484130967864894913,132895326144236278589196
10000000000000000000000,214400367204046439832846,-745585586896618158285254728275898822459816655181,-745585586896618158285254728275898822459816655180,132895326144236278590167
10000000000000000000000,214400367204046439832847,-33013893530080442731872410747452896773764498927,-33013893530080442731872410747452896773764498926,132895326144236278590164
10000000000000000000000,214400367204046439832848,679557799836457272821480243345829013207537504506,679557799836457272821480243345829013207537504507,132895326144236278590162
```

Actual strip widths, display: 4.7425867294504876e-29, 4.662524826041355e-27, 4.6625247460594334e-26, 4.662524745979452e-25. Prior slope outward endpoints at 10^65: 2144003672040464398327479053201895915244457582534758801046616201823,2144003672040464398327479053201895915522250747157183873287998853857.
Prior c,d boxes at 10^30: [99141010437680654620437916203756,99141010437680654628564001195910],[9690862659641548432988461360525,9690862659641549206936415331527].
Actual exact joint polytope with original 90-decimal data and exact prior slope: 14 inequalities, 364 triples, 16 distinct feasible vertices. Outward endpoint integers divided by 10^65:
 rho [2144003672040464398327479053201895915383511059205534267009916916214,2144003672040464398327479053201895915383511059210197732368843911261]
 c [9914101043768065462450064423599002004708107128825705078213279851445,9914101043768065462450064423608408134191280008369071986034950481729]
 d [969086265964154843298846136052500000000000000000000000000000000000,969086265964154920693641533152700000000000000000000000000000000000]
Widths (display) rho=4.663465358926995e-47 (59567970005.53722-fold), c=9.40612948317288e-29 (86391379224.48529-fold), d=7.73947953971002e-16 (unchanged). For compact reproduction allow rho<4.664e-47, c<9.407e-29. This improves continuous coefficients without asserting new integer windows or independent review. The 1111 finite certificate remains intact.

## 4. Compact standalone checker

Extract the CSV block above into triplets60.csv and run the following Python code. The original local run used the same exact algorithm with 90-decimal rows and exact prior rho, outward root rounding at 10^60. No floats govern comparisons.

```python
from fractions import Fraction as F
from itertools import combinations
from math import floor,ceil
G=10**60
box=[(F(2144003672040464398327479053201895915244457582534758801046616201823,10**65),F(2144003672040464398327479053201895915522250747157183873287998853857,10**65)),(F(99141010437680654620437916203756,10**30),F(99141010437680654628564001195910,10**30)),(F(9690862659641548432988461360525,10**30),F(9690862659641549206936415331527,10**30))]
rows=[list(map(int,s.split(','))) for s in open('triplets60.csv') if s.strip()]
assert len(rows)==12
ineq=[]
for j,(l,u) in enumerate(box):
    a=[F(int(i==j)) for i in range(3)]
    ineq.extend([(a,u),([-v for v in a],-l)])
for a,b,c in zip(rows[::3],rows[1::3],rows[2::3]):
    m,k=b[:2]
    assert a[:2]==[m,k-1] and c[:2]==[m,k+1]
    z=[F(m),F(1),F(1,m)]
    assert k-1<=sum(v*l for v,(l,u) in zip(z,box))<=sum(v*u for v,(l,u) in zip(z,box))<=k+1
    y=[F(t[2]+t[3],2*G) for t in [a,b,c]]
    R=max(F(2*t[4]+t[3]-t[2],2*G) for t in [a,b,c])
    delta=(y[2]-y[0])/2;q=(y[2]+y[0]-2*y[1])/2
    lower=F(44,1000)**2-F(1000,m)-F(620,m*m)
    assert lower>0 and delta>2*abs(q)
    E=F(5,4)*(R+F(620,m*m)*(delta+R)/lower)
    P=lambda x:y[1]+delta*x+q*x*x
    def bracket(target):
        lo,hi=F(-1),F(1)
        assert P(lo)<target<P(hi)
        for _ in range(220):
            v=(lo+hi)/2
            if P(v)<target:lo=v
            else:hi=v
        return lo,hi
    l=k+F(floor(bracket(-E)[0]*G),G)
    u=k+F(ceil(bracket(E)[1]*G),G)
    ineq.extend([(z,u),([-v for v in z],-l)])
def det(M):
    a,b,c=M
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
verts=set()
for tri in combinations(ineq,3):
    A=[v[0] for v in tri]; b=[v[1] for v in tri]; d=det(A)
    if not d:continue
    x=tuple(det([[b[i] if j==k else A[i][j] for j in range(3)] for i in range(3)])/d for k in range(3))
    if all(sum(a*v for a,v in zip(row,x))<=rhs for row,rhs in ineq):verts.add(x)
assert verts
w=[max(v[j] for v in verts)-min(v[j] for v in verts) for j in range(3)]
assert w[0]<F(4664,10**50) and w[1]<F(9407,10**32)
print(len(verts),[float(v) for v in w])
```

Raw local evidence SHA256:
triplets.py 1d17bfba30f983f9edbb628139f1e028efceb3575bf30dff6a8003afa07df999
triplets.json 760e6c0c65cceda1134de82eb652eae0e7b97f9823337197e8ee97adfad94213
joint.py 2ef6227e90b15a89f35249c1a8811f89afb743245eef769f391391eb5f1d5575
joint_result.json dd10d2ea74bbddb23f8ecccd41e1278619a66ec70480ec7517b0ee20d0153a3e
triplets.log cc748da8823ad994c92c4d6de39c063c0cdbb907ddf9ac88eae430731acb3d81

## 5. Next
Keep joint strips as well as projected boxes; investigate direct high-order signed density jet with 6400 anchor and correlated anchor duals, or extend interpolation to cubic order after proving explicit third-order moment expansion. Seek meaningful d tightening and more efficient precision supply; uniform arithmetic separation, exact zero and other spectrum classification remain open. No new claim, Result, review or shared task mutation. Owner request r6-20261126-2245-owner-read-v1 SUCCEEDED/error=null, source f2b13fd86435e3ae495ac777ddcc25130a233f6c, as-of 2026-11-26T14:46:37.980310Z, LEASED filter empty, next_cursor null. Own registration original r6-20261123-2358-session-start-own-v1 SUCCEEDED.
