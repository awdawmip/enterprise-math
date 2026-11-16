# R762CJ — Constructive K4 signed-area orbits and optimal named-state repair

**Scientific lineage:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Continues R762CI at [Draft PR #2578](https://github.com/awdawmip/enterprise-math/pull/2578), immutable source commit \`1bfacabec94f2e6740948b4cdb6072e017aa17ff\`, theorem \`R762CI_K4_HIDDEN_SYMMETRY_THEOREM.md\`. Original frozen scientific axiom: [P000 at a72226e](https://github.com/awdawmip/enterprise-math/blob/a72226e2430ffa4786321ac86e7f0c599d5f0389/p000_reality_foundation.json). Current behavioral protocols read separately.

**Status:** exact combinatorial theorem within the *conditional* K4/X6 pair-area observer; author-side Python exhaustive verification at q=2,...,16; independent mathematical review \`NOT_REVIEWED\`. The existing six signed X6 spatial axes, time type, triadic arity, native 120-degree \`PERP_E\`, BRC path branches and P000 are retained. No new native \`TRIADIC_CLOSURE_E\` event has been admitted.

## 1. Problem and representation

R762CI labels three opposite-edge oriented loop-history residuals
\[
z=(C_{01,23},C_{02,13},C_{03,12})\pmod q\in Z_q=(\mathbb Z/q\mathbb Z)^3,\quad q\ge 2.
\]
The induced vertex-relabeling image of \(S_4\) is \(D_3\), the 24 even-sign monomial matrices on three coordinates. The full \(S_4\)-invariant observer is the orbit \(O(z)=D_3z\); named pair/Port queries may distinguish states inside one orbit.

Define the **folded value**
\[
a_q(x)=\min\{x,q-x\}\quad(0\le x<q),\qquad 0\le a_q(x)\le\lfloor q/2\rfloor.
\]
A folded value is self-inverse iff \(2a=0\pmod q\): always \(a=0\), also \(a=q/2\) for even q. For \(z\), sort its three folded values into \(a\le b\le c\). If all three are non-self-inverse, define \(\epsilon(z)\in\{0,1\}\) as the parity of the number of coordinates represented by the negative residue \(-a_q(z_i)\) rather than the positive residue \(+a_q(z_i)\). Otherwise set \(\epsilon(z)=*\).

## 2. Constructive complete invariant (Theorem A)

Two vectors \(z,z'\in Z_q\) belong to the same \(D_3\)-orbit **if and only if**
\[
\boxed{(a,b,c;\epsilon)(z)=(a,b,c;\epsilon)(z').}
\]

**Proof.** Permutations preserve the multiset of folded residues, and an even number of sign changes preserves the sign parity when every entry has two distinct signs. Conversely, choose a permutation matching the sorted folded values. If all three are non-self-inverse, vectors with equal sign parity differ by an even number of sign changes; such a diagonal sign matrix is in \(D_3\). If a self-inverse coordinate is present, reversing it leaves the actual residue unchanged. This invisible flip adjusts the parity of the signed matrix, so *every* assignment of signs to the other entries is related by an even-sign matrix. Thus the displayed invariant distinguishes precisely the orbits. QED.

Write \(m=\lfloor q/2\rfloor\), \(t=m+1\) for all folded choices and \(n=\lfloor(q-1)/2\rfloor\) for non-self-inverse folded choices. The number of multisets of three folded choices is \(\binom{t+2}{3}\). Exactly \(\binom{n+2}{3}\) such multisets contain no self-inverse coordinate and therefore split into two parity classes. Here \(\binom{u}{3}=0\) for \(u<3\). Consequently
\[
\boxed{A(q)=\binom{\lfloor q/2\rfloor+3}{3}+
               \binom{\lfloor(q-1)/2\rfloor+2}{3}.}
\]
For odd q this is \((q+1)(q+2)(q+3)/24\). For even q this is \((q^3+6q^2+20q+24)/24\). This gives a direct combinatorial proof of the R762CI Burnside count and an explicit canonical orbit index.

## 3. Exact orbit fibres and optimal repair bits (Theorem B)

For a sorted folded triple \(a\le b\le c\), let \(p=3!/\prod_j m_j!\) be its number of distinct coordinate arrangements, where \(m_j\) are multiplicities of repeated folded values. Let \(s\) count the self-inverse entries, including multiplicity.

* If \(s>0\), there is exactly one orbit with this folded multiset, of size \(p\,2^{3-s}\).
* If \(s=0\), there are exactly two parity orbits, each of size \(4p\).

The formulas follow immediately from Theorem A: each non-self-inverse coordinate has two distinct signed residues, and each self-inverse coordinate has one. Distinct arrangements and sign assignments are disjoint vectors, and the parity classes have equal size when \(s=0\).

Let \(M(q)=\max_z|O(z)|\). Then
\[
\boxed{M(q)=
\begin{cases}
3,&q=2,\\
12,&q=3,4,\\
24,&q\ge5.
\end{cases}}
\]
**Proof of sharpness.** The group has 24 elements, so every orbit has at most 24. At q=2 all coordinates are self-inverse, so the action reduces to permutations of a binary triple; the largest orbit has size 3. At q=3 the only non-self-inverse folded value is 1 and the only self-inverse value is 0; the preceding formula gives maximum 12, achieved at (0,1,1). At q=4, the non-self-inverse folded value is again only 1; the self-inverse choices are 0 and 2. Directly treating s=0,1,2,3 in the displayed formula gives maximum 12, achieved at (0,1,2). For every q>=5, folded values (0,1,2) are distinct, with exactly one self-inverse entry and both 1 and 2 non-self-inverse, so p=6, s=1, and the orbit has size \(6\cdot2^2=24\). QED.

If an observer already knows the invariant orbit \(O(z)\), the minimum *worst-case fixed-length binary repair* allowing exact recovery of the **named** residual \(z\) is therefore
\[
\boxed{R(q)=\lceil\log_2 M(q)\rceil=
\begin{cases}
2,&q=2,\\
4,&q=3,4,\\
5,&q\ge5.
\end{cases}}
\]
The lower bound follows because the largest orbit contains \(M(q)\) states sharing the same observation. The upper bound is constructive: generate its at most 24 distinct group translates, sort them lexicographically, and transmit the state's zero-based rank within that orbit. Thus, despite growing q, **five extra bits always suffice, and for q>=5 are necessary, to restore all three named hidden residuals from their exact S4 orbit label.** This is a finite group-symmetry repair statement, not a promise that the orbit observation itself costs five bits.

## 4. Exact positive N-BRC source-mass preservation (Theorem C)

Continue the R762CI q-slot positive branch model with
\[
f_q(0)=2,\qquad f_q(x)=\binom qx\quad(1\le x<q),\qquad
w_q(z)=\prod_{i=1}^3 f_q(z_i).
\]
For every \(D_3\)-orbit \(O\),
\[
\boxed{W_q(O)=|O|\,\prod_{a\in\text{sorted folded}(z)} f_q(a)\quad(z\in O),}
\qquad \sum_O W_q(O)=2^{3q}.
\]
The weight is invariant under permutations and sign reversal (the binomial symmetry, with \(f_q(0)=2\)). Each orbit's total is its cardinality times the common positive weight; the orbits partition the \(2^{3q}\) labeled B/L branch histories. This is an exact N-BRC **source multiplicity** accounting, not an identification of positive mass with force amplitude or signed cancellation.

The q=3 five orbit masses sorted are \(8,72,108,108,216\), totaling 512. Theorem A permits calculating every orbit and its positive mass without enumerating all \(q^3\) vectors, while the attached checker independently enumerates all vectors for q=2,...,16.

## 5. Native scope, verification, and next falsifiable obligation

The S4 action here is a valid *conditional relabeling operation on the K4 opposite-edge pair-area diagnostic*. If the native future event language contains a fixed named pair/Port query, Theorem B gives a precise, optimal repair interface: retain the orbit label plus rank bits; it recovers the full named z before any event-predicate evaluation. Thus the construction provides a BRC observer-safe completion for **all functions of these three named residues**, regardless of the chosen named queries.

It does not yet certify that this three-coordinate carrier suffices for **all 15 X6 pair areas**, the complete Cell/Link/Port state, or a true \`TRIADIC_CLOSURE_E\` event. The direct native dependency remains: obtain a current, source-backed triadic event-admission predicate and licensed V17/V29/V39 signed Cell/Link/Port transport, then decide which oriented pair coordinates can actually affect a legal future event. A decisive test is to construct two histories with identical STAR observations and identical repaired named hidden z, yet different legal suffix outcomes; such a witness would show additional provenance is required. If none exists under a proved complete event language, formulate the corresponding exact descent certificate.

**Verification:** The companion pure-Python \`R762CJ_K4_ORBIT_REPAIR_VERIFY.py\` implements the 24 vertex-induced signed matrices independently of the folded invariant, enumerates all q^3 states for every q=2,...,16, partitions them into actual orbits and checks signature uniqueness, predicted sizes, exact class counts, maximal fibre sizes and N-BRC positive mass. Results are in \`R762CJ_K4_ORBIT_REPAIR_EVIDENCE.json\`. No randomized sampling, external floating point or formal proof checker is claimed. Proofs above establish all q>=2; Python is author-side finite consistency validation.