# Independent review of the compressed full Selmer kernel and vertical quotient

Disposition: PAPER_PASS, no must-fix, for the exact primitive-core coordinate reconstruction, compatibility kernel, nonvertical quotient and finite dimension/coverage criteria. The matrices M and K are compatibility forms, not Cassels pairings. This verdict computes no actual matrix rank, rational rank or Sha group and does not promote any earlier pairing PASS to this new tenth object.

Reviewer EM-DVR-BFF6DC, own session MCP-47562f9f432d4978a7bea0dd60ecc4aa and DA-144D0C4639CACEEE75DC. Actual author EM-DVR-F73673, /root/public129_line_reviewer. Primary P11_FULL_SELMER_COMPRESSED_KERNEL_AND_VERTICAL_QUOTIENT_PAPER.md has 14420 bytes, SHA256 286f3e9be9369b1eb14ec6421e28904d5c4262972c530eab8daa57365473286e, Git blob 9a9d7e61ce4584bb8f290f1dda6154004d348415. The 1235-byte freeze has SHA256 fe1c3584fa723ee6214f1e77ce4d0f1ccb67b00dda1a6d2451a014ef88f362d4 and blob e837aac05f1998a410a266f50f0ea6d6ec798fc6. I read the complete frozen paper and handoff, checked their exact pins and preserved copies. This new author object is local pending its actual Source at review time; I do not invent a publication.

This is genuine nonauthor review in directed NONBLIND context. Root authorized a separate bounded full-Selmer/vertical-quotient review contingent on true author freeze; I started only after receiving that completed frozen input, with no requested conclusion. The topic was known before freeze, but I gave no construction, equations, witness, correction or preliminary assessment. My prior independent first-input consumption and fourth-through-ninth reviews are disclosed. They are separate scoped evidence, not approval of the present proof. No code/input/certificate/plan contribution was supplied to the fixed-curve author, and no other actor's identity or authority is adopted.

No scientific program, numerical/symbolic matrix consumer, rank computation, point search, parameter enumeration, factorization routine, new helper calculus or literature search was used. All deductions below are paper checks. Managed Source reads, text copying and byte/SHA/Git-blob custody are administrative only. Original author and previous frozen reviewer files remain unchanged. No Native scientific vote, Task/claim/RA, Working Truth or Foundation change is made.

## 1. Exact dependency strength and primitive support

The first complete parameter-local primary is actual Source270c9c6470db2cb14885f82d1021754f2bf19b23, research_notes/owner_goal_20261016/p11_parametric_local_images/P11_PARAMETRIC_LOCAL_IMAGE_AND_DYADIC_OBSTRUCTION_PAPER.md, 11894 bytes, SHA256 13e6d431795353340280c2f9b14c148e117139c85bbd797bf73336e891d453c6. The eighth complete valuation-four dyadic primary is actual Sourcefe6eb52b197ab7c3f1791fcf9e4a75decc16bc78, research_notes/owner_goal_20261016/p11_complete_dyadic_local_images/P11_MISSING_DYADIC_VALUATION_FOUR_COMPLETE_IMAGE_PAPER.md, 9596 bytes, SHA256 7bef7c3940ba9b2aeb63d1663bf0976c67bca1d4032e150e5ae042d949ba9934. I personally consumed complete managed immutable readbacks of both, verified byte/SHA/blob agreement with the frozen inputs and checked their exact all-place scopes. No generic local-table summary replaces these inputs.

The classical bridge is the previously read exact Stoll 2001 edition, DOI10.4064/aa98-3-4, PDF SHA256 b4854a404601da748a687c64a3d72a36033590a4ba911b7021db53340c5aa9d1: full split-cubic Kummer coordinates, zero convention, homomorphism/kernel, local indices and Proposition 4.2's global Selmer condition. Root order remains (0,P^2,Q^2), and the third class is ab. No Cassels theorem is needed for the new membership/compatibility/quotient proof. The optional final rank inequality has its own inherited genuine-pairing hypothesis.

Primitivity and opposite parity make A=r^2-s^2 positive odd, B=2rs positive even, gcd(A,B)=1, and P=A+B,Q=|A-B| positive coprime odd with distinct roots. The norm identities for P and A-B prove (2/p)=1 at every odd prime of PQ: p cannot divide s, so division by s is legitimate. Thus these primes are exactly in the permitted residue possibilities 1 or 7 modulo 8. This joint parameter fact is essential; a general odd P,Q input cannot use the compression unchanged.

