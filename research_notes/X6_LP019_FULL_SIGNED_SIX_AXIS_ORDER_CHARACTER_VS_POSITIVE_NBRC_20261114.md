# X6 LP019 — exact full-six-axis inversion-character separation from native positive N-BRC

Date: 2026-11-14. Mother task `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable publication `TP2-B4A441B23DA3159232C2`; author `EM-X6-FB6990` and original Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Evidence: **NEW AUTHOR-SIDE EXACT THEOREM / EXECUTED FINITE INTEGER CHECK / UNREVIEWED / NOT_ADMITTED**. Original signed-X6 native experiment and the R063 C3/C4 benchmark were **not** rerun.

## 1. Frozen object, provenance and genuinely new question

The scientific input is P000 V5 at `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` (`p000_reality_foundation.json`, blob `c93d8150f1d223424b3506a6d2cdd5280b50825f`), selected native Cell anchor and signed six-axis `Z^6` primitive steps. The immutable historical comparison generation is `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

The already published 20:00 unit identified `experiments/brc_weighted_log_semiring_check.py` (historical blob `0fdae08413b8caff4c08ca52649d5f4b0fa8292c`, lines 128–137): a **legitimate deliberately weighted** signed two-path cancellation, not subtraction of N-valued positive native shortest paths. Its 60 two-axis signed endpoint tests establish `native BRC=2` while a chosen antisymmetric order character is zero. This unit answers a **different, stronger finite-to-universal question:** given an arbitrary six-axis native endpoint, classify exactly when an explicitly defined inversion-parity readout cancels, and determine what positive N-BRC information survives. This optional readout is **not** claimed to be the historical graph's arbitrary externally assigned weights, not the R063 `C4` phase law, and not an actual located erroneous LP019 native caller.

## 2. Source/target and exact theorem

Fix the original signed native Cell-to-Cell displacement `d=(d_1,...,d_6) in Z^6`. The shortest native primitive words have `c_i=|d_i|` repetitions of the **axis-labeled step with the sign of `d_i`**, total length `n=sum c_i`. The original N-valued shortest-path mass is

```
B(c) = n! / product_i(c_i!) in N.
```

Keep this mass unchanged. Introduce a separate, explicitly optional **Z-valued order-character**: fix the native axis-label order `1<2<...<6`. For each *distinct labeled shortest word* `w`, let `inv(w)` be the number of pairs of positions `p<q` with `axis(w_p)>axis(w_q)`. Define

```
S(c) = sum_{shortest native axis-words w} (-1)^inv(w) in Z.
E(c) = (# words with even inv) = (B(c)+S(c))/2
O(c) = (# words with odd inv)  = (B(c)-S(c))/2.
```

The sign of a step in physical native X6 is **not** the sign `(-1)^inv`; the latter is an added character observer. Changing the native signs of nonzero step components changes the signed endpoint but leaves `B,S` invariant under the chosen label order.

**Theorem (all signed native six-axis shortest words, exact).** Let `k=# {i : c_i is odd}`. Then

```
if k>=2: S(c) = 0;
if k<=1: S(c) = floor(n/2)! / product_i(floor(c_i/2)!).
```

In particular `S=0` **if and only if** at least two axes have odd nonzero step counts. The exact channel sizes `E,O` are nonnegative integers, even when `S=0` and `B>0`.

**Proof.** First take two ordered axes with multiplicities `a,b`, with the inversion rule that later-ordered-axis letters preceding earlier-ordered-axis letters count as inversions. Let `F(a,b)` be the signed word sum. By classifying the last letter,

```
F(a,b) = (-1)^b F(a-1,b) + F(a,b-1), F(a,0)=F(0,b)=1.
```

Exact induction over the four parity cases gives

```
F(a,b) = 0                                    if a,b odd;
F(a,b) = binom(floor((a+b)/2), floor(a/2))   otherwise.
```

For six ordered letters, build the multiset-word shuffle by inserting each next label among all earlier ones. Inversion exponent separates into the prior word's inversion count plus the binary shuffle inversions; the total signed sum therefore factors into these two-axis `F` factors on successive cumulative counts. The first insertion that makes the cumulative count odd **and** adds another odd multiplicity gives `F=0`. If at most one multiplicity is odd, every factor is a positive ordinary binomial of halved counts, and the product telescopes to the displayed half-multinomial formula. All native shortest words are counted exactly once by this insertion construction. QED.

