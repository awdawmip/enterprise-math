# RP12-REPLICA: repeated-coordinate carriers and diagonal rounding

Progress-Event-ID: RP12-REPLICA-C971348E-20260928
Status: AUTHOR_DERIVATION / STATIC_SOURCE_INSPECTION / LOCAL_VALIDATION_PENDING / UNREVIEWED / NOT_ADMITTED
Global read snapshot: c48036ef0431c6f6b8f0224dec0995e6c7981a08
EM scientific/control intake: 69252ec43e972d8f178e51349627b1e00f8a41d7
Publication preflight: 957447513c6ccbef47002e87801d428cf1e45d6f
Parent implementation: RP11-CLOSED engine SHA256 120a8cd500711ac1b6a675e167a87547c6834e3370fe99b04ff0e5347f48430e.
Parent archive recorded SHA256: 2c262feaff7663023f2723233a50db3c7e1625e0b16b8e0990707722531ce211. The archive was NOT rehashed or extracted successfully in this turn.

## 0. What was actually read and what was not executed

The complete attached RP11_CLOSED_研究报告.md, RP11_CLOSED_Proof.md and RP11_CLOSED_BankCertificate.json were read through Files. The certificate explicitly contains all13 complete61-coordinate basis arrays, their Gram, gate columns on that13-space, rank residuals and source information. The source research note at the intake commit was also read. Parent claims are consumed at their existing author-executed/not-admitted strength, not newly independently accepted.

All three local execution routes attempted in this turn (container, analysis Python, visible Python) returned ClientError. No new BRC numerical call, gate-image test, computed output law, timing run, archive extraction, byte-hash verification or new runtime ZIP is claimed. The results below are explicit algebraic derivations and a static comparison of the published basis arrays. In particular, the pending full-carrier gate binding in section3 must not be silently promoted to a passed implementation test.

P000 is unchanged. Coordinates below are ZERO-BASED INTERNAL AMBIENT MODE INDICES, not work labels or additional native spatial axes. All work labels, signs, exact dyadic scales, ordered actual b12 gate identities and coherent collision rules remain.

## 1. An exact factorization already visible in the parent basis

Write the parent's basis as E with13 columns and ambient61 rows. Direct inspection of EVERY published column gives

    E[3,:]=E[2,:],
    E[15,:]=E[14,:],
    E[17,:]=2 E[14,:],
    E[k,:]=0 for k>20.

These are relations of the fixed complete basis, not a statistical fit, current-readout equivalence, or deletion of work labels. They imply the same identities for every x=Ec.

Let I18=(0,1,2,4,5,6,7,8,9,10,11,12,13,14,16,18,19,20). Index y by these representatives. Define the injective replication map H18 by

    x_i=y_i for i in I18;
    x_3=y_2; x_15=y_14; x_17=2y_14;
    x_k=0 for k>20.

H18 has18 independent columns of disjoint supports. Its exact induced metric W18=H18*H18 is diagonal: weight2 at representative2, weight6 at representative14, and weight1 at each of the other16 representatives. Therefore

    Q(H18 y)=sum_i w_i y_i^2,
    J(H18 y,H18 v)=sum_i w_i y_i v_i,
    sum_i w_i=24.

Let B be E restricted to rows I18. Then E=H18 B and

    G=B* W18 B.

This last identity is exact for the EXISTING13-coordinate state and does not depend on extending the gates outside that13-space. It provides an immediate same-target norm/pairing implementation candidate: evaluate the18 linear forms Bc, then use the diagonal metric. Parent basis entries are zero or powers of two, so these linear forms use signed sums and shifts. This is18 squares after linear-form evaluation instead of the parent's68 nonzero upper-triangle weighted Gram terms. The linear forms, temporary bit lengths and memory traffic are real costs; no wall-time advantage follows from the square count alone. No new hot kernel was executed.

The18-dimensional image of H18 is LARGER than the minimum13-dimensional linear invariant space. A nonminimal carrier can have a simpler metric and a quantizer with a cheaper safety proof. Dimension minimization and arithmetic-cost minimization are different objectives.

## 2. A19-coordinate exact-Q candidate, versus the18-coordinate new target

Define I19=(0,1,2,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20). H19 repeats only x3=x2 and x15=x14, leaving coordinate17 independent. W19 is diagonal with weights2 at2,14 and1 elsewhere; its weights sum to21.

For the inherited common-shift, sign-preserving, coordinatewise toward-zero Q_K, duplicate equal coordinates remain equal. Removing only exact duplicate coordinates leaves the maximum magnitude and common two-adic factor unchanged. Consequently Q_K H19=H19 Q_K(rep), provided the same original shift/canonicalization convention is used. Norms and pairings must use W19, not unweighted representative counts. Once section3's full-gate binding is verified, H19 gives a same-target implementation of the original21-coordinate Q16 dynamics and can preserve full decoded rows and identical random-tape behavior. This is an unexecuted quotient proposal, not a new benchmark or a proof of minimal nonlinear dimension19.

