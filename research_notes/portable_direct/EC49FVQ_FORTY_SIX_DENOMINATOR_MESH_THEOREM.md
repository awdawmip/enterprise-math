# EC49FVQ — Forty-six-layer 11-adic rational-phase certificate mesh

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_PERIOD_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

**Frozen scientific input:** BRC16943's derived Bernoulli observer and the exact formulas recorded in EC49FVP, unchanged. Parent: `awdawmip/enterprise-math@d22d515b5f453dd110ed5bc54d5e78f0b98f599b:research_notes/portable_direct/EC49FVP_FOURTEEN_LAYER_PROJECTIVE_MESH_THEOREM.md`. This is independent portable science about rational phases, not a native X6/FUQ/FUR result. The previously observed `RS-EC49AS` canonical publication-directory absence does not establish a current shared owner or an authorized CLAIM.

## Claim and scope

Write `S_H` for the reduced fractions `h/d∈(0,1)` with `d≤H` that satisfy the inherited **complete projective mod-11 no-root certificate** for the Bernoulli rational switching phase. These fractions are rigorously *excluded* candidate values: `t(x)≠h/d` for every rational detection width `x∈(0,1)` whenever the inherited criterion applies.

**Theorem (46-layer gap and intensity).** For every integer `H≥256` and every real interval `I⊆[0,1]`,

\[
\boxed{|I|>\frac{1760}{377H}\quad\Longrightarrow\quad I\cap S_H\ne\varnothing.}
\]

This is a uniform covering improvement over the prior `880/(91H)` threshold (a reduction of `15/29 = 51.7241%`). More precisely, for `j=floor(log_2 H)`, `k=2^j`, the constructed set `T_j⊆S_H` has max gap, including endpoints, at most

\[
\frac1k\begin{cases}\frac{880}{377},&j\text{ even},\\[2pt]\frac{3680}{1647},&j\text{ odd}.\end{cases}
\]

For each half-open `I=[a,b)⊆[0,1]`, it also obeys

\[
\boxed{\#(T_j\cap I)=\frac{67}{22}k(b-a)+E_j(I),\qquad |E_j(I)|\le\frac{359}{11}.}
\]

The sharper discrepancy oscillation is `8434/297` for even `j` and `359/11` for odd `j`. Counts use the half-open convention.

## Exact 46-denominator construction

The 18 parent layers are indexed by `(r,e)`:

```
(1,0),(7,3),(13,4),(1,1),(1,2),(1,3),(1,4),(7,4),
(13,5),(7,5),(1,5),(1,6),(7,6),(13,6),(1,7),(7,7),(13,7),(91,7).
```

Add `(3,e)` for `2≤e≤7`. Then, for each `r` in

```
47, 11, 23, 53, 27, 31, 29, 61
```

add all `(r,e)` with `ceil(log2 r)≤e≤7`. There are `18+6+2+4+3+2+3+3+3+2=46` distinct layers. For `j≥8`, set `k=2^j` and `d=r 2^(j-e)` for each layer; `T_j` is the union of certified reduced phases `h/d` with `0<h<d`.

Let `L=lcm(r : (r,e) in menu)=84915883381329`, and use the *integer* observer coordinate

\[
y=Lk\frac{h}{d}=\frac{L2^e}{r}h.
\]

For each layer, the step `s=L2^e/r` is an integer. Its exact mask is

\[
\{sh: 0<h<M/s,\ \gcd(h,2r)=1,\ C_{11}(h,r2^{j-e}-h)=1\},\quad M=14080L,
\]

where `C_11` is the inherited complete projective no-root predicate. The denominator only needs to be evaluated modulo `110` inside `C_11`.

## Proof of period reduction and exhaustive certificate

Since `j>e` and `r` is odd, `gcd(h,d)=1` is equivalent to `gcd(h,2r)=1`. Shifting `y` by the common period `M=14080L` shifts the layer numerator by

\[
\Delta h=\frac{14080r}{2^e}=2^{8-e}\cdot55r,
\]

which is a multiple of `110` for all `e≤7` and a multiple of `2r`. Thus coprimality and the exact certificate predicate remain unchanged. Also `r2^{j-e} (mod 110)` repeats as `j` advances by `20` (all `j-e≥1`). Consequently the complete masks for `j=14,...,33` are a full finite certificate for every `j≥8`.

For each of the twenty exponent states, exact integer enumeration gives precisely **42,880** points in `[0,M)` and the following outcomes:

| Exponent parity | Max cyclic integer gap | Gap after dividing by L | Counting-discrepancy oscillation |
|---|---:|---:|---:|
| even | 198212141579760 | 880/377 | 8434/297 |
| odd | 189733121337760 | 3680/1647 | 359/11 |

The verifier reconstructs `C_11` independently from finite-field projective evaluations for all 12,100 pairs `1≤h,n≤110`, then computes all twenty full sets. It separately enumerates actual reduced fractions for `j=8,...,15`. These are **finite exhaustive certificates** after the periodicity argument.

The finite cyclic gap bound implies the same gap bound after restricting the periodic mask to `[0,Lk]` and inserting endpoints. Every interval longer than this bound meets an interior certificate point. As `k≤H<2k`, the worst-case estimate implies `maxgap/(Lk) < 1760/(377H)`, proving the theorem.

A period of physical phase has length `M/(Lk)=14080/k`. Its point density is `42880/(14080/k)=67k/22`. For sorted cyclic mask `0≤y_0<...<y_{N-1}<M`, the exact periodic counting-discrepancy oscillation is

\[
\frac{\max_i(iM-Ny_i)-\min_i(iM-Ny_i)+M}{M}.
\]

Applying the two exhaustive values proves the uniform interval-counting bound.

## Verification, provenance and next question

Execute `python EC49FVQ_FORTY_SIX_DENOMINATOR_MESH_VERIFY.py` with Python 3 standard library. The output file ends in `ALL PASS`; no floating-point arithmetic is used in certification or gap comparisons. The 46-layer menu is an explicit finite witness, not a global optimum. The result depends on the prior EC49FVP polynomial reduction/no-root equivalence. Independent mathematical review and formal Result admission are pending; a native Heartbeat X6 or FUQ/FUR transfer requires a separately verified bridge.

**Next question:** Can mixed-prime projective certificates or optimized denominators decrease the uniform covering coefficient toward the elementary lower bound 1, while controlling discrepancy at scales near `1/H`? Compare finite-menu certificate distribution with the full four-prime phase-certificate density on shrinking intervals.
