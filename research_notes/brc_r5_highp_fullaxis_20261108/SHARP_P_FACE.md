# Sharp F-face p threshold at a low-t, high-q corner

**Date:** 2026-11-08. Exact rational author proof. Frozen scientific pins and seven-node model are inherited from the companion RESEARCH.md.

For the FULL_HIST source at \(t=1/13,\ q=1,\ \theta=\kappa=0,\ 0\le p\le1\),

\[
x(p)=\left(1,\frac1{13},1,\frac{3p}{80},0,\frac{279}{1040},0\right).
\]

**Sharp if-and-only-if theorem.** There exists a lawful seedless target on the single F face \(z'=a'/10,\ v'-z'=9b'/40\), with nonnegative seven-node Blackwell transport preserving both frozen times and every randomized terminal declaration, **if and only if**

\[
\boxed{\frac{2741}{3900}\le p\le1.}
\]

## Exact dual identity, necessity

Let the candidate target be \(y=(g,a,b,u,v,w,z)\). Define the nonnegative physical slack variables

\[
A=a,\quad B=g-b,\quad C=u,\quad D=3a/40+21b/80-w.
\]

Let the time and F-face equality residuals be

\[
E_P=T_P(y)-T_P(x(p)),\quad E_Q=T_Q(y)-T_Q(x(p)),
\]
\[
E_{F1}=z-a/10,\quad E_{F2}=v-z-9b/40.
\]

**Exact polynomial identity for arbitrary formal variables \((p,g,a,b,u,v,w,z)\):**

\[
\boxed{\begin{aligned}
p-\frac{2741}{3900}={}&\frac{37}{5}A+\frac{82}{15}B+\frac{80}{3}C+\frac{236}{15}D\\
&+\frac{212}{5}E_P-\frac{718}{15}E_Q
+\frac{82}{15}E_{F1}+\frac{82}{15}E_{F2}.
\end{aligned}}
\]

The identity is checked exhaustively over affine coefficients in VERIFY_SHARP_P.py, using the constant point and all eight basis directions. For a lawful, time-matched target on F, all four E residuals vanish and A,B,C,D are nonnegative, forcing \(p\ge2741/3900\). This is an **F-face representation obstruction**; another seedless face is a different admissible representation.

## Exact attainment, all-real sufficiency

At \(p_*=2741/3900\), choose the rational F-face target

\[
y_*=(1199/1300,0,1199/1300,0,10791/52000,25179/104000,0).
\]

Its five exact hinge differences \(H_k(y_*)-H_k(x(p_*))\), in ascending order of the interior LR nodes, equal

\[
\left(
\frac{3306821}{117000000},\
\frac{43078673}{936000000},\
\frac{3311821}{52000000},\
\frac{3311821}{72000000},\
\frac{3311821}{117000000}
\right)>0.
\]

All capacity, mass, LR normalization and stop-time conditions also hold exactly. At \(p=1\), the companion VERIFY.py supplies a valid F-face corner target indexed by \((t{\rm bit},p{\rm bit},q,\theta,\kappa)=(0,1,1,0,0)\).

For every real \(p\in[p_*,1]\), convexly interpolate the two targets using \(s=(p-p_*)/(1-p_*)\). The source is affine in p, the F face is linear, and all capacity/mass/time/hinge constraints are affine. Their nonnegative interpolation therefore preserves every condition. Finite-support Strassen gives the required seven-node Blackwell transfer, establishing exact sufficiency for the whole real interval.

## Reproduction and continuation

Execute python3 VERIFY_SHARP_P.py beside VERIFY.py. The former checks nine affine-basis evaluations for the identity, two exact endpoints, and 201 rational interpolation regressions. Exact local stdout is in SHARP_OUTPUT.txt. The all-real proof follows from the polynomial identity and affine interpolation.

**Next scientific question:** extend the complete five-parameter F-face slab below p=5/7 using nearby G/F or third-face charts. Test \(p=7/10,\ t=1/13,\ q=1,\theta=\kappa=0\) with a different target face. The new threshold is scoped to the single F face. Source-native claim, independent review and mathematical admission remain unperformed.
