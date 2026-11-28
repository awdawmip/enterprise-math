# D25/LIFT — exact invariant algebra and sharp polynomial observer depth for opposite-weight source ports

**2026-10-28; author-derived auxiliary theorem / exact-checked / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** This is a theorem about a declared finite-field scalar gauge action. Its algebra is a standard cyclic invariant-theory construction applied here to the source/provenance observer question; it is not a claim of novel general invariant theory, a native CM identification, or a canonical Source Result. Previous two-port orbit enumeration and Galois fiber counts on Draft PR #1566 are reused, not recounted as new work.

## Scientific question, carrier and BRC use

Let `k=F_q`, `q=p^e`, and `d | q-1`, `d>=2`. Let `H=mu_d(k)` act on the **ordered, oriented** carrier `(x,y) in k^2` by

`zeta.(x,y)=(zeta*x,zeta^(-1)*y)`.

Preserve the two source ports, the direction of the action, the coefficient field, the allowed group, and the intended future polynomial-observer horizon. The prior product-only observer `c=xy` is invariant but loses phase/oriented branch information. The BRC interface used here is exact *observer-fiber constancy*: determine the full invariant polynomial algebra, a finite separating coordinate system, and the least degree at which an invariant polynomial can distinguish a product fiber. This establishes sufficiency **only for H-invariant polynomial operations** (and operations proven to factor through their algebra), not arbitrary signed Green/Hesse, normalized native Frobenius, or unmarked source reconstruction.

## Theorem 1 — complete invariant polynomial algebra, no omitted relation

Set `c=xy`, `u=x^d`, and `v=y^d`. Then, as **graded k-algebras** (with `deg(c)=2`, `deg(u)=deg(v)=d`),

\[
\boxed{k[x,y]^H\cong k[c,u,v]/(uv-c^d).}
\]

**Proof.** The order of `H` is `d`, and `p` does not divide `d` because `d | q-1`. The monomial `x^a y^b` has weight `zeta^(a-b)`, so a polynomial is `H`-invariant exactly when every nonzero monomial coefficient has `a-b=0 mod d`. To see the `only if` without cancellation, decompose the polynomial ring into the direct sum of the `d` character-weight subspaces; distinct monomials are linearly independent and the group contains a primitive `d`-th root. If `a>=b`, the invariant monomial is `c^b u^((a-b)/d)`; if `b>=a`, it is `c^a v^((b-a)/d)`. Thus `c,u,v` generate. The relation `uv=c^d` holds. Reducing any polynomial in `k[c,u,v]` modulo this relation leaves only monomials `c^i`, `c^i u^j (j>=1)`, or `c^i v^j (j>=1)`; their images have distinct `(x,y)` exponent pairs. Hence there are no additional polynomial relations and the proposed presentation is injective. `QED`.

The presentation is over the algebraic polynomial ring, not merely equalities of function-values at `q^2` points. In particular its grading remains meaningful even when a high-degree polynomial coincides with a lower-degree function on the finite point set.

## Theorem 2 — exact rational-orbit separator and realizability condition

For every pair of **k-rational** source states, equality of `(c,u,v)` is equivalent to `H(k)`-gauge equivalence. The k-point images of the invariant map are exactly the triples satisfying `uv=c^d` and `u,v in {0} union (k^times)^d`, with the following zero rule: `u=0` iff `x=0`, and similarly for `v`.

**Proof.** If `x,x' !=0` and `x^d=(x')^d`, then `zeta=x'/x` belongs to `H`. If `c=xy=x'y'`, it follows that `y'=zeta^(-1)y`. If `x=x'=0`, equality of `v=y^d=(y')^d` gives the same conclusion for `y !=0`; for both zero the orbit is trivial. The case `x!=0, x'=0` contradicts equality of `u`. Conversely `c,u,v` are invariant. The stated realizability condition is necessary. It is sufficient when `u,v !=0`: choose `x^d=u`, set `y=c/x`, then `y^d=c^d/u=v`; on either zero axis choose the nonzero root directly. `QED`.

The orbit cardinality follows without a hidden source-collapse: `1` origin orbit, `2(q-1)/d` oriented axis orbits and `(q-1)^2/d` nonzero-product orbits, totaling `1+(q^2-1)/d`. This count and the earlier product-fiber classification already appear in prior author work; the newly supplied information is the complete algebra of allowable polynomial observers and its sharp degree bound.

## Theorem 3 — sharp minimal polynomial observer degree

**For every `d>=2`, any H-invariant polynomial of total degree strictly less than `d` is a polynomial in `c=xy`.** Therefore a family of H-invariant polynomial coordinates separating **all** H-orbits on `k^2` must include an observer of degree at least `d`. This lower bound is attained by `(c,u,v)`, whose maximum degree is exactly `d`.

**Proof.** An invariant monomial `x^a y^b` with `a+b<d` satisfies `a-b=0 mod d`. Since `|a-b|<=a+b<d`, we have `a=b`, so the monomial is `c^a`. Weight-space decomposition from Theorem 1 extends this to every polynomial. The two states `(1,0)` and `(0,1)` have the same `c=0` but lie in distinct oriented gauge orbits; every invariant polynomial of degree `<d` gives them the same value. Finally `(c,u,v)` separates all orbits by Theorem 2 and has degree at most `d` because `d>=2`. `QED`.

This minimality is **for separating all k-point H-orbits using invariant polynomial coordinates**, with ordinary total degree counted in the source coordinates. If nonpolynomial indicators such as zero-port ranks are admitted, or if only a restricted nonzero branch is observed, the minimal-degree question changes. For `d=1` the action is trivial and the two linear coordinates `(x,y)` suffice; the lower bound becomes one.

