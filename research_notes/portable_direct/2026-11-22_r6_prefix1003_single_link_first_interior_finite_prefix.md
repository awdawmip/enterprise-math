# PREFIX-1003 — Native X6 single-Link mask: finite-prefix locality and exact first-interior BRC reduction

Date: 2026-11-22 (+08). Status: AUTHOR_ANALYTIC_PROOF / TYPED_Z2_BRC_COVER_EXACT_CHECKED / NOT_REVIEWED. Independent portable mathematics; no shared Task CLAIM, formal Result, PROGRESS, or independent review is asserted.

## 1. Exact frozen scientific setting

Frozen P000 V5 is \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`. Use the native X6 Cell torsor with *chart-relative* six signed displacement coordinates; the time-step index is a separately typed update count. Retain the Stage46 same-author coherent BRC candidate, not an admitted material dynamics: 12 signed primitive-axis directions, incoming-neighbour port \(h\), outgoing direction \(d\), and local amplitude \(C_{hd}=1/6-\mathbf1_{h=d}\). After travelling \(d\), the next incoming-neighbour port is \(-d\). Start at Cell anchor 0 with incoming-neighbour port \(-e_1\). The amplitude observer retains both terminal Cell displacement and last incoming-neighbour port, sums signed paths within each such fibre, then squares and sums. A positive BRC weight cover alone is not the amplitude observer; the finite phase group is \(\mathbb Z_2\), with sign character \(+1,-1\).

The single native undirected Link \(\{0,e_1\}\) is closed in *both* traversal directions by removing the outgoing branch without degree renormalization. Let \(T\) denote the unrestricted Stage46 transfer and \(T_L\) the absorbed transfer. This continues PREFIX-1002, with the same input and observer.

Define \(s(x)=\sum_{i=1}^6x_i\). Let \(\Psi_{n,k}\) (respectively \(\Psi^L_{n,k}\)) denote the coherent endpoint-and-port amplitude packet at exact step count \(n\) with exactly \(k\) **negative** primitive-axis steps under \(T\) (respectively \(T_L\)). Thus it lies at grade \(s=n-2k\). Let \(P_m=\Psi_{m,0}\), and let \(\tau_{e_1}\) translate the terminal Cell but preserve the named terminal port. All these amplitudes are vectors indexed by \((x,h)\), not aggregated coordinate-only scalars.

## 2. Theorem 1003.1: finite-prefix horizon for any fixed interior grade

For every \(k\ge0\), every length-\(n\) path with exactly \(k\) negative steps that attempts the blocked Link must make **its first such attempt no later than step \(2k+1\)**. More strongly, every attempted traversal of this Link on such a path occurs by step \(2k+1\). Consequently, for all \(n>2k+1\), the masked exact-\(k\)-negative packet is determined by its masked prefix of length \(2k+1\) and the **unrestricted**, source- and port-preserving transfer on the remaining \(n-(2k+1)\) steps, with the remaining negative-step budget tracked.

Proof. Immediately before step \(t+1\), if \(c\) of the first \(t\) movements are negative, then the grade equals \(t-2c\) because each primitive positive (negative) movement changes grade by \(+1\) (\(-1\)). A forbidden \(0\to e_1\) step requires grade zero, so \(t=2c\le2k\), giving step at most \(2k+1\). A forbidden \(e_1\to0\) step requires departure grade one, so \(t=1+2c\); that forbidden step itself is negative, hence \(c\le k-1\), giving step at most \(2k\). The inequality applies to every possible attempt, including an attempt following another forbidden attempt in an unrestricted path. After the horizon there can be no branch deletion in this exact sector. Transfer decomposition at the complete named state and retained count is exact coefficientwise in the BRC \(\mathbb N[\mathbb Z_2]\) phase cover. QED.

This is a **fixed-grade finite-memory statement**, not a claim that the all-grade masked walk is a finite perturbation in time: when \(k\) increases, the required prefix grows.

## 3. Theorem 1003.2: three-packet exact identity at the first interior grade

For all \(n\ge3\),
\[
\boxed{\Psi^L_{n,1}=
\Psi_{n,1}-\frac16\,\tau_{e_1}\Psi_{n-1,1}
+\frac{25}{216}\,\tau_{e_1}P_{n-3}.}
\tag{1}
\]
For \(n=2\) omit the final summand; for \(n=1\), \(\Psi^L_{1,1}=\Psi_{1,1}\). All packets on the right use the same initial incoming-neighbour port \(-e_1\), with their own indicated step counts. This is an **identity of complete terminal Cell-and-port coherent amplitudes**, not merely an equality of norms.

Proof. In a path with one negative step, forbidden attempts are possible only at steps 1, 2, 3 by Theorem 1003.1. At step 1, the forbidden outgoing branch is \(+e_1\), with amplitude \(+1/6\). Its complete continuation after translation by \(e_1\) starts with incoming-neighbour \(-e_1\), the same initial port as the original packet, so its contribution is exactly \((1/6)\tau_{e_1}\Psi_{n-1,1}\). A forbidden step-2 return \(e_1\to0\) can only follow the already deleted first \(+e_1\) step; hence it is already included in this removed family.

Among paths **not previously deleted**, the only forbidden step-3 move is \(0\to e_1\). There must have been one negative step in the first two moves, returning to 0. There are exactly eleven phase-labelled, retained-provenance prefixes:
- \((+e_r,-e_r,+e_1)\) for \(r=2,\ldots,6\), each with signed numerator \(-5\) over \(6^3\);
- \((-e_r,+e_r,+e_1)\) for \(r=2,\ldots,6\), each again with signed numerator \(-5\);
- \((-e_1,+e_1,+e_1)\), with signed numerator \(+25\).
All eleven finish at the **same** \((x=e_1,h=-e_1)\) terminal fibre and have consumed the unique negative step. Their coherent signed numerator is \(5(-5)+5(-5)+25=-25\). They therefore contribute \((-25/216)\tau_{e_1}P_{n-3}\), since their subsequent tail is positive-only. Subtract this from the unrestricted packet after removing the first family, yielding the plus sign in (1). The cancellation is performed only after establishing the common complete fibre. QED.

## 4. Corollary: scalar exact reduction with bounded observer overlaps

Let \(A_n=\Psi_{n,1}\), \(B_n=(1/6)\tau_{e_1}\Psi_{n-1,1}\), and \(D_n=(25/216)\tau_{e_1}P_{n-3}\). For \(n\ge3\), with the usual real inner product over jointly retained \((x,h)\) fibres,
\[
M^L_{n,1}=\|A_n-B_n+D_n\|^2
=\|A_n\|^2+\|B_n\|^2+\|D_n\|^2
-2\langle A_n,B_n\rangle+2\langle A_n,D_n\rangle-2\langle B_n,D_n\rangle.
\tag{2}
\]
The unrestricted norms are available from PREFIX-996–1001. Thus the remaining scalarization task is the **three explicitly identified signed, shift-marked collision overlaps** in (2), not an unbounded set of masked endpoint histories. No unproved reduction of those overlaps to \(A_6(m)\) alone is claimed.

Equation (1) and the prefix horizon are exact BRC-phase-cover identities. The observer permits ordinary rational display only *after* applying the signed \(\mathbb Z_2\) character to phase-labelled branches. No classical \(\pi\), trigonometric rule, matrix exponential, Taylor, Padé, Cayley, or newly calibrated physical heartbeat time enters the result.

## 5. Finite exact verification

A separate typed \(\mathbb N\)-weight / \(\mathbb Z_2\)-phase-cover checker is published as \`PREFIX1003_BRC_PHASE_COVER_CHECK.py\`. It encodes branch identity by ordered signed outgoing port, native Cell, incoming-neighbour port, negative-step count and phase. Local numerator is \((1,0)\) for the \(+1/6\) case, and \((5,1)\) for the \(-5/6\) reversal; it accumulates positive cover coefficients, then applies the sign character **per terminal joint fibre**. It is an independent phase-cover implementation of the already specified Stage46 operator, **not** an invocation of the historical canonical Stage46 core. This accurately states the execution coverage.

All 6 initial coordinates are retained; input is \((0,-e_1)\). For \(n=1,\ldots,8\), unrestricted and one-Link-masked phase-cover recurrences were computed independently, and (1), including boundary cases, agreed **for every nonzero or zero terminal joint fibre**. An independent length-three signed-prefix enumeration verified the eleven histories collapse to signed numerator \(-25\) in one joint fibre. Checks use nonnegative integer cover weights and exact rational observation, no floating equality test.

| n | exact masked first-interior mass \(M^L_{n,1}\) |
|---:|---:|
| 1 | \(5/6\) |
| 2 | \(175/216\) |
| 3 | \(2555/46656\) |
| 4 | \(1945/93312\) |
| 5 | \(5285/419904\) |
| 6 | \(9715/1259712\) |
| 7 | \(1341545/272097792\) |
| 8 | \(259181485/78364164096\) |

Verifier source SHA256 at local execution: \`aa360e39a69638a9b47eff0d75754503c0de8f59e8c5eb3617a8d2a36a46dad9\`. Certificate local SHA256: \`c9c0f073aafdafaf61630f5d8dfc25527570db9e427759618028fe0988ea49c7\`. Exact output is in \`PREFIX1003_R6_EXACT_RESULTS.json\`.

## 6. Next discriminating problem and contribution boundary

Determine whether each of the three marked overlaps in (2) reduces to a finite combination of the already-known six-label collision integers \(A_6(m)\) with polynomial coefficients, or whether a new exact marked-collision family is needed. Test the result at general \(k=2\), where the finite-prefix horizon becomes five steps and the prefix-state residual can grow. Then compare absorption with a declared norm-preserving Link response, preserving the entire port observer.

The result is an analytic consequence of a **candidate** BRC constitutive law. No independent Review, Working Truth/Foundation promotion, or physical material coupling is asserted. Historical scientific provenance: original R6 line Researcher \`EM-DIRECT-FBEA5D\`, Activity \`RA-3FB2D033BE6048D8712FF056\`; this metadata does not authenticate current writer identity or authorize a claim or Activity CAS. Mother objective \`B_fix,odd(32) in {19,20}\` remains open.
