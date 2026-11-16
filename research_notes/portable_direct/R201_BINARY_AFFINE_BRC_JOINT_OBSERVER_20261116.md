# R201 — Field-uniform binary affine realization of the paired provenance–event-tail quotient

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_DESCRIPTOR_FINITE_CHECKED / NOT_REVIEWED / NATIVE_PACKAGE_EXECUTION_PENDING.
Scientific frozen pin: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Depends on R200@8cb50690 (the finite paired observer and its exact state count), R195/R196 (source reset and BRC affine-effect transport). Native code contract was inspected at \`src/enterprise_math/brc_transport.py\` under the frozen pin, blob \`be1debe367263931bd5e93fd750be3ed54624fe1\`.
Scope: P000's X6 native 12 signed directions remain 12 directions of six spatial axes; time, complete native paths, branch identity, phases/signs and unobserved provenance remain separately typed. This theorem represents only the declared finite quotient and compatible positive-weight total-affine BRC operation.

## Theorem R201-A (compact faithful affine action, any field)

Let A={0,...,a−1}, a>=1, and lambda:A -> K union {bottom}, K={0,...,k−1}, each label i in K having a preimage. Let L>=0. R200's joint observer is F(w)=(s(w),tail_L(w)): s is the last-occurrence order of selected labels, oldest first, and tail is the final min(L,|w|) complete event symbols (not merely marginal directions). Its image J is the finite quotient monoid under concatenation.

Let b=ceil(log2(a+1)), choose nonzero distinct b-bit words c(x) encoding x+1 (little-endian in the implementation), and put

    d = k + C(k,2)
    D = d + b L.

For every field E, including F_2, there is an explicit **faithful monoid homomorphism** \rho:J -> Aff(E^D), with composition in chronological order, generated only by coordinate selection and setting coordinates to 0 or 1. In the degenerate D=0 case this means the unique affine action on a zero-dimensional singleton.

Construction. Source registers comprise U_i for each i and V_{ij} for i<j. Initially all are zero. Upon an event x labeled i, set U_i=1; set V_{ij}=1 for every j>i; set V_{ji}=0 for every j<i; leave all other source registers unchanged. A bottom label changes no source register. Tail registers T_1,...,T_L each have b coordinates, all initially zero. Every event x applies

    (T_1,...,T_L) -> (T_2,...,T_L,c(x)).

For L=0 this block is absent. These are affine transformations with coefficients and offsets in {0,1}, therefore valid over any field.

**Orbit proof.** After a history w, U_i=1 iff i has appeared. For i<j, V_ij=1 iff last(i)>last(j), with absent last=-infinity and a both-absent tie recorded as zero. Thus U and V determine the entire partial last-occurrence order s(w). Tail registers contain a zero left-padding followed by exactly the b-bit encodings of tail_L(w). Because no event has zero code, the tail is uniquely recovered, including its length. Hence the action on the zero initial vector recovers F(w).

**Descent proof.** For any history w, the induced source-register transformation for U_i either keeps U_i or sets it to 1, determined by whether i occurs in w. For V_ij it either stays unchanged (neither i nor j occurs in w), or is set to 1 or 0 according to which of i,j occurs last in w. These choices depend only on s(w). The tail transformation for |w|<L shifts by |w| and appends the entire w, which equals its observed short tail; for |w|>=L it is the constant map to the final L event codes. Thus the complete affine transformation depends only on F(w). Distinct F(w) have distinct transformations because they yield different images of the zero vector. Concatenation of word actions gives \rho(F(wz))=\rho(F(w)) then \rho(F(z)), proving a faithful affine realization of the R200 quotient (no appeal to sampling).

For the finite alphabet A=[m]×(K union {bottom}), a=m(k+1). In native X6 with m=12, k=6, L=2:

    a=84, b=7, d=21, D=21+14=35.

R200's exact count at these parameters is |J|=1,407,685, giving 21 bits for an arbitrary optimal fixed binary state code. The present 35-coordinate representation is a **field-uniform affine-action upper bound**, not a claim of affine minimality. Over F_2 the orbit-cardinality lower bound is 21<=minimum dimension<=35.

## Theorem R201-B (native EffectHistogram joint lifting)

Let the physical BRC affine-action dimension n>=1. For each original physical action P and paired observer state f in J, define the block action

    Lift(P,f) = P direct_sum \rho(f) on E^(n+D).

For E=Q, the block action is a valid \`enterprise_math.brc_transport.Affine\`; it does not require the blocks to be invertible. Its exact input is (physical affine effect, complete paired source-event observer, positive rational branch weight, positive integer multiplicity). Under the existing total-action, fixed-weight, no hidden-path-sensitive access assumptions, mapping each joint term (q,P,f,c) to (q,Lift(P,f),c) is injective. Indeed the physical block recovers P and the source/tail block is faithful to f. Therefore \`EffectHistogram.from_terms\` merges precisely the same weighted joint keys.

For alternative multiset addition and serial convolution, respectively,

    Lift(H + G) = Lift(H).alternatives(Lift(G)),
    Lift(H * G) = Lift(H).then(Lift(G)).

The second identity follows from (P direct_sum \rho(f)).then(Q direct_sum \rho(g)) =
(P.then(Q)) direct_sum \rho(fg), together with q*r positive rational weight multiplication and c*d integer multiplicity multiplication. This is an algebraic native-interface construction, not a claim that the package was installed/executed in this author environment. Phase/signed cancellation, partial actions, state-dependent branch weights, and hidden original path queries require their richer carriers.

A dense \`Affine\` representation adds 2nD+D^2+D rational scalar slots per term compared with dimension n (counting the linear matrix and translation vector); for n=2,D=35 this is **1,400** slots. The observer-only update can instead be stored as D row descriptors, each either an input-coordinate selector or a literal 0/1. Row-descriptor composition takes O(D) selector operations; its entries and composed constants remain 0/1. Dense matrix or general Fraction arithmetic costs are separate. This explains why preserving a native interface does not require materializing dense blocks for every intermediate operation.

## Exact finite validation

Code: \`R201_binary_affine_joint_observer_check.mjs\` (pure descriptor, Boolean and BigInt reference; no physical numerical model and no classical trigonometry). Stored data: \`R201_verification.json\`.
Six parameter models, including nonuniform labels and k=0/L=0 degeneracies; 1,374 words enumerated, 58 distinct reachable states and 58 distinct affine actions; equality of F and of affine maps checked in both directions, affine zero-orbit readout checked, and 1,800 fixed-seed ordered composition checks. Formula (R200.1) is cross-checked with each exhaustive state count; independent BigInt substitution for X6 gives 1,407,685 and D=35. All checks PASS. Symbolic argument covers all a,k,L and all fields, not merely these finite tests.

\`R201_native_brc_joint_observer_check.py\` is a direct runnable integration probe against the real \`Affine\` and \`EffectHistogram\` imports, with Fraction-based positive weights and physical block actions. It is supplied for use in the installed project; its execution status in this run is **NOT_EXECUTED** because the local Python environment lacks \`enterprise_math\`.

## Next scientific frontier

1. Execute the native package probe under the frozen source pin, validating exact package outcomes and branch/path identity carriers.
2. Determine tighter faithful affine dimension bounds between the 21-bit orbit lower bound and this 35-coordinate constructive upper bound over F_2 for a=84,k=6,L=2.
3. Measure construction, input conversion, composition, canonical serialization, size and integer/rational bit costs for dense \`Affine\`, row-descriptor lift, and R200's 21-bit rank codec. Retain the original full provenance wherever the requested future operation does not descend through F.

Control/provenance: Independent portable scientific material; no formal TASK CLAIM, Result, Review, P000 modification, or native deployment asserted.