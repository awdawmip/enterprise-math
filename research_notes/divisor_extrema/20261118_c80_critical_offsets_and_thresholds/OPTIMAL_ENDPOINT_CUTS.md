# Optimally placed repeated endpoint rounding phases

Let $z=b/c$, $a=15/4$, and let $U_c(X)=c^{3/4}(g(c;v,w)-1)$ and $W_c(X)=c^{3/4}(g(c+b;v,w)-1)$ at $X=(v/c,w/c)$. The interior smooth extensions below are the actual finite spectra of C77–C79. Put
$$
\delta=c^{3/4}2^{-p},\qquad T_c=\frac{M\sqrt z}{c}(1+\delta^{-1}).
$$
Designs are fixed before the unknown template is given; they may depend on $c,b,p$. The two banks of phases are independent, each bank with $M$ available readings. $V_c$ is the fraction unique in the entire catalogue. Then
$$
\sup_{\rm designs}V_c\to1\quad\Longleftrightarrow\quad T_c\to\infty,
\qquad T_c\to0\quad\Longrightarrow\quad\sup_{\rm designs}V_c\to0 .
$$
The supremum and the existence formulation agree by taking designs within $1/c$ of the supremum. All assertions concern $c\to\infty$, $1\le b\le c$. In particular $T_c\asymp M/c^{3/2}$ for $p=0,b=1$. The factor $1+\delta^{-1}$ can equivalently be replaced by $\max(1,\delta^{-1})$.

## Support, cuts and sufficiency

The normalized support at either endpoint lies in a fixed $[0,C)$ by the C77 global bound quoted in C79 REPEATED_ENDPOINT_PHASES. A shifted quantizer gives cuts spaced by $\delta$ in these coordinates. The total number of cuts on any fixed bounded interval is at most $C_1 M(1+\delta^{-1})$ per bank. Multiple coincident cuts can be counted repeatedly throughout all upper bounds.

For $\delta<C$, repeat with phases $j/M$, giving effective normalized step $\delta/M$. For $\delta\ge C$, choose $M-1$ equally spaced interior cuts in $[0,C)$, one per legal phase; their period translates do not enter its interior. The normalized effective mesh on the whole physical support is $C/M$ in this case. Every additional phase can only refine the output. By C78, as applied also to real mesh by C79, either construction yields $V_c\to1$ when $T_c\to\infty$, since $\sqrt z/(c\,\mathrm{mesh})\asymp T_c$ with constants depending only on $C$.

## Subcritical zero fraction for all designs

On fixed interior compact charts covering all but arbitrarily small source mass, $|W_c-U_c|\le C_K z$ and a physical coordinate derivative of $U_c$ is bounded away from zero. These follow from the signed spectrum's uniform inventory derivative bound and the nonconstant analytic first spectrum off its zero loci, as in C79 FIXED_STOCK_BANK. Take finite rectangular subcharts on which the same partial derivative has fixed sign. Divide $U_c$ into intervals of length $z$. Per interval and chart, rowwise monotonicity bounds the number of source points by $O_K(c(cz+1))=O_K(c^2 z)$, since $cz=b\ge1$. The second endpoint then lies in a fixed multiple enlargement of the same interval. If $k_j,l_j$ count the corresponding cuts on these two intervals, the number of globally unique points in the interval and chart is at most
$$
\min\{C_K c^2 z,(k_j+1)(l_j+1)\}\le C'_K c\sqrt z(2+k_j+l_j).
$$
Endpoint conventions for half-open intervals may instead use $+2$ uniformly. Both interval families have bounded overlap and there are $O_K(1+1/z)$ first intervals. After summing and dividing by $c^2$ one obtains $O_K(T_c+(c\sqrt z)^{-1})$. Since $c\sqrt z=\sqrt{bc}\to\infty$, exhaustion gives the zero-fraction result.

## Interior rank loss with a moving first reading

