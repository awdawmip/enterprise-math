# R762CI — K4 opposite-edge provenance: signed symmetry and exact N-BRC orbit theorem

**Lineage:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Continues R762CH, [PR #2575](https://github.com/awdawmip/enterprise-math/pull/2575), immutable reference 5ab7ba9db4a3c32744f3679a32fb738ecabd85fa. **Scientific input is frozen:** P000@a72226e2430ffa4786321ac86e7f0c599d5f0389; native six signed primitive X6 axes, separate time and triadic arity. **Status:** exact conditional algebraic observer theorem, author-tested; independent review NOT_REVIEWED. This is not yet an authenticated TRIADIC_CLOSURE_E event license.

## 1. Exact input and new question

R762CH establishes the K4/FCC four-STAR diagnostic atlas with axes labeled by the six *unoriented edge names* 01,02,03,12,13,23 (these are six different X6 axis labels, not a new spatial plane). The four triples expose exactly 12 of the 15 ordered closed-path pair-area residues. The three dormant opposite-edge pair coordinates are

\[
z=(z_0,z_1,z_2)=(C_{01,23},C_{02,13},C_{03,12})\pmod q,\quad q\ge2.
\]

Here C_{a,b}=-C_{b,a} is the alternating **path provenance** from R762CH, not a physical force amplitude. On its common Cell/time/signed-step-histogram source fibre, q individually labeled B/L loop slots at each pair realize the full set of q^3 hidden residue vectors. Its positive integer N-BRC weight is

\[
w_q(z)=\prod_{i=0}^2 f_q(z_i),\quad
f_q(0)=2,\quad f_q(a)=\binom qa\;(1\le a<q).
\]

We characterize the exact S4 label-relabeling symmetry and the strongest quotient available when future observations are genuinely S4-invariant.

## 2. Signed K4 action (theorem and proof)

Let S4 permute vertices 0,1,2,3 and thereby permute the six *unoriented* K4 edge labels. For each ordered pair of distinct edge axes, the induced map sends C_{a,b} to C_{g(a),g(b)}, with a minus sign if the result must be reversed to the displayed opposite-edge pair order.

**Theorem A.** On the three hidden residues, the *integral* representation of S4 is faithful and consists of all 24 signed permutation matrices having an even number of negative entries (D3, isomorphic to S4). The unsigned permutation action is S3 and its kernel is V4. Modulo q≥3 the signed action is faithful; modulo 2, negation is invisible and the action factors through S3.

**Proof.** The three coordinates correspond to the three partitions of four vertices into two unordered disjoint edges, so S4 acts transitively on them and maps surjectively to S3. Its kernel consists of the identity and the three double transpositions V4. Directly swapping the vertices in a double transposition swaps the order within *exactly two* of the three displayed opposite-edge pairs, producing two negative signs. An adjacent vertex transposition also induces an even sign pattern and swaps two coordinate positions. Because adjacent transpositions generate S4, all image matrices have even sign parity. No nonidentity element acts trivially on all three oriented pairs over Z: an element outside V4 moves a coordinate, and a nonidentity V4 element reverses two signs. Hence 24 distinct integral matrices occur, exactly the 3!×4 possible even-sign monomial matrices. Reduction mod q≥3 retains +1≠-1; reduction mod 2 erases every sign. QED.

**Theorem B (S4-invariant pair-probe support).** S4 has exactly two orbits on the 15 unordered pairs of distinct edge axes: 12 incident-edge pairs and 3 opposite-edge pairs. Therefore an S4-invariant set of named pair probes is one of ∅, the incident 12, the opposite 3, or all 15. An interface already containing the four STAR triples that adds *one* opposite-edge probe must add all three if the set of probes must be closed under S4 relabeling.

**Proof.** Two distinct K4 edges either intersect at one vertex or are disjoint. S4 acts transitively on the four vertices and on all partitions into disjoint edge pairs. There are 4·binom(3,2)=12 incident pairs and binom(6,2)−12=3 disjoint pairs. An invariant subset is a union of these two orbits. QED.

Theorems A/B concern **label symmetries and allowed diagnostic interfaces**, not assertions that corresponding frame changes or probes are licensed in the native physical event language.

## 3. Complete orbit census for every modulus

Define g_q=gcd(2,q), exactly the number of solutions of 2x=0 mod q.

**Theorem C (exact S4-invariant observer cardinality).** The number of S4-orbits of hidden provenance vectors z in (Z/qZ)^3 is

\[
\boxed{A(q)=\frac{q^3+6q^2+8q+3qg_q^2+6g_q^2}{24}}
\]

and hence

\[
A(q)=
\begin{cases}
(q+1)(q+2)(q+3)/24,&q\ \mathrm{odd},\\
(q^3+6q^2+20q+24)/24,&q\ \mathrm{even}.
\end{cases}
\]

An orbit-valued invariant observer requires exactly ceil(log_2 A(q)) bits in an optimal fixed-length class code. The **named** three-residue observer requires ceil(log_2 q^3) bits instead. For q=2,3,4 the orbit counts are 4,5,11, versus named counts 8,27,64.

**Proof.** Apply Burnside's lemma to the 24 even-sign permutation matrices. For the identity underlying permutation, the identity sign pattern fixes q^3 vectors; each of the three two-negative patterns fixes q·g_q^2, totaling q^3+3qg_q^2. For the three transpositions, each has two sign patterns with positive 2-cycle sign product (each fixes q^2 vectors), and two with negative 2-cycle sign product (each fixes g_q^2 vectors); their total is 6q^2+6g_q^2. For the two 3-cycles, all four even-sign choices per cycle fix q vectors, giving 8q. Divide the sum by 24. The two closed forms substitute g_q=1 for odd q and 2 for even q. Distinct orbits yield different invariant class values and a class index attains the fixed-length information lower bound. QED.

## 4. Exact positive N-BRC pushforward and unsafe named collapse

**Theorem D (orbit mass).** The above labeled-square-loop N-BRC positive source weight is constant on signed permutation orbits, and

\[
\boxed{W_q(O)=|O|\cdot w_q(z)\quad(z\in O),\qquad\sum_O W_q(O)=2^{3q}.}
\]

**Proof.** The binomial symmetry f_q(q-a)=f_q(a), including a=0 where q-a is also 0 mod q, implies invariance under sign changes; the product is also coordinate-permutation invariant. Each source history has a unique residue, so summing its positive multiplicity over orbits partitions all 2^{3q} choices. QED.

For q=3 there are five orbit sizes 1,4,4,6,12 and sorted exact masses **8,72,108,108,216**, summing to 512=2^9. Given fixed STAR-visible residues in the independent 15-pair square-slot family, multiply each hidden-orbit mass by the visible N-BRC multiplicity; no source branches are lost.

**Theorem E (named Port/pair guard obstruction).** Quotienting by S4 is safe only when the declared output *and all permitted future operations* descend through this quotient. It fails for fixed named pair queries. At q=3, z=(1,0,0) and z'=(2,0,0) belong to the same orbit: a nontrivial double transposition reverses the first and one zero coordinate. However the named query [z_0+2=0 mod 3] returns true for z and false for z'. Thus a five-class orbit code cannot safely replace all 27 named residual states when the named query is available. QED.

This explicitly separates invariance under **renaming the observer itself** from maintaining named event semantics; BRC observer-safe compression is scoped by the declared operation language.

## 5. Validation, limits, and continuing task

The companion pure-Python verifier enumerates all 24 vertex permutations and 15 axis-pairs, checks the exact D3 image and both pair-label orbits, and independently enumerates all residual vectors and all 24 fixed-point tests for each q=2,...,12. It compares the explicit orbit count with the closed Burnside formula and verifies each N-BRC orbit mass and the total 2^{3q}. The machine-readable JSON records the exact outcomes. The general statements have direct algebraic proofs above; the finite run is an author-side consistency check, not independent review.

**Unresolved native dependency:** read the actual signed Cell/Link/Port admission predicate TRIADIC_CLOSURE_E and the lawful V17/V29/V39 transducer; identify whether S4 means allowed state update, mere chart relabeling, or only comparison of diagnostic frames. Check if even one of the three opposite-edge residues is accessible through a *licensed* named suffix. That result decides whether the conditional A(q) quotient, the 12-pair STAR quotient, or a richer labeled provenance carrier is adequate. The frozen P000 axioms and full X6 spatial semantics are unchanged.