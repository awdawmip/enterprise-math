# R741 — X6 edge-current fibers and native-loop ordering residuals

Date: 2026-11-12 Asia/Shanghai. Author-side exact finite combinatorial result.
Parent line: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen science:
awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Direct predecessor: R740 PR #2142, commit ad5d6df690b9f646f98e3c462b3aad931a440551.

## I. Carrier, observer, and four-axis theorem

Let C be a chosen Cell anchor in the P000 native affine X6 torsor. Choose
four distinct native axes, keep all eight signed primitive step tokens
+e_0,-e_0,...,+e_3,-e_3, and enumerate their 8! rooted closed orders.
Each word is a separately counted positive BRC source branch. Nonbacktracking
(NB) means no two consecutive steps are inverse primitive steps.

For the canonical oriented coordinate edge (u,i), where u is its lower
i-coordinate endpoint, define j_w(u,i) as positive traversals minus negative
traversals. This is an integer *coordinate path observer*, different from
positive BRC branch mass and not automatically the native V39 network j.
The coordinate anchor is not a universal origin.

**Exact finite theorem.** The full 40,320-word family has 14,449 different
j values, with fiber histogram
{1:13056, 2:384, 14:960, 160:48, 5376:1}.
Its NB subset has 13,824 words, 13,440 currents, with fiber histogram
{1:13056, 2:384}. Precisely 192 of the double fibers have four nonzero
oriented edges and 192 have eight. All 1,536 six-edge NB currents and
11,520 remaining eight-edge NB currents are singleton.

The BRC observer (j,Q) has the same 384 double fibers; Q gives the first
sign on each selected axis. With R738's orientation-parity bit epsilon,
(j,Q,epsilon) has 13,632 fibers: 13,440 singletons and 192 doubles.
The pair (j,first signed primitive step) is injective on NB. Every
two-history NB j fiber has two *different first steps*. Its fiber-wise
root-edge choice therefore supplies an S6-equivariant two-element
selector; one bit of residual information is both necessary and sufficient
in the worst case. Under the uniform NB source counting measure,
H(Path | j)=(384*2)/13824=1/18 bit.

**Proof of |NB|.** Inclusion-exclusion over the four forbidden adjacent
inverse pairs gives
sum_{k=0}^4 (-1)^k binom(4,k) 2^k (8-k)! = 13,824.

**Proof of the remaining exact finite assertions.** The accompanying
deterministic Python standard-library checker enumerates *every*
permutation of eight distinct signed tokens exactly once. For each word,
it starts from the anchor, accumulates signed lower-endpoint edge currents,
removes zero entries, tests adjacency, and forms dictionaries keyed by
j, (j,Q), (j,Q,epsilon), and (j,first step). The script asserts each
histogram and injectivity. It independently constructs all 40,320 words
as 2,520 multiset occurrence patterns times 16 first-sign choices,
so the complete domain is checked by two different parameterizations.
For each of 40,320 paths it also checks the five adjacent S6 label
generators (201,600 exact covariance tests). All operations are finite
integer equality tests. This establishes the asserted results for the
declared finite family.

NB support/fiber table:

| Nonzero coordinate edges | Fiber size | Number of current classes |
|---:|---:|---:|
| 4 | 2 | 192 |
| 6 | 1 | 1,536 |
| 8 | 1 | 11,520 |
| 8 | 2 | 192 |

## II. Six-axis three-square order theorem

In the chosen X6 Cell chart, define based four-step coordinate squares

A=(+0,+1,-0,-1),
B=(+2,+3,-2,-3),
C'=(+4,+5,-4,-5).

Every permutation of the three squares is a twelve-step NB closed path.
These six different BRC histories have exactly the same 12-edge oriented
coordinate current j*=j_A+j_B+j_C', first-sign vector Q=(+,+,+,+,+,+),
coordinate circulation J, and first-axis occurrence parity epsilon=+1.
Changing the order of two two-axis blocks changes inversion parity by
(-1)^(2*2)=+1. Thus (j,Q,J,epsilon) has a six-element observation fiber;
the worst-case extra cost to recover complete history is ceil(log2 6)=3 bits.

More generally k independently rooted squares on disjoint axis pairs in
a 2k-axis coordinate carrier give k! distinct NB orderings with one j.
The k=3 construction uses all six native X6 axes. These are composite
coordinate loops, not purported four-/six-force primitive stable events.

## III. A typed V39 network/holonomy instance

The current project record
research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md
was read from current Source main as **method comparison**, not silently
repinned as scientific input. Its declared port (j,h) carries integer
network cycle-chain current j in ker(partial) and based active-frame S3
transport h. Its safe operation language L_JH queries this pair, composes
based loops, and reads deterministic functions thereof.

Take a finite based graph consisting of the union of the three coordinate
squares, with network edges identified with their native oriented coordinate
edges. Then the induced incidence chain map A is the identity on the
selected edges, so the *abstract network* j_V39 = A j_X6 exactly for
these words. On a different graph map A, j_X6 is recoverable from j_V39
on a declared word population W **if and only if**
A j(w)=A j(w') implies j(w)=j(w') for every w,w' in W.
This is precisely fiber constancy of the desired reconstruction observer.

Assign the three rooted loop generator holonomies to S3 transpositions:
h(A)=(01), h(B)=(12), h(C')=(02). The three-square wedge has a
free based-loop group on these generators, so the assignment defines a
homomorphism to S3. Composition uses the stated V39 convention
h(gamma;r)=h(r) o h(gamma). Explicit results (permutations as image tuples):

| Loop order | S3 transport h |
|---|---|
| ABC' | (0,2,1) |
| AC'B | (2,1,0) |
| BAC' | (1,0,2) |
| BC'A | (2,1,0) |
| C'AB | (1,0,2) |
| C'BA | (0,2,1) |

There are exactly three transports, each attained twice. Thus (j,h)
has three double history fibers, and another binary selector restores
the complete history in this instance. For ANY three fixed S3 packet
transports, the six order products have the SAME sign/parity (the product
of the three signs), hence at most three different S3 values. At least
two of the six histories must share (j,h). This parity argument is a
general algebraic obstruction within this six-order source family.

V39's coarsest exact quotient for L_JH remains valid: complete event-order
queries were explicitly outside that future-operation language. The
present result pinpoints the minimal added provenance when the language
does include ordered-loop observations.

## IV. Source and continuation

Run R741_X6_LOOP_ORDER_VERIFY.py; its exact integer result marker is
R741_X6_LOOP_ORDER_BRC_EXACT_PASS. The companion JSON lists all
histograms, the six S3 products, the common coordinate current and source
pin. Full local calculations used 40,320 signed permutations, an independent
40,320-word occurrence/sign construction, and 201,600 S6 current transport
checks.

The typed network/S3 construction is a mathematical realization of the
declared loop algebra. A native physical TRIADIC_CLOSURE_E Cell/Link/Port
event, its actual V29 PASS update and actual V17/V39 frame transport
remain the exact outstanding correspondence test. The next unit must
extract one such legal event from the frozen scientific source, supply its
edge incidence map and check commute of the native update with the
typed j and h maps. P000 and the task's science pin remain unchanged.
This author-side report is not a native Result/Driver review.
