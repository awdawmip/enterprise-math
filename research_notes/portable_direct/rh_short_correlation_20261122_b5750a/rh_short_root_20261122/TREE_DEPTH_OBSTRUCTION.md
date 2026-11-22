# Exact optimal envelopes need not admit logarithmic-depth trees

Author auxiliary source family, 2026-11-22. This continues the freely ordered
ancestor-envelope theorem. It is a general-source example, not an example
or counterexample for the actual matched arithmetic road.

## 1. A rational complete-integer family at the old fine-scale threshold

For each integer \(s\ge8\), set

\[
 X=s^4,\qquad h=s^3=X^{3/4},\qquad
 x_j=X+jh\quad(0\le j\le s).
\]

The true block is \([X,2X]\). Its endpoint interpolant is \(J=0\).
Prescribe the fine samples

\[
 y_j=j^2\quad(0\le j<s),\qquad y_s=0.
 \tag{1}
\]

Define the complete road on *every* integer by evaluating the following
piecewise polynomial, and extend it by zero outside the block:

\[
 q(x_j+uh)=(1-H(u))y_j+H(u)y_{j+1},\qquad
 H(u)=3u^2-2u^3,\quad0\le u\le1.
 \tag{2}
\]

All integer values are exact rationals with common denominator dividing
\(h^3\). The endpoint derivatives of every cell are zero, so the extension
is \(C^1\); its second derivative is bounded on each cell and has no
point mass at a join. In particular,

\[
 |q''|\le\frac{6\max_j|y_{j+1}-y_j|}{h^2}
 \le\frac{6(s-1)^2}{s^6}\le\frac6X.
\]

The exact averaging identity
\(\Delta^2q(n)=\int_{-1}^1(1-|u|)q''(n+u)\,du\) gives

\[
 \boxed{|f_n|=|{-\Delta^2q(n)}|\le6/X\le12/n
       \quad(X\le n\le2X).}
 \tag{3}
\]

The continuous polynomial is only a convenient proof of an inequality
about the specified rational integer sequence. It introduces no additional
native direction, continuum premise, or arithmetic-road identification.

## 2. Any exactly optimal ancestor tree is a chain

Let \(F=I_\Pi q\) be the fine linear interpolant through (1). It is
nonnegative. The freely ordered ancestor theorem says the minimum possible
partial-interpolation envelope is \(\max(J,F)=F\).

Suppose a legal binary tree attains that minimum at all integer points.
Its first inserted point must be \(x_1\). If it instead inserted \(x_j\)
with \(j>1\), the first interpolation at \(x_1\) would be

\[
 y_j\frac{x_1-X}{x_j-X}=j>1=F(x_1).
 \tag{4}
\]

Because the ancestor envelope retains the maximum of all partial
interpolants, this overshoot cannot be undone by later insertions.

After the forced insertion of \(x_k\), all previously exposed points on
the left are \(x_1,\ldots,x_k\), while the remaining right interval has
endpoints \(x_k,2X\). If its next root were \(x_j\), \(j>k+1\), the
chord from \((x_k,k^2)\) to \((x_j,j^2)\) would take the value

\[
 k^2+\frac{j^2-k^2}{j-k}=k^2+j+k
 >(k+1)^2=F(x_{k+1}).
 \tag{5}
\]

Thus every next root is forced. The unique attaining hierarchy is the
right-going chain
\(x_1,x_2,\ldots,x_{s-1}\), with \(s-1\) occupied depth levels. It is
also the min-Cartesian hierarchy of the increasing residual samples.

\[
 \boxed{\text{Exact optimality forces depth }s-1=X^{1/4}-1.}
 \tag{6}
\]

This conclusion concerns exact attainment. It does not by itself give a
lower bound on the cost of an approximate envelope at prescribed depth.

## 3. The example retains the source and fine-remainder controls

The depth obstruction is not obtained by putting an order-one point mass
in the source. Equation (3) supplies a fixed source constant. Moreover,
the fine remainder \(P=q-F\) tends to zero in critical weighted norm.

On cell \(j\),

\[
 P(x_j+uh)=(y_{j+1}-y_j)(H(u)-u),\qquad
 |H(u)-u|=|u(1-u)(2u-1)|\le1/4.
\]

Summing all integer interiors, with zero remainder at the knots, gives

\[
 \|P\|_w^2
 \le\frac{h}{16X^2}\sum_{j=0}^{s-1}(y_{j+1}-y_j)^2.
\]

The exact finite difference sum is

\[
 (s-1)^4+\frac{(s-1)(4(s-1)^2-1)}3.
\]

Consequently

\[
 \boxed{\|P\|_w^2\le\frac1{16s}+\frac1{12s^2}\longrightarrow0.}
 \tag{7}
\]

This also bounds \(\|P_+\|_w^2\). The actual positive road energy remains
of constant size. Indeed \(0\le q\le s^2=\sqrt X\), so \(S(q)\le2\).
On the cells \(j=\lceil s/2\rceil,\ldots,s-2\), the road is at least
\(s^2/4\); their combined length is at least \(X/4\) for \(s\ge8\).
Since \(n\le2X\),

\[
 \boxed{1/256\le S(q)=\sum_{n=X}^{2X}q_n^2/n^2\le2.}
 \tag{8}
\]

Thus the example has true endpoints, the complete integer population,
uniform \(|f_n|\le12/n\), the previous \(X^{3/4}\) fine scale, a
vanishing fine remainder, and bounded critical energy, yet no
logarithmic-depth tree attains its optimal ancestor envelope exactly.

## 4. What this changes in the continuation

The unrestricted sorting construction is a valid exact optimization
theorem, but its hierarchy can be deep. Arguments which depend on
logarithmic depth must retain that condition or pay the depth actually
constructed. The all-tree matching theorem in
`UNIFORM_ADAPTIVE_REFERENCE_STABILITY.md` already uses a bound valid for
every integer hierarchy, so it survives this example.

Signed-frontier retention offers a different tradeoff: keep a shallower
geometric tree while preserving some negative subtree information.
Neither this depth example nor the optimal ordering theorem supplies the
missing arithmetic estimate for the actual matched road.

The accompanying script checks the complete rational road and all source
values for \(s=8,12,16\), the forced-root inequalities, and the stated
energy/remainder bounds using exact integer arithmetic with outward
rational energy rounding. The proof above establishes the infinite family.
