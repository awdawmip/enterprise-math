# PREFIX-952 — Exact named diagonal witness multiplicities and floor-sum first moments

**Date:** 2026-11-20. **Scientific pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Exact predecessors:** [PREFIX-951](https://github.com/awdawmip/enterprise-math/blob/989ff20b7377d1f80e0042a6d5865ad8423e535e/research_notes/portable_direct/2026-11-20_r6_prefix951_universal_diagonal_core_saturation_q19.md) (existence classification); [PREFIX-948](https://github.com/awdawmip/enterprise-math/blob/89869c424e51e943733d1f4e7991ec9e51db8597/research_notes/portable_direct/2026-11-20_r6_prefix948_resonance_determinant_joint_census.md) (two-core resonance regression). The preceding source provenance is R6 `EM-DIRECT-58C410` / historical SID `MCP-31edc522830749ad8775ca012e02ef30` / historical Activity `RA-25432C4AAE9BF66A907F5115`. This independent scientific note does not claim the historical private capability or a new Task CLAIM. Status: **AUTHOR_PROVED / EXACT_INTEGER_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED**.

## Model

Auxiliary named-XOR two-port observer, not a native signed-X6 or typed-BRC theorem. Fix any integer p≥3; H=2^(p−1), M=2^p and Q_p={H+1,H+3,…,M−1}. Fix an odd 1≤k<H and a∈Q_p. Let w_p(k,a) count distinct ordered *named source-bit pairs* (i,j)∈{0,…,p−1}² for which a positive integer t satisfies

```
       (k*a XOR 2^j) - 2^i = t*a.                     (1)
```

Each valid (k,a,i,j) determines t uniquely. Original source/port and bit names are retained. Theorem is in the unbounded trace model or any state bound permitting all named histories.

## Theorem 1 — COMPLETE classification of every named diagonal witness

Let Z_p(k,a)=p−popcount((k*a) mod M), the number of zero bits at positions 0…p−1. Then

```
 w_p(k,a) = Z_p(k,a) + 2 * [a=H+1] * [k>=3].         (2)
```

The complete (i,j,t) list is (j,j,k) for each zero bit j of k*a, and, when a=H+1 and k≥3, exactly two extras (0,p−1,k−1) and (p−1,0,k−1).

**Proof.** Write v=ka. If its bit j is zero, XOR adds 2^j, and (1) is (k−t)a=2^i−2^j. Since |2^i−2^j|≤H−1<a, this is possible precisely when i=j, t=k. If its bit j is one, XOR subtracts 2^j, and (k−t)a=2^i+2^j. Since 0<2^i+2^j≤2H<2a, a must equal this sum and t=k−1 must be positive. Because a is odd, exactly one of i,j equals zero, and a≥H+1 forces the other index to equal p−1. Thus a=H+1. Conversely, for odd k<H, k(H+1)≡H+k (mod M), so bits 0 and p−1 of k(H+1) are both one. Both extra source pairs work for k≥3. The classification is exhaustive. □

The extra witnesses at a=H+1 exist even when other zero-bit witnesses already exist. This strictly refines PREFIX-951, which settled the Boolean existence condition.

## Theorem 2 — exact O(log M) arithmetic-step first moment

Let N=H/2 and define the integer floor sum F(n,m,u,v)=Σ_(r=0)^(n−1) ⌊(ur+v)/m⌋. Put

```
B_p(k) = F(N,H,2*k,k*(H+1))
       - 2*F(N,2*H,2*k,k*(H+1)).
S_p(k) = sum_(a in Q_p) w_p(k,a).
```

Then B_p(k) counts the moduli in Q_p with bit_(p−1)(ka)=1, and

```
S_p(k) = (p−2)*N/2 + N − B_p(k) + 2*[k>=3].       (3)
```

**Proof.** Every ka is odd, so bit 0 is always one. For each j=1,…,p−2, the consecutive odd moduli in Q_p visit each odd class mod 2^(j+1) equally often; multiplication by odd k permutes these classes. Therefore precisely N/2 have bit j zero. The binary identity bit_(p−1)(x)=⌊x/H⌋−2⌊x/(2H)⌋ for nonnegative x, with a=H+1+2r, proves the expression for B_p(k). The two extra witnesses are the last term. Euclidean floor-sum computes F using logarithmically many integer arithmetic steps, with input-size-dependent bit complexity. □

## Exhaustive strict-Q19 / 32-bit finite result

Set p=19, a∈{262145,262147,…,524287} (131072 moduli), and odd k∈[1,8191] (4096 cores). All named trace endpoints fit in 32 bits since 8191*524287+2^18=4294696961<2^32.

| Exact quantity | Result |
|---|---:|
| Core/modulus configurations | 536,870,912 |
| **Total named diagonal source-pair witnesses** | **4,831,509,378** |
| Ordinary zero-bit source witnesses | 4,831,501,188 |
| Additional smallest-modulus sources | 8,190 |
| Sum across cores of top-zero counts | 268,098,436 |
| Configurations with zero witnesses | 2,051 |
| Maximum named sources for one (k,a) | 18 |

Complete count histogram for witness multiplicity w=0,…,20:

```
[2051,36888,313067,1672848,6273853,17550161,
 38030573,65205329,89635646,99573331,89596342,
 65145281,38007559,17544795,6260479,1669917,
 313829,36906,2057,0,0]
```

The exactly 2051 witness-free configurations agree with PREFIX-951's modular-inverse exceptions. The total 8190 additional sources equals 2*4095.

**Independent previous-result regression.** For k=21 and k'=23 the rank-one resonant witness multiplicity is

```
Σ_(a∈Q19) Z_19(21,a) * Z_19(23,a) = 10,541,739.
```

The C++ scan exactly reproduces PREFIX-948's resonant witness total and 131071 common positive-zero-bit diagonals. The two exceptional extra witnesses with c≠0 are not rank-one resonant and must not enter this product.

## Verification and reproducibility

* C++17 direct full scan computes the popcount-predicted multiplicity, full per-core CSV, histogram, total, and k21/k23 regression over all 536870912 (k,a). Observed standalone run 1.89 s, peak RSS about 1.6 MiB; compilation and total input-preparation time excluded.
* Independent Python uses Euclidean floor_sum for **all 4096** per-core totals and matches the C++ CSV one by one. It additionally enumerates **all source pairs (i,j) and positive t** in the original equation for p=3,…,8, every odd k<H and every a∈Qp: 126 different (p,k) parameter cases. All checks passed. Exception (p,k,a)=(7,63,65) gives exactly the two witnesses (0,6,62) and (6,0,62).
* Full original source, CSV, exact JSON outputs, SHA-256 manifest and independent reimplementation are preserved in the separately verified PREFIX-952 reproduction package. No floating-point or stochastic calculations; general Theorems 1–2 are proved and the Q19 aggregates are exact finite integer computations.

## Scope and next problem

This theorem measures *labeled witness multiplicity*, not new distinct modulus-pair coverage. Prior conditional certificate union remains 7,597,037,839; mother objective B_fix,odd(32)∈{19,20} remains open. The result exhibits a concrete observer-information loss: Boolean pair support does not determine resonant named-witness counts. Next, use the exact labeled zero-bit multiplicity carrier to subtract rank-one diagonal contributions and attack the **6203 distinct off-diagonal** W21∩W23 pairs with grouped determinant/CRT arithmetic. Preserve original source-bit provenance and separate the author proof, finite computation, independent review and formal Source admission.
