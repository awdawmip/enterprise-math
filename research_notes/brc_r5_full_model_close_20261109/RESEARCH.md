# R5 — Exact complementary triangle closes the frozen FULL_HIST/seedless-LR model (author-side)

**2026-11-09, Asia/Shanghai.** Evidence: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs: GK `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current normative reading: GK canonical main `ae28c03db2bfeac4fac5c66cc73c1f7588e9acd2`; EM canonical main `9ed5882e3e38c54bef259a90b28c595076e76123`. P000, ACTIVE worldview and six-axis native spatial semantics are preserved. The theorem concerns only the **frozen seven-likelihood-node P/Q-BRC terminal-observer statistical model**.

## Source and target model

Set the likelihood-ratio grid
\[
r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
\]
A lawful FULL_HIST flow \(f=(g,a,b,u,v,w,z)\) satisfies
\[
\begin{gathered}
0\le a,b\le g\le1,\quad
0\le u\le 13a/40+b/80,\quad
0\le w\le 3a/40+21b/80,\\
0\le z\le a/10,\quad
0\le v-z\le 9b/40.
\end{gathered}
\]
For every lawful flow the seven \(Q\)-terminal masses \(M_i(f)\) sum to one and have mean likelihood ratio one; exact maps \(M_i,T_P,T_Q\) are transcribed in the independent runnable checker VERIFY_PGEQ.py. The seedless condition is \(9bz=4a(v-z)\).

Normalize \(g=b=1\), set \(a=t\), and parameterize the four lawful capacity coordinates:
\[
x(t,p,q,\theta,\kappa)=\left(
1,t,1,\left(\frac{13t}{40}+\frac1{80}\right)p,\;
\frac{9\kappa}{40}+\frac{t\theta}{10},\;
\left(\frac{3t}{40}+\frac{21}{80}\right)q,\;
\frac{t\theta}{10}\right).
\]

## New exact all-real theorem: complementary \(p\ge q\) triangular prism

For **every real**
\[
\boxed{
\frac1{13}\le t\le\frac15,\qquad
0\le q\le p\le1,\qquad
0\le\theta,\kappa\le1
}
\]
there exists a lawful seedless target \(y\) on the common **F face**
\[
z'=a'/10,\qquad v'-z'=9b'/40
\]
which preserves the two calibrated stopping times exactly and dominates the source in likelihood-ratio convex order. Hence a nonnegative declaration-independent \(7\times7\) Blackwell/martingale coupling exists preserving every seven-node randomized terminal declaration, and thus \((e_P,e_Q,T_P,T_Q)\).

### The 24 rational certificates

Take \(t\in\{1/13,1/5\}\), \((p,q)\in\{(0,0),(1,0),(1,1)\}\), and \(\theta,\kappa\in\{0,1\}\). The self-contained checker stores **all 24 exact rational triples** \((g',a',b')\). Set \(P=T_P(x)\), \(Q=T_Q(x)\); reconstruct the remaining target coordinates from the target F-face and two time equalities:
\[
\begin{aligned}
u'&=-17a'/40-19b'/80-g'/2-P+3Q/2-1/2,\\
w'&=-7a'/40-39b'/80-g'/2+P-Q/2-1/2,\\
z'&=a'/10,\qquad v'=a'/10+9b'/40.
\end{aligned}
\]

The Fraction checker verifies every corner's source/target capacities, all seven nonnegative masses, \(\sum_iM_i=1\), \(\sum_i r_iM_i=1\), both exact \(T_P,T_Q\) equalities, seedless F-face equation, and the five convex-order hinges
\[
H_k(y)-H_k(x)\ge0,\qquad
H_k(f)=\sum_i(r_i-r_k)_+M_i(f),\quad k\in\{r_1,\ldots,r_5\}.
\]
All five minimal corner hinge gaps are exactly zero; no negative margins occur.

**All-real passage.** Interpolate with the \(t\) endpoint barycentric weights, with triangle weights
\[
\beta_{00}=1-p,\quad\beta_{10}=p-q,\quad\beta_{11}=q,
\]
and with the two Bernoulli endpoint weights for \(\theta,\kappa\). These are all nonnegative and sum to one. The source is *separately affine* in \(t,p,q,\theta,\kappa\), including its \(tp,tq,t\theta\) terms, so the convex mixture of vertex sources is precisely the requested source. The convex mixture of vertex targets lies on the same linear F face. Capacities, masses, times, and hinge inequalities are affine and remain exact under the same mixture. Finite-support convex-order/martingale coupling (Strassen's theorem) therefore supplies \(E_{ij}\ge0\) satisfying
\[
\sum_j E_{ij}=M_i(y),\quad
\sum_iE_{ij}=M_j(x),\quad
\sum_i r_iE_{ij}=r_jM_j(x).
\]
The theorem consequently holds at **all real**, irrational and boundary inputs, rather than being inferred from rational regressions. Relevant reference: Leskelä & Vihola, *Conditional convex orders and measurable martingale couplings*, Bernoulli 23(4A), 2017, DOI 10.3150/16-BEJ827, finite-support case.

**Scaling.** For \(b>0,\ 0\le b\le g\le1,\ 0\le a/b\le1\), scale the normalized source, target and coupling with coefficient \(b\); add \((g-b)E_1+(1-g)E_0\) to source and target, where \(E_1=(1,0,0,0,0,0,0)\), \(E_0=(0,0,0,0,0,0,0)\), with identity martingale couplings on these latter flows. This reconstructs any lawful physical \(u,v,w,z\) via the normalized \(p,q,\theta,\kappa\), preserves seedless F, all mass/time equations and nonnegativity.

## Author-side complete-domain corollary, using prior exact proofs

For **every lawful real FULL_HIST flow** \(0\le a,b\le g\le1\) and physical \(u,v,w,z\), the seven-node frozen observer has a lawful seedless LR Blackwell realization preserving every randomized declaration and the four observables. The proof is the following covering of every source sector:

| Sector | Proof/evidence already published (immutable PR head) |
| --- | --- |
| \(b\le a\) (including \(b=0\)) | PR #1798, `74d31afd03a303eea866ce25fcf4ec192e538b1a` |
| \(b>0,\ a/b\in[0,1/13]\), any \(p,q,\theta,\kappa\) | PR #1821, `edd5391600d24eade7958aeb794f78f0f15caa68` |
| \(a/b\in[1/13,3/20]\), \(p\le q\) | PR #1823, `4cfa1ca9af363bc6800aaafd62c23e305811c045` |
| \(a/b\in[1/13,3/20]\), \(p\ge q\) | New 24-corner triangular theorem above |
| \(a/b\in[3/20,7/39]\), any \(p,q,\theta,\kappa\) | PR #1829, `82b9565c79be2521cc5d1c292651ba4a33c301c0`, using #1827 |
| \(a/b\in[7/39,1/5]\), \(p\le q\) | PR #1823, file F_HIGH_T_BRIDGE.md |
| \(a/b\in[7/39,1/5]\), \(p\ge q\) | New 24-corner triangular theorem above |
| \(a/b\in[1/5,1]\), any \(p,q,\theta,\kappa\) | PR #1800, `58f1444c42d487ac8d2c9a1801f3c3adfade003f` |

Every \((p,q)\in[0,1]^2\) lies in \(p\le q\) or \(p\ge q\), and the \(t\)-intervals cover \([0,1]\). The case \(a>b\) is already covered by #1798. The scaling lemma connects normalized and general flows.

**Evidence scope:** This is an **author-side global coverage proof conditional on the exact predecessor statements and certificates cited above**. The current run actually executed the new 24-corner checker. Earlier PRs remain unmerged, author-verified, and unreviewed; this proof has not been independently mathematically reviewed, granted a formal Task CLAIM/Result, accepted into Working Truth/Foundation, or interpreted as native X6 physical dynamics.

## Reproducibility / exact output

Execute `python -S VERIFY_PGEQ.py` (standard library, no float LP); actual sandbox run 2026-11-09 Asia/Shanghai returned exit code 0:
~~~text
PASS_EXACT_24_F_FACE_TRIANGLE_CORNERS
MIN_HINGE_GAPS 0 0 0 0 0
PASS_EXACT_251_NORMALIZED_AND_SCALED_REGRESSIONS
THEOREM_ALL_REAL_T_1_13_TO_1_5_P_GE_Q_F_FACE_STRASSEN
~~~
The 251 normalized/scaled Fraction cases are implementation regressions, not the universal proof. Separate exact table, analytic interpolation and finite Strassen provide that proof. Output is also retained in EXACT_OUTPUT.txt.

## Next unit

Independently reconstruct and review the entire stitched proof (including #1798, #1800, #1821, #1823 and #1829), verify matching frozen pins, seven-node observers, Blackwell coupling direction and all boundaries, then use current authenticated Owner/CLAIM and independent Driver review paths for formal admission. As a distinct algorithmic question, build an explicit sparse martingale coupling \(E\) for arbitrary rational inputs from the verified target certificates, and analyze bit complexity, input cost and output size; the existence proof alone is not a computational complexity bound.
