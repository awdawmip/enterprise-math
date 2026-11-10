# R37 — Certified suffix saturation for many-arc last-source selection

Date: 2026-11-10. **Status: author-side theorem and exact computation; independent mathematical review pending.**
Parent frontier: R36, PR #1951, commit `31312689388d3ed5accac612f1bf6a94ba2bcc1f`.
Frozen S23/AV science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
This is an auxiliary finite-horizon rotation observer, not a claim about native X6/BRC dynamics; P000 remains unchanged.

## Exact problem and last-source theorem

Fix an irrational `0<θ<1`, historical phases `{sθ}` for `0<=s<m`, and their `m` circular half-open arcs `I_k` (left endpoint included). Given an integer source window `[j-N,j)`, `N>=1`, define the labelled final source

`τ_k(j,N)=max{t∈[j-N,j):{tθ}∈I_k}`, or `⊥` if the set is empty.

For each arc define its backward hitting age
`r_k(j)=min{r>=1:{(j-r)θ}∈I_k}` and `H(j)=max_k r_k(j)`.
By irrational-rotation density, every `r_k(j)` is finite.

**Theorem R37.1 (suffix saturation).** If `N>=H(j)`, all owners are represented and `τ_k(j,N)=j-r_k(j)`. If `N<H(j)`, a complete backward scan of `N` sources computes `τ_k` and every missing owner exactly. A reverse scan can therefore stop as soon as (a) all `m` owners have been encountered or (b) all `N` sources have been visited, whichever happens first.

**Proof.** Backward scan age `r` increases while source index `j-r` strictly decreases. The first hit of `I_k` is hence its greatest source index among all older hits. Once each arc is seen, none of the omitted older sources can replace its first hit. Exhaustion of the window similarly visits every allowed source. The first depth at which all `m` owners are seen is precisely `H(j)`. QED.

Consequently R36's owner-labelled histogram is preserved. In any fixed applicable Farey stage the extinction function still satisfies
`F(n)=m-h+# {finite τ_k : τ_k<n-i}`, with `h` finite labels; hence R35's risk-increment formula applies without materializing the full source window.

## Exact covering certificate via rational convergents

Let `δ>0` be the minimum circular arc length of the historical partition. For any reduced rational `p/q` (`gcd(p,q)=1`) define
`ε=(q-1)|θ-p/q|` and `G=1/q+2ε`.

**Lemma R37.2 (perturbed q-grid).** The maximum circular gap between the `q` phases `{rθ}` for `0<=r<q` is at most `G`. Whenever `G<δ`, every block of `q` consecutive integer sources meets all historical arcs, and `H(j)<=q` for every integer `j`.

**Proof.** The residues `{rp/q}` form the uniform `q`-grid; the circle distance between each associated true phase and its grid node is at most `r|θ-p/q|<=ε`. Were a circular gap between observed phases longer than `1/q+2ε`, removing `ε` at each end would leave an arc longer than `1/q`; it would contain a grid node whose associated observed phase must lie in the alleged empty gap. Contradiction. Every shift of a block of `q` consecutive indices translates the phase set by a common angle and preserves its maximum gap. Thus each arc of length at least `δ>G` contains a point. QED.

**Rational-interval certificate.** With `θ∈[ℓ,u]`, the historical circular order is stable if `floor(dℓ)=floor(du)` for every `1<=d<m`. A lower bound for each historical arc length is its midpoint value minus `m(u-ℓ)`; let their positive minimum be `δ_*`. If

`1/q+2(q-1)max(|ℓ-p/q|,|u-p/q|)<δ_*`,

then `H(j)<=q` for all `θ∈[ℓ,u]` and all integer `j`. In a reverse scan, a selected source `t` assigned to arc with consecutive historical endpoints `s,e` has interval-invariant owner if both `floor((t-s)ℓ)=floor((t-s)u)` and `floor((t-e)ℓ)=floor((t-e)u)` (with identically zero differences handled as exact ties). Only these two adjacent boundaries can change that owner. Hence a saturated suffix carries a whole-parameter-interval final-source certificate without classifying any earlier source.

## A uniform theorem for bounded partial quotients

**Corollary R37.3.** Suppose the ordinary continued-fraction partial quotients of irrational `θ` are all bounded by a fixed integer `A>=1`. Then for any history length `m>=2` and every integer `j`,

`H(j)<4(A+1)(A+2)m.`

Thus every owner-labelled `τ_k(j,N)` is computable with `O_A(m log m)` exact phase comparisons, independently of the window length `N`, after sorting history phases.

