# X6 Unit174 — exact sharp Barlow period-drift deviation and frozen production callgraph

Date: 2026-11-20. Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2.

**Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_EXECUTED / FROZEN_SOURCE_TYPED / UNREVIEWED / NOT_ADMITTED.** This is a genuinely incremental sharpness theorem for the existing derived Barlow producer, not an X6 native-path identity, native Result, formal acceptance or a rerun of original R063.

## Exact source and typed production consumer

Historical comparison commit: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Scientific reference pin: `59538f585d037d09ef687b28715c4bc1a3f9fe03`. The audited frozen production chain is:

1. `src/enterprise_math/p022_barlow_stacking.py` (Git blob `cfa12c17671692d1fe0371b7d80e4cc019fbcf54`), `effective_vertical_signs` lines 114–132 and `stacking_prefix_imbalance` lines 139–142.
2. `src/enterprise_math/p022_barlow_precision.py` (Git blob `34f351f55f25c115a872a9cbaf1a6dd7212089af`), actual imports at 17–24 and `barlow_prefix_normal_form` at 53–72.
3. `src/enterprise_math/p022_barlow_growth.py` (Git blob `4185cafdb3e4ad4f55c58ff111747013e710af43`), imports at 27–28, `period_drift` at 130–133 and `drift_deviation_bound` at 249–268. Other actual producer use is `barlow_prefix_normal_form` at 110.
4. `tests/test_p022_barlow_growth.py` (Git blob `8e8418a87a1fbbdad9ba5ff03cbe532af0f6f224`) consumes the growth module at 3–13 and tests periodic growth/recurrence at 66–166; it does not explicitly test `drift_deviation_bound` in the inspected version. Thus production-to-production imports are verified, and test scope is stated precisely.

The original growth function documents a valid bound for all signed target layers, but does not claim an optimal constant. This unit proves the **same function** computes the exact least possible uniform constant, with a shorter one-sided integer formula.

## Theorem (all finite nonempty periodic ±1 words; all signed layers)

Let `p=(p_0,...,p_(L-1))` be any word of length `L>=1`, with entries `p_i in {-1,+1}`. Extend it periodically to all integer interfaces. Let `D=sum_i p_i` and `P_r=sum_(i=0)^(r-1) p_i` for `0<=r<=L`, so `P_0=0`, `P_L=D`. Let `delta_k` be the *effective* signed imbalance from layer zero to signed target layer `k` under the frozen Barlow convention, which negates interface signs on downward traversal. Define

```text
E_p(k) = | L*|delta_k| - |D|*|k| |,  k in Z
H_r    = L*P_r - D*r
C*(p)  = max( |H_r| : 0 <= r < L ).
```

Then

```text
min { C >= 0 : E_p(k) <= C for every integer k }
 = max_(k in Z) E_p(k)
 = C*(p)
 = drift_deviation_bound(p)
```

with all quantities exact integers and the maximum **attained** at some signed layer.

## Proof

For `k=nL+r >= 0`, `n>=0`, `0<=r<L`, periodicity gives `delta_k=nD+P_r`, so `L*delta_k-D*k=H_r`. The reverse triangle inequality `||a|-|b||<=|a-b|` yields `E_p(k)<=|H_r|`.

For a negative target layer `k=-(nL+r)`, with `0<r<L`, periodicity and inversion of traversed interface signs give `delta_k=-nD-(D-P_(L-r))`. Thus `L*delta_k-D*k = H_(L-r)`, and again `E_p(k)<=|H_(L-r)|`. For multiples `k=nL`, `E_p(k)=0`. Therefore `E_p(k)<=C*(p)` for every integer k.

For sharpness when `D != 0`, take any `0<=r<L` attaining `C*`. Choose `n` sufficiently large that `nD+P_r` has the same sign as `D`. Then for `k=nL+r`, the absolute values in `E_p(k)` have aligned signs and `E_p(k)=|L*delta_k-D*k|=|H_r|=C*`. When `D=0`, the same equality holds already at `k=r`. Hence the supremum is a maximum and is the least uniform constant.

To compare with the *frozen implementation*, first reverse all signs of the word if necessary (this leaves its reported bound and `|H_r|` unchanged), so take `D>=0`. Every one of its `0<|k|<L` upper/lower samples has error at most `C*`, as above. Conversely, for any `1<=r<L`:
- If `P_r>=0`, at the short upward layer `k=r`, `E_p(r)=|L P_r-D r|=|H_r|`.
- If `P_r<0`, at the short downward layer `k=-(L-r)`, the effective magnitude is `|delta_k|=D-P_r>0` and `E_p(k)=|L(D-P_r)-D(L-r)|=|H_r|`.
The frozen loop evaluates both short signs for every `1..L-1` and also includes zero. Therefore its returned maximum is exactly `C*`. This also covers `L=1`, all-one-sign patterns, and `D=0`.

The signed-prefix algorithm is a one-pass computation of `C*` using `L,D` and `P_r` only; it preserves the existing interface sign orientation and original producer output for every word.

## Concrete nonzero error witness

Take `p=(+1,+1,-1,-1,-1)`, so `L=5,D=-1`, and `P_2=2`. Then `H_2=5*2-(-1)*2=12`. The sharp bound is `C*=12`, attained at `k=-3` and `k=47` (each gives `E=12`). The residual is intrinsic to the periodic derived stacking observation, not a defect in an X6 signed-native argmax.

## Independently executed finite check

An independent local integer-only Python checker (not an import/execution of the frozen module) exhausted all 2,046 sign words of periods 1..10. It compared the frozen loop's precisely transcribed algorithm with the new signed-prefix formula; checked 149,518 short signed-layer observations, 16,368 far-layer observations, and an explicit sharpness witness for every pattern. Zero discrepancies. 20 word patterns had sharp bound zero and 2,026 had positive bound. Normal, `python -O`, `python -OO` runs produced byte-identical JSON. See `research_checks/X6_UNIT174_SHARP_BARLOW_DRIFT_CHECK_20261120.py` and `research_checks/X6_UNIT174_SHARP_BARLOW_DRIFT_RESULTS_20261120.json`; the former must be attributed as the independent verifier, not original native R063.

## 28-LP disposition and obligations

**KEEP / CORRECTLY_TYPED_DERIVED_BARLOW_PERIODIC_GROWTH / SHARP_BOUNDED_RESIDUAL**. This gives an additional precise frozen producer→production consumer provenance and sharpens an actual documented invariant. It does not assert physical X6 rotation/plane equivalence. No verified LP011 wrong-native argmax or LP019 positive N-BRC illegal subtraction at these inspected functions. Alleged original erroneous `commit:path:line` remain `UNRESOLVED_PROVENANCE`, and the rest of the 28-LP producer-consumer crosswalk remains open. The original R063 17/17 and 512/512 native benchmark was not rerun.

Prior Units1–173 and Activity190 are reused. Independently review before any formal admission. Units172–174 Native semantic PROGRESS remains contingent on same-lane current CLAIM/RUN authority and is not established by this GitHub evidence.
