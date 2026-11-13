# D25/LIFT — Exact Galois cocycle obstruction for field-defined cyclic gauge

**Date:** 2026-10-28. **Evidence status:** `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`. **Frozen original scientific source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3`, unchanged.

## Scope and non-duplication

This is a narrowly scoped extension of the earlier author-only `D25_RESTRICTED_GAUGE_GALOIS_DESCENT_OBSTRUCTION_20261028.md` on Draft PR #1566. The predecessor treated **only** `H=μ_d(F_p)`, `d|p−1`, acting by scalars on `F_(p^e)^r`. Here `H=μ_d(F_(p^e))` may be **defined over the extension field**, `d|p^e−1`, and Frobenius acts nontrivially on H. The new output is an exact **cohomological classification and uniform fiber count** of fixed gauge classes, not merely another toy example. This does not re-prove the prior full `GL_m×GL_n` descent theorem or constitute an original CM H0/B0 computation.

### Typed carrier, group, and observers

Let `p` be prime, `e,r≥1`, `k=F_(p^e)` and `d|p^e−1`. Let `H=μ_d(k)⊂k^×` act **freely on nonzero vectors** of `M=k^r` by scalar multiplication, and let `Q=M/H`. Frobenius `σ(v)=v^p` acts coordinatewise and preserves H as a set; the resulting action on Q is well-defined. For any `0≤j<e`, set

\[
\tau=\sigma^j,\quad g=\gcd(e,j),\quad k_0=\mathbb F_{p^g},\quad
f=e/g,\quad S=\frac{p^e-1}{p^g-1},\quad
 t=\gcd(d,p^g-1),\quad h=\gcd(d,S).
\]

Here `gcd(e,0)=e`. The **observer** is the full H-orbit of the ordered source vector. The future operation under examination is Frobenius, with the explicit question whether a τ-fixed gauge class has a source representative in the fixed field `k_0`. Neither the quotient nor its model dimension is identified with native P000 X6 space, native three-dimensional slices or the original H0/B0 module.

## Theorem — exact cocycle labels and uniform descent-failure fibers

The cyclic cohomology group for the τ-action on H is

\[
\mathcal C_j :=H^1(\langle\tau\rangle,H)
   =\frac{\ker(N_{k/k_0}|_H)}{\{\tau(u)/u:u\in H\}},
\qquad |\mathcal C_j|=c_j=\boxed{\frac{ht}{d}}\in\mathbb Z_{\ge1}.
\tag{1}
\]

Every **nonzero** τ-fixed H-orbit has a canonical cocycle obstruction **class** in `C_j`: choose `v≠0` in the orbit, write the unique scalar relation `τ(v)=ζv`, and take `[ζ]∈C_j`. This class is independent of the representative `v` and completely decides descent: **the H-orbit meets `k_0^r` if and only if `[ζ]=1`.**

The map from τ-fixed, nonzero H-orbits to `C_j` is **surjective** and every cohomology label has **exactly**

\[
\boxed{\frac{p^{gr}-1}{t}} \tag{2}
\]

H-orbits. In particular,

\[
\boxed{\#\operatorname{Fix}_{Q}(\tau)=1+\frac{h(p^{gr}-1)}{d}},\tag{3}
\]

\[
\boxed{\#\{[v]\in\operatorname{Fix}_{Q}(\tau):[v]\cap k_0^r\ne\varnothing\}=1+\frac{p^{gr}-1}{t}},\tag{4}
\]

and the exact **non-descent defect** is

\[
\boxed{D_j=\frac{p^{gr}-1}{t}\left(\frac{ht}{d}-1\right)}.\tag{5}
\]

Thus this scalar-gauge family has exact fixed-orbit descent for the j-th Frobenius power if and only if `ht=d`, equivalently `C_j` is trivial. The full semilinear H-orbit count is

\[
\boxed{\widetilde N_{p,e,d}(r)=\frac1e\sum_{j=0}^{e-1}
\left(1+\frac{\gcd(d,(p^e-1)/(p^{g_j}-1))(p^{g_jr}-1)}d\right)},\quad g_j=\gcd(e,j).\tag{6}
\]

All claims hold for every prime `p` and every stated `e,r,d`; the finite enumeration below is a check, not the universal proof.

### Proof

Because `k^×` is cyclic of order `p^e−1`, the kernel of the norm `N_{k/k_0}(z)=z^S` intersects H in exactly `h=gcd(d,S)` elements. The coboundary homomorphism `H→H`, `u↦τ(u)/u=u^{p^j−1}`, has kernel `H∩k_0^×` of order `t=gcd(d,p^g−1)`, so its image has size `d/t`. Its image is contained in the norm kernel (the product telescopes). Consequently `h t/d` is an integer, and (1) follows.

If `[v]` is τ-fixed and `v≠0`, there is a **unique** `ζ∈H` with `τ(v)=ζv`. Iterating τ exactly `f` times yields `N_{k/k_0}(ζ)=1`. Replacing `v` by `uv`, `u∈H`, changes ζ to `(τ(u)/u)ζ`; thus `[ζ]∈C_j` is well-defined. Its class is trivial precisely when there is `u∈H` making `τ(uv)=uv`, i.e. when the same H-orbit contains a vector of `k_0^r`. This proves the descent equivalence.

For any `ζ∈ker(N|_H)`, the scalar equation `τ(z)=ζz` has a nonzero solution. One elementary proof: the image of `z↦τ(z)/z=z^{p^j−1}` in cyclic `k^×` has size `(p^e−1)/gcd(p^e−1,p^j−1)=S`, exactly the size of the norm-one kernel; hence the two coincide. Every vector solving `τ(v)=ζv` lies in `z k_0^r`; there are exactly `p^{gr}−1` nonzero solutions. The different ζ-eigenspaces are disjoint away from zero.

For a prescribed cohomology label, the ζ-values form one coboundary coset of size `d/t`. Accordingly exactly `(d/t)(p^{gr}−1)` nonzero vectors represent that label. Quotienting by the free H-action divides by d, proving (2), its surjectivity and the count `c_j`. Adding the unique zero orbit yields (3); the trivial label plus zero yields (4); subtraction yields (5). Averaging (3) over the e Frobenius powers by Burnside proves (6). `□`

## Exact recoveries of earlier results

**Earlier base-defined sign/scalar gauge:** if `d|p−1`, then `t=d` and `S≡f (mod d)`, so `h=gcd(d,f)` and (3)–(5) specialize exactly to the preceding theorem on `μ_d(F_p)`. This is genuine theorem reuse, not a second proof of the same statement.

**All scalar gauge:** if `H=k^×`, `d=p^e−1`, then `h=S` and `t=p^g−1`, so `ht=d` and the obstruction vanishes for every j. The condition is connected to, but is not claimed to imply, the earlier full-quiver `GL_m×GL_n` stabilizer theorem; those are different gauge actions.

## A qualitatively new p=373 obstruction with extension-defined H

Take `k=F_(373²)=F_373[t]/(t²−2)`; 2 is a quadratic nonresidue, so `σ(t)=−t`. Set `r=1`, and take the **norm-one group** `H=ker(N_{k/F_373})=μ_374(k)`, which is **not contained in** `F_373^×`. Here `d=374`, `g=1`, `S=374`, `t=gcd(374,372)=2`, `h=374`, hence `|C_1|=2`. Equations (3)–(5) give

\[
\#Q=373,\quad \#\operatorname{Fix}(\sigma)=373,\quad
\#\text{fixed H-orbits with an }F_{373}\text{-representative}=187,
\quad\boxed{D_1=186}.
\]

The norm gives a **complete** nonzero H-orbit invariant `N:k^×/H≅F_373^×`, hence every H-orbit is Frobenius-fixed; however an `F_373` representative `c` has norm `c²`, a square. The source `v=t` has norm `N(t)=−2=371`, a **nonsquare** in `F_373`, so `[t]` is Frobenius-fixed without any base-field representative. The loss is not repaired by observing that the quotient invariant itself lies in the base field. The `186` missing classes are the nonsquare norm fibers. This is an algebraic **auxiliary** finite-field source example and is **not** a native `Z/373²` Frobenius lift or CM-class measurement.

For a smaller complete certificate, take `F_9/F_3`, `d=4`, `r=2`: there are `21` linear H-orbits, `9` Frobenius-fixed H-orbits, `5` of those containing an `F_3²` representative, `4` failing descent, and `15` semilinear orbits. The obstruction group has order 2. These counts are exhaustively checked below.

## Executed, exact author-side verification

The companion checker `d25_general_mu_d_galois_cocycle_checker_20261028.py` imports only the exact polynomial finite-field arithmetic (`Field`) from the already-published previous author checker `d25_restricted_gauge_galois_descent_checker_20261028.py` in this **same directory**. It enumerates **all** vectors, all H actions, all H-orbit representatives, all Frobenius powers and the cocycle classes; separately traverses Frobenius orbit permutations to check the Burnside count. For each nonzero fixed orbit, it verifies all coordinate equations `τ(v)=ζv`, its cohomology label, uniform fiber counts and equality of trivial-label orbits with exact fixed-field representative orbits. The check used **17 full-field configurations, 11,971 configuration-weighted source vectors and 90,788 configuration-weighted H actions**; all assertions passed. The p=373 row is computed exactly by formula and Legendre-symbol arithmetic rather than enumerating a 373² field.

Evidence is an author's exact computation + universal algebraic proof, not an independent mathematical review. It is not an actual original-class H0/B0 test, and it grants no Source CLAIM/Result/acceptance.

## BRC, original-source boundary and precise continuation

`COMPOSE_APPLIED`: the **carrier** is the ordered source vector, the **operation** is restricted scalar gauge plus Frobenius, the **observer** is the H-quotient, and the cohomology class `[ζ]` is the smallest additional source tag that decides base-field descent of a fixed orbit. A coarser Frobenius-fixed/readout-in-base classification deletes exactly the `D_j` non-descent source distinctions in (5); retaining this cocycle tag repairs this **particular declared** observer. This makes no claim about unrelated future observers or a universal BRC-positive-mass reduction.

The original parent scientific target is source-faithful `H0/B0` Frobenius, signed/odd Green–Hesse and `Δ_p−R_p`, with scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` fixed. `enterprise-math#1559` still requires the genuine original-module rank, norm/η directions, allowed norm-one or other gauge subgroup, observer map, and raw native experiment. Only after that can any of (1)–(6) be tested for transfer to the original source. The already-completed UR portable math has a **separate** unresolved exact four-file V2 provenance target: 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. No old mathematics is re-run or an unattested bundle reconstructed.
