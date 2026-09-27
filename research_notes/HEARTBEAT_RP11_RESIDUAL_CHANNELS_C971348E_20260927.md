# RP11：最小残差通道与质量加权增广

Progress-Event-ID: RP11-C971348E-20260927-RESIDUAL-CHANNELS-01
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_SYMBOLIC_DERIVATION_ONLY / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: a5db9bde552b24f58112dbd8ad6bff181e9d411f
EM control read: d1bbde635c9236c3b922e2eca64121600b1e19d5
Publication preflight: e94096e43b6a46c5d76d1bf4212cdb583e7a8968
Own logical conversation: chat-stage101-c971348e64294a5882dfc50fcc8217f1
Research-Activity-ID: UNKNOWN / REGISTER_PENDING; no new CLAIM, formal run, Result or independent acceptance.

## 0. Frontier and actual execution status

This note continues the attached RP9 report/proof and the read-back Google Doc “RP10：固定 Gram 演化与双行抽样（证明稿）”, document id 10kwKcPvHfnNi5dp4g87MiefRgXGNntmcbbx2tmEiiH0. RP10 already gives C, A, D, the direct-coordinate target, its two-row sampling proof, and leakage/coordinate-error composition. Those are antecedents, not new discoveries here. RP9's 85-row and 512-outcome experiments are not repeated or counted as new evidence.

This turn container.exec, analysis Python and user-visible Python each returned ClientError before a usable local result. There are ZERO new numerical BRC experiments, rank evaluations, timing observations or execution checks in this note. All statements below are conditional algebraic propositions with proofs. No actual value of rank(D), a usable leakage threshold for the RP9 bases, or performance benefit is reported. Remote text persistence is not a scientific runtime check.

P000, the actual typed BRC-only arithmetic requirement, signs, exponents, complete work-label incidence and mathematical admission boundaries remain unchanged. F* below denotes the adjoint of the already declared complete61 BRC pairing J. It does not import a different native spatial metric or create new native spatial axes. A later execution must actually use the certified BRC gates and Gram interfaces; ordinary numerical matrices cannot be substituted and renamed BRC.

## 1. Setup and inherited leakage identity

Let H be the finite 61-mode real carrier with positive-definite BRC pairing J and norm Q. Let F have r independent columns, S=range(F), G=F*F>0. Let T be one actual certified norm-preserving ordered word within a linear stretch, not a word obtained by moving a nonlinear Q_K boundary. Define

    C=F*TF;  GA=C;  Pi=F G^{-1} F*;
    E=(I-Pi)TF=TF-FA;
    D=E*E=G-C^T G^{-1}C.

These identities are inherited from RP10. In particular F*E=0 and 0<=D<=G. G^{-1} is mathematical notation; solves may use the already established triangular interfaces rather than store an inverse.

## 2. New finite augmentation proposition

Set q=rank(D). Then

    dim(S+T S)=r+q,   0<=q<=min(r,61-r).

Thus precisely q extra linear coordinates are necessary and sufficient to represent EVERY vector in S and EVERY image T x with x in S, retaining complete vectors. This minimality concerns linear full-state representation of S+TS. It is NOT a lower bound for every task observation, every nonlinear codec, or a particular single input field.

Proof. Since E*E is a Gram matrix, ker(D)=ker(E): c^T D c=Q(Ec). Therefore rank(D)=rank(E). The decomposition TF=FA+E and F*E=0 give S+TS=S direct-sum range(E). Its dimension is r+rank(E). Any linear representation containing both S and TS must have at least this dimension; their span attains it.

No measured claim “seven old coordinates plus one new coordinate suffice” follows until the actual D has been evaluated. The bound can grow to the full carrier.

## 3. Construct the augmentation with selected actual gate images

Choose an index set I of k columns for which D_II is positive definite. Let E_I and (TF)_I denote those columns. Define

    K_I = solve(D_II, D_I:),
    R_I = D-D_:I K_I.

Then R_I>=0 and is exactly the Gram matrix of the component of E orthogonal to range(E_I). For all c,

    Q((I-Pi_I)TFc)=c^T R_I c,

where Pi_I projects onto S_I=S+range(E_I).

To avoid imposing long orthogonal basis vectors as the stored representation, use

    H_I=[F,(TF)_I].

It spans the same S_I. Its complete Gram is

    G_I = [[G,C_:I],[C_:I^T,G_II]].

Its Schur complement in G is D_II>0, so H_I has independent columns. The projected gate image has explicit coordinates:

    Pi_I TF = F(A-A_I K_I)+(TF)_I K_I.

Proof. Projection of E onto E_I is E_I (E_I*E_I)^{-1}E_I*E = E_I K_I. Substitute E_I=(TF)_I-F A_I. Orthogonality to S gives the stated Gram residual. If k=q and the selected columns span range(E), then R_I=0 and the displayed reconstruction is exact for all c. If q=0, use I empty and no new columns.

