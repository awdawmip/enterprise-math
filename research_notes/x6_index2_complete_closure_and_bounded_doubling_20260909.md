# X6 index-2 closure: complete endpoints, flag multiplicity, and bounded doubling

Status: `RESEARCH_NOTE / EXACT_DERIVATIONS_AND_EXECUTED_FINITE_CERTIFICATE / NOT_INDEPENDENTLY_REVIEWED / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-09`
Researcher-ID: `EM-X6COUNT-3B06CF / TASK_RESEARCH`
Research-Activity-ID: `RA-X6COUNT-3B06CF3EC023`
Activity path: `research_activity_records/RA-X6COUNT-3B06CF3EC023.json`
Session key: `local-chat-x6count-3b06cf3ec023` (locally assigned writer key, not a platform-authenticated session ID).
Question: continue the direct-user count/metric research, classify the 63 index-2 branches and three-stage isotropic closure, and persist in EM.
Frozen source snapshot: `awdawmip/enterprise-math@cf224163a9fe5ea4f3ac6d8dd5e13f1b771daf44`.
Global entry snapshot: `awdawmip/chatgpt-global-knowledge@972981de198d0701835e24687e2c64bcc6963b2e`.
Parent: `research_notes/x6_count_metric_split_rotating_index_closure_20260908.md`.

## 0. Scope and recovery

The parent's results are consumed, not restarted as new discoveries: the X6 signed integer-coordinate carrier, quadratic readout, count-to-equivalent-volume scale, cube necessary gate, sharp one-map defect minimum 8, and one disjoint-pair closure were already present.

All statements below use a chosen Cell chart with translation group Z^6 and quadratic readout Q(z)=sum z_i^2. P000 is unchanged. Matrix orthogonality here refers to this admitted component readout; it does not replace native PERP_E/120-degree semantics by classical angle semantics. A pair-H map is a composite lattice/index transport, not a primitive Cell step. Its normalized orthogonal factor is not automatically an admitted complete native rotation.

Three notions must remain separate:

- additive successor n -> n+1;
- multiplicative index doubling n -> 2n;
- a unit signed-axis spatial transition.

This note constructs the second, not a universal law for the first or third. It does not prove spatial equidistribution, native dynamics, or a physical law. The isotropic scale n^(1/6) remains a declared equivalent-volume observer, not a newly deduced unique microscopic placement.

## 1. Complete classification of the index-8 isotropic endpoint

Let A be an integer 6 by 6 matrix. Exact isotropy at index 8 means

    A^T A = 2 I_6.                                      (1)

The index follows as |det A|=8. Every integer column in (1) has exactly two nonzero entries, each +/-1. Two such columns cannot have supports intersecting in exactly one coordinate, because their scalar product would be +/-1. Their supports must therefore be equal or disjoint.

A common support of size two accommodates at most two orthogonal nonzero columns. Full rank requires six columns and six coordinate positions. Consequently there are exactly three disjoint coordinate pairs, with exactly two columns per pair. On each pair the 2 by 2 block is equivalent by row/column sign changes and permutations to

    H = [[1,1],[1,-1]],    H^T H = 2 I_2.

Conversely any such three-block construction satisfies (1). Thus every solution is a signed-row/column-permutation version of diag(H,H,H). These sign/permutation operations describe the matrix classification; no new native rotation ontology is inferred.

For a perfect matching M of the six named axes, the image sublattice is exactly

    L_M = {z in Z^6 : z_i+z_j is even for every {i,j} in M}. (2)

Column sign changes/permutations change its generating frame, not its image. Row sign changes are invisible modulo 2. Distinct matchings give distinct image lattices, since their weight-two parity checks recover the pairs.

Therefore there are exactly

    6!/(2^3 3!) = 15

embedded isotropic index-8 endpoint lattices. With ordered, signed generating frames there are 15*6!*2^6=691200 matrices. Up to the S6 axis-permutation action, the 15 endpoints form one orbit with stabilizer size 720/15=48.

This is classical weight-two orthogonal-matrix/coding-theory structure specialized to the EM carrier, not a claim of a new classical classification.

## 2. Complete classification of the 63 first-step branches

Every index-2 sublattice of Z^6 is

    L_h = {z : h dot z = 0 mod 2},  0 != h in F_2^6.

For a matching M define its parity-check space

    W_M = span_F2{e_i+e_j : {i,j} in M}.

