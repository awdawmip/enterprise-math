# R131.5 — A nonzero-step one-hot witness window

Date: 2026-11-14 (Asia/Shanghai). Continuation of R131 on the same frozen S23 auxiliary scientific input 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Author-side proof; independent review pending.

## Statement

Use the S23 correlated observer

  S_i(theta) = 1[ {x+(A+i*d) theta} < {E theta} ],
  0<=i<m, {z}=z-floor(z), theta in (0,1).

Let integers m>=1 and B>=m+2, and set

  x=0, A=B, d=1, E=1.

Here d is nonzero: S_i(theta)=1[{(B+i)theta}<theta], so the coordinates are not all identical.

**Theorem (exact one-hot tiling).** Define the rational window

  W = [1/(B+m-1), 1/(B-1)).

For every real theta in W, exactly one of the m bits equals 1. More precisely,

  S_i(theta)=1  iff
  theta in [1/(B+i), 1/(B+i-1))  (theta restricted to W).

The m half-open intervals tile W without a gap or overlap, ordered from
i=m-1 down to i=0. Thus each one-hot word e_i is attainable. The all-zero
word is also attainable outside W.

An exact rational one-hot witness is

  theta_i = (1/(B+i) + 1/(B+i-1))/2,

and an exact all-zero witness is

  theta_empty = 1/(2(B+m-1)).

Their numerators and denominators are O((B+m)^2), hence each witness
has O(log(B+m)) bits. Given a target of the form 0^m or e_i, a
membership certificate is computed by O(m) pattern scanning and a
constant number of exact integer arithmetic operations on O(log(B+m))-bit
values. The theorem establishes **at least m+1 distinct attained words**.
It makes no assertion that these are all globally attained words over
theta in (0,1).

**Proof.** For theta in W and every 0<=i<m, the assumptions B>=m+2
give

  0 < (B+i)*theta
    < (B+m-1)/(B-1)
    <= (2B-3)/(B-1) < 2.

Thus floor((B+i)theta) belongs to {0,1}. If it is zero then
{(B+i)theta}=(B+i)theta>theta because B+i>=2, hence S_i=0.
If its floor is one, then

  S_i=1 iff (B+i)theta-1 < theta
         iff theta < 1/(B+i-1).

The floor-one condition is theta>=1/(B+i). Therefore in W,

  S_i=1 iff 1/(B+i)<=theta<1/(B+i-1).

The right endpoint for index i is the left endpoint for i-1:
1/(B+i-1). The largest-index interval begins at the left end of W,
and index zero ends at the right end of W; the strict endpoint
convention assigns every internal boundary to the interval starting
there. Consequently the intervals partition W and exactly one bit is 1.

The theta_i are strict interior points of the appropriate intervals.
At theta_empty each (B+i)theta <=1/2 and exceeds theta, so all bits
are zero. Numerators and denominators of these rational witnesses
have the stated size, giving polynomial bit complexity. QED.

## Input-sensitive trace consequence

The first bit S_0(theta)=1[{Btheta}<theta] is exactly the
R131.1 pulse indicator, with 2B-3 genuine cuts in (0,1).
Each change of S_0 necessarily changes the complete m-bit word,
regardless of the other coordinates. Hence the full ordered joint
trace has at least 2B-3 actual cuts and explicit trace generation
costs Omega(B) event records, while the above m+1 particular
pattern/exact-witness questions have polynomial input-bit cost.
The latter is a partial membership oracle, not a solution for
arbitrary m-bit patterns of the nonzero-d family.

## Exact verification

Companion check_r131_onehot.py independently computes all bits by
the original Fraction-based fractional-part comparison. For
m=1..18 and B=m+2..m+42, 738 parameter pairs were checked
against every cut and open-cell sample of W: 14,022 positions.
A total of 7,749 positive/negative rational certificates were checked.
Further tests cover 5,000 deterministic random (m,B,i) samples
and a 121-decimal-digit B at m=64.
Result: R131_NONZERO_D_ONEHOT_PASS.

The finite tests validate the implementation and half-open boundaries;
the general conclusion is established by the proof above.
No native X6 event-licensing assertion or independent review is made.

## Next question

Determine which additional patterns occur outside W for
x=0,A=B,d=E=1, and seek a polynomial-in-(m,log B)
decision method for **arbitrary specified patterns** when B is large.
This is more demanding than generating the m+1 known certificates
and avoids conflating full trace output with word membership.
