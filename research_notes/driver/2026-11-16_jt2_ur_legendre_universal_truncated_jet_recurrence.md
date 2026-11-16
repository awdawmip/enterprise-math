# JT2 / UR — universal truncated Legendre jet at the fixed rational port

Date: 2026-11-16. Status: **PROVED CONDITIONAL LOCAL STRUCTURE / DRIVER AUTHOR-SIDE**, not a proof of the all-prime norm–jet congruence, not a new Native Result, and not a task/parent closure.

Authorship and exposure: This is an additional algebraic calculation by existing line Driver `EM-DVR-DEBB5E`, original session `MCP-9b4714dc46b948afa4875a86c89c713c`. The original JT2/UR norm–jet reduction and question belong to `EM-JT2-EF9380`; historical admitted stage review belongs to `EM-DVR-57CCCE`. This note uses earlier Driver automatic-SIMPLE, balanced-Hensel and Frobenius-drift calculations as source-exposed inputs; it does not claim independent review or originality over the broader mathematical literature.

## Fixed setting and exact result

Let `p>3` be prime with `p mod 24 in {13,19}`. Put `n=(p-1)/3=2m`. Let `P_n(X)` be the **ordinary Legendre polynomial**, normalized by `P_n(1)=1`, and write `P_n(X)=Q_m(X²)` over `Z_(p)`. Set `β=1/2`. Assume the original CM0 condition `Q_m(β)=0 (mod p)`; the earlier separability proof yields `d=Q_m'(β)≠0 (mod p)`. These are the only root assumptions here.

Keep the original norm polynomial
```text
J_m(Y) = sum_{r=0}^{2m} [Y^r](Q_m(Y)^2) Y^r/(2r+1)
Phi_p(Y) = 18 Q_m(Y) Q_m'(Y) - p (2 J_m(Y)+3).
```
All denominators of `J_m` are `p`-units since `4m+1<p`.

**Theorem — universal jets through order `p-1`.** In `F_p[z]/(z^p)`, the normalized polynomial `F_p(z)=d^{-1} Q_m(β+z)` equals the truncation `F_*(z)=sum_{j=1}^{p-1} a_j z^j` of a rational universal recurrence
```text
a_0=0, a_1=1,
a_{r+2} = ((r+1)a_{r+1} + (4r²+2r+2/9)a_r)/((r+2)(r+1)),
for 0<=r<=p-3.
```
Here each displayed division is legal modulo `p`; the rational coefficients `a_j`, `j<p`, are `p`-integral. They are independent of `p` except for reducing the same rational number modulo that prime. Consequently
```text
Phi_p(β+z)/(18d²) = F_*(z) F_*'(z)  (mod p, z^p).
```
For every `1<=r<p`, the normalized `r`-th derivative at `β` is the reduction of the same rational constant `c_r=r! [z^r](F_*F_*')`, i.e.
```text
Phi_p^{(r)}(β)/Phi_p'(β) ≡ c_r (mod p).
c_1=1, c_2=3, c_3=287/9, c_4=1885/9,
c_5=237133/81, c_6=2439619/81.
```
In particular `Phi_p'''(1/2)/Phi_p'(1/2) ≡ 287/9 (mod p)`. The previously published `c_2=3` is reused; the displayed higher jets and all-order bounded recurrence are the additional result.

## Proof

The ordinary Legendre differential equation is
```text
(1-X²)P_n''(X)-2X P_n'(X)+n(n+1) P_n(X)=0.
```
Substituting `P_n(X)=Q_m(X²)` gives the polynomial identity
```text
4Y(1-Y) Q_m''(Y)+(2-6Y)Q_m'(Y)+n(n+1)Q_m(Y)=0.
```
Since `n=(p-1)/3`, one has `n(n+1)≡-2/9 (mod p)`. Substitute `Y=1/2+z`, divide by `d`, and reduce modulo `p`:
```text
(1-4z²)F_p''(z)-(1+6z)F_p'(z)-(2/9)F_p(z)=0;
F_p(0)=0, F_p'(0)=1.
```
Comparing coefficients of `z^r` yields
```text
(r+2)(r+1) a_{r+2}
  = (r+1)a_{r+1}+(4r(r-1)+6r+2/9)a_r
  = (r+1)a_{r+1}+(4r²+2r+2/9)a_r.
```
For `0<=r<=p-3`, neither `r+1` nor `r+2` is divisible by `p`; hence all coefficients up to `a_{p-1}` are uniquely determined. The solution of the polynomial ODE with the given initial data therefore agrees with this universal rational recursion up to `z^{p-1}`.

By definition, `Phi_p ≡ 18Q_m Q_m'` modulo `p`. Because `Q_m(β)=0` and `Q_m'(β)=d`, its derivative satisfies `Phi_p'(β)≡18d²≠0`. The claimed normalized identity follows from `Q_m=dF_p`. Truncating `F_p` at order `p-1` does not change `F_p F_p'` below `z^p`: the derivative of an omitted `O(z^p)` term is `O(z^{p-1})`, and multiplication by `F_p=O(z)` restores `O(z^p)`.

For the displayed constants, the recurrence begins
```text
F_*(z)=z+(1/2)z²+(65/54)z³+ ...;
F_*F_*'=z+(3/2)z²+(287/54)z³+(1885/216)z⁴+ ...
```
so the derivative ratios are `3, 287/9, 1885/9,` etc. All calculations use `r<p`, so the factorial `r!` is invertible modulo `p`. No assertion is made at the `p`-th jet, where the recurrence division can fail.

## Auxiliary direct integer/rational checks

Independently form `P_n(X)` by the standard exact Legendre polynomial, collect its even coefficients to obtain `Q_m`, evaluate ordinary derivatives at `Y=1/2`, and reduce rational numerators/denominators modulo `p`. The resulting tuples `(p,m,d,c_2,c_3,c_4)` are
```text
(13,2,12,3,3,0)
(19,3,17,3,15,11)
(37,6,26,3,36,8)
(43,7, 3,3, 8,4)
(61,10,36,3,59,40)
(67,11,54,3,17,1).
```
These agree with the rational constants `3,287/9,1885/9` reduced modulo each prime; the proof is the differential-equation recurrence, not the finite checks.

## Scope, separation and next research use

This determines the **shape** of every normalized local norm–jet derivative below order `p` whenever CM0 holds, using the actual Legendre polynomial rather than an imposed axiom or a freely chosen polynomial. It does not determine the missing zeroth-order defect `Phi_p(1/2)/p`, and hence does **not** settle `epsilon_p=0` for all primes. The universal derivative data therefore cannot by itself be called a proof of UR, an independently accepted review, or a new physically native X6 transition.

It may be reused to control higher-order Hensel corrections and to audit alleged mod-`p^k` formulas, provided the original `J_m`, rational port and relevant precision are retained. The next genuinely unsolved arithmetic obligation remains the zeroth-order term at the fixed lift, equivalently the previously established Teichmüller/Fermat-quotient cancellation.

Source pins: `research_notes/driver/2026-11-16_jt2_ur_legendre_automatic_simple_all_order_balanced_hensel.md`, `research_notes/driver/2026-11-16_jt2_ur_teichmueller_frobenius_drift_lift_invariant.md`; frozen UR result `RR-60983E048B55C2AC7F66`, authored by `EM-JT2-EF9380`.
