# C86: independent regularity and cubature audit

This note audits the exact chamber representation used by
`../certify_mellin_integral.py`. It does not use an independence assumption
between lattice competitors. Its inputs are the finite signed width kernels
in `../smallarea/mellin_chambers.json`.

## 1. Complete coverage of the spline chambers

Write

\[
h_{K,r}(z)=(1-W_K(r,z))_+,
\qquad
W_K(r,z)=\max_{v\in K}(rv_1+zv_2)
             -\min_{v\in K}(rv_1+zv_2).
\]

The supplied knots have the form \(z_i(r)=\alpha_i+\beta_i r\), with
constant slope jumps \(A_i\), on each interval with endpoints
\(0,1/3,1/2,2/3,1\). The independent verifier reconstructs

\[
\widehat h_{K,r}(z)=\sum_i A_i(z-\alpha_i-\beta_i r)_+.
\]

It checks all 60 polygon/parameter pieces on entire regions. Between
successive affine knots the region in the \((r,z)\) plane is a trapezoid.
The reconstructed function is affine there. The verifier chooses an
ordered polygon difference \((d_x,d_y)\) and checks the exact coefficient
identity \(\widehat h=1-d_xr-d_yz\). At all four rational vertices it
checks both \(\widehat h\ge0\) and

\[
d_xr+d_yz\ge e_xr+e_yz
\quad\text{for every ordered polygon difference }(e_x,e_y).
\]

These are affine inequalities, so the vertex checks cover the complete
trapezoid. The two unbounded exterior rays are covered by an outward
ordered difference with width at least one. Empty spline pieces are
covered by the exact minimum-width bound. The checks also establish
\(\sum A_i=\sum A_i\alpha_i=\sum A_i\beta_i=0\), so the reconstructed
function vanishes outside its support.

This is a finite exact coverage proof, rather than a test at several
parameter values. The run completed 246 polyhedral checks. It then
regenerated all ten merged chamber expressions from these verified
atoms and matched the supplied expressions exactly.

## 2. Continuity is sufficient; global differentiability is false

Set \(p=41/20\) and define the unscaled signed expression

\[
S(r,s)=\sum_j w_j|a_jr+b_js+c_jrs|^p,
\qquad
H(r,x)=r^{-p}S(r,rx)
       =\sum_j w_j|a_j+b_jx+c_jrx|^p.
\]

There are twelve shared chamber edges in \(0\le s\le r\le1\).
The verifier substitutes the exact edge coordinate, merges the resulting
affine arguments up to sign, and compares rational coefficient ledgers.
All twelve value ledgers and all twelve tangential-derivative ledgers
match exactly. Thus \(S\), and hence \(H\), is continuous on the relevant
closed chamber union. At \(r=0\), the first-chamber formula itself defines
the continuous extension of \(H\), so no division by zero is used.

Normal derivatives do not always match. At \((r,s)=(1/2,1/4)\), the
left-minus-right jump of \(S_r\) has a strictly positive, rationally
enclosed value

\[
0.011302809106204369\ldots.
\]

The exact rational endpoints are recorded in
`mellin_regularity_audit.json`. They are obtained by integer twentieth-root
bisection at 100 bits. Several individual polygon widths have a flat
minimum; when their support disappears at \(r=1/2\), a first derivative
can jump. Consequently a proof using a global \(C^1\) assumption would
be invalid. The parent cubature explicitly treats cells crossing a
chamber edge by continuity and bounded piecewise gradients.

## 3. Derivative bounds on a complete rectangle

For one chamber term put

\[
u(r,x)=a+bx+crx,\qquad f(r,x)=w|u(r,x)|^p.
\]

Let \(R=[r_a,r_b]\times[x_a,x_b]\subset[0,1]\times[1/3,1]\). Define

\[
M=\max_{r\in\{r_a,r_b\},\ x\in\{x_a,x_b\}}|u(r,x)|,
\quad Q=\max(1,M),
\]

\[
D_r=|c|x_b,
\qquad D_x=\max(|b+cr_a|,|b+cr_b|).
\]

The bilinear function \(u\) attains its maximum absolute value at a
corner, and \(M^{1/20}\le Q\). Direct differentiation gives the valid
rational bounds

\[
|f_r|\le p|w|MQD_r,
\qquad |f_x|\le p|w|MQD_x,
\]

\[
|f_{rr}|\le p(p-1)|w|QD_r^2,
\qquad |f_{xx}|\le p(p-1)|w|QD_x^2,
\]

\[
|f_{rx}|\le |w|\{p(p-1)QD_rD_x+pMQ|c|\}.
\]

The function \(|u|^{41/20}\) is twice continuously differentiable even
at \(u=0\). Therefore the bounds also hold on the extension of a chamber
formula beyond its own chamber, throughout the rectangle. Summing these
bounds over the merged terms gives the five bounds used by the parent
certifier. The audit JSON records exact chamberwise global bounds as
an additional reproducible check; the certificate uses tighter local
rectangle bounds.

## 4. Weighted centroid quadrature

The integration measure is the nonnegative product measure

\[
d\nu=r^{1/20}\,dr\,(3/x-1/x^2)\,dx.
\]

On \([a,b]\), its radial mass and first moment are

\[
M_r=\frac{20}{21}(b^{21/20}-a^{21/20}),
\qquad L_r=\frac{20}{41}(b^{41/20}-a^{41/20}).
\]

The corresponding horizontal expressions are

\[
M_x=3\log(b/a)+1/b-1/a,
\qquad L_x=3(b-a)-\log(b/a).
\]

