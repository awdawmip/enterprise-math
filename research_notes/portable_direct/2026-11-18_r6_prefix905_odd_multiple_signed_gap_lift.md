# PREFIX-905 — Uniform odd-multiple lift of signed dyadic gaps and exact 19-bit coverage

Date: 2026-11-18 (Asia/Shanghai).
Lane: 进取数论研究6, independent portable-direct BRC auxiliary mathematics.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged).
Predecessor: PREFIX-904 (signed two-source gap theorem and certified union).
Status: AUTHOR_PROVED / COMPLETE_DECLARED_FINITE_CENSUS / INDEPENDENT_INTEGER_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model

Let p=32, N=2^32, Q={262145,262147,...,524287}, |Q|=131072.
The legal provenance-preserving named XOR trajectories are Z_x=(x,x)
and F^i_x=(x,x XOR 2^i) for 0<=x<N and 0<=i<32.
The observer is Phi_(a,b)(u,v)=(u mod a, v mod b).

## Theorem 905-A: odd-multiple signed-gap lift

Suppose a,b are in Q, a>b, and there are an odd integer
\`m\` satisfying \`1<=m<=8191\`, integers \`1<=j<i<=17\`,
and a sign \`s in {+1,-1}\` for which
\[
      m(a-b)=2^i+s\,2^j.
\]
Then **two distinct legal named single-source XOR trajectories collide**
under Phi_(a,b). For b>a the corresponding statement follows
by reversing the two trajectories and interchanging observer ports.

**Proof.** Put \`A=ma\`, \`B=mb\`, \`H=2^i\`, \`h=2^j\`,
and \`t=2h\`. Because j<i, t<=H. We first construct two
distinct starting states with difference A.

- If \`s=+1\`, choose \`x=(h-(A mod t)) mod t\`, \`y=x+A\`.
  Then 0<=x<t<=H and \`y mod t=h\`, hence
  \`x XOR H=x+H\` and \`y XOR h=y-h\`.
  The directed named trajectories
  \[
       (x,x+H)\quad\text{[source i]}, \qquad
       (y,y-h)\quad\text{[source j]}
  \]
  have first-endpoint difference \`y-x=A=ma\`
  and second-endpoint difference
  \`(y-h)-(x+H)=A-H-h=B=mb\`.

- If \`s=-1\`, choose \`x=(-A) mod t\`, \`y=x+A\`.
  Now \`y mod t=0\`, so \`x XOR H=x+H\`
  and \`y XOR h=y+h\`; the same first-endpoint difference
  \`A\` accompanies second-endpoint difference
  \`A+h-H=B\`.

Thus the two first endpoints agree modulo \`a\` and their
two final endpoints agree modulo \`b\`. Every endpoint
lies in [0,N): indeed \`x<2h<=H<=2^17\`,
\`y=x+ma\`, and even the generous sufficient bound
\[
      ma+3\cdot2^{17}\le8191\cdot524287+393216
      =4,294,828,033<2^{32}
\]
holds for the entire declared domain. Both flips are legal,
and their source indices differ, so the directed named
trajectories are distinct. Port-reversal preserves legal XOR
flips and yields the opposite-order case. QED.

The theorem is valid for m=1 as well, recovering PREFIX-904.
Here the new coverage is from odd multipliers 3 through 8191.

## Theorem 905-B: complete declared finite overlap-free count

Let D_old be the positive gap set already certified by PREFIX-903/904:
the power-of-two differences 2^h (1<=h<=17) together with all
2^i+2^j and 2^i-2^j (1<=j<i<=17).

Define \`G_905\` to be all positive even integers d not in D_old
such that \`m d=2^i±2^j\` for some odd
\`3<=m<=8191\`, \`1<=j<i<=17\`. Multiple representations
of a gap are deduplicated by d, retaining one valid witness
representation. Exact integer generation gives
\[
             |G_{905}|=\boxed{276}.
\]

Each d yields \`131072-d/2\` positive ordered parameter pairs
(a,b) with \`a-b=d\`, and the theorem explicitly certifies
every one. Reversing the two ports gives a second disjoint set
of pairs \`b-a=d\`.

The previous PREFIX-904 exact certificate union C_904 consists
of (i) the old four-family set E, (ii) all pairs touching a
192-row panel P, and (iii) all old signed/dyadic-gap pairs.
Since G_905 excludes D_old, it suffices to remove E and P
from the newly enumerated gap pairs.

The E and P sets are reconstructed from the original definitions:
\[
\begin{split}
E=\{(a,b):\;&ab<33N\;\lor\;a\in U\;\lor\;b\in U\\
&\lor\operatorname{lcm}(a,b)<N\\
&\lor33\lceil N/a\rceil>b\;\lor33\lceil N/b\rceil>a\},
\end{split}
\]
where U is the exact 552-element PREFIX-897 special modulus set, and
\[
P=\{510001+194j,\ 510003+194j,\ 510005+194j:0\le j<64\}.
\]

The **complete positive-gap census** is:

| Certificate class | Distinct pairs |
|---|---:|
| All newly eligible positive-gap pairs | 35,343,349 |
| Already in E | 15,821,917 |
| Touch an old P row or column | 92,568 |
| E and P intersection | 549 |
| Previously covered (E union P) | 15,913,936 |
| **Genuinely new relative to C_904** | **19,429,413** |

The subtraction is exact:
\[
15,821,917+92,568-549=15,913,936,\quad
35,343,349-15,913,936=19,429,413.
\]
After source-preserving port reversal, the new ordered-pair
coverage equals
\[
           \Delta_{905}=2(19,429,413)=\boxed{38,858,826}.
\]
Combining the explicitly disjoint new gap family with the
verified predecessor:
\[
    |C_{905}|=7,648,061,976+38,858,826
             =\boxed{7,686,920,802}
\]
out of \`|Q|²=17,179,869,184\` ordered strict-19-bit odd modulus
pairs. The complement of this exact stated certificate union is
\[
        \boxed{9,492,948,382}.
\]
These complementary parameters are the remaining *search domain*.

**Previously uncovered concrete witness.** Take
\`a=376497, b=376475, m=3, i=6, j=1\`. Then
\`m(a-b)=66=64+2\`.
The valid named flips
\[
 F^6_3=(3,67),\qquad
 F^1_{1129494}=(1129494,1129492)
\]
have differences \`1129494-3=3a\`
and \`1129492-67=3b\`; both port observations coincide.
The gap 22 is outside D_old, and this pair is outside E/P.

## Complete finite verification

The published \`PREFIX905_R6_ODD_MULTIPLE_GAP_CENSUS.py\`
is the executed NumPy-int64 implementation.
It generates all 276 distinct eligible gaps from all 4095 odd
multipliers 3..8191 and all 272 signed source-index configurations,
selects one valid representation per gap, and visits **all**
35,343,349 positive parameter pairs in the declared domain.
For each pair, it constructs the named trajectories as above
and checks both precise XOR equalities, both observed congruences,
valid endpoint bounds and the multiplier identity.
It then computes E and P by exact integer vector operations,
emitting the complete 276-row JSON certificate:
\`PREFIX905_R6_ODD_MULTIPLE_GAP_RESULTS.json\`.

The actual NumPy run completed with all assertions.
A separate, independently implemented V8 JavaScript
integer census reconstructed U/E/P and the 276 gaps and
reproduced every aggregate count listed above; the uploaded
JSON was emitted from that second computation. No floating
or probabilistic error is present. No independent mathematical
review or formal admission has been performed.

This is a BRC-compatible auxiliary observer
with *named* source/provenance intact.
The P000 six-dimensional spatial ontology and typed time,
native trace and safe-observer descent stay in their original
scopes; no change of the frozen scientific input is made.

## Next scientific question

The mother question remains
\[
       B_{\mathrm{fix,odd}}(32)\in\{19,20\}.
\]
One useful continuation is to characterize small unequal
multipliers \`k a-\ell b\` as signed source-bit gaps,
with endpoint bounds and exact de-duplication. Another is
to test the complement of C_905 using the original complete
flip/flip checker, preserving any verified injective modulus pair.
The control plane must independently establish owner,
Researcher-ID/Activity and any shared CLAIM or Result rights.
