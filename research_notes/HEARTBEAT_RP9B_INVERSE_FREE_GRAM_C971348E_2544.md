# RP9-B: inverse-free Gram acceptance, exact integer rebasing, and approximate transport certificates

Progress-Event-ID: RP9B-C971348E-GRAM-2544
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_SYMBOLIC_DERIVATION_AND_SOURCE_SUBSTITUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: a668c148c80cf836ff7e520ccb57e8d0e919b731
EM control intake: 2034df3def543e151ef122e8e260d417331de0aa
Publication preflight: 529797f4c3ffee4323d9412ba5e8214e631bd4f2
Research-Activity-ID: UNKNOWN / REGISTER_PENDING

No numerical program ran in this turn. container.exec, python.exec and python_user_visible.exec each returned ClientError. No new BRC runtime receipt, replay, benchmark, probability sweep, byte-count measurement, tested solver or scientific runtime bundle is claimed. The two integer examples below are exact algebraic substitutions into already supplied BRC Gram data, not new core executions. This is a noncanonical provenance note, not a formal Task/Result, independent review or promotion. P000, b12 bank, full signed 61-mode carrier, exact exponents, label incidence and all original Q_K boundaries remain unchanged.

## 1. Recovered frontier and a real source-version distinction

The current conversation attachments are RP8_Proof.md, RP8_研究报告.md, RP8_PACKED_CHECKPOINTS.json and RP8_DELIVERY.json. Their delivery record identifies RP7 scientific parent d2d2c685a89598e2c729885ae1bd921a2d328d1b and the runtime ZIP of 35840220 bytes, recorded SHA256 d680a1d633f32df579ee8fa27e3281b6a98d1cb72d82ad36a66ae4ab516d94a0. This turn read the proof/report/packed JSON through Files. The ZIP hash is a source-reported identifier, NOT a hash rechecked this turn.

Attachment identity: proof file_00000000273c820baf5b6adb3e9355c2; report file_000000008f80820ba1b3c06afd898e76; packed fixture file_000000000e88820b900184c4537001e9; delivery file_000000008b80820b9c55eacc2fb07320. Attachment payload records are N253:10502 original/9466 with Gram and flags, N143:7902/7329, with N143 label126 escaping. These are inherited reports, not new measurements.

Live Drive also contains a DIFFERENT RP8 folder/version, 1kuU8dq9ex7jS199c1_EY6QADOG3Iutqf, suffix a71213a7. Its ZIP 1fm-e34kV8ioCTDHj2uacWV6NHQgOiyKX has metadata size 33494271, not 35840220. This distinction must not be silently reconciled by replacing either version. This turn has not established their byte ancestry or equivalence.

An existing RP9 transported-frame derivation was recovered and consumed, not rediscovered:
https://github.com/awdawmip/enterprise-math/blob/7c0fc0e9a8d5658929c121c595d670dd97443bb4/research_notes/HEARTBEAT_RP8_RECOVERY_RP9_TRANSPORT_C971348E_2541.md
Its immutable blob is b4be21a69dc7e18b9827650c9e3b376d90130601. Its Drive mirror is document 1FVIrctxN5Ffrgfd0HK7pCtvEs9jAA5FNNZbPgxTV3PA in folder 1BzNW9cdQ6ZZvAplJCYK1R0NIUKm8yVYj. It already proves joint-frame raw updates and optimal-projection leakage using G^-1 H. It contains no executed transported-basis benchmark. This note is RP9-B, an additive continuation.

Inherited vendor identity from RP8: bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py; blob 4e6b3132580e3cd70a20a0d8bd4d28792b961afb; recorded SHA256 7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26. Runtime identity must be verified before implementation replay; no present execution is implied by inheriting it.

## 2. Acceptance does not need the exact least-squares coefficients

Q and J are the inherited full BRC quadratic form and signed pairing. Let F have r actual full-mode columns, G_ij=J(f_i,f_j), R=Q(x)>0 and b_i=J(f_i,x). For ANY dyadic candidate d define

    A=b^T d, Y=d^T G d,
    E(d)=R-2A+Y=Q(x-Fd).

This identity is already present in the RP8 proof; the new solver contract uses it as a stopping/acceptance test, rather than first requiring c=G^-1 b. It remains valid for a dependent frame, provided G is the actual Gram, not a fabricated positive matrix. No inverse, optimal coefficient, condition number or E_perp is required to test a particular candidate.

