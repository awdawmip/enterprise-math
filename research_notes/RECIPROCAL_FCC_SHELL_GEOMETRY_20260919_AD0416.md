# Reciprocal-normalized FCC shells: exact divisor geometry

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `reciprocal-fcc-shells-20260919-AD0416`
Status: `RESEARCH_NOTE / PROVED_CARRIER_DERIVATIONS / EXACT_FINITE_CHECK`
Authority: no Task-ID, CLAIM, review, Working Truth or Foundation promotion.
Question: 如果研究数的倒数在立体进取几何里的排列，能有什么规律吗
Source snapshots: global a66a26f4d8f4b91b1e66dcb707db164fa557468e; EM 08199f00adff9e957dcecf3c4c8876a0290c86cd.

## Scope and proposed observation

Use the selected FCC coordinate carrier, not an identification of native P000 six-dimensional states with a Euclidean three-dimensional chart. This note proposes a placement; the user did not specify one. Integer n labels the nth nearest-neighbor graph shell; multiply every point in that shell by 1/n. These are rational readout coordinates, not physical subdivisions of native Cells, one point per integer, or crystallographic reciprocal-lattice vectors. Preserve all underlying native provenance.

## Carrier, shell, count

Lambda={(x,y,z) in Z^3:x+y+z even}, with twelve generators given by permutations of (+/-1,+/-1,0). A lattice basis is (1,1,0),(1,0,1),(0,1,1); basis coordinates are
q(v)=((x+y-z)/2,(x+z-y)/2,(y+z-x)/2).

Exact graph distance:
h(v)=max(|x|,|y|,|z|,(|x|+|y|+|z|)/2).
Proof: each step changes one coordinate by at most 1 and L1 by at most 2. By signed permutation assume a>=b>=c>=0. If a<=b+c, use (a+b-c)/2,(a+c-b)/2,(b+c-a)/2 steps in the three positive paired directions. If a>=b+c, pair b and c moves with the first coordinate and cancel the remaining even number a-b-c of subordinate moves in pairs. Both attain the lower bound.

Define S_n={v in Lambda:h(v)=n}, R_n={v/n:v in S_n}, n>=1. All R_n lie on the common cuboctahedral boundary h=1. Intrinsic FCC face counting gives
C_n=|R_n|=12+24(n-1)+8(n-1)(n-2)/2+6(n-1)^2=10n^2+2.
Terms respectively count vertices, edge interiors, triangular interiors, square interiors.

## Exact overlap and divisibility

In a fixed lattice frame,
(Lambda/m) intersect (Lambda/n)=Lambda/gcd(m,n),
(Lambda/m)+(Lambda/n)=Lambda/lcm(m,n).
The second operation is subgroup/Minkowski sum, not union. Both follow coordinatewise in the lattice basis from integer divisibility and Bezout.

Intersecting the first identity with h=1 proves
R_m intersect R_n=R_gcd(m,n).
Consequently m divides n iff R_m is contained in R_n; the reverse implication follows from strictly increasing C_n.
Examples: R_6 intersect R_9=R_3 (92 points); coprime shells intersect in R_1 (12 vertices).

The laws are unchanged by common carrier rotations, and FCC lattice symmetries preserve each shell. They do not establish the same law for independently, arbitrarily rotated non-symmetry lattices or a full native rotation lift.

## Primitive births and prime layers

Let B_n=R_n minus union_{k<n} R_k, P_n=|B_n|. The least lattice denominator of u=v/n is
d=n/gcd(q1(v),q2(v),q3(v),n).
A point born at d appears precisely in shells whose indices are multiples of d. Hence R_n is the disjoint union of B_d over d|n:
C_n=sum_{d|n} P_d.
Mobius inversion proves P_1=12 and, for n>1,
P_n=10 J_2(n)=10 n^2 product_{p|n}(1-1/p^2).

For n>1, n is prime iff R_n has exactly 12 inherited points. A prime has only proper divisor 1; a composite has a proper divisor d>=2 and therefore inherits the whole larger R_d. Composite layers still introduce many new points.

n,total,new,inherited:
2,42,30,12
3,92,80,12
4,162,120,42
5,252,240,12
6,362,240,122
7,492,480,12
12,1442,960,482

The exponent 2 comes from this carrier boundary count, not from a claim about native dimension. Ambient gcd(x,y,z) is not enough for FCC primitiveness: (2,0,0)/2 is not in Lambda.

## BRC reuse and reciprocal weights

REUSE_APPLIED: definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json at the EM source snapshot; explicit rational multiplicity/histogram and observer-preserving typing. No new BRC family, recurrent implementation, or signed-cancellation claim.

At finite cutoff N retain labeled occurrences (n,v), with observed position u=v/n. Assign each occurrence the declared positive weight 1/n. For a position first born at denominator d and N>=d:
count=floor(N/d),
exact histogram=sum_{k=1}^{floor(N/d)} [1/(kd)],
total W_N(u)=H_floor(N/d)/d,
dominant M_N(u)=1/d.
Support alone erases repeated visits. Count/total/dominant summarize only those declared observations, not arbitrary later moments or original provenance.

For d=2,N=30 the total is 1195757/720720. At each fixed born point the infinite cumulative weight diverges harmonically, despite individual weights tending to zero. Total shell mass is C_n/n=10n+2/n. These conclusions depend on weighting EVERY shell occurrence by 1/n; one point per integer or shell probability normalization defines another model.

## Arithmetic overlap kernel

K_mn=|R_m intersect R_n|=10 gcd(m,n)^2+2=sum_{d|m,d|n}P_d.
For A_nd=1[d|n], K=A diag(P_d) A^T. A is unit lower triangular, so K is positive definite and det(K)=product_d P_d.
With reciprocal layer weights the inner-product kernel is K_mn/(mn).
This is a derived gcd-kernel interpretation, not a novelty claim, RH proof, or efficient prime-generation result.

## Actual local validation

Standard-library integer BFS from the origin and exact fraction canonicalization independently checked:
- 30 shells; 94,611 vertices in the closed radius-30 graph ball;
- 77,762 distinct normalized positions through shell 30;
- all 465 unordered shell pairs including the diagonal obey gcd intersection;
- all 30 shell counts and birth counts match the formulas;
- all 900 ordered entries match the divisor-kernel factorization;
- one sample born in each d<=30 obeys the exact multiple-index and harmonic-weight rules.

A separate standalone checker was executed with --max-shell 30 and passed. No floating tolerance, hosted computation, Lean verification, independent mathematical review or novelty audit is claimed. Finite checks complement the proofs, not replace them.

## Next exact research unit

Specify a native provenance-preserving Cell/path lift of the chosen shell observation and test whether the desired observable factors through carrier coincidence. Retain hidden fibers when it does not. Do not equate identical displayed rational coordinates with native-state identity.

## Source authority

Global P000_REALITY_FOUNDATION.json and P000_FCC_PRIMARY_COORDINATE_CARRIER.json under projects/enterprise-math at global a66a26f4d8f4b91b1e66dcb707db164fa557468e govern scope. The BRC substrate above governs typing. Classical context only: Geoffrey B. Campbell, Ramanujan and Eckford Cohen totients from Visible Point Identities, arXiv:1212.2818. All specific shell/overlap identities above include their own derivations.
