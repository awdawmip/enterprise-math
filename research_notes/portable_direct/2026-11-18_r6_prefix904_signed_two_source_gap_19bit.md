# PREFIX-904 — Uniform signed two-source gaps and exact non-overlapping 19-bit collision coverage

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6.
Scope: independent portable-direct, named-source two-port BRC auxiliary observer.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unaltered).
Predecessors: PREFIX-897/900/901/902 (exact old union), PREFIX-903 (dyadic-gap theorem).
Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / INDEPENDENT_INTEGER_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Current shared-X6 CLAIM: not asserted; real owner/registration is determined separately by control readback.

## 1. Exact observation model

Set p=32, N=2^32 and Q={262145,262147,...,524287}, with |Q|=131072.
The full legal trajectory identity is the directed pair with named source:
Z_x=(x,x) or F^i_x=(x,x XOR 2^i), 0<=x<N, 0<=i<32.
For odd a,b in Q, define Phi_(a,b)(u,v)=(u mod a,v mod b).
Distinct names and provenance are retained before observation.

## 2. Constructive signed-two-power collision theorem

**Theorem 904-A.** Let a,b belong to Q, a>b, and suppose
\[
 a-b=2^i+2^j\quad\text{or}\quad a-b=2^i-2^j,
 \qquad 1\le j<i\le17.
\]
Then two different legal named XOR trajectories have identical
Phi_(a,b) observations. The same holds when b>a by swapping the two ports
and reversing the directed trajectories.

**Proof.** Write h=2^j, H=2^i and m=2h. Since j<i, m<=H.
We explicitly build two flips with sources i and j.

Case \`a-b=H+h\`: set x=(h-(a mod m)) mod m and y=x+a.
Then 0<=x<m<=H, so bit i of x is 0 and x XOR H=x+H.
Also y mod m=h, so bit j of y is 1 and y XOR h=y-h.
Thus
\[
 F_x^i=(x,x+H),\qquad F_y^j=(y,y-h).
\]
Their first endpoints differ by y-x=a, while their second endpoints
differ by (y-h)-(x+H)=a-h-H=b. Hence both observed residues agree.

Case \`a-b=H-h\`: set x=(-a) mod m, y=x+a.
Again 0<=x<m<=H and x XOR H=x+H. This time y mod m=0,
so bit j of y is 0 and y XOR h=y+h. Consequently
\[
 F_x^i=(x,x+H),\qquad F_y^j=(y,y+h)
\]
have starting difference a and ending difference
(y+h)-(x+H)=a+h-H=b.

Every endpoint lies in [0,N): x<m<=2^17, y<=524287+x,
and the flip endpoints add at most 2^17. Distinct starting
points x and y, and distinct source labels i and j,
give distinct named directed trajectories. Reversing both
trajectories, with labels preserved, and swapping the observer
ports proves the case b>a. QED.

This statement uses only exact integer residues and XOR. The
well-defined term \`same observations\` concerns the two-port
auxiliary observer; it is not an identification of two native
six-axis Heartbeat World states.

## 3. Complete non-dyadic gap census and de-duplication

Let G be the **set of distinct positive differences**
d=2^i+2^j or 2^i-2^j with 1<=j<i<=17, after removing
the power-of-two gaps already counted in PREFIX-903.
The exact generated set has |G|=241. Different representations
of the same d count only once. For each d, there are
131072-d/2 pairs (a,b) in Q^2 satisfying a-b=d.
The theorem proves a collision in each, and port reversal
provides a disjoint corresponding pair with b-a=d.

E is precisely the previous four-family sufficient collision
set from PREFIX-897:
\[
 ab<33N\ \lor\ a\in U\ \lor\ b\in U\
 \lor\operatorname{lcm}(a,b)<N\
 \lor 33\lceil N/a\rceil>b\
 \lor 33\lceil N/b\rceil>a,
\]
where |U|=552 and the source code reproduces U's exact
16 named rows, two 256-member panels and 24 axis moduli
(their disjoint union, by the explicit membership test).
P is the 192 distinct prefix rows
\[
 P=\{510001+194j,510003+194j,510005+194j:\ 0\le j<64\}.
\]
The PREFIX-902 certified set is E union (P×Q) union (Q×P),
and the PREFIX-903 improvement additionally includes every
dyadic-gap pair. Since G excludes dyadic differences,
the newly counted G-pairs are disjoint from that last added family.

The exact census of **a>b** pairs for d in G is:

| Category | Count |
|---|---:|
| All G-pairs | 27,820,024 |
| Already in E | 12,326,831 |
| Touching a P row/column | 68,660 |
| In E and touching P | 580 |
| Already certified by PREFIX-902 | 12,394,911 |
| **New relative to PREFIX-903** | **15,425,113** |

Each count is over distinct ordered parameters (a,b).
The inclusion-exclusion identity is
12,326,831+68,660-580=12,394,911, so 27,820,024-12,394,911
=15,425,113 new increasing pairs. Reversal doubles the new count:

\[
 \Delta_{904}=2(15,425,113)=\boxed{30,850,226}.
\]
Thus relative to the verified predecessor's explicit union,
\[
 |C_{904}|=7,617,211,750+30,850,226
          =\boxed{7,648,061,976}.
\]
The explicit union's complement in Q² has
\[
 131072^2-7,648,061,976=\boxed{9,531,807,208}
\]
ordered modulus pairs not yet covered by this family of certificates.
This complement is the next search domain, not a list of injective pairs.

**Direct previously uncounted witness:** for a=376495, b=376489,
i=2, j=1, x=3 and y=376498, the named flips
F^2_3=(3,7) and F^1_376498=(376498,376496) satisfy
\[
 376498-3=376495=a,\qquad 376496-7=376489=b.
\]
Consequently both observed residues are identical, and neither
parameter pair lies in E or touches P or has dyadic gap.

## 4. Executed verification and reproduction

The preserved standard-library Python program
\`PREFIX904_R6_TWO_SOURCE_GAP_CENSUS.py\` enumerates every
positive pair across all 241 distinct gap values, constructs
its actual named-XOR witness, and asserts every XOR and modular
equality before counting exact E/P membership. There is no
sampling within the declared gap family.

\`PREFIX904_R6_TWO_SOURCE_GAP_RESULTS.json\` saves all 241
per-gap counts, the full summary, exact input pin and one
concrete new witness. Its 241 rows were independently recounted
by a separate NumPy/int64 vectorized implementation, checking
the six class counts for every d. The independent local test
reported \`INDEPENDENT_EXACT_VECTOR_RECOUNT_PASS 241 30850226 7648061976\`.
A separate V8 JavaScript integer implementation reproduced the
same aggregate totals and emitted the published JSON.

The auxiliary verifier source
\`PREFIX904_R6_INDEPENDENT_NUMPY_CHECK.py\` is retained for reruns.
All compared integers fit signed int64; no floating approximations
were used. The scientific proof is elementary and complete;
the exact 19-bit union number additionally uses the two declared
finite checks and predecessor PREFIX-903 exact-union input.

## 5. Retained mother objective and next discriminating step

The full 19-bit injectivity question remains open:
\[
 B_{\rm fix,odd}(32)\in\{19,20\}.
\]
The next useful test is a larger *uniform* difference family
or a bit-window/carry argument that handles gaps with three
or more binary runs. Alternatively, run the exact two-flip
checker only on the complement of this union and preserve a
genuine injective witness if encountered.

A task-specific authenticated CLAIM, formal Result/Review and
independent acceptance must be processed under their current
separate contracts. Existing P000/native-six-axis inputs,
named-source identity and the frozen science pin are preserved.
