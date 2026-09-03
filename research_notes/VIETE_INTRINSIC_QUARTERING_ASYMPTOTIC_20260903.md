# Viète intrinsic precision law: target-free error quartering and the universal leading coefficient in terms of the rotation completion constant

Status: `FREE_RESEARCH / EXACT TARGET-FREE ASYMPTOTIC / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent: `research_notes/VIETE_TARGET_FREE_ROTATION_COMPLETION_CONSTANT_20260903.md`

## 1. Intrinsic completion constant

The parent constructs, without trigonometry or the target value of classical `pi`, the increasing finite sequence

\[
\Pi_n=2^{n+1}s_n
\]

from

\[
c_0=0,
\qquad
c_{n+1}=\sqrt{\frac{1+c_n}{2}},
\qquad
s_n=\sqrt{1-c_n^2},
\]

and proves that it has a finite limit

\[
L:=\Pi_{\mathrm{rot}}=\lim_{n\to\infty}\Pi_n.
\]

This note derives the leading convergence law using only these finite algebraic relations.

## 2. Exact longitudinal defect identity

Define

\[
d_n:=1-c_n.
\]

Since

\[
1-c_n^2=s_n^2,
\]

one has

\[
\boxed{
d_n=\frac{s_n^2}{1+c_n}.}
\]

Also

\[
s_n=\frac{\Pi_n}{2^{n+1}}.
\]

Therefore the exact scaled defect is

\[
\boxed{
4^{n+1}d_n
=
\frac{\Pi_n^2}{1+c_n}.
}
\]

The parent already proves `c_n->1` and `Pi_n->L`, so

\[
\boxed{
4^{n+1}d_n
\longrightarrow
\frac{L^2}{2}.
}
\]

Thus the longitudinal unresolved-orientation defect itself has an intrinsic quadratic dyadic scale before classical calibration.

## 3. One-step precision increment

Define the positive increment

\[
\Delta_n:=\Pi_{n+1}-\Pi_n.
\]

The finite telescoping law gives

\[
\Pi_n=c_{n+1}\Pi_{n+1}.
\]

Hence

\[
\Delta_n
=
\Pi_n\left(\frac1{c_{n+1}}-1\right)
=
\Pi_n\frac{d_{n+1}}{c_{n+1}}.
\]

Multiply by `4^(n+2)`:

\[
4^{n+2}\Delta_n
=
\frac{\Pi_n}{c_{n+1}}
\left(4^{n+2}d_{n+1}\right).
\]

Using the previous defect limit,

\[
\boxed{
4^{n+2}\Delta_n
\longrightarrow
\frac{L^3}{2}.
}
\]

## 4. Increment ratio tends to one quarter

The exact defect recurrence is

\[
d_{n+1}
=
\frac{d_n}{2(1+c_{n+1})}.
\]

Since `c_n->1`,

\[
\boxed{
\frac{d_{n+2}}{d_{n+1}}
\longrightarrow
\frac14.
}
\]

From

\[
\Delta_n=\Pi_n\frac{d_{n+1}}{c_{n+1}},
\]

one obtains

\[
\frac{\Delta_{n+1}}{\Delta_n}
=
\frac{\Pi_{n+1}}{\Pi_n}
\frac{d_{n+2}}{d_{n+1}}
\frac{c_{n+1}}{c_{n+2}}.
\]

Every factor except the defect ratio tends to `1`. Therefore

\[
\boxed{
\frac{\Delta_{n+1}}{\Delta_n}
\longrightarrow
\frac14.
}
\]

This is a target-free statement: one additional dyadic orientation refinement asymptotically quarters the newly gained scalar correction.

## 5. Tail lemma for a positive ratio-q sequence

Let `a_n>0` and suppose

\[
\frac{a_{n+1}}{a_n}\to q,
\qquad 0\le q<1.
\]

Then for the convergent tail

\[
A_n=\sum_{k=n}^{\infty}a_k
\]

one has

\[
\boxed{
\frac{A_n}{a_n}\to\frac1{1-q}.
}
\]

Proof: for every `epsilon>0`, eventually

\[
q-\epsilon
\le
\frac{a_{k+1}}{a_k}
\le
q+\epsilon
\]

with `q+epsilon<1`. Iterating bounds the normalized tail between the two corresponding geometric series. Let `epsilon->0`.

Apply this with `a_n=Delta_n` and `q=1/4`.

## 6. Exact intrinsic leading error law

Because

\[
L-\Pi_n
=
\sum_{k=n}^{\infty}\Delta_k,
\]

the tail lemma gives

\[
\frac{L-\Pi_n}{\Delta_n}
\longrightarrow
\frac1{1-1/4}
=
\frac43.
\]

Together with

\[
4^{n+2}\Delta_n\to\frac{L^3}{2},
\]

we get

\[
\boxed{
4^{n+2}(L-\Pi_n)
\longrightarrow
\frac{2L^3}{3}.
}
\]

Equivalently,

\[
\boxed{
L-\Pi_n
\sim
\frac{L^3}{6\,4^{n+1}}.
}
\]

This is exactly the classical leading form with `pi` replaced by the intrinsically generated completion constant `L`.

## 7. Error itself quarters intrinsically

Let

\[
E_n:=L-\Pi_n.
\]

From the asymptotic above,

\[
\boxed{
\frac{E_{n+1}}{E_n}
\longrightarrow
\frac14.
}
\]

Thus the statement

> one extra bit of dyadic orientation resolution yields asymptotically two bits of scalar completion precision

is already a theorem of the target-free finite refinement system.

It does not depend on Taylor expansion of sine, on circumference geometry, or on knowing the target constant in advance.

## 8. Classical coefficient is recovered only afterward

The separate compatibility theorem identifies

\[
L=\Pi_{\mathrm{rot}}=\pi.
\]

Substituting into the intrinsic law gives

\[
\pi-\Pi_n
\sim
\frac{\pi^3}{6\,4^{n+1}}.
\]

Therefore the familiar coefficient `pi^3/6` is not an input used to explain the precision rate. It is the classical name for the intrinsically generated coefficient

\[
\boxed{L^3/6}.
\]

## 9. Precision-state interpretation

The finite state variables already determine the asymptotic precision mechanism:

- `Pi_n` is the current scalar readout;
- `d_n` is the longitudinal unresolved-orientation defect;
- the exact identity
  `4^(n+1)d_n = Pi_n^2/(1+c_n)`
  links state defect to scalar precision;
- the local correction increments have limiting ratio `1/4`;
- the total remaining error has the same limiting ratio.

Hence the quadratic precision gain is structurally encoded by the half-angle recurrence itself.

## 10. Strength boundary

This theorem assumes the G1 target-free normalized equal-resultant refinement already derived for #1158. It does not upgrade that refinement to a canonical G0 Cell rotation law.

What is now closed at G1 strength is substantially stronger:

1. the completion constant exists without classical `pi`;
2. finite states internally bracket it;
3. its convergence order is intrinsically `4^-n`;
4. the exact leading coefficient is `L^3/6`;
5. only afterward does classical compatibility rename `L` as `pi`.

The unresolved native question is therefore solely about how the Cell/trace substrate generates or realizes the refinement, not about why the resulting precision sequence converges or why its error quarters.
