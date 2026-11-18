# PREFIX-893 — Exact disjoint collision certificates for 16 complete strict-19-bit rows

Date: 2026-11-18 (Asia/Shanghai). Project: Enterprise Math / BRC named-source observation auxiliary. Frozen scientific-input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessors: PREFIX-882/883 (general collision index/count); PREFIX-887/888 (axis collision); PREFIX-891 (ZF endpoint); PREFIX-892 (dyadic positive completion). Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED**. This report is independent scientific analysis, not ownership or execution of the shared RS-X6-NATIVE-TIME-DYNAMICS Task.

## Exact model and scope

For `p=32`, `N=2^p`, let a legal named directed trajectory be a zero-step `Z_x=(x,x)` or a single named XOR flip `F^i_x=(x,x xor 2^i)`, with `0<=x<N`, `0<=i<p`. The ordered time-port observation is `Phi(s,t)=(s mod q1,t mod q2)`. The source label `i`, the zero/flip type and the order of both ports remain part of the trajectory identity.

Let `Q={262145,262147,...,524287}` (131,072 strictly 19-bit odd moduli). Fix `q1` at each of the sixteen axis-free integers:

`262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285`.

For every one of the **2,097,152 ordered pairs** in this exactly specified panel, a pair of distinct legal trajectories with identical observations has been explicitly constructed.

## Theorem 893-A: complete finite disjoint classification

The first-success classification is defined **in this exact order**:
1. `ZF`: PREFIX-891 endpoint test finds a zero-step/one-flip collision, with direct witness.
2. `positive_completion_only`: PREFIX-892 gives `kq1+ell q2=2^p` and two highest-source FF trajectories.
3. `zero_step_only`: `L=lcm(q1,q2)<N`; witnesses `(0,0)` and `(L,L)`.
4. `zero_anchored_ff_only`: a congruence candidate gives `(0,2^i)` and `(a,a xor 2^j)` with `a=kq1`, both flipping one named bit, and equal observations.
5. `general_ff_dp`: use the full signed two-flip CRT search and exact binary carry-DP described below, constructing `(x,x+d)` and `(x+a,x+a+e)`.

The exhaustive C++17 program `PREFIX893_R6_FULL_PANEL_EXCLUSION.cpp`, compiled with assertions enabled, enumerates every pair and implements categories 1-4. It serializes the complete row counts and the **exact 67 otherwise unresolved pairs** in `PREFIX893_R6_PANEL_EXCLUSION_PRECERT.json`. The Python3 program `PREFIX893_R6_REMAINDER_FF_DP.py` applies category 5 to **all 67**, returning and verifying one actual XOR trajectory pair for each in `PREFIX893_R6_FULL_PANEL_CERTIFICATE.json`. Therefore the entire panel is collision-positive in the specified finite model.

| First applicable certificate | Disjoint ordered pairs |
|---|---:|
| Zero/flip endpoint | 1,308,292 |
| Dyadic positive-completion FF (not ZF) | 10,386 |
| Two zero steps (neither previous) | 15,250 |
| Zero-anchored FF (none above) | 763,157 |
| General FF carry-DP (none above) | 67 |
| **Total** | **2,097,152** |

The sum is exactly `1,308,292+10,386+15,250+763,157+67=2,097,152`. A pair belongs to precisely one first-success category. In the final 67 cases the computed witness passes explicit start/end range, named XOR, distinctness and two modular-observation equality assertions. This is a **complete negative certificate for the chosen 16-row 19-bit panel**: no observation-injective ordered modulus pair exists in that panel. No global conclusion about all 131,072 possible q1 values follows from only sixteen rows.

## Theorem 893-B: complete zero-anchored FF candidate index under lcm>=N

Write `g=gcd(q1,q2)`, `M=q2/g`, `K=floor((N-1)/q1)`. If `lcm(q1,q2)=q1*M>=N`, then `M>K`. For every `i,j in {0,...,p-1}`, seek a collision between

`X=(0,2^i)`, `Y=(a,a xor 2^j)`, `a=kq1`, `1<=k<=K`.

If bit j of a is 0, the second XOR delta is `+2^j` and its congruence is `kq1 equiv 2^i-2^j (mod q2)`. If bit j of a is 1, the delta is `-2^j` and the congruence is `kq1 equiv 2^i+2^j (mod q2)`. Accordingly `g` must divide the relevant right-hand side `D`. As `q1/g` is invertible modulo `M`, there is exactly one modular residue candidate:

`k0 = (D/g) * inverse(q1/g mod M) (mod M)`, `0<=k0<M`.

