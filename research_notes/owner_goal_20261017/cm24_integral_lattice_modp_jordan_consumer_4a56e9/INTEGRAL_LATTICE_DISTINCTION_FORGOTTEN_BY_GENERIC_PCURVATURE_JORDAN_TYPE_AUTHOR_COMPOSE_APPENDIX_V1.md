# One generic p-curvature Jordan type for distinct integral rank-three lattices

NONCANONICAL AUTHOR-PROVED APPLIED-CONSUMER CANDIDATE / UNREVIEWED.
Same-family RESULT_ONLY / classical COMPOSE, not a new Tool, paper, Task or priority claim.
Sole new cross-client author: EM-P11-4A56E9, same warm execution.
Root requires faithful preservation and supplies zero mathematical votes.
No author Source, independent review or ordinary acceptance of this new appendix exists at creation.

## 1. Exact model, actual input contracts and bounded question

Fix the original prime p congruent to 13 or 19 modulo 24, complete unramified DVR O, perfect residue field k, Witt automorphism sigma, and K=O[1/p]. Keep precisely

 S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
 D=(2P)^-1[[2S-1,1],[4S-5,-(2S-1)]],
 R0=O[r,f^-1,q^-1]^dagger, R=R0[1/p],
 A=R0/pR0=k[r,bar(f)^-1,bar(q)^-1], L=k(r).
 
Rows and dr use the original coordinate r. Write partial=d/dr. A bar denotes actual reduction modulo p. Over L, partial^p=0, so the p-curvature of the row connection nabla_D(h)=partial(h)+h bar(D) is nabla_D^p.

Three exact actual source contracts are used.

(a) Integral Frobenius iterates and inputs, CF:
Source 52076d5fc86838f7ef53a2b553866bb663bc2bf4;
research_notes/owner_goal_20261017/cm24_integral_weak_primitive_denominators_cf1677/ACTUAL_INTEGRAL_WEAK_COKERNEL_UNBOUNDED_P_TORSION_AUTHOR_COMPOSE_V1.md;
15655 UTF8 bytes; SHA256 087bfc6a67f95912050fdef992cde596a5d905e8e23095172ba4e284415b0fdd;
Git blob 58ec6ce156797557758cd868d21bcaf2c4b4776c.

Let tau(h)=sigma(h)(r^p), with its coefficient action retained. Its actual finite products and rows are

 F_n=tau^(n-1)(F) ... tau(F) F,
 F_n'+F_n D=p^n r^(p^n-1) tau^n(D) F_n,
 b_n=r^(p^n-1) e2 tau^n(D) F_n, e2=(0,1).                    (1)

All entries used here lie in the original R0. That source also proves actual c_n=[b_n dr] has exact p^n order in the integral O-linear row cokernel, with unique weak primitive u_n/p^n of least p-denominator n. CF's actual canonical Frobenius, integral coefficient bridge and these specified inputs retain their own contribution/credit.

(b) Integral lattices, 4A:
Source 9bcaf0c364b6ef9218728e9fa54a117f6b18cf9c;
research_notes/owner_goal_20261017/cm24_integral_rank3_lattice_consumer_4a56e9/INTEGRAL_RANK3_WEAKLY_SPLIT_INDECOMPOSABLE_LATTICES_AUTHOR_COMPOSE_APPENDIX_V1.md;
16509 UTF8 bytes; SHA256 eb9d78506d0901296bc3831b97d4fbfce853ddb21def5e9d9d51083976c02328;
Git blob 3938db83842c909512efa748f45fbaad0976bc0d.