**Why this distinguishes algebraic cancellation from N-BRC annihilation:** for `c=(1,1,0,0,0,0)`, the two native words exist, `B=2,S=0,E=O=1`. For `c=(1,1,1,0,0,0)`, `B=6,S=0,E=O=3`. For `c=(2,2,2,0,0,0)`, `B=90,S=6,E=48,O=42`. The zero value of `S` is not a zero native path mass and cannot be used as Boolean nonreachability. The invariant ordered word object and the signed-native endpoint/provenance should be retained when later consumers need either one. These are strict differences between N-valued and Z-valued observers, not an error assertion against a source that is explicitly typed as weighted.

## 3. New executed, independently structured exact test

Standalone original checker: `research_checks/X6_LP019_SIGNED_SIX_AXIS_INVERSION_CHARACTER_20261114.py`, GitHub commit `9c7420a67b3276ca23e6e6961c6229caf7dc2bab`, blob `fdc946ba5f407a706e9447ba2aa04acd5c585ee6`, SHA256 `fd26da49e9568dcb9f99e7c4b192be774da7ad335422f13f29fb2d7cb20e7d87`.

Execution in this Research turn with Python exact integers exited 0:

```
PASS_X6_LP019_SIX_AXIS_INVERSION_CHARACTER six_axis_profiles= 4096 max_total_steps= 18 zero_character_profiles= 3648 independent_brute_profiles= 81 signed_two_axis_endpoints= 60
```

For all `4^6=4096` six-axis nonnegative multiplicity vectors `c_i in {0,1,2,3}` (total path length up to 18), three independent calculations were compared: (i) the closed-form signed character, (ii) a direct signed-word last-letter recurrence, and (iii) the exact unsigned multinomial against a separate unsigned-word recurrence. All parity-channel integrality and `|S|<=B` bounds passed. A separate explicit list of **actual word permutations** checked 81 four-axis vectors `c_i in {0,1,2}` and agreed. The 60 signed two-axis primitive endpoints reproduce, without silently substituting, the 20:00 unit's two-versus-zero boundary. The universal theorem above rests on induction and shuffle factorization, not on this finite check.

The checked source is a standalone newly authored regression; it does **not** execute the original R063 C3/C4 benchmark, replace its validation conditions, mutate any original historical program, or assert newly accepted native physics.

## 4. Claim-level LP019 source disposition and continuation

- `PRESERVE_PATH_BRC`: original `B(c)` is always the positive natural shortest-word multiplicity. In particular, no path is removed by an observer-level signed sum.
- `PRESERVE_DERIVED_SIGNED_READOUT`: the optional inversion-character `S(c)` is a Z-valued, axis-label-order-dependent higher observation. For two odd counts it cancels exactly even though the native multiplicity survives.
- `KEEP_WEIGHTED_SOURCE`: frozen `experiments/brc_weighted_log_semiring_check.py` lines 128–137 intentionally uses externally chosen signed weights; its operation is not the new inversion-character formula, and neither is a found erroneous LP019 native subtraction caller.
- `UNRESOLVED_PROVENANCE`: actual historical/current wrong LP011 signed-native argmax selector and LP019 wrong positive-native multiplicity-subtraction caller remain unidentified outside the already audited frozen corpora. The prior 268 historical direct Python-body audit, 24 additional X6 nested bodies, and current typed-consumer checks remain consumed, not rerun.

The mother claim-level 28-LP dependency/source ledger and independent Driver `REQUEST_REVISION` remain unclosed; no formal Result/review is inferred. Next exact action: with original Research SID/CLAIM/RUN and current owner-checked authority, publish this single new GitHub-proven scientific unit into the canonical semantic checkpoint and original Activity; then inspect **one genuinely unexamined, explicit, current R063/LP019 downstream source** at immutable commit/function/line or hand off the original unexecuted C3/C4 benchmark for same-object execution. Do not repeat the 17:00 safety-denied report in any form. Retain all earlier 13 Source units and original benchmark boundaries.
