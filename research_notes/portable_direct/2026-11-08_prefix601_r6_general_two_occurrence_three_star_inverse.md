# PREFIX-601-R6 — Universal two-occurrence three-STAR phase inversion theorem

Date: 2026-11-08 (Asia/Shanghai).
Researcher-ID: \`EM-DIRECT-A20D88 / TASK_RESEARCH\` (Source-registered activity \`RA-C08546417E8843F001D2CEC4\`; no CLAIM).
Status: AUTHOR_PROVED / EXACT_FINITE_GENERIC_GRAPH_TESTED / UNREVIEWED / NOT_ADMITTED.
Native frozen seed: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Original source: \`research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py\`, immutable Git blob \`7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41\`.
Prior result: \`2026-11-08_prefix600_r6_phase_matching_sparse_inverse_smith.md\`. This theorem abstracts **only the exact phase graph**, not arbitrary signed BRC rewards, P000 physical claims, or a new native science pin.

## Mother question and construction

PREFIX-600 found a twelve-swap phase involution and a sparse inverse for the original four 3-STAR native graph. Do these facts depend on the particular six absolute axis labels \`1,...,6\` and their original incidence, or solely on the STAR incidence law?

Let \(\mathcal S=(S_a)_{a\in V}\) be any finite family of \(s=|V|\) three-element sets of distinct *positive* labels such that **each label appears in exactly two different STARs**. Repeated pairs of STARs may share different labels; no graph simplicity is assumed. Write \(m\) for the number of distinct labels: \(2m=3s\), hence \(s\) is even. The original frozen BRC \`STARS\` is one such family with \(s=4,m=6\).

Define the \(12s\) signed phases \((a,p,c)\) as follows: \(c=\pm k\) for \(k\in S_a\), and \(p=-\operatorname{sgn}(c)\ell\) for any \(\ell\in S_a\setminus\{|c|\}\). There are two choices of \(p\) for each signed \(c\). Let \(\operatorname{near}(a,c)\) be exactly the two signed alternatives for \(p\), as in PREFIX-565.

Let \(b(a,k)\) be the unique STAR other than \(a\) that also contains absolute label \(k\). Define the three phase successors:
\[
\mathrm{NEXT}(a,p,c)=\Big(
 (a,c,u),\ (b(a,|c|),c,v_1),\
 (b(a,|c|),c,v_2)\Big)
\]
where \(u\) is the unique member of \(\operatorname{near}(a,c)\setminus\{p\}\), while \(v_1,v_2\) are precisely the two members of \(\operatorname{near}(b(a,|c|),c)\). All successors are valid signed phases.

Define \(A_{xy}=\#\{j\in\{0,1,2\}:\mathrm{NEXT}(x)_j=y\}\), let \(S\) be the permutation matrix of successor slot 0, define \(F(a,p,c)=(a,p,c^\star)\), where \(c^\star\) is the other allowed signed component with the same \((a,p)\), and set \(B=S^\mathsf TA-I\).

## Theorem A — symbolic incidence involution, independent of the STAR geometry

The slot-0 permutation \(S\) consists of exactly \(2s\) disjoint six-cycles, so \(\det S=+1\). The involution \(F\) has \(6s\) two-element orbits indexed by \((a,p)\), with signed \(p\) and \(|p|\in S_a\).

**For any phase \(x=(a,p,c)\), the two non-slot-0 successors after reversing slot 0 are precisely the two phase states with fixed \((b(a,|p|),p)\).** Equivalently,
\[
 B_{x,y}=1
 \ \Longleftrightarrow\
 y=(b(a,|p|),p,c')\quad\text{for one of the two allowable }c'.
\tag{A}
\]

Consequently \(B\) is a direct sum of **\(3s\) identical 4-by-4 incidence blocks**
\[
H=\begin{pmatrix}
0&0&1&1\\
0&0&1&1\\
1&1&0&0\\
1&1&0&0
\end{pmatrix},
\]
after simultaneous permutation of rows and columns. The pair-level map is **symbolic and table-free**:
\[
\tau(a,p)=\big(b(a,|p|),p\big).
\tag{B}
\]
It has exactly \(3s=2m\) independent transpositions, one for each signed label \(\pm k\).

**Proof.** Slot 0 sends \((a,p,c)\) to \((a,c,u)\) where \(u\) is the third absolute label in the STAR with sign opposite to \(c\). Tracking any initial signed ordered pair through this deterministic transformation visits the six sign-alternating oriented pairs of the three labels and returns in six steps; since there are 12 signed phase pairs per STAR, there are exactly two such six-cycles per STAR. Now choose \(x=(a,p,c)\); its unique slot-0 predecessor is \((a,u,p)\), with \(u\) the third signed alternative. The cross-STAR slots 1 and 2 out of this predecessor necessarily preserve signed component \(p\) as their new second field, switch to the unique other STAR containing \(|p|\), and choose both signed alternatives there as their third fields. This gives (A) and hence (B) for all allowed incidences without enumerating the individual phases. Swapping to the other STAR with \(|p|\), then again, returns to the source, with no fixed STAR, because every label occurs in exactly two distinct STARs. Every signed label yields one transposition of twin pairs and the indicated four-state H block. QED.

## Theorem B — determinant, exact inverse, and Smith normal form for all such STAR systems

The table-free description immediately gives
\[
 F^2=I,\qquad BF=FB=B,\qquad B^2=2(I+F).
\tag{C}
\]
Each H block has eigenvalues \(2,-2,0,0\); \(I_4+H\) has determinant \(-3\). As \(s\) is even,
\[
\boxed{\det(A)=(-3)^{3s}=3^{3s}\ne0.}
\tag{D}
\]

Moreover \((I+B)(I+B-2F)=3I\) yields
\[
\boxed{3A^{-1}=(I+B-2F)S^\mathsf T \in\mathrm{Mat}_{12s}(\mathbb Z).}
\tag{E}
\]
Every row of \(3A^{-1}\) has **one -2 and three +1**, independent of the STAR incidence or its size. Since the inverse is integral after multiplying by 3 and \(|\det A|=3^{3s}\), all nontrivial Smith invariants must equal 3 and
\[
\boxed{\operatorname{SNF}(A)=\operatorname{diag}(1^{9s},\,3^{3s}).}
\tag{F}
\]
Thus \(\mathrm{rank}_{\mathbb F_3} A=9s\); for every prime \(\ell\ne3\), the matrix is invertible over \(\mathbb F_\ell\). Its inverse has four-sparse rows, which provides an exact, constant-sparsity per-row inverse of the **phase-background adjacency**, not an end-to-end reduction of the native BRC reward language. QED.

For the actual frozen PREFIX-565 native STARs, \(s=4\), recovering PREFIX-600's phase determinant \(3^{12}=531441\), Smith form \(\operatorname{diag}(1^{36},3^{12})\), and 12 phase twin-pair swaps; formula (B) is the requested *direct native symbolic explanation* of those swaps.

## Exact test and limitations

The accompanying standard-library Python certificate generates the signed phase graph from five incidence systems: two STARs sharing three labels (3-parallel-edge cubic multigraph), four STARs of \(K_4\) (isomorphic to the frozen 4-STAR incidence), six STARs of \(K_{3,3}\), six STARs of a triangular prism, and eight STARs of the cube. It checks the complete symbolic (A) correspondence, \(F^2=I\), \(BF=FB=B\), \(B^2=2(I+F)\), fixed-point-free pair swap and their counts; all five systems returned \`ALL_CHECKS_PASS\`. This is an exact finite regression for the general derivation, **not** a substitute for its combinatorial proof and **not** a rerun of all BRC signed-reward and gate rules for changed incidence.

The theorem is an **abstract graph family extending the frozen source's phase formula**. Only its original four-STAR instance belongs to the actual frozen science input; other STAR incidences are new mathematical examples, not declared additional native X6 worlds. In particular the full seven-reward rank 49/50 of PREFIX-600 requires its original frozen gate and reward structure; it is not asserted for arbitrary \(\mathcal S\). Formal CLAIM, Result/Review, Foundation and Working Truth unchanged.

## Next

Study full seven-reward observer kernels under controlled variations of gate-target and incidence. Test whether the unique exceptional phase-background factor 3 induces any independent native BRC congruence or symmetry observation, and measure coefficient/bit growth and full input/output costs before proposing algorithmic complexity improvements.
