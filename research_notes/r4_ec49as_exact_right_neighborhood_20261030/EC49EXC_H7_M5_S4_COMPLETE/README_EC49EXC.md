# EC49EXC — Complete exact H=7 / M=5 / S=4 optimum

Date: 2026-11-03. Research mode: author-side portable mathematical proof; not an admitted native Source Result.
Predecessor: EC49EXB, immutable commit `0a8be226b838cced08120135e3213779a9b6954d`, Draft PR #1730.
Frozen scientific inputs (unchanged): GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Current behavior rules were read separately from canonical `main` on 2026-11-03; the scientific source pins remain frozen. The P000 / ACTIVE worldview is unchanged.

## Theorem EC49EXC-1 (global exact optimum)

In the frozen native signed-X6 seven-operation model with operation codewords

```
a=(-E1,-E1), b=(-E2,-E2), c=(+E1,+E2,-E1,-E2),
d=(+E2,+E1,-E2,-E1), e=(+E3,+E1,+E1,-E3),
f=(+E1,-E1), g=(+E2,-E2),
```

consider every horizon `h in {2,3,4,5,6,7}`. Each selected operation word has exactly `h` operation letters, ends at native displacement `(2,0,0,0,0,0)`, and all words in one horizon have the same **complete six-axis positive-step-count** vector `p_h`. The nine starting seam-history states and five observation buckets are the original model in the pinned `VERIFY_EC49ER.py` code. Every horizon must supply rational-linear observation rank nine.

Let `E` count distinct nonempty ordered **primitive signed native-X6 step prefixes** over all selected words, `M` count distinct six-component `p_h` BRC symbolic factor cache keys, and `S` count distinct nine-state observation transfer signatures. Then

**`min E | H=7, M=5, S<=4 = 80`**, and an attaining construction has **`(E,M,S)=(80,5,4)`**.

This is an exact finite-model result; it uses the BRC *symbolic positive-step monomial cache key*, not a physical Heartbeat/BRC simulation or a full native-world dynamic law.

## Proof of lower bound

The second horizon forces exactly the four transfer signatures `T4 = {sig(ce),sig(de),sig(ec),sig(ed)}`. Their exact rank table by subset size is `(3,5,7,9)`. Since `S<=4`, every horizon must realize all four signatures; each candidate key fiber is therefore `T4`-complete. The complete eligible-key counts for `h=2..7` are `(1,3,7,13,22,34)`; among 204,204 total ordered key schedules, 26,037 have exactly five distinct keys.

The predecessor EC49EXB proved that the 21,583 **early-repeat** schedules (repeated key pair `(3,4)`, `(4,5)`, `(4,6)`, or `(5,6)`) require `E>=80` using the exact H6/M4/S4 theorem `E6>=72` plus the native-code terminal two-edge lemma `E7-E6>=8`.

For the remaining **4,454 late-repeat** schedules (repeat pair `(5,7)` or `(6,7)`), the present finite proof closes all cases, with three successively stronger admissible lower bounds:

1. **Exact H5-prefix screen**: for each of 251 distinct H3–H5 key triples occurring in these schedules, solve the full four-signature native prefix-tree minimum `E5` using exact integer OR-mask dynamic programming. Every new full-four-signature horizon adds at least eight primitive edges by EC49EXB's verified terminal lemma. Thus `E7>=E5+16`. This proves `E7>=80` in **4,090** late schedules, including all 1,251 `(5,7)` schedules. The remaining 364 have repeated key pair `(6,7)`.
2. **Exact bounded H6 optimization**: for each of the 364 remaining distinct H3–H6 key schedules, solve `E6` with a **cost bound of 71** using the exact pruned trie DP from pinned EC49ES. Cost pruning discards only nonnegative-cost partial forests already greater than 71. In 332 schedules no cover of cost <=71 exists, so `E6>=72`; adding eight new H7 terminal edges gives `E7>=80`. In exactly **32** schedules, the exact H6 minimum is `E6=68`.
3. **Optimistic-free H7 prefix-tree lemma**: for each of these final 32 schedules, form the union `U` of *all* admissible primitive prefixes of the corresponding H2–H6 `T4`-signature candidate fibers, including the mandatory H2 base. This `U` is a superset of the earlier prefixes in **every feasible selected solution**. Assign every prefix in `U` zero cost, every other prefix unit cost; minimize the cost of four terminal H7 words with the four necessary `T4` signatures, common fixed H7 positive key `p7=p6`, and legal native displacement. Exhaustive four-color native-prefix-tree DP yields a minimum of **12** new edges in **each** of the 32 cases. Replacing actual paid earlier prefixes by the larger free set `U` can only reduce this incremental cost; hence any actual solution must add >=12 to its exact H6 minimum of 68. Therefore `E7>=68+12=80` for these 32.

