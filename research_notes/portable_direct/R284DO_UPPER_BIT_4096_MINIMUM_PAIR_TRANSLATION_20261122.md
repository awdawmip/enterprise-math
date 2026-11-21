# R284DO — 冻结 Port 联合四读数最小间隔的高位翻转与行列式机制

Date: 2026-11-22 (Asia/Shanghai)
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**.
Scope: the frozen auxiliary 34-bit Port observer; this is a finite, source-local theorem, not a native X6 or BRC dynamics theorem.

## 1. Exact frozen input and previous frontier

Immutable source: awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py, Git blob SHA-1 b46e0f682b58e47c27094b4bea6fa4e55119a3ee. The ordered source-word SHA-256 is b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4. There are 65,536 source matrices, modulus P=17,179,869,143, and 64 labeled oriented integer circular arcs.

Write f(i) for the farthest integer distance of source codeword g(i) from the 64 arcs. Source flips R and W correspond to XOR by 1 and 64. The ordered four-read observer is

\[
U(i)=\bigl(f(i),\,f(i\oplus1),\,f(i\oplus64),\,f(i\oplus65)\bigr).
\]

R284DN exactly classified the four-read Chebyshev minimum as 60, with exactly 256 minimizing unordered pairs, described by pair SHA-256 7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a. Here the question is which source bit mutation and exact determinant term generate all those witnesses.

## 2. The upper-source-bit increment

Use the original lower matrix variables \(L=(u_1,a,x,y,u_2,w,b,z,u_3,g,h,r)\), each in \(\{1,2\}\), and four upper binary bits \(\beta_0,\beta_1,\beta_2,\beta_3\). In the frozen determinant:

\[
t=6-a,\quad s=13-b,\quad u=ts-xw,
\]
\[
p_1=su_1+xu_2,\qquad p_2=tu_2+wu_1,
\]
\[
\boxed{q_3(L)=u\,u_3+p_1g+p_2h.}
\]

The determinant's dependence on its fourth upper bit is exactly \(-\beta_3 q_3(L)\). Therefore, if a source index \(i\) has fourth upper bit \(\beta_3=0\) and \(j=i\oplus4096\), then, identically for every possible lower matrix,

\[
\boxed{g(j)-g(i)\equiv-q_3(L_i)\pmod P.}
\]

This is a symbolic, all-source algebraic identity derived directly from the pinned det function. The lower-bit flips R and W commute with the upper-bit flip. The coefficient \(q_3\) is independent of \(r\), and its change under \(w\mapsto3-w\) is

\[
\boxed{q_3(T_wL)-q_3(L)=(3-2w)(-xu_3+u_1h).}
\]

This isolates a source-local mechanism rather than treating the observed minimal gap as an accidental equality.

## 3. Exact finite theorem for all 256 minimizing pairs

**Theorem.** Every unordered pair \(\{i,j\}\) at four-read Chebyshev distance 60 in the frozen 65,536-state population has \(i\oplus j=4096\). Taking \(i<j\), the lower matrices coincide, \(\beta_3(i)=0,\beta_3(j)=1\), and for the original pair and each of its four R/W translates indexed by \(v\in\{0,1,64,65\}\):

1. \(g(j\oplus v)-g(i\oplus v)\equiv-q_3(L_{i\oplus v})\pmod P\).
2. Both translated codewords have the same **unique** maximizing arc label; consequently, the local integer-distance comparison can be made on one identical active arc.
3. The observed absolute scalar change satisfies
   \[
   \boxed{|f(j\oplus v)-f(i\oplus v)|=q_3(L_{i\oplus v})\in\{59,60\}.}
   \]

For the 256 base pairs (before translating), the ordered two-coefficient histogram \((q_3(L_i),q_3(T_wL_i))\) is

| Coefficient pair | Number of base minimizing pairs |
|---|---:|
| (60,60) | 128 |
| (60,59) | 64 |
| (59,60) | 64 |

Since R leaves \(q_3\) unchanged, the four-coordinate absolute gap patterns in R284DN follow immediately:

\[
(60,60,60,60):128,\quad
(60,60,59,59):64,\quad
(59,59,60,60):64.
\]

In all 1,024 pair-plus-translate comparisons, the common unique farthest-arc labels have histogram:
\(21:180,\ 32:84,\ 44:148,\ 45:76,\ 55:256,\ 56:172,\ 63:108\).

The signed scalar changes \(f(j\oplus v)-f(i\oplus v)\) and coefficients have frequency:
\((59,-59):256,\ (60,-60):356,\ (60,+60):412\).

**Proof.** The \(-q_3\) increment and \(r,w\) dependence are obtained algebraically by isolating \(\beta_3\) in the source determinant polynomial; no finite search is needed for those identities. For the exhaustive classification of the **minimizing population**, the R284DO checker regenerates the original 65,536 distinct word residues and verifies their ordered SHA-256, calculates all 4,194,304 point–arc distances, forms the 65,536 four-read signatures, and exhaustively sweeps pairs with first-coordinate gap at most 60. A pair of four-read Chebyshev distance at most 60 must be in that sweep. Exactly 256 pairs attain 60, and their exact 256-pair SHA-256 equals R284DN's published value.

For each of those 256 pairs and each of the four translations, the checker evaluates \(q_3\) from the original source indices, verifies the modular word-difference formula, obtains all 64 arc distances to verify the uniqueness and identity of the winning label on both sides, and checks the integer distance-gap equation. It checks 1,024 such translated pair records, yielding the coefficient, label and signed-gap counts above. These exhaustive calculations prove the finite theorem. In particular, equality of winning arc labels alone is not substituted for the integer-distance check: the latter is explicitly verified on every witness. QED.

The last statement is **a complete structural explanation of the already classified minimum-pair family**. It is not a proof that every possible upper-bit flip with \(q_3\in\{59,60\}\) globally attains the minimum: the active-arc and other two bit-flip conditions must also hold.

## 4. Reproduction, preservation and cost

Scientific files in this directory:
- R284DO_upper_bit_4096_nearest_mechanism_checker.py — independent standard-library integer verifier using the already published R284DM frozen-source helper.
- R284DO_upper_bit_4096_nearest_mechanism_certificate.json — 256-pair digest agreement, 1,024 actual translated comparisons, coefficient/arc-label/signed-gap histograms.

Full frozen-residue digest and R284DN minimum-pair digest are asserted. The verification uses exact unbounded integers; no floating point or numeric fitting. Author-controlled exact finite certificate; independent mathematical review **NOT_REVIEWED**. The 256-pair classification is the required finite verification part, while the determinant coefficient identity is symbolic and holds throughout the source family.

## 5. Next scientific unit and attribution

Seek algebraic inequalities characterizing precisely which upper-bit flips with small \(q_3\) retain a common active farthest arc under both R and W. Such an inequality test might predict the minimum gap without first enumerating all 65,536 farthest-distance values. Compare the full costs of constructing source matrices, generating the candidate family, checking arc-envelope events and reconstructing witnesses. A second useful direction is to test whether the observed seven active labels admit a compact interval rule.

This is independent portable TASK research, preserving historic earlier contributions without impersonating any existing authenticated identity. No formal Task/CLAIM, Result/Review or current native Researcher capability is asserted. Owner inventory request r1-20261122-0100-owner-check-v1 failed with SOURCE_TREE_TRUNCATED; no protected task was taken. Activity-source linkage remains pending legitimate original-session permission and Source CAS.
