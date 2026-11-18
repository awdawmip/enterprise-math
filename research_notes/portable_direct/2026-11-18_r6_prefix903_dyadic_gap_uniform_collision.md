# PREFIX-903 — A uniform dyadic-gap named-XOR collision theorem and exact overlap-free 19-bit coverage

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6; independent portable-direct BRC auxiliary mathematics.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Predecessor: PREFIX-902 (three-panel 192-row union); PREFIX-897 four-family exclusion.
Status: AUTHOR_PROVED / EXACT_DECLARED_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Researcher provenance: earlier real session `EM-DIRECT-8A42B6` / `RA-2EBCA87CB3F6736530738843`; independent science, no claim to shared X6 task ownership.

## 1. Exact finite model and theorem

Let `p=32`, `N=2^32`, `Q={262145,262147,...,524287}` (`|Q|=131072`).
An admissible, **named** directed trajectory is `Z_x=(x,x)` or `F^i_x=(x,x XOR 2^i)` for `0<=x<N`, `0<=i<32`. Its source name `i`, direction and two endpoints remain part of the full trajectory identity. The auxiliary observer is
\[
\Phi_{a,b}(u,v)=(u\bmod a, v\bmod b).
\]

**Theorem 903-A (uniform same-source dyadic-gap collision).**
For any odd `a,b` in `Q`, if `|a-b|=2^h` for some integer `1<=h<=17`, then there are distinct admissible **same-source** bit-flip trajectories with identical two-port observations. The construction needs no CRT search, floating point, or auxiliary carry automaton.

*Constructive proof for `a=b+2^h`.* Put `t=2^(h-1)`, `i=h-1`, and `r=a mod (2t)`. Define
\[
x=\begin{cases}0,&r\ge t,t-r,&r<t,\end{cases}
qquad y=x+a.
\]
Because `a` is odd and `2t` is even, `r` is odd and nonzero. Hence `0<=x<t`, so bit `i` of `x` is zero, whereas `(x+a) mod 2t` lies in `[t,2t)`, so bit `i` of `y` is one. Thus the two admissible named trajectories
\[
F^i_x=(x,x+t),qquad F^i_y=(y,y-t)
\]
flip **the same named source** in opposite directions. Their respective starting points differ by `y-x=a`, and their ending points by
\[
(y-t)-(x+t)=a-2t=b.
\]
Therefore both starting residues modulo `a` and both ending residues modulo `b` coincide. Both trajectories lie in `[0,N)`: `a<=524287`, `t<=65536`, `x<t`, hence `y<a+t<N`. They are distinct since `y>x`. QED.

For `b=a+2^h`, reverse the two displayed trajectories and swap the observation ports, obtaining the same constructive collision in the reverse ordered pair; this is a trajectory-level permutation in the finite auxiliary model, not an assumption about native physical time reversal.

Concrete **previously uncovered** example: `a=376491`, `b=376489`, `i=0`; `F^0_0=(0,1)` and `F^0_{376491}=(376491,376490)` collide. Neither parameter belongs to the old four-family collision set or its 192-row panels.

## 2. Exhaustive dyadic family and exact de-duplication

Different odd moduli in Q differ by a multiple of two. The maximum positive difference is `524287-262145=262142`. Consequently all power-of-two positive differences are exactly `2^h` with `1<=h<=17`.
For each h, the number of increasing ordered pairs `(a,b)` with `a-b=2^h` is `131072-2^(h-1)`. Dyadic families do not overlap across different h; their reverses are disjoint. The full ordered family contains
\[
D=2\sum_{h=1}^{17}(131072-2^{h-1})=\boxed{4,194,306}
\]
pairs, every one of which has a named-XOR collision certificate.

Define E as the **exact PREFIX-897** symmetric certified set:
\[
E=\{(a,b)\in Q^2:ab<33N \lor a\in U \lor b\in U
 \lor \mathrm{lcm}(a,b)<N
 \lor 33\lceil N/a\rceil>b \lor 33\lceil N/b\rceil>a},
\]
where U is the 552-element special-modulus set (16 PREFIX-893 rows, 24 PREFIX-887 axis moduli and 512 PREFIX-895 rows), reproduced exactly in the attached program. Let P be the 192-element PREFIX-900/901/902 three-panel set, also specified in the program. The complete previously counted **explicit union** is `C_902=E union (P×Q) union (Q×P)`, with `|C_902|=7,614,875,038`.

For dyadic pairs, `gcd(a,b)=gcd(b,2^h)=1` because b is odd; thus `lcm(a,b)=ab>N`, and the zero-zero LCM branch of E cannot occur. The independent `E` and `P` membership tests, **for every positive-gap pair**, produce the following exact ordered counts after ×2 for time reversal:

| Classification inside D | Ordered pairs |
|---|---:|
| All dyadic-gap pairs | 4,194,306 |
| Previously in E | 1,846,732 |
| Touching an existing P row or column | 10,878 |
| E and P overlap | 16 |
| Previously certified C_902 intersection = E + P - overlap | 1,857,594 |
| **Genuinely new relative to C_902** | **2,336,712** |

Thus the strengthened duplicate-free finite **certified union** is exactly
\[
\boxed{|C_{903}|=7,614,875,038+2,336,712=7,617,211,750}
\]
ordered pairs, and its complement in `Q^2` contains exactly
\[
\boxed{17,179,869,184-7,617,211,750=9,562,657,434}
\]
pairs. The latter are **outside the stated certificate union**, not assertions of injectivity.

The machine-readable JSON includes all seventeen disjoint gap-class subtotals. `PREFIX903_R6_DYADIC_GAP_CENSUS.py` is standard-library Python that enumerates **all 2,097,153 increasing dyadic pairs**, constructs and asserts the precise named-source witness and both modular equalities for each, recomputes E and P membership from their exact definitions, and verifies the two inclusion-exclusion totals. All arithmetic is exact integer arithmetic. There is no sampling in this full family; no independent reviewer has examined the proof.

## 3. Role, ontology and next mathematical question

This lemma concerns a bounded, provenance-preserving **auxiliary** two-port BRC observer. It does not equate the two residue ports to the full P000 native six-dimensional X6 Cell state, nor certify descent under future native operations; source labels and trajectories remain distinguishable before observation. It does not change P000, the ACTIVE Heartbeat World (6 spatial axes + separately typed time), three-dimensional slice semantics or residual-fidelity constraints. The historical frozen science input remains unchanged.

The mother question `B_fix,odd(32) in {19,20}` remains open. Next: derive a broader uniform collision lemma for non-dyadic differences, or run an exhaustive and independently crosschecked general two-flip candidate checker on the remaining uncovered parameter families. Preserve any genuine injective modulus pair if discovered. Activity/CLAIM/Result/Review statuses must be separately verified; this scientific publication is not a formal shared-X6 CLAIM or mathematical admission.
