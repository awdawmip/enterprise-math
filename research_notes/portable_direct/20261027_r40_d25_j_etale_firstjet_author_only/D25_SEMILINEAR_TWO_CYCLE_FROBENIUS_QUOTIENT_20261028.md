# D25/LIFT — semilinear Frobenius quotient of the full two-cycle gauge orbit model

**2026-10-28. Author-only auxiliary theorem and exact check; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** This extends the already author-proved, unreviewed *linear* two-cycle triple-core theorem preserved on Enterprise Math Draft PR #1566. This model is a finite-field auxiliary representation, not the original fixed CM/H0/B0 divided-power Frobenius. The original-class input and actual admissible gauge group must be independently authenticated under Issue #1559 before any transfer to `Delta_p-R_p`.

## Precise question

Let `k=F_(p^e)` with coefficientwise Frobenius `σ(a)=a^p`, `V=k^m`, `W=k^n`, and `X:W→V`, `Y:V→W`. Fix the chosen `F_p` coordinate structures to make `σ(X)` and `σ(Y)` well typed. Define the extended (conditional) gauge group

\[
\widetilde G=(\mathrm{GL}_m(k)\times\mathrm{GL}_n(k))\rtimes\operatorname{Gal}(k/\mathbb F_p),
\]

acting by

\[
(g,h,\sigma^j)\cdot(X,Y)
 =\bigl(g\,\sigma^j(X)h^{-1},\,h\,\sigma^j(Y)g^{-1}\bigr).
\]

This is a **declared auxiliary observer**. Its Galois factor is not asserted to be a valid gauge operation on the original H0/B0 source-marked class.

## Theorem 1: exact classification and sharp stabilization under semilinear extension

Set

\[
S=\ker X\le W,\quad D=\operatorname{im}Y\le W,\quad T=YX\in\operatorname{End}_k(W),
\quad d=n-\dim S+\dim D-\operatorname{rank}T.
\]

For all `m,n≥0`, the `\widetilde G`-orbits of pairs `(X,Y)` are in natural bijection with `ΓL_n(k)=GL_n(k)⋊Gal(k/F_p)`-orbits of **joint triples** `(S,D,T)` satisfying

\[
 S\subseteq\ker T,\quad \operatorname{im}T\subseteq D,\quad d\le m.
\]

In particular, for `n≥1` and every finite field `k`, the orbit count strictly increases as `m` goes from `0` to `2n`, and stabilizes precisely for `m≥2n`. For `n=0` there is one orbit.

**Proof.** Under a linear gauge `(g,h)`, the triple transforms to `(hS,hD,hTh^{-1})`; the prior two-cycle theorem proves this triple is both complete and realizable when `d≤m`. Under coefficientwise `σ^j`, kernels, images and products commute with field automorphisms:

\[
(\ker X,\operatorname{im}Y,YX) \mapsto
(\sigma^j S,\sigma^j D,\sigma^j T).
\]

Consequently passage from the full linear gauge quotient to `\widetilde G` amounts *exactly* to subsequently taking Galois orbits of triples. Both `d` and its defining constraints are invariant under the extended action. The linear theorem supplies all triples with `0≤d≤2n` and a witness at **each** such `d`: choose `X` and `Y` with disjoint intermediate images and `YX=0` and ranks `r=min(d,n)`, `s=d-r`. Since `d` is invariant under the new Galois transformations, an orbit with `d=m+1` cannot be represented in dimension `m`; for `m≥2n` no larger core is possible. This establishes strictness and stabilization without assuming the Galois action is free. ∎

## Theorem 2: exact `n=1` semilinear orbit count

For `n=1`, write `\Gamma=Gal(k/F_p)`, `|\Gamma|=e`. Let

\[
C_{p,e}=\#(k^\times/\Gamma)
=\frac1e\sum_{j=0}^{e-1}(p^{\gcd(e,j)}-1),
\]

where `gcd(e,0)=e`. Then the exact counts are

\[
\boxed{\widetilde N_{p^e}(0,1)=1,\qquad
\widetilde N_{p^e}(1,1)=3+C_{p,e},\qquad
\widetilde N_{p^e}(m,1)=4+C_{p,e}\ (m\ge2).}
\]

**Proof.** The `n=1` triple components are `S,D∈{0,k}` and `T∈k`, with `S⊆ker T`, `im T⊆D`. For `T≠0` only `S=0,D=k` occurs; the ordinary `GL_1(k)` action fixes each scalar `T`, whereas Galois permutes it by `t↦t^p`. The zero-`T` triples comprise four possible ordered `(S,D)` combinations, with minimal core dimensions `0,1,1,2`. Hence `m=0` admits one, `m=1` admits three, and `m≥2` admits all four. The Galois action fixes these four flags. Burnside's lemma on `k^×` gives `C_(p,e)` because `Fix(σ^j)=F_(p^gcd(e,j))` has `p^gcd(e,j)−1` nonzero elements. ∎

