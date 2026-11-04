# D25 — second-parameter-jet elimination by a finite first-jet adjoint (original 216)

2026-11-05 · **TASK_RESEARCH author-side** · Research logical conversation: \`chatgpt-research-onhour-enterprise-math-20260923\`.
Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`. Publication: \`TP2-B6F4FC938FF94941C1B7\`.
Scientific source pin unchanged: \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.
Classification: **EXACT FINITE-ADJOINT THEOREM / ORIGINAL-SOURCE PARAMETER-JET PROOF / 80 FINITE-PRIME CHECKS / AUTHOR-PUBLISHED / UNREVIEWED / NOT_ADMITTED**.
The original fixed-class native H0/B0 experiment is separately **NOT_RUN/PENDING_OWNER (#1559)**.

## 1. An exact finite deformation of the original weighted 216 sum

Let \(n\ge1\) be an integer, \(K=2n,\ N=3n\), and write
\[
 a_\varepsilon=-3n+\varepsilon/2,\qquad
 b_\varepsilon=-2n+\varepsilon/3,\qquad
 c_\varepsilon=-4n+2\varepsilon/3,
\]
\[
 f_k(\varepsilon)=
 \frac{(a_\varepsilon)_k(b_\varepsilon)_k(c_\varepsilon)_k}{(k!)^3},
 \qquad f_{k,j}=[\varepsilon^j]f_k(\varepsilon)\quad(j=0,1,2).
\]
All these coefficients lie in \(\mathbb Q\). At a prime \(p=6n+1\), setting \(\varepsilon=p\) gives the *original* upper parameters \(1/2,1/3,2/3\), and evaluating at \(t=1/2\) gives exactly the 216 denominator of the original source. The original weight is retained as \(6k+1\). No coordinate, source model or cutoff is changed.

Put \(w_k=f_{k,0},\ v_k=f_{k,1},\ u_k=f_{k,2}\), and
\[
 P(\theta,\varepsilon)=(\theta+a_\varepsilon)
   (\theta+b_\varepsilon)(\theta+c_\varepsilon)
   =P_0(\theta)+\varepsilon P_1(\theta)
      +\varepsilon^2P_2(\theta)+\varepsilon^3/9,
\]
where
\[
\begin{split}
P_0(x)&=(x-3n)(x-2n)(x-4n),\\
P_1(x)&=\tfrac12(x-2n)(x-4n)
       +\tfrac13(x-3n)(x-4n)
       +\tfrac23(x-3n)(x-2n),\\
P_2(x)&=\tfrac{13}{18}x-2n.
\end{split}
\]
For \(k\ge1\) the exact rational coefficient recurrences are
\[
\begin{split}
 k^3w_k&=P_0(k-1)w_{k-1},\\
 k^3v_k&=P_0(k-1)v_{k-1}+P_1(k-1)w_{k-1},\\
 k^3u_k&=P_0(k-1)u_{k-1}+P_1(k-1)v_{k-1}
                                 +P_2(k-1)w_{k-1},
\end{split}\tag{1}
\]
with \(w_0=1,\ v_0=u_0=0\). These follow by comparing powers of \(\varepsilon\) in \(k^3f_k(\varepsilon)=P(k-1,\varepsilon)f_{k-1}(\varepsilon)\).

## 2. Main theorem: exact finite adjoint eliminates the second-jet sequence

Let \(t=1/2\), \(h_k=(6k+1)t^k\), and define the *backward* rational dual weights
\[
 \lambda_N=h_N,\qquad
 \lambda_k=h_k+\frac{P_0(k)}{(k+1)^3}\lambda_{k+1}
 \quad(k=N-1,\ldots,1).
\]
The original half-sum's second-parameter-jet coefficient \(S_2\), which was previously evaluated by differentiating every summand twice, is **exactly**
\[
\boxed{
 S_2=\sum_{k=1}^{N}\frac{\lambda_k}{k^3}
 \left(P_1(k-1)v_{k-1}+P_2(k-1)w_{k-1}\right).
}\tag{2}
\]
This is an equality in \(\mathbb Q\), not an asymptotic or modular approximation.

**Proof.** Set \(r_k=P_0(k-1)/k^3\), \(b_k=(P_1(k-1)v_{k-1}+P_2(k-1)w_{k-1})/k^3\).
Equation (1) gives \(u_k-r_ku_{k-1}=b_k\).
Multiply by \(\lambda_k\), sum \(1\le k\le N\) and shift the \(r_k u_{k-1}\) summand. Its coefficient of \(u_k\) becomes \(\lambda_k-r_{k+1}\lambda_{k+1}=h_k\) for \(k<N\), and \(\lambda_N=h_N\). The initial term vanishes since \(u_0=0\). Thus
\[
\sum_{k=1}^N\lambda_k b_k
=\sum_{k=1}^N h_k u_k=S_2.
\]
QED.

The exact *single-zero-factor* cut is visible as \(P_0(K)=0\), hence \(\lambda_K=h_K\): the lower dual kernel \(1\le k\le K\) is insulated from the upper \(K+1\le k\le N\) recurrence. Also \(w_k=0\) for \(k>K\), so the upper-block forcing in (2) contains **only the first parameter jet \(v_{k-1}\)**. Thus the unknown second derivative is replaced by an explicit first-jet forcing plus a source-specific adjoint observer, with both original blocks and signs preserved.

## 3. One first-jet endpoint controls the nonzero terminal source

At the original cutoff \(N=3n\), \(P_0(N)=0\) and \(w_N=0\), while \(P_1(N)=-n^2/2\). Equation (1) therefore gives the *exact rational* endpoint identity
\[
\boxed{
 f_{N+1,2}=-\frac{n^2v_N}{2(N+1)^3}
          =-\frac{n(2n)!(4n)!}
                  {6(3n+1)^3((3n)!)^2}\ne0.
}\tag{3}
\]
Here \(f_{N+1,0}=f_{N+1,1}=0\), and the displayed second-jet coefficient is nonzero. To verify the factorial form, omit the two unique zero factors \(j=N\) and \(j=K\) from \((a_\varepsilon)_{N+1}\) and \((b_\varepsilon)_{N+1}\); their two slopes multiply to \(1/6\), leaving the signed products displayed in (3).

Define the weighted finite original polynomial
\[
Y_N(\varepsilon,t)=\sum_{k=0}^{N}(6k+1)f_k(\varepsilon)t^k
\]
and the ordered (noncommutative \(\theta t=t(\theta+1)\)) operator
\[
\mathscr L_\varepsilon
=(6\theta-5)\theta^3-t(6\theta+7)P(\theta,\varepsilon),
 \quad \theta=t\,d/dt.
\]
Direct coefficient cancellation gives the exact, untruncated-in-\(\varepsilon\) identity
\[
\mathscr L_\varepsilon Y_N
=-(6N+7)(6N+1)(N+1)^3 f_{N+1}(\varepsilon)t^{N+1}.
\]
Writing \(Y_{N,j}=[\varepsilon^j]Y_N\) and \(\mathscr L_\varepsilon=\mathscr L_0+\varepsilon\mathscr L_1+\varepsilon^2\mathscr L_2+\cdots\), its first three coefficients obey
\[
\begin{split}
 \mathscr L_0Y_{N,0}&=0,\\
 \mathscr L_0Y_{N,1}+\mathscr L_1Y_{N,0}&=0,\\
 \mathscr L_0Y_{N,2}+\mathscr L_1Y_{N,1}+\mathscr L_2Y_{N,0}
  &=B_nt^{N+1},
\end{split}\tag{4}
\]
with \(\mathscr L_j=-t(6\theta+7)P_j(\theta)\) for \(j=1,2\) and
\[
 \boxed{
 B_n=\frac{(18n+7)(18n+1)n(2n)!(4n)!}{6((3n)!)^2}.
 }\tag{5}
\]
Equation (4) is the **forced second-jet differential equation** with an explicit, nonzero terminating source; it is complementary to the finite adjoint (2).

At every prime \(p=6n+1\ge7\), all denominators in (1)–(5) are \(p\)-units. The previously verified original source's signed shell unit \(U_p\) is now accessible from *only the terminal first jet*:
\[
\boxed{U_p\equiv-2^{-(N+1)}f_{N+1,2}
       \equiv\frac{n^2 v_N}{2^{N+2}(N+1)^3}\pmod p.}\tag{6}
\]
This is precisely the unit in the previously proved original upper-shell identity
\(T_A(p)=-2U_p(3\theta+2)G_n(1/2)\pmod p\), with the original reflected \(G_n\).
The nonzero terminal source is not removed by differentiation or quotienting.

## 4. A first-jet-only equivalent certificate for the live third digit

The existing original three-jet theorem states
\[
\frac{W_p-p}{p^2}\equiv D_{\mathrm{center}}+S_2+T_A(p)\pmod p,
\quad D_{\mathrm{center}}=(S_0+pS_1-p)/p^2\pmod p,
\]
where the division uses the accepted first-digit congruence, and \(T_A\) is the signed *original* upper shell. Combining it with (2), (3), (6) gives the following **exact equivalent finite certificate**:
\[
\boxed{
D_{\mathrm{center}}+
\sum_{k=1}^{N}\frac{\lambda_k}{k^3}
 [P_1(k-1)v_{k-1}+P_2(k-1)w_{k-1}]
+2^{-N}f_{N+1,2}(3\theta+2)G_n(1/2)
\equiv0\pmod p.
}\tag{7}
\]
Every quantity in (7) is constructed by finite rational recurrences from **zeroth- and first-parameter-jet** data, a backward adjoint and the already established reflected terminal shell. In particular, the second parameter derivative \(u_k\) has disappeared from the *input requirements* of the live certificate. This is a reduction of the required parameter-jet order, not an all-prime proof that (7) vanishes. The original signed target, base, and boundary remain unchanged.

Equivalence is under the frozen parent scalar interface and the previous original-source upper-shell theorem. Neither the ordinary 216 arithmetic nor \(U_p\) has been identified with native fixed H0/B0 crystalline Frobenius.

## 5. Executed evidence, status and continuation

The executable, standard-JavaScript exact finite-field checker
\`research_notes/portable_direct/d25_first_jet_dual_elimination_checker_20261105.mjs\`
computes \(w,v,u\) directly by the formal parameter-coefficient recurrence, computes \(\lambda\) independently backwards, checks their two \(S_2\) sums and the signed endpoint \(U_p\), and enforces the block zero \(P_0(K)=0\).
**All 80 primes \(7\le p\le997,\ p\equiv1\bmod6\)** pass; 0 failures. Exact anchor tuples \((p,S_2,f_{N+1,2},U_p)\):
\[
 (7,4,6,4),\quad(13,0,6,3),\quad(19,18,4,2),
 \quad(139,4,77,108),\quad(373,240,166,83).
\]
This is finite validation of the implementation and reuses earlier anchor values; the rational identities (1)–(5) are proved by finite coefficient algebra.

**Mother objective:** frozen original D25/LIFT, ultimately \(\Delta_p-R_p=0\bmod p\) for \(p\equiv13,19\bmod24\). The all-prime vanishing of (7) is OPEN; construct a terminating, \(p\)-dependent adjoint/WZ formula pairing the dual forcing with \(D_{\mathrm{center}}\) and the signed shell. This is the next exact mathematical action.

**Native experiment:** the existing support issue #1559 is OPEN/PENDING_OWNER. Exact native original-class p=373 H0/B0 divided-power \([X]U\bmod139129\), module rank, semilinear \(F\) direction, normalization \(\eta\), signed odd Hesse/Green observer, native \(\kappa\), \(\Delta-R\), and independent reproduction remain **NOT_RUN**; this calculation is not a surrogate.

**Control:** ordinary Research lane \`chatgpt-research-onhour-enterprise-math-20260923\` only. Earlier own native session \`MCP-491afa3ba2b94ec9b900ed3df6e345a3\` was registered, but the private capability is unavailable in this run; no claim, run, native Source checkpoint, or formal Result is asserted. Original current continuation read is \`onhour11-20261105-0657-d25-public-cont\`; use its exact receipt/reconcile, never reissue it. The maintenance logical conversation has no authority transfer here.

**Do not rework:** accepted D24 UR/JT0; original weighted shell \(T_A\), reversed \(4F3\) and \(-p^2U_p\); original integer-centered three-jet; previous Sun/Green arithmetic scans; native H0/B0 remains a separate required experiment.