**Proof.** Standard convergent best-approximation inequalities give `||dθ||>1/((A+2)d)` for each integer `d>=1`: if `q_k<=d<q_{k+1}`, then `||dθ||>=||q_kθ||>1/(q_k+q_{k+1})`, and `q_{k+1}<=(A+1)q_k`. An arc between two historical phases corresponds to an index difference `1<=d<m`, so its length is at least `||dθ||>1/((A+2)m)`. Choose the first convergent denominator `q>=4(A+2)m`, and let `q_next>=q` be its successor. Since `|θ-p/q|<1/(q q_next)`, the grid-gap bound gives `G<1/q+2/q_next<=3/q<=3/[4(A+2)m]<δ`. Hence `H(j)<=q`. The convergent recurrence and minimality of the chosen `q` imply `q<4(A+1)(A+2)m`. QED.

This result concerns bounded-type irrational rotations and source selection. It composes R36's proven final-source reduction and established continued-fraction facts; it is not a claim of a new three-gap theorem or of native physics.

## Algorithm and bit-cost accounting

Sort `m` historical phases and save owner labels. Traverse sources `j-1,j-2,...`, determine each owner by a binary predecessor search, and record the first source of every owner. Stop on full coverage or complete exhaustion. Use R36's per-arc Floor Sum binary-select if an explicitly chosen scan budget is reached first. If the scan terminates after `S=min(N,H(j))` sources, arithmetic comparison cost is `O(m log m+S log m)`, storage is `O(m)`; after sorted `τ_k` preprocessing, extinction rank query cost is `O(log m)`. The dense fallback costs `O(m log N)` per-arc count queries, plus the bounded scan if used. Exact multiplication, modular division, rational interval comparisons, source index bit size `log j`, parameters and Floor Sum Euclidean bit costs remain part of a full bit-complexity claim.

## Exact experiments

`VERIFY_R37.py` implements suffix scanning, interval owner certificates and a mathematically independent R36-style Floor Sum rank/select whole-window reference. It also runs complete small-window enumeration tests. It uses Python big integers, `Fraction` and `isqrt`; no floating-point quantity decides a result.

| θ | m | j | N | Reverse scan | Strategy | R36 count queries | Grid sufficient q |
|---|---:|---:|---:|---:|---|---:|---:|
| sqrt(2)-1 | 16 | 10^12 | 10^9 | 22 | suffix saturated | 496 | 70 |
| sqrt(2)-1 | 32 | 10^12 | 10^9 | 34 | suffix saturated | 991 | 169 |
| sqrt(2)-1 | 128 | 10^12 | 10^9 | 133 | suffix saturated | 3960 | 408 |
| sqrt(2)-1 | 257 | 10^12 | 10^9 | 471 | suffix saturated | 7949 | 985 |
| Frozen S23/AV θ | 128 | 10^12 | 10^9 | 142 | suffix saturated | 3960 | 553 |
| 1/3 + sqrt(2)/10^7 | 21 | 10^9 | 10^8 | 2000 (3/21 owners) | Floor Sum fallback | 581 | 4714045 |

Every saturated case returns the exact same owner-labelled `τ_k` vector as the independent whole-window Floor Sum oracle at the rational midpoint (0 mismatches); every scanned suffix owner is verified constant over the stated rational interval by the adjacent-boundary floor condition. The sixth case documents when saturation is expensive and dense Floor Sum selection is the better method; its whole-window comparison is at the declared rational midpoint. Finite small-window enumeration confirms empty-owner and short-window semantics. The full owner vectors and exact rational certification data are in `CERTIFICATE_R37.json`.

Frozen S23/AV remains pinned at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The previously certified R36/R32 trillion-horizon 298-run file still has SHA256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`; R37 tests the source-selection primitive at a separate large window and does not assert that its full prediction was rerun.

Tool reuse: composition of the R36 last-survivor histogram, R29 Floor Sum count oracle and standard continued-fraction grid approximation. Checked the current tool registry/inventory and bounded source search; publish this as an auxiliary observer-specific result, pending independent review and any shared-tool admission.

## Next problem

For high-partial-quotient parameters where the bounded suffix lacks most historical owners, develop an exact joint multiple-arc source-select by Ostrowski block decomposition or batched cumulative-count reuse. Compare bit costs with R36 per-arc binary-select, retain owner labels and rational-interval certificates, and test `m=16,32,128,257`, a near-rational family and one independent whole-window reference.
