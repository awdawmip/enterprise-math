# R206 — Exact depth-one affine minimum and Stirling source-tail fibre bounds

Date: 2026-11-16 (Asia/Shanghai).
Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Dependencies: R195 (field-uniform source-order minimum), R200 (full paired-event joint quotient), R201 (affine upper construction), R204 (nilpotent suffix bound), R205 (source retraction and additive lower bound).
Scope: a typed **selected-source/full-paired-event observation quotient** of the X6 event carrier; native X6 has SIX spatial axes and TWELVE signed directions. No P000 change, full-native-path compression, formal Result, or independent review is asserted.

## Definitions

Fix a finite field `F_q` (q a prime power), m>=1 signed event-direction labels, k>=1 selected provenance labels `1,...,k`, and an additional neutral provenance label `⊥`. The independent full event alphabet has size `a=m(k+1)`. A word's selected-source observation `s(w)` is the list of the selected labels in order of **last occurrence**, with no repeats. Its complete paired tail `t_L(w)` consists of the final `min(L,|w|)` ordered events, including their directions and provenance labels. The finite quotient `J_{m,k,L}` remembers `(s(w),t_L(w))` and multiplies by concatenation. Define `d_orbit(q,m,k,L)` as the minimum dimension of an affine action of the quotient over `F_q` admitting **one separating orbit point**. For L>=1, R205 proves

`d_orbit >= k(k+1)/2 + L ceil(log_q(2m))`

and R201 supplies `d_orbit <= k(k+1)/2 + L ceil(log_q(m(k+1)+1))`.

## R206-A — Exact theorem for tail depth one

**For every finite field F_q, m>=1, k>=1:**

`d_orbit(q,m,k,1) = k(k+1)/2 + ceil(log_q(2m)).`

For k=0, the suffix theorem R204 instead yields `ceil(log_q(m+1))`.

**Proof (lower bound).** Set L=1 in the established R205 additive source-retraction/nilpotent-kernel theorem. It gives `k(k+1)/2 + ceil(log_q(2m))` in every affine action with a separating orbit, even when source and tail coordinates are arbitrarily coupled.

**Proof (attainment).** Put `d_s=k(k+1)/2`, `r=ceil(log_q(2m))`. Take R195's `d_s` source reset coordinates (one singleton per selected source and one pair comparison for each unordered pair), initialized to all ones. They recover `s(w)` after any word and yield an affine action factoring through the source-order quotient. Choose any injection

`c: {0,...,m-1} × {N,S} -> F_q^r`,

where N denotes neutral provenance and S denotes *some selected provenance*. There are precisely `2m` such symbols, so the injection exists. Initialize the r tail coordinates to `c(0,S)`. On an event `(d,ℓ)`, apply the R195 source reset for ℓ (identity if ℓ=⊥) and **constantly reset** the r tail coordinates to `c(d,N)` if ℓ=⊥ or `c(d,S)` otherwise. All these operations are affine over any F_q; in fact each matrix row is identity or zero and each output bias is a field constant.

For any nonempty word, the resulting affine transformation consists of the R195 action for `s(w)` and the constant tail reset `c(direction(last event),N/S)`. Thus its action depends only on `J_{m,k,1}`. Conversely, from the separating orbit state one first reads `s(w)`. From the tail code one reads the final direction and neutral/selected flag. When the flag is S, **the final event provenance equals the final label of s(w)**; hence the full paired final event is recovered. When the flag is N, the provenance is ⊥. The initial empty word is uniquely distinguished: `s=empty`, tail code `c(0,S)`, whereas every nonempty word with empty source order must finish neutral and has code `c(d,N)`. Since the two code classes are disjoint, the initial point is distinct. Therefore the orbit map is injective. The lower bound is attained. QED.

**Exact special case.** `q=2,m=12,k=6,L=1`: source block 21, tail block 5, dimension **26**. R201's general upper construction used 21+7=28; this closes the two-dimensional gap for depth one. The reachable joint observation quotient has `(m+1)+2m(N_k-1)` elements, where `N_k=sum_{j=0}^k k!/(k-j)!`; here `N_6=1957`, so `|J_{12,6,1}|=46957`. The 26-bit optimum concerns **affine transitions**; an unrestricted state number requires only `ceil(log_2 46957)=16` bits.

## R206-B — Stirling/Bell fibre lower bound for all tail depths

Let `{n \brace r}` denote the Stirling number of the second kind. Define