## Theorem 4 — norm-one gauge and Frobenius descent at quadratic extensions

Let `k=F_(p^2)` for odd prime `p`, `k_0=F_p`, and `H=ker(N_{k/k0})=mu_(p+1)(k)`. Thus `d=p+1`, and

\[
\boxed{(c,u,v)=(xy,N(x),N(y)),\quad u v=N(c).}
\]

The two source norms are in `F_p` and the product may be in `k`. The triple separates every H-orbit and any H-invariant polynomial observer of total degree `<p+1` factors through `c` over `k`. In particular **the first polynomial invariant capable of separating every source-gauge orbit has source degree exactly `p+1`**.

The k-orbit is Frobenius-fixed exactly when `c` lies in `k_0`: Frobenius sends `(c,u,v)` to `(c^p,u,v)`, and the triple is a complete invariant. For a fixed `c in k_0^times`, the `p-1` possible nonzero norms `u` index the fixed gauge orbits; exactly `(p-1)/2` have a representative `(x_0,y_0) in k_0^2`, namely those where `u=x_0^2` is a quadratic residue. On `c=0`, there is the origin and two oriented sets of `p-1` norm-labeled fixed orbits; `1+2*(p-1)/2=p` of these have a base-field representative. Hence

\[
\boxed{\#\mathrm{Fix}_{\sigma}=p^2,\qquad
\#\mathrm{Fix}_{\sigma}\text{ with a base-field source}=\frac{p^2+1}{2},\qquad
\#\text{descent failures}=\frac{p^2-1}{2}.}
\]

**Proof.** Surjectivity of the finite-field norm, `ker N=mu_(p+1)`, and Theorems 1–3 give the separation and degree statements. Frobenius fixes `u,v`; it fixes the orbit iff it fixes `c`. For `c in k_0^times`, a base-field source has `N(x_0)=x_0^2`; conversely if `u=x_0^2`, set `y_0=c/x_0`, which has the required `N(y_0)`. The zero axes are analogous. Count the strata as above. `QED`.

This reuses the previously computed Galois fixed-orbit totals; its new role is to identify **the exact minimal polynomial degree** of a complete permitted source-gauge observer and derive an explicit norm-coordinate certificate for the BRC future-operation gate.

### Exact `p=373` witness, and the coefficient-ring boundary

Take `k=F_373[t]/(t^2-2)` (irreducible because `373=5 mod8`, hence `2` is a nonsquare). `Frob(t)=-t`, so `N(t)=(-t)t=-2=371 mod373`. For `(x,y)=(t,t)`, `c=2` lies in `F_373` and the H-orbit is Frobenius-fixed, while `u=N(t)=371` is a **nonsquare** in `F_373`, so no `F_373` source representative exists. The state `(1,2)` has the same product `c=2` but `u=1`; the norm coordinate distinguishes them. The sharp polynomial observer degree is

\[
\boxed{d=p+1=374,\quad \#\mathrm{Fix}=139129,\quad
\#\text{base-representable}=69565,\quad
\#\text{failures}=69564.}
\]

These are **field-extension** facts. The native original-class `p=373` coefficient ring `Z/373^2` is not `F_(373^2)`; neither the order-374 norm-one gauge nor this polynomial bound is attributed to native H0/B0 without a verified source interface.

## Executed exact checks and limits

`d25_opposite_weight_invariant_ring_checker_20261028.py` uses Python standard-library exact modular arithmetic. Fourteen prime-field `(p,d)` cases cover 2,198 ordered source states, 131 monomials below the claimed threshold checked at all 21,563 monomial/point combinations against a generating gauge element, and exact orbit separation by `(c,u,v)`. Three quadratic-extension cases `p=3,5,7` cover 3,107 ordered states and all norm-one gauge orbits, with independent Frobenius-fixed and base-representative counts. All assertions passed. The `p=373` case uses exact Legendre-symbol arithmetic and the above formulas; **no full `373^4` enumeration was run**. The universal polynomial invariant algebra and degree lower bound are algebraic proofs; finite checks are author-side falsification tests, not independent review.

## Source and next transfer gate

- Reused prior author-only interface: `research_notes/portable_direct/20261027_r40_d25_j_etale_firstjet_author_only/D25_DUAL_WEIGHT_PRODUCT_FIBER_GALOIS_DESCENT_20261028.md` and `D25_FIELD_DEFINED_CYCLIC_GAUGE_H1_DESCENT_20261028.md`, existing Draft PR #1566 at pre-unit head `12646b78e55d3dec94583a72472d23f9aa5ace30`.
- Frozen scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. P000 ACTIVE Heartbeat X6 and joint observer preservation remain prior project assumptions, but auxiliary field dimensions are not native X6 axes.
- BRC resolution: `COMPOSE_APPLIED` at **declared gauge-invariant polynomial observer algebra** and **finite future polynomial-operation horizon**. An arbitrary source-marked observer `f` descends only if `f(zeta*x,zeta^(-1)*y)=f(x,y)` for all actual allowed `zeta` and source states. If it fails, retain that source port instead of replacing it by `c`/norm data.
- Native gate: authorized owner from `awdawmip/enterprise-math#1559` must first supply the genuine CM H0/B0 original-class mod `p^2` coefficient ring, Frobenius, actual gauge and signed odd source port. Only then identify (or refute) this auxiliary opposite-weight representation and test exact future-operation fiber constancy for `Delta_p-R_p`.
- Exact Source execution/session/claim/review/writer is unverified for this caller. GitHub author storage does not confer those states. The UR V2 original four-file 94,687-byte SHA256 match remains a separate provenance-only recovery obligation; do not re-prove UR mathematics or synthesize an unverified replacement.
