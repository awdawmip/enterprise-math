# R284BM — Exactly which diagonal settings can be frozen for a noisy 3×3 binary star-Port observer?

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_CERTIFICATE_PASSED / NOT_REVIEWED. An independent portable arithmetic observer result continuing **R284BJ** (immutable scientific pin: \`ba9ac42ee03c61e34a057ede0d57561d0c418f6b:research_notes/portable_direct/R284BJ_FINITE_FIELD_INFORMATION_OPTIMAL_PORT_SCALAR_20261120.md\`) and R284BL-FX1 (pinned \`42cd735e6fe3e806079e94616a14e821da4c4d76\`). Account-wide behavior is current, not science-repinned. Not a formal CLAIM, Result or independent review.

## Model and exact research question

For every binary positive matrix \(C\in\{1,2\}^{3\times3}\), set
\[
F_C(d_0,d_1,d_2,z_1,z_2)=
\det(\operatorname{diag}(d_0,d_1,d_2)-C-z_1E_{01}-z_2E_{02}).
\]
Choose one index \(j\in\{0,1,2\}\) and **freeze \(d_j=t\)** to the same prescribed integer for all candidates. The other two diagonal controls and both named directed star-Port strengths are freely set once; the instrument returns exactly one residue \(F_C\bmod p\) for a chosen prime \(p\), corrupted by any integer error \(e\in[-3,3]\) modulo \(p\). Require simultaneous exact recovery of all 512 possible \(C\) by cyclic nearest-center decoding. All arithmetic below is in integers or the specified finite field.

## Theorem BM1 — sharp finite-alphabet frozen-diagonal classification

A choice of prime \(p\) and fixed remaining four control settings achieving worst-case recovery for **all** \(C\) exists **if and only if**
\[
\boxed{\begin{aligned}
j=0 &:~ t\notin\{-1,0,1,2,3,4\},\\
j=1\text{ or }2 &:~ t\notin\{-9,-8,\ldots,7\}.
\end{aligned}}
\]
In particular the smallest nonnegative integer successful freeze is \(t=5\) for root diagonal \(d_0\), and \(t=8\) for either leaf diagonal \(d_1,d_2\). The criterion quantifies over arbitrary primes and arbitrary settings of the four free controls. Existence means at least one fixed setting, not a claim of efficient parameter discovery or general native physical implementation.

### Proof, exact obstruction direction

For a candidate pair \(C\ne C'\), let \(Q=F_C-F_{C'}\), and write \(x\) for the four unfrozen controls. The determinant is affine in \(d_j\) and separately affine in every coordinate of \(x\), hence
\(Q(t,x)=U(x)+tV(x)\), where \(U,V\) are integer multilinear polynomials of the four coordinates. Equality \(Q(t,x)\equiv c\) for all settings \(x\), with integer \(c\in[-6,6]\), is equivalent to equality on all \(2^4=16\) Boolean settings \(x\in\{0,1\}^4\). This equivalence follows from the invertible Boolean evaluation/Möbius coefficient transform, not from sampling intuition.

For each of the \(\binom{512}{2}=130816\) unordered candidate pairs, the exact checker forms the sixteen \(u_k=Q(0,x_k)\) and \(v_k=Q(1,x_k)-Q(0,x_k)\). Requiring \(u_k+tv_k=c\) for all \(k\) reduces to the linear equations
\[
(u_k-u_0)+t(v_k-v_0)=0\quad(0\le k<16).
\]
If every \(v_k-v_0=0\), either this can never be constant or it is constant at every \(t\) with value \(u_0+t v_0\); integer solutions to \(|u_0+tv_0|\le6\) are enumerated without a bounded scan. Otherwise the first nonzero slope uniquely determines a rational \(t\), checked against all sixteen equations. Only integral \(t\) and \(|c|\le6\) are retained. This is a complete exact finite decision procedure over **all integer** frozen values.

Its checked union of obstruction values is precisely the two boxed sets. For root \(j=0\), zero pairs have a difference independent of all four free controls for every \(t\); for each leaf, exactly 256 unordered pairs have such a difference, with ten distinct integer-affine forms \(u_0+tv_0\), explicitly listed in the companion JSON. The exact enumeration uses every binary matrix in lexicographic order and compares two independent 3×3 determinant expansions for the final fixtures. If \(|Q|\le6\) is a fixed integer independent of the free controls, the two radius-three cyclic error balls overlap under every prime modulus, so the claimed uniform recovery is impossible.

### Proof, sufficiency direction

If \(t\) avoids the classified obstruction set, then for every \(C\ne C'\) and every integer \(c\in[-6,6]\), the polynomial \(Q(t,x)-c\) is nonzero over \(\mathbb Z[x]\). Choose a prime \(p\) larger than every absolute coefficient of these finitely many polynomials, larger than seven, and with
\[
p>4\cdot 2\cdot13\binom{512}{2}=13\,604\,864.
\]
Each nonzero polynomial stays nonzero modulo \(p\), and has total degree at most two: the common degree-three term \(d_0d_1d_2\) cancels between candidates; specializing \(d_j=t\) cannot increase degree. The finite-field Schwartz–Zippel bound makes the probability of a specified equation \(Q(t,x)=c\bmod p\) at most \(2/p\) for four independent uniform free controls. A union bound over 13 differences and 130816 pairs gives failure probability below \(1/4\). Therefore a successful one-read setting exists, even for an arbitrarily prescribed allowable integer \(t\). QED (conditional on the exact exhaustive obstruction certificate).

### General non-exhaustive lemma BM2 (n≥3)

For the bounded positive integer family \(C\in\{1,\ldots,H\}^{n\times n}\), write \(N=H^{n^2}\), \(J=\binom N2\), choose integer noise radius \(\delta\), and assume the R284BJ/R284BB nonconstant polynomial completeness. Let \(M=n!(H+2)^n\), and any prime
\[
p>\max\{2M,\ 4(n-1)(4\delta+1)J\}.
\]
For **each selected diagonal index \(j\)** at most \((4\delta+1)J\) values \(t\in\mathbb F_p\) make one of the pairwise difference-minus-error polynomials identically zero after \(d_j=t\). Indeed, each nonzero polynomial \(F_C-F_{C'}-c\), with \(c\in[-2\delta,2\delta]\), has degree at most one in \(d_j\), so at most one specialization can annihilate all its coefficients in the remaining variables. All other frozen values leave a nonzero polynomial of degree at most \(n-1\); randomizing only the other \(2n-2\) controls succeeds for all candidates with probability strictly greater than \(3/4\) by the same union bound. Thus the count of admissible frozen controls is at least \(p-(4\delta+1)J\). This is an existence/counting result; the explicit 3×3 obstruction classification is stronger and is separately certified.

## Concrete deterministic 24-bit certificates

All three witnesses use the prime \(p=13604881\), integer noise radius \(\delta=3\), and the same set of 512 candidates. An entry \((d_0,d_1,d_2;z_1,z_2)\) means all controls are fixed before the unknown matrix is supplied.

| Frozen control | Full setting | Minimum circular center gap |
|---|---|---:|
| \(d_0=5\) | \((5,6533875,4219379;912295,3441724)\) | 644 |
| \(d_1=8\) | \((2134880,8,7707204;8299942,5571858)\) | 7 |
| \(d_2=8\) | \((7506413,9793806,8;7755770,3250345)\) | 7 |

Each has 512 distinct residues and 3584 uniquely decoded radius-three integer-noise outcomes. The independent six-term and Laplace 3×3 determinant formulae agree on all 1536 matrix/fixture evaluations. The checker verifies primality by trial division, all 512 cyclic gaps including wraparound, and a direct table of every noisy residue; the JSON stores the complete summary and SHA256 commitments of lexicographically ordered residue lists. The modulus needs \(\lceil\log_2 p\rceil=24\) transmitted bits, and all four unfrozen settings are at most 24 bits each. This experiment does not optimize modulus or decoding memory.

## Meaning, exact boundary, and next question

R284BH gave a frozen-diagonal non-identifiability family over all strictly positive **rational** matrices. BM1 pinpoints a different behavior for a finite **integer** candidate alphabet: root and leaf diagonals have different precise failure intervals when the allowed measurement noise is ±3. Exact polynomial injectivity and **noise-correctable** injectivity are distinct: for example, leaf \(d_1=5\) can distinguish the 512 response polynomials but has pairs with a free-control-independent difference of only 4, 5 or 6, so no radius-three robust single reading is possible at that freeze.

The determinant/finite-field construction is a typed auxiliary algebraic observer; it does not identify native six-axis space, full BRC state or a three-dimensional slice with a 3×3 matrix. No P000 axiom or frozen original scientific pin changes.

**Unfinished:** classify sharp frozen-diagonal ranges for \(H>2\), general \(n\), and noninteger noise; find near-packing moduli and efficiently decodable single readings; independently audit the 130816-pair enumeration and finite-field transfer. All author-side mathematical claims remain \`NOT_REVIEWED\`.

## Reproduction

Run \`python3 R284BM_frozen_diagonal_binary_checker.py > out.json\`, then compare to the companion \`R284BM_frozen_diagonal_binary_verification.json\`. The code enumerates the *entire* candidate domain, uses exact \`fractions.Fraction\` for isolated exceptions, derives the integer obstruction set without bounding \(t\), and verifies all three modular fixtures and ±3 error cases. A historical Researcher lineage \`EM-DIRECT-E6B1DD\` is retained as provenance; this file itself is not proof of a live native execution capability or CLAIM.
