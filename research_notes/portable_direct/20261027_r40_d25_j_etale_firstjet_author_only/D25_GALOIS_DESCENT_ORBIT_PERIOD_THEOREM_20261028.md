# D25/LIFT — Galois descent and exact orbit-period repair for the two-cycle observer

**Date:** 2026-10-28. **Status:** AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. **Scope:** auxiliary finite-field matrix representation only, conditional on the *declared* full linear or semilinear gauge groups. **Scientific source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unaltered). Related author-only predecessors: full two-cycle joint-triple classification and semilinear Frobenius quotient, Draft PR #1566. This note proves a new **field-descent counting and exact period-repair theorem** rather than repeating the joint-triple proof.

## Question and typed interfaces

Fix a prime `p`, an integer `e>=1`, `k=F_(p^e)`, `V=k^m`, and `W=k^n`. The auxiliary **carrier** is the ordered, source-typed directed pair

\[
X:W\to V,\qquad Y:V\to W.
\]

The full linear gauge is `G(k)=GL_m(k)×GL_n(k)`, acting as `(g,h)·(X,Y)=(gXh^{-1},hYg^{-1})`. Write `L_q(m,n)` for the number of its orbits when `k=F_q`. The additional *conditional* gauge includes coefficientwise `Gal(k/F_p)=<σ>`, `σ(a)=a^p`, acting simultaneously on both arrows. Let `\widetilde L_(p,e)(m,n)` be the resulting semilinear orbit count. An original H0/B0 source-marked signed observer is **not** assumed to be invariant under this added action.

The previously verified *author-side* joint classification uses the **linked** triple `(S,D,T)=(ker X,im Y,YX)` with `S⊆ker T`, `im T⊆D` and `d=n−dim S+dim D−rank T≤m`. In this note the observer is first the whole linear orbit class, and then its Galois quotient. A minimal repair mark refers only to restoring the **linear orbit class**, not the full raw `(X,Y)` or any native CM/DP object.

## Lemma: connected algebraic stabilizers

For every algebraically closed extension `\Omega` of `F_p` and every pair `(X,Y)` over `\Omega`, its stabilizer in `GL_m(\Omega)×GL_n(\Omega)` is the unit group of

\[
E_{X,Y}=\{(u,v)\in M_m(\Omega)\oplus M_n(\Omega):uX=Xv,\;vY=Yu\}.
\]

The equations defining `E` are **linear**, so `E` is an affine space. The stabilizer is the nonempty Zariski-open set `det(u) det(v)≠0` inside that space; it contains the identity, is smooth and geometrically irreducible, and is therefore geometrically connected. The acting product of general linear groups is also smooth and connected. This argument holds for all `m,n`, including singular, nilpotent and zero arrows; it does not require a classification of indecomposable representations.

## Theorem A: Galois-fixed full-gauge classes descend exactly

For any divisor `g|e`, the `Gal(k/F_(p^g))`-fixed elements of the set of `G(k)`-orbits of `(X,Y)` are **in bijection** with the `G(F_(p^g))`-orbits of the same typed pairs defined over `F_(p^g)`:

\[
\boxed{\#\operatorname{Fix}_{\sigma^g}\bigl((\operatorname{Hom}(W,V)\oplus\operatorname{Hom}(V,W))/G(k)\bigr)
      =L_{p^g}(m,n).}
\]

In particular, `Fix(σ^j)` has cardinality `L_(p^{gcd(e,j)})(m,n)`, where `gcd(e,0)=e`.

**Proof.** Let `F=F_(p^g)` and take the algebraic closure `\bar F`. An `F`-Frobenius-stable geometric orbit `\mathcal O` contains an `F`-rational point: if `Frob(x)=a·x`, Lang's surjectivity for connected `G` produces `b` with `b^{-1}Frob(b)=a^{-1}`, so `b·x` is Frobenius-fixed. The stabilizer of any rational point is geometrically connected by the lemma. Applying Lang's theorem to this stabilizer proves that all `F`-points in the geometric orbit form one `G(F)`-orbit, and likewise all `k`-points form one `G(k)`-orbit. Thus an `F`-stable `G(k)`-orbit is the base change of exactly one `G(F)`-orbit, and two distinct `F`-orbits cannot coalesce over `k`. An orbit fixed by `σ^j` is fixed under the cyclic subgroup it generates, precisely `Gal(k/F_(p^{gcd(e,j)}))`. This proves the claimed bijection and count. `\square`