It has dimension three. The exact incidence law is

    L_M subset L_h  iff  h belongs to W_M.               (3)

The seven nonzero words in W_M have weights 2,2,2,4,4,4,6. Equivalently, the support of h is a union of matching pairs. No odd-weight first branch can contain an isotropic index-8 endpoint.

For a fixed h of weight 2s, the number of compatible matchings is

    (2s-1)!! (5-2s)!!,

with (-1)!!=1; match its support and its complement independently. This gives:

| weight(h) | first branches | compatible endpoints per branch | closing length-3 chains per branch |
|---|---:|---:|---:|
| 1 | 6 | 0 | 0 |
| 2 | 15 | 3 | 9 |
| 3 | 20 | 0 | 0 |
| 4 | 15 | 3 | 9 |
| 5 | 6 | 0 | 0 |
| 6 | 1 | 15 | 45 |

Thus 31 of the 63 first branches admit at least one exact three-stage isotropic completion, and 32 do not. This is a statement about general nested index-2 sublattice chains. It is NOT a statement that all 31 branches arise from the parent's minimal-defect pair-H packet.

## 3. BRC counts: endpoints are not chains

A chain ending at L_M has the form

    Z^6 > L_1 > L_2 > L_M,

with each index equal to two. Since 2Z^6 is contained in L_M, it corresponds exactly to a flag

    0 < W_1 < W_2 < W_M

with dimensions 1,2,3 in the dual parity space. There are seven choices for W_1. For each such line, W_M/W_1 has dimension two, giving three choices for W_2. Therefore every endpoint has exactly 21 chains, and

    endpoint count = 15,
    path/flag count = 15*21 = 315.                        (4)

With the first branch fixed, each compatible endpoint has three remaining flags. This proves the last column of the table.

There are 63^3=250047 unrestricted length-three index-2 chains, because each rank-six lattice has 63 index-2 sublattices. Uniform choice at each such step therefore has exact closure probability

    315/63^3 = 5/3969.

By contrast, there are GaussianBinomial(8,3)_2=97155 index-8 sublattices, so a uniform endpoint-layer choice has closure probability 15/97155=1/6477. These are different measures, not competing answers.

The certificate independently enumerates all 1395 dimension-three subspaces of F_2^6. Exactly 15 are self-dual for the binary dot pairing, and they are exactly the W_M. This code classification agrees with the classical binary self-dual-code database, which has one equivalence class at length six. Named-axis embeddings retain 15 distinct objects.

## 4. Exactly which pair-H words close

Let H_P act by H on coordinate pair P and by identity elsewhere. Every H_P has |det|=2 and Delta_6=8, where

    Delta_6(A) = 6 tr((A^T A)^2) - tr(A^T A)^2.

In the explicitly declared 15-map alphabet {H_P},

    (H_R H_Q H_P)^T(H_R H_Q H_P)=2I
    iff P,Q,R are pairwise disjoint.                     (5)

Proof of necessity, not merely exhaustive evidence: put C_1=H_P H_P^T=I+P_P, where P_P is the diagonal projection onto the pair. Then

    tr(C_2) = tr(H_Q C_1 H_Q^T) = 10+|P intersect Q|.

If the third step closes, C_2=2(H_R^T H_R)^(-1)=2I-P_R, whose trace is 10. Hence P and Q are disjoint. In that case C_2=I+P_P+P_Q, and comparison forces R to be their complement. Sufficiency follows from disjoint support.

There are 15*3!=90 successful ordered words out of 15^3=3375, giving fraction 2/75 under this separately specified uniform packet-word measure. For each endpoint these are six particular chains inside the 21 general chains in section 3.

The statement does not classify arbitrary changes of generating bases between stages as if they were the same 15-letter alphabet.

## 5. Symmetric choice and least local defect are incompatible without extra state

The 63 branches split into S6 orbits by Hamming weight. The only nonzero vector fixed by every coordinate permutation is h=(1,1,1,1,1,1). Thus the unique S6-invariant index-2 sublattice is

    D_6 = {z : sum_i z_i is even}.                       (6)

However, equality in the parent's sharp Delta_6>=8 theorem forces the Gram matrix to be diagonal with entries (2,2,1,1,1,1), up to permutation: any nonzero integral off-diagonal entry already contributes at least 12. The four norm-one columns occupy four different coordinate positions. The other two columns must form a pair-H block on the two remaining positions. Its image is a weight-two parity branch.

