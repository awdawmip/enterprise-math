# EC49DD — Exact all-h positive-BRC rank degeneracies and two-parameter gauge invariance

**Status:** `AUTHOR_ANALYTIC_PROOF / INDEPENDENT_2CHANNEL_LITERAL_CHECK_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`.

**Scientific input snapshot fixed for this unit:** GLOBAL_KNOWLEDGE_V1 canonical `main@c7ecb04571837f8758569284f6ea77ed86b1c74a`; Enterprise Math canonical `main@a673d9c9852957727a17317b223423451f48f6a1`; predecessor EC49DB/DC PR #1730 `2d593a347014d05be6c1970710907495988706f0`. The global bootstrap/manual and the matching P000 projection (verified original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`), ACTIVE worldview, native X6, observer-preservation and portable research contracts were read. P000/worldview remain unchanged. Service 0.6.11 authenticated read returned `research_authority_granted=false`, `UPSTREAM_CODE_REVIEW_REQUIRED`, quota 5/5, with no verified active task owner, claim, Source-native research activity or independent review. This is an author-side durable **noncanonical** proof candidate, not a canonical Result or accepted Foundation theorem.

## 1. Declared population and positive-branch BRC

Retain the exact EC49DB object population: genuine ordered signed primitive six-axis paths `p` of fixed literal length `n` and chart-relative six-axis endpoint `D`; all complete returning suffix words in `S'={a,b,c,d,e}` of exactly `h`, or 1 through `h`, operations. The operations are `a=(-1,-1)`, `b=(-2,-2)`, `c=(+1,+2,-1,-2)`, `d=(+2,+1,-2,-1)`, `e=(+3,+1,+1,-3)`. For every suffix, keep the four joint final A/B tag outputs with A=(+1,+2), B=(+2,+1), including prefix/suffix boundary effects. Use two *separate* positive BRC channel products with positive-axis weights `x=(x1,...,x6)`, `y=(y1,...,y6)` and negative-axis weights 1, plus one independent branch-count channel. The full nine-state order-sensitive prefix process remains intact; no loss of native paths or later-access provenance is asserted.

Write `T_{s,t}(p)=1[tag(p·s)=t]`. The actual three-channel future-observer matrix on the fixed `(n,D)` fiber has rows

`F^x_(s,t)(p)=W_x(p) W_x(s) T_(s,t)(p)`, `F^y_(s,t)(p)=W_y(p) W_y(s) T_(s,t)(p)`, and `F^1_(s,t)(p)=T_(s,t)(p)`.

For `h>=2` and `n=2h+8`, put `k=|s|+v`, `delta=h-k` for `D=(2s,2v,0,0,0,0)`, `v>=0`, `k<=h`. The known order-sensitive tag-row upper bounds, from EC49DB's six-feature quotient, are

| Fiber | exact-depth tag bound `r_=h` | cumulative tag bound `r_<=h` |
|---|---:|---:|
| Boundary `delta=0` | 4 | 4 |
| Interior, odd `delta` | 5 | 6 |
| Interior, positive even `delta` | 6 | 6 |

The purpose of EC49DD is to determine **true rank loss at exceptional positive BRC weights**; EC49DC's polynomial `P=0` is only a potential certificate failure and is not by itself a rank-failure certificate.

## 2. Theorem A — two independent positive-weight gauge transformations

For any real `c,d>0` and arbitrary positive real `x,y`, replacing `(x,y)` with `(c x, d y)` preserves the rank of *every fixed `(n,D)` returning-suffix observer*, at every finite suffix depth. Rational inputs and positive rational `c,d` preserve the statement over Q.

**Proof.** Every prefix in the fixed fiber contains exactly

`P_+(p)=(n+sum_i D_i)/2`

positive letters, because each literal signed step contributes `+1` or `-1` to the sum of six endpoint coordinates. Thus `W_{cx}(p)=c^P W_x(p)` with the **same** `P` for all prefix columns. For a fixed complete suffix `s`, `W_{cx}(s)=c^{P_+(s)} W_x(s)`. Therefore the `x` observer row `(s,t)` is multiplied by the nonzero scalar `c^{P+P_+(s)}`. Similarly each `y` row is multiplied by a nonzero `d^{P+P_+(s)}`, and count rows are unchanged. This is invertible *row* scaling of the original matrix, so its rank is unchanged. End of proof.

**Interpretation:** these two overall channel scales are true gauge freedoms **for the declared fixed-length, fixed-endpoint observer only**; this does not delete the full ordered signed-X6 path, extend to mixed path lengths without a length coordinate, or establish a physical gauge law.

