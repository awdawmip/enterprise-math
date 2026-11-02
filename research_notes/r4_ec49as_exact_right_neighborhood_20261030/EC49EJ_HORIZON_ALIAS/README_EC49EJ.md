# EC49EJ — Complete cross-horizon alias classification for the native-X6 equal-positive-count BRC observer

**Date:** 2026-11-02. **Parent:** EC49EI (and EC49EH), original author-side Draft PR #1730. **Status:** `AUTHOR_ANALYTIC_PROOF / TWO_EXACT_CHECKS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Frozen scientific sources carried forward:** GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral rules were read separately from canonical main, global `8916715838c5cf6433a62b7890f476f8ba46a04e` and EM `1656181794935bb191381ba4b51a7941e80ffdca`. P000, ACTIVE Heartbeat World and existing scientific task inputs are unchanged.

## Exact native model and question

The seven *ordered signed-X6* operation words are `a=(-E1,-E1)`, `b=(-E2,-E2)`, `c=(+E1,+E2,-E1,-E2)`, `d=(+E2,+E1,-E2,-E1)`, `e=(+E3,+E1,+E1,-E3)`, `f=(+E1,-E1)`, `g=(+E2,-E2)`. Historical chart-relative displacement is `-2E1`, so a returning future operation word has net displacement `+2E1`. The operation horizon `h` counts letters a–g; native path length `L` counts individual signed six-axis primitives. For every word `w`, retain its positive native-step vector `p(w)`, two strictly-positive multiplicative BRC factors `X(w)=product_i x_i^p_i(w)`, `Y(w)=product_i y_i^p_i(w)`, its original ordered primitives and its five-bucket first-A/B seam observer on the nine EC49EI historical atoms.

**Question:** For a prescribed six-axis positive-count vector `p`, at which *operation horizons* can a returning future word exist? What information can and cannot be cached by its positive BRC factor?

## Theorem (all integer count fibers, all strictly positive real BRC instruments)

Fix integers `e>=1`, `p1>=2e`, `p2>=0`, and `p=(p1,p2,e,0,0,0)`. Put `m=min(p1-2e,p2)`. The set of **all and only** valid returning operation horizons compatible with this exact p is

```
H(p)={p1+p2-1-r : r=0,1,...,m}.
```

It contains exactly `m+1` consecutive integers. Every such word has the **same** native signed primitive-step length

```
L(p)=2(p1+p2+e)-2,
```

and the **same** exact positive-BRC future multipliers

```
X_p=x1^p1*x2^p2*x3^e,     Y_p=y1^p1*y2^p2*y3^e
```

for arbitrary strictly positive real x,y on all six axes.

If `m>=1`, every supported horizon has full nine-atom future observation rank 9. At the **longest** horizon `h_max=p1+p2-1` (equivalently `r=0`), exactly **two** distinct returning operation words are necessary and sufficient for rank 9. At each of the `m` **shorter** horizons (`r>=1`), exactly **four** distinct words are necessary and sufficient. For `m=0`, only the longest horizon exists; its exact nine-row rank is `5+2[p1>2e]+2[p2>0]`.

In the explicitly defined **independent-per-word native-step billing model** (no sharing between any two words or horizons), computing all `m+1` full-rank horizons of one multi-horizon fiber requires exactly

```
(2+4m)*L(p)=(4m+2)*(2(p1+p2+e)-2)
```

primitive invocations. This is a separate baseline from the cross-word/cross-horizon prefix-trie optimum `U_eq(H)`.

## Proof

Let `n_a,...,n_g` be nonnegative letter multiplicities in a valid returning operation word. Native displacement gives `n_b=0`, `n_e=n_a+1`; write `n_e=e` and `r=n_c+n_d`. Positive primitive counts are `p1=2e+r+n_f`, `p2=r+n_g`, `p3=e`. Thus `n_a=e-1`, `n_f=p1-2e-r`, `n_g=p2-r`. Nonnegativity yields exactly `0<=r<=m` and the operation horizon is `h=2e-1+r+n_f+n_g=p1+p2-r-1`. Conversely each such r is realized by a word with `r` c's, `e-1` a's, `e` e's, `n_f` f's and `n_g` g's. All carry native return `+2E1`, so the characterization is necessary and sufficient.

