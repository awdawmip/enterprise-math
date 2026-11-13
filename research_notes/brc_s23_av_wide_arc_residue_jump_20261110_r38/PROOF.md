# R38 — Exact modular-residue last-source selection in wide historical arcs

2026-11-10 · Author-side mathematical derivation + exact finite verification; independent mathematical review pending.

## Context and fixed scientific input

Continue R37 suffix saturation (PR #1955, immutable commit 1594ea1d17c876435e8bd166a52ecf9183bb6df9), inheriting R36 owner-labelled last-source definition and R29/R36 Floor Sum rank/select oracle. Frozen S23/AV science: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. This is an **auxiliary circle-rotation observer**. No assertion of native X6/BRC physical dynamics, no P000 change, no shared claim, Result or review authority.

## Theorem — wide-arc modular jump

Let irrational 0<θ<1, historical phases {aθ} for 0≤a<m sorted around the circle, and the m half-open circular arcs I_h=[α_h,β_h). Let the source window be [j−N,j), N≥1, with per-arc last source

τ_h(j,N)=max{t∈[j−N,j): {tθ}∈I_h},

with τ_h=⊥ for no hit. Select integers p,q, q≥1, with D=qθ−p≠0 and d=|D|<1. Assume each historical arc has circular length λ_h≥d.

Partition backwards ages r=1,...,N into residue classes r=s+kq, s=1,...,min(q,N), k=0,...,K_s=floor((N−s)/q). Define t_s=j−s and x_s={t_sθ}. Then phases satisfy

{(j−s−kq)θ}={x_s−kD}.

For each arc I_h and residue s, the **earliest eligible k** (hence latest source in that residue) is exactly:

* x_s∈I_h: k_h(s)=0.
* x_s∉I_h and D>0: k_h(s)=floor( { (t_s−b_h)θ } / d )+1, where β_h={b_hθ}.
* x_s∉I_h and D<0: k_h(s)=ceil( { (a_h−t_s)θ } / d ), where α_h={a_hθ}.

The different floor/ceiling treatment is essential. In the positive case the right boundary β_h is excluded; in the negative case the left boundary α_h is included.

The exact last source is

τ_h(j,N)=max_{s:1≤s≤min(q,N), k_h(s)≤K_s}(j−s−qk_h(s)).

The empty maximum yields ⊥. This preserves the full original owner label h.

**Proof.** Each fixed-residue phase moves by a signed circular step D. Suppose D>0. If x_s begins outside I_h, in the clockwise direction it first approaches the excluded upper boundary β_h at clockwise distance z={(t_s−b_h)θ}. For integer k≤floor(z/d) it has not entered I_h; at k=floor(z/d)+1 it lies on the clockwise segment (β_h−d,β_h], excluding β_h itself (if z is a multiple of d, the extra step is necessary). Since λ_h≥d, the new phase belongs to I_h. If D<0 the movement is counterclockwise toward the **included** lower boundary α_h, and k=ceil(z/d) is precisely the first arrival or crossing; the next phase is at most d from α_h and therefore inside I_h. Both arguments use lifted circular order, so they also cover arcs crossing zero. The least k corresponds to greatest source t within its residue; taking the maximum across all residues yields τ_h. □

**Cost.** After sorting m historical phases in O(m log m) comparisons, evaluate at most q*m residue/arc candidates and O(q) first-owner classifications. The number of exact rational operations is independent of N; integer bit cost still depends on j,N,θ representation and each rational division. The method is useful for small q and arbitrarily large partial quotient near p/q. If λ_min<d, use R37 saturated suffix or R36 Floor Sum selector instead.

## Proof-certified irrational interval

Represent θ by a strict rational enclosure [L,U]. Historical order is fixed when floors of all nonzero differences of historical indices agree at both ends. The arc length is then an affine fractional-part expression in θ. Confirm sign(qθ−p) and λ_h(θ)≥|qθ−p| at L and U: the difference is affine on the enclosure, establishing the premise throughout.

For each starting x_s verify its owner by the floors for its two historical boundaries. For each nonzero candidate put v=t_s−b_h (D>0) or v=a_h−t_s (D<0); floor(vL)=floor(vU) fixes the fractional-part branch. The quotient frac(vθ)/|qθ−p| is linear fractional and monotone or constant on the enclosure. Equality of the endpoint floors (D>0), respectively endpoint ceilings (D<0), proves the selected k is constant for **all** θ in that enclosure. Exact endpoint checks therefore certify all labels and candidate cutoffs, not just the rational midpoint.

## Executed exact verification

A standalone Python Fraction/isqrt checker (VERIFY_R38.py) implements this formula, certifies rational-enclosure branch stability and checks complete last-source vectors against a separate per-arc Floor Sum binary-search oracle. Its complete certificate is in CERTIFICATE_R38.json. The exact experimental summary is:

| θ family | m | p/q | candidate checks | independent Floor Sum queries | outcome |
|---|---:|---:|---:|---:|---|
| 1/3+√2/10^7, j=10^9, N=10^8 | 21 | 1/3 | 63 | 581 | equal 21/21 |
| same, j=10^12, N=10^9 | 21 | 1/3 | 63 | 650 | equal 21/21 |
| same larger historical set | 63 | 1/3 | 189 | 1949 | equal 63/63 |
| 2/7+√2/10^8 | 31 | 2/7 | 217 | 858 | equal 31/31 |
| same larger set | 70 | 2/7 | 490 | 2165 | equal 70/70 |
| 1/3−√2/10^7 | 21 | 1/3 | 63 | 650 | equal 21/21 |
| √2−1 | 16 | 5/12 | 192 | 496 | equal 16/16 |
| frozen S23/AV | 128 | 43/164 | 20992 | 3960 | equal 128/128, slower option |
| √2−1 | 16 | 2/5 | — | — | premise correctly fails |

Eight applicable parameter/window cases, 94 additional brute-force finite-window regressions all pass. Counts compare different exact operation kinds; no measured time speedup is asserted. The S23 result validates an alternate last-source selector only, **not** a rerun of its 298-run trillion-horizon risk table. The upstream 298-run digest remains 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6.

## Open unit

Remove the wide-arc restriction λ_min≥|qθ−p| when a small modular step can skip a narrow historical interval. Seek an exact Ostrowski/continued-fraction return-map first hit with a full bit-cost analysis; test counterexamples to naive one-revolution shortcuts. Preserve source/arc labels and use R36 Floor Sum as independent oracle. Mathematical independence review and any native X6/BRC bridge remain pending.