## 3. Theorem B — genuine low-rank algebraic strata for all finite horizons

Let `w*=(2,3,3,2,1,1)`. There is a single nonempty relatively Zariski-open, Euclidean-open dense subset `V` of the strictly positive real six-weight orthant, containing `w*`, with the following properties for **all integers `h>=2`** simultaneously, for every returning endpoint fiber at `n=2h+8`:

1. If `x=lambda w`, `y=w` for any `lambda>0` and `w in V`, then rank is exactly **`2r`** for each of the exact and cumulative observer languages. The same `2r` applies to `(x,y)=(alpha*1,w)` and `(w,beta*1)` for arbitrary `alpha,beta>0` and `w in V`. Here `1=(1,1,1,1,1,1)`; one of the three channels is redundant for each future suffix/tag, but the two retained channels are independent.
2. If **both** `x=alpha*1` and `y=beta*1`, for arbitrary positive `alpha,beta`, then rank is **exactly `r`** for each fiber. Both positive BRC channels are redundant relative to count, but the ordered-tag observer is still complete inside its declared tag-row subspace.

For positive rational weight parameters the identical rank assertions hold over Q. The formulas for the total observable rank at `n=2h+8` are:

| Weight stratum | exact `h` | cumulative `1..h` |
|---|---:|---:|
| Generic three-channel EC49DC open set (prior, not newly proved) | `3(11h^2+15h+8)/2` | `18h^2+24h+12` |
| The three explicit two-channel families in item 1 | **`11h^2+15h+8`** | **`12h^2+16h+8`** |
| Both channels axis-uniform | **`(11h^2+15h+8)/2`** | **`6h^2+8h+4`** |

This is a **partial stratification**, not a classification of all parameters on the certificate-zero locus. These are dimensions at `n=2h+8`; they do not claim the earliest reduced-weight saturation length equals `2h+8`.

### Proof: upper bounds and exact observer descent

In each row `(s,t)`, if `x=lambda y` then, since `P_+(p)` is fiber-constant, `F^x_(s,t)=lambda^{P_+(p)+P_+(s)} F^y_(s,t)`, with a scalar independent of prefix column `p`. If `x=alpha*1`, then `F^x_(s,t)=alpha^{P_+(p)+P_+(s)} F^1_(s,t)`; similarly `y=beta*1`. Thus rank is at most twice the tag-row rank `r` for all three two-channel families. If both channels are axis-uniform, **every** weighted row is a nonzero multiple of its corresponding tag/count row, hence rank equals `rank(T)<=r`. This is an exact observer-relative factorization, not deletion of branch provenance from the underlying object space.

### Proof: all-h lower bounds with nine fixed seed minors

The attached `VERIFY_EC49DD.py` consumes existing `EC49DB_SEEDS.json.zlib.b64` from the **same preexisting** EC49DB research directory (no replacement of the seed file). It independently constructs every literal signed-X6 prefix/suffix and recomputes tag, endpoint and the positive BRC channel with weights `w*`.

For each of the nine EC49DB seed families (exact h=2/3 and cumulative h=2), write its existing `r` selected suffix/tag rows into the **two-channel** matrix with rows `(W_w, count)`. The script selects `2r` actual prefix columns via modular Gaussian elimination and independently evaluates a nonzero `2r×2r` integer minor modulo prime 1,000,003. These nine determinantal polynomials in `w` are `d_j(w)`. It also selects `r` columns of the tag-only matrix with a nonzero `r×r` modular determinant. All nine `d_j(w*)` and tag-only minors are nonzero (exact recorded pivots and residues in `EC49DD_RANK_CERT.json`). Nonzero mod prime proves the corresponding integer determinant is nonzero over Q, not merely a floating numerical fit.

The original EC49DB gate insertions and horizon shifts preserve every literal final A/B suffix result and the last relevant positive-letter history. At arbitrary positive `w`, every selected *weighted* matrix row is multiplied by a fixed positive product `g_w`, independent of which prefix column is chosen; each count row is unchanged. The lifted selected `2r×2r` determinant is therefore `g_w^r d_j(w)`. The tag-only minors retain exactly their previous entries. The same nine seeds cover **every interior fiber and both future-depth languages for all h>=2** by the predecessor's explicit integer formulas, with no new guesswork about an unbounded grid.

