# EC49FFF — Canonical 17-key BRC quota theorem and minimum-key census

Date: 2026-11-09 Asia/Shanghai. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Author-side exact finite proof with actually executed standard-library Python reproducer; independent Driver review/Source Result pending. Original signed-X6 six-operation BRC, complete key (x,y,z), nine-state DFA, H2–H9. This extends the exact observer staircase of EC49FFD and the EC49FFE 24-path family. P000 and ACTIVE worldview unchanged.

## Theorem 1 — maximal signature reach of a fixed terminal horizon

The native full-key count identities are:
#a=z-1, #e=z, t=#c+#d=x+y-h-1, #f=h+1-y-2z, #g=h+1-x.
All counts are nonnegative. Therefore z≥1, x≥2z, y≥0. Put H=x+y-1 and r=min(x-2z,y). EC49FFD proves this exact observer staircase: at each integer h in [H-r,H-1] all four low labels L={1,2,4,8} are reachable; at h=H label 16 is reachable iff x>2z, and label 32 iff y>0. No other horizon has nonzero terminal support.

**Canonical domination theorem.** For each integer H≥3 put f=floor((H-1)/2), g=H-1-f and K_H=(2+f,g,1). For every count-admissible key K with the same terminal H, the canonical K_H supports every nonzero observation signature that K supports at every horizon. In fact K_H supports both high labels at H and all four low labels at each integer horizon ceil((H+1)/2)≤h<H.

**Proof.** At terminal H, f_original=x-2z, g_original=y and f_original+g_original=H+1-2z≤H-1. Hence r=min(f_original,g_original)≤floor((H-1)/2). The proposed z=1 canonical K_H attains that bound and f,g≥1 when H≥3. Its observer support therefore contains the original key's entire low interval and its terminal high subset. The staircase's explicit word constructions establish realizability. QED.

At H=2, f+g=1: there are two nonzero terminal supports, separately represented by K_{2,16}=(3,0,1) and K_{2,32}=(2,1,1). Neither supports low observations. Thus with nonnegative y two distinct full keys are required for simultaneous H2 labels 16 and 32. If x,y,z must all be strictly positive, H2 label 16 is unreachable, since its count requires y=0.

## Theorem 2 — exact finite oracle for arbitrary H2–H9 quota requirements

For H≥18 the earliest possible low horizon is ceil((H+1)/2)≥10, and its high horizon H is outside H2–H9. Keys with H<2 also give no requested nonzero label. Replacing every original key by the dominating representative at its H leaves its required signature coverage intact and never increases key count. Hence the potentially unbounded complete-key domain reduces exactly, for **minimum key cardinality and quota feasibility**, to 17 candidates:

K0 = {(3,0,1),(2,1,1)} ∪ { K_H : H=3,...,17 }.

For the strictly positive domain remove (3,0,1), leaving 16 candidates. Conversely every representative is a valid full key with actual DFA witness words, so the reduction is both necessary and sufficient.

Any required subset of low signatures at a given horizon can be represented by a single low bit, because any low-capable full key produces all L. At H3–H9, a single high bit suffices because a canonical key supplies both high labels. H2 needs separate bits for 16 and 32. Thus there are exactly 17 requirement bits: low bits H2–H9 (8), high bits H3–H9 (7), and two H2 high bits. Enumerate the 2^17 possible canonical-key subsets, store exact bitwise coverage and key count, then apply an exact min-over-supermasks transform to determine the minimum key count for **each of the 131,072 possible requirement masks**. This fully solves the quota-cardinality problem, even when high and low signatures are both requested at one horizon, provided separate legal words are permitted for each label.

## Executed integer census (all 131,072 requirement masks)

| Minimum full keys | Count-admissible (y≥0) | Strictly positive |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 76 | 75 |
| 2 | 1146 | 1071 |
| 3 | 6748 | 5677 |
| 4 | 20109 | 14432 |
| 5 | 34152 | 19720 |
| 6 | 35192 | 15472 |
| 7 | 22576 | 7104 |
| 8 | 8896 | 1792 |
| 9 | 1984 | 192 |
| 10 | 192 | 0 |
| unreachable | 0 | 65536 |

All 65,536 strictly-positive unreachable masks are exactly the masks demanding high label 16 at H2. The standalone Python checker recomputes **all 294** count-admissible H2–H9 (h,K) original-DFA supports and compares against the maximal representative, with zero discrepancies. It then exhaustively computes all 131,072 requirement minima for both key domains. Executed result: EXACT_PASS.

For the original **15** 22-path template requirements (H3 full high, four later full-high windows, all other windows full-low), 10 patterns require five keys and five require six keys when the cardinality cap is relaxed. For the original **15** 24-path templates (H2/H3 full low, four later full-high windows, remaining windows full-low), nine patterns require five keys and six require six keys. The H3-low, high H6/H7/H8/H9 pattern requires **six** keys; a valid canonical quota witness is (3,1,1),(3,2,1),(4,3,1),(5,3,1),(5,4,1),(6,4,1). This recovers EC49FFE's nine feasible <=5-key patterns by a separate, more general exact algorithm.

## BRC interface, provenance, next problem

This result is an exact observer-signature **quota** and *minimum-number-of-full-keys* theorem. The declared carrier for later cost work is still the full ordered operation word expanded to signed native X6 microsteps. The canonical replacement need not preserve native signed prefixes, path order, branch/provenance or native edge cost; the later C_native optimization uses the original full keys and words. In particular the mother's target of at most five keys and at most **93 distinct ordered signed-X6 prefix edges** remains open.

Sources (immutable scientific provenance): native operation semantics EC49FFC at 2dd856c416f111d90d523dcb10cde952248ec814; original nine-state observer staircase EC49FFD at df0dbc54707a6926db858631e5a03fea189dccde; last 24-path fixed-inventory optimum 106 and census EC49FFE at 9f2e6ae960fbbd55e021302de875b54868797f6b. Original science frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. The adjacent Python file is standalone and uses exact integers only.

**Next EC49FFG:** apply this complete quota oracle to inclusion-minimal unclassified support masks with <=5 full keys; for survivors enumerate actual keys, not only canonical representatives, then compute exact ordered native prefix lower bounds or explicit <=93-edge constructions. Preserve independent Driver review and formal Source CLAIM/Result boundaries.