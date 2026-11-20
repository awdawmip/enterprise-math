# C85: a rigorous Haar cusp contribution to the reading-position comparison

## Statement and scope

Use the endpoint-normalized three-read function from C84, with
`l_theta(u,v)=(u,(1-theta)u+theta v,v)`. The auxiliary unit-covolume Haar lattice
has reduced coordinates

\[
 v=\rho e_\phi,\qquad
 w=x\rho e_\phi+\rho^{-1}e_\phi^\perp,
 \quad |x|\le\tfrac12,\quad y=\rho^{-2},\quad0\le\phi<\pi.
\]

The three source phases are independent and uniform on `[0,1]^3`. They have
the exact joint limiting meaning already proved in C84. No native spatial
coordinates are replaced by these auxiliary lattice coordinates.

Let `S_theta` be the largest scale at which some nonzero lattice vector
retains all three source bins. Put `q=1/10`, and define the *unnormalized cusp
contribution*

\[
 I_\theta^{\rm cusp}(Y)
  =\mathbb E[S_\theta^q\mathbf1_{\{y\ge Y\}}].
\]

The cusp has Haar probability `3/(pi Y)` for `Y>=1`. This note proves

\[
 \boxed{I_{1/4}^{\rm cusp}(Y)<I_{1/2}^{\rm cusp}(Y)
 \quad\text{for every }Y\ge5.}                 \tag{1}
\]

In particular, this comparison covers a lattice-shape region of probability
`3/(5 pi)`, approximately 19.1%, including all shears, all orientations and all
source phases. At `Y=5` the contribution difference satisfies the concrete
bound

\[
 \boxed{I_{1/4}^{\rm cusp}(5)-I_{1/2}^{\rm cusp}(5)<-1/60000.} \tag{2}
\]

The compact complementary shape region remains part of the full comparison
`I_(1/4)<I_(1/2)`. Its sign is not asserted here.

## 1. Exact phase integral for a single direction

Write `B_theta(v)` for the largest successful scale from the unoriented
primitive direction `+/-v` alone. If

\[
 m_j=|l_{\theta,j}(v)|,\qquad M=\max_jm_j,
\]

then the plus and minus feasibility boxes give

\[
 \Pr(B_\theta(v)>s)
 =2\prod_{j=0}^2(1-sm_j)_+
  -\prod_{j=0}^2(1-2sm_j)_+.                 \tag{3}
\]

Consequently, for any `0<q<2`,

\[
 \mathbb E B_\theta(v)^q
  =K_q q\int_0^{1/M}s^{q-1}
       \prod_{j=0}^2(1-sm_j)\,ds,
 \qquad K_q=2-2^{-q}.                       \tag{4}
\]

For `v=(u,v_2)`, convex interpolation gives
`M=max(|u|,|v_2|)`, independently of theta. With `a=|u|`, `b=|v_2|`, and
`m=|(1-theta)u+theta v_2|`, the expression in (4) is affine decreasing in `m`.
It is therefore concave as a function of theta for each fixed lattice
direction after phase integration. This assertion concerns one direction;
the maximum over all competing directions has not been interchanged with
the phase expectation.

For a unit direction `e_phi`, put

\[
 C_\theta(\phi)=\mathbb E B_\theta(e_\phi)^q,
 \qquad
 H_q(r)=\frac1{(q+1)(q+2)}-
        \frac r{(q+2)(q+3)}.
\]

The coefficient of `-m` in (4) is
`K_q q M^(-q-1) H_q(min(a,b)/M)`.

## 2. All other directions have a uniformly small critical scale

A vector `k=m v+n w` outside the short direction has integer `n!=0` and
`det(v,k)=n`. If it succeeds at scale sigma, its endpoint coordinates satisfy
`|sigma k_1|<1` and `|sigma k_2|<1`. Hence, for
`d(phi)=|cos phi|+|sin phi|`,

\[
 \sigma|n|=|\det(v,\sigma k)|\le\rho d(\phi).
\]

In particular, for every shear and every phase,

\[
 B_\theta(v)\le S_\theta
 \le\max\{B_\theta(v),\rho d(\phi)\}.       \tag{5}
\]

Let `e_2(m)=m_0m_1+m_0m_2+m_1m_2` and `e_3(m)=m_0m_1m_2`, now evaluated
at the unit vector `e_phi`. When `s<=rho d` and `y>=3`, all factors in (3)
are untruncated, because `2 s rho M<=2 sqrt(2)/3<1`. The exact lower-tail
polynomial is

\[
 \Pr(B_\theta(\rho e_\phi)<s)
  =2e_2(m)\rho^2s^2-6e_3(m)\rho^3s^3.       \tag{6}
\]

By (5), layer integration gives the fully uniform estimate

\[
\begin{split}
0\le\mathbb E[S_\theta^q-B_\theta(v)^q]
&\le\int_0^{\rho d}q s^{q-1}
           \Pr(B_\theta(v)<s)\,ds\\
&=\frac{2q e_2(m)d^{q+2}}{q+2}\rho^{q+4}
 -\frac{6q e_3(m)d^{q+3}}{q+3}\rho^{q+6}\\
&\le\frac{2q e_2(m)d^{q+2}}{q+2}\rho^{q+4}.
                                                        \tag{7}
\end{split}
\]

Thus the error does not require an infinite vector search, a fixed-radius
cutoff assumption, or independence between different lattice directions.

## 3. Haar integration: a power law with an explicit remainder

The normalized Haar measure on this cusp is

\[
 d\mu=\frac6{\pi^2}\rho\,d\rho\,dx\,d\phi.
\]

