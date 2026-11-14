# EC49EV — Seven-window three-BRC-key, six-observer exact native-X6 prefix optimum

**Research date:** 2026-11-03 (Asia/Shanghai). **Parent:** exact native-six-axis BRC/resource model in EC49EU (`e2424cb9ad15e4761140a9e647997acb9d8516e0`), Draft PR #1730. **Status:** `AUTHOR_FINITE_EXHAUSTIVE_PROOF / EXACT_INTEGER_DP_PASS / INDEPENDENT_NODE_PASS / OPTIMAL_WITNESS_MILP_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Immutable scientific input pins (inherited, not refreshed):** Global Knowledge `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current applicable behavioral rules were separately read at Global canonical `main@7cd91a99d0ede0dcef074ee17ad9243271df9253` and Enterprise Math canonical `main@96946f1cc55a4c0f135a5d2100751fe722b384ba`. P000 and ACTIVE worldview unchanged.

## 1. Statement and domain

The finite native-X6 model uses the ordered primitive signed-axis codes

```
a=(-1,-1)  b=(-2,-2)  c=(+1,+2,-1,-2)  d=(+2,+1,-2,-1)
e=(+3,+1,+1,-3)  f=(+1,-1)  g=(+2,-2)
```

Each code acts in the first three of the six native spatial axes, with axes four through six retained as zero components. The nine specified historical seam states and five observation buckets `N,A,B,AB,BA` are as in the inherited EC49EU model. A returning word of length `h` has total signed displacement `(+2,0,0,0,0,0)`. For every `h=2,3,4,5,6,7`, select at least one returning ordered word, all words in that horizon sharing the same **complete six-axis positive-step count** `p_h`. The five-bucket observations over the nine history states, stacked across selected words for that horizon, must have rational rank 9. Ordered primitive words and branch provenance are retained.

Let `E` count the nonempty signed *native primitive prefix edges* in the union of selected words, `M` the number of distinct `p_h` vectors (keys for the symbolic strictly positive two-channel BRC factors `X_p=∏x_i^{p_i}`, `Y_p=∏y_i^{p_i}`), and `S` the number of distinct five-bucket history-to-output transfer signatures globally. In this **entire finite seven-operation model**, the exact optimum is

\[
\boxed{\min\{E:\;H=7,\ M=3,\ S\le 6\}=86.}
\]

The optimum also occurs with `S=6` exactly, so `min(E | H=7,M=3,S=6)=86`.

## 2. Exhaustive finite observer-reduction lemma

The unique rank-nine horizon-two positive key is `p0=(3,1,1,0,0,0)`. Its four necessary words `ce,de,ec,ed` have four distinct transfer signatures `T4`, and consume precisely 28 primitive prefix edges. The two no-event words `feg,gef` form two other signatures `T2` and together give full observation rank 9. All possible returning words across horizons two through seven have a union of exactly 11 distinct transfer signatures, including the forced four T4 signatures. Consequently any solution with global `S<=6` must choose at most two of the seven signatures outside T4. It is sufficient to consider the 21 pairs of extras: allowing an unused extra only enlarges admissible choices, which preserves lower bounds and includes every feasible construction.

The independent seven-letter-language enumeration enumerates *all* returning ordered operation words, counts exactly `8,51,304,1770,10224,58947` by horizon, and checks every fixed-positive-key transfer family. For **20 of the 21 extra pairs**, every rank-nine fixed-positive-key horizon must contain all four T4 signatures. Under exactly three distinct positive keys, these are the three all-T4 schedules already solved by EC49EU with exact costs 116,116,128. For the unique pair of extra signatures `T2`, every rank-nine fixed-key horizon requires either the complete four T4 signatures or the complete two T2 signatures. This alternative is exact for the declared finite domain, not an observer equivalence assumption.

For reproducible coverage, all positive-count fibers are enumerated without pruning token orders. If `e=#e`, `a=#a`, `r=#c+#d`, `f=#f`, `g=#g`, then native return and total length imply `a=e-1`, `r=p1+p2-h-1`, `f=p1-r-2e`, `g=p2-r`, with nonnegative counts; `b=0`, `e>=1`, and positive components 4–6 are zero. Enumerate the nonnegative possibilities, every `c/d` split, and all operation multiset permutations. Under `S<=6` and `M=3`, the unique T2-extra pair admits exactly **465** distinct horizon-key schedules (including the three all-T4 cases). The other 20 extra pairs each admit the same three all-T4 schedules. The independent Node.js checker enumerates the unfiltered full `7^h` language instead of depending on this fiber generator and reproduces the counts and rank classification.

Rational rank is checked using an exact finite prime `q=1000003`. Every signature produces a 5-by-9 binary observation matrix. Any 9-by-9 0/1 minor is bounded in absolute value by Hadamard's inequality `3^9=19683<q`; hence rank nine modulo q is **equivalent** to rank nine over the rationals for the matrices in this model. Rank of lower-dimensional unions is determined by exact modular Gaussian elimination; this establishes the stated full-rank criterion without a floating-point tolerance.

## 3. Exact global minimum by native-prefix integer dynamic programming

