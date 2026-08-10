# P022 — Franel tail continuant and Euler–Wallis projective return

Status: `PROVED_WIP / EXACT LARGE-TERMINAL NORMAL FORM`  
Owner: `P022 / program/p022-geometry-v2`  
Depends on: large terminal gap reduction; Franel recurrence; Euler–Wallis formulas  
Scope: the remaining `q>4r-3` terminal escape after primitive twin-center deferral

## 1. Starting point

Let `q` be an odd prime which first divides the Franel sequence at rank `r`, and
assume the large-terminal range

\[
q>4r-3.
\]

The existing delayed-capture analysis shows that the dangerous second Franel
zero is

\[
F_{2r-2}\equiv0\pmod q.
\]

The large-gap companion reduction already replaces this by divisibility of the
fixed integer

\[
R_r=P_{r-2}\!\left(-\frac{4r-3}{2}\right),
\]

where `P_g(x)` is the universal companion-gap continuant.

This note identifies `R_r` inside the ordinary integer-normalized Franel
recurrence and then inside the Euler–Wallis continued-fraction system.

## 2. Prior-art boundary

Joseph Tonien, *Franel Numbers and a Continued Fraction Conjecture Discovered
by the Ramanujan Machine*, The Mathematical Intelligencer (2026), proves the
Ramanujan-Machine continued fraction and records its Euler–Wallis recurrence

\[
p_n=a_np_{n-1}+b_np_{n-2},
\qquad
q_n=a_nq_{n-1}+b_nq_{n-2},
\]

with

\[
a_n=7n^2+7n+2,
\qquad
b_n=8n^4,
\]

and the exact numerator identity

\[
\boxed{p_n=(n+1)!^2F_{n+1}.}
\]

The paper also gives the second Franel basis solution and the standard
Casoratian.

All of that is prior art.  P022 owns only the specialization of this system to
the Barlow terminal-gap obstruction and the resulting exact capture normal
forms below.

## 3. P022-TC01 — integer-normalized Franel recurrence

Set

\[
U_n=(n!)^2F_n.
\]

The Franel recurrence becomes

\[
\boxed{
U_{n+1}
=(7n^2+7n+2)U_n+8n^4U_{n-1}.
}
\]

This is exactly the Euler–Wallis recurrence of the continued fraction.

For fixed `r>=4`, define the normalized tail solution

\[
T_r^{(r)}=0,
\qquad
T_{r+1}^{(r)}=1,
\]

and propagate it by the same integer recurrence.

## 4. P022-TC02 — the fixed companion gap is a standard tail continuant

The affine companion elimination uses the formal reflection scale

\[
S_r
=
\frac{4^{r-2}(2r-3)!!}{r(r+1)}.
\]

A direct factorial calculation gives

\[
\boxed{
S_r^2
\left(\frac{(r+1)!}{(2r-2)!}\right)^2
=4^{r-3}.
}
\]

Consequently the fixed gap integer is exactly

\[
\boxed{
R_r
=(-1)^{r+1}4^{r-3}T_{2r-2}^{(r)}.
}
\]

Thus `R_r` is not a new auxiliary sequence: away from the prime `2`, it has
exactly the same prime divisors as the standard tail continuant of the
integer-normalized Franel recurrence.

The first values are

\[
R_4=-848,
\quad
R_5=2173312,
\quad
R_6=-10712812544,
\quad
R_7=88888688640000.
\]

## 5. P022-TC03 — exact Euler–Wallis cross determinant

Let `p_n/q_n` be the Euler–Wallis convergents.  The general continuant
cross-determinant identity specializes to

\[
\boxed{
 p_{2r-3}q_{r-1}-p_{r-1}q_{2r-3}
 =
 2^{r+6}(r!)^4R_r.
}
\]

Because

\[
p_{r-1}=r!^2F_r,
\qquad
p_{2r-3}=(2r-2)!^2F_{2r-2},
\]

this is already an exact bridge between the fixed gap and the two Franel
values relevant to terminal escape.

## 6. P022-TC04 — explicit unit state at the first zero

Assume now that

