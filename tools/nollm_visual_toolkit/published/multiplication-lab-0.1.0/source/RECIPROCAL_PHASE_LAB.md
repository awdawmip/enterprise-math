# Reciprocal Phase Resolution Lab 0.1.0

This is an additive experiment for Nollm Visual Toolkit 0.3.0 and the published Multiplication Field Lab 0.1.0. It does not rewrite either baseline.

## Candidate

For phase modulus `M=2^b`:

- `a_2=M/8` (45 degrees),
- `a_p=p^{-1} mod M` for odd primes,
- `phi(n)=sum_p v_p(n)*a_p mod M`.

The phase multiplication law is exact **by construction**. The polar rendering and nearest hex-cell display are observer layers and are not promoted to native Nollm geometry.

## Generate and preview

```sh
python -m nollm_visual_toolkit.reciprocal_phase_lab --out reciprocal.html --phase-bits 11
python -m nollm_visual_toolkit.reciprocal_phase_lab --site reciprocal-site --preview
```

The comparison site generates the same integer population at 11-bit and 16-bit phase resolution. Each page remains self-contained and uses the existing toolkit preview server when `--preview` is requested.

The original Multiplication Field Lab remains unchanged and still defaults to its historical golden-rank phase. The reciprocal page adds an `inverse` observer preset instead of silently changing old saved experiments.

## Why compare 11 and 16 bits?

At `N=65,536`, scale `C=1`, the outer-circle spoke spacing is approximately

`2*pi*sqrt(N)/M`.

The finite experiments show a sharp occupancy improvement as this spacing crosses roughly one display-cell center spacing. 11 bits (`M=2048`) is already near the occupancy plateau for this population, while 16 bits is a useful higher-resolution control. This is a finite sampling heuristic, not a uniform theorem.

## Recorded finite results

For all 65,536 integer identities:

| mode | angular CV (64 sectors) | occupied display cells | max cell load |
|---|---:|---:|---:|
| reciprocal, 16 bit | 0.029426 | 57,339 | 4 |
| reciprocal, 11 bit | 0.025983 | 57,342 | finite control |
| golden by prime value, 16 bit | 0.059165 | 55,841 | 5 |
| golden by prime rank, 16 bit | 0.199383 | 47,491 | 9 |

The reciprocal candidate is close to the independent-area Poisson occupancy reference for this display observer. That comparison is diagnostic only; it does not establish that the deterministic field is Poisson or asymptotically equidistributed.

At `N=1,000,001`, 13-bit reciprocal phase has occupied ratio about `0.87268`; 14-bit is about `0.87475`. In 100 consecutive 10,000-integer windows at 13 bits, 64-sector CV has mean about `0.07701`, close to the iid reference `0.07937`.

## Exact dyadic lift

For every odd prime `p`, if `u_m=p^{-1} mod 2^m`, then

`u_{m+1}=u_m+b_m*2^m`, `b_m in {0,1}`.

Thus each odd-prime generator admits an exact one-bit refinement. This is a useful arithmetic interface for future multi-resolution geometry; it does not by itself provide a full nested physical address for composites.

## BRC / identity boundary

Prime valuations and integer identities are retained before the phase observer. Display-cell collisions retain all IDs and are never used as an identity quotient. The web page changes observation parameters, not source coordinates or relations.

Status: `FINITE_RESEARCH_CANDIDATE / NOT_FOUNDATION / NOT_NOLLM_RUNTIME`.