This recovers the original linear `q+2` (`m=1`) and `q+3` (`m≥2`) when `e=1`, but changes the counts when `e>1`.

## Theorem 3: exact `F_4` full two-dimensional port certificate

For `k=F_4=F_2[z]/(z²+z+1)`, `W=k²`, the attached standard-library integer-only checker exhaustively enumerates all **seven** linear subspaces of `W`, all `4^4=256` endomorphisms `T`, and every triple satisfying the above constraints. Precisely **529** labeled triples survive. The complete `GL_2(F_4)` has order 180.

By core dimension `d=0,...,4`, explicit linear group orbits number

\[
\boxed{(1,6,27,6,1)},
\]

and Frobenius-fixed **linear orbit classes** number

\[
\boxed{(1,4,11,4,1)}.
\]

Burnside for the 2-element Gal group therefore yields the **semilinear** orbit distribution

\[
\boxed{(1,5,19,5,1)},
\]

and cumulative counts for `m=0,1,2,3,m≥4`:

\[
\boxed{\widetilde N_4(m,2)=(1,6,25,30,31)},
\]

compared with linear counts `(1,7,34,40,41)`. Thus Galois identifies precisely ten *pairs of distinct linear classes* at saturation, while leaving 21 linear classes fixed. The program obtains the 31 semilinear orbits in **two independently implemented ways**: apply Galois to all 41 enumerated linear orbits and use the involution fixed-point formula, and directly partition all 529 states under the full `GL_2(F_4)⋊Gal(F_4/F_2)` action. Both agree at every `d`. This is a finite exhaustive certificate for **exactly** this finite domain, and a code check of the general theorem's consequences; it is not a universal proof by enumeration.

## Exact `p=373` signed-observer witness and BRC boundary

At `p=373`, `2` is nonsquare in `F_p` (`2^186≡−1 mod373`). In the quadratic field `k=F_p[t]/(t²−2)`, Frobenius gives `σ(t)=−t`. In the `n=1,m=2` model, fix

\[
X(1)=\begin{pmatrix}1\\0\end{pmatrix},\qquad
Y_t(v_1,v_2)=t\,v_1.
\]

The pair `(X,Y_t)` has `T=YX=t`. Its coefficientwise Frobenius transform `(X,Y_{−t})` has `T=−t`. These are **one extended semilinear orbit**, but the signed coefficient-of-`t` readouts are `+1` and `−1` (equivalently `1` and `372 mod373`). Both have the same trace `0` and norm `−2=371 mod373`. This is an exact information-loss witness for the declared Galois-containing gauge quotient.

The certificate is **conditional on allowing σ as gauge**. If an original-class normalization marks which Frobenius orientation is physical, or its actual allowed gauge subgroup omits `σ`, the signed coefficient can remain meaningful. No claim is made that the native `H0/B0` observer admits this semilinear quotient. In particular the field `F_(373²)` calculation is not a replacement for a native `Z/373²` divided-power computation; their rings, precision and observers differ.

BRC interpretation: the carrier is the ordered, signed `(X,Y)` pair together with a declared Frobenius action and typed source basis. The observer for Theorems 1–3 is the **extended group orbit**, not the original CM source port. The three joint coordinates preserve exactly this quotient; further signed source observation is safe only after its fiber constancy under every **actually authorized** gauge generator and its subsequent operation horizon has been proved. Do not erase the sign by taking trace or norm before that descent check. This is an auxiliary finite-field relation theorem within the active P000/Heartbeat X6 project, **not** an extra native spatial dimension or an X6 reduction.

## Executed exact verification, source and next gate

Run `python d25_semilinear_two_cycle_frobenius_checker_20261028.py`; the same-branch JSON output is `d25_semilinear_two_cycle_frobenius_author_check_20261028.json`. Arithmetic is entirely exact GF(4) bit-polynomial and integer modular arithmetic. At all 529 admissible triples it checks GL-conjugacy closure, Frobenius invariance, the two semilinear counting routes and invariant `d`. It counts 7,380 direct complete-group images of one representative per linear orbit, and 11,160 direct images of one representative per semilinear orbit. These counts specify the exact actual loops, not inflated per-state comparison totals.

**Source controls.** This is a continuation of the *author-only* D25 auxiliary model family already on Draft PR #1566; original scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged. Native Source execution permission for this Site caller remains absent; Source CLAIM/run/Result/admission and independent replication are not asserted.

**Next exact scientific action.** The owner path at `enterprise-math#1559` must supply the real same-original-class Frobenius rank, normalization, sign/odd port and allowed gauge `H`. Check whether Frobenius conjugation belongs to `H`, and test fiber constancy for the source-marked signed `Delta_p-R_p` observer. If it does **not**, the native observer must retain a marked sheet/orientation or equivalent residual; if it does, a legitimate observer descent theorem is needed. Keep UR V2 four-file original-source recovery and proper writer/provenance/checkpoint work separate from this new auxiliary theorem.
