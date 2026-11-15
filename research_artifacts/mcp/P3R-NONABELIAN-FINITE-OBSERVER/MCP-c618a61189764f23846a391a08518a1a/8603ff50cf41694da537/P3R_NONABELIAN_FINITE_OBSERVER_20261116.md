# P3R finite-field non-Abelian observer — deterministic certificate and typed dependency ledger

Date: 2026-11-16 Asia/Shanghai. Formal task: `P3R-NONABELIAN-FINITE-OBSERVER`, current V2 publication `TP2-5A4F26DCA4706C3B933A`. This is a research tool / concrete worked certificate for the stated dependent cross-check, not a new 3-sphere recognition theorem. Independent mathematical review remains open.

## 1. Finite certificate and exact validation

For a group presentation

\[G=\langle g_1,\ldots,g_n\mid r_1,\ldots,r_m\rangle,\]

fix a prime \(p\) and specify matrices \(A_i\in\mathrm{SL}_2(\mathbb F_p)\). An exact certificate contains integer entries modulo \(p\), relator words written as signed generator indices, and optional words whose image matrices span \(M_2(\mathbb F_p)\). The attached deterministic Python checker:

1. Verifies primality and every matrix determinant equals 1 modulo \(p\).
2. Multiplies each signed relator word in the declared generator order; every relator must evaluate to \(I\). This gives a homomorphism \(G\to\mathrm{SL}_2(\mathbb F_p)\).
3. If any generator image differs from \(I\), the image and hence the presented group are nontrivial. **For a correctly verified finite presentation of a 3-manifold group, this alone certifies nontrivial fundamental group**, so the manifold is not \(S^3\); no geometric characterization or GRH is needed to *check the supplied certificate*.
4. If the supplied image words have vector-space rank four, their matrices span \(M_2(\mathbb F_p)\). Their generated algebra then equals the full matrix algebra; after extending scalars to an algebraic closure, the algebra remains full. Consequently the 2-dimensional representation is **absolutely irreducible**. A rank below four only says this particular span certificate is insufficient; it is not a general reducibility verdict.
5. Optionally enumerates the finite matrix image for small primes and checks the group order, as a reproducibility test only.

The implementation currently supports prime fields \(\mathbb F_p\) exactly, an explicit subfamily of finite fields \(\mathbb F_q\). A full prime-power interface would add an irreducible-polynomial modulus with fixed basis representation and exact polynomial arithmetic; no such extension is claimed here.

## 2. Three exact examples

**Poincaré homology sphere.** Use the known binary icosahedral presentation \(\langle s,t\mid s^3=t^5=(st)^2\rangle\). Over \(\mathbb F_5\), take

\[
S=\begin{pmatrix}0&1\\4&1\end{pmatrix},\qquad
T=\begin{pmatrix}0&4\\1&3\end{pmatrix}.
\]

Direct modular multiplication verifies \(\det S=\det T=1\), \(S^3=T^5=(ST)^2=-I\). The four word images \(I,S,T,ST\) have rank 4 over \(\mathbb F_5\). Complete finite closure of \(\langle S,T\rangle\) has **120** elements, exactly the order of \(\mathrm{SL}_2(\mathbb F_5)\). This is a concrete surjective absolutely irreducible finite-field image of that presentation.

**Ordinary three-sphere.** The empty presentation of \(\pi_1(S^3)=1\) has no nonidentity generator image. The checker reports image order 1, nontrivial=false, span rank 1 for \(\{I\}\).

**Cyclic sanity control outside integral homology-sphere scope.** For \(\langle a\mid a^3\rangle\), use \(A=\mathrm{diag}(2,4)\) over \(\mathbb F_7\). The image has order 3 and is nontrivial, while the tested word-span rank is 2 and does not certify absolute irreducibility. This tests the crucial distinction between **nontrivial finite image** and **absolutely irreducible image** without treating a lens-space-type control as an integral homology 3-sphere.

Exact test output:

| Example | \(p\) | image order | nontrivial | word-span rank | abs. irreducible certified |
|---|---:|---:|---|---:|---|
| Poincaré homology sphere | 5 | 120 | yes | 4 | yes |
| \(S^3\) | 5 | 1 | no | 1 | no |
| cyclic \(\mathbb Z/3\) sanity control | 7 | 3 | yes | 2 | no |

The checker additionally rejects a deliberately altered presentation matrix and a determinant-not-one generator. All arithmetic is modular integer arithmetic; no floating-point approximation or external group package is used.

## 3. Source-audited dependency ledger

| Arrow or inference | Provenance / status | Exact dependency |
|---|---|---|
| Presented group + verified matrices satisfying relators \(\Rightarrow\) group homomorphism into \(\mathrm{SL}_2(\mathbb F_p)\) | Elementary exact algebra; implemented | Unconditional **for the supplied, correct presentation** |
| Nonidentity finite matrix image \(\Rightarrow\) group nontrivial; a correct presentation of \(\pi_1(M)\) then shows \(M\not\cong S^3\) | Group theory | Unconditional **certificate verification**; correctness of manifold-to-presentation input must be established separately |
| Span of image words equals \(M_2(\mathbb F_p)\) \(\Rightarrow\) absolute irreducibility | Finite-dimensional algebra over algebraic closure | Unconditional rank certificate for the given representation |
| Every non-spherical integer homology 3-sphere has irreducible \(\mathrm{SL}_2(\mathbb C)\)-representation | Raphael Zentner, *Integer homology 3-spheres admit irreducible representations in SL(2,C)*, arXiv:1605.08530 (2016; Duke Math. J. 2018) | **Geometrization-dependent general theorem**; not an independent proof of Poincaré |
| Gröbner/representation-variety recognition method from finite presentations | Michael Heusener and Raphael Zentner, *A new algorithm for 3-sphere recognition*, arXiv:1610.04092 (2016) | Its correctness invokes preceding general representation-existence theorem and hence **geometrization** |
| Uniform small/effective finite-field witness-prime bound in a quantitative recognition complexity result | Zentner (2016) cites Kuperberg for coNP claim | **GRH-dependent effective bound**; cannot infer a polynomial-size prime from any single example |
| Existence of an \(\mathbb C\)-point \(\Rightarrow\) a specific small finite-field irreducible image | Requires algebraic integral model and good reduction/witness-prime analysis | **Not furnished by this checker.** A finite witness can be checked exactly once supplied; general extraction, ramification and height/discriminant bounds remain separate obligations |

Primary references: https://arxiv.org/abs/1605.08530 and https://arxiv.org/abs/1610.04092. Background group identification: the binary icosahedral group is the fundamental group of the Poincaré homology sphere and is isomorphic to \(\mathrm{SL}_2(\mathbb F_5)\), with the two-generator presentation above; this is a known, reused fact, not a newly proved topological statement in this test.

## 4. Independent frontier and limitations

The checker establishes a practical exact negative-certificate channel for *presented* groups with an exhibited finite representation. It does not decide whether a general presented group admits such a representation, produce a small prime for all eligible groups, or independently resolve 3-sphere recognition. The next meaningful module is a source-pinned test from a real triangulation to a formally correct finite presentation and matrix certificate, with versioned presentation-construction output. Separately audit the algebraic reduction/specialization and effective GRH prime bounds before any general complexity claim.

The mathematics is deliberately separate from Enterprise Math canonical Result/Driver acceptance and the P000-native geometric program.