Since `M>K`, a valid `k` exists **if and only if** `1<=k0<=K` and the declared bit j condition on `a=k0q1` holds. All endpoint and modular assertions then hold automatically or are checked explicitly. Thus under `lcm>=N`, checking all 2p² signed candidate combinations is **complete for this zero-anchored FF family**. This theorem does not assert completeness for all FF collisions.

If `lcm<N`, category 3 already provides an exact zero-step witness; thus the condition `M>K` is guaranteed on every entry reaching category 4.

## Theorem 893-C: exact general two-source FF carry test

Assume `lcm(q1,q2)>=N`, hence `M>K`. Put `d=s_i2^i`, `e=s_j2^j`, where `s_i,s_j in {+1,-1}`. Let `a=kq1` with `k>=1`. A collision between

`X=(x,x+d)`, `Y=(x+a,x+a+e)`

must satisfy `kq1 equiv d-e (mod q2)`. It therefore has at most one candidate `k` for fixed `i,j,s_i,s_j`, found by CRT modulo `M`, subject to `g|(d-e)` and `1<=k<=K`.

For that `a`, perform a p-bit carry automaton for adding `x+a`. At bit `h`, choose the bit `x_h in {0,1}`; update the carry by the exact sum `x_h+a_h+carry_h`. Require `x_i=0` if `s_i=+1` and `x_i=1` if `s_i=-1`. Simultaneously require the resulting bit `(x+a)_j=0` if `s_j=+1` and 1 otherwise. Require zero final carry (so `0<=x,x+a<N`). Maintain one minimal representative `x` for each carry. This DP is **necessary and sufficient** to find a valid base state for fixed `a,i,j,s_i,s_j`, in O(p) small-integer state transitions. When it succeeds, all XOR rules and modular observations are verified directly.

The fourfold signed source search over `i,j` plus the DP is a complete decision procedure for FF collisions under `lcm>=N`, not merely the original zero-anchored family. Since any collision of two distinct trajectories is Z/Z, Z/F or F/F, the cascade has exhaustive type coverage for every specified input pair. The final 67 use this full procedure and each yields an actual witness.

One residual case: `q1=262147, q2=425987`, `k=13`, `a=3407911`, `i=0`, `j=4`, `d=-1`, `e=-16`, `x=17`. The trajectories

`X=(17,16)`, `Y=(3407928,3407912)`

are each a legal named flip, distinct, and obey `Phi(X)=Phi(Y)`.

## Reproducibility and source evidence

- `PREFIX892_R6_DYADIC_COMPLEMENT_CENSUS.cpp`: earlier independently checked dyadic construction and modular inverses, imported by the next C++ source.
- `PREFIX893_R6_FULL_PANEL_EXCLUSION.cpp`: full specified 16 x 131072 ordered pair enumeration and exact disjoint-first-hit counters, with assertions for actual witnesses. Compile as `g++ -O2 -std=c++17 PREFIX893_R6_FULL_PANEL_EXCLUSION.cpp -o prefix893`. Run `./prefix893 > PREFIX893_R6_PANEL_EXCLUSION_PRECERT.json`. Compile without `-DNDEBUG`.
- `PREFIX893_R6_REMAINDER_FF_DP.py`: from that JSON, reconstruct all 67 exact FF witnesses; checks 13,432 p=2..6 fixed-candidate DP cases against direct state enumeration. Run `python3 PREFIX893_R6_REMAINDER_FF_DP.py PREFIX893_R6_PANEL_EXCLUSION_PRECERT.json > PREFIX893_R6_FULL_PANEL_CERTIFICATE.json`.
- Both named JSON certificates preserve exact row membership, totals, all 67 residual modulus pairs and 67 full witnesses. All arithmetic is exact integers; there is no floating point.
- Prior PREFIX-892 C++17/Python3 independently agreed on every one of its 16 complete rows. This run's PREFIX-893 full disjoint cascade is one exhaustive C++ implementation, separately crosschecked for its last 67 cases with the Python DP and 13,432 direct small tests; this is not an independent end-to-end second implementation of all five PREFIX-893 categories.
- Source publication via GitHub `main` with each scientific artifact compared to its immutable GitHub blob readback. Author proof and exact finite enumeration are retained as distinct evidence components. No Lean/formal checker or independent reviewer has been applied.

## Scientific frontier and state

The 16-row panel is **completely eliminated** for observation-injective 19-bit ports in the frozen named-transition model. For a global decision of `B_fix,odd(32) in {19,20}`, advance to the remaining first-port values in `Q` with exact structured row certificates, preserving duplicate-free evidence. Test the full two-source criterion on survivors after inexpensive ZF/axis/zero-step/zero-anchored tests; analyze whether a parameterized proof can replace exhaustive per-pair checking. Do not silently replace the frozen observer, P000 native space or independently owned RS-X6 native time frontiers. Activity linkage is a separate control bookkeeping item.