`C_{k,L} = sum_{j=0}^{min(k,L)} {L+1 \brace j+1}`.

**Theorem.** For `m,k,L>=1` and every finite field F_q,

`d_orbit(q,m,k,L) >= k(k+1)/2 + max( L ceil(log_q(2m)), ceil(log_q(m^L C_{k,L})) )`.

**Exact fibre lemma.** Fix a source order `s` containing all k selected sources. There are exactly `m^L C_{k,L}` different *length-L complete paired tails* which can occur jointly with this final source order.

**Proof of fibre lemma.** In any possible length-L provenance suffix, take the j distinct selected labels that occur. Their last-occurrence order in the suffix must be the final j labels of s, in that order; the remaining prefix selected labels lie before all of them. Conversely, any suffix using exactly these j labels in that relative last-occurrence order, with neutral labels placed arbitrarily, can be preceded by a source-order prefix to realize s. For fixed j and a prescribed last-occurrence order, the number of words of length L over these j labels plus the neutral symbol, containing every selected label, is

`1/j! * sum_{i=0}^j (-1)^i binom(j,i)(j+1-i)^L = {L+1 \brace j+1}`.

The numerator counts all words in which each selected label occurs; permutation symmetry partitions them equally among j! last-occurrence orders. The right-hand identity is the standard Stirling inclusion-exclusion identity. Summing over all possible j yields C. Each of L event positions has m independent direction choices, giving the factor `m^L`. QED.

**Proof of lower bound.** In R205's affine-span argument, appending a fixed neutral event z repeatedly L times gives an idempotent retraction E and a linear projection P with `U=im(P)`, `K=ker(P)`; `dim(U)>=k(k+1)/2` by R195. Every orbit point from the fibre just counted has the same source order, so E maps all of them to **one point**. Their pairwise differences therefore lie in K. Since the separating orbit contains `m^L C_{k,L}` distinct points in this affine fibre and `|K|=q^{dim K}`, necessarily `dim K>=ceil(log_q(m^L C_{k,L}))`. R205 independently yields `dim K>=L ceil(log_q(2m))` from nilpotence of `M|K`. Add the source dimension. QED.

For k>=L, `C_{k,L}` is exactly the Bell number `B_{L+1}`. On the original `q=2,m=12,k=6` parameters: the fibre sizes for L=1,2,3,4,5,6 are respectively `24,720,25920,1078272,50512896,2618707968`. Their kernel dimension lower bounds are `5,10,15,21,26,32`, compared with R205's `5,10,15,20,25,30`. Hence the total minima obey `d_orbit(2,12,6,4)>=42` and `d_orbit(2,12,6,6)>=53`. The L=2 bound remains `31<=d_orbit<=35`.

## Boundary and counterexample for naive longer-tail reuse

The depth-one shortcut cannot simply record a neutral/selected bit per tail position at depth two: set k=2,m=1, one fixed direction. Histories `[1,2,2]` and `[2,1,2]` have identical final source order `[1,2]` and tail flag string `SS`, but their **full paired last-two-source tails** are `[2,2]` and `[1,2]`. The R200 observation distinguishes them. A valid deeper-tail construction must preserve this distinction.

## Reproducible exact evidence and outstanding questions

Execute `node research_notes/portable_direct/R206_exact_depth_one_affine_check.mjs` to reproduce `R206_verification.json`. It checks all depth-one orbit states and exact generators/compositions for 27 small models `q in {2,3,4}, m=1..3, k=1..3`; the F4 labels represent arbitrary field elements and only constant/identity coordinate operations occur. It also checks all 46,957 orbit states for `q=2,m=12,k=6`, a deterministic subset of event transitions/compositions, and exhaustively checks 20 source-tag fibre models `k=1..4,L=1..5`. Exact arithmetic is integer-digit and BigInt, with no floating-point acceptance criterion. General theorems rely on the proofs above.

Scientific inputs remain frozen. The chosen quotient remains a declared observer; original X6 path/Cell semantics, BRC physical affine action, port/branch identities, signed quantities, exact rational weights and multiplicities stay in their separate native carrier. No native `enterprise_math.brc_transport.EffectHistogram` integration was executed.

**Next exact open unit:** Determine 31–34-dimensional feasibility for `q=2,m=12,k=6,L=2` using mixed source/finite-memory generator relations or a valid lower-dimensional construction; independently execute the existing R201 native BRC integration probe and R203 mixed-moment tests under a pinned installed version. Retain independent mathematical review as NOT_REVIEWED.
