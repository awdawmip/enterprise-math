# R762CB — 729 sign-gate policies, 90 exact return spectra, two-probe identification

Date: 2026-11-16. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Research status: AUTHOR-PROVED CONDITIONAL MODEL / FINITE INTEGER CHECKS PASSED / INDEPENDENT REVIEW NOT_REVIEWED.

## Inputs and model

Frozen scientific inputs and P000 remain unchanged. This result extends R762CA, PR #2551@7530269499c7f799e65cb20b50a0f5c698b4b1c7, using the conditional V17 active-frame connection and the exact R762BV/R762BY based-return formulas. It does not assume a physically licensed native TRIADIC_CLOSURE_E predicate.

Fix a chosen X6 Cell, an equal quantum, three named Ports carrying a directed Link cycle, six distinct axis labels, and a sign word s in {+,-}^3. Occupied axes form an ordered injection a=(a0,a1,a2). A conditional event (p,y) replaces the axis at enabled Port p with one of the three vacant axes; it retains the sign word, Cell, Links, Port identities and event order. A C3-invariant sign-only closure C(s) and a C3-covariant rooted gate g(s,p) are coherent when g(s,p)<=C(s). There are 729 such policies (R762CA). A sign word with C(s)=0 is excluded from legal starting configurations in this candidate model.

For a closed sign word set J(s)={p:g(s,p)=1}, k(s)=|J(s)|. Define N_P(m) as the total number of ordered length-m paths that begin with named axes (1,2,3) and end on the unordered axis triad {1,2,3}, summed over all closed sign words. Counts are nonnegative integers, with path multiplicity. This aggregate based-return observer does not include full branch provenance or final named-Port rotation.

## Theorem A: complete all-length formula

Let n_k(P)=number of closed sign words with exactly k enabled Ports, k=0,1,2,3. Then for every integer m>=0,

\[
N_P(m)=n_0[m=0]+n_1\frac{3^m+3(-1)^m}{4}
+n_2\frac{6^m+4+5(-2)^m}{10}
+n_3\frac{9^m+5\cdot3^m+9(-1)^m+5(-3)^m}{20}.
\]

The fractions are exact integers for all m. Proof: a fixed sign word has a fixed enabled-Port subset J. Relabeling named Ports maps any k-element J to any other k-element J, preserving based-return path counts. B0(m)=[m=0]. For k=1, the one replaceable slot moves on K4 with adjacency eigenvalues 3,-1,-1,-1 and B1(m)=(3^m+3(-1)^m)/4. For k=2, the two replaceable slots give the Johnson graph J(5,2) with spectrum 6,1,-2 of multiplicities 1,4,5 and B2(m)=(6^m+4+5(-2)^m)/10 (R762BY). For k=3, the active-triad based-return spectrum is the R762BV formula B3(m)=(9^m+5*3^m+9*(-1)^m+5*(-3)^m)/20. Summing B_{k(s)}(m) over closed sign words establishes the formula. QED.

## Theorem B: exact 90-class output quotient

The weighted multivariate census polynomial of the 729 coherent policies is

\[
F(u_0,u_1,u_2,u_3)=(1+u_0+u_3)^2(1+u_0^3+3u_1^3+3u_2^3+u_3^3)^2.
\]

An exponent vector is (n0,n1,n2,n3); its coefficient is the number of policies with that vector. Proof: each of the two homogeneous C3 sign orbits is either excluded (1), closed with no allowed Port (u0), or closed with all Ports (u3). Each of the two mixed size-three sign orbits is either excluded (1), or closed with a rooted subset of k enabled Ports (binomial(3,k) choices). All three cyclically rotated sign words share k, contributing u_k^3. Multiplication proves F. Evaluating all u_k=1 gives 3^2*9^2=729.

The polynomial has precisely 90 distinct exponent vectors, by complete exact four-factor expansion. Distinct exponent vectors have distinct all-length N_P because

\[
\begin{pmatrix}N(0)\\N(2)\\N(3)\\N(4)\end{pmatrix}
=
\begin{pmatrix}
1&1&1&1\\0&3&6&9\\0&6&18&36\\0&21&138&369
\end{pmatrix}
\begin{pmatrix}n_0\\n_1\\n_2\\n_3\end{pmatrix},
\qquad \det=324\ne0.
\]

Thus 729 policies yield exactly 90 distinct full sequences (N_P(m))_{m>=0}; the minimal binary index for these *aggregate-spectrum equivalence classes* has ceil(log2 90)=7 bits. Class size -> number of classes is 1->9, 2->18, 4->9, 6->18, 9->6, 12->18, 18->9, 36->3, giving 5,013 unordered policy pairs with the same aggregate return spectrum. These claims are checked by exhaustive integer enumeration of all 729 policies.

## Theorem C: two exact count probes are sufficient and necessary

For this finite policy population the pair (N(0),N(4)) determines the entire all-length return-count sequence. Explicitly,

\[
(N(0),N(4))=(n_0+n_1+n_2+n_3,\ 21n_1+138n_2+369n_3).
\]

Exact expansion of F and enumeration of its 90 exponent vectors show that this pair is injective on that finite support. The companion executable enumerates all 729 policy choices and verifies that the pair attains 90 different values. Separately, N(0) has 9 values and N(4) has 30 values.

Two probes are *minimal among single-exact-length full integer count probes*. For any m>0, policies with one versus two closed homogeneous sign words but no enabled Port have different N(0) and equal N(m)=0. At m=0, one closed homogeneous word with no enabled Port versus one with three enabled Ports both have N(0)=1, but different N(2). Hence no single fixed length can identify all aggregate sequences. QED.

For the positive-sign gate in R762CA, n=(1,3,3,1); its two-probe signature is (8,846). The all-m formula exactly reproduces its m=0..8 counts 8,0,36,108,846,5418,41580,324576,2664810.

## Theorem D: separately typed terminal holonomy

If the observer instead distinguishes the terminal signed named-Port permutation (over the union of all finite return lengths), the fixed-sign holonomy group is S_J, of order k! (R762BY). The number of available terminal signatures is therefore

\[
H_P=\sum_{k=0}^3 n_k k!.
\]

Across the 729 laws H ranges from 0 (no legal sign sector) to 48. The sharp fixed-length index bit counts 0 through 6 have policy frequencies respectively 3,1,24,100,357,221,23. A zero-signature law is counted as zero bits by bookkeeping convention only. This is not a complete branch-history compression statement.

## Evidence, provenance and next question

Companion Python verifier exhausts 729 policies, constructs 90 spectral vectors, verifies the 4x4 determinant and the two-probe injection, checks the return formula against an independent exact finite frame-state DP through m=8 for k=0,1,2,3, and reproduces the terminal signature distribution. The all-m formula follows from the cited exact graph spectra; no extrapolation from 0..8 is used. The JSON evidence contains the integer census. Independent review remains NOT_REVIEWED.

Next: read the actually licensed signed TRIADIC_CLOSURE_E Cell/Port/Link event predicate, and its lawful V17/V29/V39 transducer. Restrict the candidate graph, then recompute the event-admissible spectrum and BRC safe observer quotient. Signs, directed Link state, event provenance and Cell context remain typed; equality of N_P does not grant erasure for observers that access those variables.
