# PREFIX-831 — Sixteen-source exact first separation at step eleven by overlap-cancelled PTE lifts

**Status:** AUTHOR_PROVED / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen scientific input:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; continuation of PREFIX-827 through PREFIX-830. Auxiliary positive weighted BRC Q-only, not native X6 physical time.
**Question:** improve the known bound `11 <= p_min(11) <= 20` for a complete occupancy histogram first difference at Q step eleven.

## Theorem 831.1 — Exact 16-source certificate

In the PREFIX-829 model let the capacity be `q=p=16`, with the distinguished mark initially absent, insertion weight `a=2` and marked-source removal weight `b=3`. The two positive-integer multisets are:

```text
A = [2,18,49,54,79,111,113,116,143,175,187,190,206,246,251,276]
B = [1,26,31,71,87,90,102,134,161,164,166,198,223,228,259,275]
```

Writing `Y_l(t;X)` for the total positive weighted count of all labelled Q trajectories of length `t` ending with `l` occupied sources, then

- `Y_l(t;A)=Y_l(t;B)` for **every** `0 <= t <= 10` and `0 <= l <= 16`;
- at `t=11` the sole difference is at occupancy `l=5`;
- the signed *difference between two positive trajectory counts* is exactly
  `Y_5(11;A)-Y_5(11;B) = +15433735631061927532953600000`.

Consequently **`11 <= p_min(11) <= 16`**, improving the previously certified upper bound 20. Minimality at 16 is **not** claimed.

### Reusable lemma: overlap-cancelled one-step lift

For equal-size integer-weight multisets `U,V` with first unequal elementary symmetric coefficient at degree `n`, let `h>0` and set
`U*=U disjoint_union (V+h)`, `V*=V disjoint_union (U+h)`. Remove every common element from both sides, including multiplicity. The result has the same power-sum difference polynomial because identical terms cancel. Its first differing elementary symmetric coefficient is at degree `n+1`, with
`Delta e_(n+1) = n*h*Delta e_n`.
Its number of sources on each side is exactly `2p-c`, where `c` is the multiset intersection cardinality of `U*` and `V*`.

**Proof.** Use Laurent generating polynomials `F_U(z)=sum_(u in U) z^u`, with multiplicity. The unpruned lifted difference is `(1-z^h)(F_U-F_V)`; removing a common labelled weight from both multisets changes neither the signed Laurent polynomial difference nor its order of vanishing at `z=1`. Equality of ordinary power sums through degree `n-1` is equivalent to vanishing of order at least `n` at `z=1`. Multiplying by `1-z^h` increases the exact order by one because `h>0`. The binomial identity gives `Delta s_(n+1)^* = -(n+1)h Delta s_n`; Newton's identities give the stated coefficient identity. Common-weight removal is a **new witness construction**, not a claim that arbitrary distinct labelled source histories can be quotiented under future operations. QED.

### Exact witness construction and proof

Start from the previously recorded ideal 9-term integer PTE witness in PREFIX-830:

```text
S = [-98,-82,-58,-34,13,16,69,75,99]
T = -S = [98,82,58,34,-13,-16,-69,-75,-99]
```

A direct elementary-coefficient calculation gives equality through `e_8` and `Delta e_9 = 3377425033382400` (S minus T). Apply the lemma first with `h=24`. The common weights are `[-75,-58,-34,58,82,99]`; cancel all six to obtain **12** sources per side, with first difference at degree ten. Apply the lemma again with `h=53`. The common weights are `[-45,-16,8,37,40,69,93,122]`; cancel all eight to obtain **16** sources per side, with first difference at degree eleven. Translate both resulting multisets by `+100`, preserving all lower power-sum equalities, to obtain exactly A and B above, now strictly positive.

The first nonzero elementary symmetric difference is
```text
Delta e_11 = 9*10*24*53*Delta e_9
           = 386647617821617152000.
```
All `Delta e_k=0` for `0 <= k <= 10`. By the exact saturated-absent-mark triangular observer theorem proved in PREFIX-829, these conditions imply equality of *complete* future Q occupancy histograms for steps 0 through 10. At step 11 only bin `p-11=5` can depend on `e_11`, and its difference is `11!*Delta e_11`, yielding the integer above. This proves Theorem 831.1.

## Separate named-state verification

The accompanying Python 3 standard-library checker independently enumerates weighted Q trajectories using the full **named subset bitmask and marked-source presence bit**. It applies a removable named source's own positive integer weight, mark removal weight 3, and mark insertion weight 2 only below capacity. Its recurrence does **not** use PREFIX-827's closed-form histogram formula.

It checked both 16-source families for steps `t=0,...,11`, all `17` occupancy bins per step: **204 exact scalar comparisons**, **525970 named states visited** in total, and **4092476 named transition updates**, with all assertions passing. Independent coefficient recurrence checks both lift identities and the predicted `Delta e_11`. No floating-point arithmetic or approximation is used. The theorem follows from the proof above; the finite exact test supports this particular certificate.

Reproduce with `python3 PREFIX831_R6_N11_OVERLAP_LIFT_MINICHECK.py`. The result JSON records explicit parameter values and comparison counts. Files are intended for Source `research_notes/portable_direct/`, not a claimed formal Task Result or Review.

## Interpretation, provenance and next questions

Observer: full nonnegative occupancy histogram. Operation language: repeated `Q=R+A` only, on positive count mass and the exact named-source transition rules; capacity initially saturated and mark absent. This does not certify safety for independently addressable `R,A`, for an individual source, for signed amplitudes, for native X6 Cell/Link/Port or for physical heartbeat durations. P000, joint-relation observer preservation and the frozen science pin are unchanged.

Existing mathematics reused: PREFIX-829 first-separation theorem and delay-lift, PREFIX-830 size-nine ideal PTE witness. New part: explicit **two-stage overlap cancellation**, finite positive 16-source step-eleven certificate, rigorous improved bound and independent labelled-state verification. Related classical mathematical provenance retained from PREFIX-830 (Prouhet–Tarry–Escott problem); no claim that the seed PTE solution is original.

**Open:** establish whether a step-eleven ideal 11-source PTE witness exists, or improve `11 <= p_min(11) <= 16` to 12–15 by a different construction; study simultaneous source count and maximum weight, and which addressed-source observers detect distinctions earlier. Independently retain the q>=5,b>0 positive Q-carrier question and native X6 event-licensing bridge. 
