# R5 — An unbounded geometric family with pure edge-switching Q

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED (six sample members) / NOT_REVIEWED.
Scientific input remains frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Parent finite witness: `N5_SWITCH_ONLY_Q_GEOMETRIC_THEOREM.md`, Draft PR #2427.

## Theorem

For every integer `m >= 0`, take `n=5+m` indexed integer events with consecutive gaps

```text
(3, 2, 2, 3, 5, ..., 5)  [exactly m trailing length-5 gaps]
```

Set coverage radius `rho=2`, choose exactly `K=3+m` center **indices**, minimize total nearest-center integer distance subject to covering all events. Let closure a shorten the first length-3 gap to 2, and closure b shorten the fourth length-3 gap to 2.

For all four closure masks the optimum value is exactly `J=4`. Define the common forced appended center suffix

```text
H_m = {5,6,...,4+m};  H_0 = empty.
```

Then the **entire** optimizer family for each mask is exactly

```text
F_mask^(m) = { S union H_m : S in F_mask^(0) },
```

where `F_mask^(0)` is one of the four explicitly enumerated 5-event families in the parent note. Consequently

```text
P_m = empty,
Q_m = { {1,2,3} union H_m },
(|F0|,|Fa|,|Fb|,|Fab|) = (1,4,4,8).
```

On rank-labeled optimal-center path graphs (including source and sink arcs),

```text
E_ab^(m) = E_a^(m) union E_b^(m)
```

for every `m>=0`. Thus a genuinely geometric **joint-only path with no neutral joint edge** exists for unbounded event count and center budget.

## Proof

Every appended event has distance at least **5** from every other event in every mask; the closure operations affect only the original first and fourth gaps. Since radius is 2, every appended event can only be covered by a center at its own index. All m appended indices are therefore forced, and they serve only themselves. With budget K=m+3, exactly three centers remain for the five original events. Added centers have zero effect on those five event distances, so minimizing the full objective is *identical* to minimizing the original 5-event objective over three centers. This proves the family bijections, cost, P and Q.

The corresponding rank-labeled paths consist of an original three-center prefix followed by the fixed index suffix H_m. For `m>0`, replace each original terminal arc `last→sink` with `last→5`, append the same fixed chain `5→6→...→4+m→sink`, and preserve every other original arc. The map is identical in all four closure masks, and injective on old terminal arc labels; union of edge supports commutes with this common extension. Since the five-event witness has `E_ab^(0)=E_a^(0)∪E_b^(0)`, the identity holds for every m. When m=0 it holds by the parent certificate. The unique joint-only center set extends likewise.

All path descriptions retain original center-index provenance and ranks. No quotient or observer identification is used.

## Finite reproducibility and limits

Run `python VERIFY_R5_UNBOUNDED_SWITCH_FAMILY.py` in the same directory as `VERIFY_R5_N5_SWITCH_ONLY.py`. Its executed local output checks every m=0,1,...,5 using exact enumeration, the four costs, family sizes, P/Q and rank-edge equality, returning `PASS_R5_SWITCH_ONLY_INFINITE_FAMILY_SIX_FINITE_CHECKS`.

- Executed finite output SHA-256: `624fbb44558bf2a56667253eda88e362bba1229f6595d425308c034dea2bacb4`.
- Executed Python file SHA-256: `546de6b93ee20b4696b99f3276374fa87f0d73b16cfe8ee57b5b801e4311f595`.
- The **unbounded conclusion follows from the forced-center factorization proof**, not from the six finite tests.
- The length-5 separator gaps are outside the original shrink-to-2 operation. The original five-event gap alphabet and finite minimality certificate remain as stated in the parent result.

## Next question

Find a **connected, bounded-gap** unbounded family (e.g., all gaps at most three) where the mixed-color phenomenon persists, or derive a gap/rank-compatible sufficient condition excluding it in the frozen 954-event R5 special model. Determine whether common mandatory anchors forbid or actually facilitate mixed-color factorization.

This is an auxiliary one-dimensional radius-two optimizer theorem; no native X6 transfer, formal task claim, independent review or Foundation promotion is asserted.
