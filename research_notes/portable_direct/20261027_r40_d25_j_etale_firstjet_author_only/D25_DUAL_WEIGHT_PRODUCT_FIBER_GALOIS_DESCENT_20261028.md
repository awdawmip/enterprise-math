# D25/LIFT — Dual-weight two-arrow gauge: exact composite-product fibers and Galois descent

**Research date:** 2026-10-28. **Author-side classification:** `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`. **Frozen scientific Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (preserved). Parent objective: source-faithful original-class H0/B0 Frobenius and signed `Δ_p−R_p`; the results below concern a strictly specified auxiliary finite-field model, not the original CM class.

## 1. New, narrow question and previous results consumed

The existing Draft PR #1566 contains (a) full `GL_m×GL_n` two-arrow classification, (b) Lang/Galois descent for the full gauge, and (c) exact scalar-gauge descent obstructions for `μ_d(F_(p^e))` acting with **the same weight** on all coordinates. The actual two-arrow block-change operation on `X:k→k`, `Y:k→k` uses **opposite weights** `X↦uX`, `Y↦u^(−1)Y`, so the composite `YX` is invariant. In a general cyclic subgroup this dual-weight representation is **not** the previous same-weight representation: for example, if `u` has order above 2, the same-weight action sends `XY↦u² XY`.

The new problem is to count, **within each fixed composite-product observer fiber**, which restricted-gauge classes remain distinguishable, which Frobenius-fixed classes have a fixed-subfield source, and exactly what source coordinate repairs the collapsed observer. This reuses the previous cyclic-cohomology calculation but does not reproduce its scalar-vector theorem as a new result.

## 2. Typed data, operations, and observables

Let `p` be a prime, `e≥1`, `k=F_q` with `q=p^e`, and `d|q−1`. Let `H=μ_d(k)⊂k^×`, a specified **restricted gauge**. The source is the ordered pair of directed arrows `(x,y)∈k×k`, and its action is

\[
\zeta\cdot(x,y)=(\zeta x,\zeta^{-1}y),\qquad\zeta\in H. \tag{1}
\]

The composite observer `c=xy∈k` is strictly H-invariant. For `0≤j<e`, the future operation is coefficientwise Frobenius `τ=σ^j` with `σ(z)=z^p`. It normalizes H, so τ acts on the orbit set `Q=k²/H`. Put

\[
 g=\gcd(e,j),\;k_0=\mathbb F_{p^g},\;q_0=p^g,\;S=\frac{q-1}{q_0-1},\;
 t=\gcd(d,q_0-1),\;h=\gcd(d,S),\;M=\frac{q-1}{d},\;
 c_j=\frac{ht}{d}.
\tag{2}
\]

Here `gcd(e,0)=e`. Existing scalar-gauge work proved `c_j=|H¹(<τ>,H)|∈Z_{≥1}`; below we derive how it controls each dual-weight composite fiber. All parameters `p,e,j,d`, ranks and field dimensions are **external auxiliary algebra**; none are native X6 axis counts, native three-dimensional layers or independent time axes.

## 3. Theorem A — complete source-faithful orbit coordinates and sharp full-gauge information loss

Let `C=k^×/H`, a cyclic group of order `M`. The restricted-gauge orbits are in canonical bijection with the following **disjoint** set:

\[
\boxed{\;
\{\mathbf0\}\;
\sqcup\;
(\{X\text{-only}\}\times C)\;\sqcup\;
(\{Y\text{-only}\}\times C)\;\sqcup\;
\bigsqcup_{c\in k^\times}(\{c\}\times C).
\;}\tag{3}
\]

In the `c≠0` fiber, the complete coordinate is `(c,[x]_H)` with `y=c/x`. At `c=0`, the complete coordinate is one of: the zero state; `X-only` together with `[x]_H`; or `Y-only` together with `[y]_H`. Therefore

\[
\boxed{|Q|=1+(q+1)M=1+\frac{q^2-1}{d}.}\tag{4}
\]

The complete **full** `GL_1(k)×GL_1(k)` gauge quotient has `q+2` classes: one for each `c≠0`, and the three zero-product types. The full-gauge projection deletes exactly

\[
\boxed{(q+1)(M-1)}\tag{5}
\]

restricted-gauge orbit distinctions; at each `c≠0` it collapses `M` classes into one, and at `c=0` it collapses the `M` classes in each nonzero directed branch into one. If `H=k^×` (`d=q−1`, `M=1`), the loss is exactly zero. This is **classification by the declared gauge**, not a statement that all original-source distinctions are physically measurable.

