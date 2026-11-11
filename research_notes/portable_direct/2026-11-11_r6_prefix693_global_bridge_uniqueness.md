# PREFIX-693-R6 — Full-bridge uniqueness of the frozen BRC variance crossover

Date: 2026-11-11 (Asia/Shanghai). Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Evidence: AUTHOR_DERIVED / FULL_189_ROW_EXACT_FRACTION_REPLAY / UNREVIEWED / NOT_ADMITTED.
Researcher-ID: EM-DIRECT-951682; Research-Activity-ID: RA-93F7717F1FB34A806E144081.
Model scope: finite first-stop 189-level Poissonized two-clock observer readout, **not** native X6 physical dynamics.

## Definitions and inherited precise frontier

Preserve both clock labels Y(z,z) and Y(0,z), their survivor-count histories and the positive rational joint kernels until the mean/variance readout is constructed. Define
\[
A(z)=\operatorname{Var}(Y(z,z))-\operatorname{Var}(Y(0,z)),\quad
B(z)=E Y(z,z)-E Y(0,z),\quad F_q(z)=qA(z)-B(z).
\]
For q>0 the two sampled-variance values differ by qF_q(z).

Let
\[
L=0.0528706,\ R=0.0530659,\ b=53/1000,\ T=647/5000000,
\quad q_-=\frac{63055771}{5256000},\ q_+=\frac{660614143}{27500000}.
\]
Earlier exact results: PREFIX-690 proves F_q(L)>0>F_q(R) for every real q in [q_-,q_+]. PREFIX-688 gives 0.656<A(L)<0.657 and 0.329<A(R)<0.330. PREFIX-692 gives B(z)>7.85 throughout [L,R]. The old open question was uniqueness of zeros throughout the bridge, not just the three narrow q=12/18/24 corridors.

## Theorem 693.1: global derivative signs on the entire spatial bridge

For every real z in [L,R],
\[
\boxed{-1751<A'(z)<-1611},\qquad \boxed{128<B'(z)<129}.
\]

**Exact proof and computational certificate.** Let N=189, M=188. For each frozen survivor row, write the polynomial in its true Bernstein form
\[
 S_n(z)=\sum_{k=0}^{n}\frac{r_{n,k}}{\binom nk}\binom nk z^k(1-z)^{n-k},
 \qquad 0\le r_{n,k}\le \binom nk.
\]
Therefore each normalized Bernstein coefficient is in [0,1]. For j>=1, the standard j-th finite-difference derivative identity and the positive/negative binomial coefficient sums give
\[
 |S_n^{(j)}(z)|\le C_j:=2^{j-1}(M)_j \quad (z\in[0,1]),
\]
with falling factorial (M)_j, and C_0=1. Both probability kernels used by the frozen readout are
\[
 K_{nm}=\binom{n+m}{n}/2^{n+m+1},\qquad J_{nm}=(n+m+1)K_{nm}/2.
\]
They satisfy K,J>=0, \(\sum_{m<N}K_{nm}\le1\), \(\sum_{m<N}J_{nm}\le N\). The readout's exact mean and half-second-moment relations are
\[
\mu_d=2\sum_n S_n-K(S,S),\quad
\mu_e=\sum_n(S_{0,n}+S_n)-K(S_0,S),
\]
\[
H_d=2\sum_n(n+1)S_n-J(S,S),\quad
H_e=\sum_n(n+1)(S_{0,n}+S_n)-J(S_0,S),
\]
\[
B=\mu_d-\mu_e,\quad A=2(H_d-H_e)-\mu_d^2+\mu_e^2.
\]
Here S_0 is the independent edge-clock survivor polynomial evaluated at 0, with fixed row values.

For j>=1, let
\[
 U_0=3N,\quad
 U_j=N\left(4C_j+\sum_{i=1}^{j-1}\binom ji C_iC_{j-i}\right).
\]
The kernel row-sum inequalities and Leibniz rule imply
\[
 |\mu_d^{(j)}|,|\mu_e^{(j)}|\le U_j,\quad
 |H_d^{(j)}|,|H_e^{(j)}|\le NU_j,\quad
 |\mu_d|,|\mu_e|\le U_0.
\]
Hence the sixth derivative bounds, globally for z in [0,1], are
\[
 |B^{(6)}|\le 2U_6=17896441402901698560,
\]
\[
 |A^{(6)}|\le4NU_6+2\sum_{i=0}^6\binom6iU_iU_{6-i}
 =201273663850076722544640.
\]
The corresponding third-order formulas recover the earlier exact bounds
\(218571424275456\) and \(69527880576\), independently checking the combinatorial envelope.

