# D25/LIFT GH-81–GH-82 — CM–Cartier classification of the odd Laurent source and its nonzero transverse jet

Date: 2026-10-29 Asia/Hong_Kong. Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is an author-side extension of the prior unreviewed GH-74/GH-75 CM proof, **not** an independent review, native Source checkpoint, original GH-3 completion or p² lifting proof. Stable research logical conversation: \`chatgpt-research-hourly-enterprise-math-20260923\`, separate from the maintenance lane. Scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged.

## Exact inherited source

Let \(p=8m+7\ge7\) be prime, \(d=2m+1=(p-3)/4\). GH-80 (just published as \`20261029_hourly_d25_gh80_odd_clausen_legendre_bridge.md\`) proves, in the *entire* \(\mathbb F_p[z]\), the originally labeled GH-16 coefficient polynomial and its Laurent observer:
\[
U_d(z)=(1-z)F(z)^2,\quad
F(z)=\sum_{r=0}^m\frac{(-m)_r^2}{(2m+3)_r r!}z^r,\quad
\mathcal H_d(z)=(8z\partial_z+5)U_d(z),
\]
\[
\mathcal H_d(z)=F(z)B(z),\quad
B(z)=16z(1-z)F'(z)+(5-13z)F(z),\quad
\deg F=m,\quad\deg B=m+1.
\]
With \(D=\binom{3m+2}{m}\), \(t^2=(z-1)/z\) and \(P_d\) ordinary Legendre,
\[
DF(z)=z^mP_d(t)/t,\qquad
\mathcal H_d(9)=-D^{-2}9^dP_d(t)[tP_d'(t)-P_d(t)]
\quad(t^2=8/9).
\]
Here \(t\in\mathbb F_p^\times\), because \(p\equiv7\bmod8\). Distinguish \(F,B\), GH-16 \(U,\mathcal H\), the Hasse coefficient \(H\) below, and the even-branch GH-22 \(F_m,G_m\).

## GH-81A: Hasse normalization holds for ODD d, with a minus sign

For **every** prime \(p=4d+3\ge7\) set \(N=(p-1)/2=2d+1\),
\[
C_T:y^2=x^3+x^2+b_Tx,\quad b_T=(1+T)/8,
\quad H_p(T)=[x^{p-1}](x^3+x^2+b_Tx)^N.
\]
Expansion from the *actual curve* gives
\[
H_p(T)=\sum_{j=0}^d\binom N{2j}\binom{2j}j b_T^j.
\]
Use \(N\equiv-\tfrac12\), \(-N/2\equiv d+1\), \((1-N)/2\equiv-d\) in \(\mathbb F_p\), and compare every coefficient with the terminating Legendre hypergeometric expansion. All \(j!\) up to \(d\) are units. This proves the entire polynomial identity
\[
\boxed{H_p(T)=P_d(-T)=(-1)^dP_d(T)\quad\text{in }\mathbb F_p[T].}\tag{81.1}
\]
GH-73 established the \(d\) even special case. **For the present odd \(d\), \(H_p(T)=-P_d(T)\); losing this sign breaks the actual Hasse normalization.**

Likewise the second-kind coefficient
\[
K_p(T)=[x^{p-2}](x^3+x^2+b_Tx)^N
\]
has the entire-polynomial identity
\[
\boxed{
K_p(T)=-\frac{1+T}{4}H_p(T)+(1-T^2)H_p'(T).}\tag{81.2}
\]
To verify it, write \(H_p(b)=\sum_{j=0}^d h_jb^j\), \(h_j=\binom N{2j}\binom{2j}j\). The coefficient of \(b^{j+1}\) in \(K_p\) is \(\frac{N-2j}{j+1}h_j\), while
\(\frac{N-2j}{j+1}h_j=2[(j+1)h_{j+1}-(4j+1)h_j]\) in \(\mathbb F_p\), including the terminal \(j=d\) with \(h_{d+1}=0\). Therefore \(K_p=2b[(1-4b)\partial_bH_p-H_p]\), giving (81.2). This is an extension of GH-75's **source coefficient proof**, not an assertion from finite samples.

## GH-81B: extend the *endomorphism-based* Cartier certificate to p ≡ 7 (mod 8)

At \(t^2=8/9\), GH-74 constructed an explicit separable degree-six CM endomorphism of the smooth elliptic curve \(C_t\), with \(c^2=-6\), \(A=(2+t)/4\) and
\[
\mu_t^*\omega=c\omega,\qquad
\mu_t^*\eta\equiv-c(\eta+A\omega)\pmod{\mathrm{exact}},
\quad\omega=dx/(2y),\ \eta=x\,dx/(2y).
\]
These *rational map and meromorphic-differential identities* require no \(t^p=-t\) hypothesis: they hold for either algebraic root of \(t^2=8/9\). Their denominators are units and both 2- and 3-isogenies remain separable for every present prime \(p\ge7\), **including \(p=7\)**. The curve is nonsingular because \(t^2\ne1\). Over a perfect splitting field, Cartier commutes with the isogeny pullback and kills exact differentials. The degree bound on \(xf_t(x)^N\) gives
\[
\mathscr C(\omega)=H^{1/p}\omega,\quad
\mathscr C(\eta)=K^{1/p}\omega,\quad
H=H_p(t),\ K=K_p(t).
\]
Applying Cartier to the *second* de Rham vector and raising to the \(p\)-th power gives the true CM constraint
\[
\boxed{(c^p+c)K+cAH=0.}\tag{81.3}
\]
No assumption about which field contains \(t\) is used here; that affects only the actual Frobenius branch. Since \(c^p/c=(\frac{-6}{p})\), (81.3) reads
\[
(1+\chi_{-6}(p))K+AH=0.
\]
For \(p\equiv7\bmod24\) this gives \(2K+AH=0\). Inserting (81.2) at \(t^2=8/9\) yields
\[
0=-\frac t4H+\frac29H'(t)\quad\Longrightarrow\quad
\boxed{tP'_d(t)=P_d(t).}\tag{81.4}
\]
For \(p\equiv23\bmod24\), \(\chi_{-6}(p)=-1\) and \(AH=0\). Now \(A=0\) would imply \(t=-2\), so \(t^2=4=8/9\) would require \(p\mid28\); the sole odd prime possibility is \(p=7\), **not in this inert class**. Hence \(A\ne0\), and
\[
\boxed{P_d(t)=0\quad(p\equiv23\bmod24).}\tag{81.5}
\]

These conditions are exclusive, not merely two sufficient zero tests. The Legendre ODE has ordinary point \(t^2=8/9\) with \(1-t^2=1/9\ne0\), and \(\deg P_d=d<p\). If \(P_d(t)=P_d'(t)=0\), repeated coefficient comparison in the local Taylor expansion (with \(r!\) units through degree \(d\)) forces \(P_d=0\), contrary to its nonzero leading coefficient. Thus (81.4) implies \(P_d(t)\ne0\), while (81.5) implies \(P_d'(t)\ne0\). From GH-80's exact Legendre transform, \(F(9)\ne0\) in the split class; in the inert class \(F(9)=0\), \(F'(9)\ne0\) because \(dt/dz=1/(2tz^2)\) is a unit at \(z=9\).

**All-prime author classification in the previously open odd branch:**
\[
\boxed{
\begin{array}{ll}
p\equiv7\pmod{24}:&
F(9)\ne0,\quad B(9)=0,\quad U_d(9)\ne0,\\[2pt]
p\equiv23\pmod{24}:&
F(9)=0,\quad F'(9)\ne0,\quad U_d(9)=U'_d(9)=0.
\end{array}}
\qquad\boxed{\mathcal H_d(9)=0\text{ in both classes}.}\tag{81.6}
\]
The \(p=7\) split edge is included: \(m=0,\ F=1,\ U=1-z,\ \mathcal H=5-13z\equiv5+z\pmod7\); at \(z=9\equiv2\), \(\mathcal H=0\) with nonzero derivative.

## GH-82: exact nonzero transverse derivative in BOTH odd classes

The classification strengthens GH-79's finite observations to an all-prime theorem about the original observer's first jet, without substituting a quotient \(U'/U\) where \(U=0\).

If \(p\equiv7\bmod24\), the valid \(B(9)=0\) condition is
\(-1152F'(9)-112F(9)=0\); hence \(F'(9)=-7F(9)/72\).
The polynomial \(F\) satisfies
\[
z(1-z)F''+(5/4-11z/4)F'-(49/64)F=0.
\]
At \(z=9\), this gives
\(F''(9)=-47F'(9)/144-49F(9)/4608\).
Differentiating \(B\) and reducing yields \(B'(9)=-8F'(9)-3F(9)/4=F(9)/36\). Since \(\mathcal H=FB\), it follows that
\[
\boxed{\mathcal H_d'(9)=F(9)^2/36\ne0\qquad(p\equiv7\bmod24).}\tag{82.S}
\]
If \(p\equiv23\bmod24\), \(F(9)=0\) is a *simple* zero. Then
\(B(9)=-1152F'(9)\), so
\[
\boxed{\mathcal H_d'(9)=-1152F'(9)^2\ne0\qquad(p\equiv23\bmod24).}\tag{82.I}
\]
Here \(U_d(9)=U_d'(9)=0\) and \(U_d''(9)=-16F'(9)^2\ne0\). In particular the \(p=23\) witness of GH-79 is correctly retained: \((U(9),U'(9),U''(9),\mathcal H'(9))=(0,0,21,17)\pmod{23}\). Every denominator and coefficient required for nonzero is a unit for \(p\ge7\).

Hence **the original GH-16 double-pole obstruction polynomial has a simple zero at \(z=9\) for every prime \(p\equiv7\bmod8,\ p\ge7\)**. GH-77 had supplied an analogous conclusion in the different even branch \(p\equiv3\bmod8\), conditional on GH-75's author proof. These do **not** complete the original GH-3 truncated congruence or its Laurent first-order residual.

## Exact regressions, limits and successor

Executed a Python **standard-library** checker with separately constructed GH-16 coefficients, odd Gauss coefficients, odd Legendre polynomials and elliptic Hasse \((H,K)\) coefficients. Full polynomial factorization and Legendre transform: all 78 primes \(7\le p<2000,\ p\equiv7\bmod8\). Exact F/GH-16 observer jets, full CM Cartier scalar, Hasse sign, split/inert branch and nonzero derivative: all 308 primes \(7\le p<10000\), split 156 / inert 152. Every check passed; no native Hasse port, p² experiment or independent review was performed. The universal conclusion rests on the displayed author algebra and the **unreviewed** GH-74 elliptic endomorphism proof, not on the samples.

BRC **COMPOSE_APPLIED**: the ordered \(p,d,m,z,r\), original GH-16 coefficients, odd \(F,B,U,\mathcal H\), \(H,K\) as *separate* Cartier observations, \(t,c,A\) with Frobenius branch, exact derivatives and Laurent order remain typed. In the inert branch \(U'/U\) is undefined; its two-jet cannot be safely quotiented away. These are auxiliary finite-field charts, not native X6, W/S or the six native Hasse ports. P000 ACTIVE untouched.

**Next exact action:** read the original GH-15/GH-16 rank-transfer \(\alpha_p,C_r\) at its pinned source to determine which full-rank Laurent \(A_r(9)=0\) and \(A'_r(9)\ne0\) claims now follow for \(p\equiv7\bmod8\). Then attack **GH-3's genuine finite endpoint and first-order \(BL\) terms** (including the \(p\equiv3\bmod8\) branch); the current parity-square factorization, Hasse special value and formal parameter derivative are *not* a mod-\(p^2\) certificate. Maintain the independent \(p=373\) native H0/B0 and higher-digit obligations.

Control/continuation: current gateway 0.6.11 reported \`research_authority_granted=false\`, \`executor_binding_configured=false\`, Source control \`CODE_REVIEW_REQUIRED\`, quota active_jobs=5/5. No new Source session/CLAIM/OPEN/checkpoint/Result/review is inferred; old request/session/staging remains untouched. Existing control support issue #1558 is the owner path. The frozen Source scientific pin and task schedules are not changed.