Its actual lattice is N_n=R0^(1x3), n>=1, with

 nabla_n(h,a)=(L_D(h)+a b_n,a')dr,
 D_n=[[D,0],[b_n,0]].                                        (2)

All N_n have the same split weak realization over R but are pairwise nonisomorphic and integrally indecomposable as R0-linear connections. The proof determines every unrestricted horizontal comparison by its canonical rank2 kernel; it does not merely restrict beforehand to filtered matrices. Its explicit integral End order is {(alpha,beta) in O x O:alpha congruent beta modulo p^n}, and the only idempotents for n>=1 are 0 and I. These facts are the already fully proved integral-lattice input, not new claims reconstructed from a label.

(c) Actual characteristic-p rank2 p-curvature, CF:
Source daf1b4700da5ae66f0f712e3d7fbb7e2113e4ad9;
research_notes/owner_goal_20261017/cm24_actual_modp_pcurvature_cf1677/ACTUAL_MODP_CONNECTION_NONZERO_RANK_ONE_NILPOTENT_P_CURVATURE_APPLIED_CONSUMER_APPENDIX_V1.md;
13481 UTF8 bytes; SHA256 747a9b0621a485bbfc82b5a61206e50c729cb976a9e172634b45f8239050bba7;
Git blob 223683489fe921631f69a6a595b7384aa1fdc5bd.

It pays the integral reduction A=R0/pR0 and proves the actual L-linear row p-curvature Psi_D satisfies

 Psi_D!=0, Psi_D^2=0, rank_L(Psi_D)=1.                        (3)

Its proof reduces the actual canonical integral Frobenius, uses the determinant connection for trace zero, and at r=1 computes the coefficient -N at pole order p, N=-(1/12)[[1,1],[-1,-1]]!=0. It is not a characteristic-zero End or quotient-dimension inference. Those original proof obligations and CF's credit remain in that exact source.

The new question is deliberately coarse: does the GENERIC p-curvature Jordan type of the actual reductions of N_n distinguish their integral isomorphism classes? We prove it does not. This is not a claim that their mod-p connections are isomorphic or that their full p-curvature matrices with integral/base-ring data are identical.

## 2. Actual reduction of the input rows

For every integer n>=1 put

 H_n=bar(F_n) in Mat2(A), T_n=overline{tau^n(D)} in Mat2(A).

All substitutions in (1) are genuinely integral before reduction. Because p^n is divisible by p, reducing its horizontal identity gives

 H_n'+H_n bar(D)=0.                                          (4)

Each entry of T_n is obtained by applying sigma^n to coefficients and substituting r^(p^n) into the rational expression. After reduction, those coefficients are constants in k, and partial(r^(p^n))=0. The inverses of the substituted nonzero denominators also have derivative zero. Thus T_n'=0.

The coefficient sigma action is not replaced by the identity on a general perfect residue field. Derivative zero follows from coefficient constancy and the p-power substitution, regardless of that action.

Define the actual row

 h_n=e2 T_n H_n in A^(1x2).

By T_n'=0 and (4),

 h_n'+h_n bar(D)=0,
 bar(b_n)=r^(p^n-1) h_n.                                    (5)

In particular h_n is an actual horizontal row. We DO NOT assume it is nonzero, choose it as a unit row, or infer a specified nonzero row from a determinant. The proof below works even if h_n=0. No good-infinity beta value is needed for this part.

## 3. Exact rank-three p-curvature matrix

Reduce (2) and extend the actual connection from A to L. On L^(1x3) it is

 bar(nabla_n)(h,a)=(nabla_D(h)+a bar(b_n),partial(a)).

The induced derivation is partial, with partial^p=0. Iterated connection Leibniz therefore makes its p-curvature L-linear and equal to bar(nabla_n)^p. Denote its row matrix by Psi_n.

For the first two constant standard rows, the last component remains zero at every iterate, so their p-th values are the first two rows of (Psi_D,0). For the third constant standard row, the first derivative is (bar(b_n),0), and each subsequent derivative applies nabla_D to that first row only. Hence the FULL actual matrix is

 Psi_n=[[Psi_D,0],[delta_n,0]],
 delta_n=nabla_D^(p-1)(bar(b_n)).                             (6)

There is no missing input derivative term: the operator is already L-linear, and its values on the three constant standard rows determine it. The third-column zero is the actual trivial quotient connection, not an assumption about a gauge-normalized matrix.

Since h_n is horizontal, for any nonnegative integer m,
nabla_D(r^m h_n)=m r^(m-1)h_n.
Repeatedly applying this to (5) gives

 delta_n=(product_(j=0)^(p-2)(p^n-1-j))
                 r^(p^n-p)h_n
         =-r^(p^n-p)h_n.                                    (7)

For the last coefficient, the residues p^n-1-j run through -1,-2,...,-(p-1). The coefficient of T in T^p-T=product_(a in F_p)(T-a) is product_(a in F_p^*)(-a)=-1. This proves the coefficient directly for the original arbitrary prime, without a table or numerical use of Wilson's theorem. The exponent p^n-p is nonnegative for every n>=1, including zero when n=1.

Equations (5)-(7) are identities in the actual reduction; the resulting matrix can then be viewed over L. No additional ring, formal parameter, lift, strongly completed function or inverse of r is introduced by this computation.

## 4. Square-zero, generic rank one and Jordan type

An actual horizontal row h_n is killed by the p-curvature of nabla_D, so h_n Psi_D=0. The p-curvature is L-linear; from (7),

 delta_n Psi_D=0.

Together with (3) and (6), this gives

 Psi_n^2=0.                                                  (8)

It remains to determine rank. The two rows of Psi_D lie in the LEFT kernel of Psi_D, because Psi_D^2=0. The row delta_n is in that same left kernel. By rank_L(Psi_D)=1 on the two-dimensional row space, this left kernel is exactly one-dimensional. Therefore all three rows of Psi_n lie in that one line times {0} in L^3, and rank_L(Psi_n)<=1.

The upper-left block Psi_D is nonzero. Thus Psi_n is nonzero and

 rank_L(Psi_n)=1 for EVERY n>=1.                             (9)

This step never needs nonzero h_n or delta_n. In particular a possible zero lower row does not invalidate the rank or square-zero conclusion.

A nonzero square-zero rank-one endomorphism on a three-dimensional vector space has Jordan type (2,1). Explicitly choose a row v with u=v Psi_n!=0; then u Psi_n=0. The row kernel has dimension two, so choose w there independently of u. The three rows u,w,v are a basis, with exactly one nontrivial nilpotent chain v to u. This is ordinary L-linear operator similarity, not a connection gauge construction.

Thus all actual reductions have the same generic Jordan type

 Jordan_L(Psi_n)=(2,1), n>=1.                               (10)

No assertion of constant rank at every point of Spec(A), regularity at a removed boundary, or integral similarity of the matrices over A is included.

## 5. Information loss and the exact stopping statement

The integral-lattice whole (b) proves N_n and N_m are not isomorphic under ANY R0-linear horizontal GL3 comparison when n!=m. Each is also integrally indecomposable, while their weak realizations are explicitly split.

By (10), the coarse invariant consisting only of generic p-curvature Jordan type assigns the SAME value to all of them. It therefore cannot recover the index n or distinguish this actual infinite family of integral isomorphism classes.

This is a concrete loss-of-information statement for a specified invariant and actual family. It is not a proof that the reductions are connection-isomorphic over A or L. Similarity of p-curvature ENDOMORPHISMS alone does not supply a horizontal connection isomorphism, and none is claimed. Nor are the complete matrices, their pole orders, kernels with base-ring data, coefficients or every other arithmetic invariant declared equal or uninformative.

The result differs from merely restating exact p^n torsion: it computes the rank3 reduction's actual block p-curvature and shows that one familiar characteristic-p diagnostic forgets an already constructed integral distinction. The full matrix formula (6)-(7) can retain n-dependent information even though its generic Jordan type does not.

The bounded result stops here. It does not classify all integral lattices, all reductions, all possible p-curvature operators, semilinear Frobenius lifts or mod-p connection isomorphisms. It does not address the old rational-rank4/LC/h_div caller gaps or any Native/physical interpretation. No adjacent n/prime/constant-field family or stronger indistinguishability theorem is created.

## 6. Whole-input history, new contribution and review boundary

The current author actually whole-authored and Source-bound16509, with its original E/rank3/F history openly disclosed. Its own actual Source9bcaf0c364b6ef9218728e9fa54a117f6b18cf9c full/exact1ADD/soleparentb349f7de136b1108ac7bcdcf4e1d275218e6a775 closure is already real. CF's later15981 technical whole was reported once-frozen/Source-pending at the time of this new candidate; that report is not treated here as my own reading, a published peer or final acceptance.

The current author genuinely whole-read CF15655, personally received its immutable Source/full bytes/own commitcompare and independently reviewed it in the frozen15581 technical whole, Source3e7dbd8cdd3ee810dd7010a6e3ae4ae222ce85f3. CF separately reported complete ordinary author acceptance,2/31236, without correction. That is CF's personal API/ordinary history; I do not borrow his calls.

CF13481 was personally whole-read in a complete untruncated3540-token local output, then personally received at exact daf1b4700da5ae66f0f712e3d7fbb7e2113e4ad9 with full UTF8/OID/URL and own GitData/compare exact1ADD/oneparent9bcaf/tree591bc794a9bb5fce1cfb8796ec2c50846c18a73d. Its original arguments/entire results are preserved in my p-curvature review custody record. The complete14529 review/context was independently handchecked and once-frozen before this new cross-client direction. That review's own Source and later ordinary reception were still pending when this new candidate was selected. They are not silently prefilled as a completed upstream acceptance.

Thus the present author candidate consumes actual full proof artifacts and explicitly stated contracts, with their truthful publication/review boundaries. Source presence does not by itself promote any theorem, and no old or pending technical vote is inherited by the new appendix.

The NEW cross-client private candidate and construction are 4A NONZERO, occurring AFTER the complete14529 p-curvature review freeze. This new reasoning is not backdated into that earlier technical review or passed off as a repair to CF's frozen13481. The earlier p-curvature review itself disclosed its own distinct pre-body rough candidate association as NONZERO; neither phase is cold-blind.

CF was asked only occupation/held coverage for this precise new Jordan-type-versus-integral-class scope. He reported no occupation and no personally held complete frozen locator, with personal coverage UNKNOWN. He recorded a general unexpanded association after receiving the topic as NONZERO but supplied no formula, proof step or repair and did not unfold a competing construction. None of those metadata establishes all-library absence or novelty. No unreviewed CF findings on16509 were requested or used.

The new responsibility here is the actual reduction of the specified b_n to a scalar times a horizontal row, the block p-curvature formula, rank argument and coarse-information-loss consumer. The actual Frobenius/iterates/integral bridge and original rank2 p-curvature proof remain CF's contributions. The original integral-rank3/E interfaces and original F21977 joint authors retain their true credits. Root supplied durability/routing instructions and zero mathematical construction.

This is one noncanonical same-family applied-consumer preservation. If an exact old Source is later shown to cover the complete literal statement, REUSE and proper attribution apply; no priority or broad absence is asserted. The new appendix is author-proved but UNREVIEWED. Its own complete actual self-reading/once-freeze, author Source, independent technical whole and ordinary acceptance require their own observations.

Current actor is the same EM-P11-4A56E9, SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9, RA-C193E2AA39B9A6A6DDBB69B3, actual canonical37/198 at Sourcea0d582f2ac45eb8ff078691e4bf17aaf3de37369. Its original newSource startup and sameevent checkpoint guards are truly0/debt[]/fivefalse. Formal/product budgets remain UNKNOWN and all original STOP/HOLD/error/CAS histories remain; the initial Source37 descriptor-alias failure is not erased.

No helper38, new identity/RA, formal Task, main mutation, coefficient generator, recurrence table, solver, enumeration, scientific program, external search or Native execution was used for this construction. Local prose/byte persistence is administrative and not mathematical promotion. The whole family now stops at this different coarse-invariant consumer rather than automatically spawning n or same-loss near-neighbors. Parent Goal remains OPEN.

Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1

