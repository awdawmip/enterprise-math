# R059D Stage AJ — proof of the C phase theorem and resolver-robust circle constant

Researcher-ID: `EM-R059D-AJ-6D4A19`

Task: `RS-R059D-STAGE-AJ-C-PHASE-DELAY-RESOLVER-ROBUST-ALGEBRAIC-CONSTANT`

## 1. Exact C_s semantics

Let

`Q(x,y)=x^2+xy+y^2`.

For an integer subdivision `s>=1`, put `D=3s`.  The exact AD microcentroid set is

- `A_s={(3i+1,3j+1): i,j>=0, i+j<=s-1}`;
- `B_s={(3i+2,3j+2): i,j>=0, i+j<=s-2}`.

Its cardinality is `s^2`.  If a macrotriangle has vertices `P0,P1,P2`, the point indexed by `(u,v)` is

`Z=D P0 + u(P1-P0)+v(P2-P0)`.

The triangle is C_s-occupied iff

`2*#{Z: Q(Z)<=(rD)^2} >= s^2`.

Equality is selected.  This is exactly the inherited AD rule; no continuum-area resolver is introduced.

## 2. Edge support and the balanced shell event

Work in the left half of the canonical first sextant: `a>=b>=0`.
For `p=(a,b)`, the inward shared edge from `(a,b)` to `(a-1,b)` has adjacent triangles

`U(a-1,b)` and `D(a-1,b-1)`.

Reflection in that lattice edge is an isometry of the triangular quadratic form on displacement vectors.  In the stated half-sector it sends the outward U triangle to the inward D triangle and weakly decreases `Q` pointwise.  Hence if `U(a-1,b)` passes the majority threshold, so does its D companion.  Every other shared-edge pair incident to `p` contains a triangle no farther inward than `U(a-1,b)`.  Thus the edge-supported vertex criterion reduces to the majority status of `U(a-1,b)`.

Fix a shell `m=a+b`.  Moving `(a,b)` toward balance by `(a,b)->(a-1,b+1)` preserves `x+y` and reduces the tangential absolute coordinate in

`Q(x,y)=3(x+y)^2/4+(x-y)^2/4`.

Using reflection of the microcentroid cloud gives a point pairing with nonincreasing Q, so coverage is maximal at

`a_m=ceil(m/2), b_m=floor(m/2)`.

Define `T_m=U(a_m-1,b_m)` and

`K_s(r,m)=#{(u,v) in A_s union B_s : Q(D(a_m-1)+u,Db_m+v)<=(Dr)^2}`.

Then

`E_C(r,m,s) <=> 2 K_s(r,m)>=s^2`.

This is the exact one-dimensional C event criterion.  It is evaluated directly from the finite microcentroid rule, not from a C ledger.

The same tangential monotonicity makes each supported shell section a reflection-symmetric interval around the balanced point.  Together with the fact that every vertex of the D6 hexball `H_r` is supported, the first-sector boundary is a nonnegative single-peak Motzkin path.  If `M_C_s(r)` is its maximal shell, then

`J_C_s(r)=M_C_s(r)-r=#1=#3`,

`#2=r-J_C_s(r)`,

`|W_C_s(r)|=M_C_s(r)`,

and therefore

`C_C_s(r)=6 M_C_s(r)=6(r+J_C_s(r))`.

## 3. The no-ahead lemma

Let `c_m` be the centroid of `T_m`.  Suppose `Q(c_m)>r^2`.
For a microcentroid `z=c_m+d`,

`Q(z)-Q(c_m)=grad(Q)(c_m).d + Q(d)`.

Since `Q(d)>=0`, any sample with `Q(z)<=r^2<Q(c_m)` must lie strictly in the inward tangent halfspace

`grad(Q)(c_m).d<0`.

It remains to prove that this tangent halfspace contains strictly fewer than half of the AD microcentroids.

### 3.1 Barycentric composition form

A-type microcentroids correspond to ordered nonnegative triples

`p0+p1+p2=s-1`

with barycentric numerators `(3p0+1,3p1+1,3p2+1)`.
B-type centroids correspond to

`p0+p1+p2=s-2`

with numerators `(3p0+2,3p1+2,3p2+2)`.

For an odd shell `m=2k+1`, the tangent vertex weights are proportional to

`(-2,1,1)`,

so the inward condition is

`-2p0+p1+p2<0`.

For an even shell `m=2k`, `k>=1`, the tangent weights are

`(-6k+1, 3k-2, 3k+1)`.

The additive `+1` or `+2` barycentric residues cancel because the three weights sum to zero.

For a composition layer `p0+p1+p2=S`, write

`A=9k-3`, `B=9k`, `C=6k-1`.

The exact number of even-shell inward compositions is

`N_k(S)=sum_{j=0}^{floor((CS-1)/B)} ( floor((CS-1-Bj)/A)+1 )`.

Relaxing the floors gives

`N_k(S) <= 25 S^2/108 + 13 S/12 + 1`,

because

