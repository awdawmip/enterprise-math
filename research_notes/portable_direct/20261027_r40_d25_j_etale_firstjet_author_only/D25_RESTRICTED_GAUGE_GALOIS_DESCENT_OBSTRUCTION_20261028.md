# D25/LIFT — Exact failure of Galois orbit descent for restricted scalar gauge

Date: **2026-10-28**. Evidence status: **AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. This is a new auxiliary finite-field obstruction, not an original-class H0/B0 experiment and not an independent reviewer verdict. Frozen scientific source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

## Narrow question and prior result reused

The preceding author-only D25 Galois-descent theorem at Draft PR #1566 proves for the **full** two-cycle gauge `GL_m × GL_n` that Frobenius-fixed linear-gauge orbits descend exactly to the corresponding subfield. Its proof uses the geometric connectedness of every full-gauge representation stabilizer. The original H0/B0 permitted gauge subgroup is **not yet known**. We now determine explicitly how this descent identity can fail for a smaller, perfectly legitimate finite gauge subgroup. This closes a different, previously open *hypothesis-necessity* subproblem; it neither re-proves full-gauge descent nor replaces the native experiment.

## Carrier, operations and exact finite-field model

Let `p` be prime, `e≥1`, `k=F_(p^e)`, `r≥1` and `d|p−1`. Put `H=μ_d(F_p)={ζ∈F_p^×:ζ^d=1}`. Its order is exactly `d`. The typed **source carrier** is `M=k^r`; the restricted gauge acts by `ζ·v=ζ v`. This is realized in the prior two-cycle quiver as the unidirectional sector `Y=0`, with `X:k^r→k`, under the restricted block gauge `(ζ, I_r)∈GL_1(k)×GL_r(k)`. The coefficientwise Frobenius `σ` acts on `M` and commutes with `H`.

Define `Q(k)=M/H`, the set of **linear restricted-gauge classes**. Its class count is `|Q(k)|=1+(p^(er)−1)/d`. The additional semilinear quotient is `Q(k)/<σ>`. These are external auxiliary vector-space dimensions, not P000 native spatial dimensions. The only claimed future observer here is the full restricted-gauge class; stronger signed/source observers require their own equivariance/fiber-constancy proof.

## Theorem — exact Galois fixed-point defect

For each `0≤j<e`, write `g=gcd(e,j)` (with `gcd(e,0)=e`), `f=e/g`, and `h_j=gcd(d,f)`. Then

