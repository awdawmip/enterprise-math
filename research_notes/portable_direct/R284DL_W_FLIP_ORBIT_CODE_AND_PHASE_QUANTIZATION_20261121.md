# R284DL — 冻结 Port 双读观察的轨道残差码与非单调量化

Date: 2026-11-21 (Asia/Shanghai)
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**.
Scope: frozen auxiliary 34-bit Port observer only; independent portable scientific result, no native X6 or BRC dynamics inferred.

## 1. Frozen scientific input

Pin: awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py; Git blob b46e0f682b58e47c27094b4bea6fa4e55119a3ee. The original 65,536-word SHA-256 is b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4. Its modular determinant generates 65,536 distinct residues modulo P=17,179,869,143, with 64 labeled oriented integer arcs. Let D(x) be the maximum integer circular distance to the arcs. Source states are indexed S={0,...,65535}; let T(i)=i xor 64, the flip of the lower w variable. T is an involution without fixed points. Define E(i)=(D(g(i)),D(g(Ti)))=(a_i,b_i). The earlier R284DI/R284DK injectivity assertion is separately checked over the entire frozen S here.

## 2. Theorem A — lossless orbit residual under the w flip

**Exact theorem.** On the full finite source population E is injective, E(Ti)=(b_i,a_i), and a_i is never equal to b_i. The unordered two-distance key K(i)=(min(a_i,b_i),max(a_i,b_i)) has exactly 32,768 values and distinguishes precisely the 32,768 two-state T orbits. With the orientation residual epsilon(i)=[a_i>b_i], the pair (K,epsilon) uniquely identifies all 65,536 states. For every n>=0,

\[
K(T^n i)=K(i),\qquad \epsilon(T^n i)=\epsilon(i)\oplus(n\bmod2).
\]

Thus for future operations generated solely by T, the latent exact state is updated at the observer layer by toggling a single direction bit, without an inverse dictionary, determinant, arc-distance recomputation, or kernel lookup. Given an unordered K, exactly one direction bit is necessary and sufficient to distinguish the two states in that orbit.

**Proof.** The checker independently enumerates all frozen words, verifies their digest, computes all 65,536 E values and checks injectivity. Since T²=id, the defining expression gives E(Ti)=swap(E(i)). If a_i=b_i then E(Ti)=E(i), contradicting injectivity because Ti≠i. If K(i)=K(j), then E(j) equals E(i) or swap E(i)=E(Ti); injectivity forces j=i or j=Ti. Therefore K is a bijective orbit identifier, and epsilon separates its two orientations. The update follows by induction on n. The exact one-bit lower bound is the two-element fiber of each K. QED.

Full 32,768-orbit integer enumeration finds the **sharp within-orbit distance gap**

\[
\min_{i\in S}|a_i-b_i|=59.
\]

A minimizing orbit is (61333,61397), with E(61333)=(8343605786,8343605727). Across **all distinct ordered states**, the Chebyshev minimum is 53; this run independently finds exactly two minimizing unordered pairs, (61333,65493) and (61397,65429).

## 3. Theorem B — complete common-phase quantization atlas for steps 1..70

For integers s>=1 and t in {0,...,s−1}, apply the **same phase on both coordinates**:

\[
Q_{s,t}(d)=\left\lfloor\frac{d-t}{s}\right\rfloor,\qquad E_{s,t}(i)=(Q_{s,t}(a_i),Q_{s,t}(b_i)).
\]

**Exact finite theorem.** In the complete frozen population,

\[
\{s\in\{1,\ldots,70\}: E_{s,t}\text{ is injective for every }t\}
=\{1,\ldots,55\}\cup\{59\}.
\]

The first loss of universal phase safety is step 56: precisely phases 24,25,26 collide. Steps 57 and 58 have respectively two and one colliding phases, while step **59 is injective for all 59 phases again**. Step 64 has 38 colliding and 26 safe phases (including a collision at t=0, agreeing with R284DK). Step 70 collides at every phase. This is a concrete counterexample to monotonic deterioration of identifiability when integer quantization step sizes are **not divisibility-nested**.

