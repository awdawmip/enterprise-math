# R146C — Exact endpoint-divisor flow of total phase-index mass

Date: 2026-11-14 Asia/Shanghai.
Scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`, unchanged.
Scope: external scalar tied-phase S23 observer, `m>=1,K>=2`; independent review NOT_REVIEWED.
Direct predecessor: R145 total fiber conservation, and R146 exact wordwise fibers, in the immutable cited research line.

Let `L=K-1>=1`. Write `S_m(L)=sum_{w in W_m} C_w(L+1)` for the total number of distinct nonempty integer phase-index/word blocks. For Euler's totient `phi` define the **truncated joint-divisor mass**
[
 D_m(n)=sum_{substack{2le qle m\qmid n}}arphi(q).
]

## R146C.1 — Two-endpoint exact flow theorem

For every `m>=1,L>=1`:
[
 oxed{S_m(L+1)-S_m(L)=m+1+D_m(L)-D_m(L+m+1).}	ag{10}
]

**Proof.** R145's exact collision formula is
[
S_m(L)=(m+1)L+inom m2
-sum_{q=2}^{m}arphi(q)
left(leftlfloorrac{L+m}{q}ightfloor-leftlfloorrac{L-1}{q}ightfloor-1ight).
]
Subtract the formula at `L` from the formula at `L+1`. For each integer `q>=2`:
[
lfloor(L+m+1)/qfloor-lfloor(L+m)/qfloor=mathbf1_{qmid(L+m+1)},
]
and
[
lfloor L/qfloor-lfloor(L-1)/qfloor=mathbf1_{qmid L}.
]
All fixed terms cancel and (10) follows. QED.

This formula requires just the divisor membership tests for the two integers `L` and `L+m+1`, rather than enumerating the rational phase atoms. It retains composite divisors in the exact interaction count: no prime-only or observer-information reduction is performed.

## R146C.2 — Exact periodicity and first total-mass decrease

Let `P_m=lcm(1,...,m)`. Since `D_m(n+P_m)=D_m(n)` for all `n`, the increment sequence in (10) is periodic with period dividing `P_m`. Summing it over any `P_m` consecutive coefficients gives
[
oxed{S_m(L+P_m)-S_m(L)=(m+1)P_m.}	ag{11}
]
This also follows immediately from the collision formula, since every `q<=m` divides `P_m`.

For `m=1,2,3,4,5`, the minimum value of the step in (10) over every positive integer `L` is respectively `2,2,2,0,0`. These are *exact all-L statements*: exhaust all residue classes `L mod P_m`, with periods `1,2,6,12,60`. At `m=6,L=53`, `L+m+1=60`, `D_6(53)=0` and
`D_6(60)=phi(2)+phi(3)+phi(4)+phi(5)+phi(6)=1+2+2+4+2=11`. Hence
[
oxed{S_6(54)-S_6(53)=7-11=-4.}	ag{12}
]
The first word-length admitting a **decline of total phase-index mass** is therefore exactly `m=6`. A drop need not mean loss of a language word: (10) concerns all phase-index/word blocks, retaining multiplicity.

## Computational verification and status

The accompanying `check_r146c.py` tested (10) using two independent exact integer expressions for each of `m=1..50`, `L=1..500`: 25,000 comparisons, pass. It found `m=6,L=23` step `-2` and `m=6,L=53` step `-4`, agreeing with the historical R137 event-count nonmonotonicity. The all-L `m<=5` conclusion follows from explicitly enumerating a full period, not from extrapolating the `L<=500` window.

The universal theorem follows from symbolic floor differences; current findings are author-side mathematical results and exact finite computations. No native Task CLAIM or independent mathematical review is asserted.

## Next

Combine the per-word loss/recovery law of R146B with the total endpoint-divisor flow (10) to identify which negative aggregate steps arise from multiplicity reductions and which can coincide with missing Sturmian words near `E(m)`. Maintain the individual phase-index fibers when comparing against the complete word language.