At a return, negative step counts are `p1-2,p2,e` on axes 1–3. Summing positive and negative counts gives `L=2(p1+p2+e)-2`. Multiplicativity of the two exact positive-BRC instruments gives the displayed monomials; this result is independent of how the path is segmented into a–g operations.

For `r=0` and `m>=1`, both `n_f` and `n_g` are positive. The word starting with f and the word starting with g (with all other letters following) realize the two EC49EI seam types F/G; their nine historical-atom terminal indicator columns have an integer unimodular 9-by-9 minor, and no single word gives more than five bucket columns. Thus the minimum is two. For `r>=1`, each equal-p fiber realizes the four event types `ce,ec,de,ed` by placing either c/d or e first, taking the remaining event letters all c or all d and appending the remaining a/e/f/g letters. The four left-kernel row-pair witnesses and the nonzero unimodular minor in [EC49EI](../EC49EI_FIBER_RANK_DICHOTOMY/README_EC49EI.md) prove their joint rank 9 and individual necessity. The rank theorem is used at its exact nine-atom observer/future-operation scope. Finally, each chosen word in a fixed fiber consumes exactly L native primitive steps, so multiplying L by the exact 2/4 word minima proves the independent-billing identity.

## Unbounded constructive alias and decisive exact example

For **every** `m>=1`, choose `e=1`, `p=(m+2,m,1,0,0,0)`. Then exactly `m+1` different operation horizons `m+1,m+2,...,2m+1` share one p, one pair of formal BRC monomials and the same native length `4m+4`. All these horizons individually recover full rank 9. In particular, at m=1:

| Horizon | Full-rank words | Native steps per word | Positive vector | X for x=(2,3,5,7,11,13) | Y for y=(3,4,7,11,13,17) |
|---|---|---:|---|---:|---:|
| h=2 | `ce,ec,de,ed` | 8 | `(3,1,1,0,0,0)` | 120 | 756 |
| h=3 | `feg,gef` | 8 | `(3,1,1,0,0,0)` | 120 | 756 |

Therefore, **even full positive counts together with both positive-BRC monomials and the exact native primitive length do not identify the operation horizon**. A cache indexed solely by p can safely reuse the positive-weight multiplier calculation, while the operation horizon, actual native word identities, prefix-trie provenance and nine-atom terminal observation remain separate typed keys. The many-to-one map is unbounded in the number of compatible horizons.

## Executed exact checks / proof boundaries

Two independently written standard-library implementations were actually executed: `VERIFY_EC49EJ.py` (Python `fractions.Fraction` exact rational rank) and `VERIFY_EC49EJ.js` (V8 GF(2) rank with exact native signed-X6 and BigInt BRC monomials). Both return PASS on all 273 fiber-horizon pairs for `1<=e<=3`, `0<=p1-2e<=5`, `0<=p2<=5`: rank distribution 5/7/9 equals 3/30/240; 75 different fibers permit multiple horizons. Both also check the unbounded family's first eight m, with exact native length and full rank at every supported h. A rational/BigInt rank-9 certificate is exact because rank over GF(2) equal to 9 implies rank over Q equal to 9. The all-integer/all-real theorem follows from the algebra and EC49EI's exact transfer classification; finite tests are an independent scoped audit.

The BRC arithmetic here uses **the actual typed positive-weight path-multiplication interface** with ordered signed-X6 source; no signed/phase cancellation or physical time inference is made. The horizon is operation-word length, while the native six-axis ordered path is retained. Native project research authority remains separate from author-side GitHub storage.

## Research status / next

GitHub identity `awdawmip` can write the project repository. At this run, native Enterprise Math gateway 0.6.11 returned `research_authority_granted=false`, a session-start denial `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`, and owner inventory `CONTROL_QUOTA`; active authenticated owner was not established. No native CLAIM, Result, independent Driver review or Foundation admission is asserted. Source pins, P000 and ACTIVE worldview are unchanged.

**EC49EK:** use the exact 2/4-type fiber theorem to optimize `U_eq(7)` and then `U_eq(8)` with a finite prefix-edge MILP or a direct type-trie lower-bound certificate; determine whether the proposed `min(8H+12,4H+30)` remains sharp. Exploit the horizon-collision classification to share only BRC monomial evaluation, retaining provenance for trie and seam readout; separately count edge, positive-monomial and observer-column costs.
