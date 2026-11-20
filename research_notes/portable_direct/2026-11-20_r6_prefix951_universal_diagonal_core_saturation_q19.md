# PREFIX-951 — Universal diagonal saturation of the named XOR odd-core certificates

Date: 2026-11-20. Research line: R6, standalone portable mathematical output. Frozen scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`; source predecessor PREFIX-950 at `b0940239212ac57b174944601e6943dcb019f3f5`. Historical original researcher provenance `EM-DIRECT-58C410`, SID `MCP-31edc522830749ad8775ca012e02ef30`, Activity `RA-25432C4AAE9BF66A907F5115`. No new shared CLAIM. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Object and source preservation

In the auxiliary **named-XOR two-port** model, the two distinct histories `F_0^i=(0,2^i)` and `F_(ka)^j=(ka,ka XOR 2^j)` yield the same first-port residue modulo `a`. For the diagonal ordered pair `(a,b)=(a,a)`, they yield identical second-port residues precisely when the positive quotient equation

`(ka XOR 2^j)-2^i=t a`, `t>=1`, `0<=i,j<=p-1`

holds, and both traces fit in the stated state range. The bit names i,j and the original histories are retained. This diagonal slice does not describe native six-axis X6 dynamics, a typed BRC computation, or the complete off-diagonal collision population.

## Exact diagonal classification (arbitrary bit width)

**Theorem.** Let `p>=3`, `M=2^p`, `H=M/2`, `Q_p={H+1,H+3,...,M-1}`, and k be a positive odd integer. Work in an unbounded integer trace model, or assume the corresponding trajectories are legal. Define the unique residue

`e_p(k)=(-k^{-1}) mod M`, `0<=e_p(k)<M`.

Then the diagonal pair (a,a), a in Q_p, has a named collision witness if and only if one of the following holds:

(A) `a != e_p(k)`; or

(B) `a=e_p(k)=H+1` and `k ≡ H-1 (mod M)`.

When (B) holds, a witness is `i=p-1, j=0, t=k-1`. In all (A) cases an explicit witness is `i=j` at any zero bit j of `ka mod M`, with `t=k`.

**Proof.** If `ka mod M != M-1`, some source bit j in [0,p-1] is zero. Then `ka XOR 2^j = ka+2^j`; selecting i=j gives t=k. Conversely, if all these bits equal one, then `ka XOR 2^j=ka-2^j` and an integer quotient requires `a | (2^i+2^j)`. For i=j this positive sum is a power of two, impossible for odd a>1. For i!=j write `2^i+2^j=2^u(1+2^v)` with `u=min(i,j)`, `1<=v<=p-1`; odd a divides `1+2^v <= H+1 <= a`. Hence necessarily `a=H+1`, `u=0`, `v=p-1`. The condition `ka ≡ -1 (mod M)` becomes `k ≡ -a^{-1} ≡ H-1 (mod M)` because `(H+1)^2 ≡ 1 (mod M)`. Conversely that congruence gives `ka ≡-1`; with j=0, i=p-1, the difference is `ka-(H+1)=(k-1)a>0` (k>=3). Every other all-ones candidate fails. QED.

## Full strict Q19/32-bit corollary and all-core saturation

Put p=19, Q19={262145,262147,...,524287}, and the 32-bit state interval [0,2^32). Consider **all 4096 odd cores k in [1,8191]**. All named histories used by the theorem are legal uniformly, since

`8191*524287 + 2^18 = 4294696961 < 4294967296`.

The rescue core residue `H-1=262143` is outside [1,8191]. Thus **exactly one** diagonal modulus fails W_k if `e_19(k) in Q19`; otherwise all 131072 diagonals are in W_k. For distinct k in [1,8191], their exceptional residues are distinct by modular invertibility. Consequently, for ANY finite core family K in this range,

`|{(a,a): a in Q19, (a,a) in W_k for every k in K}| = 131072 - |{e_19(k):k in K} ∩ Q19|`.

For the entire K={1,3,...,8191}, an exact modular-inverse census gives **2051 distinct exceptional moduli**, hence

`|diagonal intersection of all 4096 W_k| = 131072 - 2051 = 129021`.

This means **at least 4095 of the 4096 odd cores certify each diagonal**, while 129021 diagonals are certified by *every* core. As a specific precedent check: `e_19(21)=274627` lies in Q19, while `e_19(23)=182361` does not; therefore the diagonal portion of `W21∩W23` is exactly **131071**, reproducing PREFIX-948's observed zero-offset diagonal count without enumerating intersection pair IDs. The previously reported 6203 additional off-diagonal pairs remain a separate computation.

## Exact verification and evidence scope

Two checker families are provided under the same folder.

1. C++17 O3 direct scanning tests all `4096*131072=536870912` (core,a) combinations for the all-one-bit exception, computes an independent Newton modular inverse for each k, compares the omission sets, and validates **1,048,571** explicit named-bit witness instances for eight representative cores. Output: `PREFIX951_R6_Q19_CORE_SATURATION_CPP_RESULTS.json`; all assertions passed. Wall observation on this execution environment: 0.48 seconds, peak RSS 1536 KiB, not a general benchmark.
2. Independent Python `pow(k,-1,2^19)` census checks 2051 and 129021. It also directly exhausts all i,j and positive quotients for p=3,...,8, every odd k in [1,2^(p+1)-1], all odd a in Q_p: **504 (p,k) cases**, including the exceptional rescued case `p=7,k=63,a=65` with t=62. Output: `PREFIX951_R6_INDEPENDENT_RESULTS.json`; all assertions passed.

Finite computation establishes the numerical 2051 census and supports the general proved classification; no external theorem acceptance is claimed. Counted objects are diagonal ordered moduli, not a new certificate-union increment. Previously reported conditional complete-pair union `7597037839` is unchanged.

## Relevance and next open question

The exact core-universal diagonal is an aggressively reusable, provenance-preserving baseline. For full adjacent-core intersections, remove this **known** diagonal contribution first and count only `a!=b` determinant-nonzero candidates, while separately retaining source-bit and quotient witness multiplicities. Test a CRT/floor-sum count of those off-diagonal pairs against the previously verified `W21∩W23` value 6203. This paper claims no direct progress on the still-open mother objective `B_fix,odd(32) in {19,20}`, and no formal Result, independent Review or shared X6 completion.
