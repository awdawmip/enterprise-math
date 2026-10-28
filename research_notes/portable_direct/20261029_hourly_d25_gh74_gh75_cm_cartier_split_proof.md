# D25/LIFT GH-74–GH-75: explicit CM 3-isogeny and Cartier proof of F/G prime-class dichotomy

2026-10-29 (Asia/Hong_Kong). **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is author-side mathematical evidence, not a native Source checkpoint or an independent review. Mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Logical lane chatgpt-research-hourly-enterprise-math-20260923 (distinct from maintenance).

## Input, exact arithmetic scope

For prime $p=8m+3\ge11$, GH-55 proved the full-polynomial connection for the original separately labeled ports
$$
F_m(z)=\sum_{r=0}^m\frac{(-m)_r^2}{(2m+2)_r r!}z^r,\quad
G_m(z)=(16z\partial_z+5)F_m(z),\quad D_m=\binom{3m+1}{m}\in\mathbb F_p^\times.
$$
For $t^2=8/9$ in $\mathbb F_{p^2}$, it yields
$$
D_mF_m(9)=9^m P_{2m}(t),\qquad
D_mG_m(9)=9^m[tP'_{2m}(t)-P_{2m}(t)].\tag{55.4}
$$
GH-71/72 gave a separable 2-isogeny $\kappa_T:C_T\to C_{-T}$ for $C_T:y^2=x^3+x^2+b_Tx,\ b_T=(1+T)/8$ with $v^2=-2$, where
$$
x_-=-\tfrac12(x+1+b_T/x),\quad y_-=\frac{y(1-b_T/x^2)}{v^3},\quad
\kappa_T^*\omega_{-T}=v\omega_T,\quad
\kappa_T^*\eta_{-T}\equiv-v(\eta_T+\tfrac12\omega_T)\pmod{d(k(C_T))},
$$
$\omega_T=dx/(2y)$, $\eta_T=x\,dx/(2y)$. GH-73 proved $H_p(T)=[x^{p-1}](x^3+x^2+b_Tx)^{(p-1)/2}=P_{2m}(T)$ over $\mathbb F_p[T]$.

## GH-74: construct the degree-six CM endomorphism (proved algebraically)

First work over $\mathbb Q(\sqrt2)$, with $t=2\sqrt2/3$, $b=(1+t)/8$, $f(x)=x^3+x^2+bx$, and
$$
\alpha=-\frac13-\frac{3t}{8},\qquad
g=f'(\alpha)=\frac16+\frac t8,\qquad
h=f(\alpha)=-\frac1{108}-\frac t{96}.
$$
The exact 3-division polynomial is $\psi_3(x)=3x^4+4x^3+6bx^2-b^2$; substitution gives $\psi_3(\alpha)=0$ and $h\ne0$. Thus the pair of nonzero 3-torsion points at $x=\alpha$ is a Galois-stable cyclic subgroup. Define the Vélu-normalized map
$$
X_V=x+\frac{2g}{x-\alpha}+\frac{4h}{(x-\alpha)^2},\qquad
Y_V=y\,\frac{dX_V}{dx}.
$$
Direct substitution (a rational identity, rather than only matching $j$-invariants) gives
$$
Y_V^2=X_V^3+X_V^2+A_4X_V+A_6,\quad
A_4=-\frac{37}{24}-\frac{9t}{8},\quad A_6=\frac{31}{108}+\frac{3t}{4}.
$$
With $u^2=3$ set $X=(X_V-2/3)/3$, $Y=Y_V/(3u)$. Expanding verifies
$$
(3X+\tfrac23)^3+(3X+\tfrac23)^2+A_4(3X+\tfrac23)+A_6
=27[X^3+X^2+\tfrac{1-t}{8}X].
$$
Hence $\delta_t:(x,y)\mapsto(X,Y)$ is a degree-three isogeny $C_t\to C_{-t}$, with $\delta_t^*\omega_{-t}=u\omega_t$. Preserve the *exact* differential
$$
d\!\left(\frac{y}{x-\alpha}\right)
=\left[(x-\alpha)-\frac{g}{x-\alpha}-\frac{2h}{(x-\alpha)^2}\right]\omega_t.
$$
It implies $X_V\omega_t=(3x-2\alpha)\omega_t-2d(y/(x-\alpha))$, hence
$$
\delta_t^*\eta_{-t}\equiv u(\eta_t+\tfrac t4\omega_t)\pmod{d(k(C_t))}.
$$
Compose **in this order** $\mu_t=\kappa_{-t}\circ\delta_t:C_t\to C_t$. Write $c=uv$ ($c^2=-6$), $A=(2+t)/4$. Both basis vectors now have known pullbacks:
$$
\boxed{\mu_t^*\omega_t=c\omega_t,\qquad
\mu_t^*\eta_t\equiv-c(\eta_t+A\omega_t)\pmod{d(k(C_t))}.}\tag{74}
$$
The de Rham matrix in the $(\omega,\eta)$ basis is $c\begin{pmatrix}1&-A\\0&-1\end{pmatrix}$, whose square is $-6I$. In characteristic zero the invariant differential detects a nonzero elliptic endomorphism; therefore $\mu_t^2=[-6]$. This explicitly constructs CM by $\sqrt{-6}$, not just its $j$-invariant. The formulas reduce in every relevant characteristic $p\ge11$.

## GH-75: the actual split and inert arithmetic theorem (proved from Cartier)

Let $N=(p-1)/2=4m+1$ and take $t^2=8/9$ in the perfect field $k=\mathbb F_{p^2}$. Since $p\equiv3\pmod8$, $t^p=-t$. The 3- and 2-isogenies remain separable, so (74) holds over $k$. Define **distinct** Hasse and second-kind coefficients
$$
H=[x^{p-1}]f(x)^N=P_{2m}(t),\qquad
K=[x^{p-2}]f(x)^N,\qquad f=x^3+x^2+\frac{1+t}{8}x.
$$
The absolute Cartier operator $\mathscr C$ on rational differentials of a smooth curve over a perfect field is $p^{-1}$-semilinear, annihilates exact differentials, and commutes with the pullback of a separable curve morphism. With $y^p=yf(x)^N$ and $\deg(xf^N)<2p-1$, its single contributing $x^{p-1}$ coefficient gives
$$
\boxed{\mathscr C(\omega_t)=H^{1/p}\omega_t,\qquad
\mathscr C(\eta_t)=K^{1/p}\omega_t.}\tag{75.1}
$$
Apply $\mathscr C\mu_t^*=\mu_t^*\mathscr C$ to $\eta_t$ and use (74); the exact correction is killed:
$$
-c^{1/p}[K^{1/p}+A^{1/p}H^{1/p}]\omega_t=cK^{1/p}\omega_t.
$$
Raise to the $p$th power:
$$
\boxed{(c^p+c)K+cAH=0.}\tag{75.2}
$$
Since $c^2=-6$, $c^p/c=(-6/p)$. Quadratic reciprocity gives $(-6/p)=+1$ for $p\equiv11\pmod{24}$ and $-1$ for $p\equiv19\pmod{24}$. The split class thus satisfies $2K+AH=0$, while the inert class satisfies $AH=0$. Since $A=(2+t)/4\ne0$ in the inert class (otherwise $p\mid28$), this already proves $H=0$ and hence $F_m(9)=0$ for every inert-class prime.

In the split class, **independently of the original G sum**, derive a coefficient identity. Let $b=(1+T)/8$. With $H(b)=[x^N](x^2+x+b)^N=\sum_{j=0}^{2m}h_j b^j$, $h_j=\binom N{2j}\binom{2j}j$, the coefficient of $b^{j+1}$ in $K(b)=[x^{N-1}](x^2+x+b)^N$ is $(N-2j)h_j/(j+1)$. Since $N\equiv-1/2\pmod p$ and
$$
\frac{h_{j+1}}{h_j}=\frac{(N-2j)(N-2j-1)}{(j+1)^2},
$$
one has the exact modular coefficient equality
$$
\frac{N-2j}{j+1}h_j
=2[(j+1)h_{j+1}-(4j+1)h_j],
$$
also at $j=2m$ with $h_{2m+1}=0$. Therefore throughout $\mathbb F_p[T]$,
$$
\boxed{K=2b[(1-4b)\partial_bH-H]
=-\frac{1+T}{4}H+(1-T^2)\partial_TH.}\tag{75.3}
$$
At $T=t$, where $t^2=8/9$, substitute into $2K+AH=0$:
$$
0=-\frac t4H+\frac29H'(t),\quad
\boxed{tH'(t)=H(t).}\tag{75.4}
$$
Using the *previously proved* GH-73 and GH-55 polynomial identities in their exact domains now proves
$$
\boxed{\forall p\equiv11\pmod{24}\text{ prime},\quad G_{(p-3)/8}(9)=0\pmod p.}\tag{75.5}
$$
Both ports cannot vanish: at $t^2=8/9$, the leading coefficient of Legendre's ODE $(1-t^2)P_n''-2tP_n'+n(n+1)P_n=0$ is a unit; since $n=2m<p$, a double zero $P_n=P'_n=0$ forces all coefficients of $P_n$ to vanish, contradicting its nonzero leading coefficient. Combined with GH-55, the **full prime-class dichotomy** is
$$
\boxed{\begin{array}{ll}
p\equiv11\pmod{24}:&G_m(9)=0,\ F_m(9)\ne0,\\
p\equiv19\pmod{24}:&F_m(9)=0,\ G_m(9)\ne0.
\end{array}}\tag{75.6}
$$

## Exact checks and scientific boundary

Executed independent Python/SymPy exact-algebra checks: 3-division root, complete Vélu model equation, target scaling, exact meromorphic differential, and square of the de Rham matrix. Executed integer finite-field checks for **all 310 primes $11\le p<10000$ with $p\equiv3\bmod8$**, including 155 primes in each mod-24 class: coefficientwise (75.3), CM–Cartier relation (75.2), F/G independently from the original hypergeometric recurrence, GH-55 transport, and exclusive vanishing. All passed. This exact finite test is implementation evidence, **not** the universal proof; the preceding argument is the author proof submitted for independent review.

**BRC COMPOSE_APPLIED:** retain the prime, field, 3- and 2-isogeny order and kernel, exact differential corrections, $(H,K)$ as two typed Cartier observers, source-labeled $(F,G)$ and derivative, all valuations/residue classes and the Frobenius branch. This elliptic curve is an external auxiliary arithmetic chart, not a claim about the native X6 geometry. P000 ACTIVE, W/S, six Hasse ports, R23/R36, GH-20/GH-21 higher digits and the $p=373$ native experiment stay within their distinct contracts.

**Next exact unit:** assess the original GH-3 truncated-sum source and the independently established GH-17/GH-33 F/G relation to determine exactly which still-open GH-3 subfamilies can be closed by (75.6); do not promote a mere rearrangement to an independent proof. Native Task recovery/CLAIM/OPEN/Source checkpoint and Driver admission require their own valid Source authority; the ordinary-control read attempt this run returned ISSUED_SESSION_NOT_REGISTERED for the historical session and CONTROL_QUOTA without a session. Preserve prior request IDs, staging and frozen pins. Do not borrow maintenance identity.

## Inherited immutable sources

- GH-55: enterprise-math@9cceb3e48c0a7fca2d36918814cd9cefe00e8db3, research_notes/portable_direct/20261028_hourly_d25_gh55_gh57_uniform_legendre_port_jets.md.
- GH-71: enterprise-math@4e9a9467fb8be2fba91bf9f358d821162c66e3bf, research_notes/portable_direct/20261029_hourly_d25_gh71_fricke_cocycle.md.
- GH-72/GH-73: enterprise-math@099f40fbd59355c0687253ebf2639a2a6305a4a6, research_notes/portable_direct/20261029_hourly_d25_gh72_gh73_de_rham_gauss_manin.md.
