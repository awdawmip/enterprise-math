# Stage413-B — Sharp asymmetric raw-suffix boundary for two Q pops and one paired cancellation

Date: 2026-11-04 (Asia/Shanghai). Research2 portable author research, continuing Stage412-B at `bf6df609eeee0a4a3ec66b0f63dd2643defc904e`, Draft PR #1736. **AUTHOR-PROVED / EXACT INTEGER EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Source and precise model

Immutable scientific input remains Global Knowledge `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, and P000 source blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative rules were separately checked against Global Knowledge canonical main `e2697bf474acb5db3f4a457fb72452942ebe3495` and Enterprise Math main `7e529b7f873b82b684d4cc8a259fa7951e0a9e1e`. No world axiom or locked pin is changed.

Let `D={+E_j,-E_j:1<=j<=6}` be the **twelve signed directions in six native spatial axes**, interpreted as individual ordered steps in the X6 chart relative to an explicitly chosen Cell. Use `A=+E1`, `B=-E1` only for the witnesses/family below, not as a separate native two-dimensional space. Each state is two ordered words `P,Q`; initial lengths are equal `n`. The complete instantaneous observer is

`O(P,Q)=(|P|,|Q|,z(P),z(Q),J_P,J_Q,K(P,Q))`,

where `J_X(a,b)` counts directed adjacent native labels, `z` is the exact signed six-component displacement, and `K(P,Q)=sum_{t=1}^{min(|P|,|Q|)} [P_t=Q_t]` compares **absolute positions**, not relative offsets. Enabledness of attempted actions is observed. Future operations `L2` are arbitrary paired `APP(a,b)` for any `a,b in D`, at most **two** Q-only `POP_Q`, and at most **one** paired `CANCEL`. A `CANCEL` is enabled only when the last two letters of **each** source form an inverse pair; it removes two final letters from each source. Budgets and choices are common knowledge. An invalid attempted action is a distinct observer outcome.

Positive, exactly labelled path multiplicity/Euler residual transitions implement the applicable BRC counting structure; this is not a calculation of signed interference amplitudes, physical time or native Shor dynamics.

## Theorem 413.1 — Universally sufficient and coordinatewise sharp window `(4,5)`

For arbitrary two initially equal-length full-X6 history pairs `(P,Q)` and `(P',Q')` with **the same complete initial `O`**, if

`last_4(P)=last_4(P')` and `last_5(Q)=last_5(Q')`,

then the complete observation and action enabledness agree after **every finite legal future** from `L2`, including arbitrary twelve-direction paired appends. Here `last_h` retains the entire word when its length is below `h`.

Moreover neither `4` nor `5` can be decreased while using a componentwise raw-suffix certificate: a `P` window of length three fails even when the entire `Q` word is known, and a `Q` window of length four fails even when the entire `P` word is known. Thus **the coordinatewise minimum universal raw-suffix pair is `(4,5)`**. This is a representation-specific optimality theorem; the minimum future-equivalence quotient of an individual observation fiber can be smaller.

### Sufficiency proof (complete future, not a finite search)

Track a given common operation trace with an original-prefix/append-stack decomposition:

`P_t=P[1:n-d_P] U`, `Q_t=Q[1:n-d_Q] V`.

Because all operations act at the right endpoint, the word `U` (resp. `V`) consists of surviving appended letters in their original order; `d_P,d_Q` are the numbers of original letters removed. For the two compared histories, `(d_P,d_Q,U,V)` are identical inductively, once enabledness is identical. The single paired cancellation removes at most two original `P` letters and two original `Q` letters; two Q pops remove at most two additional original `Q` letters. Thus throughout:

`0<=d_P<=2`, `0<=d_Q<=4`.

For each source, its truncated ORIGINAL endpoint is the original endpoint minus exactly the removed original letter displacement vectors, known from its shared suffix. Its truncated directed-edge histogram is the original histogram minus the `d` trailing edges, known from `last_(d+1)` of the original (P needs at most 3, Q at most 5). If the entire original word has been removed, the same calculation uses its fully retained short word. The junction edge from the remaining original last letter to the first surviving appended letter and all edges internal to the appended stack are identical across compared histories.

For the joint observer, partition matching positions into (i) original-original, (ii) original-appended in either order, and (iii) appended-appended. The original-original contribution is the *initial* `K` minus the initial equality indicators on the last `max(d_P,d_Q)<=4` original positions, all of which are determined by shared `P`-four and `Q`-five tails. Each original-appended overlap occurs within at most `d_Q<=4` terminal original P labels or `d_P<=2` terminal original Q labels, respectively; these are also shared. Appended-appended matches use identical `U,V` and their absolute positions because the cut lengths are identical. Hence the complete `K` is identical.

Finally, an enabled `CANCEL` is determined by the last two letters of each current word whenever the cancel budget is still available. If no appended letters cover those positions, the needed original P pair is contained in `P`-four (at most two original P letters were removed), and the needed original Q pair is contained in `Q`-five: before the cancel is spent, at most two original Q letters have been popped, so its last two remaining original letters lie within the last four original Q positions. If all four original Q letters have been removed, both Q pops and the cancel have already been spent; no further destructive action is enabled, and future appends only need the known last single original label for the junction edge. For short words the retained full word and length decide boundary availability. Hence every next `APP`, `POP_Q`, or `CANCEL` has identical enabledness and identical decomposition updates. Induction on the future trace length proves the theorem.

### Coordinatewise lower witnesses

Witness P, `n=6`:

- `(P1,Q)=(AABAAB,AAABAA)`;
- `(P2,Q)=(ABAAAB,AAABAA)`.

Their complete initial observers coincide (`K=3`), their P tails of length 3 are both `AAB`, and their Q words are identical. After `POP_Q, POP_Q, CANCEL`, the states become `(AABA,AA)` and `(ABAA,AA)`, with `K=2` versus `K=1`. All three operations are enabled. Therefore P-three cannot be universally sufficient for L2, regardless of how much of Q is retained.

Witness Q, `n=7`:

- `(P,Q1)=(AAAAAAB,AABABAA)`;
- `(P,Q2)=(AAAAAAB,ABAABAA)`.

Their complete initial observers coincide (`K=4`), P is identical, and the Q tails of length 4 are both `ABAA`. After `POP_Q, POP_Q, CANCEL`, the states become `(AAAAA,AAB)` and `(AAAAA,ABA)`. The Q directed-edge multisets are `{AA:1,AB:1}` and `{AB:1,BA:1}`, respectively. All operations are enabled. Thus Q-four cannot be universally sufficient. These exact word witnesses, endpoints, edges and match counts were rechecked by the executable evidence.

## Theorem 413.2 — Exact raw-suffix multiplicities for the full one-B/two-B family

Use Stage411/412's complete `F_n` initial observer, `n>=5`: `P_i=A^(i-1)BA^(n-i)` has one interior B, and `Q_{r,s}=A^(r-1)BA^(s-r-1)BA^(n-s)` has two nonadjacent interior Bs; `2<=r`, `r+2<=s<=n-1`, `i in {r,s}`. Exact initial `J`, endpoints and `K=n-1` are specified in Stage412. The family has `(n-3)(n-4)` histories. For `n>=7`, the **complete** multiset of `(last_4(P),last_5(Q))` has the following fourteen possible keys and counts (zero-count keys are absent at the indicated boundary):

| P tail | Q tail | Exact number |
|---|---|---:|
| AAAA | AAAAA | `(n-7)(n-8)` |
| AAAA | BAAAA | `2(n-7)` |
| AAAA | ABAAA | `n-6` |
| BAAA | ABAAA | `n-6` |
| AAAA | AABAA | `n-6` |
| ABAA | AABAA | `n-6` |
| AAAA | AAABA | `n-6` |
| AABA | AAABA | `n-6` |
| AAAA | BABAA | `1` |
| ABAA | BABAA | `1` |
| AAAA | BAABA | `1` |
| AABA | BAABA | `1` |
| BAAA | ABABA | `1` |
| AABA | ABABA | `1` |

**Proof.** Split according to the second Q defect `s`. If `s<=n-5`, all final P-four/Q-five labels are A, and choosing nonadjacent `r<s` with `s<=n-5`, followed by either `i`, gives `(n-7)(n-8)` histories. If `s=n-4`, the `n-7` choices `2<=r<=n-6` each give two histories with `AAAA|BAAAA`. If `s=n-3`, the `n-6` choices `r<=n-5` give P tails `AAAA` and `BAAA` with Q tail `ABAAA`. For `s=n-2`, choices `r<=n-5` give `AAAA|AABAA` and `ABAA|AABAA`, while `r=n-4` gives the two `BABAA` keys. For `s=n-1`, choices `r<=n-5` give the two `AAABA` keys; `r=n-4` gives the two `BAABA` keys; `r=n-3` gives the two `ABABA` keys. All choices are mutually exclusive and exhaustive. The sum is `(n-3)(n-4)`. This proof is a full-parameter combinatorial derivation; the exact Euler/K residual transfer independently verifies the counts for selected `n` without enumerating full history pairs.

The sufficient raw-suffix state count is consequently `12` at `n=7`, `13` at `n=8`, and **14 for every `n>=9`**. At `n=6`, direct evaluation gives six sufficient raw-suffix keys, and `n=5` gives two. In particular the safe count is eventually bounded despite quadratic growth of the observation fiber.

## Theorem 413.3 — Six traces distinguish nine persistent classes under L2

Consider the following six finite observer tests, with `C` denoting paired `CANCEL` and `P` a Q-only `POP_Q`:

`T1=P`; `T2=P,P`; `T3=P,P,C`; `T4=P,P,APP(B,A),C`; `T5=P,P,APP(B,B),C`; `T6=P,C,P`.

For `n>=6`, these six traces partition `F_n` into the following nine **test-observable** classes. Some are empty for small `n`:

| Group | Exact condition on `(r,s,i)` | Cardinality |
|---|---|---:|
| G0 | `s<=n-4` | `(n-6)(n-7)` |
| G1 | `s=n-3` | `2(n-6)` |
| G2 | `s=n-2, i=r` | `n-5` |
| G3 | `s=n-2, i=s` | `n-5` |
| G4 | `s=n-1, i=r, r<=n-4` | `n-5` |
| G5 | `s=n-1, i=s, r<=n-5` | `n-6` |
| G6 | `s=n-1, i=s, r=n-4` | 1 |
| G7 | `s=n-1, i=r, r=n-3` | 1 |
| G8 | `s=n-1, i=s, r=n-3` | 1 |

**Proof of exact test partition.** Directly apply the six fixed tests to `P_i,Q_{r,s}`. Each trace removes or tests at most the last four original Q labels and two original P labels. The retained final endpoints and labelled edges are obtained by subtracting those suffix letters; `K` is updated at the same absolute positions. Thus all six observation signatures are constant within the nine listed conditions. The nine signatures are pairwise different: `T1` separates `s=n-1` from earlier `s` using the removed `BA` edge; `T2` separates `s<=n-4`, `s=n-3`, `s=n-2` and `s=n-1` via changes to `J_Q(AA), J_Q(BA),K`; `T3` identifies G8 via an enabled cancel and the resulting observer; `T4` separates G2/G3 by post-cancel `K` (`-2` and `-3` relative to the initial count); `T5` separates G0/G1 via post-step `J_Q(AA)` changes (`-3` and `-2`) and G4/G7 via `J_Q(BA)` changes (`-1` and `-2`); `T6` separates G5/G6 via `J_Q(BA)` changes (`-1` and `-2`). These change values are direct substitutions, independent of `n` wherever the corresponding group is nonempty. The conditions partition the combinatorial `(r,s,i)` ranges; summing the number of choices gives the table. The executed checker verifies complete six-trace signatures for every individual family history at `n=6..20` in its selected cases, rather than relying on the displayed abbreviated distinguishing coordinates.

Consequently the **true all-horizon quotient** has at least as many states as this finite test partition. Together with Theorem 413.1/413.2:

- `q_L2(F_5)=2` and `q_L2(F_6)=6` (matching whole-fiber upper bounds).
- `8 <= q_L2(F_7) <= 12`.
- `9 <= q_L2(F_8) <= 13`.
- **For every `n>=9`, `9 <= q_L2(F_n) <= 14`.**

Thus the Stage411-B all-horizon `L1` five-state result necessarily splits under `L2` for **every** `n>=7`, not only the shortest `n=6` witness. The lower bounds are unconditional within the declared `L2` path-observer model; the upper bounds use the proved universal raw-suffix preservation theorem. The exact `L2` minimum for `n>=7` remains to be determined.

## Executed verification and evidence scope

`REPRO_STAGE413B.py` uses only exact Python integers, deterministic directed-edge counts and the twelve-label native displacement map. It compares the sharpness witnesses' **full** initial observations, replays the enabled operations and checks the distinguishing output. It implements the exact sparse `J_P,J_Q,K` residual Euler transition with unit weight per allowed next labelled edge type; a next-edge multiplicity is never multiplied by the residual count of identical edge copies. It compares exact terminal `(4,5)` suffix multiplicities against independent complete-word enumeration for `n=5..10`; runs the residual transfer also at `n=12,16,20`; and checks the six-trace nine-class certificate for these same instances. Returned marker: `STAGE413B_SHARP_ASYMMETRIC_BOUNDARY_PASS`. Generic sufficiency and all-n counting are proved above rather than inferred from finite computation. The code is a portable independently executable verifier, not a platform-signed formal proof.

## Carry-forward question and admission state

Stage414-B: determine the **exact** `L2` future equivalence relation among the 14 eventual safe suffix classes (possibly a nine-state quotient), by a symbolic all-twelve-direction transition refinement or a scope-correct coinductive bisimulation. Test whether G0/G1 etc. are sufficient under arbitrary appended directions, not merely the six diagnostic traces. Preserve full joint absolute K and the actual remaining eraser budgets, source labels and BRC provenance. Extend the residual Euler transfer to count proved equivalence classes without full history enumeration. The native Enterprise Math control gateway currently exposes read-only scopes and did not confirm any active owner; no CLAIM/Result/Driver admission is asserted. All above results are author-side mathematical outputs awaiting independent review.
