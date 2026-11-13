# PREFIX-760-R6 — Exact 189-layer Gamma variance sign reversal and a full-second-clock moment-gap refinement

Date: 2026-11-14 (Asia/Shanghai). Independent author-level continuation after PREFIX-759; not a formal Result or review.
Scientific input fixed to awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Model is the *external* stopped-Bernoulli / independent Gamma-clock auxiliary model. No native X6-time, spatial three-dimensional slice, or P000 transfer is asserted.
Evidence status: AUTHOR_EXACT_INTEGER_RATIONAL_COMPUTATION_AND_ANALYTIC_IDENTITIES / UNREVIEWED / NOT_ADMITTED.

## Theorem 760.1: exact finite two-clock moments (including variance)

Let T_x be the integer first-stop layer of the frozen 189-layer BRC kernel. Put S_i(x)=Pr(T_x>i), for 0<=i<=188, and assume T_x<=189. Let C_x given T_x=m have Gamma(m,1) law, with C_p and C_z independent, and Y(p,z)=max(C_p,C_z). The Erlang survival identity is

$$ H_x(t)=\Pr(C_x>t)=e^{-t}\sum_{i=0}^{188}S_i(x)t^i/i!. $$

Define the entirely rational coefficient

$$ K_{ij}={\binom{i+j}{i}\over2^{i+j+1}}, \qquad L_{ij}=(i+j+1)K_{ij}. $$

Then the raw moments of the maximum obey the **exact** finite identities

$$ \mu(p,z)=\sum_{i=0}^{188}(S_i(p)+S_i(z))-\sum_{i,j=0}^{188}S_i(p)S_j(z)K_{ij}, $$

$$ M_2(p,z)=2\sum_{i=0}^{188}(i+1)(S_i(p)+S_i(z))-\sum_{i,j=0}^{188}S_i(p)S_j(z)L_{ij}. $$

Consequently

$$ \operatorname{Var}Y(p,z)=M_2(p,z)-\mu(p,z)^2, \qquad V_q(p,z)=q^2\operatorname{Var}Y(p,z)-q\mu(p,z) $$

can be evaluated as an exact rational number whenever p,z,q are rational. No floating-point Gamma moment quadrature or BLAS rounding claim is needed for these pointwise certificates.

**Proof.** By independence, Pr(Y>t)=H_p(t)+H_z(t)-H_p(t)H_z(t). The positive variable moment formula E[Y^r]=r∫t^(r-1)Pr(Y>t)dt, finite polynomial expansion and the Gamma integral show that the cross-term for r=1 is (i+j)!/(i!j!2^(i+j+1))=K_ij, and for r=2 is 2(i+j+1)!/(i!j!2^(i+j+2))=L_ij. Single-clock integrals are Σ_i S_i and 2Σ_i(i+1)S_i. Every interchange is a finite sum of integrable terms. QED.

## Theorem 760.2: variance and Vq are not coordinatewise monotone in the frozen auxiliary model

Fix p_0=0 and p_1=1/4, define

$$ \Delta\mu(z)=\mu(p_1,z)-\mu(p_0,z),\quad \Delta\sigma^2(z)=\operatorname{Var}Y(p_1,z)-\operatorname{Var}Y(p_0,z), $$

$$ \Delta V_q(z)=q^2\Delta\sigma^2(z)-q\Delta\mu(z). $$

Reconstruct the frozen integer width predicate from PREFIX-754, then perform the preceding *fraction-exact* 189-by-189 sums. The accompanying standalone Python checker verifies these strict rational inequalities by comparisons of Python Fraction values (printed decimals are only presentations):

* At z=0: 367 < Δσ² < 369, 111 < Δμ < 112; hence ΔV_q > 0 for every real q>=2.
* At z=1/4: Δσ² < -159 and Δμ > 10; hence ΔV_q < 0 for every real q>0.
* At z=1/16: ΔV_2 > 259, while at z=5/64: ΔV_2 < -113.
* At z=5/64: Δσ² > 14, while at z=3/32: Δσ² < -78.

The first pair proves variance is **not monotone increasing** in p at all fixed z: its increment is positive for z=0 and negative for z=1/4. The same pair establishes that V_q also has no global fixed sign under raising p from 0 to 1/4 across all z for each fixed q>=2. Since all S_i(z) are polynomials in z, continuity implies:

