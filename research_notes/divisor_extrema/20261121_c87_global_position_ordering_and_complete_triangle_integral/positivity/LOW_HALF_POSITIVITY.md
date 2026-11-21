# C87: strict pointwise Mellin positivity on the complete low-half square

## Statement and inherited object

Keep C86's exact Mellin numerator T(r,s)=r^p H(r,s/r), where p=41/20,
and write q=p-2=1/20. T is symmetric in r,s. The original H(0,1) observer,
all integer relations, and the established auxiliary-model bridge and typing
remain unchanged.

This note proves

\[
\boxed{T(r,s)>\frac{37}{500}(rs)^{41/20}
\qquad(0<r\le1/2,\ 0<s\le1/2).}\tag{1}
\]

Equivalently, H(r,x)>(37/500)(rx)^(41/20) whenever 0<rx<=r<=1/2.
This covers all three low-half chambers, including the entire ratio axis
x→0. It strengthens and extends C86's first-chamber bound. No grid sample is
used in the argument.

## 1. Extend the first-chamber expression formally

Put f(z)=z^p for z>=0 and define
Delta_h^2 f(z)=f(z+2h)-2f(z+h)+f(z). Write

\[
\begin{aligned}
T_0(r,s)={}&C(p)(rs)^p
-s^p\Delta_r^2f(1-2r)-r^p\Delta_s^2f(1-2s)\\
&+3\Delta_{rs}^2f(r+s-3rs),
\end{aligned}\tag{2}
\]

with

\[
C(p)=12/6^p-9/3^p-16/2^p+6(2/3)^p+7+4(3/2)^p-4\,2^p.
\]

All arguments in (2) are nonnegative on the whole low-half square. C86's
exact first-chamber formula is T=T0 for r,s<=1/3; here T0 is simply continued
as an explicitly defined comparison expression up to r,s<=1/2.

## 2. A uniform positive bound for T0

The identity

\[
\Delta_h^2 f(z)=p(p-1)h^2
\int_0^1\int_0^1(z+h(u+v))^q\,du\,dv
\tag{3}
\]

reduces every second difference to an average of the concave function z^q.
Jensen's inequality gives

\[
\Delta_r^2 f(1-2r)\le p(p-1)r^2(1-r)^q.
\tag{4}
\]

For the positive term, use the chord of z^q on each half of the interval
[z,z+2h]. The triangular density of u+v assigns weights 1/6, 2/3, 1/6 to
the three interpolation nodes. Thus

\[
\Delta_h^2 f(z)\ge\frac{p(p-1)h^2}{6}
\{z^q+4(z+h)^q+(z+2h)^q\}.
\tag{5}
\]

Let U=1/r, V=1/s and W=U+V, so U,V>=2 and W>=4. Dividing the resulting
bound for (2) by (rs)^p yields

\[
\begin{aligned}
\frac{T_0}{(rs)^p}\ge C(p)+p(p-1)\big[&\tfrac12(W-3)^q+2(W-2)^q
+\tfrac12(W-1)^q\\
&-(U-1)^q-(V-1)^q\big].
\end{aligned}\tag{6}
\]

Concavity also gives (U-1)^q+(V-1)^q<=2^(1-q)(W-2)^q. All three remaining
coefficients are positive, including 2-2^(1-q), so the bound increases with
W and is minimized at W=4. Therefore

\[
\frac{T_0}{(rs)^p}\ge
\delta_0:=C(p)+p(p-1)\{2^{q+1}+\tfrac12 3^q-\tfrac32\}.
\tag{7}
\]

Numerically delta0 is about 0.09279315076116; the proof below certifies the
smaller final constant with exact radical bounds.

## 3. The exact chamber corrections

Define E(r)=0 for r<=1/3. For 1/3<=r<=1/2, put

\[
\begin{aligned}
E(r)={}&r^p\{1-2(3/2)^p+2^p\}
+\Delta_{r/2}^2f(1-2r)\\
&-2^{1-p}\Delta_r^2f(1-r).
\end{aligned}\tag{8}
\]

Exact collection of the stored C86 chamber terms proves

\[
\boxed{T(r,s)=T_0(r,s)+s^pE(r)+r^pE(s)}
\tag{9}
\]

on the entire low-half square. The executable certificate checks both
nontrivial chamber identities with rational coefficient dictionaries.

It remains to bound the corrections uniformly. With U=1/r in [2,3], define

\[
e(U):=E(r)/r^p=D_0+\Delta_{1/2}^2f(U-2)
-2^{1-p}\Delta_1^2f(U-1),
\]

where D0=1-2(3/2)^p+2^p. Let g(z)=z^(p-1). Homogeneity gives

\[
e'(U)=p\,2^{1-p}
\{\Delta_1^2g(2U-4)-\Delta_1^2g(U-1)\}\ge0.
\tag{10}
\]

Indeed 2U-4<=U-1 for U<=3, and g'' is positive and decreasing because
1<p-1<2. By the integral form of a second difference, Delta_1^2 g is
decreasing in its base point. Endpoint U=2 follows by continuity.

Consequently e(U)>=e(2), where

\[
e(2)=6+2^p-4(3/2)^p-2^{2-p}\approx-0.00919801640441.
\tag{11}
\]

The correction E=0 below 1/3 satisfies the same lower bound because e(2)<0.
Equations (7), (9), and (11) now give

\[
T(r,s)\ge\delta_{1/2}(rs)^p,
\qquad\delta_{1/2}:=\delta_0+2e(2).
\tag{12}
\]

## 4. Exact certificate and scope

`certify_low_half.py` uses only Fraction arithmetic and comparisons of
integer twentieth powers. It checks the two chamber corrections, proves
e(2)<0, and encloses delta_(1/2), whose approximate value is

\[
\delta_{1/2}=0.07439711795233989885\ldots>37/500=0.074.
\]

The output is `low_half_certificate.json`, with the exact rational bounds
and the SHA-256 of the inherited C86 chamber source. This proves (1).

The theorem here is pointwise and concerns the three low-half chambers.
Positivity on the remaining chambers is a separate stronger question;
the averaged-kernel method used elsewhere in C87 does not require that
stronger pointwise statement.
