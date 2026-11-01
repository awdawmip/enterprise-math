# BRC N=4 BU: second rational-splice theorem, capacity optimum through b=73/500

2026-10-29 · Author-side exact analytic theorem, UNREVIEWED / NOT_ADMITTED.

## Input and preserved scope

Use the previously established BRC N4 BU finite strictly positive P/Q 16-leaf probability model with target `F=(a,b,1,0)` and full terminal observer `(T,Decision,Z_BU)`. Competitors are all legal real causal randomized S2/S23 policies. The four-atom reduction, event-TV bounds `L0,L3` and capacity lower bound are the author-side exact results used in Enterprise Math PR #1713, merged commit `f4fda6745598fa27aaacfed0d812da5f1be23899`, and earlier predecessor `d78e2b5729c824918126aec8ffb26ff3e5dc4cb5`. This result extends that theorem and leaves P000/X6, 3D slice, AU/future observer or physical-time mapping outside its statement.

Use the same formulas:

\[
\alpha(b)=\frac{\sqrt{121b^2+10b+25}-4b}{5},\quad
C=\frac{7-a-21b}{4a+12b+2},\quad
\delta=\frac{1-a}{3},\quad B_*=b-\delta,\quad E=\frac{B_*C}{4},
\]

\[
G(a,b)=5a^2+8ab-21b^2-2b-5,
\]

\[
L_0(u)=\frac{4a-14b-3au-(a+3b)u^2}{2(23-2u)},\qquad
L_3(u)=\frac{u[a-(a+3b)u]}{2(7-2u)}.
\]

The inherited *legal observable-event* lower bounds are `e>=L0(u)` for `0<=u<=3/7`, `e>=L3(u)` for `0<=u<=1` and `e>=B_*u/4` when `B_*>0`. Previously checked exact identities include `L3(C)=E` and `E-δ=G/[8(2a+6b+1)]`. All claims below are conditioned on these inherited proofs and no independent review is claimed.

## New all-real-parameter theorem

For every real

\[
\boxed{0<b\le\frac{73}{500}=0.146,\qquad\alpha(b)\le a\le1,}
\]

all lawful real competitors have the exact common optimum

\[
\boxed{d_2=d_{23}=\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}=E.}
\]

The new rational splice is `k=9/25=0.36`. The preceding PR #1713 covered only `b<=27/200=0.135`; the original `b_sharp≈0.127407` is therefore strictly inside the now-proved region, and cannot represent a genuine phase switch. The number `73/500` is a sufficient endpoint of this certificate, not a proved sharp phase boundary.

## Complete exact proof relative to the inherited observer lemmas

Let `a0=9607/10000`, `b1=73/500`. The positive a-root of G is α(b). At fixed a=a0, G is strictly concave quadratic in b; its maximum over all real b occurs at `b0=(8a0-2)/42=2369/17500`, where

\[
G(a_0,b_0)=-310557/700000000<0.
\]

Thus `G(a0,b)<0` for every real b, and since G is strictly increasing in positive a, `alpha(b)>a0` for all `0<b<=b1`. Also the exact identity `G(1-3b/5,b)=-24b²<0` implies `alpha(b)>1-3b/5`. Hence `B_*>4b/5>0`, `E>=δ>=0`, `C<1`. The same derivative formulas as in PR #1713 show C strictly decreases in a,b over this domain, with the exact lower bound

\[
C\ge C(1,b_1)=489/1292>9/25=k
\quad\text{(difference }597/32300\text{)}.
\]

The k=9/25 substitutions give two *new exact* gap formulas:

\[
L_0(k)-E=\frac{N(a,b)}{334200(2a+6b+1)},
\]

\[
N=55781a^2+243936ab-90472a+229779b^2-692766b+97475,
\]

\[
L_3(k)-E=\frac{(61a+633b-157)(121a+363b-175)}{94200(2a+6b+1)}.
\]

On the larger rational rectangle `a0<=a<=1`, `0<=b<=b1`, one has

\[
\partial_bN\le-95433633/250<0,
\quad \partial_aN(a,b_1)\ge261601347/5000>0,
\]

so

\[
N(a,b)\ge N(a,b_1)\ge N(a_0,b_1)=1044937989/100000000>0.
\]

For the other gap, the factors are bounded above by `−1791/500` and `−501/500`, so both are negative and the product strictly positive. Thus `L0(k)>E` and `L3(k)>E` everywhere claimed.

The inherited monotonicity and no-interior-minimum results for L0/L3 now prove, for **all real** `u in [0,1]`, by the exhaustive three-piece partition:

\[
\begin{array}{ll}
0\le u\le k:& e\ge L_0(u)\ge L_0(k)>E;\\
k\le u\le C:&e\ge L_3(u)\ge\min\{L_3(k),L_3(C)\}=E;\\
C\le u\le1:&e\ge B_*u/4\ge B_*C/4=E.
\end{array}
\]

For the matching lawful upper bound take the genuine causal strategy

\[
(A,B,u,U,V)=(1,B_*,C,B_*(1+C),B_*).
\]

It satisfies `0<B_*<=b<=73/500`, `0<C<1`, `0<U<2b<=73/250<1=A`, `0<=V=B`. The complete four observed signed atom differences, inherited and independently checked by the code, are exactly

\[
\Delta_Q=(\delta,E-\delta,0,-E),\qquad \Delta_P=(0,0,E,-E).
\]

As `0<=δ<=E`, both P- and Q-law total variations are E. Hence the global lower and upper bounds match throughout the claimed continuous real domain. QED.

## Exact new witness and verification range

At `(a,b)=(961/1000,73/500)` one has `G=417/1000000>0`, so it is inside this theorem. Exact construction gives

\[
C=991/2532,\quad \boxed{\operatorname{TV}_P=\operatorname{TV}_Q=E=131803/10128000}.
\]

`VERIFY_K9P25.py` reuses the immutable prior full 16-leaf harness and actually executes 10 *new* exact symbolic identities and three *new* rational witnesses (both P and Q law), in addition to the imported 29 earlier symbolic checks and six earlier witnesses. Its imported predecessor is the actual earlier GitHub `VERIFY.py`, not a substitute semantic simulation. The saved evidence is stdout from execution. This is author-side analytic plus exact testing, not formal independent proof checking. Native active owner/CLAIM/Result/review was not acquired, and P000/worldview remains unchanged.

## Next

Investigate b>73/500, beginning with b=147/1000 and rational a>=alpha(b). The current fixed splice may fail because L0(k)-E becomes negative at the lower curve; seek variable legal joint-event dual or an exact two-law 16-leaf counterexample, and separate certificate insufficiency from genuine strategy change.
