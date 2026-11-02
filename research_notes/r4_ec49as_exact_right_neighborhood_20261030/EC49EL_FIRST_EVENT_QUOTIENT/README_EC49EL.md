# EC49EL — Native X6 first-event quotient, all-horizon BRC fiber observability, and sharp q=0 prefix cost

**Research date:** 2026-11-02. **Branch lineage:** EC49EK in Draft PR #1730. **Research status:** `AUTHOR_ANALYTIC_THEOREM / EXACT_DP_CHECK_PASS / DIRECT_NATIVE_FINITE_REGRESSION_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

## 1. Frozen model and question

Keep the scientific grammar of EC49EK, at immutable predecessor `caa970c88315d55d1b1669589ef096a83c7d059b`:

```
a=(-E1,-E1), b=(-E2,-E2),
c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1),
e=(+E3,+E1,+E1,-E3), f=(+E1,-E1), g=(+E2,-E2).
```

Words of exactly `h` operations return displacement `+2E1`, so `#b=0` and `#e=#a+1`. The nine actual seam history atoms are `N0,N1,N2,A0,A2,B0,B1,AB0,BA0`; their terminal first-A/B buckets are `N,A,B,AB,BA`. A occurs at adjacent `(+E1,+E2)`; B occurs at `(+E2,+E1)`. Two independently weighted positive BRC factors are monomials indexed by the complete six-axis positive-native-step count `p`; distinct ordered words remain distinct observation carriers.

Write `r=#a`, `q=#c+#d`, `u=#f`, `v=#g`, so `#e=r+1`, `h=2r+1+q+u+v`. Then every such word has

```
p=(2r+2+q+u, q+v, r+1, 0,0,0),
L_native=2h+2r+2q+2.
```

Given `(h,p)` the four multiplicities are uniquely recovered:

```
r=p3-1, q=p1+p2-h-1, u=h-p2-2r-1, v=h+1-p1.
```

A fiber exists exactly when these integers are all nonnegative and the displayed identity for h holds.

## 2. New all-horizon first-event quotient theorem

**Theorem A (native primitive-path exact quotient).** For every nonempty finite operation word `w` in the above grammar, its complete nine-history terminal A/B transfer signature depends only on:

1. the first operation's leading signed direction class `tau`: `1` for `c,f` (initial `+E1`), `2` for `d,g` (initial `+E2`), or `0` for `a,e`;
2. the ordered A/B first-occurrence reduction of the word's `c,d` subsequence, taking one of `N,A,B,AB,BA`.

**Proof.** Each operation ends with a negative primitive direction. Thus no new positive-positive adjacent A/B event crosses a boundary between two operations. Internally `c` gives exactly A, `d` gives exactly B, and `a,e,f,g` give neither. The only possible history-to-future event is across the *initial* seam: if the first operation starts `+E1`, history last `+E2` yields B; if it starts `+E2`, history last `+E1` yields A. Apply this seam event followed by the reduced `c,d` event sequence to each of the nine specified historical states. All terminal buckets agree exactly. QED.

The quotient is used **only** for the declared nine-atom terminal observer. Full word order and the native prefix tree remain present in the execution-cost problem.

## 3. New all-horizon fiber-rank and counting theorem

**Theorem B (exact all-h classification).** Fix `h>=1` and any realizable positive-count fiber `(h,p)`, with recovered `(r,q,u,v)` as above. Its nine-row terminal observation span over Q is full rank **if and only if**

```
q >= 1 OR (q == 0 AND u >= 1 AND v >= 1).
```

When `q=0`, the rank is exactly 9 if `u,v>=1`, exactly 7 if one is zero and the other positive, and exactly 5 if both are zero.

**Proof.** If `q=0`, the internal A/B event string is empty. Every word's transfer is one of the three initial seam classes. At least one `e` allows neutral first; first `f` is available precisely for `u>0`; first `g` precisely for `v>0`. The rank of the neutral class is 5; neutral plus either single nonneutral class has rank 7; the `f` and `g` classes have a 9x9 zero-one minor of determinant `-1` (explicit omitted-column 0 certificate, source `VERIFY_EC49EL.py`). Thus the q=0 cases follow.

If `q>=1`, use four words with the common multiplicities `(r,r+1,q,u,v)`:

```
C = c e^(r+1) a^r f^u g^v c^(q-1)
D = d e^(r+1) a^r f^u g^v d^(q-1)
E_C = e^(r+1) a^r f^u g^v c^q
E_D = e^(r+1) a^r f^u g^v d^q.
```

They yield quotient types `(tau,event)=(1,A),(2,B),(0,A),(0,B)`. Nine explicit terminal columns indexed `[1,3,4,7,8,11,13,17,18]` among the four blocks of five give integer determinant **`-1`**. All four words remain in the same `(h,p)` fiber, so rank 9 follows. QED.

**Theorem C (exact fiber multiplicities).** For each realizable `(h,p)`:

```
N(h,p) = h! 2^q / (r! (r+1)! q! u! v!).
```

The factor `2^q` assigns each zero-displacement c/d operation its two possibilities; the multinomial coefficient permutes the resulting operation multiset. The total number of return words and positive fibers are therefore