**External standard theorem used:** Lang's theorem for connected smooth algebraic groups over a finite field: the map `z↦z^{-1}Frob(z)` is surjective. This is a known theorem, not a custom assumption or an author-side finite experiment. Original reference: S. Lang, *Algebraic Groups Over Finite Fields*, American Journal of Mathematics 78 (1956), 555–563, DOI `10.2307/2372673`. Its hypotheses are explicitly checked above; no `sorry`, `admit` or target-specific axiom is introduced.

**Important boundary.** The conclusion uses the **whole** `GL_m×GL_n`-orbit relation and its connected stabilizers. For smaller partial gauge groups, disconnected stabilizers or a pinned physical source basis, this descent equality requires a separate proof and can fail. Native H0/B0 falls under this boundary until its actual gauge group is authenticated.

## Theorem B: exact orbit count and optimal period repair

By Burnside's lemma and Theorem A,

\[
\boxed{\widetilde L_{p,e}(m,n)
 =\frac1e\sum_{j=0}^{e-1} L_{p^{\gcd(e,j)}}(m,n).}\tag{1}
\]

For each `d|e`, let `E_d` be the number of linear gauge classes of **exact** Frobenius orbit length `d`. Since a class has period dividing `d` precisely when it is fixed by `σ^d`, Möbius inversion yields