$$ \forall q\ge2,\ \exists z_q\in(0,1/4):\Delta V_q(z_q)=0. $$

Moreover the q=2 root lies in (1/16,5/64), while **at least one variance-increment root** lies in (5/64,3/32). These two certified intervals are disjoint. Neither uniqueness of roots nor a global extremum is claimed.

Illustrative values (rounded only after exact Fraction evaluation):
| z | Δμ | ΔVar | ΔV_2 |
|---|---:|---:|---:|
| 0 | 111.0623599516273 | +367.8660242514655 | +1249.339377102608 |
| 1/16 | 92.9425857453490 | +111.3805825098591 | +259.6371585487385 |
| 5/64 | 86.1929469012537 | +14.5991623830024 | -113.9892442704977 |
| 3/32 | 78.7535083796446 | -78.5260255984851 | -471.6111191532297 |
| 1/4 | 10.8816823293262 | -159.3866864592493 | -659.3101104956497 |
| 1/2 | 0.1218662990391 | -3.5892126368841 | -14.6005831456146 |

This explicitly refutes any attempted promotion of PREFIX-757/759 first-order stochastic order to variance monotonicity. It does not refute the stochastic order, the exact raw-moment bounds, or the existing cellwise comparator certificates.

## Theorem 760.3: retain the entire second-clock distribution in the row-25 witness

Assume the previously proven order S_i(p_2)>=S_i(p_1), p_2>p_1, and set D=S_25(p_2)-S_25(p_1)>0. For every real r>0,

$$ \Delta E[Y^r]\ge D B_r(z), $$

where

$$ B_r(z)={r\over25!}\left[\Gamma(r+25)-\sum_{j=0}^{188}{S_j(z)\Gamma(r+25+j)\over j!\,2^{r+25+j}}\right]>0. $$

**Proof.** The frozen row-25 witness gives H_p2(t)-H_p1(t)>=D e^-t t^25/25!. Multiplying by the full F_z(t)=1-H_z(t) and integrating r t^(r-1) gives the identity defining B_r. It is positive because F_z(t)>0 for t>0. Since F_z(t)>=g(z)F_25(t), the new bound dominates PREFIX-759's g(z)-only bound; equality holds at z=0, and is strict for 0<z<=1/2 where there are later positive stopping masses. QED.

Exact rational numerical witnesses for integer r:
| z | B_1(z) | B_2(z) | B_1/PREFIX759 | B_2/PREFIX759 |
|---|---:|---:|---:|---:|
| 0 | 0.5561375863296085 | 31.72603380562007 | 1 | 1 |
| 1/4 | 0.0004979985734309839 | 0.02903864894103324 | 1.189910416062475 | 1.216267323249 |
| 1/2 | 0.00000003358751883148741 | 0.000001919169613808823 | 1.013247570729659 | 1.0148864919196 |

## Reproducibility and limits

Scientific input: immutable commit f42f2906d77f24085c123f3ccfe9667d41caa96d. WIDTH predicate and integer Pascal recursion reproduce PREFIX-754 and PREFIX-755 (W=2^18; N=189). Exactly 9,529 nonzero alive coefficient positions on layers 0..188 and zero at 189 are asserted and checked. All S_i are built by integer polynomials divided by the corresponding exact rational denominator. Every key variance, q=2 and bounds comparison is a Fraction inequality; all displayed decimal values are converted only *after* assertions. A separate small Erlang pair identity is checked, and the z=0 equality to PREFIX-759 is checked.

The program was executed locally and returned ALL_CHECKS_PASS. This is an author-reconstructed replay of the frozen kernel, not a separately reviewed original scientific pin or a theorem about native X6 dynamics. Independent mathematical review remains pending. No new Gamma exclusion *area* is counted.

Next research: use the exact finite K and L kernels as an exact-arithmetic oracle to verify a genuinely remaining 1/768 comparator cell; investigate whether useful variance-sensitivity bounds can be certified over a full rational parameter box, with direct interval bounds and no unjustified monotonicity step. Owner/CLAIM checks remain separate from independent direct mathematical publication.
