# Stage391-B — X6 selected-three-component observer and exact BRC future-fiber theorem

2026-11-03, author-side Research2 portable research; parent Stage390-B e01d84eac5603ddc1b8d2d6ee06cb8e42ed1a078; Draft PR #1736. This is the constructive bridge alternative authorized by Stage391-B's task packet. Argument status: proved within the declared symbolic model, executed exact rational certificate; UNREVIEWED / NOT_ADMITTED.

Frozen scientific sources: GLOBAL_KNOWLEDGE_V1 bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488 (identical when checked at current EM main). Applicable current rules read separately at global main 35f1c89412ea58b9cf48aa3d0bdf220558d89f34, EM main 3bdef5a60a736f9f6a89891aa3bc2ec1cedbc407, including the native X6, centered three-axis slice, joint observer preservation, BRC and portable research contracts. No P000/worldview change.

## Carrier and exact source-labelled BRC outputs

Choose a native Cell chart anchor c in the native affine X6 torsor. Internal signed chart displacements are a=(a1,a2,a3,a4,a5,a6) in Z^6, with six independent native axes and their positive/negative primitive directions. This anchor is a Cell, not a distinguished global ontic origin. The selected triple is pi3(a)=(a1,a2,a3), retaining the genuine third component. The actual centered 3-axis native slice through c is iota_c(Z^3)={c+(a1,a2,a3,0,0,0)}; pi3 applied to an arbitrary X6 state is an observer, NOT a proof of slice membership. No native plane or independent 3-dimensional world is introduced; full public Cell addresses require the separate registered six-nonnegative-field codec.

A state also has a separately typed abstract operation order n>=0 (not a physical heartbeat clock) and source sigma in {P,Q}. Define for k=0,1,2,3:
 B_k(z)=z^k (1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9).
 For each sigma fix rational auxiliary bridge test parameters (uP,vP)=(1/4,3/4), (uQ,vQ)=(1/3,2/3).
 R_k(sigma)=[4 B_k(u_sigma)+B_k(v_sigma)]/5-m_k/160.
 A_sigma consists of all 16 ordered signed differences B_k(z)-B_k(q) for (z,q)=(u_sigma,1/4),(u_sigma,3/4),(v_sigma,1/4),(v_sigma,3/4), k=0..3.
Retain the source label, order, and sign of each comparison and all four independent residuals (no absolute-value simplification). The parameters are independent *test* choices for the bridge, not a change of the frozen Bernoulli optimizer, its budget, its cost or its theorem.

Define current readout O(a,n,sigma)=(a1,a2,a3,n,sigma,A_sigma[16],R_sigma[4]).
The exact primitive-axis BRC interface for an integer signed displacement d in Z^j is
 L_j(d)=sum_i |d_i|, M_j(d)=L_j(d)!/product_i(|d_i|!).
M counts shortest *ordered* signed native-axis words from a declared anchor. It is typed combinatorial path multiplicity, not a phase, amplitude, physical propagation or spatial-dimensional replacement.

## Declared operation family, exact theorem and proof

Define a symbolic test family A0 with 14 operations: for each i=1..6, native-edge T_i+ and T_i- add +1 or -1 respectively to the raw coordinate a_i; source switch S changes P to Q or Q to P (recomputing A_sigma and R_sigma); and H increments a1 by +1 iff a4 is odd, else takes an idle spatial step. Every operation increments abstract index n by one. H is expressly a chosen *model-test future operation*, not a claimed native physical heartbeat update.

Theorem. For all a in Z^6, n>=0, sigma in {P,Q}, and all finite words over A0:

(A) O has nonconstant future fibers. Let a=(0,0,0,0,0,0), a'=(0,0,0,1,0,0), n=0, sigma=P. Their O-readouts are equal. Under H, pi3 becomes (0,0,0) versus (1,0,0); BRC selected lengths become 0 versus 1 (shortest multiplicity both 1). Thus H does not descend through O.

(B) The repaired observer C(a,n,sigma)=(O(a,n,sigma), a4 mod 2) is future-safe for every finite A0 word. Proof: for Ti+/- with i<=3, C records the changed selected component; for i=4 it toggles retained parity; for i=5,6 it leaves selected triple and parity fixed. Under H, the retained parity exactly decides the selected +E1 increment. Under S the retained source label selects the exact 16 audits and four residuals. All operations increase retained n. Hence for every generator G, C(s)=C(t) implies C(Gs)=C(Gt). Induction on word length proves the statement for every word (including empty word). This is an *all-integer/all-finite-word* algebraic proof, not an extrapolation from tests.

(C) The future-equivalence classes in every nonempty O-fiber under A0* are exactly the two parity classes of a4. Same parity implies equality after every word by (B); different parity is distinguished by one H by (A) regardless of a1,a2,a3, n or sigma. A single bit is therefore an exact and sharp minimal repair, relative to this current observer and operator family.

(D) For the larger declared symbolic alphabet A1=A0 union {J_m : m in Z}, where J_m adds +E1 iff a4=m (otherwise idle), full integer a4 must be preserved to obtain future safety on O-fibers: for a4=m != m', operator J_m separates the readouts. In particular a4=0 versus a4=2 share C but J_0 distinguishes them in one step. If current readout includes the full native BRC length L6 from c, this particular pair is already distinguished (L6=0 versus 2). Thus the sharp safe compression is observer- and future-operation-scoped.

Full native six signed coordinates remain available as raw state during these tests; neither compressing an observer nor using an auxiliary rational four-channel model changes the P000 ontology.

## Exact executed verification

The attached REPRO_STAGE391B_X6_FIBER.py uses standard-library Fraction for the full source-tagged 16-audit/four-residual arrays and integers for native BRC shortest word counts. It checks the two exact distinguishing pairs, a 392-case model-generator descent table and 8,865 word comparisons from three equal-C pairs for all words of lengths 0..3 over the 14-operator alphabet. These finite tests audit the implementation; the proof in (B) covers every finite word.

Program executed twice independently, stdout byte-identical:
STAGE391B_X6_FIBER_EXACT_PASS
table_checks 392
sampled_word_checks 8865
audit_labels_per_source 16
residual_channels_per_source 4
certificate_bytes 2068
certificate_sha256 20aa1451d1faa142fabb88531f78b22cd491913bc00ec381c12c4d05d0e205de

The exact JSON certificate was generated by the executed source (2068 UTF-8 bytes). Source SHA256 was 838d87c549479c5cdb1baa65d212b83c2fc35f80d70bb64e740d99a0abc51c15.

## Claim scope and next science

This is a typed, internally exact P000-X6 observer test construction, reusing the combinatorial BRC path law and source-labelled Bernoulli residual outputs. The symbolic H, J_m, and S are explicitly declared test operators, and no physical heartbeat dynamics, globally safe compression for unspecified operations, Stage381 optimizer transfer, independent review, native Result or Foundation promotion is asserted.

Next Stage392-B: choose an *actual version-pinned native signed-X6/BRC operation* from the project, determine exact future-observer fiber safety with the third component and full signed provenance, and furnish a concrete repaired quotient proof or an exact pair of indistinguishable-current/distinguishable-future states. Alternatively independently audit the frozen Stage366/367 auxiliary optimization certificates. Preserve all scientific frozen pins and actual source exposure.