**Proof.** Every nonzero pair `(x,y)` has trivial H-stabilizer, since either nonzero arrow forces `ζ=1`. If `xy=c≠0`, the arrow x determines y as `c/x`, and two choices of x give H-equivalent pairs exactly when they differ by H, yielding one copy of C. If `xy=0`, both arrows cannot be nonzero; the two one-arrow branches stay distinct under (1) and each has C classes, in addition to the fixed zero pair. This proves (3)–(4). For the full block gauge, any two nonzero choices of x with fixed c are related by a suitable element of `k^×`; both nonzero zero-product branches each form one full-gauge orbit. This proves the `q+2` count, and subtracting it from (4) gives (5). `□`

## 4. Theorem B — Galois fixed-point and descent defect, resolved *per composite fiber*

Define

\[
 a_j=\gcd(M,p^j-1),\qquad b_j=\frac{q_0-1}{t}. \tag{6}
\]

Then **exactly** `a_j` restricted H-orbits in each nonzero `c∈k_0^×` fiber are τ-fixed; exactly `b_j` of them admit a representative whose two arrows lie in `k_0`. Every nonzero `c\notin k_0` has **zero** τ-fixed orbits. In the zero-product fiber there are

\[
 \boxed{1+2a_j\ \text{τ-fixed classes},\qquad1+2b_j\ \text{subfield-representable classes}.}\tag{7}
\]

The two nonzero directed zero-product branches each contribute `a_j` and `b_j`, respectively. The exact identity

\[
 \boxed{a_j=c_j b_j=\frac{h(q_0-1)}d}\tag{8}
\]

makes the **per-fiber and total non-descent defects** explicit:

\[
\boxed{D(c\ne0)=a_j-b_j=b_j(c_j-1),\quad
D(0)=2(a_j-b_j),}\tag{9}
\]

\[
\boxed{\#\mathrm{Fix}_Q(\tau)=1+(q_0+1)a_j,\quad
D_{\mathrm{all}}=(q_0^2-1)\frac{c_j-1}{t}.}\tag{10}
\]

For each fixed nonzero product `c∈k_0^×`, the τ-fixed classes split into exactly `c_j` cohomological obstruction labels, each occurring `b_j` times. The same uniform distribution holds **separately** in each nonzero branch of `c=0`. In every fiber, the trivial label is exactly the set of classes with a fixed-subfield source. Thus the obstruction tag is the smallest *categorical* repair for the specific yes/no descent question, while the full coset `[x]_H` or `[y]_H` is required to recover the complete restricted-gauge state.

**Proof.** On a nonzero fixed product `c∈k_0^×`, equation (3) identifies the H quotient with `C=k^×/H`, and τ acts as `zH↦z^(p^j)H`. Since C is cyclic of order M, its τ-fixed subgroup has cardinality `a_j=gcd(M,p^j−1)` (with `gcd(M,0)=M`). For a zero-product nonzero directed branch the same C action applies, giving `1+2a_j` including the zero state. An orbit fixed by τ must have τ(c)=c, proving the absence of fixed orbits above `c∉k_0`.

A class represented by `x∈k^×` has a representative in `k_0^×` iff its coset lies in the image of `k_0^×→C`. The kernel is `k_0^×∩H` of size `t`, so the image has cardinality `b_j=(q_0−1)/t`, with the same size in each fiber. For the zero-product branches use x or y accordingly.

For the refinement, the cyclic exact sequence `1→H→k^×→C→1` yields, on τ-fixed elements, the exact sequence

\[
1\to H^\tau\to k_0^\times\to C^\tau
\xrightarrow{\delta} H^1(\langle\tau\rangle,H)\to1.
\tag{11}
\]

The surjectivity of `δ` can be proved without assuming a nontrivial black-box: a cocycle representative `ζ∈H` has norm one, so the equation `τ(u)/u=ζ` has a solution `u∈k^×`, by cyclicity of `k^×` (the image and norm-one subgroup both have order `(q−1)/(q_0−1)`). The solution coset `uH∈C^τ` maps to `[ζ]`. Moreover a fixed coset maps trivially exactly when it comes from `k_0^×`. The earlier exact cyclic-group calculation gives `|H^1|=ht/d=c_j`. Since all are finite groups, every δ-fiber has size `|\mathrm{im}(k_0^×)|=b_j`, proving (8) and the uniform obstruction partition. For `c≠0` use `δ([x])=[τ(x)/x]`. For `Y-only` use the inverse-weight form `[y/τ(y)]`, which gives the same descent criterion and the same uniform label counts. Equations (7), (9) and (10) follow by summing over the `q_0−1` nonzero products and two nonzero zero-product branches. `□`