Reuse RP8's established radial rule, not a new discovery: if A<=0 or Y<=0, do not accept that candidate. Otherwise take a positive inward dyadic lambda <= min(1,A/Y), put z=lambda Fd, and evaluate

    Q(z)=lambda^2 Y,
    E_lambda=R-2lambda A+lambda^2Y.

Cauchy-Schwarz A^2<=RY implies Q(z)<=R. Moreover

    R-Q(z)-E_lambda=2lambda(A-lambda Y)>=0.

Accept only if E_lambda<=beta R, beta<1; otherwise improve the candidate or keep x exactly. Nonzero accepted input rows remain nonzero. A candidate proposer may be approximate; it cannot override the exact certificate. This is not permission to substitute a non-BRC phase engine. Gram and b construction, scalar verification, reconstruction and escape storage must all be charged.

A direct small normal-equation residual is NOT by itself a relative field-error certificate for ill-conditioned G. Use E_lambda itself. Computing it by nearly cancelling floating-point values without certified error is not the proposed interface.

## 3. Exact integer changes of basis before any new approximation

For integer k and i!=j, replace f_j by f_j-k f_i. Write U=I-k e_i e_j^T. Then det(U)=1 and U^-1=I+k e_i e_j^T. Transform

    F'=FU, d'=U^-1 d, G'=U^T G U, b'=U^T b.

Consequently F'd'=Fd, d'^T G'd'=d^T Gd, b'^Td'=b^Td. Every decoded row, sign, relative exponent, label and future deterministic operation is unchanged. Existing radial scales and escape rows are retained. There is ZERO added approximation until any subsequent coefficient rounding. Do not round d' merely because its bit length grew and still call the change exact.

Choosing k as a nearest integer to G_ij/G_ii (with a fixed tie rule) gives

    Q(f_j-kf_i)=G_jj-2kG_ij+k^2G_ii,
    |J(f_i,f_j-kf_i)|<=G_ii/2,
    Q(f_j-kf_i)<=G_jj.

This is an elementary integer basis operation, not a claim of a new LLL algorithm, global lattice reduction or a condition-number guarantee. Updating all stored coefficients costs O(S) scalar operations for S labels; F and Gram also require updates, and integer bit costs count. A smaller basis vector alone does not imply a smaller complete payload. A practical accept rule must compare basis+Gram+all coefficients+exponents+escapes+metadata before committing an exact rebase. Strict decrease of that integer-valued payload at a fixed checkpoint ensures only finitely many accepted reductions, not cheap discovery or bounded intermediate memory.

### Exact source-derived witness A: attached N143, zero-based indices i=1,j=7

Stored Gram entries:

    G_11=3298174993, G_17=3301492493, G_77=3304859401.

Use k=1, so f'_7=f_7-f_1. The nonzero-coordinate prefix (remaining 40 coordinates are zero) is

    [76,-65,-3,-3,-8,-7,-8,-18,-26,-5,-9,-11,-93,-171,-3,-3,-3,-8,0,0,-2].