The final 32 cases use just four H7 positive keys: `(4,5,1,0,0,0)`, `(5,4,1,0,0,0)`, `(6,3,1,0,0,0)`, `(7,2,1,0,0,0)`. Independent Node.js enumeration and independent four-color prefix DP reproduced the exact 12-edge bound for all 32 without importing Python code.

The complete exhaustive partition is:

| Subclass | Schedules | Proof |
|---|---:|---|
| Repeated key before H7 | 21,583 | inherited exact E6>=72, H7>=8 |
| (5,7) late repeat | 1,251 | exact E5>=64, H6+H7>=16 |
| (6,7), H5 bound sufficient | 2,839 | exact E5>=64, H6+H7>=16 |
| (6,7), H6 bound sufficient | 332 | exact E6>=72, H7>=8 |
| (6,7), optimistic H7 bound | 32 | exact E6=68, H7>=12 |
| **Total** | **26,037** | **all E>=80** |

Every subset is disjoint; the partitions and necessary key/signature completeness checks are explicitly generated in the executed code.

## Attaining construction (upper bound)

- `h=2`: `ce`, `de`, `ec`, `ed`.
- `h=3`: `cec`, `ded`, `ecc`, `edd`.
- `h>=4`: `cefg`, `degf`, `ecfg`, `edgf`, each followed by `f` repeated `h-4` times.

Direct native-X6 decoding verifies displacement `(2,0,0,0,0,0)` for every word, one complete positive-count key per horizon, exactly five distinct keys across six horizons, exactly the four `T4` signatures and rational rank nine at every horizon. The distinct primitive native prefix count is **80**, so the lower bound is attained.

## Exact computation and independent checks

The exact Python screen was executed (Python 3.13):

- `SCREEN_EC49EXC.py`: all 58,947 returning seven-letter words, all complete-key fibers and 4,454 late-repeat schedules; exact H5 DP for 251 distinct key triples; outcome 4,090 certified and 364 remaining.
- `SCREEN_H6_BOUNDED_EC49EXC.py`: native-prefix-tree bounded DP for 364 H6 schedules, cutoff 71. Outcome: 332 with `E6>=72`, 32 with `E6=68`.
- `SCREEN_FINAL_H7_EC49EXC.py`: full returning-word re-enumeration for the four relevant positive keys, the optimistic-free set `U` specific to each case, and exact 4-color tree DP for the final 32. Outcome: `min_new_cost=12` in all 32.
- `VERIFY_EC49EXC_INDEPENDENT.js`: Node.js 22 independently re-enumerates native signed paths, constructs T4 signatures and optimistic earlier prefix sets, and recomputes the four-color H7 DP. Outcome: **PASS**, 32/32 at exactly 12 new edges.

The recurrences keep for each trie node and observation-color bit mask the minimum integer number of occupied signed native edges. Child costs combine by bitwise OR of color masks; an occupied non-root native prefix is charged once, unless it is in the explicitly declared optimistic-free set. All edge costs are 0 or 1. Every admissible terminal set induces one such connected rooted forest; every represented cover reconstructs legal root-to-terminal native words, so the dynamic programming minima are exact for their finite declared inputs. For the H6 bounded pass, rejecting partial costs above 71 is sound because later additions are nonnegative.

Evidence: `EC49EXC_EVIDENCE.json.gz.b64` is a deterministic gzip/base64 envelope containing the *full* exact-screen outputs, all 364 bounded H6 decisions, 32 case-specific H7 costs, and the independent Node.js result. Reproduce with `base64 -d EC49EXC_EVIDENCE.json.gz.b64 | gzip -d > EC49EXC_EVIDENCE.json`. The optional SHA256 manifest verifies the plaintext script/evidence byte content and has no mathematical authority.

Required unchanged helper code: `VERIFY_EC49ER.py` from EC49ER's immutable evidence archive at `ed3ade49956f8a4deba33d0718097d5b30657539`, and `VERIFY_EC49ES.py` from EC49ES at `d1c0a0b8450bf0ca5caca926909e1c02c7c44668`. Place these beside the four current checkers; then run the four commands in the listed order. The long original source proof is this Markdown; older helper source and previous exact H6 results are reused, not redefined.

### Scope and admission

The theorem is exact within the declared seven-operation, finite-window, positive-key symbolic-BRC and nine-state observer model. The computation is finite and exact, plus the inherited terminal-edge lemma. It does not assert universal optimization for arbitrary operation alphabets, native six-axis real dynamics, or the entire H7 `(E,M,S)` Pareto frontier. This author-side artifact preserves P000/ACTIVE and the frozen scientific pins. Formal native CLAIM, Result and independent Driver mathematical admission are separate.

## Next research problem

EC49EXD: solve `H7, M=4, S<=6` exact minimum E, using the current known 72-edge feasible point and the present nested prefix-tree lower-bound technology; then combine surviving H7 resource regimes into the complete Pareto frontier. The exact no-go/optimality proof is still open there. See `NEXT_EC49EXD.md`.
