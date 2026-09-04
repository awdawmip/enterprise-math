# Free Research — Variable-Depth Signed Stopped Resolvent

Status: `FREE_RESEARCH_FRONTIER / EXACT ALL-DEPTH RESOLVENT / RESIDUAL COST d OVER LOG N / IDEAL DEPTH-TWO CANCELLATION / SIGNED KERNEL MIXING IS UNIQUE GATE / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_VOLterra_COMMUTATOR_JET_V18_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Executive advance

The first parity-fold defect and the complete prime error admit an exact variable-depth resolvent.

With the fixed-top operators

\[
H_N=S_N+J_N,
\qquad
T_N=I-H_N=I-S_N-J_N,
\]

`T_N` is the signed stopped kernel: an invalid action keeps the state and its sign, while a valid quotient action lowers the state and flips the sign.

At top evaluation `ell_N`,

\[
\boxed{
\ell_NT_N^2=-\ell_N([S_N,J_N]-J_N^2).
}
\]

For every integer `d>=2` and every field `f`, if `g=H_Nf`, then

\[
\boxed{
 f(N)
=g(N)-J_Ng(N)
+\ell_NT_N^df
+
\sum_{j=2}^{d-1}\ell_NT_N^jg.
}
\]

Since `T_N` is a signed contraction in sup norm and `J_N` is sub-Markov,

\[
\boxed{
|f(N)|
\le
 d\,\|H_Nf\|_\infty
+
|\ell_NT_N^df|.
}
\]

For the normalized prime error, V14 gives

\[
\|H_Nr\|_\infty=O(1/\log N).
\]

Consequently every choice `d=d(N)=o(log N)` gives

\[
\boxed{
|r(N)|
\le
O(d/\log N)
+|\ell_NT_N^dr|.
}
\]

Thus the native prime remainder is exactly reduced to decay of one signed stopped endpoint kernel.

---

## 2. Fixed-top operators

Fix `N` and put

\[
u_a=\Lambda(a)/a,
\qquad
A=A(N)>0.
\]

Define

\[
(S_Nf)(n)=A(n)f(n)/A,
\]

\[
(J_Nf)(n)=A^{-1}
\sum_{a\le n}u_af(q_a(n)).
\]

Then

\[
H_N=S_N+J_N,
\qquad
T_N=I-S_N-J_N.
\]

At every state `n`, the signed row of `T_N` consists of

- diagonal mass `1-A(n)/A>=0`;
- negative quotient masses `-u_a/A` for `a<=n`.

Its row total variation is exactly one. Hence

\[
\boxed{
\|T_Nf\|_\infty\le\|f\|_\infty.
}
\tag{2.1}
\]

Also

\[
\|J_Nf\|_\infty\le\|f\|_\infty.
\tag{2.2}
\]

---

## SSD-T01 — First fold as `-T^2`

Let `ell_N` denote evaluation at `N`. Since

\[
\ell_NS_N=\ell_N,
\]

expand

\[
T_N^2=(I-S_N-J_N)^2.
\]

After applying `ell_N`, the `I,S_N,S_N^2` terms cancel and

\[
\begin{aligned}
\ell_NT_N^2
&=-\ell_NJ_N+
\ell_NJ_NS_N+
\ell_NJ_N^2\\
&=-\ell_N([S_N,J_N]-J_N^2).
\end{aligned}
\]

Therefore

\[
\boxed{
D_{N,1}f(N)=-\ell_NT_N^2f.
}
\tag{3.1}
\]

The parity fold is literally the signed two-step stopped endpoint measure.

---

## SSD-T02 — Exact depth replacement

Put

\[
g=H_Nf=(I-T_N)f.
\]

Since `H_N=I-T_N` is a polynomial in `T_N`, the two operators commute. For `d>=2`,

\[
\begin{aligned}
T_N^2f-T_N^df
&=T_N^2(I-T_N^{d-2})f\\
&=T_N^2
\sum_{j=0}^{d-3}T_N^j(I-T_N)f\\
&=\sum_{j=2}^{d-1}T_N^jg.
\end{aligned}
\]

Thus

\[
\boxed{
T_N^2f
=T_N^df+
\sum_{j=2}^{d-1}T_N^jg.
}
\tag{4.1}
\]

---

## SSD-T03 — Variable-depth scalar resolvent

The first commutator resolvent is

\[
f(N)=g(N)-J_Ng(N)-D_{N,1}f(N).
\]

Using (3.1) and (4.1),

\[
\boxed{
 f(N)
=g(N)-J_Ng(N)
+
\ell_NT_N^df
+
\sum_{j=2}^{d-1}\ell_NT_N^jg.
}
\tag{5.1}
\]

By (2.1)--(2.2),

\[
\begin{aligned}
|f(N)|
&\le2\|g\|_\infty+
|\ell_NT_N^df|+
(d-2)\|g\|_\infty\\
&=
\boxed{
 d\|H_Nf\|_\infty+|\ell_NT_N^df|.
}
\tag{5.2}
\]

This is exact for every finite cutoff and every chosen finite depth.

---

## 6. Prime-error specialization

Let

\[
r(n)=\psi(n)/n-1.
\]

The full adaptive residual is uniformly bounded:

\[
\rho_n(r;n)
=A(n)r(n)+
\sum_{a\le n}u_ar(q_a(n))
=O(1).
\]

But

\[
(H_Nr)(n)=\rho_n(r;n)/A(N).
\]

Therefore

\[
\boxed{
\|H_Nr\|_\infty
=O(1/A(N))
=O(1/\log N).
}
\tag{6.1}
\]

Substitution into (5.2) gives

\[
\boxed{
|r(N)|
\le
O\!\left(\frac d{\log N}\right)
+|\ell_NT_N^dr|.
}
\tag{6.2}
\]

A quantitative native theorem is therefore obtained from any estimate

\[
|\ell_NT_N^{d(N)}r|
\le\varepsilon_N
\]

with

\[
d(N)=o(\log N),
\qquad
\varepsilon_N\to0.
\]

---

## 7. Probabilistic meaning

Lift the state by a parity bit. At state `n`, one step:

- stays at `n` and preserves parity with probability `1-A(n)/A`;
- moves to `q_a(n)` and flips parity with probability `u_a/A`.

Let `(X_d,Pi_d)` be this signed stopped history, with `Pi_d=(-1)^(number of valid moves)`. Then

\[
\boxed{
(\ell_NT_N^df)
=\mathbb E_N[\Pi_df(X_d)].
}
\tag{7.1}
\]

Hence the remaining operator norm is the parity imbalance of the finite stopped endpoint bundle.

The endpoint alone is insufficient: the parity bit is retained provenance and cannot be reconstructed after sign-blind recoalescence.

---

## 8. Ideal continuum cancellation

For

\[
(Sf)(t)=tf(t),
\qquad
(Jf)(t)=\int_0^tf(u)du,
\]

put

\[
T=I-S-J.
\]

At top evaluation,

\[
\ell_1T^2=0
\]

because `[S,J]=J^2`. Therefore

\[
\boxed{
\ell_1T^d=0
\qquad(d>=2).
}
\tag{8.1}
\]

Probabilistically, the stopped endpoint is the running minimum of iid uniforms, while each new record flips parity. Conditional on the final minimum, the even and odd record-order histories cancel exactly after two or more proposals.

Thus the entire arithmetic obstruction is the failure of the discrete prime-mass quotient process to realize this exact record-parity involution.

---

## 9. Relation to fixed-depth no-go

For arbitrary bounded arithmetic fields, no fixed `d` gives a uniform contraction as `N` grows. Energy can concentrate on the all-small-action corner, where every move is valid and the parity is nearly deterministic.

Equation (6.2) does not contradict this. It allows `d=d(N)` to grow. The correct target is a cumulative signed-kernel gap, not a fixed-depth constant.

Potential routes are:

1. increasing-depth record-parity mixing;
2. a relation-energy norm in which `T_N^d` contracts before sup-norm conversion;
3. an arithmetic slow-oscillation theorem for `r`;
4. a hybrid bulk/boundary argument.

---

## 10. Smallest new theorem target

Prove, for one choice such as

\[
d(N)\asymp c\log\log N,
\]

that

\[
\boxed{
|\ell_NT_N^{d(N)}r|
\le
O((\log N)^{-\eta})
}
\]

for some `eta>0`, using only retained signed histories and the bounded full residual.

The depth cost in (6.2) is then

\[
O(\!\log\log N/\log N),
\]

which is smaller than every target power `(log N)^(-eta)` with `eta<1`.

---

## 11. Classification

Closed exactly:

1. signed stopped operator and sup-norm nonexpansion;
2. first parity fold as `-ell T^2`;
3. all-depth replacement identity;
4. variable-depth scalar resolvent;
5. residual cost `O(d/log N)`;
6. probabilistic parity interpretation;
7. ideal depth-two fiberwise cancellation.

Open:

1. decay of the arithmetic signed stopped kernel on the actual prime-error field;
2. a growing-depth record-parity coupling;
3. a quantitative relation-energy norm for `T_N^d`;
4. a promoted native remainder.
