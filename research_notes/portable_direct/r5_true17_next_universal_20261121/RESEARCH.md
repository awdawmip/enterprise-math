# R5 — Genuine-incidence primitive-17 next Laurent coefficient: universal nonvanishing

Scientific date: 2026-11-21. Evidence state: **AUTHOR_EXACT_DERIVATION / TWO_EXACT_ALGORITHMS_CHECKED / NOT_REVIEWED**. Frozen R5 inputs and original five failure events are unchanged. This note continues immutable predecessor \`enterprise-math@1ac65225046de8ae8213f1c5156403cea61b0f36:research_notes/portable_direct/r5_true17_phase_periodic_20261121/RESEARCH.md\`; it does not rewrite that note, claim a canonical review, or assert a new formal Task CLAIM/RUN.

## Theorem (all integer thresholds)

Let \(\zeta\) be any primitive 17th root, \(D=q\,d/dq\), and let \(R_m(q)\) be the **genuine five-event inclusion-exclusion numerator** in the frozen 101-price R5 model. For every \(m\ge1\), the primitive-17 contribution to \(F_m(q)=R_m(q)\prod_{p=214}^{314}(1-q^p)^{-1}\) has a nonzero \(N^5\) or \(N^4\) Fourier term in coefficient index \(N\). In particular, **every fixed positive threshold** satisfies
\[
 17\mid M_m\bigl(O_m(N^3)\bigr).
\]
Here \(M_m(O_m(N^3))\) means the minimal coefficient-quasipolynomial period when the permitted coefficient error is \(O_m(N^3)\). This is a necessary prime factor, not a complete numerical evaluation of \(M_m\).

The predecessor established \(R_m(\zeta)\ne0\) for \(m\bmod17=1,\ldots,12\), and \(R_m(\zeta)=0\) for \(m\bmod17\in\{13,14,15,16,0\}\). We now prove **infinite-threshold** nonvanishing of \(DR_m(\zeta)\) on the latter five classes.

Put \(r=13,14,15,16,17\) (17 represents residue zero), \(k\ge0\), and \(A_r=DR_r(\zeta)\), \(B_r=DR_{r+17}(\zeta)\), regarded as 16-coordinate vectors in \(\mathbb Z[\zeta]=\mathbb Z[z]/\Phi_{17}(z)\). Then the *whole vector* obeys
\[
 \boxed{DR_{r+17k}(\zeta)=
  \begin{cases}
    A_r+(k/2)B_r,&k\text{ even},\\
    ((k+1)/2)B_r,&k\text{ odd}.
  \end{cases}}
\]
The first basis coordinates, calculated exactly, are:

| r | first coordinate of A_r | first coordinate of B_r |
|---:|---:|---:|
|13|-13328|-29087|
|14|-6681|-10268|
|15|-7565|-17782|
|16|-12631|-25262|
|17|-4046|-6545|

Both entries are strictly negative in all five rows, so **every** vector in the displayed formula is nonzero for every \(k\ge0\). Since \(\Phi_{17}\) is irreducible, nonzero at one primitive 17th root means nonzero at each conjugate. At a zero of \(R_m\), the sixth-order pole of the complete Euler denominator loses exactly one order; a nonzero fifth-order primitive-17 pole gives a nonzero \(N^4\) Fourier term. A quasipolynomial of period not divisible by 17 cannot reproduce that term modulo \(O_m(N^3)\).

## Derivation of the universal 34-step denominator

Write \(R_A\) for the genuine union of overlapping events \(E_0,E_1,E_2\), and \(R_0\) for the single event \(E_0\). The independent 17-price block \(E_4\), and the block \(E_3\) with four 17-divisible prices, give at every primitive 17th root:
\[
 DR_m(\zeta)=DR_A(\zeta)-5202\lceil m/17\rceil(1-R_0(\zeta,m)).
\]
In the small overlapping block, denote \(a=a_{214},b=a_{215}\), let \(u\) be the total multiplicity of prices \(216,217,218\) and \(j\) the total multiplicity of prices \(219,220,221\). The three separate constraints are:
\[
 L_0=a+b+u<m,\quad L_1=a+u+j<m,\quad L_2=b+u+j<m.
\]
Put \(X=\zeta^{214}=\zeta^{10}\), \(Y=\zeta^{215}=\zeta^{11}\). Each grouped complete homogeneous sequence is a linear combination, **over the exact cyclotomic field**, of three exponentials \(U^u\), \(V^j\), with
\[
 U\in\{\zeta^{12},\zeta^{13},\zeta^{14}\},\qquad
 V\in\{\zeta^{15},\zeta^{16},1\}.
\]
The three roots in each group are distinct, so this follows by ordinary partial fractions of their exact rational generating functions. No approximation or collapsed-union constraint is used.

For any one such pair of characters \(U,V\), define \(P_I(t)=\sum_{m\ge1}P_{I,m}(\zeta)t^{m-1}\) for a genuinely constrained event intersection. Write \(T=t\) for readability. The following **exact rational kernels** enumerate the load maxima; the common factor \(1/(1-T)\) follows from \(\sum_{m>\max L}T^{m-1}=T^{\max L}/(1-T)\):

\[
P_1=\frac1{(1-T)(1-XT)(1-UT)(1-VT)},\quad
P_2=\frac1{(1-T)(1-YT)(1-UT)(1-VT)}.
\]
\[
P_{01}=\frac{1-YVT^2}
 {(1-T)(1-XT)(1-UT)(1-YT)(1-VT)(1-YVT)},
\]
\[
P_{02}=\frac{1-XVT^2}
 {(1-T)(1-YT)(1-UT)(1-XT)(1-VT)(1-XVT)},
\]
\[
P_{12}=\frac{1-XYT^2}
 {(1-T)(1-UT)(1-VT)(1-XT)(1-YT)(1-XYT)},
\]
\[
\boxed{P_{012}=
\frac{1-XYVT^3}
 {(1-T)(1-UT)(1-XT)(1-YT)(1-VT)(1-XYVT^2)}.}
\]
For instance, \(P_{012}\) uses
\(\max(a+b,a+j,b+j)=a+b+j-\min(a,b,j)\).
Partition the triples by the unique cases \(a\le b,j\), \(b<a,\ b\le j\), and \(j<a,b\). The three cone series sum to the displayed fraction; the numerator simplifies exactly to \(1-XYVT^3\). The other three intersections follow from \(\max(b,j)\), \(\max(a,j)\), or \(\max(a,b)\), with ties counted once.

Each linear denominator factor \(1-\zeta^sT\) divides \(1-T^{17}\). The quadratic factor \(1-XYVT^2\) divides \(1-T^{34}\). In every listed term, every complex root has multiplicity at most two: the only possible collision involving the quadratic factor is \(V=\zeta^{16}\), when \(XYV=X^2\); and the possible \(V=1\) collisions among the linear factors are at most double. These claims can also be checked directly from the exponent sets \(\{10,11,12,13,14,15,16,0\}\) modulo 17.

Therefore **every kernel denominator divides \((1-T^{34})^2\)**. Their numerator degrees after multiplying by that common denominator are at most \(64\): for \(P_1,P_2\), denominator degree 4 and numerator degree 0; for \(P_{01},P_{02},P_{12}\), degrees 6 and 2; for \(P_{012}\), degrees 7 and 3. In each case \(68-\deg(\mathrm{denominator})+\deg(\mathrm{numerator})=64\).

The derivative of the true overlapping union is
\[
 DR_A(\zeta,m)=DR_0(\zeta,m)-221\,B_m,
\]
where
\[
 B_m=W_1P_{1,m}+W_2P_{2,m}
 -W(P_{01,m}+P_{02,m}+P_{12,m})+WP_{012,m},
\]
\(W_1=\prod_{p\in S_1\setminus\{221\}}(1-\zeta^p)\),
\(W_2=\prod_{p\in S_2\setminus\{221\}}(1-\zeta^p)\), and
\(W=\prod_{p\in(S_0\cup S_1\cup S_2)\setminus\{221\}}(1-\zeta^p)\).
Thus \(B(T)=H_B(T)/(1-T^{34})^2\) with \(\deg H_B\le64\).

For completeness, put \(W_0(q)=\prod_{p=214}^{218}(1-q^p)\), \(Q(T)=\prod_{s\in\{1,\ldots,16\}\setminus\{10,\ldots,14\}}(1-\zeta^sT)\), \(\deg Q=11\). The single-event leading series is \(W_0(\zeta)Q(T)/(1-T^{17})\). Differentiating in \(q\) before evaluating at \(q=\zeta\) shows \(\sum_m DR_{0,m}(\zeta)T^{m-1}\) has denominator \((1-T^{17})^2\) and numerator degree at most 28. Finally
\[
\sum_{m\ge1}\lceil m/17\rceil(1-R_0(\zeta,m))T^{m-1}
=\frac{(1+T+\cdots+T^{16})-W_0(\zeta)Q(T)}
{(1-T^{17})^2}.
\]
Changing these two denominators to \((1-T^{34})^2=(1-T^{17})^2(1+T^{17})^2\) raises their numerator degrees to at most 62 and 50. Hence:
\[
\boxed{\sum_{m\ge1}DR_m(\zeta)T^{m-1}
=\frac{H_{17}(T)}{(1-T^{34})^2},\quad
\deg H_{17}\le64.}
\]
Extracting the coefficient of \(T^{m+67}\), which always lies above the numerator degree for \(m\ge1\), yields the **full-field identity**
\[
\boxed{DR_{m+68}(\zeta)-2DR_{m+34}(\zeta)+DR_m(\zeta)=0
\quad(m\ge1).}
\]

## Finite exact base certificate and the all-m lift

The predecessor's exact incidence program and an independent maximum-load generating-kernel convolution were used at the four blocks \(m=r,r+17,r+34,r+51\), \(13\le r\le17\). In \(\mathbb Z[\zeta]\), all five pairs of identities
\[
 DR_{r+34}=DR_r+DR_{r+17},\qquad
 DR_{r+51}=2DR_{r+17}
\]
hold as **complete 16-coordinate vector equations**, not only by one plotted or floating coordinate. The two exact algorithms agree at 20 checked thresholds; the independent generating-kernel calculation computed all \(m=1,\ldots,68\). The previous exact published leading-phase certificate was also reused; no theorem relies on unreviewed local claims beyond its declared scope.

The 68-step recurrence applies to each parity subsequence \(r,r+34,r+68,\ldots\) and \(r+17,r+51,r+85,\ldots\). The two displayed base identities then prove the formula in the theorem for every \(k\ge0\). The strictly negative first coordinates above complete the nonvanishing proof.

## Exact reproducibility and boundaries

- \`VERIFY_FAST.py\` implements genuine individual event masks in the cyclotomic ring at thresholds needed for the universal certificate.
- \`VERIFY_KERNELS.py\` independently builds threshold generating functions using max-of-load kernels and convolution rather than enumerating each threshold's masks.
- \`RESULT.json\` records the base coordinates, exact vector-equality checks, and tested coverage; no floating-point arithmetic.
- The integer64 path is exact on the declared \(m\le68\) validation window: positive unweighted count bounds (at most \(68^4\binom{70}{2}^2\) for a four-group sum, multiplied by at most \(2^7\) for a seven-factor \(W\)) remain below \(2^{63}-1\); independent intersection and final output vectors are also far below the bound. For unbounded numerical experiments use arbitrary-precision integers.
- The universal extension itself is **symbolic**, by the rational kernel identity and finite 20-vector certificate. Independent mathematical review remains open. No statement here promotes a native BRC/Heartbeat physical interpretation: this is a fixed scalar counting model whose source/error residuals retain their declared type.

## Next work

Recheck the affected second Laurent coefficients at primitive 11th and 13th roots with the same genuine-event incidence, then combine independently certified necessary factors and a complete pole-order upper bound to rebuild the **numerical** strict minimum-cost quasipolynomial period at \(O_m(N^3)\). Historical invalid four-class periodicity claims remain preserved as corrected history; they are not inputs to this result.
