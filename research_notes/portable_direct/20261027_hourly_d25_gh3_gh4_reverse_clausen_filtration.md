# D25/LIFT GH-3 and GH-4 — reverse Clausen single-port reduction and exact W/S Gauss filtration

2026-10-27 Asia/Hong_Kong. TASK_RESEARCH logical conversation: chatgpt-research-hourly-enterprise-math-20260923. Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / D25-LIFT-JT2 remains OPEN. **Scientific Source frozen** at c47e13e4aba0e006366f989d6334d443f6333ae3; this note does not modify it. Author-side: DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Mathematical Gauss indices are auxiliary coefficient indices, not native spatial axes; the underlying project ontology is P000's Heartbeat World native X6 + separately typed time when necessary.

Inputs, consumed without recredit: GH-2's original S Cl(a)usen carrier and labelled MM/LH sources, its proved combined conservation G_MM + G_LH = 0 for p ≡ 19 (mod 24), its separately identified two-valuation-band obstructions, and GH-1's different W Gauss carrier. Original S/W input and genuine finite cutoff remain unchanged. This note proves an exact single-hypergeometric-sum reduction of GH-2's separate-port question and the *entire* rational rank-diagonal carrier filtration, rather than asserting an unproved W/S supercongruence.

## GH-3. Reverse middle block and a single low-window hypergeometric obstruction

Fix any prime p ≡ 19 (mod 24), p ≥ 19, and write

\[
a=\frac{p-3}{8},\quad b=\frac{3p-1}{8},\quad h=\frac{p-1}{2}=a+b,\quad H=2b,\quad d=b-a-1=\frac{p-3}{4}.
\]

Keep the original GH-2 S Gauss carrier and its *normalized, labelled* middle coefficients:

\[
u_k=\frac{(1/8)_k(3/8)_k}{(k!)^2\,9^k},\qquad
\beta_i=(u_i/p)\bmod p,\quad a<i\le b.
\]

All \(\beta_i\) are nonzero in \(\mathbf F_p\). Define \(g_r=\beta_{b-r}/\beta_b\) for \(0\le r\le d\). This is a reverse-order observer of the original middle source, *not* a relabelling of native X6 states.

**Theorem GH3.1 (exact reverse recurrence).** For \(0\le r<d\),

\[
\frac{g_{r+1}}{g_r}\equiv
\frac{9(r+1/8)^2}{(r+1)(r+3/4)}\pmod p,\qquad
g_r\equiv9^r\frac{(1/8)_r^2}{r!(3/4)_r}\pmod p.
\]

All inverses used here are p-units on the stated interval.

**Proof.** The original recurrence is
\(u_{k+1}/u_k=(8k+1)(8k+3)/(576(k+1)^2)\).
Backward substitution \(k=b-r-1\) gives
\[
\frac{\beta_{b-r-1}}{\beta_{b-r}}\equiv
\frac{576(b-r)^2}{(8b-8r-7)(8b-8r-5)}
=\frac{9(r+1/8)^2}{(r+1)(r+3/4)}\pmod p,
\]
because \(8b=3p-1\). The quotient is between two middle p-normalized units. Multiply ratios from \(0\) to \(r-1\). QED.

Preserve GH-2's distinct middle-middle port

\[
G_{MM}=\sum_{h<n\le H}(8n+1)
 \sum_{\substack{a<i,j\le b\\i+j=n}}\beta_i\beta_j
 \quad\in\mathbf F_p.
\]

**Theorem GH3.2 (single-port equivalence, all primes in the frozen 19-class).** Put

\[
C_r=9^r\frac{(1/4)_r^3}{(1/2)_r(3/4)_r\,r!},\qquad
T_p=\sum_{r=0}^{d}(8r+1)C_r\bmod p.
\]

Then, **with the original source labels preserved,**

\[
\boxed{G_{MM}=-\beta_b^2T_p\pmod p,\qquad
G_{LH}=+\beta_b^2T_p\pmod p.}
\]

In particular \(G_{MM}=G_{LH}=0\) if and only if \(T_p=0\bmod p\). This is a reduction, not an unconditional proof of the last zero.

**Proof.** Substitute \(i=b-r,j=b-s\). The original high-degree cutoff \(i+j>h=a+b\) is exactly \(r+s\le b-a-1=d\); no sum term outside the original cutoff is inserted. Also
\(8(i+j)+1=8(2b-r-s)+1=6p-1-8(r+s)\equiv-(8(r+s)+1)\).
Consequently
\[
G_{MM}=-\beta_b^2\sum_{t=0}^{d}(8t+1)
          \sum_{r+s=t}g_rg_s.
\]
For each \(t\le d\), the exact classical Clausen identity
\[
{}_2F_1(1/8,1/8;3/4;z)^2
={}_3F_2(1/4,1/4,1/4;1/2,3/4;z)
\]
and GH3.1 give \(\sum_{r+s=t}g_rg_s=C_t\pmod p\). The first displayed identity follows without invoking the S truncation theorem. GH-2 established \(G_{MM}+G_{LH}=0\) using its genuine finite cutoff and the independently sourced Guo–Zudilin S-only truncation congruence, which gives the second identity. QED.

**Computational consequence.** The two apparently independent weighted double-source ports are controlled by one scalar \(T_p\) and the retained unit \(\beta_b^2\). The algebraic reduction permits \(O(p)\) single-pass modular checking instead of a quadratic convolution. It does *not* remove the labelled MM/LH joint input or grant a new native Hasse/WZ correspondence.

## GH-4. Complete p-adic cost of the exact rank-diagonal W-to-S Gauss ratio