Fix a subsequence with $T_c\le K$ and pass further to $z\to z_0\in[0,1]$. The following charts are fixed after $z_0$ is chosen. Work in $0<A<1$, $0<D<1$, where $A=4x^a$, $D=4(y/x)^{9/4}$, $m=7A^4D/16$. Set $U=G_1$. On this sign chart the C79 spectrum gives exactly, up to the fixed positive normalization of $G_1$,
$$
U=C_0 A^{19/5}D^{14/3}(1-A)(1-D)/[(1+m)(1+Am)],
$$
$$
\frac{G_s}{U}
=s^4\frac{1-sA}{1-A}\frac{(1+m)(1+Am)}{(1+s^4 m)(1+s^5 Am)},\qquad s=(1+z)^{-a}.
$$
Here $R_z=(G_s/U-1)/z$ and $R_0$ is its continuous extension. Formulae differentiated in $A,D$ at $z=0$ are justified by smooth division in $z$ on the compact external-inventory interval. Uniformly for $D$ in a compact neighborhood of $d_*=14/17$,
$$
R_z=(s^4-1)/z + k_z A+O(A^2),\quad
k_z=s^4(1-s)/z>0,\quad k_0=a,\qquad
\partial_D R_z=O(A^4),\quad \partial_A R_z=k_z+O(A).
$$
The expansion and its derivatives at $A=0$ follow from the rational formula, with $\partial_D$ only acting through $m$. For $A$ small, $(\partial_A R_z)$ does not vanish. Define
$$
B_z=\partial_D\log U-
 \partial_A\log U\,(\partial_D R_z)/(\partial_A R_z).
$$
This extends smoothly to $A=0$ in the chosen $D$ neighborhood, with
$$B_z(0,D)=14/(3D)-1/(1-D).$$
It has a simple zero at $d_*$, since its derivative is $-14/(3D^2)-1/(1-D)^2<0$. The implicit function theorem gives a smooth $D=d_z(A)=d_*+O(A^3)$ (the $D$-dependent term of $\log U$ starts at order $A^4$); all that is needed here is convergence with bounded derivatives. Along this curve $u=U(A,d_z(A))$ is strictly increasing at small positive $A$, owing to $U\asymp A^{19/5}$ and $\partial_A\log U=19/(5A)+O(1)$. Use a fixed small interval $A\in[A_0,2A_0]$ with a margin, then choose a compact positive-length $u$ interval $I$ strictly inside its image. Write $d_f(u)$ for $d_{z_0}(A(u))$, and $\tau=D-d_f(u)$. The coordinates $(u,\tau)$ are regular there because $\partial_A U|_D>0$. In these coordinates the limiting normalized divided endpoint difference is
$$P(u,\tau)=uR_{z_0}(A,D).$$
Its $\tau$ derivative on $\tau=0$ vanishes by $B_{z_0}=0$ (differentiate at fixed $u$). Thus $|P(u,\tau)-P_f(u)|\le C\tau^2$, with $P_f(u)=P(u,0)$. No lower bound on this quadratic term is required.

The relevant finite chart uses $u=U_c$ and $\tau=D-d_f(u)$, keeping the same $d_f$. By C77's inner-chart convergence of the finite smooth signed spectra and their first external-inventory derivative with spatial derivatives, $(W_c-U_c)/z$ represented in these finite coordinates converges uniformly to $P$ on the fixed chart. For $z\to0$ this follows by writing the divided difference as the integral of the inventory derivative. Our sign chart stays strictly away from both zero factors throughout $1\le n/c\le2$. Therefore, for every fixed sufficiently small $h>0$ and all sufficiently large $c$, on $u\in I, |\tau|\le h$ we have
$$|W_c - W_f^{(c)}(u)|\le Czh^2,\qquad W_f^{(c)}(u)=u+zP_f(u).$$
These center maps have uniformly bounded derivatives bounded away from zero on $I$. Indeed, $G_s/U=s^4(1+O(A))$ on the limiting fold, with bounded derivatives of the $O(A)$ term in $A$, and $u(dA/du)=O(A)$. Hence $1+z_0P_f'(u)=s_0^4(1+O(A))>0$ on the chosen chart. Convergence $z\to z_0$ then gives the same property for the center maps, after choosing $A_0$ small. For $z_0=0$ the limiting derivative equals exactly $1$.

## Curvature in the physical integer coordinates