`C^2/(2AB)<=25/108`, `C/B<=2/3`, `C/(2A)<=5/12`.

Summing the two AD composition layers `S=s-1,s-2`, the difference between `s^2/2` and that upper bound is

`s^2/27 - 7s/9 + 5/54`,

which is positive for every integer `s>=21`.

For `1<=s<=20`, only a finite exact check is needed.  Here `S<=19`.  For a fixed composition, the even tangent sign has the form

`3k(S-3p0)+(S-3p1)`.

If `S-3p0` is nonzero, a sign change can occur only at

`|k|<=2S/3<13`.

Thus exact enumeration of `k=1,...,13` plus the stabilized tail covers every even shell.  The deterministic checker performs that enumeration for both composition layers.  The worst counts are all strictly less than `s^2/2`.  Odd-shell counts are enumerated simultaneously and also satisfy the strict bound.

Consequently fewer than half of the C_s microcentroids can satisfy `Q(z)<Q(c_m)`.  Therefore, if N rejects shell `m`, C_s rejects shell `m` for every `s>=1`.

Hence

`M_C_s(r) <= M_N(r)`.

## 4. The at-most-one-delay lemma

Now suppose N accepts its maximal shell `m=M_N(r)`.
If `J_N(r)=0`, then `m=r`.  Every vertex of `T_r` has nonnegative coordinates and coordinate sum at most `r`, hence

`Q(x,y)<= (x+y)^2<=r^2`.

So C_s accepts shell `r` for every s and `M_C_s=M_N`.

Assume `J_N(r)>0`, so `m>=2`.  We show the complete preceding limiting triangle `T_{m-1}` lies inside the N limiting-centroid radius `Q(c_m)`.

If `m=2k`, the three vertex gaps are

`Q(c_m)-Q(v) = (15k-8)/3, 2(3k-1)/3, 2(3k-1)/3`,

all positive for `k>=1`.

If `m=2k+1`, `k>=1`, the gaps are

`(15k-2)/3, (6k+1)/3, 2(3k-1)/3`,

again all positive.

Since Q is convex, its maximum over a triangle occurs at a vertex.  Thus every point of `T_{m-1}`, in particular every one of its `s^2` microcentroids, satisfies

`Q(z)<=Q(c_m)<=r^2`.

So C_s accepts shell `m-1` for every s, and

`M_C_s(r)>=M_N(r)-1`.

Together with the no-ahead lemma,

`M_C_s(r) in {M_N(r),M_N(r)-1}`.

Define

`chi_s(r)=M_N(r)-M_C_s(r)`.

Then for every `s>=1,r>=0`,

`chi_s(r) in {0,1}`

and

`J_C_s(r)=J_N(r)-chi_s(r)`.

The exact delay-bit criterion is

`chi_s(r)=1 iff 2 K_s(r,M_N(r)) < s^2`.

Equality gives `chi=0` because AD selects exact half coverage.

## 5. Circumference and the resolver-robust constant

From the boundary-word theorem,

`C_C_s(r)=6(r+J_C_s(r))`.

Using the phase theorem,

`C_C_s(r)=C_N(r)-6 chi_s(r)`.

Hence the sharp all-radius difference bound is

`0 <= C_N(r)-C_C_s(r) <= 6`.

Stage AI proved

`-2/r < C_N(r)/(2r)-kappa_E < 1/r`

for `r>=1`, where `kappa_E^2=12` and `kappa_E>0`.
Subtracting `3 chi_s(r)/r` yields

`-5/r < C_C_s(r)/(2r)-kappa_E < 1/r`.

Therefore

`sup_{s>=1}|C_C_s(r)/(2r)-kappa_E| < 5/r -> 0`.

The convergence is uniform over the entire finite-sampling C family, and every C_s shares the same algebraic Enterprise circle constant.

For a fixed endpoint correction epsilon,

`C_C_s(r)-(2r+epsilon)kappa_E`

is bounded uniformly in s because AI gives the exact N floor-slack form and `chi_s` is binary.  Hence

`C_C_s(r)/(2r+epsilon) -> kappa_E`

whenever the denominator is eventually positive.  Replacing `r` by any fixed integer multiple `hr` proves refinement-subsequence invariance as well.

## 6. Precision and ties

No sampling threshold `s0` is needed for the theorem: the phase bound is already true for every `s>=1`.
Pointwise phase decisions may depend on s.  AJ does not claim that all sufficiently large s become identical at every radius.

Exact-half ties do occur.  Examples include

- `s=2,r=5,m=6`: 2 of 4 samples;
- `s=8,r=24,m=28`: 32 of 64;
- `s=12,r=11,m=13`: 72 of 144.

All are selected by the inherited AD `>=` rule.

The 19 AF `s=1024` one-radius delay pairs are independently reproduced by the exact event criterion after the theorem was frozen.

## 7. Semantic boundary

The result proves resolver robustness of the Enterprise-native count-geometry constant.  It does not identify `kappa_E` with the standard real number pi, does not prove a theorem about Euclidean pi, and does not select N or C as the unique canonical resolver.
