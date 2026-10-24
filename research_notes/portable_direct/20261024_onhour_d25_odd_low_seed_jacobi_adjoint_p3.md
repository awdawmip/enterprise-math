# D25/LIFT — odd LOW seed cancellation by a Jacobi adjoint, and its complete third-digit jet

2026-10-24 | original on-hour TASK_RESEARCH lane | **AUTHOR EXACT PROOF + EXECUTED CHECKER; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Not a Source run/checkpoint, native benchmark, Result, CM admission or independent review.

**Authority / provenance.** Mother objective \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; **frozen scientific Source pin** \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, unchanged. This author's stable ordinary logical research lane is \`chatgpt-research-onhour-enterprise-math-20260923\`; it is not the maintenance lane \`chatgpt-hourly-enterprise-math-20260921\` nor the separate hourly Researcher lane. Consume rather than re-credit: original exact all-rank WZ/FIVE from \`c7fb90fd7ec451a954b553b963dd85d4ec99fc96\`, fixed-p five-port transport to p³ from \`7724e73f2d15c92ce98520e6a55b8231d737fa03\`, odd-seed valuation and 103/1500 terminal pair from \`89963639c6616698dc596672fdcc1264f38da030\`, and even-seed Jacobi cancellation/jet from \`5404753a7a923c4ca9a3654256c057db878a7f35\`. The other lane's latest top-edge WZ seam \`20261024_hourly_d25_original_top_edge_wz_seam_bridge.md\` is a separate source and is not claimed here.

## 1. Original immutable object and exact odd parameterization

For every integer r>=0, retain the actual original source expression

\[
A_r=\frac{(6r)!}{3^{6r}((2r)!)^3},\qquad
R_{r,0}=1,\qquad
\frac{R_{r,n+1}}{R_{r,n}}=
\frac{(4r+2n+1)(3n+1)(3n+2)}
{36(n+1)(2r+n+1)(4r+n+1)},
\]
\[
T_{r,n}=A_r(6n+12r+1)R_{r,n},\qquad
S_r=\sum_{n=0}^{4r}T_{r,n}.
\]

Fix **any prime** \(p=12r-5\ge19\), with integer r>=2. This includes every hard-target \(p\equiv19\pmod{24}\) (r even), and also \(p\equiv7\pmod{24}\) (r odd, p>=31). Let

\[
N=4r,\quad K=N-3=4r-3,\quad p=3K+4.
\]

Thus K is odd. The target prime's upper rank is m=2r-1 and its original LOW rank is r=ceil(m/2).

The source-fixed hypergeometric factor has the **exact Q parameterization**

\[
R_{r,n}=
\frac{(-K+p/2)_n\,(-K-1+p/3)_n\,(2/3)_n}
{2^n n!\,(1/2-K+p/2)_n\,(8/3+p/3)_n}. \tag{1}
\]

For \(0\le n\le K\), all unshifted numerator and denominator factors are p-units. Put

\[
u_n=\frac{(-K)_n(-K-1)_n}{(1/2-K)_n\,n!\,2^n},\qquad
c_n=u_n\frac{(2/3)_n}{(8/3)_n}
=\frac{10u_n}{(3n+2)(3n+5)}. \tag{2}
\]

The source's last three original terms are \(U=T_{r,K+1}\), \(V=T_{r,K+2}\), \(W=T_{r,K+3}\). The inherited, already proved valuation theorem says v_p(T_(r,n))=0 for n<=K; v_p(U)=1 and v_p(V)=v_p(W)=2. **None of these original ports is discarded.**

## 2. Theorem A — exact Jacobi-adjoint cancellation factor for every odd K

For any odd positive integer K, not necessarily attached to a prime, let

\[
F_K(x)=\sum_{n=0}^{K}
\frac{(-K)_n(-K-1)_n}{(1/2-K)_n\,n!}x^n,\qquad
M_s(K)=\sum_{n=0}^{K}\frac{u_n}{n+s}.
\]

These are exact rational numbers for s=2/3 and 5/3. **Theorem A:**

\[
\boxed{
\sum_{n=0}^{K}(n+1)c_n
=(3K+4)L_K,\qquad
L_K=\frac5{27}\left[
4M_{2/3}-(3K+9)M_{5/3}+3F_K(1/2)
\right].} \tag{A}
\]

This is an exact identity **over Q** and is stronger than a finite-field observation. It explicitly exhibits the missing factor \(3K+4\).

**Proof, step 1: exact odd-degree Jacobi boundary.** Hypergeometric coefficient recurrence gives

\[
x(1-x)F_K''+(1/2-K+2Kx)F_K'-K(K+1)F_K=0.
\]

For \(P_K(t)=F_K((1+t)/2)\), this becomes

\[
(1-t^2)P_K''+(1+2Kt)P_K'-K(K+1)P_K=0. \tag{3}
\]

The degree-K polynomial solution is, up to a nonzero rational scalar, the Jacobi polynomial with \(\alpha=-K-3/2,\ \beta=-K-1/2\). Its Rodrigues representation is

\[
P_K(t)\sim (1-t)(1-t^2)^{K+1/2}
\frac{d^K}{dt^K}\left[(1+t)(1-t^2)^{-3/2}\right]. \tag{4}
\]

Both the Jacobi equation and (4) are algebraic terminating polynomial identities for this integral K. Polynomial uniqueness follows by the original Taylor coefficient recurrence at x=0, where all denominators \((n+1)(n+1/2-K)\) are nonzero.

Write \(g(t)=(1+t)(1-t^2)^{-3/2}=\sum_{h\ge0}a_h(t^{2h}+t^{2h+1})\), with \(a_h=(3/2)_h/h!\). The prefactor in (4) has logarithmic derivative -1 at t=0. For K=2h+1 odd,

\[
\frac{g^{(K+1)}(0)}{g^{(K)}(0)}
=(K+1)\frac{a_{h+1}}{a_h}
=(K+1)\frac{h+3/2}{h+1}=K+2.
\]

Consequently

\[
\boxed{F_K'(1/2)/2=(K+1)F_K(1/2).} \tag{5}
\]

**Proof, step 2: exact weighted-adjoint integration.** Let \(y(z)=F_K(z/2)\). It satisfies

\[
z(2-z)y''+(1-2K+2Kz)y'-K(K+1)y=0. \tag{6}
\]

For s=5/3, multiply (6) by \(h(z)=z^{s-1}\), integrate exactly from 0 to 1, and integrate by parts twice. The lower boundary vanishes since s>1. The upper boundary is \(y'(1)+(2-s)y(1)=(K+4/3)y(1)\) by (5). The formal adjoint has coefficients

\[
(ha)''-(hb)'-K(K+1)h
=(s-1)(2s+2K-1)z^{s-2}
-(s+K)(s+K+1)z^{s-1},
\]

where \(a=z(2-z)\), \(b=1-2K+2Kz\). Since \(\int_0^1 z^{s-1}y(z)\,dz=M_s(K)\), the result is the exact rational identity

\[
\boxed{
2(6K+7)M_{2/3}
-(3K+5)(3K+8)M_{5/3}
=-3(3K+4)F_K(1/2).} \tag{7}
\]

Write \(q=3K+4\) in (7) and collect terms:

\[
M_{2/3}+2M_{5/3}
=\frac q2\left[
4M_{2/3}-(q+5)M_{5/3}+3F_K(1/2)
\right]. \tag{8}
\]

Finally the exact partial fraction identity

\[
\frac{10(n+1)}{(3n+2)(3n+5)}
=\frac{10}{9}\left(\frac1{3n+2}+\frac2{3n+5}\right)
\]

gives \(\sum(n+1)c_n=\frac{10}{27}(M_{2/3}+2M_{5/3})\). Substitution of (8) yields (A). QED.

**New all-prime corollary.** For p=12r-5>=19 prime, all denominators in (2), (A) and (8) are p-units: \(K<p\), \(2K<p\), \(3n+2\le p-2\), and the numbers \(3n+5\) for n<=K skip p (maximum p+1). Thus \(L_K\in\mathbb Z_{(p)}\). The scalar in the exact original LOW sum is \(6n+12r+1=p+6(n+1)\), while U,V,W vanish modulo p. Therefore

\[
S_r\equiv 6A_r\sum_{n=0}^K(n+1)c_n
=6pA_rL_K\equiv0\pmod p. \tag{9}
\]

**This proves, for the entire odd-m hard-target class \(p\equiv19\pmod{24}\), the previously missing original LOW-seed first-digit cancellation.** It also holds for p≡7 mod24, p>=31. This is not an assertion about the terminal S_m modulo p³.

## 3. Theorem B — exact source-faithful p³ seed jet, including nonzero tail pair

For \(0\le n\le K\), define p-integral finite harmonic jets (empty sums zero):

\[
\begin{aligned}
D_n={}&\frac12\sum_{j=0}^{n-1}\frac1{j-K}
+\frac13\sum_{j=0}^{n-1}\frac1{j-K-1}
-\sum_{j=0}^{n-1}\frac1{2j+1-2K}
-\sum_{j=0}^{n-1}\frac1{3j+8},\\
E_n={}&\frac14\sum_{j=0}^{n-1}\frac1{(j-K)^2}
+\frac19\sum_{j=0}^{n-1}\frac1{(j-K-1)^2}
-\sum_{j=0}^{n-1}\frac1{(2j+1-2K)^2}
-\sum_{j=0}^{n-1}\frac1{(3j+8)^2}.
\end{aligned} \tag{10}
\]

Each displayed denominator is a p-unit in the stated index range. Taking the first and second exact logarithmic derivatives of the four finite Pochhammer factors in (1) proves, term by term in \(\mathbb Z_{(p)}\),

\[
\boxed{R_{r,n}\equiv c_n
\left[1+pD_n+\frac{p^2}{2}(D_n^2-E_n)\right]\pmod{p^3},
\qquad 0\le n\le K.} \tag{11}
\]

Set

\[
C=\sum_{n=0}^Kc_n,\quad
N_D=\sum_{n=0}^K(n+1)c_nD_n,\quad
D_C=\sum_{n=0}^Kc_nD_n,\quad
N_E=\sum_{n=0}^K(n+1)c_n(D_n^2-E_n).
\]

The inherited **exact** terminal-pair theorem (not re-proved here) is
\(V+W\equiv (103p/1500)U\pmod{p^3}\), and v_p(U)=1.

**Theorem B:** For every prime p=12r-5>=19,

\[
\boxed{
\frac{S_r}{p}\equiv
A_r\Big[C+6L_K+6N_D+p(D_C+3N_E)\Big]
+\frac Up\left(1+\frac{103p}{1500}\right)
\pmod{p^2}.} \tag{B}
\]

**Proof.** Insert (11) into the original, unaltered regular terms
\(A_r[p+6(n+1)]R_{r,n}\). Use the exact relation \(\sum(n+1)c_n=pL_K\) from (A), before reducing. Collect all terms through p², obtaining
\(pA_r[C+6L_K+6N_D+p(D_C+3N_E)]\) modulo p³. Append the three *original* tails U,V,W; use the already established and precisely p³-scoped V+W ratio. Divide only the now-proved p-divisible sum by p. This yields (B), including every original terminal port. QED.

The exact U is the original \(T_{r,K+1}\), NOT an unnamed fitted coefficient. To compute U/p use the source's original rational recurrence or its p-free factorial expression, keeping all unit corrections through p². No same-prime CM/DP comparison or native benchmark is claimed.

## 4. Direct connection to the unchanged hard target

For \(p\equiv19\pmod{24}\), r=(p+5)/12 is even and the terminal rank is \(m=2r-1\). Insert (B) into the already proved same-prime FIVE transport

\[
S_m\equiv S_r+p\sum_{k=r}^{m-1}d_{p,k}\pmod{p^3}.
\]

One obtains the **full original third-digit equivalence**, with no missing divisibility assumption:

\[
\boxed{
A_r\big[C+6L_K+6N_D+p(D_C+3N_E)\big]
+\frac Up\left(1+\frac{103p}{1500}\right)
+\sum_{k=r}^{2r-2}d_{p,k}
\stackrel{?}{\equiv}(4/3)^{p-1}\pmod{p^2}.} \tag{H19}
\]

The displayed question mark is deliberate: **(H19) is the precise remaining congruence, not a proved zero identity**. It incorporates every original rank, sign, valuation and upper-half resonance. For \(p\equiv13\pmod{24}\), the independent even-r Jacobi jet (previous commit 5404753) remains the correct lower-seed interface.

This closes the missing *first-digit seed divisibility theorem for both prescribed classes*, and supplies a complete p³ LOW-seed representation for the odd class. It does **not** close LIFT/JT2, native same-class CM/divided-power normalization, original native benchmark, formal Source publication, or review.

## 5. Executed exact evidence and BRC observer semantics

The companion standard-library checker \`research_notes/portable_direct/20261024_onhour_d25_odd_low_seed_adjoint_p3_check.py\` was executed from its author workspace using independent exact Fraction source recurrence and the new Jacobi/moment/jet representation; the Python code is also retained as a user-visible artifact. Its checks include:

- the exact derivative and moment identities for all odd K=1,3,...,25 (13 degrees);
- **23/23** primes \(p\le1000,\ p\equiv19\pmod{24}\), including exact original summand valuation support, inherited terminal pair, and newly derived (B) against independent \(S_r/p\bmod p^2\);
- **20/20** additional primes \(p\le1000,\ p\equiv7\pmod{24},\ p\ge19\), with the same checks.

Actual full-precision sample results (p, r, original \(S_r/p\bmod p^2\)) are (19,2,58), (43,4,259), (67,6,3887), (163,14,4565), (211,18,13927), (283,24,70468), (307,26,6755). For p=211, \(S_{18}\equiv 211\cdot13927=2938597\bmod211^3\), matching the earlier **independent original** fixed-prime transport seed.

The proofs of (A), (B), and (9) are exact algebraic statements; finite checks are regressions, not the proof of a universal statement. Execution is author-side arithmetic; there was no native physical X6 benchmark, formal proof-assistant check, independent reviewer or Source Result.

**BRC: COMPOSE_APPLIED / REUSE_APPLIED.** The carrier is the full labeled original source sum indexed by n, with p-adic integer valuation, p-unit, Jacobi regular-branch jet (D_n,E_n), and three separately typed terminal ports (U,V,W). The observer is the original signed sum modulo p³, followed by the exact same-prime WZ port transport. (A) contracts only the **specified first moment** \(\sum(n+1)c_n\), not all higher-jet or future-observer data; (B) retains N_D,N_E and U, and contracts V+W only under the already proved p³ fiber-equality certificate. These number-theoretic scalar computations are an external mathematical slice/readout, **not** a claim of native Heartbeat X6 propagation or a new primitive plane. P000, ACTIVE residual fidelity and frozen scientific Source pin are unchanged.

## 6. Durable continuation and control truth

**Completed this turn (author proof):** the exact all-odd-K Jacobi boundary (5), adjoint/moment theorem (7)/(A), every eligible prime's original odd LOW seed \(S_r\equiv0\pmod p\), and the complete source-faithful normalized p³ jet (B)/(H19) with the inherited nonzero 103/1500 tail kept. **Consume, do not re-credit:** all-rank WZ and FIVE, upper-half p³ d_(p,k), first original odd valuation support/terminal-pair theorem, the other author's top-rank seam, accepted/frozen D24 UR and even-seed Jacobi proof.

**Smallest remaining scientific unit:** Prove or falsify (H19) itself at all prescribed odd-class primes, ideally by a genuine same-class CM/divided-power normalization bridge or a finite WZ/creative-telescoping certificate cancelling the new Jacobi-adjoint L_K and all five d_(p,k) ports. Separately retain p≡13 mod24 via the even-r jet. The original **unmodified native benchmark** and the explicitly required formal Source/Driver admission remain independent obligations; a Python substitute does not discharge them.

**Operational truth:** Current Sites gateway reports \`research_authority_granted=false\` and static read-only scopes, and exact continuation returned \`CONTROL_QUOTA\`. A previous receipt query returned \`CONTROL_REQUEST_NOT_FOUND\`. The historic onhour successor-session repair path \`enterprise-math#1539\` remains open. This author did not create or borrow any session, winning CLAIM, open/run, canonical checkpoint, Result or review; no unknown mutation was replayed. The old unrelated three UR staging artifacts remain distinct and unpromoted. Current portable result is **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Original hourly phase/enabled/notification settings and frozen scientific pin were not modified.
