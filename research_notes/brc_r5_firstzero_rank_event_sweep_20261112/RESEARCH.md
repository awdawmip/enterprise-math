# R5 — Exact 2,909 rank-order chambers of the first-zero spectrum

Date: 2026-11-12 Asia/Shanghai. Status: author-side exact finite combinatorial result, dependent on the frozen external P/Q–BRC Blackwell auxiliary-model first-zero theorem (Draft PR #2139, immutable commit `0db2aa81587b0ec7e70cfb7404cf016f70eeb8b5`). Original 15-atom scientific fixture: `435e77af0d180eac32bd1f9c4c464bc4010b7551`; frozen science pins: Global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.

## Statement and scope

This note classifies the **ordered list of distinct subset first-zero capacities**, not all legal full 15-step executions. The previous certified reduction says that for every real `r` in

```
I=[L,U]=[-427508577031693280/628800490619, 1/23],
x=155682221/25142124560000000, E=9/115400000
```

the interior spectrum is the set of fixed values `t_n=36*x/n` for `n in N`, together with moving values `u_q(r)=x*(1-23*r)/q` for `q in {15,12,3}` when `rho_q<r<U`, where `rho_q=(1-q*E/x)/23`. The original frozen integer atoms are

```
w=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80).
N={-sum(w_a for a in S): S subset of 15 atoms, sum(w_a for a in S)<=-3}.
```

Here `|N|=1144`. The source theorem establishes that every listed value occurs and no other coordinate creates an interior first-zero capacity; that certified 28-coordinate reduction is reused, not silently re-proved in this note.

**Theorem (complete ordered-spectrum chamber census).** Over the open parameter interval `L<r<U`, there are exactly **2,908 distinct interior walls**: 3 activation gates and 2,905 fixed/moving collisions. Their complement has exactly **2,909 open intervals**. Every interval has one constant total order of the labeled fixed/moving capacities, and the 2,909 resulting ordered-label sequences are all distinct. The collision walls comprise 2,603 single-pair, 77 two-pair and 225 three-pair simultaneous events. No two moving values coincide for `r<U`.

The three gates, in increasing order, are precisely

```
rho_15=-16881105436483/2066058754891
rho_12=-13486918620883/2066058754891
rho_3 =-3304358174083/2066058754891.
```

The distinct collision walls in the four regions cut out by these gates are respectively `0,1,18,2886`; of the 18 in the two-moving region, 16 are single and 2 are double. In the three-moving region, there are 2,586 single, 75 double, and 225 triple walls.

## Multiplicity formula and exact double-event refinement

For every labeled pair `(q,n)` with `q in {15,12,3}`, `n in N`, the unique equality `u_q(r)=t_n` is at

`r_(q,n)=(1-36*q/n)/23`.

The gates precede these equality points, and all points lie in `(L,U)`. A collision parameter depends only on the rational ratio `q/n`, hence a two-pair collision occurs iff one of three elementary signed-index conditions holds. Writing `k` for a positive integer, their exact counts are:

| Pair of moving labels | Equivalent membership in N | Count inclusive of triples | Pure double (no third label) |
|---|---|---:|---:|
| 3,12 | k,4k in N | 298 | 73 |
| 3,15 | k,5k in N | 227 | 2 |
| 12,15 | 4k,5k in N | 227 | 2 |

There are exactly 225 `k` with `k,4k,5k in N`; these are precisely the triple collisions. In particular the 77 pure doubles split as **73 + 2 + 2**. Inclusion–exclusion gives `3432 - (298+227+227) + 225 = 2905` distinct collision parameters. A triple collision parameter contains **three equality pairs at generally different capacity values**; it is not a collision of moving values with each other.

## Exact rank and chamber sweep algorithm

For an active moving family `q` at a nonwall parameter `r`, its one-based rank within the increasing list of all distinct first-zero capacities is

```
rank_q(r) = 1
   + #{n in N: n > 36*q/(1-23*r)}
   + #{q' in {15,12,3}: rho_q'<r<U and q'>q}.
```

The middle term counts fixed values below `u_q`, while the last counts strictly smaller moving values. Each family enters from the high-capacity end at its gate and crosses every fixed value exactly once as `r` increases. Consequently the number of inversion events counted with pair multiplicity is exactly `3*1144=3432`. If two or three pair-events share one r, they are processed in the same wall bundle; the labels that cross at different capacity levels remain distinct.

Construct `N` without enumerating masks by a shifted Boolean subset-sum bitset. Let `B=1348`; initialize `bits=1<<B`. On integer atom `w_i`, perform `bits |= bits<<w_i` if positive, otherwise `bits |= bits>>(-w_i)`. The set `N` consists of `B-i` for set bits in positions `i<=B-3`. The support has 2,293 distinct sums in the interval [-1348,1348]. Create the 3,432 labeled exact rational events, sort and bundle by r, insert three gates, then sweep in ascending order. After precomputing the support, the event sort costs `O(3432 log 3432)` rational comparisons; producing the full output sequence on every chamber has its natural `O(2909*1147)` output cost. The bitset preprocessing depends on the integer weight range and integer bit complexity and is pseudopolynomial in that range, not a general polynomial-in-bit-length solver.

The 2,909 chamber labels cannot repeat: the moving rank relative to each fixed threshold is monotone strictly decreasing (and each activated moving label remains present until the excluded endpoint U). Any distinct nonwall intervals are separated by an actual gate or a fixed/moving pair crossing, and this pair order cannot revert.

At the zero-perturbation parameter `r=0`, the three collision pairs are `(15,540),(12,432),(3,108)`; the set cardinality is 1,144. At a generic parameter above `rho_3`, it is 1,147.

## Validation, reuse, and next problem

`VERIFY_R5_EVENT_SWEEP.py` was author-side executed with exact Python `Fraction` arithmetic on 2026-11-12 and checked integer bitset support against full 2^15 enumeration; it independently compares all 2,909 ordered-label sequences, event multiplicities, gate positions, triple/double refinements and sector counts. The exact execution transcript is `EXACT_OUTPUT.txt`. This extension reuses the two-coordinate source theorem and its original BRC residual carrier; it is a specialized exact rank classifier, not a new accepted global BRC tool. The published bytes require independent clean-environment rerun and mathematical review; the original P000, X6/native correspondence, shared Task CLAIM and formal Source Result status remain unchanged.

**Next unfinished unit:** derive a compact per-wall update certificate for the rank vector (rather than materializing all full ordered sequences), test whether fixed-spectrum witness masks can be attached to the event stream without exposing hidden-coordinate mistakes, and determine conditions under which the bitset-and-rational event sweep extends to arbitrary finite BRC transport fibers with coordinate-margin certificates. Track full integer bit complexity and initial spectrum-reduction cost.