The basis images TF_I, coefficients, solves and their denominators may still be long. This proposition does not assert reduced bit payload or time. It merely avoids a requirement to store a full 61-mode orthogonalized basis.

## 4. Several words may share leakage directions

For a finite prepared list of actual words T_1,...,T_m, set E_j=(I-Pi)T_j F and stack E_all=[E_1,...,E_m]. Its block Gram has entries

    D_all[i,j]=F* T_i* T_j F-C_i^T G^{-1} C_j.

Then

    dim(S+T_1 S+...+T_m S)=r+rank(D_all).

This follows from the same orthogonal direct-sum argument. The required channel count is not automatically the sum of the separate ranks, nor their maximum: overlap of leakage directions matters and is recorded in the cross blocks.

This only contains the listed images of the ORIGINAL S. It does not establish invariance of the augmented space under repeated arbitrary words. For repeated use, certify the action on newly added directions or iterate the closure construction. RP10's joint-invariant-space route remains an antecedent. Nonlinear original Q_K boundaries can break a linear invariant subspace and are not erased by this argument.

## 5. Exact field-weighted leakage at a two-arm boundary

Assume the CURRENT complete field is accurately represented by x(w)=F c_w, with all signs and exact scales. Existing approximation in this field is a separate error. A basis-external escape row must be included exactly in an enlarged basis, or the following whole-field formula is inapplicable; it cannot be silently omitted.

Define the coefficient second moment and current mass

    W=sum_w c_w c_w^T >=0;    M=tr(GW)>0.

For actual modular bijection P and bit sign s_b, the raw child is

    a_b(w)=[F c_w+s_b T F c_(P^{-1}w)]/2.

Projection onto S_I has error only in its acted arm:

    Q((I-Pi_I)a_b(w))=c_(P^{-1}w)^T R_I c_(P^{-1}w)/4.

Summing over BOTH bits and ALL work labels, and using the bijection, gives

    ell_I = (1/2) tr(R_I W);
    theta_I = ell_I/M;
    total projected child mass = M-ell_I.

Because 0<=R_I<=G, 0<=theta_I<=1/2. The corresponding operator bound R_I<=epsilon^2 G implies theta_I<=epsilon^2/2, but the exact field-weighted theta can be much smaller. A norm bound for every conceivable coefficient vector is stronger than needed for this particular known field.

W is not a replacement for work-label incidence. In particular raw bit probabilities depend on the cross-label term sum_w c_w^T C c_(P^{-1}w), which is not determined by W alone. Keep the actual labels or a separately proved sufficient incidence representation. Constructing W may require O(number_of_labels*r^2) arithmetic and access to the field; this is a CHECKPOINT-SIDE certificate, not a free point-query operation and not a statistic estimated from one sampled latent path.

## 6. One more channel: an exact gain formula without spectral decomposition

At any selection stage let R>=0 be the current residual Gram. For a candidate column j with R_jj>0, appending that remaining residual direction gives

    R_new=R-R_:j R_j:/R_jj.

Hence the decrease of the weighted residual is exactly

    Delta_j = tr((R-R_new)W)
            = (R_:j)^T W R_:j / R_jj >=0.

The decrease in two-arm lost mass is Delta_j/2. One may choose the largest Delta_j among available columns, with a fixed index tie-break. This is a deterministic, exact best single-step gain WITHIN THIS COLUMN CANDIDATE SET for the fixed W. It is not a globally optimal k-channel choice, not a bit-cost optimum, and not a factor-success maximizer. Zero diagonal means a zero column for a PSD residual and is skipped. Update W only when the actual represented field changes; do not pretend an old covariance remains valid.

After each chosen column, recompute/verify the Schur residual and theta. Stop when the declared weighted-loss budget is met. A hard column cap does not guarantee the budget can be met. If insufficient, preserve the complete state or report the resource-limited attempt as incomplete, rather than claiming both fixed memory and fixed accuracy. No inverse of a full 61x61 operator or eigendecomposition is algebraically needed for this selection; G solves, current r-dimensional products and selected pivots remain real work.

This is a field-weighted pivoted-Gram/Schur construction, closely related to established partial Cholesky/Nystrom methods. Worldwide novelty is not asserted.

## 7. Sampling and multi-boundary error: conditional contract

For a projected new target, select the original bit using its raw mass and accept with projected/quantized child mass divided by raw mass. Whole-attempt rejection is required. A point-query sampler additionally requires a fixed, history-determined basis/selection and consistent row function; a private walker's earlier query order cannot choose the basis. A full-field sampler may use the same child-mass ratio. Zero-mass branches are handled without division.

Let an in-subspace Gram quantizer have nonincreasing norm and relative squared error <=tau_i^2 on each projected row. Projection loss and in-subspace error are orthogonal. If every history at depth i verifies theta_h<=theta_bar_i, then the total one-step squared error is bounded by

    beta_i M,
    beta_i=theta_bar_i+(1-theta_bar_i)*tau_i^2.

