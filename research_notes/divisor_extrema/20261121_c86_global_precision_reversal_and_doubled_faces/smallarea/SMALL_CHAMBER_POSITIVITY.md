# C86: strict positivity of the complete small-(r,s) Mellin chamber

Use the exact kernel of `ALL_AREA_FAREY_MELLIN.md`, and let p=41/20. On
0<s<=r<=1/3, its unscaled numerator is T(r,s)=r^p H(r,s/r). The 16 exact terms
in the first chamber combine to

\[
\begin{aligned}
T(r,s)={}&C(p)(rs)^p
-s^p\Delta_r^2 f(1-2r)
-r^p\Delta_s^2 f(1-2s)\\
&+3\Delta_{rs}^2f(r+s-3rs),\qquad f(z)=z^p,
\end{aligned}\tag{1}
\]

where Delta_h^2 f(z)=f(z+2h)-2f(z+h)+f(z), and

\[
C(p)=\frac{12}{6^p}-\frac9{3^p}-\frac{16}{2^p}
+6\left(\frac23\right)^p+7
+4\left(\frac32\right)^p-4\,2^p.
\tag{2}
\]

Since f'' is nonnegative and increasing,

\[
p(p-1)h^2z^{p-2}\le\Delta_h^2f(z)
\le p(p-1)h^2(z+2h)^{p-2}.
\]

The two negative terms in (1) have z+2h=1. In the positive term,
r+s-3rs=r+s(1-3r)>=r>=s. Consequently

\[
\begin{aligned}
T(r,s)
&\ge C(p)(rs)^p
+p(p-1)(rs)^2\left[3(r+s-3rs)^{p-2}-r^{p-2}-s^{p-2}\right]\\
&\ge(rs)^p\left[C(p)+p(p-1)s^{2-p}\right]\\
&\ge(rs)^p\left[C(p)+p(p-1)3^{p-2}\right].
\end{aligned}
\]

`certify_small_chamber.py` bounds every twentieth root by rational bisection and
proves

\[
\boxed{C(41/20)+\frac{41\cdot21}{400}3^{1/20}
>\frac7{4000}=0.00175.}\tag{3}
\]

The constant is approximately 0.00175059445047. Therefore the whole chamber,
including arbitrary ratios s/r in (0,1], has the strict bound

\[
\boxed{T(r,s)>\frac7{4000}(rs)^{41/20},\qquad
H(r,x)>\frac7{4000}(rx)^{41/20}.}\tag{4}
\]

This controls the origin analytically in the two-variable formula. For the
quarter point, the remaining region is compact: 1/3<=r<=1 and 1/3<=x<=1.
Positivity or sufficiently accurate integration there remains a separate
proof obligation.
