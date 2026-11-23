# X6 R152 — complete Port-10 middle-`B` bridge-to-tail BRC atlas

Date: 2026-11-24 (Asia/Shanghai). Evidence: author analytic splice of previously established R151/R148 plus fresh exact full-population `Fraction` replay; independent mathematical review **NOT_REVIEWED**. Formal native Result/Review **NOT_SUBMITTED**.

## Scope, immutable input and typed meaning

Scientific inputs remain R121@`8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd` and R122@`0687aa24f5402da3b35f914dd6907967a9805b94`. P000 V5 / ACTIVE Heartbeat World. These are conditional **static centered three-axis slice BRC six-pair observer** calculations, not the complete native X6 six-axis dynamics, full Cell address or an inferred physical residual.

For a nonzero integer triple `v=(x,y,z)` with `q=max(sum positive parts, sum absolute negative parts)<=10`, identify only `v` and `-v` (not integer multiples). Exactly 1,935 unoriented directions. Define
`h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`,
`g=(|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|)`;
`s=(136+B,312,136+D,B+176,B+D,176+D)`;
`F_v=max_i g_i/s_i`, `eta=min_v F_v`, `N={v:2F_v<3eta}`.
All weights positive. R150 already gives a complete six-member support set for `B>=20,D>=528`.

## R152 theorem: exact entire middle-B half-strip

For **every real `20<B<136` and `D>=528`**, use the six directions

```text
A=(1,0,0);   C=(5,-4,1); K=(5,-1,0);
H=(9,-5,1); J=(4,-1,0); E=(6,-4,1).
```

Let
```text
L(B)=1872-B,
T_AC(B)=min(1584+8B,L(B)),
T_K(B)=min(1224+8B,L(B)),
T_H(B)=528+2B      for 20<B<=32,
       =1056+5B    for 32<B<136,
T_in(B)=min(704+3B,832-B),
T_one(B)=2448+17B.
```
Then the **complete** strict `3/2` near-direction set is

```text
N(B,D)=
  ({A,C} if D<T_AC(B) else empty)
  union ({K} if D<T_K(B) else empty)
  union ({H} if D<T_H(B) else empty)
  union ({J} if T_in(B)<D<T_one(B) else empty)
  union ({E} if D>T_in(B) else empty).
```

Every equality in these strict tests excludes the indicated direction. This exact decision formula determines every real point in the entire unbounded middle-`B` half-strip; near-counts 1 through 6 all occur.

**Seam theorem.** At `D=L(B)` the near-set is **exactly `{J,E}`**, and `eta=12/(B+D)=1/156`. When crossing `L(B)` from below, the exact number of directions lost at the seam is:

- `20<B<32`: none (the other directions exited earlier);
- `32<=B<72`: `A,C` simultaneously (two);
- `72<=B<136`: `A,C,K` simultaneously (three).

Thus `B=32` and `B=72` are exact seam multiplicity transitions. This uses **one-sided neighborhoods** below the seam: for any fixed B satisfying the row, sufficiently close D<L(B) gives the indicated additional near members.

## Analytic proof

1. For `528<=D<L(B)`, R151 (author-verified at commit `4ae79914697b8acb12f6f13df71cf696be80033e`) proves all six membership tests on the open bridge region. On that region the explicit `D<L(B)` cap is redundant in the `A,C,K` indicators; the strict `T_AC,T_K` expressions reduce to the exact R151 conditions. For every `20<B<136`, the inequality `1056+5B<1872-B` is equivalent to `B<136`; consequently `H` exits strictly before the seam. Also `T_in(B)<L(B)<T_one(B)`, so J/E are both present sufficiently near the seam.

2. For `D>=L(B)`, R148 (author-verified at commit `444363f2f8bc670c9fbc0d94a52ca165bb6f69a8`) proves directly, from complete integer population coverage, `N={E} union ({J} if D<T_one(B))`, with `eta=F_E=12/(B+D)`. Consequently the candidate indicators of `A,C,K,H` must be false, as their thresholds are at or below L; `E` remains true because `T_in(B)<L(B)`. The piecewise formula therefore agrees on both sides and at equality, with no unclassified gap.

3. To count seam losses, compare `1584+8B` and `1224+8B` against `L=1872-B`. The former is >=L exactly when `B>=32`; the latter is >=L exactly when `B>=72`. Both directions A,C share the former threshold and K has the latter. H exits strictly earlier; J,E continue. At the seam, R148's proof uses the nonzero second-gap lower bound `3/312=1/104` against `(3/2)eta=1/104`, so strict equality correctly removes all those directions.

4. At `D=T_one(B)`, J fails the strict comparison against E, leaving exactly E thereafter (sharp singleton onset), as in R148. The exact J/E entrance and all other walls are already fixed by R151. The full result is obtained by combining complete analytic proofs over two exhaustive adjacent parameter domains, not by extrapolating samples.

## Verification and provenance

Companion self-contained Python `Fraction` verifier: `research_notes/portable_direct/x6_r152_full_bridge_tail_verify.py`. Actual local run 2026-11-24:
```text
R152 FULL MIDDLE BRIDGE-TO-TAIL ATLAS PASS
complete_integer_directions 1935 exact_rational_full_population_cases 404
count_histogram {1: 61, 2: 101, 3: 22, 4: 99, 5: 70, 6: 51}
sharp cuts B=32 and B=72; all equality probes tested
```
The 404 tests independently enumerate all 1,935 directions at each exact rational parameter probe, including boundary equality and both sides of B=32,72 and D=L,T_one. Continuum proof uses R151+R148 analytic arguments and their underlying R150 finite-population certificate.

Dependencies: [R151](https://github.com/awdawmip/enterprise-math/blob/4ae79914697b8acb12f6f13df71cf696be80033e/research_notes/portable_direct/2026-11-24_r2_x6_r151_irredundant_bridge_near_direction_atlas.md), [R148](https://github.com/awdawmip/enterprise-math/blob/444363f2f8bc670c9fbc0d94a52ca165bb6f69a8/research_notes/portable_direct/2026-11-23_r2_x6_r148_all_positive_B_sharp_eventual_singleton_tail.md), R150 six-support.

**Scientific frontier:** this closes the entire `20<B<136,D>=528` membership region. Next substantive question: derive a globally minimized chamber complex for all `B>0,D>0`, especially `D<528`, and determine whether all optimizer witness-change walls are mathematically necessary to describe membership. Review and native Result remain separate.