The even member e gives v2(D)=3+v2(e), so the complete first/eighth images cover both primitive cases: valuation at least five if 4|e and valuation four otherwise. J_P,J_Q are disjoint labeled 1-modulo-8 prime supports of P,Q, and T is the odd prime support of D, disjoint from both. Multiplicities do not enter membership valuation bits beyond parity, but actual factorizations and labels remain required provenance. No factorization was performed by a program here.

## 2. Forced first and second coordinates are exact

Start in the full signed S-unit pair carrier with S the prime support of 2PQD. The good-prime theorem justifies this restriction and covers all places outside S. At odd D primes the first coordinate is locally square, so every first D-prime valuation bit vanishes. At PQ primes congruent to 7 modulo 8 the unit-pair image kills both valuation bits. At 2 both complete images force the first valuation bit to vanish, and infinity kills its sign. The only surviving first bits are therefore the positive J_P and J_Q prime products alpha_P,alpha_Q.

At p in J_P the local image is diagonal, so first and second p valuation bits agree. At q in J_Q the second coordinate is locally square, killing its q valuation bit. All other second PQ bits were already removed. At 2, a second 2 bit is free in the higher-valuation vertical image and forbidden in the valuation-four complete image. Hence the necessary global reconstruction is exactly

    a=alpha_P alpha_Q,
    b=alpha_P c,
    c=(-1)^u 2^(epsilon v) product_(ell in T) ell^(z_ell).

There is no optional v coordinate when epsilon=0. The sign u is retained. Distinct signed rational prime squareclasses prove uniqueness: a recovers each alpha bit, and b/alpha_P recovers every remaining c bit. Conversely any such coordinate choice has precisely the eliminated valuation and real-sign properties. It is not an arbitrary local-residue replacement of a global class.

Every prime of J is 1 modulo 8, so the reconstructed a is a Q2 square. In the higher-valuation branch the complete dyadic image allows any second class. In the valuation-four branch the reconstructed b is an odd-unit class, exactly the allowed vertical target. Thus no remaining dyadic unit-character condition is lost. The genuine local first class 5 from the eighth theorem cannot occur as the restriction of this primitive-core global first coordinate, even though positive nontrivial J products can remain distinct global rational squareclasses. Local squareness at 2 does not prove global squareness.

## 3. All remaining local constraints and their matrix entries

At ell in T the first coordinate has zero ell valuation, so its local square condition is exactly chi_ell(alpha_P alpha_Q)=0. At p in J_P, the ratio a/b=alpha_Q/c is a unit after the common alpha_P factors cancel globally. Its character equals chi_p(alpha_Q c), because a quadratic unit character is unchanged by inversion. There is no surviving same-J_P term: those factors canceled, including all of them rather than just p itself. At q in J_Q, b=alpha_P c is a unit and its square condition is exactly chi_q(alpha_P c)=0. These are precisely the three row families in the paper.

All other PQ primes have the complete unrestricted unit-pair image and add no character equation once their valuation bits vanish. The dyadic and real places have just been checked, odd D places are covered by the first row family, and the universal good-prime table handles every remaining prime. Thus the three families are necessary and sufficient for full Selmer membership by Stoll's all-place criterion, not merely necessary linear constraints.

For j in J, chi_j(-1)=chi_j(2)=0 because j=1 modulo 8. The sign and optional 2 bit of c are genuinely free in all remaining equations. For the nonfree vector (z,alpha), L has entries chi_j(ell). Quadratic reciprocity gives chi_ell(j)=chi_j(ell) since j=1 modulo 4, even if ell=3 modulo 4. It also identifies chi_q(p) and chi_p(q) across J_P,J_Q. The cross-only block K=[0 B;B^T 0] is therefore correct; no undefined self-character or dropped same-side coupling is hidden in its zero diagonal blocks.

The first row family becomes L^T alpha=0; the J_P and J_Q families become Lz+Kalpha=0. Their order is exactly the stated M=[0 L^T; L K] on (z,alpha). The explicit unique reconstruction makes F2^(1+epsilon) times ker M isomorphic to the full Selmer group. This coordinate reduction preserves the joint relation between a and b rather than forgetting their common alpha_P factor.

M is symmetric with zero diagonal, hence alternating over F2; its rank is even. The paper's two-by-two nondegenerate-block induction is valid in characteristic two and does not need division by two. This is an alternating compatibility form on the auxiliary coordinate carrier. It is not the elliptic Cassels form and supplies no rational-Kummer radical statement by itself.

## 4. The exact quotient and dimension identities

