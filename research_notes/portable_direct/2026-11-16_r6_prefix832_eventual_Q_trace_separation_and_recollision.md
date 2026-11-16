# PREFIX-832 — Exact all-time Q-trace separation, persistent observers and a transient recollision

**Date:** 2026-11-16. **Status:** AUTHOR_PROVED / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.  
**Scientific freeze:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Continue PREFIX-827/829/830/831. This is the positive, unnormalized, named-source auxiliary BRC counting model, not native X6 Cell/Link/Port event licensing or physical time.

## Scope and precise source model

There are `p>=1` initially present, distinguishable unmarked sources, each removable once with positive integer weight `w_i`; capacity is `q=p`; the distinguished marked source is initially absent. Each `Q=R+A` step is the sum of all legal weighted operations: remove one present unmarked source with its weight, remove the mark with weight `b>0`, or insert an absent mark with weight `a>0` when capacity permits. Distinct legal operation histories contribute additively with positive integer mass. Observer `Y_l(t;W)` counts the full mass ending at occupancy `l` after `t` Q steps, for `l=0,...,p`. The only signed quantities below are *differences between two positive masses*.

For equal-cardinality positive weight multisets `A,B`, let `e_d(W)` be elementary symmetric functions, `e_0=1`, `Delta_d=e_d(A)-e_d(B)` (also set `Delta_0=0`), and `lambda=ab`. Assume `A != B` as multisets and set `n=min{d>=1:Delta_d!=0}` and `D=max{d>=1:Delta_d!=0}`. Both are in `[1,p]`.

## Theorem 832.1 — Closed formula for every future difference bin

For `t=0`, all histogram differences are zero. For each `t>=1` and `l=0,...,p`,

```text
Delta Y_l(t) =
  sum over 1<=d<=min(p,t) and m in {0,1}
    with l=p-d+m, r=(t-d-m)/2 a nonnegative integer:
      d! * Delta_d * C(t-1,d-1) * a^(r+m) * b^r .
```

In particular the first difference occurs at `t=n`, solely in occupancy `p-n`, and equals `n! Delta_n` (recovering PREFIX-829). This formula specifies *all* subsequent separations and possible re-collisions, not merely the first.

**Proof.** Every positive-length history starts with an unmarked removal, since the initially absent mark cannot be inserted at saturated capacity. If exactly `d>=1` unmarked sources are removed, their ordered, weighted selection sums to `d!e_d(W)`. A marked-source operation sequence alternates insert/remove, starting with insertion; it has `r+m` insertions, `r` removals and final mark flag `m in {0,1}`. After the compulsory first source removal, the remaining `d-1` unmarked removals can be interleaved with those `2r+m` prescribed alternating marked operations in precisely `C(t-1,d-1)` ways. All interleavings are legal: source removal only lowers occupancy, and the first removal creates room for any later insertion. The final occupancy is `p-d+m`. Sum over `d,m` and subtract the two weight profiles. QED.

## Theorem 832.2 — An exact eventual-separation certificate

For each `t>=D` with `t-D` even, the histogram coordinate at occupancy `p-D` is

```text
Delta Y_(p-D)(t) = D! * Delta_D * C(t-1,D-1) * lambda^((t-D)/2) != 0.
```

For `D>=2` and `t=D+1+2r` (`r>=0`), the coordinate at occupancy `p-D+1` is

```text
Delta Y_(p-D+1)(t) =
  D! * Delta_D * C(t-1,D-1) * a * lambda^r
  + (D-1)! * Delta_(D-1) * C(t-1,D-2) * lambda^(r+1).
```

Factoring the nonzero positive integer `(D-1)! * C(t-1,D-2) * a * lambda^r` leaves the affine function

```text
(D * Delta_D * (t-D+1))/(D-1) + b * Delta_(D-1).
```

Since `Delta_D!=0`, this expression vanishes for **at most one** eligible odd-parity time `t>=D+1`. If `D=1`, the second contribution is absent, and the trace differs at every `t>=1`.

**Therefore any two distinct equal-size positive source-weight multisets have different complete Q histograms at every sufficiently large integer step; for `t>=D`, at most one step can have an equal full histogram.** A possible exceptional time must equal

```text
t* = D-1 - ((D-1) * b * Delta_(D-1)) / (D * Delta_D)
```

and must be an integer `>=D+1` of parity opposite to `D`. This criterion is necessary for an exceptional full-histogram coincidence, not sufficient in general: other bins must also vanish.