Consequently no basis of the invariant D_6 branch realizes Delta_6=8. Full symmetry and a deterministically selected locally minimum-defect branch cannot both be imposed on a bare unmarked state. This is not a contradiction: they optimize different conditions.

Likewise, no matching is fixed by S6. A deterministic S6-equivariant selector from an S6-fixed initial state to a single matching cannot exist. Retaining the full matching branch family, a uniform distribution, or an explicit symmetry-breaking frame can avoid this obstruction. None is selected uniquely by P000 or by the present proof.

The existing finite_symmetry implementation is executed unchanged to verify the orbit, fixed-point and stabilizer statements.

## 6. Exact infinite continuation with bounded metric distortion

At each three-stage block, choose any perfect matching and use its three pair maps, in any order. Different blocks may use different matchings. Write F_k for the total product after k index-doubling events, and k=3t+s with s in {0,1,2}. Every complete block B satisfies B^T B=2I, so induction gives

    F_(3t)^T F_(3t) = 2^t I,
    |det F_k| = 2^k.                                    (7)

This is an all-t exact proof, not an extrapolation from experiments. At an incomplete block the previous total is 2^(t/2) times an orthogonal factor. The current partial matching multiplies 2s directions in squared norm by 2 and leaves the other 6-2s unchanged. Therefore the spectrum of F_k^T F_k is

    2^(t+1), multiplicity 2s;
    2^t,     multiplicity 6-2s.                          (8)

For s=0 all six eigenvalues are 2^t. Hence

    condition_number(F_k) = 1 if s=0, sqrt(2) otherwise.

Writing rho(2^k)=2^(k/6), every vector satisfies the uniform bound

    2^(-1/3) rho(2^k) ||v|| <= ||F_k v||
                             <= 2^(1/3) rho(2^k) ||v||. (9)

For s=1,2 the raw defect is 8*4^t; its growth is a scale effect and does not contradict the uniform normalized distortion bound. At each complete block the defect vanishes exactly.

The certificate checks 180 prefixes across 60 blocks with changing matchings using integer matrix arithmetic. The infinite statement is established by (7)-(9), while those prefixes are regressions only.

This is a bounded-distortion realization of 1,2,4,8,16,... as index objects. It is NOT yet a realization of successive integers 1,2,3,4,..., a mixing/equidistribution theorem, or an autonomous physical successor law.

## 7. A concrete unsafe-compression witness and a scoped repair

