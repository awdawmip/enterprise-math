# R630｜两次非连续探针识别全部720种方向：signed BRC 模3算术层析

2026-11-08 | AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED.
R629 prefix lower-bound source @ `ec2f19f968fbab2270615cbf21f45d0164624828`; frozen signed R462 input @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`, theta=0; generator blob `7fa7a762f758b30c6090468ac43487daa34abad8`.
Mother target: type-safe signed BRC provenance over native X6, towards a future-operation-preserving internal-field readout. Probe index below is an auxiliary scheduling parameter, not native heartbeat time/branch grade.

## 1. Fixed model and new question

Use R629's six X6 axis labels, unknown orientation pi in S6, signed frozen branches P_j=K_(2j-1), M_j=K_(2j), D_j=P_j-M_j over Z[t]. At each axis x, gain A_x in Z[[t]] is fixed across the probe pair; nuisance is an independent integer Newton polynomial

`H_x(k)=sum_(l=0)^h B_(x,l) binom(k,l)`, `B_(x,l) in Z[[t]]`, h>=0.

At integer index k, the positive probe reads `A_x P_j+H_x(k)` and the negative probe reads `A_x M_j+H_x(k)` (j=pi^-1(x)). The question is whether **nonconsecutive integer indices** can exploit arithmetic divisibility to reduce the h+2 consecutive-prefix probes of R629.

Assume all gains have a known common exact t-adic valuation a>=0 and leading coefficient not divisible by 3 (they may otherwise differ across axes). For each fixed h choose `L=3^s` as the **least power of 3 strictly greater than h** (L=1 when h=0), and take **exactly two scalar-series readouts per axis**:
`Y_x^0=A_x P_j+H_x(0)` and `Y_x^L=A_x M_j+H_x(L)`.
Since L is odd, this agrees with the alternating sign selection at k=0 and k=L.

## 2. Modular nuisance cancellation lemma

For s>=1 and every `1<=l<3^s`,
```
binom(3^s,l) = 0 mod 3.
```
Indeed, in F3[X], the freshman's-dream identity gives `(1+X)^(3^s)=1+X^(3^s)`. For every finite h<L, therefore,
```
Y_x^L - Y_x^0 = -A_x D_j + sum_(l=1)^h B_(x,l) binom(L,l)
             = -A_x D_j   (mod 3).
