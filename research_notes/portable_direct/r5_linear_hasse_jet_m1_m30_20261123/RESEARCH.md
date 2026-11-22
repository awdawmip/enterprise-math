# R5 — Exact degree-≥1 coefficient period at thresholds 1–30

2026-11-23. **Author-side finite-field Hasse-jet proof; NOT_REVIEWED.** Independent portable research, without formal Task CLAIM, Result, native X6 proof or theorem promotion.

## Theorem and exact scope

Use the *unchanged* frozen five-event scalar integer-cost observer in \`awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`. For nonnegative integer counts \(a_{214},\ldots,a_{314}\), total cost \(N=\sum_{p=214}^{314}pa_p\), define five failure events \(\sum_{p\in S_i}a_p<m\), where

- \(S_0=\{214,215,216,217,218\}\)
- \(S_1=\{214,216,217,218,219,220,221\}\)
- \(S_2=\{215,216,217,218,219,220,221\}\)
- \(S_3=\{223,\ldots,290\}\), \(S_4=\{296,\ldots,312\}\).

Let \(f_m(N)\) count configurations of cost \(N\) satisfying at least one event, and \(M_m^{(\ge1)}\) be the minimal common period of all coefficient functions of \(N^j\), \(j\ge1\), in this quasipolynomial (discarding its bounded constant coefficient). Then

\[
\boxed{M_m^{(\ge1)}=814202665467037976682352800\qquad(1\le m\le30).}
\]

The previous \(m=1,\ldots,5\) theorem and exact residues are archived at \`enterprise-math@f8b3c531069885c1a68dc81a202943336947e4a9:research_notes/portable_direct/r5_m1_linear_spectral_period_20261123/\`. This result extends the **threshold** interval through \(30\), while covering every cost \(N\) in each interval member.

## Complete mathematical argument

Set \(D(q)=\prod_{p=214}^{314}(1-q^p)\). Genuine simultaneous-inequality inclusion/exclusion yields \(F_m(q)=\sum_N f_m(N)q^N=R_m(q)/D(q)\), \(R_m\in\mathbb Z[q]\). At a primitive order-\(d\) root, \(D\) has zero multiplicity
\[
 n_d=\#\{214\le p\le314:d\mid p\}.
\]
Only poles of order at least \(2\) affect quasipolynomial coefficient functions of degree \(\ge1\). Consequently for every \(m\ge1\),
\[
 M_m^{(\ge1)}\mid\Lambda_1=\mathrm{lcm}_{n_d\ge2}d
 =814202665467037976682352800.
\]
The 18 orders
\[
32,54,25,49,11,13,17,19,23,29,62,37,41,43,47,59,61,73
\]
each have \(n_d\ge2\), and their lcm is \(\Lambda_1\).

For each \(m\in[1,30]\) and each listed \(d\), the companion checker explicitly certifies a prime \(p\), an element \(z\in\mathbb F_p\) of **exact order \(d\)**, and \(0\le j\le n_d-2\) such that
\[
[t^j]R_m(z(1+t))\not\equiv0\pmod p.
\]
If \(\Phi_d(q)^{n_d-1}\mid R_m(q)\) in \(\mathbb Z[q]\), this divisibility would persist modulo \(p\). Since \(p\nmid d\), \(z\) is a simple root of \(\Phi_d\pmod p\); all Hasse coefficients through order \(n_d-2\) would vanish, a contradiction. Therefore the complex rational function \(F_m\) has a pole of order \(\ge2\) at the primitive \(d\)-th roots. The corresponding nonzero degree-\(\ge1\) Fourier/quasipolynomial coefficient forces \(d\mid M_m^{(\ge1)}\). Taking the lcm over these 18 orders gives \(\Lambda_1\mid M_m^{(\ge1)}\), hence equality.

### Exact event computation

For each nonempty \(I\subseteq\{0,1,2\}\), take \(U_I=\bigcup_{i\in I}S_i\) and
\[
P_{I,m}(q)=\sum_{\substack{a_p\ge0,\ p\in U_I\\
\sum_{p\in S_i}a_p<m\ (i\in I)}}q^{\sum_{p\in U_I}pa_p}.
\]
The overlapping numerator is
\[
A_m=\sum_{\varnothing\ne I\subseteq\{0,1,2\}}(-1)^{|I|+1}P_{I,m}(q)\prod_{p\in U_I}(1-q^p).
\]
The checker computes each \(P_{I,m}\) using a truncated multivariate DP over the *actual joint loads*, with an unbounded-geometric update for every price. This avoids brute-forcing \(m^8\) assignments.

For the two disjoint blocks \(T=S_3,S_4\), the correct numerator is
\[
H_{T,m}(q)=\prod_{p\in T}(1-q^p)\sum_{j=0}^{m-1}h_j((q^p)_{p\in T}),
\]
using complete homogeneous polynomials, **not** the previously corrected invalid product \(\prod_p(1-q^{mp})\). With \(B_m=H_{S_3,m}\), \(C_m=H_{S_4,m}\), disjointness gives \(R_m=1-(1-A_m)(1-B_m)(1-C_m)\). All operations are performed exactly in \(\mathbb F_p[t]/(t^{J+1})\), using \(q=z(1+t)\), \(q^a=z^a\sum_{j\le J}\binom ajt^j\), and \(J=\min(2,n_d-2)\). Products already having more than \(J\) root factors are identically zero in this truncated ring and are safely skipped.

## Reproduction and exact data

Run \`python3 VERIFY_R5_M1_M30_JET_PERIOD.py R5_M1_M30_WITNESS_JETS.csv\`; the same checker accepts optional \`first last\` integer bounds for smaller runs. The CSV consists of the full 540 rows and is also archived as a deterministic gzipped-base64 file, with the decoding instruction in its header.

Local bounded runs produced:

- \(m=1..20\): **360/360** witnesses, first nonzero jet orders \(0:337,\ 1:22,\ 2:1\).
- \(m=21..30\): **180/180** witnesses, orders \(0:170,\ 1:10,\ 2:0\).
- Combined: **540/540**, orders \(0:507,\ 1:32,\ 2:1\).

Notable: at \((m,d,p,z)=(20,11,23,4)\), the first two coefficients vanish but the second Hasse jet equals **11 modulo 23**. Because \(n_{11}=9\), the surviving pole still has order at least seven. Testing only \(R_m(\zeta_d)\ne0\) would miss this.

At \((m,d)=(9,41),(11,59),(18,59),(29,62)\), the first selected finite-field conjugate gave a zero, but alternative *primitive conjugates* respectively \((p,z)=(83,3),(709,20),(709,20),(311,11)\) yield certified nonzero values. A zero at one finite-field root is not evidence of characteristic-zero cyclotomic divisibility.

The earlier 90 values for \(m=1..5\) were independently reproduced by a separate direct modular DP and matched the archived tables. This result is a **finite threshold-range exact calculation**, not an all-\(m\) classification. No floating-point approximation or Lean checker was used.

## Next issue

Find the first actual threshold \(m\) (if any) where \(M_m^{(\ge1)}<\Lambda_1\), by determining the full \(\Phi_d\)-adic multiplicity of \(R_m\) rather than relying on a zero residue at a single root. Seek a rational recurrence in \(m\) for the corrected joint-load numerator and its first jets, to replace finite-range enumeration. Signed cyclotomic residues here are an auxiliary scalar observer; transfer to native X6 or BRC requires a separately proved observer-preserving map. Frozen scientific input, P000, ACTIVE world semantics and the independent NOT_REVIEWED status are preserved.