\[
\boxed{\#\operatorname{Fix}_{Q(k)}(\sigma^j)=1+\frac{h_j\bigl(p^{gr}-1\bigr)}{d}.}\tag{1}
\]

The number of `H`-orbits of vectors over the fixed subfield `F_(p^g)` is

\[
\boxed{L_{p^g}^{H}(r)=1+\frac{p^{gr}-1}{d}.}\tag{2}
\]

Thus **the exact descent defect** is

\[
\boxed{\#\operatorname{Fix}(\sigma^j)-L_{p^g}^{H}(r)
=\frac{(h_j-1)(p^{gr}-1)}{d}.}\tag{3}
\]

In particular, the full-gauge fixed-orbit/subfield-orbit equality does **not** remain valid for an arbitrary restricted gauge. Equality in this family holds exactly when `gcd(d,e/g)=1` (or the trivial `r=0` case, excluded by our hypotheses). By Burnside,

\[
\boxed{\#(Q(k)/\langle\sigma\rangle)
=\frac1e\sum_{j=0}^{e-1}\left(1+\frac{\gcd(d,e/g_j)(p^{g_jr}-1)}d\right),\quad g_j=\gcd(e,j).}\tag{4}
\]

**Proof.** Every nonzero `H` orbit has precisely `d` vectors. Its class is fixed by `τ=σ^j` exactly when `τ(v)=ζv` for some **uniquely determined** `ζ∈H`. The automorphism `τ` has order `f` and fixed field `F_(p^g)`. Applying `τ^f=id` to a nonzero solution forces `ζ^f=1`, so exactly `h_j` group elements qualify. For each such `ζ`, the equation `τ(z)=ζ z` on `k^×` has a solution because `Norm_(k/F_(p^g))(ζ)=ζ^f=1`: explicitly, `z↦z^(p^g−1)` has as its image the norm-one subgroup of the cyclic group `k^×`. Every solution is `z_0 w`, `w∈F_(p^g)^×`. Thus the eigenspace `E_ζ={v∈k^r:τ(v)=ζv}` is `z_0 F_(p^g)^r`, containing `p^(gr)` vectors. Different `ζ` eigenspaces intersect only at zero. Consequently the union of those eigenspaces has `1+h_j(p^(gr)−1)` vectors, and its nonzero vectors fall into free `H`-orbits of size `d`. This gives (1). Equation (2) counts zero plus the free nonzero `H`-orbits over the fixed subfield. Subtraction yields (3), and ordinary Burnside yields (4). The argument is exact for all fields in the stated scope. `□`

Note that the restricted stabilizer of a nonzero source is trivial, but the geometric finite gauge itself is disconnected; the connected full-gauge Lang argument cannot be transferred by substituting this `H`.

## Smallest operational two-arrow witness and p=373 specialization

For **odd** `p`, take `e=2`, `d=2`, and `r=2`. In the full two-arrow sector with `m=n=1`, restrict the two-block gauge to `H={(-1,1),(1,1)}`, acting on an ordered pair `(X,Y)∈k²` by simultaneous sign `(X,Y)→(-X,-Y)`. The scalar-action theorem applies to this pair of typed entries as an `r=2` source vector. It gives

\[
\#Q(k)=\frac{p^4+1}{2},\qquad
\#\operatorname{Fix}(\sigma)=p^2,\qquad
\#Q(F_p)=\frac{p^2+1}{2},
\]

and the exact semilinear count

\[
\boxed{\#(Q(k)/\langle\sigma\rangle)=\frac{(p^2+1)^2}{4}.}\tag{5}
\]

The count supplied by **incorrectly** reusing the full-gauge descent identity is `((p^4+1)/2+(p²+1)/2)/2`, smaller than (5) by `(p²−1)/4` (and potentially nonintegral for small cases). For `p=373`, `p²=139129`, the exact numbers are:

| Object | Exact count |
|---|---:|
| Raw ordered source pairs `(X,Y)` over `F_(373²)` | 19,356,878,641 |
| Restricted **linear** `H` gauge orbits | 9,678,439,321 |
| Frobenius-fixed restricted `H` orbits | 139,129 |
| Restricted `H` orbits from the base field `F_373` | 69,565 |
| Frobenius-fixed orbits with **no** base-field representative | 69,564 |
| True semilinear `H⋊Gal` orbits | **4,839,289,225** |
| False subfield-descent average | 4,839,254,443 |
| **Exact spurious identification deficit** | **34,782** |

Because `373≡5 (mod 8)`, `2` is a quadratic nonresidue. Let `k=F_373[t]/(t²−2)`; then `σ(t)=−t`. The pair `(X,Y)=(t,t)` satisfies `σ(X,Y)=(-t,-t)∈H·(X,Y)` and has `YX=t²=2∈F_373`. Its restricted `H`-orbit has **no** pair over `F_373`. Compare the base-field pair `(1,2)`: it has the same ordered composite `YX=2` but is **not** restricted-`H` gauge equivalent to `(t,t)`; they would become equivalent under the **full** `GL_1×GL_1` gauge via `(g,h)=(t^{-1},1)`. This supplies an exact source-typed witness of information loss from enlarging the gauge relation.

## Exact author-side checker and inference strength

`d25_restricted_gauge_galois_descent_checker_20261028.py` implements exact `F_(p^e)` using a monic irreducible polynomial found by integer polynomial trial division. It enumerates **all** vectors `k^r`, forms the entire finite `H` quotient, calculates Frobenius action on each orbit, verifies every fixed-point count `j`, and separately traverses the Frobenius orbit permutation for the semilinear count. It checks **17** `(p,e,r,d)` configurations, **91,104** raw-vector visits (counting each configuration), with `p∈{2,3,5,7,11}`, `1≤e≤4`, `r∈{1,2}`, and divisors `d|p−1`. The output JSON records the exact irreducible polynomial, counts and the analytical `p=373` witness; all assertions passed on the author side. The universal theorem follows from the displayed proof, **not** from finite tests. The `p=373` counts use closed formulas rather than a `373^4` state enumeration.

The witness is an auxiliary finite-field obstruction, not a native `Z/373²` divided-power Frobenius experiment. The original-class ring, H0/B0 source labels, actual allowed gauge, sign/odd operation and `Δ_p−R_p` mapping must come from the authorized original source before any native transfer.

## BRC and continuation boundary

BRC classification: **COMPOSE_APPLIED** to the typed quotient/observer factorization requirement. The carrier retains source coordinates and ordered arrows, the subgroup `H` is a **specified operation**, and the field/Galois quotient is the observer; (3) is the exact fiber defect caused by confusing fixed quotient classes with subfield classes. These are not positive branch masses, and no weighted/physical BRC claim is introduced. Any compression must separately prove that the intended signed future readout is constant on the exact declared gauge fibers. Neither `r` nor `e` represents native X6 spatial dimension, three-dimensional research slice, or time.

For original-class transfer, issue `awdawmip/enterprise-math#1559` must yield authentic same-class Frobenius, real subgroup `H`, original sign/odd source ports, and reproducible raw evidence. If the native permitted gauge is restricted or has disconnected stabilizers, the hypothesis of the prior full-gauge descent theorem must be checked rather than assumed. Preserve the author-only parent evidence at Draft PR #1566, and resolve native Source session/CLAIM/checkpoint through a legitimately authorized, Source-verified identity. UR V2 is a distinct original-source/provenance recovery task: exact required bytes `94,687`, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; mathematics was previously completed and is not repeated here.