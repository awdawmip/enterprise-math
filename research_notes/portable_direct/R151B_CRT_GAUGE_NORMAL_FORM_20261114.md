# R151B — Exact gauge-normal form and complete classification of CRT covariance waveforms

Date: 2026-11-14 (Asia/Shanghai).  
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged).  
Scope: external S23 scalar joint-CRT residue covariance; not a native X6 equivalence.  
Status: author-side proof with exact finite verification, NOT_REVIEWED.  
Predecessors: R150 (exact lag inverse) and R151 (clock-origin gauge obstruction).

## R151B.1: One residue completely classifies the waveform

Fix integers \(n,m\ge1\), \(g=\gcd(n,m)\), and \(s,t,u,v\in\mathbb Z\), with \(\gcd(s,n)=\gcd(t,m)=1\). For \(g>1\), let \(\ell=s^{-1}\pmod g\) and set

\[
\boxed{\rho=(v-t\ell u)\bmod g\in\{0,1,\ldots,g-1\}.}\tag{1}
\]

Let \(q=(g-1)/2\) and define

\[
A_j=((sj+u)\bmod g)-q,\quad B_j=((tj+v)\bmod g)-q,\quad
F(h)=\frac1{gnm}\sum_{j=0}^{g-1}A_jB_{j+h}.\tag{2}
\]

**Theorem.** The complete covariance sequence obeys the *gauge-normal derivative law*

\[
\boxed{nm\bigl[F(h+\ell)-F(h)\bigr]=((th+\rho)\bmod g)-\frac{g-1}{2}}\quad(h\in\mathbb Z).\tag{3}
\]

Conversely,

\[
\boxed{\rho=nm[F(\ell)-F(0)]+\frac{g-1}{2}\in\{0,\ldots,g-1\}.}\tag{4}
\]

For fixed \((n,m,s,t)\), two offset pairs \((u,v),(u',v')\) yield **identical complete lag-covariance waveforms** if and only if

\[
\boxed{v-t\ell u\equiv v'-t\ell u'\pmod g.}\tag{5}
\]

Equivalently, there is a common-clock translation \(r\) for which \(u'\equiv u+sr\) and \(v'\equiv v+tr\pmod g\). There are exactly \(g\) distinct complete waveforms among the \(g^2\) offset pairs modulo \(g\), each waveform having \(g\) offset-pair representatives.

**Proof.** R150 gives \(nm[F(h+\ell)-F(h)]=B_{j_*+h}\) with \(j_*=-u\ell\pmod g\). But \(t(j_*+h)+v\equiv th+(v-t\ell u)\equiv th+\rho\pmod g\). This proves (3) and, at \(h=0\), (4). If two waveforms agree then (4) forces their \(\rho\)'s to agree. Conversely equal \(\rho\) makes the increments (3) identical. Since \(\ell\) is a unit, the sequence of increments traverses all \(g\) lags and determines the waveform up to a constant; the constant is fixed by \(\sum_{h=0}^{g-1}F(h)=0\). Thus the whole waveforms agree. Choosing \(r=\ell(u'-u)\) aligns the first offsets, and equality of \(\rho\) aligns the second, establishing equivalence to common translation. For fixed \(\rho\), \(u\) can be chosen arbitrarily and \(v\equiv\rho+t\ell u\pmod g\) follows; hence the orbit and waveform counts. QED.

For \(g=1\), \(F(0)=0\) and there is exactly one offset class and one zero waveform. The above classification extends by putting \(\rho=0\), without requiring a modular inverse modulo 1.

## R151B.2: Optimal compression *for the waveform observer*

At fixed \(n,m,s,t\), the entire \(g\)-term exact covariance waveform is a deterministic injective function of the single residue \(\rho\); equation (4) recovers that residue. Thus \(\rho\) is an exact, complete, minimal-cardinality sufficient statistic for *this waveform observer*: the observable has \(g\) distinct values, so any encoding that distinguishes all of them requires at least \(g\) distinct codewords or \(\lceil\log_2 g\rceil\) fixed-width bits. This is an observer-specific state-compression certificate, not a claim about retaining full independent residue streams or pointwise Sturmian phase-fiber counts.

An explicit reconstruction algorithm uses the \(g\) increments (3), follows the permutation \(h_i=i\ell\bmod g\), integrates once with \(P_0=0\), and subtracts the mean of the \(g\) partial sums to enforce \(\sum F=0\). It uses \(O(g)\) rational arithmetic operations and \(O(g)\) output; deriving \(\rho\) from one supplied full-waveform observation uses \(F(0)\) and \(F(\ell)\). Bit costs depend on input sizes.

## R151B.3: Sturmian specialization and retained absolute cuts

For a length-\(M\) finite Sturmian word \(w\), let its reduced strict slope endpoints be \(\alpha=a/b<\beta=c/d\) with absolute intercept cuts \(U,V\) as in R146. Its mixed CRT component is (2) under

\[
(n,s,u;m,t,v)=(b,a,-U;d,-c,V).
\]

Consequently, whenever \(g=\gcd(b,d)>1\),

\[
\boxed{\rho_w=(V-c\,a^{-1}U)\bmod g.}\tag{6}
\]

For the two actual length-five words in R151,

\[
w_A=01001,\quad(U,V)=(3,0),\qquad
w_B=10010,\quad(U,V)=(4,1)
\]

both have \((a,b;c,d)=(1,4;1,2)\) and \(\rho_w=1\), hence identical waveform \((-1/32,1/32)\). But \(C_A(K)\ne C_B(K)\) at every \(K=4q+2\). This is an exact operational contrast: \(\rho\) gives a lossless quotient for the *mixed CRT covariance waveform* and fails as a sufficient quotient for the *pointwise integer phase-fiber count*. The full slope/intercept cuts \(a,b,c,d,U,V\) suffice for the latter via R146's integer floor/ceil formula.

## Exact validation and next frontier

The standalone exact Python program R151B_check.py checks \(g=1,\ldots,10\), all units \(s,t\), offsets \(u,v\) modulo \(g\), verifies (3) at every lag, the injectivity of the \(g\) different \(\rho\) signatures and equality within each class. It reports **7,953** configurations, **66,021** exact derivative comparisons and **134** fixed-\((g,s,t)\) complete waveform classifications. An independent full-lcm direct joint-clock covariance check uses \((n,m,s,t,u,v)=(4,6,3,5,1,-2)\), yielding \(g=2,\rho=1,F=(-1/96,+1/96)\). All arithmetic is exact Python integers/Fraction. Program output marker: R151B_CRT_GAUGE_NORMAL_FORM_PASS.

Further research: for fixed finite Sturmian word length \(M\), classify which \(\rho\)-orbits are realized by actual word support intervals and identify the least absolute cut augmentation needed for pointwise presence and its future transitions. In particular, test whether a smaller typed repair than the pair \((U,V)\) is sufficient when the target is only the binary presence sequence over all \(K\), not the full multiplicity sequence. The global conjecture for all-length saturation remains \(T(M)=(M-2)\lfloor(M-1)/2\rfloor+1\) for \(M\ge5\).

Independent review: NOT_REVIEWED; no formal Task/CLAIM or native X6 admission is inferred.