```
This holds coefficientwise in F3[[t]] for *arbitrary* nuisance coefficients, without solving for H_x or assuming a time-independent background.

When h>=1, the integer span of `{binom(L,l):1<=l<=h}` is **exactly 3Z**. All generators are divisible by3. Because L is the least 3-power above h, `h>=L/3`. For `j=L/3`, `binom(L,j)=3 binom(L-1,j-1)`. Moreover `(1+X)^(L-1)=(1+X^L)/(1+X)` in F3[X] up to degree L-1, so the coefficient `binom(L-1,j-1)` equals `(-1)^(j-1) !=0` mod3. Thus `v_3(binon(L,j))=1` and the gcd is3. Thus the integer binomial coefficient at j=L/3 has 3-adic valuation exactly one. Consequently every increment in `3Z[[t]]` is realizable by some permissible Newton nuisance difference `H(L)-H(0)`. For h=0 the nuisance increment is identically zero.

## 3. Frozen signed BRC F3 signatures

Reconstruct the twelve frozen signed K polynomials using the R462 generator; let `nu_3(F)` denote the first t-power whose integer coefficient is nonzero mod3 (infinity for zero mod3). Direct exact coefficients give:

| j | leading integer D_j coefficient | nu_t(D_j) | nu_3(D_j) |
|---|---:|---:|---:|
| 1 | 2 | 0 | 0 |
| 2 | -8 | 2 | 2 |
| 3 | 6 | 4 | 7 |
| 4 | 106 | 6 | 6 |
| 5 | 83 | 8 | 8 |
| 6 | 9 | 10 | 11 |

The **mod3 valuations `(0,2,7,6,8,11)` are pairwise distinct**. Since the gain has valuation a and leading coefficient not divisible by3, its reduction mod3 has valuation a, hence the two-probe difference mod3 has valuation `a+nu_3(D_j)`.

## 4. Sharp two-probe theorem

**Theorem (all finite h, sharp depth).** For every integer h>=0 and a>=0, every orientation pi in S6, every independently chosen axiswise Newton nuisance of degree<=h, and every axiswise gain A_x in Z[[t]] with `nu_t(A_x)=a` and 3 not dividing its leading coefficient: the two readings at indices (0,L), with L the least 3-power>h, determine pi uniquely from their d-jets for every `d>=a+8`. Within this fixed two-reading scheme, d=a+8 is the **least uniform truncation depth**. One reading per axis never suffices under arbitrary nuisance H_x(0), so two readings is the globally minimum sample count for this declared gain/nuisance regime.

*Proof of sufficiency.* Subtract the two readings and reduce all integer coefficients modulo3. By Section2 the nuisance vanishes. The first mod3 nonzero order is one of `a+(0,2,7,6,8,11)`. At d=a+8, five distinct labels (j=1,...,5) have appeared; if one axis remains invisible it must carry j=6. Since pi is a permutation, all six labels are recovered. No gain coefficient or background value need be determined.

*Sharp truncation.* For d<=a+7, take a gain `t^a` on two axes and swap labels j=5 and j=6. Their mod3 difference signatures vanish through degree d. For h>=1 the nuisance-increment subgroup is precisely `3Z[[t]]`, so integral Newton nuisance coefficients can adjust the pair's two observations to be identical modulo `t^(d+1)` (first match Y(0), then match Y(L) by the gcd3 lemma). For h=0, the ordinary signed differences themselves vanish to that depth, and a common constant background matches the first reading and therefore the second. Other axes are identical. The bound is exact.

*One-reading lower bound.* At one index the free series `H_x(0)` can offset each proposed branch value, producing six zero readings for any pi. Thus no one-read protocol at that index uniformly distinguishes two orientations. For arbitrary single index k where h>=1, `H_x(0)` remains an arbitrary constant term and yields the same conclusion.

## 5. Observation/resource consequences

R629's h+2 count was proved for a **consecutive alternating prefix**. The present theorem shows a different sampling language can recover the same 720 orientation states with two readings **independent of h**, using arithmetic torsion in the nuisance lattice. Probe-index span is `L=3^s>h`, with `h<L<=3h` for h>=1; the cost changes from number of probes to longest scheduling interval and validity of the fixed-gain/degree-h assumptions over that interval. For h=1, L=3: `(Y_3-Y_0) mod3 = -A D` even when H is affine. For h=3, L=9 and the same law holds against a cubic Newton nuisance.

The mod3 observer is a typed coefficient reduction of genuine signed BRC source polynomials. It recovers **orientation only**; branch identity, ordered paths, multiplicity, full signed amplitudes, six-dimensional Cell displacement, field and separately typed heartbeat state remain in the actual joint state until a declared future-operator descent is proved. This is not a proof of a physical X6 sensor: the read Source still declares `fixed_heartbeat_program=null`.

## 6. Exact verification and next research

`R630_VERIFY.js` independently generates the frozen twelve K polynomials with BigInt; checks six mod3 valuation signatures; confirms binomial-gcd=3 for every h=1..80; tests full 720-permutation recovery for h=(0,1,2,3,8,9), a=(0,2), arbitrary integer-series nuisance samples; verifies 1-probe zero outputs and exact low-depth swapped-label collisions. Complete evidence in `R630_EVIDENCE.json`. A separate exact Python check of h values (0,1,2,3,4,8,9,26,27,80,100) independently confirmed the binomial gcd/sampling intervals. Universal statements above follow the elementary proofs, not extrapolation from finite tests.

**Reuse:** `T0_BRC=REUSE_APPLIED` via frozen signed K; `T6_OPERATION_SAFE_QUOTIENT=REUSE_APPLIED` for explicit observer scope; R629 Newton nuisance and R628 paired branch readout extended. The construction is a specialized observation protocol, not a new global theorem/tool-family admission.

**Next:** Quantify the exact optimal nonconsecutive probe span for a given integer-valued nuisance class and allowed prime moduli; compare p=3 with p=5 using the actual signed D mod-p signatures, including variable gain valuations. Then test a Source-defined X6 joint-field probe for the required two sign-selectable readings and stable gain across indices 0,L, preserving grade, path and physical-time typing.
