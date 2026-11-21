# C87 open strengthening: separate concavity would complete pointwise positivity

This is a conditional reduction, not a proved sign certificate.

The averaged-kernel positivity established elsewhere in C87 already suffices
for the complete ordering of I_theta. A stronger pointwise H theorem remains
of independent interest. The low-half square is now proved in
`LOW_HALF_POSITIVITY.md`; the following reduces the rest to a simple signed
fractional-power inequality.

For T(r,s)=r^(41/20) H(r,s/r), define p=41/20 and q=1/20. In each exact C86
chamber,

\[
T(r,s)=\sum_j w_j|a_jr+b_js+c_jrs|^p.
\]

Its second derivative in the first variable, in the interior of a chamber,
is

\[
\frac{T_{rr}(r,s)}{p(p-1)}
=\sum_jw_j(a_j+c_js)^2|a_jr+b_js+c_jrs|^q.
\tag{1}
\]

The exponent has dropped from 41/20 to 1/20. The exact chamber lists with
indices (3,0) and (3,1) coincide, and the lists (2,2), (3,2), (3,3) coincide.
Substituting r=1 and collecting identical affine arguments gives T(1,s)=0
exactly throughout 0<=s<=1. Symmetry gives T(r,1)=0.

Global C1 regularity is false: C86's `phase/KERNEL_REGULARITY.md`, Section 2,
certifies a nonzero normal-derivative jump at (r,s)=(1/2,1/4). No global C1
assumption is used in the conditional reduction here. The relevant local
joins along r in [1/2,1], with s fixed, are as follows.

- If 0<s<1/3, the only interior join is r=2/3 between formulas (2,0) and
  (3,0). They are not identical formulas, but their values and T_r agree
  exactly on that line.
- If 1/3<s<1/2, the only interior join is r=2/3 between (2,1) and (3,1).
  These are also different formulas with exactly matching values and T_r
  on the line.
- If s>=1/2, the formulas (2,2), (3,2), (3,3) are the same symmetric
  expression. This also covers crossing r=s. Since p>2, this single
  expression is C2 throughout the high-high square.

For the two nontrivial vertical joins, substituting r=2/3 makes every argument
an affine function alpha+beta*s. The verifier merges these arguments up to
sign. Value coefficients match exactly. For T_r, it merges the rational
affine coefficients multiplying the common functions
p*sgn(alpha+beta*s)*|alpha+beta*s|^(p-1); both constant and linear coefficient
ledgers match exactly. The fixed-s boundary cases s=1/3 and s=1/2 are covered
by analogous value and tangential T_r ledgers.

`verify_high_half_joins.py` performs all seven required local join checks,
verifies the single symmetric high-high expression, and verifies the four
zero-boundary ledgers at r=1. Its exact result is `high_half_join_checks.json`.
Thus T_r has no jump at any interior join relevant to concavity on [1/2,1].
The known jump across r=1/2 compares derivatives from the left and right of
the endpoint; it does not enter concavity restricted to that closed interval.
Nonpositive second derivatives on the open pieces would therefore imply the
required concavity by these local checks alone.

The remaining candidate is

\[
\boxed{T_{rr}(r,s)\le0\quad(1/2\le r<1,\ 0<s<1).}\tag{2}
\]

Exploratory calculations found no violation, including the full high-high
square with s>r. This is not a proof of (2). Simple stronger assertions about
stochastic ordering or pointwise exponential transforms of the signed
weights in (1) fail, so those approaches cannot be substituted for a proof.

If (2) is established, concavity and the zero boundary immediately imply

\[
T(r,s)\ge2(1-r)T(1/2,s)
\qquad(r\ge1/2,\ 0<s\le1/2).
\]

Together with the proved low-half theorem, this gives

\[
T(r,s)>2(1-r)\frac{37}{500}(s/2)^p.
\]

For r,s>=1/2, apply the same chord lower bound in both coordinates, using
symmetry for the second one:

\[
T(r,s)\ge4(1-r)(1-s)T(1/2,1/2)
>4(1-r)(1-s)\frac{37}{500}4^{-p}.
\]

Thus (2) would prove strict pointwise positivity on the entire open square
and would handle the r→1 and s→1 vanishing factors explicitly. C87 does not
claim this strengthening; it remains a precise possible next research target.