Let $r=y/x$, $D=4r^{9/4}$, $\beta=57/4$ and $\Phi(r)=D^{14/3}(1-D)$. The positive spectrum has the form $U=Cx^\beta\Phi(r)(1+O(x^a))$ at small positive $x$, with all bounded-order derivatives in $r$ and the Euler derivative $x\partial_x$ retaining the error, uniformly near $r_0=(d_*/4)^{4/9}$. At $r_0$, $\Phi'=0$, $\Phi''<0$. To see physical lattice curvature rigorously, rescale $x=x_*X,y=x_*Y$ at $x_*\downarrow0$ and divide $U$ by $C x_*^\beta$. On fixed compact neighborhoods of $(1,r_0)$ this converges in $C^3$ to $X^\beta\Phi(Y/X)$. In the limiting level parametrization
$$X(r)= (u_*/\Phi(r))^{1/\beta},\qquad Y(r)=rX(r),$$
we have $X'=0$, $X''>0$, $Y'=X>0$ at $r_0$; hence $d^2 X/dY^2=X''/X^2>0$. Also $\partial_X U_{\rm lim}>0$ there. These are open conditions under $C^2$ perturbation. At the physical fold, $D=d_{z_0}(A)\to d_*$, so we can select the compact chart above (or a smaller chart around one small $A_0$) so that every section $U=u$ is expressed as $x=f(u,y)$ with
$$0<\kappa\le \partial_{yy}f(u,y)\le C,\qquad 0<\partial_u f(u,y)\le C.$$
Here and below constants can depend on the fixed chart. By finite $C^2$ convergence the same bounds, with slack, hold for $x=f_c(u,y)$ when $U_c=u$. Use a slightly larger fixed rectangle for all these graphs to leave boundary margins.

The band $\mathcal B_c=\{u=U_c\in I,|D-d_f(u)|\le h\}$ within this chart contains at least $k h c^2$ templates as $c\to\infty$ for each fixed small $h$. This follows from locally uniform coordinate Jacobian bounds and lattice Riemann sums on a fixed limiting inner band of half the width, contained in the varying band for $c$ sufficiently large.

## Fine interval and catalogue count

Partition $I$ into intervals $I_j$ of length $\ell=z h^2$ (trim the last). Write $u_j$ for the left endpoint. For sufficiently small fixed $h$ these all remain in the larger chart. For band points with $u\in I_j$, $y$ lies in an interval of length $Ch$, because the limiting maps and the finite chart inverses are uniformly Lipschitz and $\ell\le h^2$ (the center in $y$ can be taken from the finite chart). $W_c$ is in an interval $J_j$ centered at $W_f^{(c)}(u_j)$ with radius $C\ell$. These second-endpoint intervals have bounded overlap independently of $h,z,c$ since the center map is uniformly bi-Lipschitz. Each first interval has only bounded overlap.

We need the uniform bound
$$
N_{j,c}:=\#\{X\in\mathcal B_c:U_c(X)\in I_j\}
 \le C c^2 z h^3+o_h(c).
$$
For $w/c$ in the above $y$ interval the eligible integer $v$ lies in a translate of $[0,L]$, $L=Cc\ell$, with lower endpoint $c f_c(u_j,w/c)$ (monotonicity). There are at most $Chc+O(1)$ rows. For $L\ge1$, the crude bound $O(L)$ per row suffices (the $O(1)$ extra row is absorbed for $c$ large at fixed $h$). For $0<L<1$, the eligible rows have fractional part of $c f_c(u_j,w/c)$ in an arc of length $L$, including endpoints at a cost controlled by discrepancy. Uniformly for every $u_j$ and row subinterval, at fixed nonzero integer frequency $k$, the second derivative of $k c f_c(u_j,w/c)$ with respect to $w$ has absolute value between $|k|\kappa/c$ and $|k|C/c$. The second derivative estimate for exponential sums gives $O_k(\sqrt c)$ over any such subinterval. The Erdős–Turán inequality thus gives absolute discrepancy $o(c)$, uniform in $u_j$, row intervals and the location/length of the fractional-part arc (first truncate at fixed frequency, then let it grow). Endpoints can be handled by interval enlargement and taking the enlargement to zero after $c\to\infty$. This proves the displayed bound. In particular $c^2 z\ge c$ permits absorption of $o_h(c)$ into $C c^2 z h^3$ once $h$ is fixed. The leading constant is independent of $h$.

