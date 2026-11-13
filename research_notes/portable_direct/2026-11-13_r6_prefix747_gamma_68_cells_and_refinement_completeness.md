# PREFIX-747-R6 — 68 additional closed-cell Gamma exclusions and exact-refinement completeness

Date: 2026-11-13 (Asia/Shanghai). Mother problem: PREFIX-675. Direct predecessor: PREFIX-746.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Scope: independent auxiliary Gamma mathematics on the existing 189-row stopped-survivor BRC kernel.
Grade: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.
Native registration request `r6-20261113-1153-prefix747-session-v1` was **QUEUED** during manuscript preparation. No new Task CLAIM/Result/Review is asserted.

## Theorem 1: 68 complete closed cells

Let (T_p,T_z) be the independent unit-rate Gamma-clock mixture variables determined by the frozen 189-row kernel. Write
[
Y(p,z)=\max(T_p,T_z),\quad \mu(p,z)=\mathbb E[Y],\quad M_2(p,z)=\mathbb E[Y^2],\quad W=M_2-\mu^2.
]
For real (q\ge2), define (V_q(p,z)=q^2 W(p,z)-q\mu(p,z)). Fix (e=(0,73/500)).
For the closed grid cell (R_{ij}=[i/384,(i+1)/384]\times[j/384,(j+1)/384]), let (S) be the **34 distinct** index pairs in `PREFIX747_R6_GAMMA_68_RESULTS.json`. For every ((i,j)\in S), every ((p,z)\in R_{ij}\cup R_{ji}), and **every real (q\ge2)**,
[
\boxed{V_q(e)-V_q(p,z)>\frac{q^2}{30}>0.}
]
Thus these 68 complete continuous closed cells contain no global maximizer for the frozen auxiliary objective.

### Proof and computational certificate

The symmetric integer recurrence, Bernstein coefficient inequalities, and Gamma integration formulas from the unchanged `PREFIX741_R6_INNER_STRIP_194.py` kernel give nonnegative, coordinatewise nondecreasing (\mu,M_2). For a rational closed subrectangle (Q=[a,c]\times[b,d]), define (L=\mu(a,b)\ge0), (H=M_2(c,d)) and (t=1/q\in(0,1/2]). Then uniformly for ((p,z)\in Q),
[
\frac{V_q(e)-V_q(p,z)}{q^2}
=W(e)-M_2(p,z)+\mu(p,z)^2-t(\mu(e)-\mu(p,z))
\ge W(e)-H+L^2-t(\mu(e)-L).
]
The right side is affine in (t), so its infimum for (t\in[0,1/2]) is attained at (t=0) or (t=1/2).
Partition each (R_{ij}) into 64 exact rational (8\times8) subrectangles. The least of these corner/endpoint bounds is the rational (G_8(i,j)). All 34 computed exact **integer floors** (\lfloor10^6G_8(i,j)\rfloor) are in the results JSON; each exceeds 33,333. The minimum is **36,384 at ((11,53))**. Therefore (G_8(i,j)>1/30). Exchangeability of the two Gamma clocks supplies each transposed cell.

The independent local execution reconstructed 189 recurrence rows, verified 9,529 nonzero survivor positions and the two PREFIX-741 Gamma witness-moment digest assertions. The existing published PREFIX-746 cell ((10,47)) was independently replayed with its expected (G_8) microfloor of 27,002,790. Each of the 34 new (G_8) floors was calculated using Python 3 `Fraction` in bounded sessions. All 34 also failed the original PREFIX-712 unsplit witness (e_0=(0,3/20)): their `G_1` microfloors lie between -216,314,021 and -158,035,673.

The all-34 composite checker is now published but has not yet run from start to finish in one process. Its bounded `[start_index,end_index)` mode supports reproducible complete coverage. Exact `Fraction` arithmetic has no rounding error in these comparisons.

### Counting against the historical author-level certificate union

