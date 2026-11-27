# T6 q0 signed-budget decoding: integer hot path and transfer to p11, p7, p5, p3, p2

2026-11-27. EM-DVR-DEBB5E, same Driver lane, author-side continuation of the p13 interval lemma at 84d61ba87b88d21ca6df1fda37a25975b4b7ad0e and its original basis/checker at 8aca2ae3c9dc43f9e1a0daea199c45e5478fd17b. No new independent reviewer identity. Existing T6 authors and nonterminal RR-C428294CF760BD8D99AA retain their exact scopes. No live researcher's frozen campaign was changed or rerun.

## Proposition

For p in {13,11,7,5,3,2}, consider integer u in Z^(p-1), the six q0 congruences sum_{j=1}^{p-1} u_j j^(-k) = y_k mod p^k for k=1,...,6, and separate signed masses sum (pj-1)max(u_j,0)<=A, sum (pj-1)max(-u_j,0)<=B, with A,B nonnegative integers <=2331. The following exact bounds hold for each arbitrary target (including inconsistent targets):
- p=13,11,7,5: at most one feasible integer vector, determined by at most p-1 forced integer choices and a final signed budget test.
- p=3: at most 16 complete candidate paths using the explicit basis below; p=2: at most 73. All feasible points can be recovered by bounded integer interval enumeration. These are upper bounds, not assertions of attained multiplicities.

This only solves the stated affine congruence subproblem; higher valuations, the vertical roster, smoothness, remaining rational observers and H0/lower-prime completion retain their own obligations.

## Kernel, saturation, consistency of targets

Put n=p-1 and r=min(n,6). For n>=6, the six rows on the first six columns over Z/p^6 form a Vandermonde matrix on distinct inverses, after factoring a nonzero inverse from each column. They are invertible modulo p^6. Hence the congruence homomorphism onto the six cyclic groups is surjective, kernel index p^21.

For n<6, use the last n rows, k=7-n,...,6, on all n columns. Factoring j^{-(7-n)} leaves the Vandermonde matrix on distinct nonzero inverses; thus it too is invertible modulo p^6. The high-row homomorphism is surjective and its kernel is contained in p^(7-n) Z^n (reduce the invertible matrix modulo p^(7-n)). Every lower-row congruence is therefore automatically zero on that kernel. For a general target, solve the high rows modulo the common p^6 using arbitrary lifts of their specified residues. Check the remaining lower rows once; if one fails, the target is inconsistent, since all solutions to the high rows differ by their kernel. This gives both exact initializer and exact kernel index p^E, E=sum_{k=7-r}^6 k = r(13-r)/2. The integer basis below may be obtained by successively restricting a row basis to each congruence (one p-digit at a time), HNF, and weighted LLL; saturation is independently certified by the row congruences and the determinant equal to p^E. No reliance on floating LLL or a short-vector heuristic is needed in the proof.

## Integer-only online solver

Let W=diag(pj-1), b_i be the rows of U W where U is the saturated kernel basis. Take a primitive integer normal g_i in the direction of the exact Gram-Schmidt vector of b_i relative to preceding rows, sign chosen so d_i=<g_i,b_i>>0. This is precomputation over exact rationals, clearing denominators and gcd. For all j<i, <g_i,b_j>=0. Define l_i=min(0,min_j g_i[j]), h_i=max(0,max_j g_i[j]). Any weighted feasible vector v satisfies
  A l_i - B h_i <= <g_i,v> <= A h_i - B l_i.
Start from weighted particular v_0 and descend i=n-1,...,0. At a given step v is v_0 plus the contributions of the already chosen higher rows. The unknown integer z_i must satisfy
  ceil((A l_i-B h_i-<g_i,v>)/d_i) <= z_i <= floor((A h_i-B l_i-<g_i,v>)/d_i).
Earlier rows vanish against g_i. Enumerate these integer choices and update v <- v+z_i b_i. At the last step test the original two signed masses, returning all survivors, dividing v by weights componentwise. This is exact: every feasible point is visited by induction, and every accepted point has the correct congruences and original budgets. The interval length is (A+B)(h_i-l_i)/d_i, so the product of floor(length)+1 bounds all complete candidate paths. In particular if (A+B)*max_i((h_i-l_i)/d_i)<1, each step is forced or infeasible. Online operations are integers only; no affine-coordinate inverse or Fraction arithmetic is required. This implements the earlier p13 theorem directly, not a heuristic nearest-point routine.

## Explicit exact certificate

The basis U13 is the previous source's U, reordered by (9,4,1,11,0,6,8,2,3,7,10,5). New U matrices (unweighted, rows):
p11:
[[528,-53,12,8,-2,38,-1,49,20,5],
[58,-2,-112,-9,-3,-87,3,-3,-8,-18],
[236,-140,-78,-30,5,48,-19,-28,-55,-3],
[-228,-245,44,-40,-74,47,34,19,-37,8],
[121,-56,-51,-37,124,-11,3,-37,-15,-32],
[-27,-129,114,-104,-25,-53,19,9,37,28],
[510,216,150,-10,-71,-4,32,-23,24,8],
[11,2,218,-51,-21,-57,-7,16,-51,-24],
[284,-6,-42,78,73,-42,34,10,23,46],
[-72,-274,-129,63,37,-20,-21,-58,33,-36]]
p7:
[[1022,378,-364,-224,112,-91],[-161,560,154,-448,-217,63],
[-1477,-112,175,-322,112,-287],[896,126,728,56,-175,-210],
[-1666,931,-441,392,-343,98],[959,-875,-455,-329,-497,-77]]
p5:
[[1000,-125,125,-375],[-625,-1250,625,0],[875,750,1125,375],[2000,-1500,-375,500]]
p3: [[729,0],[-243,243]]
p2: [[64]]