The existing RP10 direct-sum argument therefore yields, for the same normalized initial field in the represented space,

    TV(new accepted law, same-bank uncompressed linear law)
       <=min(1,sum_i sqrt(beta_i)),
    Z >= product_i[(1-theta_bar_i)*(1-tau_i)^2].

These are inherited propagation/sampling arguments with the newly certified field-weighted loss substituted, not new numerical results. Requiring beta_i<=b_i is equivalent to theta_bar_i<=(b_i-tau_i^2)/(1-tau_i^2) when b_i>=tau_i^2 and tau_i<1. Error guarantees must hold for every relevant history or use a separately proved ensemble weighting; one favorable sampled path is insufficient.

All current labels and signed coefficients remain. Projection may legitimately produce a zero child through the newly declared dynamics; this is not a promise of unchanged future support. The old coordinatewise61 Q_K is not equivalent to a new small-coordinate quantizer. Preserve it at its original place for an old-target implementation, or explicitly account for changing target. Initial compression, actual gate-bank approximation, candidate coefficient error, restarts and exact factor verification remain separate costs. A higher Z alone is not a factor-success guarantee.

## 8. What has and has not been accomplished

New symbolic units: minimal one-word augmentation r+rank(D); selected actual-image reconstruction; joint-word leakage Gram; exact coefficient-field-weighted loss; exact marginal gain of one residual channel; precise insertion of these certificates into the inherited sampling/error contract.

Not accomplished: actual C or D for the RP9 7/8-column bases, any observed rank/channel count, new full probability law, code execution, compression ratio, timing, finite-spectrum certificate, low-cost general membership, polynomial classical Shor, or physical/hardware advantage. Even a mathematically small channel count can produce long integers and expensive fitting. The next runtime must count those costs, labels and temporary matrices.

A bounded next execution should consume the already frozen RP9 bases and the FIRST declared next actual phase-word for each checkpoint. Obtain TF,C,D with the actual BRC engine, independently check D=E*E, find pivots, verify reconstructed full columns and W-weighted losses. Compare k=0..rank(D) without post-selecting the favorable word. Only then consider a new full finite tree or an end-to-verified-factor benchmark. Do not rerun old RP9 results as discovery.

## 9. Source, literature and recovery records

Source-only inputs include attached RP9_Proof.md and RP9_研究报告.md; the cloud RP10 document id above was actually read this turn. The current cloud RP10 already states the fixed-Gram direct sampler, the orthogonal composition of leakage and coordinate error, and the common-invariant-space antecedent. Their source framing is retained.

Official external metadata/abstracts checked: Chen, Epperly, Tropp, Webber, Randomly pivoted Cholesky, arXiv:2207.06503 / DOI10.1002/cpa.22234; and the arXiv metadata for Schaub/Zaspel, Variational Free Energy Pivot Selection for Pivoted Cholesky, arXiv:2606.01821. Their performance and optimality results are NOT transferred to this BRC implementation. No full-text novelty-completeness review.

A dedicated standard arxiv/paper_search was actually submitted to private KQB issue2553, batch cde25cc1-57a6-44e9-92a0-1e8f2d4b89d7, turn2d8171aa-4389-4768-b99d-533c8c36ce41, query '"pivoted Cholesky" "weighted" "projection"', n3. Intake request_sha2560746aa066dc7f641af70c5d1a9532b43d9d96998b17924847c3dd19f5340b322. The matched result comment5856746118 returned three unrelated titles (topological insulators, eccentricity law, robot programming), child PARTIAL, provider_query_calls_confirmed1, bridge_kimi_llm_calls0, billing unknown. This is RELEVANCE_MISMATCH, not a valid relevant cache and not NO_HIT. The provider's raw return remains in that original private comment; none of those three abstracts supports this proof and none is used as evidence.

Cloud metadata observed, not newly uploaded this turn: RP8/RP9 attachment-version supplements already exist in folder1hz6_Oc5L2_x_gp7OSGKgcCBz6JZSoRbw. RP9 run ZIP id1h76_iUbDx3uJMfiYODB-4t0z44RDX--c, size54755655; RP8 run ZIP id1W7RlQDmxmreiaFmQB_Y0f22a4xJc-OhB, size35840220. Folder listings also show reports, proofs, results, checkpoints and original delivery/pending records. They were not duplicated. No new download-hash or execution replay of those archives was possible, and no earlier branch was overwritten. A request for hash metadata did not expose a hash in the normalized connector response, so only size/identity is claimed.

Recovery request issue2552, request_id rp11-channels-20260927-c971348e-recovery01, actually SUCCEEDED as READ_ONLY local pointer recovery. request_sha256 baa4fdf13a38d72ed4c7a7fca511aa6d825f6e741205b422a415c15e5825c315. Source authority remains unverified, original start stage101-session-c971348e-02, no runs/claims/staging and no mathematical acceptance. No new identity or bypass of old denied actions. Further delivery/Drive and pre-final outcomes are recorded separately rather than predeclared here.