Keep the *different* W Gauss carrier
\[
t_k=\frac{(1/6)_k(1/3)_k}{(k!)^2\,2^k},\qquad
u_k=\frac{(1/8)_k(3/8)_k}{(k!)^2\,9^k},\quad 0\le k<p
\]
for a prime \(p=6m+1\) in either frozen class. Define the exact nonzero rational ratio \(g_k=u_k/t_k\). Its recurrence is
\[
g_0=1,\qquad
\frac{g_{k+1}}{g_k}=
\frac{(8k+1)(8k+3)}{16(6k+1)(3k+1)}.
\]
A zero/pole in a modular ratio is represented by its **integer valuation**, not by silently deleting the rank.

**Theorem GH4.1 (five-band rank filtration).** Let \(\Delta_k=v_p(g_k)\).

* If \(p=24q+19\), set \(a=(p-3)/8,\ b=(3p-1)/8,\ m=(p-1)/6\). Then
\[
\Delta_k=
\begin{cases}
0&0\le k\le a,\\
+1&a<k\le m,\\
0&m<k\le2m,\\
-1&2m<k\le b,\\
0&b<k<p.
\end{cases}
\]
* If \(p=24q+13\), set \(a=(5p-1)/8,\ b=(7p-3)/8\). Then
\[
\Delta_k=
\begin{cases}
0&0\le k\le m,\\
-1&m<k\le2m,\\
-2&2m<k\le a,\\
-1&a<k\le b,\\
0&b<k<p.
\end{cases}
\]

**Proof.** For \(0\le k<p\), the W numerator factors acquire p exactly after \(k=m\) and \(k=2m\); denominator factorials are p-units. In the 19-class the S numerator acquires p after \(k=a\) and \(k=b\), with \(a<m<2m<b\). In the 13-class it acquires p after \(k=a,b\), with \(m<2m<a<b\). No other numerator factor contributes p before \(k=p\). Subtracting the two cumulative step-valuation profiles proves both piecewise formulas. QED.

For the fixed ordered rank population \(0,\ldots,p-1\), define \(E_+=\sum_k\max(\Delta_k,0)\), \(E_-=\sum_k\max(-\Delta_k,0)\).

**Corollary GH4.2 (global determinant blind spot vs pure pole deficit).**
\[
\boxed{
(E_+,E_-,\sum_k\Delta_k)=
\begin{cases}
((p+5)/24,(p+5)/24,0),&p\equiv19\pmod{24},\\
(0,p,-p),&p\equiv13\pmod{24}.
\end{cases}}
\]
Thus the determinant of the exact rational rank-diagonal gauge \(\operatorname{diag}(g_0,\ldots,g_{p-1})\) has p-valuation \(0\) in the 19-class, despite its isolated \(+1\) and \(-1\) bands, and p-valuation \(-p\) in the 13-class. In neither class is this diagonal map a \(GL_p(\mathbf Z_p)\) map on all ranks. The determinant is **only the fixed rank-diagonal gauge**: no obstruction to a suitably proved nonlocal rank-mixing, valuation-shifting or WZ correspondence is inferred.

**Proof.** In the 19-class both nonzero intervals have length \(q+1=(p+5)/24\), with opposite signs. In the 13-class the \(-1,-2,-1\) intervals have lengths \(m=4q+2,\ a-2m=7q+4,\ b-a=6q+3\); hence \(E_-=m+2(a-2m)+(b-a)=24q+13=p\). QED.

## Author exact checks, scope and next unit

The Python-stdlib companion to this note was actually executed: it independently checks the GH-3 port identity, reverse recurrence and finite convolution on all 155 primes \(p<10000,\ p\equiv19\bmod24\), with quadratic direct source checks for \(p<2000\). It observes \(T_p=0\) for all 1227 primes \(5\le p<10000\); this much wider *finite observation* is not a universal theorem and does not use the GH-2 reduction outside its 19-class hypotheses. GH-4 independently reconstructs every valuation step on all 312 frozen-class primes \(p<10000\), including 157 in the 13-class and 155 in the 19-class. Author computations were PASS. Theorem proofs above are algebraic; finite checks are non-independent evidence.

Witness filtration counts: \(p=13:(E_+,E_-)=(0,13)\), \(19:(1,1)\), \(43:(2,2)\), \(67:(3,3)\), \(139:(6,6)\), \(181:(0,181)\), \(373:(0,373)\).

**Next smallest science obligation:** prove/refute the single-sum congruence \(T_p=0\) uniformly, first in the 19-class and, separately, for all \(p>3\), without elevating a finite check to a theorem. Test a genuine algebraic finite-field/contiguous hypergeometric or WZ certificate. Then use the GH-4 exact defect bands to propose a filtration-aware *nonlocal* W/S rank map, and connect with GH-1/GH-2, R23's unchanged low-half discrepancy and R36's distinct finite PF Green operator. All original six fixed z=2 Hasse J/E sources, finite two-endpoint information, positive-direction infinity and Frobenius η/κ remain typed obligations. Original H0/B0, [X]U mod p², p=373 native experiment, canonical checkpoint and independent Driver admission remain pending.

**Control and preservation:** Most recent direct gateway 0.6.11 status in this run reports research_authority_granted=false and executor_binding_configured=false. An attempted exact read-only control_continuation returned INVALID_ARGUMENT / CONTROL_QUOTA before a usable packet. Previous exact recovery/continuation evidence and historical predecessor-claim conflict are recorded in enterprise-math#1558 and GH-2; no current claim/open/run was established in this run. This note is portable research, not Source-authenticated completed predecessor research, registered Research-Activity, formal Result, review or P000 change. Preserve the Research lane's stable logical ID and old session/staging provenance; do not reuse maintenance identity or the rejected historical request.