For each of 465 schedules, include every complete eligible ordered word at each horizon whose signature is one of that horizon's required two or four types. Insert the **full ordered signed primitive step sequences** into a rooted trie (not a token-prefix trie). Each horizon/type pair is one required terminal color. A terminal may cover more than one eligible label. The four horizon-two base words are pre-paid, with 28 native prefix edges. For every trie node v and subset b of required colors define D_v[b] as the least number of *new* prefix edges in v's subtree whose selected terminals cover b. Set D_v[0]=0 and D_v[1<<color]=0 for every eligible terminal, and merge each child u by

\[
D_v^{new}[b\lor c]\gets \min(D_v^{new}[b\lor c],D_v[b]+D_u[c]+{\bf1}_{c\ne0}{\bf1}_{(v,u)\text{ not previously paid}}).
\]

Each child selected incurs its entering edge precisely once, and OR aggregates shared terminal colors. Induction on the finite rooted trie proves this recurrence gives the exact minimum over **all** eligible terminal word sets. The integer C++17 kernel `VERIFY_EC49EU_EXACT_DP.cpp` from the immutable predecessor is reused (original Git blob `d08c90554d205730ce6a36e89a59754e28f36902`); the frozen Python operation model also reuses its original Git blob `bcad085da0655d41753c166fd993cdb35e4d4815`. Source identity was checked against GitHub immutable content.

All **462** schedules using a T2 horizon were actually solved with the integer trie DP; the remaining three all-T4 schedules reuse the previously published and verified exact three-case predecessor report (Git blob `ccdaddc3d0b2fc0cebba641bb2cec95ac8b1f919`, costs 116,116,128). The full 465-case exact report `EC49EV_EXACT_EXECUTED.json.gz.b64` is losslessly compressed base64 JSON. The complete tally has a **unique optimum, schedule #46, at E=86**; second-lowest cost 88. The optimal trie has 3,149 nodes, 14 terminal colors, 16,384 maximum live color masks and 376,624 integer state-pair convolutions. The optimum adds exactly 58 edges to the 28 baseline edges, giving 86. The complete schedule report and original integer result can be regenerated with `VERIFY_EC49EV_ALL.py` and the referenced predecessor model/kernel in a Python 3+C++17 environment. One fast preliminary `--quick` run was separately executed; the complete report was produced by completed exact integer DP runs resumed across two bounded executions, never by extrapolation from the quick run.

## 4. Exact attaining native paths

A separately constructed and checked **86-edge** witness is:

| h | selected ordered operation words | shared positive BRC key p_h | transfer types |
|---:|---|---|---:|
| 2 | `ce, de, ec, ed` | `(3,1,1,0,0,0)` | 4 |
| 3 | `feg, gfe` | `(3,1,1,0,0,0)` | 2 |
| 4 | `degf, fegc, fegd, gfec` | `(4,2,1,0,0,0)` | 4 |
| 5 | `fegfg, gfefg` | `(4,2,1,0,0,0)` | 2 |
| 6 | `degffg, fegcgf, fegfgd, gfefgc` | `(5,3,1,0,0,0)` | 4 |
| 7 | `fegfggf, gfefgfg` | `(5,3,1,0,0,0)` | 2 |

The independent Node.js program expands every actual native signed axis step, checks six-axis return displacement, full six-positive-count equality, rational-equivalent rank nine at each horizon, exactly three globally distinct BRC keys, six distinct transfer matrices, and 86 distinct raw primitive prefix edges. The independent SciPy/HiGHS 0–1 MILP also solves the winning schedule directly: objective 86, dual bound 86, gap 0, with its own attaining word set recorded in `EC49EV_WITNESS_MILP.json`.

## 5. Verification and status

- `VERIFY_EC49EV_ALL.py`: exact fully specified enumerator and trie DP replay, including all 21 global observer-pair possibilities and the 465 surviving key schedules; original full output preserved in compressed execution report.
- `VERIFY_EC49EV_INDEPENDENT.js`: separate native seven-operation brute-force and rank implementation; actually executed with Node.js and returned `PASS`, including full enumerated word populations and witness triplet `(86,3,6)`.
- `EC49EV_WITNESS_MILP.json`: independently executed SciPy/HiGHS optimum for winning native trie (status 0, optimality gap 0); executable integer OR-mask trie supplies the **finite exact proof**.
- `EC49EV_SUMMARY.json`: finite coverage, best schedule, evidence pointers and hashes.

The model is the inherited restricted native-X6 signed-path observer, embedded in all six spatial axes, and strictly positive symbolic two-channel BRC key semantics. The result measures three precisely defined resources; extension to other future operation languages, full native Heartbeat dynamics, numerical BRC precision or physical observables requires a typed bridge if used. Formal Research Activity/CLAIM/Result/Driver review remains governed by the native service.

## 6. Next useful question

EC49EW: determine the seven-window `M=4,S=4` and `M=4,S=6` resource strata, using the 21-signature-pair reduction, exact native-prefix DP and improved lower-bound pruning. The new 86-edge point gives a useful anchor to test whether four BRC keys reduce native cost toward the unrestricted 58-edge lower bound, and how many transfer matrices this requires. Continue constructing actual native paths even where exhaustive classification is expensive.