Let C=ker L^T. A candidate first-coordinate vector alpha lifts to a full class exactly when alpha is in C and Kalpha is in im L. For the ambient nondegenerate dot product, im L=C^perp: inclusion follows from L^T beta=0 and dimensions agree. Thus the lift condition is exactly beta^T Kalpha=0 for every beta in C, namely alpha in the radical A0 of the restricted compatibility form K|C.

Every alpha in this radical has some z with Lz=Kalpha. Reconstruction then gives an actual Selmer class, because all-place membership was proved in both directions first. Its fiber differs by ker L together with the free sign/2 bits. At alpha=0 these are exactly the vertical classes V. Therefore projection to alpha proves the exact sequence 0 to V to Sel2 to A0 to 0, without a preferred splitting or any rational-point claim.

Writing rho=rank L and sigma=rank(K|C), dim C=m-rho and dim A0=m-rho-sigma. The vertical fiber has dimension 1+epsilon+d-rho. Adding dimensions gives

    nu=1+epsilon+d+m-2rho-sigma,
    rank M=2rho+sigma.

These formulas include empty-support and zero-matrix cases. Since K|C remains alternating, sigma is even. The asserted parity nu=1+epsilon+d+m modulo 2 follows, also directly from the even rank of M. It is only a Selmer-dimension parity statement. No analytic rank, root-number statement, rational-rank parity or Sha parity is inferred from it.

Vertical completeness is exactly A0=0, equivalently nondegeneracy of K|C, with the zero-dimensional case interpreted by zero radical. If dim C is odd, an alternating form has even rank below that odd dimension, so its radical is nonzero and V is a proper subspace. This obstruction follows from the actual exact quotient; it is not a failed search for nonvertical representatives. If dim C is even, nondegeneracy still requires the actual restricted matrix, not a parity argument alone.

## 5. Special branches, optional pairing bound and scope

When J is empty, C=A0=0 and nu=1+epsilon+d; this recovers d+2 for the higher-valuation all-PQ-primes-7-modulo-8 branch and d+1 for its valuation-four counterpart. The prior fixed-core papers retain their own actual support and pairing proofs. No new curve dimension is numerically evaluated here. When one of J_P,J_Q is empty, K=0, so A0=C and full vertical coverage holds exactly when L has full row rank, including the vacuous empty-row case. When both are nonempty, the cross block can matter on C and cannot be erased merely because first coordinates are locally square at 2.

If a genuine vertical Cassels restriction of rank r is supplied independently, the full alternating Selmer pairing has rank at least r. Its radical contains the complete rational Kummer image of dimension rank E+2, so rank E<=nu-2-r. This optional inequality uses that actual Cassels pairing and the full nu, not the compatibility rank of M or K, and does not require the rational Kummer image to be contained in V. It remains a bound; an uncomputed compatibility radical does not certify a full Cassels radical or an exact rank.

The new membership/quotient theorem needs only the first/eighth local tables, Stoll and elementary Legendre/quadratic-reciprocity/F2-duality inputs. The ninth pairing paper is not a hidden premise of that theorem. No full first-coordinate-nontrivial Cassels calculation is provided. A nonzero quotient flags precisely the additional directions whose pairings remain unresolved by a vertical restriction.

The finite membership carrier uses distinct prime bits, but it is insufficient to reconstruct actual D squareclass exponents or PQ multiplicities by replacing every support exponent with one. The original P,Q, root order, factor multiplicities and Euclidean core must remain attached for torsion classes, tangents and later pairing observers. The paper expressly preserves this distinction. The present faithful reduction establishes the declared membership/quotient readout without authorizing erasure of other joint arithmetic information.

The primitive/opposite-parity, disjoint correctly labeled complete supports and exact root/zero/model conventions are essential. General odd P,Q lacking the norm-two condition, a missing local table or a false primary bridge prevents invoking this compression unchanged. No actual matrix rank, point, global rank, saturation, odd-primary Sha, whole-Sha finiteness, infinite family, all-core classification or parent closure is proved. No fixed-(233,119) code/input/Task budget or scientific gate changes, and no old accepted seeds/F5/H/multiples/closed tasks are repeated.

This is a bounded domain composition of the existing full Kummer and finite linear compatibility interfaces, not a new general-purpose tool or a historical-novelty claim. External classical arithmetic retains its separate type under Heartbeat X6, with no native-plane, spatial/time reinterpretation, Working Truth or Foundation promotion. The tenth audit is complete at its exact paper strength, with no correction requested or supplied. Actual new author Source and a true correspondence sidecar remain separate. No eleventh mathematical unit is initiated by this report. All mathematical parents remain OPEN.

Driver-ID: EM-DVR-BFF6DC / CONTROL_PLANE