Integrating (4) and (7) yields, for `Y>=3`,

\[
 I_\theta^{\rm cusp}(Y)
  =\frac6{\pi^2(2-q)}Y^{-1+q/2}
       \int_0^\pi C_\theta(\phi)\,d\phi+R_\theta(Y),
                                                        \tag{8}
\]

where

\[
0\le R_\theta(Y)\le
 \frac{12q}{\pi^2(q+2)(q+6)}
 Y^{-(q+6)/2}
 \int_0^\pi e_2(m)d^{q+2}\,d\phi.            \tag{9}
\]

The principal coefficient in (8) is symmetric and strictly concave in
theta. Symmetry follows by swapping endpoint axes. For strictness, in the
opposite-sign quadrant there is a positive-measure interval of directions
whose middle coordinate changes sign between any two distinct positions;
the coefficient multiplying its absolute value is strictly positive.
This proves a precise cusp leading-term version of midpoint maximality.

## 4. The quarter/midpoint angular gap

The same-sign quadrants cancel in the integrated difference. In the
opposite-sign quadrant, pair the two endpoint orders, write
`a=max(|cos phi|,|sin phi|)`, `r=b/a`, and use

\[
\frac{|3a-b|+|a-3b|}{4}-(a-b)
 =\begin{cases}0,&r\le1/3,\\(3b-a)/2,&r\ge1/3.
 \end{cases}
\]

It follows that

\[
\begin{split}
D_q&:=\int_0^\pi[C_{1/2}(\phi)-C_{1/4}(\phi)]\,d\phi\\
&=\frac{K_q q}{2}\int_{1/3}^1
 (3r-1)H_q(r)(1+r^2)^{q/2-1}\,dr>0.         \tag{10}
\end{split}
\]

More generally, for `t=min(theta,1-theta)` and `s=1-t`, the analogous gap is

\[
2K_q q\int_{t/s}^1(sr-t)H_q(r)
       (1+r^2)^{q/2-1}\,dr.
\]

At `q=1/10`, ordinary numerical quadrature gives `D_q≈0.007230354092494249`
and the principal coefficient `6D_q/[pi^2(2-q)]≈0.002313435899383384`.
The sign proof below uses exact inequalities instead of these decimals.

## 5. An elementary sign certificate for every Y>=5

Only the positive quarter remainder in (8) is needed for an upper bound on
`I_quarter^cusp-I_mid^cusp`, because the midpoint remainder is nonnegative.
The following angular integral is exact:

\[
 Q:=\int_0^\pi e_2(m_{1/4})d^2\,d\phi
 =\frac{57}{20}+\frac{13\pi}{16}
       -\frac34\arctan(1/3)<\frac{26}5.     \tag{11}
\]

For completeness, the `m_0m_2` part equals `1+pi/4`. For the remaining part,
pair endpoint orders in `[0,pi/4]`, and split at `phi_0=atan(1/3)`. On the
lower interval the opposite-sign pair contributes `(a-b)(a+b)^3`, whose
integral is `39/100`. On the upper interval it contributes `(a+b)^4/2`.
Using

\[
\int_0^{\pi/4}(\cos\phi+\sin\phi)^4d\phi=1+3\pi/8,
\quad
\int_0^{\phi_0}(\cos\phi+\sin\phi)^4d\phi
=2/25+(3/2)\phi_0
\]

gives (11). The upper bound follows from `pi<22/7` and
`atan(1/3)>3/10`, which give `Q<145/28<26/5`.

Put `q=1/10`. Exact integration of the polynomial factor in (10) gives

\[
 H_*:=\int_{1/3}^1(3r-1)H_q(r)dr=\frac{40400}{193347}.      \tag{12}
\]

Since `(1+r^2)^(q/2-1)>=2^(q/2-1)` and `d^q<=2^(q/2)`, equations
(8)--(12) imply

\[
\begin{split}
I_{1/2}^{\rm cusp}(Y)-I_{1/4}^{\rm cusp}(Y)
\ge\frac{q2^{q/2}}{\pi^2}Y^{-61/20}
\left[\frac{3K_q H_*}{2(2-q)}Y^{21/10}
             -\frac{12Q}{(q+2)(q+6)}\right].             \tag{13}
\end{split}
\]

All following comparisons are exact integer-power or rational checks:

\[
 K_q>16/15,\qquad5^{1/10}>7/6,
\]

because `(15/14)^10<2` and `(7/6)^10<5`. Therefore the square bracket in
(13), for every `Y>=5`, is strictly larger than

\[
 \frac{175414240}{672267519}>0.                            \tag{14}
\]

Equivalently, the lower principal contribution divided by the upper
remainder is greater than

\[
 \frac{21563500}{20467161}>1.
\]

This proves (1). At `Y=5`, use `pi<22/7`, `2^(q/2)>1`, and
`5^(61/20)<150` (equivalent to the exact integer check `5^61<150^20`).
The lower bound in (13) is then greater than

\[
 \frac1{150}\frac{30697492}{11620624257}>\frac1{60000},
\]

which proves (2).

## Evidence and continuation

`verify_cusp.py` checks every rational coefficient and integer-power
inequality used in the certificate. It also checks the polynomial moment
and angular-gap identities symbolically. No random samples enter the proof.
The argument is a hand proof with exact algebraic verification; it is not
a formally checked theorem or a project-admission claim.

Next remaining comparison: the Haar shape region
`sqrt(1-x^2)<=y<5`. The cusp theorem supplies a signed, rigorous contribution
and a rapidly decaying explicit remainder, but it does not assign a sign to
that complementary region.
