# Free Research — Pi-to-Prime Geometry Frontier V18

Status: `FREE_RESEARCH_CURRENT_FRONTIER / ODD-SIMPLEX TERMINAL COERCIVITY / ODD-SIMPLEX LYAPUNOV NO-GO / PARITY FOLD AS VOLTERRA COMMUTATOR DEFECT / ALL-ORDER POSITIVE COMMUTATOR JET / ABSTRACT DELAYED BLOCK CLOSED / ARITHMETIC JET ENERGY RECURRENCE OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V17_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Research-Mode: `FREE_AXIOM_DISCOVERY`

## 1. Stable chain retained from V17

The stable arithmetic geometry remains

\[
\boxed{
\begin{aligned}
\text{prime }p
&=\text{irreducible multiplicative-holonomy birth direction},\\
p^a
&=\text{the }a\text{th winding layer},\\
\det\mathcal W_N
&=\operatorname{lcm}(1,\ldots,N),\\
\psi(N)&=\log\det\mathcal W_N.
\end{aligned}}
\]

The odd two-simplex gives the exact terminal coercivity

\[
4U_N^2|r(N)|^2
\le3\mathfrak E_N,
\qquad
r(N)=\psi(N)/N-1.
\]

The local retained relation state has the residual-free matrix

\[
T(s)=
\begin{pmatrix}
(1-2s)^2&0\\
\frac49s(1-s)&s
\end{pmatrix},
\]

and the associated Mellin critical exponent is the unique root

\[
\beta_{\rm ch}=0.522033\ldots
\]

of

\[
\beta^3-5\beta^2+10\beta-4=0.
\]

All of these statements remain valid.

---

## 2. V18 correction: the full odd simplex is not the recursive Lyapunov state

For the adaptive quotient Markov operator `P` and residual

\[
e=(I+P)f,
\]

the complete odd-simplex energy satisfies the exact identity

\[
\boxed{
\mathfrak O_P(f)
=2\bigl(f^2+P^2(f^2)+P(fe)+fPe\bigr).
}
\]

In the homogeneous interior,

\[
\mathfrak O_P(f)=2(f^2+P^2f^2).
\]

Thus the odd packet is a coercive present-plus-even-return graph norm. The direct composite chord is the correct terminal anchor, but the same chord prevents the packet from being a strict one-step positive Lyapunov function.

Accordingly, the V17 phrase “embed the whole odd-simplex energy into a strict same-type two-channel recurrence” was too strong. The valid split is now:

\[
\boxed{
\text{odd simplex for terminal scalar coercivity},
\qquad
\text{adjacent/standard channels for recursive transport}.
}
\]

The remaining even-depth component must be removed by signed cancellation, moving-boundary coercivity, or a growing-depth state.

---

## 3. The parity fold is an exact operator commutator defect

Fix top cutoff `N`, write

\[
A=A(N),
\]

and define

\[
(S_Nf)(n)=\frac{A(n)}A f(n),
\]

\[
(J_Nf)(n)=
\frac1A\sum_{a\le n}\frac{\Lambda(a)}a
f(q_a(n)).
\]

Then

\[
\boxed{
([S_N,J_N]f)(n)
=
\frac1{A^2}
\sum_{a\le n}\frac{\Lambda(a)}a
\bigl(A(n)-A(q_a(n))\bigr)f(q_a(n)).
}
\]

At the top state,

\[
\boxed{
([S_N,J_N]-J_N^2)f(N)
=
\frac1{A^2}
\left[
\sum_{ab>N}u_au_bf(q_a(N))
-
\sum_{ab\le N}u_au_bf(q_{ab}(N))
\right].
}
\]

The right side is exactly the V15 stopped parity fold.

Hence

\[
\boxed{
\text{scalar prime-error carrier}
=
\text{defect of the ideal Volterra identity }[S,J]=J^2.
}
\]

For `g=(S_N+J_N)f`, evaluation at `N` gives the exact resolvent

\[
f(N)=g(N)-J_Ng(N)-([S_N,J_N]-J_N^2)f(N).
\]

For `f=r`, the first two terms are `O(1/log N)`.

---

## 4. All-order commutator/provenance jet

For `k>=0`,

\[
\boxed{
\operatorname{ad}_{S_N}^k(J_N)f(n)
=
\frac1{A^{k+1}}
\sum_{a\le n}u_a
\bigl(A(n)-A(q_a(n))\bigr)^k
f(q_a(n)).
}
\]

Define

\[
K_{N,k}=\frac1{k!}\operatorname{ad}_{S_N}^k(J_N),
\qquad
D_{N,k}=K_{N,k}-J_N^{k+1}.
\]

Each `K_(N,k)` is a positive one-step tail-capacity channel; `J_N^(k+1)` is an ordered `(k+1)`-history channel. Thus every defect is a difference of two retained positive provenance measures.

In the ideal logarithmic continuum,

\[
(Sf)(t)=tf(t),
\qquad
(Jf)(t)=\int_0^t f(u)du,
\]

and

\[
\boxed{
[S,J]=J^2,
\qquad
\operatorname{ad}_S^k(J)=k!J^{k+1}.
}
\]

All ideal defects vanish. The finite arithmetic defects are therefore the exact noncommutative curvature of the moving prime cutoff.

---

## 5. Higher defect as one positive variance

Let `mu_(N,k)` and `nu_(N,k)` be the positive endpoint measures of `K_(N,k)` and `J_N^(k+1)`, and put

\[
\sigma_{N,k}=\mu_{N,k}+\nu_{N,k}.
\]

For every bounded readout `|f|<=B`,

\[
\boxed{
|D_{N,k}f(N)|
\le
B\bigl||\mu_{N,k}|-|\nu_{N,k}|\bigr|
+
\sqrt{
|\sigma_{N,k}|\,
\mathscr V_{\sigma_{N,k}}(f)
}.
}
\]

For fixed `k`, bounded first-mass discrepancy gives

\[
|\mu_{N,k}|,
|\nu_{N,k}|
=
\frac1{(k+1)!}+O_k(1/\log N).
\]

Hence

\[
\boxed{
|D_{N,k}f(N)|
\le
O_k(B/\log N)
+
\sqrt{
\left(
\frac2{(k+1)!}+O_k(1/\log N)
\right)
\mathscr V_{\sigma_{N,k}}(f)
}.
}
\]

The first fold recovers the V15 scalar readout; higher folds have factorially smaller terminal variance mass.

---

## 6. Delayed recanonicalization is algebraically viable

For the V17 Mellin matrix `M(beta)` and terminal variance conversion `L_9=(1,9)`, define

\[
\mathfrak m_d(\beta)
=L_9\mathcal M(\beta)^d(1,0)^T.
\]

Then

\[
\boxed{
\mathfrak m_d(\beta)
=A(\beta)^d
+9C(\beta)
\sum_{j=0}^{d-1}
A(\beta)^{d-1-j}B(\beta)^j.
}
\]

At one level,

\[
\mathfrak m_1(\beta)=1/(1-\beta)>1,
\]

which proves the per-level recanonicalization no-go.

For every

\[
0<\beta<\beta_{\rm ch},
\]

both diagonal Mellin entries are below one and

\[
\mathfrak m_d(\beta)\to0.
\]

Two exact design points are

\[
\boxed{
\mathfrak m_3(1/4)
=10429760/12326391<1,
}
\]

and

\[
\boxed{
\mathfrak m_4(1/3)
=567/625<1.
}
\]

Thus a genuine four-level arithmetic intertwiner would have a margin

\[
58/625
\]

for an energy exponent `1/3`, corresponding after the one-time square-root readout to scalar exponent `1/6`.

This is an exact conditional design calculation, not a completed prime remainder theorem.

---

## 7. Why two channels do not compose by themselves

Let

\[
H=S+J,
\qquad
U=I-S+J.
\]

In the continuum,

\[
\boxed{HU-UH=2[S,J]=2J^2.}
\]

In the arithmetic model the same commutator is the tail-capacity channel, and its failure to equal `J^2` is the parity-fold defect itself.

Therefore applying one stopped-row mean creates a new commutator channel before the next level. Repeating `M(beta)` as if the first component were again the original arithmetic root silently drops that channel.

The correct exact block state at depth `d` is finite but larger:

\[
\boxed{
\text{root/standard channels}
+
\text{commutator defects }D_{N,1},\ldots,D_{N,d-1}
+
\text{their ordered transported relation fields}.
}
\]

The carrier dimension may grow with the selected finite block depth. This remains compatible with finite-state Enterprise typing at every finite cutoff.

---

## 8. Current smallest open theorem

The vague V17 “global positive embedding” has been replaced by the following finite target.

### Four-level commutator-jet theorem

Construct a positive quadratic norm on the depth-four state containing

\[
D_{N,1},D_{N,2},D_{N,3}
\]

and their relation fields such that:

1. normal ordering of four stopped-row steps is exact;
2. every transported full residual contributes `O((log N)^-2)` after normalization;
3. moving tail terms descend to a strict lower logarithmic band;
4. the total commutator/provenance error is less than the exact margin `58/625` for all large `N`;
5. terminal conversion is paid once through the higher-fold variance readout.

If this theorem is proved, it yields the first completely native logarithmic prime remainder in the present program.

---

## 9. What is now closed

Closed exactly or at fixed-order research-note strength:

1. odd-simplex graph-norm identity;
2. no-go for treating the full odd packet as a universal fixed-type Lyapunov state;
3. parity fold as the first arithmetic Volterra commutator defect;
4. all-order positive tail-capacity jet;
5. ideal Volterra and stopped-Beta identities;
6. one-variance scalar readout for every defect order;
7. fixed-order factorial mass law;
8. delayed-recanonicalization block multiplier;
9. exact depth-three and depth-four design margins.

Open:

1. finite positive normal ordering for the depth-four relation state;
2. a Poincare/observability inequality transferring first-fold energy through the commutator jet;
3. coefficient-safe lower-scale tail iteration;
4. unconditional native logarithmic decay;
5. Working Truth, Foundation, or RH-scale promotion.

The decisive V18 interpretation is:

\[
\boxed{
\text{prime-counting error}
=
\text{finite noncommutative curvature of cutoff mass and quotient transport}.
}
\]