For boundary fibers `|s|+v=h`, the EC49DA explicit four-tag gadget construction provides, in each tag, two paths with distinct `W_w` weights: choose the first two gadgets in each of its four classes. Their weight differences are nonzero at `w*` (16 vs 24; 36 vs 24; 24 vs 36; 24 vs 36). The EC49CZ positive-mixed boundary construction instead uses its tag-safe E3 neutral pair variant and its E1 variant; their weights differ by factor `w1/w3`, nonunit at `w*` (`2/3`). The selected two-branch/count minor in each tag is nonzero. Both constructions work at *every h* with only nonzero monomial endpoint factors, establishing 8-dimensional full rank in every boundary fiber. Their four count-tag rows already witness tag-only rank4.

Define `g_tau,1`, `g_tau,2` as the two fixed EC49DA gadgets in the program; let `w(g)=product of w_i along its four positive letters`, and set

`R(w) = (w1-w3) * product_tau (w(g_tau,1)-w(g_tau,2)) * product_(j=1..9) d_j(w)`.

Each `d_j` is an integer-coefficient polynomial in six variables. `R(w*)` is nonzero by the modular witness and the explicit differences above; thus `V={w>0:R(w) != 0}` is a nonempty relatively Zariski-open and Euclidean-open dense subset. Its **finite** determinant list certifies the same rank for **all** h; no countable intersection of varying generic sets is used. The special cases `x=lambda w,y=w` and one uniform channel follow the row-factorization upper bound; the other retained weighted/count rows attain `2r`. At both-uniform weights, the already proven tag-only rank `r` applies universally. End of proof.

## 4. Validation scope, exact evidence and limits

`python3 VERIFY_EC49DD.py --seeds EC49DB_SEEDS.json.zlib.b64` was actually run against the **original unchanged EC49DB seeds**. It generated `EC49DD_RANK_CERT.json` and returned `PASS`. The checker reimplements the X6 endpoint, A/B adjacency tags, positive BRC branch products, row generation, modular rank and determinants. It checked:

- all nine `r×r` tag minors and nine `2r×2r` positive BRC/count minors, including exact pivot column indices and residues;
- **1,298** independently reconstructed lifted interior `(h,fiber,language)` rank pairs for h=2..12 (each case checked both tag-only rank `r` and weighted/count rank `2r`);
- **957** explicit boundary fibers for h=2..30, each with a genuine eight-path `8×8` nonzero integer determinant modulo 1,000,003;
- all exact/cumulative rank sums over every fiber for each h=2..12, agreeing with the closed formulas above.

The analytic all-h statements come from fixed seed minors, explicit nonzero boundary monomials, the legal prefix/suffix lift and row factorization, **not** from extrapolating the finite run. The checker tests the positive BRC carrier, not signed amplitude interference, heartbeat dynamics, three-dimensional physical slices, phase restoration or general global minimal memory.

**Genuine unresolved problems:** classify the rest of `P(x,y)=0`, where failure of EC49DC's specific determinant witnesses may or may not mean actual rank loss; determine the **earliest** full tag-only and two-channel saturation lengths. For axis-uniform two-channel weights, the tag-only extremal endpoint D=(-2h,0,...,0) has at most three of the four tag outputs at `n=2h+4`, so tag-only global saturation needs at least `2h+6`, whereas the present construction gives the upper bound `2h+8`. This two-step gap is open. Independently formalize the finite witness and all-h lifting proof before scientific admission.

## 5. Exact continuation frontier

Do not repeat EC49DB's 3-channel all-h saturation proof or these nine 2-channel seed minors in the next turn. EC49DE should first prove or refute `n_sat^tag(h)=2h+6` for every h>=2, supplying exact all-fiber count-only path constructions or a minimal counterexample; next classify one extra nontrivial component of `P=0` not covered by proportional/uniform channel gauges. Preserve the same raw signed-X6 paths and positive-branch BRC scope. Native claimant/owner status remains unverified and acceptance pending; read the current source and review the manuscript independently.

## Post-publication checker metadata correction (same mathematical evidence)

The first EC49DD transfer archive (`EC49DD_FULL_EVIDENCE.tar.xz.b64`) captures the originally executed PASS verifier. That version omitted incrementing the **report-only** field `rank_formulas_checked_h2_to12[*].boundary_fibers` (therefore printing zero in those per-h summaries), despite computing and checking all corresponding boundary rows and the correct rank sums. The current standalone `VERIFY_EC49DD.py` and `EC49DD_RANK_CERT.json` increment it for each boundary, yielding `2h+1` for every h=2..12. The corrected local verifier was rerun against the unchanged nine original seeds, returned PASS with 1,298 interior and 957 boundary checks, and did not change any witnesses, determinant residues or theorem assumptions. The original archive remains byte-for-byte preserved for audit provenance; prefer the current source/checker and the current JSON certificate for the correct per-h metadata.