The centroid is \((L_r/M_r,L_x/M_x)\). For an interior rectangle,
successive one-dimensional Taylor formulas cancel the two linear terms.
Since the variance of a distribution supported in an interval of length
\(h\) is at most \(h^2/4\), the average error is bounded by

\[
\frac18\{M_{rr}h_r^2+M_{xx}h_x^2\}.
\]

If the implemented rational node differs from the exact centroid by at
most \((\epsilon_r,\epsilon_x)\), add
\(G_r\epsilon_r+G_x\epsilon_x\). The total error is this quantity
multiplied by the cell mass.

For a boundary cell, the certifier evaluates each possible chamber's
gradient at the geometric center, using that chamber's extension. The
Hessian bounds then bound its gradient throughout the rectangle. Taking
the maximum over all possible chambers gives constants \(G_r,G_x\).
Continuity across the finite chamber interfaces allows integration of
the piecewise gradients along horizontal and vertical segments. Hence

\[
|H(r,x)-H(r_0,x_0)|\le G_rh_r+G_xh_x
\]

for any two points in the cell. This bound does not require a matching
normal derivative. The grid parameter is divisible by six, so the
horizontal \(r\)-thresholds are grid edges; the crossing-cell selection
enumerates precisely the possible \(s=rx\) intervals.

## 5. Arithmetic and observed certificate

The audited parent implementation uses 112-bit outward fixed-point
interval arithmetic. A floating twentieth-root value only proposes an
integer: before use, two exact integer power inequalities establish
the lower and upper dyadic bounds. The logarithm is enclosed by twelve
terms of its rational atanh series and a positive geometric remainder.
No floating value determines an acceptance or a final sign.

The parent run with a \(96\times96\) product grid certified

\[
-0.002116642187307301009
< I_{1/4}-I_{1/2}
< -0.001369250572380800260.
\]

The complete exact interval is in the parent certificate. The independent
audit checks its input hash, cell count, and strict endpoint sign; it
does not pretend to rerun the complete cubature. The derivation above
audits the weighted moments, the variance factor, the node correction,
the Hessian bounds, the extension argument for crossing cells, and the
exact continuity requirement.

Reproduce the audit with:

```bash
python /mnt/data/C86/phase/verify_mellin_regularities.py
```

## 6. Audit of the analytic prefactor and reflected polygons

The complete `../smallarea/ALL_AREA_FAREY_MELLIN.md` reduction was also
independently read against its finite ledgers. The following factor
checks are relevant to the final sign and normalization.

An unoriented Farey edge has four positively oriented ordered basis
representations. A Farey triangle has six representations in which the
third direction is the sum of the two basis vectors. Together with the
polygon width identity, whose edge sum has a factor one half, these
give the stored configuration-edge weights \(\pm k/8\) and
\(\mp k/12\). The basis unfolding uses
\(\delta(\det(v,w)-a)\,dv\,dw/(\zeta(2)a)\).

The canonical coefficient reflection used in the kernel generator has
linear part \((x,y)\mapsto(-x,y)\); translation does not affect width.
It replaces \(E_K(v,w)\) by \(E_K(-v,w)\), and hence reverses the
determinant constraint. Exchanging the two physical endpoint coordinates
then restores the determinant sign, preserves the endpoint overlap
factor, and preserves the symmetrized function \(g_\theta(v)\). Thus
the reflected canonicalization is valid for the complete basis integral.
It need not be a pointwise identity for a fixed \((r,s)\) kernel, and
neither the reduction nor the certificate uses such an identity.

For a compact linear-spline correlation, four integrations by parts give

\[
\int_0^\infty
\left[R(0)-\frac{R(u)+R(-u)}2\right]u^{\gamma-2}du
=\frac{\sum_{i,j}A_iB_j|t_i-t_j|^{\gamma+2}}
{2(1-\gamma)\gamma(1+\gamma)(2+\gamma)}.
\]

The numerator has a positive sign: the fourth derivative of the
correlation is the convolution of the two slope-jump measures. The
factor one half comes from integrating the even fourth derivative over
the positive half-axis. Its constant tail has vanishing boundary term
because \(\gamma<1\); at zero the even difference is \(O(u^2)\).

The radial moment difference starts with \(-\gamma\int\Delta F(a)
a^{\gamma-1}da\). The two opposite-sign endpoint quadrants contribute
a factor two. Substitution \(a=rsu\) and the preceding formula cancel
these factors \(2\gamma\), leaving

\[
-\frac1{\zeta(2)(1-\gamma)(1+\gamma)(2+\gamma)}.
\]

On \(s=xr\le r\), the original slope jumps are \(r a_i(r)\) and
\(s a_j(s)\). Their power sum scales as
\(r^{-\gamma}x^{-1-\gamma}H(r,x)\). Combining the remaining
\((rs)^{\gamma-1}\), the factor
\(g_\theta(r,-xr)=r((1-\theta)x-\theta)_+\), and the Jacobian
\(ds=r\,dx\) gives exactly
\(r^\gamma x^{-2}((1-\theta)x-\theta)_+H\).
Symmetry between \(r,s\) gives another factor two. At the quarter point
the linear positive part contributes \((3x-1)/4\), producing the final
prefactor in the main theorem.

Absolute convergence also survives before the finite signed sum is
taken. On the cone where \(g_\theta\ne0\), \(r\) and \(s\) are
comparable. A rescaled spline has uniformly bounded support and slope,
so its even correlation difference is bounded by
\(C\min(ru^2,r^{-1})\). Its Mellin energy is \(O(r^{-\gamma})\).
After the remaining factors and the substitution \(s=xr\), an absolute
majorant is \(C r^\gamma dr\,dx\), which is integrable. The exchange
of integrations therefore does not rely on cancelling divergent terms.