\[
\boxed{E_d=\sum_{a\mid d}\mu(d/a)L_{p^a}(m,n),\quad
       \#\{\text{semilinear orbits of period }d\}=E_d/d.}\tag{2}
\]

Consequently the necessary and sufficient **per-orbit repair alphabet** for recovering a linear orbit class after forgetting its Frobenius sheet has size exactly `d`: one of the `d` elements in that semilinear orbit must be marked. In information bits the best fixed-length binary mark for that orbit needs `\lceil\log_2 d\rceil` bits. The mark is conditional on an authorized linear-gauge target and may be unnecessary for a genuinely semilinear-invariant future observer.

**Proof.** Burnside counts the orbits of the cyclic Galois action on the finite set of linear gauge classes. For `d|e`, fixed classes under `σ^d` are the disjoint union of exact-period classes indexed by divisors of `d`, so standard Möbius inversion gives (2). On a semilinear orbit of length `d`, any decoder back to one of the `d` different linear classes must distinguish all `d`; the cyclic period position is sufficient. No stronger raw-state or native source reconstruction is claimed. `\square`

## Corollary C: closed formulas for every two-dimensional observation port

The already author-proved all-rank linear full-gauge classification gives (for `n=2`, `q=p^a`)

\[
L_q(m,2)=\begin{cases}
1&m=0,\\ q+3&m=1,\\ q^2+3q+6&m=2,\\ q^2+4q+8&m=3,\\ q^2+4q+9&m\ge4.
\end{cases}
\]

Define the integer Burnside averages

\[
A_{p,e}=\frac1e\sum_{j=0}^{e-1}p^{\gcd(e,j)},\qquad
B_{p,e}=\frac1e\sum_{j=0}^{e-1}p^{2\gcd(e,j)}.
\]

Then **for all primes `p`, extension degrees `e>=1`, and all `m>=0`**, equation (1) simplifies to

\[
\boxed{\widetilde L_{p,e}(m,2)=\begin{cases}
1&m=0,\\ A_{p,e}+3&m=1,\\ B_{p,e}+3A_{p,e}+6&m=2,\\
B_{p,e}+4A_{p,e}+8&m=3,\\B_{p,e}+4A_{p,e}+9&m\ge4.
\end{cases}}\tag{3}
\]

This extends the prior `F_4` observation-port enumeration from one field to **every finite extension**, and gives all exact Frobenius periods by (2). For `n=1`, (1) also recovers the previous scalar coefficient-orbit formula, without re-proving it.

## Exact integer witnesses and finite enumeration

For saturated `n=2, m>=4`:

| Field | Linear classes | Exact-period linear classes | Semilinear classes |
| --- | ---: | --- | ---: |
| `F_4/F_2` | 41 | `E_1=21, E_2=20` | **31** |
| `F_8/F_2` | 105 | `E_1=21, E_3=84` | **49** |
| `F_16/F_2` | 329 | `E_1=21, E_2=20, E_4=288` | **103** |
| `F_9/F_3` | 126 | `E_1=30, E_2=96` | **78** |
| `F_25/F_5` | 734 | `E_1=54, E_2=680` | **394** |
| `F_(373²)/F_373` | 19,357,435,166 | `E_1=140,630, E_2=19,357,294,536` | **9,678,787,898** |

The last line is an **auxiliary extension field** result. `F_(373²)` and the native divided-power coefficient ring `Z/373²` are not the same structure; the p=373 row is **not** an H0/B0 experiment.

The attached independently written integer-only checker enumerates every two-by-two matrix and **the entire generated `GL_2` group** over `F_4`, `F_8` and `F_9`. This is the `X`-invertible sector of the two-cycle pair with the canonical normalization `X=I_2`, so its orbit problem is exactly similarity of `T=YX`. For those three fields respectively, the complete matrix state counts are `256, 4,096, 6,561`; group orders `180, 3,528, 5,760`; linear similarity class counts `20, 72, 90`; Frobenius-fixed similarity class counts `6, 6, 12`; and semilinear similarity counts `13, 28, 51`. The checker also verifies the Frobenius permutation cycles and equations (1)–(3), including all five `m` values in six selected fields/degree cases. All executed assertions passed. These finite checks support only their stated domains; the universal assertion depends on the lemma and Lang's theorem.

## Residual-fidelity interpretation and native transfer gate

Under the declared two-cycle auxiliary structure, the ordered pair `(X,Y)` is the typed source carrier and a **linear gauge orbit** is the retained observer before Galois compression. The full semilinear quotient eliminates the *Galois sheet*, with exact local deficit `d−1` linear-class distinctions for an orbit of length `d`. Formula (2) computes exactly which compression fibers have which size; a period label is a **minimal sufficient repair coordinate** for restoring the former linear-gauge observer.

BRC resolution: `COMPOSE_APPLIED` at the observer/fiber-constancy interface, not an assertion that signed matrix entries are positive BRC mass. The signed or odd source port must remain typed; future operators are allowed to descend only if they are equivariant under the declared quotient and the intended readout is constant on its fibers. For the original `Delta_p−R_p`/H0–B0 problem, the independent native input owner at `enterprise-math#1559` must first provide the actual original-class Frobenius direction, module rank, allowed gauge subgroup, source orientation/odd port and compatible coefficient ring. A smaller or physically marked native gauge may retain a distinction even when the auxiliary full semilinear group would erase it.

The P000 six native spatial axes plus independent time and three-dimensional research-slice requirement remain unchanged. Neither `m`, `n`, the finite field extension degree, nor the Galois period is a native spatial dimension or a time coordinate.

## Continuation and evidence limitations

- Reuse the previous full-gauge joint triple classification and fixed `F_4` 529-triple check as predecessor **author-only** evidence, not Source predecessor-completed units.
- Exact source/role check for this run: Gateway `0.6.11`; Sites `static_machine_readonly`, `write_relay_enabled=false`, `research_authority_granted=false`; existing original request `r40_20261028_0239_task_inventory_read_v1` read returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` / `operation_sent=false`, own checkpoint list `ACCESS_DENIED`. No executable Source CLAIM or session was verified.
- This note is author proof and local exact check, not independent theorem review, formal check, native calculation or canonical Task admission. No Source result/checkpoint/claim, no reset of the frozen pin, and no scheduler change.
- Separate UR V2 original-source gate: preserve the completed mathematics, locate the **original** four-file bundle and verify byte length `94,687` and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` before any provenance checkpoint. Historical isolated uploads with `source_published=false` are neither a recovered full bundle nor native task publication.
- **Next smallest scientific discriminator:** once #1559 supplies native original-class Frobenius/gauge/odd port, test whether its authorized gauge is the connected full `GL_m×GL_n` (and whether coefficientwise Galois conjugation is allowed). Then test source-marked odd observer fiber-constancy on the actual native quotient. An exact failed descent check is a useful negative result. Until then, do not promote this auxiliary theorem into a native claim.