| Step s | Colliding phases / all phases |
|---:|---:|
| 53 | 0 / 53 |
| 54 | 0 / 54 |
| 55 | 0 / 55 |
| 56 | 3 / 56 |
| 57 | 2 / 57 |
| 58 | 1 / 58 |
| **59** | **0 / 59** |
| 60 | 1 / 60 |
| 61 | 4 / 61 |
| 62 | 9 / 62 |
| 63 | 29 / 63 |
| 64 | 38 / 64 |
| 65 | 52 / 65 |
| 66 | 54 / 66 |
| 67 | 53 / 67 |
| 68 | 61 / 68 |
| 69 | 68 / 69 |
| 70 | 70 / 70 |

**Exhaustiveness argument.** For two points to have identical floor bins of width s in both coordinates, their two raw coordinate gaps must each be strictly less than s. Sorting all 65,536 E points on the first coordinate and sweeping every subsequent first-coordinate gap <71, then checking the second, gives exactly **1,283** unordered pairs potentially colliding for any s<=70. This sweep includes every possibility by the necessary gap condition. For each s=1,...,70 and each t=0,...,s−1, the checker evaluates exact integer floor comparisons on these pairs; all missing pairs have at least one coordinate gap too large to collide. For s=53,54,55,56,59,64,70, an independent full-domain hash calculation over all 65,536 points at every phase confirms the candidate-based atlas. Consequently the displayed theorem is a complete finite integer certificate, not a numerical fit or sampling statement. At s=56,t=24 the states 61333 and 65493 explicitly collide in both quantized coordinates.

**Sharp bound if the phases are independent.** When the two coordinate quantizers may choose phases t0 and t1 separately, the largest phase-uniform safe integer step is **53**. The global ordered E separation 53 ensures every s<=53 is injective under any independent phases. At s=54, source states (61333,65493) with phases (t0,t1)=(14,10) collide; for any s>=54, the two coordinate differences 53 can each be placed into a common bin of width s using suitable independent phases. Thus the independence assumption changes the exact answer.

## 4. Future-observer preservation, cost and evidence scope

Because both coordinates use the same Q, quantization and swapping commute exactly: E_{s,t}(Ti)=swap(E_{s,t}(i)). Therefore for each proved injective (s,t) the encoded state can be propagated through any T-only sequence simply by swapping the two stored integers; for the unordered-key representation it suffices to flip the orientation bit. This is an explicit future-observer-safety certificate for the **declared operation monoid generated by T** and the declared D-based reads. It is not a statement about omitted source operations or native spatial evolution.

The Python standard-library checker uses 4,194,304 exact point-arc distances, the original frozen-word SHA-256 assertion, all 65,536 ordered codes, all 32,768 w-orbits, all 1,283 near candidate pairs for s<=70, and every common integer phase for every step 1..70. Seven steps are verified again with direct exhaustive hash enumerations. No floating point is used. Author computation status: EXACT_FINITE_CERTIFIED. Independent mathematical review: NOT_REVIEWED. The construction cost of the initial two readings and the state-recovery cost are separate from the proven constant-time repeated T update.

## 5. Continuation

Test whether both lower flips T_w and T_r admit a common compact observer with directly computable updates without a full 65,536-state inverse table; characterize the operation family and preserve its joint relations. Examine phase-aware coding for physically constrained calibration and compare end-to-end preprocessing, observation, update and recovery costs with the prior R284DG quadratic label code and R284DK modular-increment decoder.

Contributor provenance: independent portable TASK research; historical EM-DIRECT-20B766 is earlier attribution only. No authenticated new native Researcher, CLAIM, Result or Review is asserted. New Activity linkage must follow the original authenticated session and proper CAS.