The stored Gram identity gives

    Q(f'_7)=3304859401+3298174993-2*3301492493=49408.

Maximum absolute basis component changes from 56933 (16 magnitude bits) to171 (8 bits). For every packed nonescape row set d'_1=d_1+d_7 and d'_7=d_7; all other coefficients and radial scales stay fixed. Label126 remains an exact escape. This is an algebraic reconstruction identity, not an executed updated codec or an assertion of net payload savings.

### Exact source-derived witness B: attached N253, zero-based i=0,j=3

    G_00=1297951293, G_03=-1282804458, G_33=1298330304.

Use k=-1, so f'_3=f_3+f_0. Its prefix (remaining 47 coordinates are zero) is

    [-5245,-768,24,24,65,49,64,91,306,340,70,461,672,1294].

Then

    Q(f'_3)=1298330304+1297951293-2*1282804458=30672681.

Maximum magnitude changes from35133 (16 bits) to5245 (13 bits). Change d'_0=d_0-d_3, d'_3=d_3. No label is deleted. Again no full payload remeasurement, transformed coefficient scan or new BRC core call occurred in this turn.

These substitutions use the attached RP8 packed JSON, NOT the distinct cloud RP8 payload counts.

## 4. A dyadic coordinate-descent proposer with an exact per-step decrease

Freeze the frame and deterministic candidate/bit/iteration budget for a history before private sampling queries. Maintain

    g=b-Gd, E=R-2b^Td+d^TGd.

For a nonzero coordinate residual g_j with G_jj>0, the exact line minimizer is alpha=g_j/G_jj. Generate an inward dyadic increment tau of L>=2 significant bits, with sign(tau)=sign(alpha), |tau|<=|alpha| and |tau-alpha|<=delta|alpha|, delta=2^(1-L). Then

    d'=d+tau e_j,
    g'=g-tau G_:j,
    E'=E-2tau g_j+tau^2G_jj.

Writing tau=theta alpha gives 1-delta<=theta<=1, hence

    E-E'=(2theta-theta^2)*g_j^2/G_jj
          >=(1-delta^2)*g_j^2/G_jj>0.

A deterministic choice maximizes g_j^2/G_jj, using cross multiplication and index ties, not a floating ranking. A and Y can be updated as

    A'=A+tau b_j,
    Y'=Y+2tau(b_j-g_j)+tau^2G_jj.

After Gram/b setup one such proposal/update costs O(r) exact scalar operations and O(r) per-row working quantities besides the shared O(r^2) Gram. It does not store G^-1. If F and x are dyadic, all persistent d,g,A,Y,E remain dyadic; alpha's possibly odd denominator is used only to choose a dyadic step. This avoids a persistent general rational inverse, not all large-integer growth.

IMPORTANT: L-bit increments do not imply L-bit accumulated d. Exponent alignment, residual updates and cancellation can lengthen integers. If d is repacked, evaluate the ACTUAL changed d and exact E again; reject a repack that breaks the declared decrease or final acceptance. Use a deterministic total work/bit cap and exact escape. A run ending without a passing candidate is not success and does not prove that no feasible encoding exists.

For full-column-rank F only, one can quantify the possible slow convergence. Let D=diag(G), mu=lambda_min(D^-1/2 G D^-1/2)>0, and E_* be the least achievable E. Theoretical identities imply

    max_j g_j^2/G_jj >= (mu/r)(E-E_*),
    E_next-E_* <= [1-(1-delta^2)mu/r]*(E-E_*).

Proof: write e=d-c and h=D^1/2 e. Then E-E_*=h^T Hh and sum_j g_j^2/G_jj=h^T H^2 h>=mu h^THh, H=D^-1/2GD^-1/2. No numerical eigenvalue or inverse is needed for the algorithm; this rate is a proof-only diagnosis. mu can be tiny. No bounded fast convergence is inferred for the actual highly conditioned RP8 bases. A redundant frame still has the decrease identity but not this positive-mu bound on its full coefficient space.

The existing RP8 interface counterexample illustrates an exact preconditioner: (10,0),(10,1) becomes (10,0),(0,1) under f_2-f_1, with coefficient change (1,-7/8)->(1/8,-7/8). Its Gram becomes diag(100,1) and the represented row is unchanged. This symbolic example is not a new execution or evidence that the actual large frames become diagonal.

## 5. Remove the inverse from RP9's transport proposal as well

The recovered RP9 already defines V=TF and H=F^T V with V^T V=G, and uses the optimal A=G^-1H. Here let M be ANY deterministic short dyadic r-by-r candidate transport matrix; it may be obtained by the preceding proposer on each column of H. Define D_T=V-FM. Its EXACT residual Gram is

    Omega_M=D_T^T D_T
           =G-H^T M-M^T H+M^T G M >= 0.

For the actual modular predecessor label and coefficients c,d, raw bit-b output and proposal are

    a_b=(Fc+(-1)^b Vd)/2,
    y_b=F(c+(-1)^b Md)/2.

Then

    Q(a_b-y_b)=d^T Omega_M d/4.

This is valid without an inverse or orthogonality of D_T to F. Do NOT transfer the optimal-projection statement Omega<=G: for T=I,M=3I, Omega_M=4G. The residual may be large even if M is short. Keeping its accurate Gram is essential.

For a complete coefficient family W=sum_w c_w c_w^T, summing both branches and all actual labels gives total raw discrepancy tr(Omega_M W)/2. This formula does not replace label incidence in sampling and does not guarantee small relative error on a rare conditional child.

A fully inverse-free SUFFICIENT uniform certificate for Omega_M<=epsilon^2G is diagonal dominance of C=epsilon^2G-Omega_M:

    C_ii >= sum_(j!=i)|C_ij| for every i.

Indeed v^TCv >= sum_i(C_ii-sum_(j!=i)|C_ij|)v_i^2>=0. This only requires exact quadratic-form entries/absolute values, but is conservative and may fail even when C is positive semidefinite. No actual RP8 frame passed or failed this new test in this turn. Failure means use a stronger paid certificate or local row acceptance, not infer impossibility.

After the ORIGINAL nonlinear Q_K, evaluate the actual target row q=Q_K(a_b); the transport coefficients remain only proposals. Reconstruct/radially correct against q and apply section2's exact certificate. Do not drop q-a_b or move Q_K to coefficient space. Escaped rows follow the original full-row path. Rank/Gram/T-frame setup, every coefficient update, all labels and scalar bit costs are charged.

## 6. Conditional repeated-checkpoint guarantee, not an executed sampler

If the same K-bit quantizer occurs s times and m additional deterministic compressions each pass Q(q-z)<=beta_k Q(q), Q(z)<=Q(q), or escape exactly, then the existing full-history BRC isometry argument yields

    TV(P_new,P_exact_same_b12) <= min(1,s*rho+sum_k sqrt(beta_k)),
    rho=8*2^(1-K).

This compares to the untruncated SAME actual b12 instrument. Bank-to64/ideal error is separate. Exact integer rebases add ZERO to this bound. A particular new coefficient proposer can define a different approximate target from RP8/RP9; no same-random-tape or direct small RP8-to-new bound is asserted without a separate argument.

If one additionally checks loss Q(q)-Q(z)<=gamma_k Q(q), 0<=gamma_k<1, uniformly at each compression, survival is at least (1-rho)^(2s)*product_k(1-gamma_k). Error<=beta alone must not be silently interpreted as loss<=beta. Without the optional loss guard, use the existing weaker reverse-triangle bound. Surviving output is not a factor: expected time to a verified factor still charges per-trial cost divided by its true success probability, including initialization/rejections and the unchanged exact verifier.

This turn has NOT run multiple successive checkpoint compressions. The conclusion is a testable sufficient contract and exact source-data rebasing witnesses, not a measured fast algorithm, proven universal small rank, cheap point oracle, ridge locator, classical polynomial Shor result or hardware effect.

## 7. Next executable scientific unit and source integrity

On a working authorized runtime, first hash-check the exact ATTACHED d680a1d6 RP8 package or deliberately select and document the distinct cloud version. Do not mix their payload baselines. Verify original core/source pins. Then freeze a work/bit budget before measurements and implement:
1. both listed integer rebases, transform every coefficient, and test exact complete-row reconstruction and actual BRC Gram congruence;
2. inverse-free dyadic residual updates plus radial acceptance, starting from frozen candidates rather than exact inverse solutions;
3. arbitrary-M transport residual and actual BRC two-arm comparisons;
4. a declared short suffix with every original Q_K and complete escape/error records;
5. cost comparison including setup, all unsuccessful iterations, label processing, field reconstruction, certificate storage and verified-factor stopping costs.

Do not repeat RP8's prior grid, stored suffix laws or recovered RP9 transport theorem as discovery. Current absent runtime is a real execution limitation, not proof that this method fails.

## 8. Provenance, controls and external antecedents

Wright, Coordinate Descent Algorithms, arXiv:1502.04759 (primary abstract), https://arxiv.org/abs/1502.04759 . Approximate coordinate minimization and generic convergence are prior art; the specific certificate-compatible update and scope are proved here.
Lenstra/Lenstra/Lovasz, Factoring Polynomials with Rational Coefficients, Mathematische Annalen261 (1982),515-534; primary archival metadata https://eudml.org/doc/182903 . Integer lattice basis operations are not claimed as worldwide novelty; no complete LLL implementation or its performance theorem is imported.
Only metadata/abstract context was checked; no full-text novelty-completeness audit is claimed.

Own logical conversation remains chat-stage101-c971348e64294a5882dfc50fcc8217f1. Recovery2544 request recovery-rp9-gram-c971348e-01 returned SUCCEEDED for local pointers only, source_authority_verified=false, no runs/claims/staging; request_sha256 fd7bb6f6d5055460279dd4ab22f464f9a63fb427c0cc66a636264afa5ce179b9. Original start stage101-session-c971348e-02 is not newly validated. No new identity, RA, formal run/Result or independent review is asserted.

A current attempt to upload the attached RP8 ZIP via its serialized file reference was rejected before upload with validation_error: file_uri must be a connector file reference object returned by a fetch/upload action. This is an actual failed attempt, distinct from the previous absence of an upload action. Native text mirroring is a separate supported route; its completion will be reported only after readback. No archive upload, hash recovery or permissions/schedule change is inferred from text persistence.