The extra scaled equality x17=2x14 is NOT generally preserved by original Q_K. Interface counterexample, not asserted reachable and not newly run through a BRC observer: with only (x14,x15,x17)=(3,3,6) nonzero and K=2, original common shift1 gives physical values(2,2,6). Thus x17=2x14 fails. In contrast H18 retains representative y14=3 at K2 and reconstructs(3,3,6).

Therefore18-representative rounding is a NEW approximate target. It cannot be called an implementation-equivalent optimization of the old21-coordinate Q16. Its error is estimated separately below. The19 duplicate-only proposal and18 scaled-copy proposal must remain distinct in code, evidence and timing.

## 3. Gate closure lemma and the explicit pending source binding

The following sufficient lemma explains when the larger carriers remain closed. Let U=image(H) for H18 or H19. If every full actual gate has (T-I)V contained in S13=span(E), then T(U) is contained in U, since S13 is contained in U. If T is norm-preserving, it induces an exact W-isometry on the representative carrier. Equivalently, closure follows when the actual gate is an ordered composition of rank-one reflections with update vector z in U and coordinate operations supported on e0/e1.

For one reflected component

    R_z x=x-2z J(z,x)/Q(z),

write z=Hv. Then

    R_z(Hy)=H[y-2v (v*W y)/(v*W v)].

The same operator order, signs, denominator convention and original b12 parameters must be preserved. Coordinate sign changes/quarter turns on modes0,1 stay within either carrier. An actual same-root square is the same ordered composition, not a nominal phase simplification. No classical pi/trigonometric or ideal-QFT reference is introduced by this coordinate identity.

The RP11 proof identifies the inherited gates as QuarterTurn, same-root power, and rank-one FixedRotor; their root tails come from the stated E. However, the attached gate-column certificate alone only checks T on13 basis vectors. It does NOT by itself determine how an arbitrary full orthogonal operator acts on S13-perp. Since local source extraction failed, this turn does not certify the whole installed FixedRotor implementation on all18/19 representative basis vectors. Before execution/admission, inspect the exact parent gate source, establish the range/reflection condition, and verify full intertwiners T H18=H18 T18 and T H19=H19 T19, including inverses. A malicious/different action on the complement could pass the old13-column checks while violating a larger-carrier claim.

Thus section1's norm factorization is unconditional relative to the displayed E. The19 same-target sampler and18 new-target sampler in this note remain conditional on this expressly listed full-carrier gate binding. Neither sampler has been implemented or run here.

## 4. Diagonal hard-mantissa quantizer: no radial multiplier

On either diagonal positive metric W, store a representative row y=n*2^e, with exact exponent e. For K>=1 and nonzero integer tuple n, put

    b=max_i bit_length(abs(n_i)); s=max(0,b-K);
    q_i=sign(n_i)*(abs(n_i)>>s);
    z=q*2^(e+s).

Use magnitude shifts and restore signs; Python's arithmetic right-shift of a negative integer is NOT the prescribed toward-zero map. Zero input returns canonical zero. Optional exact common two-adic normalization does not enlarge the stored mantissas. A maximal component survives, so no nonzero row is deliberately erased, and every retained integer has at most K bits.

For each coordinate, z_i has the same sign as y_i and no larger magnitude. Since W is diagonal and positive,

    Q_W(z)<=Q_W(y),
    Q_W(y-z)<=Q_W(y)-Q_W(z).

The second inequality follows coordinatewise from a^2-b^2-(a-b)^2=2b(a-b)>=0 for 0<=b<=a, then multiplication by w_i and summation. Unlike the dense-Gram coordinate truncator, no radial correction or fixed factor(1-eps) is needed for contraction.

If s>0, each coordinate error is less than2^(e+s), while Q_W(y)>=2^(2e+2b-2) because min(w_i)=1. Therefore

    ||y-z||_W / ||y||_W < sqrt(sum_i w_i)*2^(1-K).

For H18 this is sqrt24*2^(1-K)<5*2^(1-K); for H19/active21 the same conservative coefficient5 is valid. If s=0 the error is zero. This is a symbolic all-input certificate on the stated carrier, not a measured typical error.

The runtime candidate no longer needs repeated Gram scoring to decide whether this particular quantizer contracts. Exact branch/acceptance masses are still required; validation still must compare the bound, full decoded rows, signs and scales. Raw gate images, products, probabilities, work labels and audit material are not K-bit objects. In particular, clipping representatives at K bits can decode x17 with K+1 bits.

## 5. Whole-history error and exact mass correction

Assume the full-carrier gate binding in section3, standard initial e0, the same b12 library through level16, the original modular work-label permutation, and original temporal ordering. Perform the diagonal quantization at every nonterminal two-arm boundary; do not quantize the terminal boundary.

For a chosen bit with prequantized total mass A and postquantized mass C<=A, retain the inherited complete-attempt mass correction C/A. A rejection terminates the WHOLE attempt and restarts the initial state. Leaving the current latent label in place and locally retrying is not this target. Induction gives surviving history mass equal to its newly defined raw field norm squared; normalize surviving terminal masses to get the target distribution.