\[
q>4r-3,
\qquad
q\mid F_r.
\]

Franel zeros cannot be adjacent, so `F_(r-1)` is a `q`-unit.  Tonien's
Casoratian for the Franel solution and the standard second solution gives

\[
F_{r-1}B_r-F_rB_{r-1}
=
\frac{(-8)^{r-1}}{r^2}.
\]

Since

\[
q_{r-1}=r!^2B_r,
\]

reduction modulo `q` yields the explicit source denominator

\[
\boxed{
q_{r-1}
\equiv
\frac{(r-1)!^2(-8)^{r-1}}{F_{r-1}}
\pmod q.
}
\]

Every factor is a `q`-unit.  Therefore the first Franel zero corresponds to
the well-defined projective convergent state

\[
\boxed{
[p_{r-1}:q_{r-1}]=[0:1]
\quad\text{in }\mathbf P^1(\mathbf F_q).
}
\]

## 7. P022-TC05 — `R_r` is the normalized terminal Franel coordinate

Use TC03 and `p_(r-1)=0 mod q`.  Because the source denominator is the explicit
unit in TC04, one obtains

\[
\boxed{
F_{2r-2}
\equiv
(-1)^{r-1}2^{9-2r}r^4
\left(\frac{(r-1)!}{(2r-2)!}\right)^2
F_{r-1}R_r
\pmod q.
}
\]

All factors multiplying `R_r` are `q`-units in the large-terminal range.
Hence

\[
\boxed{
q\mid F_{2r-2}
\iff
q\mid R_r.
}
\]

This recovers the large-gap zero equivalence, but now with its exact unit
normalization rather than only a Boolean detector.

## 8. P022-TC06 — projective-return formulation

TC03--TC05 give the geometric reformulation

\[
\boxed{
q\mid R_r
\iff
[p_{2r-3}:q_{2r-3}]
=[p_{r-1}:q_{r-1}]
=[0:1]
\quad\text{in }\mathbf P^1(\mathbf F_q).
}
\]

Thus the remaining large-terminal escape problem is:

> Can the non-autonomous Euler–Wallis projective recurrence return to the zero
> convergent state after exactly `r-2` tail steps, when its first Franel zero
> occurred at rank `r`?

This is a strictly smaller object than the original Barlow valuation problem.
It is also a standard continuant-return question in the same recurrence system
as the Franel continued fraction.

## 9. Experimental primitive-gcd boundary

Exact integer computation in the current research session gives strong but
noncanonical evidence for the sharper statement

\[
\boxed{
q>4r-3,\ q\mid F_r
\Longrightarrow
q\nmid R_r.
}
\]

Equivalently, no large projective return was found in the tested range.
A scan through `r<=2000` found no prime factor greater than `4r-3` in

\[
\gcd(F_r,F_{2r-2}).
\]

The only primitive common factors seen in that scan were the already-known
critical one-third examples `(r,q)=(2,5)` and `(50,149)`; these lie on
`q=3r-1`, not in the large-terminal range, and the critical boundary is already
captured by the separate one-third theorem.

This paragraph is `EXPERIMENTAL / NOT A THEOREM`.  It is route guidance only.

## 10. New theorem target

The most direct remaining mother statement is now

\[
\boxed{
q>4r-3,\quad r_q=r
\Longrightarrow
[p_{2r-3}:q_{2r-3}]\ne[0:1].
}
\]

Equivalent forms are

\[
q\nmid R_r,
\]

or

\[
q\nmid F_{2r-2}.
\]

A proof of any one form closes the entire large-prime terminal-escape branch.
Combined with the already-proved strict-window and critical-boundary capture
results, this would leave only the forced-copy pollution route as an alternate
proof mechanism rather than a necessary escape patch.

## 11. Executable assets

- `src/enterprise_math/p022_barlow_franel_tail_continuant.py`;
- `tests/test_p022_barlow_franel_tail_continuant.py`.

They certify the exact tail identity, the power-of-four normalization, Tonien's
scaled-Franel numerator inside the recurrence, the cross determinant, the
explicit source denominator residue, the normalized terminal residue, and the
projective-return equivalence.