The 34 original pairs all satisfy (9\le i\le21, 48\le j\le54, i<j). Their 34 transposes are distinct. They do not overlap the documented exact sets/ranges of PREFIX-741, 742, 743, 744, 745 or 746. The old PREFIX-712 sufficient test is negative for each, and PREFIX-713/716/718 are confined to different high-index ranges according to the preceding source notes. With the PREFIX-746 **conditional** historical union of 141,972 certified cells, this gives
[
141,972+68=142,040,\qquad
\frac{142,040}{147,456}=\frac{17,755}{18,432}
\approx96.32703993\%,
\qquad 147,456-142,040=5,416.
]
The **68-cell theorem is unconditional inside the frozen auxiliary model once the source recurrence and exact calculation are verified**. The **96.3270% historical union remains author-level and conditional** on the previous global certificate ledger; a full independent union audit is open.

## Theorem 2: nested refinement is convergent and relatively complete

The following result applies to the same finite Gamma auxiliary model and every fixed closed rational rectangle (R\subset[0,1]^2), independent of the numerical table.

Let
[
F(p,z,t)=W(e)-M_2(p,z)+\mu(p,z)^2-t(\mu(e)-\mu(p,z)),\quad
m_R=\min_{(p,z)\in R,,0\le t\le1/2}F(p,z,t).
]
For each positive integer (r), let (G_r(R)) be the least exact corner/endpoint lower bound over an (r\times r) equal subdivision of (R). Let
[
U=\sup_R\mu,quad B_\mu=\sup_R(|\partial_p\mu|+|\partial_z\mu|),\quad
B_2=\sup_R(|\partial_p M_2|+|\partial_z M_2|),\quad
h=\max(\operatorname{width}(R),\operatorname{height}(R)).
]
All constants are finite: the 189-row finite Gamma mixture has polynomial rational moments in ((p,z)), hence these functions and derivatives are continuous on the compact square. (Rational coefficient-norm upper estimates may replace these suprema.)

Then:
[
\boxed{0\le m_R-G_r(R)\le
\frac{h}{r}\big[B_2+(2U+1/2)B_\mu\big].}
]
Moreover, when (r\mid s), (G_r(R)\le G_s(R)\le m_R). Thus (G_{2^k}(R)\uparrow m_R). If (m_R>0), every integer
[
r>\frac{h[B_2+(2U+1/2)B_\mu]}{m_R}
]
certifies (G_r(R)>0). Conversely, (m_R\le0) precludes a **strictly positive uniform** certificate of this type for that rectangle.

**Proof.** For each subrectangle (Q), let (L=\mu(Q_{\mathrm{lower}})) and (H=M_2(Q_{\mathrm{upper}})), and choose any (x=(p,z)\in Q), (0\le t\le1/2). Writing \(\ell_Q(t)=W(e)-H+L^2-t(\mu(e)-L)\), coordinate monotonicity gives \(\ell_Q(t)\le F(x,t)\).
The exact difference is
[
F(x,t)-\ell_Q(t)=[H-M_2(x)]+[\mu(x)^2-L^2]+t[\mu(x)-L].
]
For a subrectangle side length at most (h/r), the three nonnegative terms sum to at most
[
\frac{h}{r}B_2+\left(2U+\frac12\right)\frac{h}{r}B_\mu.
]
Choosing a subrectangle and endpoint realizing (G_r(R)) gives (m_R\le G_r(R)+Kh/r). Every subrectangle's bound is valid on its domain, so (G_r(R)\le m_R). Subdivision cannot lower an individual corner bound because the lower-mean corner moves upward and the upper-moment corner moves downward; this gives monotonicity under nested refinement. Both claims follow. \(\square\)

**Implication for the research route.** The 8x8 result at ((11,53)) is a small but strictly positive exact margin. Refinement is guaranteed to capture any true compact-cell gap with strictly positive (m_R), while a genuine nonpositive (m_R) would require a different comparison point or analysis, rather than indefinite refinement. This separates finite-resolution certificate weakness from mathematical failure of the witness.

## Files and next work

- `PREFIX747_R6_GAMMA_68_EXACT.py`: complete checker, with bounded batch mode, exact assertions and disjoint reflected-count checks.
- `PREFIX747_R6_GAMMA_68_RESULTS.json`: all 34 exact microfloors, prior-union provenance and remaining conditions.
- Previous frozen kernel: `PREFIX741_R6_INNER_STRIP_194.py`.

Next: run the published composite checker over all 34 rows, independently audit the prior historical union, then test (8\times8/16\times16) near ((10,52),(11,54)) and consider changing the witness if the exact (m_R) obstruction is encountered.