**Source/observer safety interpretation.** The product `c=xy` is invariant under allowed H gauge but is not a complete state. At `c≠0` the missing source coordinate is the multiplicative coset `[x]_H`; at `c=0` even the directed branch must be retained. No future readout or operation that distinguishes those classes may be represented by c alone. The cohomology label repairs *subfield descent*, not all other future operations. This is a direct, typed BRC **COMPOSE_APPLIED** to a joint/composite observer, with no positive-mass or physical-energy interpretation.

## 5. Exact `p=373` signed-source witness, in a genuine opposite-weight action

Take `p=373`, `k=F_373[t]/(t²−2)`, `t²=2`, and `H=ker(N_{k/F_373})=μ_374(k)`. Because `373≡5 (mod8)`, `t^373=−t`, `N(t)=−2≡371`, and `−2` is a **nonsquare** in `F_373`. This is the dual-weight action (1), not the earlier same-weight scalar action. Put `c=2`.

Two representatives are `(x,y)=(t,t)` and `(1,2)`. Both have `xy=2`, but they are **not H-gauge equivalent**: `N(t)=−2` is a nonsquare while `N(1)=1` is a square, and H is precisely the kernel of the norm. Their full `GL_1×GL_1` classes coincide. The class of `(t,t)` is fixed by Frobenius since `σ(t,t)=(-t,-t)=(-1)·(t,t)` under (1), with `−1∈H`; yet it has **no** base-field representative because any `u∈F_373^×` has square norm `u²`.

Here `q=139129`, `d=374`, `M=372`, `q_0=373`, `t=2`, `c_1=2`, `a_1=372`, `b_1=186`. Exact counts:

| Object | Exact count |
|---|---:|
| Restricted dual-weight H-orbits over k | **51,756,361** |
| Full `GL_1×GL_1` two-arrow orbits | 139,131 |
| Source distinctions lost by enlarging H to full gauge | **51,617,230** |
| Frobenius-fixed H-orbits in each nonzero `c∈F_373` fiber | 372 |
| Of those, with a base-field source | 186 |
| Of those, without a base-field source | **186** |
| Frobenius-fixed H-orbits in the `c=0` fiber | 745 |
| Of those, with a base-field source | 373 |
| Of those, without a base-field source | **372** |
| All Frobenius-fixed H-orbits | 139,129 |
| Of those, with a base-field source | 69,565 |
| All non-descending Frobenius-fixed H-orbits | **69,564** |
| Full semilinear H⋊Gal orbit count | **25,947,745** |

All large numbers are exact consequences of (4)–(10), not `373^4` state enumeration. The checker separately verifies the quadratic-nonresidue Legendre equalities by modular exponentiation.

## 6. Executed author-side exact check and limitations

Companion checker `d25_dual_weight_product_fiber_checker_20261028.py` reuses only the original integer-exact finite-field `Field` arithmetic from the previous checker `d25_restricted_gauge_galois_descent_checker_20261028.py` in the same PR directory. It traverses **all** raw dual-arrow states and explicit H-actions in **19 configurations** with `p∈{2,3,5,7}`, `1≤e≤4`, `d|p^e−1`; it examines each Frobenius power, all fixed product fibers, exact base-source representative membership, each cocycle-label distribution, and independent direct Frobenius-cycle traversal against Burnside.

Executed totals: **22,982 ordered raw states**, **23,157 explicitly computed gauge-element actions** in orbit construction, all case-level assertions passed. The checker also verifies the full-gauge loss (5) and the p373 closed-form witness. Detailed result JSON is `d25_dual_weight_product_fiber_author_check_20261028.json`; finite exhaustions are author verification, not independent peer review and not a universal proof by themselves. Universal statements are established by the exact algebraic arguments above.

A real H0/B0 transfer needs **original-class** module rank, exact ring and Frobenius direction/normalization, true permitted gauge subgroup, signed/odd Green–Hesse operation and `Δ_p−R_p` source map from authorized native evidence. The canonical support intake remains `awdawmip/enterprise-math#1559` (`PENDING_OWNER / NATIVE_NOT_EXECUTED` at its cited status). The known original scalar readout at p373 has `Δ=R=196 mod373`, which must not be mistaken for `Δ=0`. The separate completed UR portable mathematics needs only its authentic four-file V2 bundle verification (expected 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) and authorized writer/provenance, not another proof.

**Continuation:** Preserve the existing scientific source pin; consume the exact Source continuation and permitted owner scope before any canonical mutation. This author PR is neither a CLAIM/OPEN/session nor a Source checkpoint/Result/Driver review. If Source returns `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`, perform complete source `input_artifacts` readback and keep predecessor `completed_units=[]`; these current author artifacts are staging, not predecessor research. Retain present mathematical result and signed source coordinates when the native bridge becomes available.