Let A=H_(1,2), A'=H_(3,4), and fix the SAME future operation U=H_(5,6)H_(3,4). Then

    Delta_6(A)=Delta_6(A')=8,
    Delta_6(UA)=0,
    Delta_6(UA')=56.                                    (10)

Thus future defect does not factor through present scalar defect. This explicitly applies the existing T6 fiber-constancy criterion from composition_safe_collapse.py; a lookup alone would not establish reuse.

For the narrow observer consisting only of future quadratic-shape readouts under left composition, the output covariance C=AA^T does provide a safe carrier:

    C -> B C B^T.

This descent law holds for arbitrarily many declared left-compositions. It does not preserve the integer image lattice, radix digits, path order, or joint arithmetic relations. For those outputs retain the actual integer transport/lattice and the required provenance; C alone is not globally authorized as a replacement.

For a fixed matching, the three pair parities are independent binary coordinates and give eight residue classes. Choosing one coordinate in each pair supplies an exact 8-digit transversal, checked for all 15 matchings. Repeating one parity check three times instead would leave only two states. Independent joint checks, not duplicated copies of an observer, supply the missing information.

## 8. Stronger classical gate: cubes are necessary but not sufficient

External theorem reuse, not a new theorem claim: Conway, Rains and Sloane, On the Existence of Similar Sublattices, Canadian Journal of Mathematics 51 (1999), 1300-1306; arXiv:math/0207177v1, Theorem 2 (PDF pages 3-4 of printed body / zero-index PDF page 4 for the table continuation).

For the integer lattice with identity Gram matrix in dimension six, that theorem states

    exists A in M_6(Z), A^T A=qI
    iff q=a^2+b^2 for integers a,b, q>0.                 (11)

The two-square block construction in the parent supplies sufficiency explicitly. Necessity is the classical similarity-multiplier theorem, not proved merely by the determinant argument.

Consequently the exact isotropic INDEX set is

    {q^3 : q is a positive sum of two integer squares}.  (12)

This sharpens, rather than contradicts, the parent's necessary cube gate. Shell landing and whole-lattice isotropy are strictly different:

- n=8: q=2, both shell landing and whole-lattice isotropy exist;
- n=27: q=3, shell landing exists at sqrt(3), but whole-lattice isotropy does not;
- n=729: q=9, isotropy exists via A=3I.

### Independent elementary obstruction for q=3

If A^T A=3I then AA^T=3I and A inverse=A^T/3. Its Smith factors all divide 3 and have product 27, hence three are 1 and three are 3. The image of A modulo 3 has dimension three and is totally isotropic for the standard nondegenerate bilinear form on F_3^6.

Extend a basis V of that image to a basis [V,W]. Its Gram matrix has block form [[0,K],[K^T,D]] with K invertible. Its determinant is -(det K)^2, but also equals det([V,W])^2. This would make -1 a square in F_3, a contradiction. The same argument excludes q=p for every odd prime p congruent to 3 modulo 4.

### Exact first-repetition corollary

For positive n=product p^a_p, define r_min(n) as the least positive r for which some integer similarity has index n^r. From (11)-(12),

    r_min(n) = lcm_p [ b_p / gcd(b_p,a_p) ],
    b_p=6 if p=3 mod 4, and b_p=3 otherwise.             (13)

Use the empty lcm=1 for n=1. Hence r_min is always in {1,2,3,6}. In particular a prime p needs three repetitions if p=2 or p=1 mod 4, but six repetitions if p=3 mod 4. Examples are r_min(2)=3, r_min(3)=6, r_min(8)=1, r_min(27)=2, r_min(6)=6.

This concerns existence of an endpoint map of the stated index. It does not assert the existence of a unique bounded-cost local selector, or that arbitrary fixed repeated matrices achieve this minimum. The experiment checks (13) against direct two-square tests for n=1,...,512; the all-n conclusion follows from the imported theorem and the displayed divisibility argument.

## 9. Evidence, reuse, and novelty boundary

Internal sources at the frozen EM snapshot:

- definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md;
- definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md;
- definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json;
- src/enterprise_math/finite_symmetry.py, exact Git blob ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2;
- src/enterprise_math/composition_safe_collapse.py, Git blob 384d166f642fb65c53fc7f2431f43dc99880693a;
- parent note and its rank-six sublattice-count formula.

Resolutions:

- T0_BRC: REUSE_APPLIED, population=nested lattice chains and pair-map words; augmentation to endpoint multiplicity and Boolean support kept separate. These are index-transport paths, not primitive signed-axis paths.
- T6_OPERATION_SAFE_QUOTIENT: REUSE_APPLIED to the exact witness (10), and the explicitly scoped covariance descent law. No global erasure of joint/parity/phase/provenance data is authorized.
- T7_FINITE_SYMMETRY_EQUIVARIANCE: REUSE_EXECUTED unchanged, exact source blob checked locally. Orbits, global fixed points, canonical-choice obstruction and stabilizer computed through the existing module.
- T1 enumeration: parent's exact Gaussian-binomial layer count reused as a count law, not new native polynomiality or a new general-purpose calculus.
- Payload classification: RESULT_ONLY / DOMAIN_CERTIFICATE; no new toolbox family is proposed.

External deduplication: Harada-Munemasa, Database of Binary Self-Dual Codes, length-six row, confirms one equivalence class. Conway-Rains-Sloane Theorem 2 supplies (11). The contribution of this note is the EM-typed complete branch/flag linkage, declared-alphabet closure test, explicit unsafe observer witness, and uniform block-doubling synthesis. No assertion that these elementary/classical components were previously unknown is made.

## 10. Executable return and next exact question

Run:

    python experiments/x6_index2_closure_v2_20260909/verify.py

The package includes results.json and a SHA256/Git-blob manifest. It verifies the full 1395-subspace census, all 3375 pair words, the independent norm-two frame census, S6 symmetry statements, 180 exact prefixes, residue transversals and 512 repetition-index checks. No floating-point tolerance is used. Whole-repository CI or independent Driver review was not run or claimed.

Next exact question: construct or obstruct a provenance-preserving cross-prime selector that combines the three-stage p=2/1 mod 4 endpoint regimes with the six-stage p=3 mod 4 regime, while retaining joint composite observers, bounded normalized distortion, and the correct multiplication/Hecke composition law. A separate additional law is still required to relate that multiplicative family to additive successor n -> n+1. Do not restart the endpoint and flag census above.
