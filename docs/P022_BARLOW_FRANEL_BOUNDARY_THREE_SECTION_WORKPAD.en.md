# P022 Barlow — Boundary three-section workpad

Status: **ACTIVE_WIP / exact algebra only / no closure claim**

This file records the next attack on the sign-free companion

\[
W_M=\sum_{j=0}^{2M-1}
\binom{2M}{j}\binom{M+j}{j}\binom{2M-1}{j}
\pmod{p},\qquad p=6M-1.
\]

At the surviving q=3r-1 boundary, `M=3m`.  Writing

\[
w_j=\binom{2M}{j}\binom{M+j}{j}\binom{2M-1}{j},
\]

we split

\[
W_{3m}=W^{(0)}_m+W^{(1)}_m+W^{(2)}_m,
\qquad
W^{(a)}_m=\sum_{j\equiv a\ (3)}w_j.
\]

The exact hypergeometric ratio is

\[
\frac{w_{j+1}}{w_j}
=
\frac{(2M-j)(2M-1-j)(M+1+j)}{(j+1)^3}.
\]

Modulo `p=6M-1`, the parameters become the fixed rational triple

\[
-2M\equiv-\frac13,\qquad
1-2M\equiv\frac23,\qquad
M+1\equiv\frac76,
\]

so the sign-free polynomial is the terminating representative of

\[
{}_3F_2\!\left[
\begin{matrix}-1/3,2/3,7/6\\1,1\end{matrix};z
\right]
\]

at `z=1`, with termination supplied by the integer parameter `-2M` before
reduction.

The three-section is naturally cyclotomic: over a field containing a primitive
cube root `omega`, if

\[
P_M(z)=\sum_{j=0}^{2M-1}w_jz^j,
\]

then

\[
W^{(a)}_m=
\frac13\sum_{t=0}^2\omega^{-at}P_M(\omega^t).
\]

For `p=5 (mod 6)`, `omega` lies in `F_(p^2)` and Frobenius exchanges
`omega <-> omega^2`.  This matches the already-frozen period-two Dwork/Galois
orbit of the cyclotomic P022 hypergeometric datum.  The next proof target is to
identify an exact Frobenius relation between `P_M(omega)` and
`P_M(omega^2)` strong enough to force `P_M(1)=W_M` nonzero on the admissible
`M=3m` twin-boundary line.

No such nonvanishing theorem is asserted here yet.