Exact maximal dual spread s and strict real threshold 1/s (integer total budgets must be strictly below the threshold):
|p|index|s|1/s approximate|max complete paths at total cap4662|
|---|---:|---|---:|---:|
|13|247064529073450392704413|100391772970311605414307379645/471503599360518379739494386363648|4696.63584385|1|
|11|7400249944258160101211|3453006707928413786165410660409/20188932200441531871245180657243558|5846.76889103|1|
|7|558545864083284007|1916/25678107|13401.93475992|1|
|5|3814697265625|89/568750|6390.44943820|1|
|3|177147|1/1215|1215|16|
|2|64|1/64|64|73|

The exact spread and row congruences/determinants were computed locally. For p3 the two ratios are 1/1458 and 1/1215, giving at most 4 choices each. For p2 the ratio is 1/64, giving floor(4662/64)+1=73. This extends the integer interval algorithm to all smaller prime layers under the stated carrier, with no branching for 11,7,5 at full cap. These basis data and formulas are a complete independently reproducible static certificate.

## Executed tests, scope and performance

Local Python with exact Fraction/SymPy setup and integer hot path. First 500 known-feasible shifted representatives per p11,p7,p5 (1500 checks) recovered their exact original u. Second deterministic test: each prime 500 generated feasible targets and 500 mixed targets (half arbitrary residue tuples, half derived from larger signed integer vectors); full or varying budgets. Results:
|p|consistent targets checked|with at least one feasible vector|inconsistent targets|
|---|---:|---:|---:|
|13|1000|500|0|
|11|1000|500|0|
|7|1000|500|0|
|5|752|501|248|
|3|750|717|250|
|2|750|749|250|
Total 5252 consistent target checks plus 748 inconsistent targets. Every returned vector checked for exact residues and masses. p2,p3 returned lists additionally compared with direct bounded coordinate enumeration for the 500 mixed tests, restricting p3 coordinates by the proved mod 3^5 invariance. p13 integer output compared on all 1000 cases with separately implemented exact rational coordinate decoder using the same basis: all equal. Single local timing, excluding setup and target initialization: exact Fraction decoder 0.502342 s, integer path 0.022365 s (22.46x speed ratio). Sample-dependent microbenchmark, not a measured acceleration of the active whole T6 campaign.

## Reproduction recipe (exact Python)

For a matrix U from above (p13 from its cited prior checker), the following is the actual certificate arithmetic in compact form. The recurrence used in the online test is the same as the proof, with no numeric tolerance:
```python
from fractions import Fraction as F
from math import gcd,lcm,prod
from sympy import Matrix
def setup(p,U):
    w=[p*j-1 for j in range(1,p)]
    r=min(p-1,6)
    assert abs(Matrix(U).det())==p**(r*(13-r)//2)
    assert all(sum(v*pow(j,-k,p**k) for j,v in enumerate(row,1))%p**k==0
               for row in U for k in range(1,7))
    rows=[[a*b for a,b in zip(row,w)] for row in U]
    g=[]; ds=[]; bounds=[]
    for row in rows:
        v=list(map(F,row))
        for b in g:
            c=sum(x*y for x,y in zip(v,b))/sum(y*y for y in b)
            v=[x-c*y for x,y in zip(v,b)]
        den=lcm(*(a.denominator for a in v))
        z=[int(a*den) for a in v]; d=gcd(*z)
        z=[a//d for a in z]
        step=sum(a*b for a,b in zip(z,row))
        assert step>0
        assert all(sum(a*b for a,b in zip(z,b))==0 for b in rows[:len(g)])
        g.append(z); ds.append(step); bounds.append((min(0,*z),max(0,*z)))
    s=max(F(h-l,d) for (l,h),d in zip(bounds,ds))
    paths=prod(int(F(4662*(h-l),d))+1 for (l,h),d in zip(bounds,ds))
    return w,rows,g,ds,bounds,s,paths
def enumerate_budget(x,A,B,setup_data):
    w,rows,g,ds,bounds,_,_=setup_data
    def visit(i,v):
        if i<0:
            if sum(max(0,a) for a in v)<=A and sum(max(0,-a) for a in v)<=B:
                yield tuple(a//b for a,b in zip(v,w))
            return
        l,h=bounds[i]; d=ds[i]; t=sum(a*b for a,b in zip(g[i],v))
        lo=A*l-B*h; hi=A*h-B*l
        for z in range(-((t-lo)//d),(hi-t)//d+1):
            yield from visit(i-1,[a+z*b for a,b in zip(v,rows[i])])
    return sorted(visit(len(w)-1,[a*b for a,b in zip(x,w)]))
```
Initializer: invert the stated r by r matrix modulo p^6 by Gaussian elimination with unit pivots, choose canonical lifts of the last r residues, multiply by inverse, extend with zeros to n coordinates, then check all six residues. This is precisely the construction proved above. The separate small-p direct comparator uses bounds -floor(B/w_j)<=u_j<=floor(A/w_j), and for p3 u_j==x_j mod 3^5.

## Scientific disposition

No new global T6 closure. Original p13 q13 author campaign remains its own work, with no change of frozen code; this is a reusable exact solver for future authorized research and audit. Nonauthor review of the earlier p13 theorem and the present transfer remains pending. No author identity/CLAIM/Result fabricated. Previous T6 exact nonterminal RR and its existing review/followup retain their original scope; no new task derived solely from a performance observation.