The attached full executable reruns the frozen acceptance predicate for all 189 survivor rows (9529 populated cells) and evaluates the exact derivatives at b, with integer and Fraction arithmetic. Its verified floor values, each equal to the integer floor of the **exact** derivative times 10^8, are:

|j| floor(10^8 A^(j)(b)) | floor(10^8 B^(j)(b)) |
|---:|---:|---:|
|0|44000296|789752024|
|1|-168056589514|12845959424|
|2|-6667624082229|-99127959112|
|3|39352687679231|-1326952329685|
|4|3189837819999830|-14895243921676|
|5|-36266294695911132|-1960958310350017|

The first three rows match PREFIX-680, while the remaining three are new. For either G=A or B, let f_{G,j} denote the listed floor and define the exact rational number
\[
E_G=\sum_{j=2}^5\frac{\max(|f_{G,j}|,|f_{G,j}+1|)}{10^8}
\frac{T^{j-1}}{(j-1)!}
+\frac{M_G T^5}{5!},
\]
where M_A,M_B are the sixth-derivative bounds. Taylor's theorem for G' gives
\[
f_{G,1}/10^8-E_G<G'(z)<(f_{G,1}+1)/10^8+E_G
\]
for every z in [L,R]. Exact Fraction cross-multiplication verifies the sharp-enough numerical brackets
\[
-1751< f_{A,1}/10^8-E_A < (f_{A,1}+1)/10^8+E_A <-1611,
\]
\[
128< f_{B,1}/10^8-E_B < (f_{B,1}+1)/10^8+E_B <129.
\]
Decimal **display only** of the rational sub-intervals:
A': (-1750.049420,-1611.082370); B': (128.325800,128.593388).
No floating approximation is used to decide any inequality.

## Theorem 693.2: global bridge uniqueness for every continuous parameter

For each real q in the **entire closed interval** [q_-,q_+], the equation F_q(z)=0 has exactly one real solution in (L,R).

**Proof.** For q>=0, the derivative sign certificate gives
\[
F'_q(z)=qA'(z)-B'(z)<-1611q-128<0\quad\forall z\in[L,R].
\]
The inherited endpoint signs are strictly opposite for the entire q interval; continuity supplies a zero. Strict decrease yields exactly one. The zero is simple/transverse. QED.

This closes the PREFIX-690/692 parity/ordered-extreme-root gap in the certified bridge: \(\ell(q)=r(q)=z(q)\), with exactly one (rather than merely an odd number of) crossing root, for each real q in the whole band. The narrow q=12,18,24 roots are the only roots in this entire bridge at those parameters.

## Theorem 693.3: monotone real-analytic inverse and slope envelope

Since A'(z)<0 and A(R)>0.329, the whole bridge obeys
\[
0.329<A(z)<0.657.
\]
As B(z)>7.85 and B'(z)>128, the rational function Q(z)=B(z)/A(z) is real analytic with
\[
Q'(z)=\frac{B'A-BA'}{A^2}>0.
\]
Let q_L=Q(L), q_R=Q(R). All real q in (q_L,q_R) have a unique z in (L,R) with Q(z)=q. The inherited endpoint signs imply \(q_L<q_-<q_+<q_R\). Thus the inverse z(q) is real analytic on the open interval (q_L,q_R) and on the certified parameter band has
\[
z'(q)=\frac{A(z(q))}{B'(z(q))-qA'(z(q))}>0,
\quad
\boxed{\frac{329/1000}{129+1751q}<z'(q)<
\frac{657/1000}{128+1611q}}.
\]
The earlier tighter local collars remain useful; this bound applies *uniformly* to the whole continuous band.

## Reproduction and remaining question

Source dependency pins: PREFIX-680 @2c91711f60aa74d93880780929f532da24140ec0; PREFIX-688 @2b0f18fe26a276a45d8860b0d9f4ab029a0afea7; PREFIX-690 @e1394a13ec0627a579db9414242a3633b773304e; PREFIX-692 @408448af569a2865463e8a50584a4dea023832d6. The frozen scientific pin remains unchanged.

Run the attached PREFIX693_R6_FULL_BRIDGE_UNIQUENESS.py using Python standard library; it reproduces all center jets with the frozen 189-row acceptance predicate, exact two-clock moments, global sixth-order envelope and rational inequalities. The matching RESULTS.json records floors and exact rational enclosures; source reproduction and proof checking are author-side, not independent admission.

Next: certify the root count in the wider interval 0.052<=z<=0.054, then join the full-bridge sign topology to the PREFIX-675 two-parameter sampled-variance maximum comparison on 0<=p<=z<=1/2. The (p,z) pair denotes an auxiliary probabilistic observation chart, **not** a native two-dimensional plane. P000/ACTIVE Heartbeat World foundations are unchanged.
