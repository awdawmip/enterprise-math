# R49 — Orbit-sumset phase automaton and permanent two-state Farey source transfer

**Status:** author-side exact derivation, finite exact computations and independent-regression evidence; independent mathematical review pending. **Frozen science:** `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct predecessors: R46 #2000, R47 #2003, R48 #2005. This studies the original-owner-labelled auxiliary irrational circle rotation with half-open arcs, not a newly claimed native X6/heartbeat dynamics.

## R49.1. Finite orbit-sumset automaton

Fix irrational `theta in (0,1)` and positive integers m,H. The boundary phases `{z theta}` for `z=0,...,m-1` define m sorted, original-labelled, cyclic half-open arcs `I_k`. For every phase x define

`A_H(x)[k] = min{1<=r<=H: {x-r theta} in I_k}`,

with an empty marker if no source age hits the arc. For the actual integer source endpoint j, `A_H({j theta})` is exactly its history-label-preserving vector of most recent source ages.

**Theorem.** `A_H(x)` is constant on each of at most m+H right-half-open circle intervals cut at `{s theta}`, `s=0,...,m+H-1`, and takes the cell to the right at a cut.

**Proof.** Age r crosses an original arc boundary z exactly at `{x-r theta}={z theta}`, equivalently `x={(r+z)theta}`. The additive index set of all possible crossings is `[1,H]+[0,m-1]=[1,m+H-1]`; add the phase 0. Irrationality makes these distinct cuts. Between adjacent cuts, no age-r membership changes; hence every original-labelled minimum age remains unchanged. The half-open arc rule determines right-continuous membership at each crossing. QED.

Let s* maximize `{s theta}` among `1<=s<=m+H-1`. Then the final phase cell is `[{s* theta},1)`, and every phase in it has the identical entire vector `A_H({s* theta})`. This compression preserves the identity and latest source index `j-r_k` of each original history label.

## R49.2. Permanent transfer on upper Farey neighbors

Let `a/i<theta<c/j` be positive-denominator Farey/Stern–Brocot neighbors and set `u=i theta-a>0`, `v=c-j theta>0`. Under the mediant traversal:

* If `(a+c)/(i+j)<theta`, the lower neighbor changes and v is unchanged.
* If the mediant lies above theta, it becomes the upper neighbor; `v_new=v-u`, with `0<v_new<v`.

Thus v is monotone nonincreasing for all future Farey stages. Define `q*=1-{s* theta}`. Whenever an upper neighbor satisfies `0<v<=q*<1`, its phase `{j theta}=1-v` lies in the final cell of R49.1. Consequently

`A_H({j theta})=A_H({s* theta})`

for that stage **and every later upper-neighbor stage**, even when denominators or partial quotients become arbitrarily large. At equality, the right-hand cell is selected by the half-open rule. This is a structural infinite-family theorem for the specified fixed irrational parameter, m,H and original labels; it does not require a bound on the future denominator.

## R49.3. Exact frozen S23/AV instance

Set `m=128,H=225,K=m+H-1=352,D=10^24` and certify `theta in (LO/D,HI/D)` with

`LO=262204504569236716045286, HI=262204504569236716045287`.

For all `s=0,...,352`, the floors of s*theta and (225-s)*theta remain constant throughout the enclosure. Exact integer comparisons at both endpoints show the largest cut phase is **uniquely s*=225**. Hence the rightmost cell throughout the parameter enclosure is `[{225 theta},1)`, with threshold

`q*=59-225 theta`,

whose numerator at LO is `3986471921738889810650` over D.

The original Farey compiler visits 78 stages. Its first two have upper denominator j=61 and upper numerator c=16. In stage 3, j=225,c=59, so `v=q*`. By upper-error monotonicity, the remaining **76 stages share the single 128-label source-age vector computed at j=225**. The first two share the vector computed at j=61. This is why all 76 distant stages have minimal suffix length 164: they share *every component*, not just the maximum. The j=61 vector has maximum age 225.

The only source-to-history differences required for the two initial vectors are `j-r-z`, j in {61,225}, 1<=r<=225, 0<=z<=127. Their union is exactly the 516 integers `[-291,224]`. Exact floor equality at the two parameter endpoints for all those integers certifies no boundary crossing anywhere in the parameter enclosure. Equality at a history boundary (difference 0) is retained with the original half-open semantics. The two computed vectors agree componentwise across both enclosure endpoints.

The vectors' compact-JSON-array SHA256 values are:

`j=61: 61622022fd12070d24bc6e3754f44aa3c75592201447cda61b6fccec5425081f`

`j=225: 061dd2812eda4fb5fba2d00e483d0b8c09c6c4ab111ae24e0ecf304ca58f4a78`.

## Exact output and source classification cost

Two-source-vector initial classification scans **225+164=389 ages per theta enclosure endpoint**, or 778 across the two endpoints. R48 classified 12,914 per endpoint or 25,828 total. The reduction in these like-for-like source inspection slots is **96.987765216%**. The independent R49 audit still reruns all 78 stage vectors at both endpoints (156 whole-vector matches), keeping audit work separate from production work.

The R45/R46 labelled-source risk compiler uses the event position `n=s-r_k+1` in each Farey stage. With two permanently transferable vectors, the independently executed program regenerates 78 stages, **9,697 positive steps** and **298 maximal affine runs**. Final exact risk is

`R_(10^12+128)=-4017401528447+15321634290944 theta`.

The full 15,356-byte regression TSV has SHA256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`, identical to the immutable R32/R46/R48 reference.

## Additional phase-atlas experiment

An independently written full phase-cell verifier constructs all **353** cells and checks them at LO and HI. The 353×128 tables agree, with **291 distinct original-labelled age vectors**; 226 cells have maximum age at most 164. The total angular measure of their union is the exact affine expression `5462-20828 theta` (approximately 0.80457883194). The two initial Farey stages occupy cell 351; the later 76 all occupy cell 352. By equidistribution of an irrational rotation, the exact angular measure is also the natural density of **all integer offsets** whose 164-source suffix hits all 128 arcs. This is a separate consequence using the standard irrational-rotation equidistribution theorem.

## Cost scope, reproducibility and next question

Each source inspection requires modular integer arithmetic and a binary search among m sorted historical phases. The two-state method also incurs original-history construction, a 353-cut certificate, 516 difference-floor stability checks, Farey generation, event construction, precision bookkeeping and output production. The reported reduction concerns repeated source classification slots and does not silently become an end-to-end bit-time claim. A generic phase-cell atlas costs `O(H(m+H) log m)` source/owner comparisons plus `O(m(m+H))` stored age entries, then gives arbitrary-endpoint lookup in `O(log(m+H))` phase comparisons. The two-state upper-error path avoids constructing that atlas for this frozen instance.

Reproducibility: `VERIFY_R49_COMPACT.py` is a runnable integer-only, standard-library verification script and produces the 298-run SHA256. The full independently executed two-state audit, complete 353-cell atlas and both JSON witness tables are retained in the original research bundle. Mathematical acceptance, formal shared-task CLAIM, independent review and native X6 transfer retain their separate authorities.

**R50:** Detect the earliest permanent-transfer stage for other irrational theta,m,H from the continued-fraction / Farey error stream; certify a failing pre-threshold example; compare full integer bit costs with R32, per-stage scanning and the generic atlas.