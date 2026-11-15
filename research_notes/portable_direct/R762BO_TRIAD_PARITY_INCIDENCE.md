# R762BO — Odd-walk obstruction and a typed three-Port incidence lift on native X6

**Date:** 2026-11-15. **Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`. **Evidence:** author-proved / locally exact checked / `NOT_REVIEWED`. This is an independently preserved portable research artifact, not an authenticated Source CLAIM, PROGRESS, Result, Review, or change to P000.

## Frozen scientific scope

Input pins: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. P000 fixes the affine `Z^6` native Cell carrier, twelve signed primitive coordinate steps, six pairwise `PERP_E` axes at internal 120°, and the requirement that a primitive nonzero stable force balance has three quanta satisfying `TRIADIC_CLOSURE_E`. Original force closure is a distinct typed relation: the frozen sources do not equate it to return of a three-step coordinate walk.

The paper proves coordinate/path mathematics, then constructs an explicitly **candidate** co-localized force Port/Link incidence model; actual original force admission remains a separate question. A three-axis coordinate selection is not automatically a fully realized three-dimensional carrier slice. Signed raw coordinates are not the six-nonnegative-field final Cell address.

## Theorem 1 — Odd primitive paths cannot close spatially

Let `w=((i_1,s_1),...,(i_m,s_m))` be any signed native unit-step word (`i_j in {1,...,6}`, `s_j in {+1,-1}`), allowing backtracking and repeated axes. Define the anchor-independent displacement `D(w)=sum_j s_j e_{i_j} in Z^6`. Then

`sum_{a=1}^6 D(w)_a = m (mod 2)`.

In particular, for any odd `m`, `D(w) != 0`. Thus **none** of the `12^3=1728` three-step native spatial walks returns to its initial Cell. More generally the pure X6 signed-unit adjacency graph is bipartite, with Cell parity `chi(c)=sum_a coord(c)_a (mod 2)` (the color label depends on the chart anchor; the difference-parity statement does not). If a nonempty P000 primitive stable triad were identified *solely* with an odd three-step zero Cell displacement, that definition would give an empty force-closure family.

**Proof.** The additive homomorphism `chi:Z^6 -> Z/2Z`, `chi(z)=sum_a z_a mod 2`, sends every `+e_i` and `-e_i` to 1, since `-1=1 mod 2`. Consequently `chi(D(w))=m mod 2`; zero displacement has parity zero. This proves the assertion for every finite odd `m`, not only a bounded computation. QED.

For three **distinct** signed axes, the displacement has three coefficients of absolute value one; hence `||D||_1=3`, and the P000 component quadratic readout is `L_E(D)^2=3`. There are `6*5*4*2^3=960` ordered three-step words, `binom(6,3)*2^3=160` endpoints, and exactly six ordered shortest realizations per endpoint. The endpoint erases order and corresponding BRC path provenance.

## Theorem 2 — Exact two-block return multiplicity

Restrict a six-step word `w=u||v` to two length-three blocks, each containing three distinct signed axes. Then `D(w)=0` iff the signed-axis set of `v` equals the coordinatewise sign reversal of the signed-axis set of `u`. For each ordered `u`, exactly `3!=6` choices of `v` work. Therefore there are exactly **5760 ordered six-step returns** of this two-block form.

**Proof.** The three nonzero coordinates of `D(u)` uniquely determine its signed-axis multiset. Cancellation by `v` forces the same three axes with opposite signs, whose order can be any of six permutations; conversely those six words all cancel. Multiply by 960 possible `u`. This is a composite path-return count, not proof that either triple is an admitted physical force-balance event. QED.

## Typed candidate: directed three-Port / three-Link incidence closure

At a chosen X6 Cell `c`, let the signed Port labels be `P={(i,s):1<=i<=6,s=+1 or -1}`. Select three Ports `U={p,q,r}` on pairwise distinct axes, each with equal positive quantum `Q=1`. Give them exactly three **nonspatial, directed incidence Links** `p->q,q->r,r->p`, considered up to cyclic starting-point rotation. The proposed candidate closure predicate `C_cycle(c,U,gamma)` holds precisely for this simple directed three-Port Link cycle, with no other participating primitive Ports or Links. A Link here is an internal typed relation between co-located force Ports; it is **not** a primitive off-axis spatial segment or a three-step Cell-return path. This is a mathematically explicit nonempty candidate, not an identification of P000 `TRIADIC_CLOSURE_E` with a physical law.

**Theorem 3 — Exact finite incidence classification.** For three different Ports there are `(3-1)!=2` directed three-cycles. There are `binom(6,3)*2^3=160` different signed Port sets, so precisely **320 unrooted oriented incidence cycles**. A distinguished starting Port gives three rooted representatives of each cycle, therefore **960 rooted cycles**. There is no such simple three-cycle with 0, 1 or 2 active Ports; this particular model has primitive arity exactly three.

Under the admitted X6 coordinate-label permutation skeleton `S6`, relabel `i` and preserve sign and directed Link incidence. The 320 incidence events form exactly **four `S6` orbits**, indexed by the positive-Port count `k=0,1,2,3`, of cardinalities `40,120,120,40`. Indeed for each `k`, there are `20*binom(3,k)` signed Port sets and two directed cycles. The symmetric group on six names is transitive on cycles with a fixed number of positive labels, since one can map the three oriented Port positions and their signs to those of any target cycle; the unused axes permute arbitrarily. This proves the four-orbit classification. Covariance concerns the **candidate representation**; force/Link/Port rotation admission beyond the known coordinate permutation skeleton remains open.

**Theorem 4 — A source-faithful update and its exact observer loss.** Let a typed state be `(c,h)`, where `h` is an ordered sequence of timestamp/order-labelled candidate incidence events. Define `Append_theta(c,h)=(c,h||theta)` for an event attached to `c`. The Cell is unchanged, and time/order is not an additional spatial axis. Relabel an entire history under `pi in S6` entrywise. Then

`Append_{pi theta}(pi c,pi h) = pi Append_theta(c,h)`,

because relabelling commutes with concatenation. This update is an incidence-log semantics, not force propagation. The full named-cycle single-event observer distinguishes all 320 possible unrooted types; any exact binary record for every named-cycle query needs at least `ceil(log2(320))=9` bits, and storing the cycle identifier attains this. With a chosen root Port there are 960 possibilities, requiring `ceil(log2(960))=10` bits. A signed Port-set-only observer has 160 values (8 bits) and loses the **one-bit directed orientation**; a Cell-only observer loses the entire event. Named directed-Link queries distinguish the opposite cycles sharing a signed Port set, so suppressing orientation is not safe for future operations that query that direction. These minima apply to the **declared one-event observation/future-query scope**; they are not assertions about unbounded histories.

The candidate does not choose a physical sign rule, Link evolution law, circulation amplitude, rotation generator, or native event adjudication. It instead supplies a typed source-preserving construction that is mathematically consistent with the P000 arity/space typing and exhibits precisely why the pure spatial return test is unsuitable.

## Exact computation and evidence

Run `node R762BO_TRIAD_PARITY_INCIDENCE_VERIFY.js R762BO_TRIAD_PARITY_INCIDENCE_EVIDENCE.json` (Node.js 18+). The companion exact checker exhaustively checks 1728 three-step signed words and 960 distinct-axis words; verifies 160 distinct endpoints with multiplicity 6; checks all 921600 ordered pairs of distinct-axis three-step blocks and finds 5760 returns; tests the 720 permutations and 691200 individual port-word transport relations; classifies 320 cyclic events and 2880 sign-count orbit images. It uses exact integer/parity operations and no floating approximations. The local execution on 2026-11-15 passed all assertions. Theorems 1–4 have the mathematical arguments above independent of finite checks. Independent review remains `NOT_REVIEWED`.

## Next decisive work

Extract the actual admitted signed `TRIADIC_CLOSURE_E` Cell/Link/Port event predicate and actual V17/V29/V39 transport semantics from source under the preserved Task scientific pin, or record that an implementation remains absent. Test whether legitimate events satisfy a co-located Link closure of this kind, and compute their true stabilizers and source-aware BRC residual under declared future operations. The odd-path parity theorem remains valid regardless of the later force-incidence construction. Do not identify a coordinate observer with an admitted force event, or discard order/source branches without a scoped exact descent certificate.
