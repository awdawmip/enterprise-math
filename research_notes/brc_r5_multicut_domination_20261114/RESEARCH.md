# R5: exact all-pattern domination profile for closing any subset of 28 gaps

Date: 2026-11-14. Status: author-side theorem, locally executed exact finite calculation; no formal Result or independent mathematical review claimed.

Scientific input pinned, unchanged: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Derived auxiliary integer-event sampling observer only; the native Heartbeat-World X6 foundations and the separate 2,520-byte certificate / 28-coordinate / 8,192-query end-to-end workload are not modified or evaluated.

## Mathematical definitions

Let `X=(x_0<...<x_953)` be the 954 event-boundary integer coordinates regenerated from the original 15 frozen integer atoms (953 rational activation thresholds, 1,065 total activations). At radius `R=2`, an admissible center belongs to `X` and every point must be within distance 2 of at least one chosen center. Let `D_2(X)` be the smallest possible number of centers. The original sequence has 28 gaps of exactly 3 and consequently 29 blocks `B_0,...,B_28`, separated by these 28 gaps.

For each subset `C ⊆ {0,...,27}`, close precisely those gaps by translating the suffix after each selected gap left by one. The resulting strictly increasing sequence is `X_C` and its domination number is `D(C)=D_2(X_C)`.

## Theorems

**Block-run factorization.** For each maximal run of consecutive closed gaps `a,a+1,...,b-1`, the corresponding consecutive original blocks `B_a,...,B_b` constitute an independent merged component after one-unit translation per interior gap. The unclosed length-three gaps still exceed the coverage radius, and no selected center can cover across them. Thus for the unique partition of block indices into intervals `[a_1,b_1],...,[a_s,b_s]` determined by `C`,

`D(C)=Σ_{h=1}^s d(a_h,b_h)`,

where `d(a,b)` is the exact radius-two domination number on the concatenation of `B_a,...,B_b` after lowering all its interior gaps. Conversely each partition of the 29 blocks into `s` consecutive segments determines one and only one closure set with `q=29-s` selected cuts. This preserves the full set of 28 Boolean closure decisions, rather than assuming pairwise additivity or discarding joint interactions.

**Exact greedy domination lemma.** For any finite strictly increasing integer coordinate sequence and a positive radius `R`, to cover the leftmost uncovered coordinate `z_i`, choose the rightmost available center candidate not exceeding `z_i+R`; discard every coordinate covered up to center+`R`, and repeat. This yields the minimum possible cardinality. Exchange proof: any feasible solution must have a center covering `z_i`; replacing its first relevant center by the rightmost eligible candidate cannot lose coverage of any not-yet-covered point at or to the right of `z_i` and cannot reduce the right endpoint of coverage. Induct on the remaining uncovered suffix.

**Exact dynamic-programming enumeration of 2^28 closure patterns.** Let `F(i,s)` be the minimum total dominating centers over all partitions of the first `i` blocks into `s` nonempty consecutive runs, and `G(i,s)` the maximum. Set `F(0,0)=G(0,0)=0`. Then

`F(i,s)=min_{s-1 ≤ j < i} (F(j,s-1)+d(j,i-1))`,

`G(i,s)=max_{s-1 ≤ j < i} (G(j,s-1)+d(j,i-1))`.

For each extremum, sum predecessor counts across all achieving `j`. Every closure pattern has a unique last run, so the recurrences count distinct bit patterns exactly once, including tie cases. Backtracking returns a constructive cut-set witness. Only 435 interval costs `d(a,b)` and polynomially many DP states are required to determine all 29 extrema profiles across the `2^28 = 268,435,456` patterns.

## Frozen R5 conclusions

The all-closed instance and the best 11-closure instance both have `D=207`, whereas the unmodified baseline has `D=213`. Exactly **11** selected closures are sufficient to attain the full possible six-center reduction; no choice of ten or fewer closures attains 207. There are exactly **two** optimal 11-closure patterns:

- `[2,3,4,6,9,12,13,16,25,26,27]`
- `[2,3,4,6,8,12,13,16,25,26,27]`

At exactly `q=11` closures, `min D=207`, achieved by two patterns, and `max D=213`, achieved by 782,145 patterns. At `q=28`, every gap is closed and `D=207`. At `q=0` it is 213. The complete q=0,...,28 profile, extremizer counts and one minimizing witness per q are in `EXACT_MULTI_CUT_OUTPUT.json`.

### Pairwise interactions

Among the `C(28,2)=378` two-gap closure sets, 375 obey the naive independent-effect formula `D({c,d})=D({c})+D({d})-D(∅)`. Exactly three adjacent pairs violate it:

| Closed gaps | Independent prediction | Actual | Interpretation |
|---|---:|---:|---|
| (5,6) | 211 | 212 | mutually overlapping improvement |
| (8,9) | 211 | 212 | mutually overlapping improvement |
| (12,13) | 213 | 212 | improvement emerges only jointly |

The complete two-closure histogram is `{211:8,212:118,213:252}`. For nonadjacent cuts the merged block-run components are disjoint, so additivity follows from the factorization theorem; the 27 adjacent pairs were computed directly. This is a concrete higher-order joint-observer phenomenon within the stated one-dimensional derived model.

## Exact reproducibility and coverage

The supplied standard-library Python verifier reconstructs all 15-atom subset events with `fractions.Fraction`, checks the original 953/954/1065 quantities and 28 cuts, computes all 435 interval costs and both complete dynamic-programming extrema/counts, checks every reported minimizing and maximizing witness, and directly enumerates all `q=0,1,2,3,4` closure sets. These contain **24,158** distinct bit patterns. It also independently brute-force checks the greedy covering lemma on **968** strictly increasing test sequences of length at most 8, each compared against every feasible center cardinality until the minimum is found. Exact integer operations are used for cover decisions and counts; rational arithmetic is confined to the exact activation-threshold reconstruction.

The local program returned `PASS_EXACT_MULTI_CUT_DOMINATION`. It establishes finite computational conclusions for precisely the frozen R5 auxiliary observer, while the generic factorization, greedy, and DP recurrences have the mathematical proofs above. Full independent review, remote published-source exact-byte rerun and the native 28-coordinate workload remain separate pending units.

## Next scientific unit

Determine whether a compact dynamic-programming witness grammar can recover the actual minimum-cardinality centers for every one of the 268,435,456 closure patterns, while preserving signed event/provenance information for the future full certificate observer. Separately evaluate joint closure effects on the entire fixed-K nearest-center correction cost frontier (not only on minimum feasible center count) and pursue the previously defined 2,520-byte/8,192-query end-to-end experiment.
