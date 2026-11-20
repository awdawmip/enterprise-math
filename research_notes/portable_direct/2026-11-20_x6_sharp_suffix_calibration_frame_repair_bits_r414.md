# X6 r414 — Sharp frame-repair bits for suffix-calibrated signed-word observations

Date: 2026-11-20 (Asia/Shanghai). Author-side mathematical deduction and exact finite check; NOT an independent Native Review or physical rotation claim.
New proof contributor: EM-DVR-DEBB5E; preserve original X6 signed-word contributor provenance EM-EMF6D046-5A2844 / EM-X6-DFD1FD / EM-X6CM-EDBD55.
Continuity: r411 (six-axis zero-side-information calibration), r412 (typed-language decision), r413 (equivariant legal-language kernel).

## Theorem A: exact residual fiber and optimal fixed-width repair

Let a finite group H act letterwise on a finite alphabet Sigma. Let E be a finite H-set, c:E->Sigma^ell injective, fixed-length and H-equivariant. Fix an event suffix s and a language L subset E*. Define U_s={u:us in L}, K_s={g in H:g c(s)=c(s)}, and O_s(u)=[c(us)]_H.

For every u in U_s, irrespective of whether L is H-invariant,

  O_s^(-1)(O_s(u)) = (K_s.u) intersection U_s.

If L is H-invariant, then U_s is K_s-invariant and the fiber is exactly the K_s-orbit K_s.u. Thus every fiber has at most |K_s| elements, independently of prefix length.

Let M_s = max_{u in U_s} |(K_s.u) intersection U_s| (set M_s=1 when U_s is empty and no encoding is needed). If an auxiliary fixed-width b-bit tag R(u) must make (O_s(u),R(u)) exactly injective for ALL u in U_s, the sharp information-theoretic requirement is

  b_min = ceil(log_2 M_s).

Necessity: the M_s distinct elements of a largest fiber must have different tags; 2^b >= M_s. Sufficiency: fix a canonical shortlex order on finite event words, enumerate the finite observer fiber of u, and tag u by its zero-based rank inside that fiber. The rank is in {0,...,M_s-1} and, together with the orbit and fixed suffix, recovers u exactly. The rank may be computed without preserving the entire raw prefix as an extra state: enumerate the at most |H| global images of one orbit representative, filter the specified suffix and actual admissibility, then sort distinct prefixes. With explicit group and lawful-language membership oracles, brute force takes O(|H|*n) image operations plus sorting (n is prefix-plus-suffix length); it is a finite construction, not a claim of optimal computational cost. The tag is the additional metadata; the base orbit representation cost is NOT included in b_min. QED.

## Corollary B: exact seven-point signed X6 calibration-versus-repair tradeoff

For the candidate static H=(C2)^6 semidirect A6, with signed primitive alphabet Sigma={+/-e1,...,+/-e6} and unrestricted U_s=Sigma*, let k be the number of DISTINCT unsigned axes appearing in fixed suffix s (sign repetitions do not matter). Let m=6-k. The pointwise suffix stabilizer fixes the k seen axes and has:
  |K_s| = 2^m * (m!/2) for m>=2;
  |K_s| = 2^m for m=0,1.

For m>=2, the parity-even permutations on the unused m axes number m!/2, with 2^m independent unused-axis flips. For m<=1, only the identity unused permutation remains.

Choose prefix u=e1 e2 e3 e4 e5 e6 (one appearance of each native positive axis). Its stabilizer in H is trivial, so K_s acts freely on u and the largest observer fiber has EXACTLY |K_s| elements. Therefore b_min=ceil(log_2 |K_s|), with the following sharp values:

| distinct suffix axes k | |K_s| | sharp fixed-width repair bits |
|:--:|--:|--:|
| 0 | 23040 | 15 |
| 1 | 1920 | 11 |
| 2 | 192 | 8 |
| 3 | 24 | 5 |
| 4 | 4 | 2 |
| 5 | 2 | 1 |
| 6 | 1 | 0 |

The k=6 entry recovers r411's shortest zero-metadata suffix condition. In particular, for k=3, a FIXED three-axis suffix PLUS five explicitly retained binary frame bits is sufficient for lossless reconstruction of an arbitrarily long signed primitive prefix; five bits are also necessary in the worst case. It is wrong to infer that six distinct suffix axes are always needed once auxiliary reference-frame metadata is allowed.

## Corollary C: the same sharp five bits in r413's candidate triadic alphabet

Let E consist of all 960 ordered signed triples with distinct unsigned axes; c(a) is the three-letter code. Fix s=a=(e1,e2,e3), and L=E* (globally H-invariant). Then |K_s|=24, and prefix u=(e4,e5,e6) is a legitimate CANDIDATE event code in E with trivial K_s stabilizer. Its 24 K_s-images are distinct and all remain admissible. Thus M_s=24 and b_min=ceil(log_2 24)=5, exactly.

If instead L is r413's H-equivariant repeat-only event language, U_a=a*, all fibers have size 1 and b_min=0. The two cases share the same alphabet and suffix but exhibit different optimal residual-storage costs solely through legal continuation. This proves a precise resource tradeoff for the representation-level observer.

## Proof boundary and relation to actual native science

These are exact statements about a candidate STATIC signed-frame group and the declared word/typed-event languages, not an intrinsic Enterprise 120-degree physical rotation, an accepted P000 triadic incidence, or a Cell/time/branch dynamics. The actual native event legality and observer scope must be supplied before transporting these bit bounds. Native Cell identity, force/Port provenance and time must not be erased merely because a static word orbit plus b frame bits is injective. Any future computational efficiency claim must separately account for orbit computation, the suffix, tag production/recovery and verification.

The original X6 Mother Objective remains open. Neither GitHub source publication nor author-side finite checking is Native Result admission, independent review, or formal Source/Activity association.
Companion checker: research_notes/portable_direct/r414_x6_frame_repair_bits_check.py.