Let $k_j,l_j$ count cuts in $I_j,J_j$. The numbers of distinct output pairs and of globally unique templates in this band piece are at most $(k_j+2)(l_j+2)$, with the harmless 2 covering endpoint conventions. As $N_{j,c}\le C c^2 z h^3$, its number of globally unique templates is at most
$$\min\{N_{j,c},(k_j+2)(l_j+2)\}\le C c\sqrt z\,h^{3/2}(k_j+l_j+4).$$
Both cut families have bounded overlap; sum them and use $\#\{j\}=O(1+1/(z h^2))$. On dividing by $c^2$, the band uniqueness is at most
$$C T_c h^{3/2}+O\!\left(\frac{h^{-1/2}}{c\sqrt z}\right).$$
For fixed $K$ take $h=d/(1+K)^2$ with a sufficiently small chart-dependent $d>0$, then $c\to\infty$. The upper bound is at most half the source band mass $kh$ asymptotically. This guarantees a positive ambiguous fraction along the subsequence independent of the design. If a sequence had $V_c\to1$ with $T_c$ failing to tend to infinity, pass to a subsequence with bounded $T_c$ and a convergent $z$ to reach this contradiction. This proves the theorem.

The argument does not compute a limiting unique fraction at a fixed critical multiplier. The following section proves its converse when at least two phases are available, in particular for the zero-bit asymptotic problem. No inter-template independence assumption is used; curvature is needed specifically to count templates in the short reading intervals along the moving fold.

## At least a positive fraction at a positive multiplier when two phases are available

For $M\ge2$ there is also a converse to the subcritical zero statement. Uniform high-multiplier sufficiency from C78 implies the existence of a fixed $A$ and a catalogue size cutoff for which each virtual uniform grid with $\sqrt z/(c\,\mathrm{mesh})\ge A$ has singleton proportion at least $1/2$. Otherwise one could select sizes tending to infinity and corresponding multipliers tending to infinity with proportion below $1/2$, contradicting C78. Only the canonical unshifted (or a common normalized-origin) grids are needed here; C79 allows the real effective step.

If $T_c\ge t_0>0$, choose an integer $q$ depending only on $t_0$ and the support bound. Take the interval $[0,C)$ for $\delta\ge C$, or one periodic cell of length $\delta$ for $\delta<C$. In the latter case the partition below repeats with period $\delta$. Divide that interval into $q(M-1)$ equally spaced cells in each axis. Its virtual multiplier is at least a fixed positive multiple of $qT_c$, using $(M-1)/M\ge1/2$, so choose $q$ to ensure at least $1/2$ of templates are globally unique in this virtual two-dimensional partition. Group the $q(M-1)$ fine cells per axis into $q$ consecutive windows each containing $M-1$ cells. Retaining the $M$ boundary cuts of one such window is legal, one reading phase per cut. It isolates each virtual cell of that window globally in the physical support, and in the periodic case per actual period. In the periodic case observations include absolute quantized integers, so different periods are distinguished. Coincidence of the two extreme boundaries of a full period simply saves one cut. Any spare readings may be added elsewhere.

Each virtually unique template has a window on each axis. Among the $q^2$ window pairs, at least one contains at least $1/(2q^2)$ of all templates that are virtually unique. Choosing those two windows preserves every such template's uniqueness against the full catalogue. Thus $\sup V_c\to0$ iff $T_c\to0$ for $M\ge2$ eventually. For $p=0$ the statement holds without an assumption on $M$: whenever $T_c$ is bounded below away from zero one already has $M\to\infty$ on that subsequence. If $T_c$ remains in a compact subinterval of $(0,\infty)$, the optimal unique fraction stays bounded away from both zero and one under these same assumptions. This assertion does not identify a limit.

The same window argument yields a uniform lower bound $k\min(1,T_c^2)$ at all sufficiently large $c$ when $M\ge2$: take $q=\lceil A'/T_c\rceil$ if $T_c$ is small, and $q=1$ when $T_c$ is sufficiently large. The proof allows $q$ to depend on $c$ since the virtual-grid conclusion is uniform.

Source. [C79 model and repeated phases](https://github.com/awdawmip/enterprise-math/blob/9d76acb849471e4b8c411a5de04066679abca8d8/research_notes/divisor_extrema/20261116_c79_critical_window_geometry/REPEATED_ENDPOINT_PHASES.md), [C79 physical normalized spectrum](https://github.com/awdawmip/enterprise-math/blob/9d76acb849471e4b8c411a5de04066679abca8d8/research_notes/divisor_extrema/20261116_c79_critical_window_geometry/WINDOW_CAPACITY.md), and [C78 precision theorem](https://github.com/awdawmip/enterprise-math/blob/24881e361378245e45f27919836ca1c9db48d04f/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision/SHARP_NEAR_STOCKS.md). Run `python3 check_fold.py` with SymPy to reproduce the symbolic and finite checks.
