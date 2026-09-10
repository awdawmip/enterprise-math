# Reciprocal-phase candidate for the multiplicative memory field

Status: `RESEARCH_NOTE / FINITE_EVIDENCE / NOT_FOUNDATION / NOT_NOLLM_RUNTIME`

Date: 2026-09-11  
Research activity: `RA-nollm-multiplication-field-20260911-c6c82`

## Question

After publishing the multiplication-field workbench, hold fixed the integer population, the exact arithmetic carrier `v_p(n)`, `R(n)^2=n`, the display hex lattice and scale `C=1`, and change only the prime phase generators. Can an arithmetic rule approach the angular and cell-occupancy behavior of an independently scattered field without giving up exact multiplicative phase composition?

## BRC gate

`REUSE_APPLIED`: the sparse prime-valuation carrier from the multiplication lab is retained before any angular or cell observer.

Population: positive integers `1 <= n < N`, with zero carried separately.  
Branch identity: `v_p(n)`.  
Serial composition: multiplication, hence valuation addition.  
Observer: angular sectors/Fourier moments and derived display-cell occupancy.  
Future operations: multiplication, generator replacement, precision refinement.

No display-cell collision merges integer identities. Finite observer quality is not promoted to an asymptotic theorem.

## Candidate

For phase modulus `M=2^b`, define

`a_2=M/8`, and `a_p=p^{-1} (mod M)` for odd prime `p`, then

`phi_M(n)=sum_p v_p(n) a_p (mod M)`.

Thus `a_2/M=1/8`, i.e. multiplication by 2 receives a 45-degree generator, matching the dyadic-frame angle used in the Nollm geometry research. This observation does **not** make the rest of the candidate native Nollm geometry.

The multiplication law

`phi_M(ab)=phi_M(a)+phi_M(b) (mod M)`

is true by construction; it is not experimental evidence.

## 65,536-integer result

At `N=M=65,536`, 64 equal angular sectors and display scale `C=1`:

| phase rule | sector CV | occupied display hex cells | collision groups | max load |
|---|---:|---:|---:|---:|
| golden angle by prime rank | 0.1993828 | 47,491 | 11,009 | 9 |
| golden angle by prime value | 0.0591655 | 55,841 | 8,517 | 5 |
| **reciprocal + 45°** | **0.0294260** | **57,339** | **7,491** | **4** |

The reciprocal candidate uses 42,455 distinct phase ticks among 65,535 positive integers. Its largest absolute Fourier coefficient over harmonics 1 through 64 is about 0.01710.

Across sixteen consecutive 4,096-integer windows, its 64-sector CV lies in `[0.09738, 0.12938]`, with mean `0.11226`. The iid-uniform reference scale for 4,096 draws is `sqrt(63/4096) ~= 0.12403`. The golden-rank candidate has window maximum `0.58172`.

## Random-like reference, not a randomness claim

A deterministic SplitMix reference using 64 seeds on prime values and 64 seeds on prime ranks has mean sector CV about `0.0308` and mean occupied-cell count about `57,316`. The reciprocal candidate lies inside this random-like finite ensemble without a seed search.

The plane-area heuristic at `C=1` has display-lattice fundamental area `sqrt(3)/2`, hence mean cell intensity

`lambda=sqrt(3)/(2*pi) ~= 0.275664`.

A Poisson occupancy reference gives `(1-exp(-lambda))/lambda ~= 0.874006` occupied cells per source identity, about 57,279 occupied cells and 7,533 cells with load at least two. The reciprocal candidate gives 57,339 and 7,491. This is a diagnostic comparison, not proof that the deterministic field is Poisson.

## Resolution scaling

Repeating the rule with `N=M=2^m`, `8 <= m <= 16`, the sector-CV divided by the iid-uniform reference remains between about 0.68 and 0.95 in the finite table. At `m=16` it is 0.949.

More importantly, the phase modulus need not equal the population size. For `N=65,536`:

| phase bits | directions M | occupied ratio |
|---:|---:|---:|
| 9 | 512 | 0.76325 |
| 10 | 1,024 | 0.85631 |
| **11** | **2,048** | **0.87497** |
| 12 | 4,096 | 0.87418 |
| 16 | 65,536 | 0.87492 |

The visible transition is explained by the outer-circle angular spacing

`Delta s ~= 2*pi*C*sqrt(N)/M`.

Once this falls below roughly one display-cell spacing, increasing the number of phase directions no longer materially improves the observed occupancy in these tests. This suggests the finite engineering budget

`b ~= ceil(log2(2*pi*C*sqrt(N)/h)) = (1/2)log2(N)+O(1)`,

where `h` is the target display-cell spacing. This is a **sampling heuristic with finite support**, not a uniform theorem.

The same transition repeats at larger populations. For `N=1,000,001`, the predicted threshold is 13 bits:

| phase bits | outer arc spacing | occupied ratio |
|---:|---:|---:|
| 11 | 3.068 | 0.76555 |
| 12 | 1.534 | 0.85464 |
| **13** | **0.767** | **0.87268** |
| 14 | 0.383 | 0.87475 |

At 13 bits, 100 consecutive 10,000-integer windows have 64-sector CV mean `0.07701`, range `0.05994–0.09753`, versus iid reference `0.07937`.

With the original 16-bit modulus at `N=1,000,001`, the reciprocal candidate has overall CV `0.00724` and occupied ratio `0.87499`; golden-rank gives CV `0.06826` and occupied ratio `0.71603`.

## Exact dyadic lift of odd-prime generators

Let `u_m(p)=p^{-1} mod 2^m` for odd `p`. Then exactly

`u_{m+1}(p)=u_m(p)+b_m(p)2^m`, with `b_m(p) in {0,1}`.

Therefore the normalized phase observer satisfies

`theta_{m+1}(p)=theta_m(p)/2+b_m(p)/2`.

All common odd primes were checked for `m=8,...,15`, with zero failures. This gives a deterministic binary refinement branch for each odd-prime generator. It does **not** imply that the full composite phase has a single simple nested address under resolution change; the 2-generator and modular carries must remain explicit.

## Large-scale obstruction

A fixed finite `M` cannot remain an angularly resolved carrier for all integers. At radius `sqrt(N)`, neighboring spokes are separated by approximately `2*pi*sqrt(N)/M`. Thus any fixed phase modulus eventually creates macroscopically separated rays. A scalable field must refine phase resolution with range/physical scale or use a different carrier.

## Current conclusion

The reciprocal rule is a stronger arithmetic candidate than the prime-rank golden angle for this finite multiplicative-field observer:

`a_2=2^(b-3)`, `a_p=p^{-1} (mod 2^b)` for odd `p`.

Its value is not that it proves uniform distribution. Its value is that it has no tuned random seed; multiplication remains exact at the valuation/phase layer; the 2-generator keeps the 45-degree dyadic angle; finite angular statistics are random-like over tested windows and resolutions; display-cell occupancy reaches the area-random reference near the geometric phase-resolution threshold; and odd-prime generators admit an exact one-bit dyadic lifting law.

Unresolved: derive a nontrivial discrepancy bound from the reciprocal arithmetic itself; understand interaction with actual Nollm 22.5°/Q40 Coverage rather than this display quantizer; determine whether a geometry-native implementation can use the refinement bits without reintroducing a hidden semantic index.
