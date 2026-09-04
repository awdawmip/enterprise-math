# Free Research — Persistent Row-Mixer Intertwiner

Status: `FREE_RESEARCH_FRONTIER / EXACT_ROW_RESTRICTION_INTERTWINER / RESIDUAL_FORCING_SUMMABLE / VARIANCE_CHANNEL_PROPAGATES_WITHOUT_INVERSE / ROOT_CHANNEL_LEFT_INVERSE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the V15 stopped/core fold, the weighted `S_3` value mixer, and the full scalar residual estimate.

## 1. Executive advance

The V15 row scattering law can be made into an exact finite intertwiner for the standard variance channel.

For a parent state `N`, fix a first action `a` and put

\[
m=\left\lfloor\frac Na\right\rfloor,
\qquad
\alpha=\frac{A(m)}{A(N)}.
\]

Inside the second-action row:

- valid actions `b<=m` carry the child cloud `g_m(b)=r(floor(m/b))`;
- stopped actions `b>m` carry the constant value `x_m=r(m)`.

Let `K_N^row` be the weighted `S_3` value mixer acting only in that second-action row:

\[
K_N^{\rm row}F
=\frac13F+\frac23\mathbb E[F\mid a].
\]

Then the restriction of `K_N^row F_N` to the valid core is exactly the already mixed child cloud `K_m g_m`, plus one constant.  Constants do not affect relation energy.  Therefore the child standard variance passes to the parent with coefficient `alpha` and **without any inverse profile-comparison factor**.

This closes one half of the two-channel state-propagation problem.  The remaining half is a root/parity left inverse that reads `r(N)` from the retained mixed state without applying the worst-case scalar factor `9` at every level.

---

## 2. Stopped/core row

Let

\[
p_N(b):=\frac{\omega(b)}{A(N)},
\qquad
\omega(b)=\frac{\Lambda(b)}b.
\]

The valid core `b<=m` has mass

\[
\alpha=\sum_{b\le m}p_N(b)=\frac{A(m)}{A(N)}.
\]

Conditioned on the core, `p_N` becomes exactly the child action probability

\[
\frac{p_N(b)}\alpha=\frac{\omega(b)}{A(m)}=p_m(b).
\tag{2.1}
\]

Define

\[
F_{N,a}(b)
:=
\begin{cases}
 g_m(b):=r(\lfloor m/b\rfloor),&b\le m,\\
 x_m:=r(m),&b>m.
\end{cases}
\tag{2.2}
\]

Let

\[
\bar g_m:=\mathbb E_{p_m}g_m,
\qquad
\eta_m:=x_m+\bar g_m.
\tag{2.3}
\]

The full residual theorem gives

\[
\boxed{|\eta_m|\ll(1+\log m)^{-1}.}
\tag{2.4}
\]

The row mean is

\[
\begin{aligned}
\mu_{N,a}
&=\alpha\bar g_m+(1-\alpha)x_m\\
&=\boxed{(1-2\alpha)x_m+\alpha\eta_m.}
\end{aligned}
\tag{2.5}
\]

Put

\[
d_m:=x_m-\bar g_m=2x_m-\eta_m.
\tag{2.6}
\]

---

## 3. Exact core restriction intertwiner

The row mixer is

\[
(K_N^{\rm row}F_{N,a})(b)
=\frac13F_{N,a}(b)+\frac23\mu_{N,a}.
\]

On the valid core,

\[
(K_mg_m)(b)
=\frac13g_m(b)+\frac23\bar g_m.
\]

Subtracting gives the exact constant shift

\[
\boxed{
(K_N^{\rm row}F_{N,a})(b)-(K_mg_m)(b)
=\frac23(1-\alpha)d_m,
\qquad b\le m.
}
\tag{3.1}
\]

Hence

\[
\boxed{
\operatorname{Var}_{p_m}
\bigl((K_N^{\rm row}F_{N,a})|_{b\le m}\bigr)
=\operatorname{Var}_{p_m}(K_mg_m).
}
\tag{3.2}
\]

This is the desired persistent-state intertwiner: the same mixed child relation state reappears literally in the parent core, modulo a harmless constant gauge.

The mean of the mixed core and the mixed stopped atom differ by

\[
\boxed{
\frac13(\bar g_m-x_m)=-\frac13d_m.
}
\tag{3.3}
\]

Thus the stopped/core contrast amplitude is divided by `3`, and its energy by `9`.

---

## 4. Exact row ANOVA after mixing

Define the persistent child standard energy

\[
\boxed{
V(m):=\operatorname{Var}_{p_m}(K_mg_m)
=\frac19\operatorname{Var}_{p_m}(g_m).
}
\tag{4.1}
\]

The law of total variance, (3.2), and (3.3) give

\[
\boxed{
\operatorname{Var}_{p_N}(K_N^{\rm row}F_{N,a})
=\alpha V(m)
+\frac19\alpha(1-\alpha)d_m^2.
}
\tag{4.2}
\]

Adding the squared row mean yields the exact second moment

\[
\boxed{
\begin{aligned}
\mathbb E_{p_N}
\bigl[(K_N^{\rm row}F_{N,a})^2\bigr]
={}&\bigl((1-2\alpha)x_m+\alpha\eta_m\bigr)^2\\
&+\alpha V(m)
+\frac19\alpha(1-\alpha)(2x_m-\eta_m)^2.
\end{aligned}}
\tag{4.3}
\]

When `eta_m=0`, this becomes

\[
\boxed{
k(\alpha)x_m^2+\alpha V(m),
}
\tag{4.4}
\]

where

\[
k(\alpha)=1-\frac{32}{9}\alpha(1-\alpha).
\]

Thus the V15 profile kernel and the persistent child variance occur in one exact row formula.

---

## 5. Residual-stable upper bound

View the first and third terms of (4.3) as a squared two-component vector.  Its homogeneous part has squared norm `k(alpha)x_m^2`.  Its residual part has squared norm

\[
\alpha^2\eta_m^2+
\frac19\alpha(1-\alpha)\eta_m^2
\le\alpha\eta_m^2.
\]

Therefore, for every `delta>0`,

\[
\boxed{
\begin{aligned}
\mathbb E[(K_N^{\rm row}F_{N,a})^2]
\le{}&(1+\delta)k(\alpha)x_m^2
+\alpha V(m)\\
&+(1+\delta^{-1})\alpha\eta_m^2.
\end{aligned}}
\tag{5.1}
\]

The error is summable after averaging over the first action.  Indeed,

\[
\begin{aligned}
\mathbb E_{p_N(a)}[\alpha\eta_m^2]
&\ll\frac1{A(N)^2}
\sum_{a\le N}
\frac{\omega(a)A(m)}{(1+\log m)^2}\\
&\ll\frac1{A(N)^2}
\sum_{a\le N}
\frac{\omega(a)}{1+\log m}\\
&\ll\boxed{\frac{\log\log N}{(\log N)^2}.}
\end{aligned}
\tag{5.2}
\]

The states `m=1` have `alpha=0`, so no singular term is hidden at the absorbing boundary.

---

## 6. The child-variance channel itself has a positive one-step bound

From (4.1), centering at zero rather than at the optimal mean gives

\[
\boxed{
V(m)
\le\frac19
\mathbb E_{p_m(b)}
\left[r\!\left(\left\lfloor\frac mb\right\rfloor\right)^2\right].
}
\tag{6.1}
\]

Consequently,

\[
\begin{aligned}
\mathbb E_{p_N(a)}[\alpha V(m)]
&\le\frac1{9A(N)^2}
\sum_{\substack{a,b\\ab\le N}}
\omega(a)\omega(b)
 r(\lfloor N/(ab)\rfloor)^2.
\end{aligned}
\tag{6.2}
\]

This is a positive valid-two-history subpacket.  In the ideal logarithmic model, its action on the barrier `T^-beta` has multiplier

\[
\boxed{
\frac1{9(1-\beta)(2-\beta)}.
}
\tag{6.3}
\]

Thus the variance channel is quantitatively compatible with the same multiplicative Volterra calculus.  What is missing is not control of this channel, but a compatible recurrence for the root/parity channel.

---

## 7. Exact remaining left-inverse problem

The V15 scalar resolvent reads `r(N)` from the **unmixed** signed folded field.  The row mixer preserves ordinary row means but not the stopped/core parity functional.  At one row,

\[
\mathbb E[\varepsilon F]=x_m-\alpha\eta_m,
\qquad
\varepsilon=
\begin{cases}-1,&b\le m,\\+1,&b>m.
\end{cases}
\tag{7.1}
\]

After row mixing,

\[
\mathbb E[\varepsilon K_N^{\rm row}F]
=\frac13\mathbb E[\varepsilon F]
+\frac23(1-2\alpha)\mu_{N,a}.
\tag{7.2}
\]

In the homogeneous case, the coefficient of `x_m` in (7.2) is

\[
1-\frac83\alpha(1-\alpha),
\]

whose minimum is `1/3`.  A rowwise scalar inversion therefore costs up to `3` in amplitude or `9` in energy, exactly the scalar-recanonicalization no-go.

The valid next theorem cannot invert row by row.  It must use either:

1. the global one/two-history parity-block coupling, where unmatched mass is only `e^-1`; or
2. a two-component parity frame whose mean and standard coordinates are transported together and read only once at the terminal scale.

---

## 8. Updated boundary

Closed exactly:

1. conditional core measure equals the child prime-power measure;
2. the mixed parent core is the mixed child cloud plus a constant;
3. child standard variance propagates with coefficient `alpha` and no inverse factor;
4. stopped/core contrast energy receives the exact `1/9` factor;
5. the full row second moment is (4.3);
6. residual forcing is `O(log log N/(log N)^2)`;
7. the variance channel is a positive two-history packet.

Open:

1. a global parity left inverse that avoids rowwise factor `9`;
2. composition with the V16 block coupling;
3. one closed two-channel Volterra recurrence;
4. any promoted logarithmic prime remainder;
5. any RH-scale conclusion.

The main gain is that the standard channel no longer has a state-propagation ambiguity.  The only unresolved state component is the scalar parity/root coordinate.