**Proof.** In the first selected bin only `d=D,m=0` and potentially `d=D+1,m=1` contribute; the latter has `Delta_(D+1)=0`. In the second selected bin only `d=D,m=1` and `d=D-1,m=0` contribute. Substitute Theorem 832.1 and use `C(t-1,D-1)/C(t-1,D-2)=(t-D+1)/(D-1)`. The affine factor is nonconstant, so has at most one zero. The `D=1` case is immediate from Theorem 832.1. QED.

**Ideal PTE corollary.** If `p=n` and `Delta_1=...=Delta_(n-1)=0`, then `D=n` and the entire histogram difference at every `t>=n` has exactly one nonzero bin. Put `m=(t-n) mod 2` and `r=floor((t-n)/2)`. It is

```text
Delta Y_m(t) = n! * Delta_n * C(t-1,n-1) * a^(r+m) * b^r !=0.
```

Thus an ideal delayed-observation pair, once distinguishable, is distinguishable at **every** later Q step. For nonideal `p>n`, the higher elementary coefficients govern later mixing.

## Theorem 832.3 — Integer separation quantization

For integer weights `A,B` with the first `n-1` power sums equal, the first differing elementary coefficient is divisible by `(n-1)!`, and the first full-histogram difference `n! Delta_n` is divisible by `n!(n-1)!`. More precisely, write

```text
F(z) = sum_{x in A} z^x - sum_{y in B} z^y.
```

Then `F(z)=(z-1)^n H(z)` for some `H(z) in Z[z]` (positive weights). Equality of moments of degrees `0,...,n-1` ensures the order of vanishing; division by the monic integer polynomial `(z-1)^n` stays integral. The power sum difference is `Delta s_n=n!H(1)`. Newton's identities give `Delta_n=(-1)^(n-1)(n-1)!H(1)`. This is an exact integer divisibility constraint useful for filtering proposed source certificates, not a lower bound on their cardinality.

For PREFIX-831's 16-source certificate, `n=11`, `Delta_11=386647617821617152000 = 10! * 106549718315040`; hence its step-eleven difference is an integer multiple of `11!10!`.

## Exact counterexample 832.4 — A genuine one-step recollision

Take `p=q=2`, `a=2`, `b=12`; `A=(1,6)`, `B=(3,3)`. Then `Delta_1=1`, `Delta_2=-3`, so `n=1`, `D=2` and the candidate `t*=3` is integral and admissible. Direct named-state enumeration gives complete occupancy histograms in bin order `(0,1,2)`:

| step | Y(t;A) | Y(t;B) |
|---:|---|---|
| 0 | (0,0,1) | (0,0,1) |
| 1 | (0,7,0) | (0,6,0) |
| 2 | (12,0,14) | (18,0,12) |
| 3 | (0,216,0) | (0,216,0) |
| 4 | (864,0,336) | (1296,0,288) |
| 5 | (0,6336,0) | (0,6912,0) |

The observers separate at step 1, coincide *again* at step 3, and separate thereafter. Hence the one-exception allowance in Theorem 832.2 cannot generally be removed.

## Verification and provenance

`PREFIX832_R6_Q_TRACE_SEPARATION_CHECK.py` independently enumerates every legal named-subset and marked-flag weighted transition, rather than using the closed formula as its dynamics. It compares all histogram coordinates against the exact combinatorial formula for ideal PTE certificates of sizes 7, 10 and 12, the nonideal 16-source PREFIX-831 certificate, and the two-source recollision. Parameters `a=2,b=3` for the first four, `a=2,b=12` for the counterexample. The range is `t=0..16` (size 7), `0..17` (sizes 10,12,16), and `0..7` (size 2): **898 exact scalar histogram comparisons and 11,962,406 independently executed named-state transition updates**. Assertions include the first-separation step, all-time formula, highest-difference witness and the step-three recollision. All passed with standard Python exact integers; the universal theorems rest on the proofs above.

Inputs and antecedents: PREFIX-827 exact Q trace counting, PREFIX-829 PTE observer criterion, PREFIX-830 ideal size-7/10 witnesses, PREFIX-829 ideal size-12 witness, and PREFIX-831 16-source bound. All named sources and observer operations remain within the declared auxiliary positive-weight BRC type. No inference about physical heartbeat duration, native X6 events, separately addressable source words, shared-task Result/Review, or Foundation admission is made.

**Next discriminating problems:** For nonideal `p>n`, classify when the single allowed exceptional recurrence time makes *all* bins equal (not merely the extremal witness); derive minimal readout coordinates to avoid such temporary blindness; pursue ideal size-11 PTE or new `p<=15` certificates, and independently the `q>=5,b>0` minimal nonnegative Q carrier.