Let eta_K=5*2^(1-K)<1. Every history obeys the same row error bound and contraction. After s=t-1 such boundaries, the inherited direct-sum argument gives

    TV(P18,K, P_exact_same_bank)<=min(1,s*eta_K),
    Z18,K >= (1-eta_K)^(2s).

For completeness, if V is the unit exact final history vector and U the subnormalized approximate vector, local relative error and contraction give ||V-U||<=s eta_K. Writing u=U/||U|| yields 1-|<V,u>|^2 <= ||V-U||^2; hence the coarse classical readout TV obeys the same bound. No assumption that nonlinear truncation is nonexpansive between arbitrary pairs of approximate states is used.

The original active21 K16 target itself obeys eta_old<=5/32768 by the same dimension-based argument (a sharpening of the earlier conservative8 constant, not a new simulation). Thus for t16:

    K18: TV(new18,old21-K16) <= 375/131072 < 3/1000;
    K16: TV(new18,old21-K16) <= 75/16384 < 1/200.

Both use a common unquantized same-bank reference and the triangle inequality. They compare to the no-extra-sharing oldQ16 target, not the RP9 two-compression target. For any unchanged exact factor-verification event G, the absolute event-probability difference is at most this TV bound. A bound below0.005 does NOT mean99.5% factoring success. Current b12 bank versus b64/ideal phase error is separate, as are work-label cardinality, query complexity, cold compilation and expected time to a verified factor.

The K18 row bound is5/131072<2^-14, matching the previous strict per-row tolerance without a radial scale. The K16 alternative uses a larger local tolerance but still has the stated global comparison bound. Neither configuration has new probability or timing data in this turn.

## 6. Exact metric implementation versus a changed target

There are THREE separate acceptance units:

A. Existing13 state/quantizer, replace c*Gc by sum_i w_i(Bc)_i^2. All outputs, quantizer decisions and random tapes must remain identical. Costs of Bc formation and temporary width count.
B. Same oldQ16 target, replace21 coordinates by19 duplicate representatives. Bind complete gates and canonicalization; decoded fields and random tapes must remain identical.
C. New18 diagonal target at a declared K. Bind complete gates, prove/test new quantizer, compare full finite laws, survival and factor events to old21. Different random paths are possible; it is NOT a same-tape optimization of oldQ16.

Do not conflate A/B exactness with C approximation. No new timing improvement, total-memory reduction, cold-start improvement or general classical Shor complexity bound is claimed. More stored coordinates can reduce metric complexity; whether18 is cheaper than13 or21 requires execution. The given18 construction is not claimed to be the smallest or optimal diagonal carrier.

## 7. Next executable finite checks, not completed evidence

1. Reuse the parent ZIP only after size/hash verification. Preserve all parent bytes. Read exact gate source before binding the reflection/range lemma.
2. Verify H18/H19 maps and E=H18 B against the actual certificate; use original positive BRC Gram/norm witnesses for representative weights and selected complete inputs.
3. Check both directions of all15 gates on18 and19 basis vectors (1110 proposed full-image comparisons in total). This count is a PLAN, not an executed result.
4. Test zero, negative mantissas, power-of-two endpoints, common normalization and scaled-relation failure. Test fixedK bounds and exact masses without assuming scalar sign cancellation proves whole-row cancellation.
5. First benchmark exact metric factorization A and duplicate quotient B against frozen parent records. Then run C on predeclared inputs/seeds and full diagnostic laws, separately reporting preparation, retained/temporary bits, labels, acceptance and time to verified factor. Preserve slow results.

## 8. Provenance, control and persistence

Parent exact source: research_notes/HEARTBEAT_RP11_CLOSED_120A8CD5_20260927.md at 69252ec43e972d8f178e51349627b1e00f8a41d7.
Attached certificate file identity: file_000000008ba48211ab67c7941f25d025; complete JSON was read, not generated here. Full report/proof identifiers: file_00000000c7288211a7501942dbac040f and file_000000005e788211992e94eb364324e2.

General invariant-subspace reduction and amplitude-query sampling are prior art. Official abstracts checked: Kumar/Sarovar arXiv1406.7069 and Bravyi/Gosset/Liu arXiv2112.08499. No full-text novelty audit, inherited external complexity guarantee or world-physics promotion is claimed.

Same logical conversation chat-stage101-c971348e64294a5882dfc50fcc8217f1. This turn's read-only status request status-rp12-replica-c971348e-20260928-01, private bridge issue2562, returned matching SUCCEEDED/0.6.8 with research_authority_granted=false, platform_session_attested=false and the original start binding stage101-session-c971348e-02. No new RA, claim, formal run/Result, review or native final_allowed is asserted. Publication of this draft is provenance, not admission.

GitHub text creation and native Google Docs editing are available even though container/Python execution failed. This note is intended as additive noncanonical research capture. No current runtime archive, numerical source hash or execution receipt is invented. The Drive mirror and journal are recorded separately after their actual readbacks. Existing source files, sharing permissions and schedules are unchanged.