```
N(h) = sum_{r=0..floor((h-1)/2)} h! 4^(h-2r-1) / (r!(r+1)!(h-2r-1)!),
F(h) = sum_{r=0..floor((h-1)/2)} (h-2r)(h-2r+1)/2.
```

Precisely **h** positive-count fibers are rank deficient: they are the `q=0` boundary choices `u=0` or `v=0`, with the doubly-zero endpoint counted once. Consequently, for **every integer h>=1**, the number of full-rank fibers is **`F(h)-h`**. QED.

**Specialization h=9:** `N(9)=1,964,862`; `F(9)=95`; **86** fibers have full rank. There are 25 q=0 fibers, 16 of which have full rank. **Specialization h=10:** `N(10)=11,374,000`; `F(10)=125`; **115** full-rank fibers.

## 4. New sharp cost refinement for every q=0 full-rank fiber

**Theorem D (fixed-fiber native-prefix optimum).** Start from the compulsory h=2 prefix tree `ce,de,ec,ed` of exactly 28 native primitive edges. For any `h>=3` and any full-rank `q=0` positive-count fiber with `r>=0,u>=1,v>=1`, the **minimum additional native primitive-prefix edge count** to recover all nine history directions at exactly horizon h is

```
Delta_q0(h,r)=4h+4r+2.
```

**Proof.** All such words have native length `L=2h+2r+2`. Full rank requires a word beginning `f` (leading native `+E1,-E1`) and a word beginning `g` (leading `+E2,-E2`), since the remaining neutral-first words supply rank at most 7 with either of these alone. Both paths have distinct leading edges. Each shares with the existing h=2 tree precisely its first primitive edge, because the h=2 tree's `+E1` branch continues to `+E2` whereas its `+E2` branch continues to `+E1`. Every other edge of these two required native paths is new. Hence at least `2(L-1)=4h+4r+2` additional edges are necessary. Choose one f-first and one g-first word with the prescribed operation multiset; they have rank 9 by Theorem B and exactly the stated additional edge count. QED.

At h=9, the best q=0 fiber has r=0 and adds **38** edges to the compulsory 28, producing **66** total. The nested q=0 schedule from EC49EK realizes 66 across all intermediate horizons. The unrestricted `U_eq(9)` also admits `q>=1` fibers, whose sharp prefix cost is the next research problem.

## 5. Executed exact validation

`VERIFY_EC49EL.py` is a self-contained standard-library checker. It directly replays **12,358** genuine signed-primitive native return words for h=1..6 with an independently programmed seam simulator; it checks the quotient on every word and matches exact grouped counts. Its dynamic program uses exact integer multiplicities and the proved quotient, rather than storing millions of full paths. It verifies all fiber word counts, rank types, q=0 classification and the closed formulas for h=1..10, reaching 4,758 aggregate states at h=9 and 7,005 at h=10.

The checker additionally compares every fiber's `(word_count,transfer_type_count,max_rank)` at h=7 and h=8 against the actual published EC49EK full reports (50 and 70 fibers), and checks the new q=0 edge formula against all 9+12 eligible prior exact tree-DP fibers. It computes both displayed `-1` minors by exact integer Bareiss elimination. Actual run: `PASS`; JSON report `EC49EL_EXECUTED.json`. It is reproducible with:

```
python VERIFY_EC49EL.py 10 ../EC49EK_EXACT_H7_H8_PREFIX_DP/EC49EK_EXECUTED.json ../EC49EK_EXACT_H7_H8_PREFIX_DP/EC49EK_H8_EXECUTED.json
```

The h=9/h=10 multiplicities are certified by exact finite-state counting and the analytic formula; the checker does **not** enumerate every raw word at those lengths. Full h=9 native-prefix optimality over `q>=1` remains open. The direct raw-word h=9 attempt exceeded the local execution limit and produced no completed output; no result is inferred from that attempt.

## 6. Provenance, authority, and next action

**Frozen scientific predecessor:** `awdawmip/enterprise-math@caa970c88315d55d1b1669589ef096a83c7d059b` (`EC49EK`); carry its historical frozen scientific input pins `GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e`, `EnterpriseMath@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, rather than replacing them with current main.

**Behavioral/control rules independently read in this run:** GLOBAL_KNOWLEDGE_V1 canonical main `f3fb0738848db1c43c2af6040c3a1f442ef7e812`; Enterprise Math canonical main `bdba5cfa529f565d303c869e19f254ae3712f446`, including `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `research_priorities/research_method.json`, project P000 and Heartbeat World. P000 and ACTIVE worldview unchanged.

**Actual owner/role evidence:** GitHub authenticated account `awdawmip`, repository collaborator `admin`. Native MCP 0.6.11 returned `research_authority_granted=false`; owner inventory read returned `CONTROL_QUOTA`. No Source-native Research Activity, CLAIM, Result, independent Driver review or admission is asserted. This author-side research proof is preserved on an existing Draft PR branch.

**Next EC49EM:** solve or sharply bound the `q>=1` prefix-tree optimization at h=9. Use the exact event quotient to group rank masks, but retain every distinct signed-X6 prefix for cost accounting. A first reproducible goal is a sound per-fiber branch-and-bound lower certificate using the 66-edge construction as the cutoff; search for a true 65-or-less edge witness or exclude it without enumeration of the 1,964,862 words in RAM. Advance the analytic all-H lower bound only after the q>=1 evidence is settled.