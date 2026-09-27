# RP8 recovery and RP9 transported-frame / leakage certificate

Progress-Event-ID: RP8R-RP9-C971348E-2541
Status: RECOVERED_SOURCE_REPORTS_PLUS_AUTHOR_DERIVATION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: c2802b5ae00d54b75920ee7f2e37b832777c3207
EM control read snapshot: 9102ef5a8285879185ca2d7a20f158f9a798ce1d
Verified predecessor source record: enterprise-math@2e81851d62c869a20b47ae083a24dde1a4c0420c:research_notes/HEARTBEAT_RP7_PROJECTIVE_D2D2C685_20260927.md
RP7 scientific parent: d2d2c685a89598e2c729885ae1bd921a2d328d1b
Recovered RP8 folder suffix: a71213a7; this suffix is NOT a newly verified full Git commit.
Research-Activity-ID: UNKNOWN / REGISTER_PENDING; no new CLAIM, run, formal Result or independent acceptance.

## 1. Recovery must precede rediscovery

The preceding interrupted turn had already uploaded RP8 materials. The current turn first lacked that response and encountered ClientError at container.exec, python.exec and python_user_visible.exec. No new numerical experiment was executed. A duplicated read-only recovery request was rejected as REQUEST_ID_ALREADY_BOUND; inspection found the original request at Issue 2539. It established only the same historical local session pointer, not Source authority. Issue 2541 is preserved as the duplicate rejection; no identity was changed to bypass it.

Current Drive reads recovered:
- Folder RP8_短非正交基与Gram校正_20260927_a71213a7: 1kuU8dq9ex7jS199c1_EY6QADOG3Iutqf.
- Report: https://drive.google.com/file/d/1mzmtOi89j-OQCp2DifIULfIJKUy_gked/view
- Proof: https://drive.google.com/file/d/1nSEy53MccBr0QFnJP2tCf2E0UAi7PJtj/view
- Results: https://drive.google.com/file/d/1TYtpV2HHBWyH3Q283Yhs3WyCaqEv4gfA/view
- Entry: https://drive.google.com/file/d/1f__qGTRA1sLsSjYa8XZlkLNqN0vLNwci/view
- RUN ZIP: 1fm-e34kV8ioCTDHj2uacWV6NHQgOiyKX, metadata size 33494271 bytes.
- Delta bundle: 1DRA46-yOrTa-eUE0QQMED_pUXUcrG5-R, metadata size 2635302 bytes.

The report and proof were read as text. The results backing JSON was fetched and parsed by Files; exact payload/Gram records were inspected. ZIP/delta contents, full hashes, source ancestry and scientific replays were NOT reverified in this turn. The entry describes a standalone runtime, but that description is not a current replay. No new RP8_DELIVERY receipt was found in the six-item folder listing.

Recovered source-reported results, not newly executed results:
- N143/a2/t16 selected 30-row state: original integer payload 7902 bits; short basis 2057 + coefficients 3040 = 5097; explicit Gram 2198; total with Gram 7295. No escapes, rank 8, max basis magnitude 16 bits.
- N253/a2/t16 selected 55-row state: original 10502; basis 1301 + coefficients 5671 = 6972; explicit Gram 1647; total 8619. No escapes, rank 7, four initially norm-increasing rows were repaired. Exact reported max relative squared error 9697851883/2418857433934856192; norm ratio 503534903014759259870469680510413/503551942859604692793950988140544. These match the inspected results fields.
- Same source's inverse-transient payload is 19519/14013 bits for the 30/55-row cases. Its bit convention excludes labels, containers and certificates, and counts exponents. Serialized archive size and RSS are different metrics.
- Source-reported local medians, original versus fitting-plus-Gram observation: N143 .066151412/.173655715 seconds; N253 .158452407/.322129748 seconds. Original pivot-discovery and bank construction were excluded. Thus a local payload reduction was achieved in those records, but not an end-to-end speedup. Other newly reported checkpoints had no with-Gram storage gain.

The recovered RP8 proof ALREADY contains short nonorthogonal bases, coefficient-error Gram identities, inward radial norm repair, exact per-row certificate with fallback, two complete diagnostic laws, and Gram-coordinate next-bit observation. These are consumed, not presented as discoveries of this turn. The current turn's initial radial-repair idea overlaps that completed work.

## 2. Scope of the new RP9 derivation

Everything below is a symbolic derivation for the inherited complete 61-mode signed BRC carrier. Q and J mean its established positive quadratic form and bilinear pairing. T is an actually admitted temporally ordered BRC word satisfying Q(Tx)=Q(x), not a substituted trigonometric or ideal-QFT propagator. P is the actual bijective modular label permutation. P000, physical claims, b12 gate precision, labels, signs and original Q_K boundaries are unchanged.

Let B have r independent full-mode columns and G=B^T B be its BRC Gram matrix, positive definite. For this local phase write the current COMPLETE field U(w)=B c_w, including each exact scale in c_w. Missing labels denote zero only in this complete representation. Escapes outside span(B) require the explicit handling below.

## 3. Exact transport needs BOTH arms

Compute V=T B once per basis column and H=B^T V. By the BRC isometry V^T V=G. Define the redundant joint frame

    F=[B,V], K=[[G,H],[H^T,G]].

For destination w, d=c_(P^-1 w), sign s_b=(-1)^b,

    a_b(w)=(B c_w+s_b V d)/2
          =F * (c_w,s_b d)/2.

Thus raw child construction needs no per-row fit or inverse, and

    Q(a_b(w))=(c_w^T G c_w+d^T G d+2s_b c_w^T H d)/4.

The raw children live in span(B,TB), NOT necessarily span(TB) or span(B). Replacing B by TB alone can discard the direct arm. F can be dependent; the displayed synthesis and Gram identities do not require K^-1. They preserve the exact raw target and add zero approximation before Q_K.

For successive exact raw steps an uncompressed joint dictionary can double its column count. Actual rank is at most 61, but detecting dependencies and constructing a smaller basis has nonzero cost and may lengthen integers. This is not a general bounded-rank or bounded-bit theorem.

## 4. Exact leakage from reusing the OLD subspace

Set

    A=G^-1 H, R=V-B A,
    Omega=R^T R=G-H^T G^-1 H.

B^T R=0 and 0<=Omega<=G in the quadratic-form order. Define

    g_b(w)=(c_w+s_b A d)/2.

Then

    a_b(w)=B g_b(w)+s_b R d/2,
    Q(a_b(w)-B g_b(w))=d^T Omega d/4.

This is an exact residual identity for the actual BRC word. G/H alone determine it. It does not require classical angles, numerical eigenvalues, or a known order/factor.

Omega=0 is equivalent to T span(B) being contained in span(B). Since T is invertible, this is equality of the subspaces. In that case g_b is an EXACT raw coefficient update inside B, irrespective of the number of work labels. It still says nothing about coordinatewise Q_K preserving the subspace.

Let W=sum_w c_w c_w^T and M=sum_w Q(U(w))=tr(GW). Because P is bijective, summing the leakage over BOTH raw children and all work labels gives

    sum_b,w Q(a_b(w)-B g_b(w)) = tr(Omega W)/2.

Consequently lambda-certified Omega<=lambda G implies total raw instrument leakage <=lambda M/2. An exact rational LDL/Schur positivity certificate for lambda G-Omega is a possible implementation; none was run this turn. The moment W preserves exact coefficient scales. Forming W and modular incidence still visits the represented data. A norm or moment alone is not a sufficient state.

This bound concerns the complete two-child instrument, not the conditional error of a possibly tiny child. Do NOT divide it by an unknown small branch probability and claim a uniform per-branch or final-output bound. Enforcing the final row/field acceptance certificate is a separate requirement.

## 5. Keep the nonlinear boundary; use predicted coordinates only as proposals

The existing quantizer generally breaks subspace closure. With q_b=Q_K(a_b) and e_Q=q_b-a_b,

    q_b=B g_b+s_b R d/2+e_Q.

Both residuals must be represented, retained as exact escapes, or covered by an explicit checked approximation. Dropping either term without charge is prohibited. No Q_K boundary is moved.

A directly testable continuation algorithm is:
1. Freeze B and its exact Gram/factorization at a previously verified history; retain the complete label-to-coefficient relation and explicit escapes.
2. At each subsequent recorded history compute T B, H and A ONCE for that history, not a new basis fitted independently to every child row.
3. Compute exact raw bit masses with the Gram formula and actual label incidence. After selecting the actual bit, form the original complete row a_b and apply the original Q_K.
4. At destinations whose two source arms are encoded in B, use g_b as a coefficient PROPOSAL. Apply the declared short-coefficient quantizer and the already-proved RP8 radial repair against q_b. Return the proposal only if the exact BRC norm/error certificate passes; otherwise retain q_b as an exact escape. Destinations involving an escape may be handled entirely by the unchanged full-row routine.
5. Preserve whole-trial rejection sampling with Q(new complete child)/Q(raw complete child). Do not apply a rowwise ratio to an operation proven contractive only for a whole block.
6. Retain the basis across compatible histories until a deterministic budget/leakage/escape trigger selects a verified update. Do not let private walker visits or cache request order decide the represented state.

This protocol can avoid repeated basis discovery and repeated Gram inversion while B is unchanged. It does NOT remove per-row coefficient operations, Q_K, fitting/certification at an update, exact escaped rows, or ordinary label work. G^-1/factorization caching retains potentially expensive state; the recovered RP8 inverse-payload figures must not be omitted from runtime accounting.

If a basis update appends independent columns selected from T B (or exact escapes), old coefficients are padded with zeros; old represented rows need no refit. New block Gram entries and Schur complements certify the augmented frame. This can trade repeated fitting for rank growth. Shortening new basis columns, deleting directions or enforcing a rank cap requires its own approximation proof; integer bit growth has NOT been eliminated.

## 6. Output-law guarantee and what changes target

Assume every new compression after Q_K has Q(new)<=Q(q), relative norm error <=theta, deterministic history semantics, exact fallback, and finite computation. Let rho=8*2^(1-K), n=t-1. The RP8 direct-sum isometry proof applies to the new proposal-selection rule:

    TV(P_transport,P_exact_same_b12)<=min(1,n(rho+theta)),
    survival Z>=((1-rho)(1-theta))^(2n), for rho,theta<1.

At t16,K16,theta=1/8192 the exact-reference bound is45/8192 and the triangle bound to RP6 K16 is75/8192<1/100. These are symbolic sufficient bounds, not new measured probabilities. Comparison with RP8's different fitted target needs an additional triangle step; do NOT claim identical trajectories or a direct one-percent RP8-to-RP9 bound automatically.

The exact joint-frame representation in section3 is target-preserving until Q_K. The fixed-frame proposal-and-escape protocol defines a potentially DIFFERENT approximate target because its candidates and accept/escape decisions differ. Gate-bank error versus b64/ideal is separate. Factor success is verified by the unchanged exact verifier; neither survival nor a local leak bound proves generic factoring success. Cost per verified factor must include failed trials and preparation.

## 7. First unfinished execution unit and recovery limits

Do not rerun the recovered RP8 short-basis sweep, its two laws or fixed timing blocks as discovery. First recover and hash-verify its actual runtime ZIP and source pins when computation returns. Then:
- start from the two already recorded RP8 checkpoints and their exact short frames, charging all initialization;
- verify V^T V=G, B^T R=0, the Omega identity and both raw children over the complete carrier using the inherited BRC interfaces;
- compare fresh-fit RP8 against frozen-frame coefficient proposals over a predeclared short suffix, preserving every Q_K and recording full error certificates, escapes, rank and bit growth;
- report setup/factorization, basis-word actions, coefficient updates, row reconstruction, correction, labels, inverse/factorization storage and time to a verified factor separately;
- all failed certificates use exact fallback, never silent zero or deleted labels.

Current execution status: container.exec, python.exec and python_user_visible.exec all returned ClientError before a new computation. No new bank build, code execution, basis migration, numerical leakage value, benchmark, hash/replay check or new scientific bundle is claimed. Files lookup for RP7 current attachments was empty; live Drive supplied the exact predecessor proof and recovered RP8. This note is a derivation and recovery record, not a substitute for the missing computational replay.

## Sources and attribution

RP7 source and the four recovered RP8 Drive files above control the inherited mathematics and reported data. Basic projection/Gram identities are not claimed as worldwide discoveries. The new bounded contribution is the explicit two-arm transported-frame/leakage identity and its compatible proposal/escape continuation contract for this BRC recurrence.

External primary context, read at abstract/publication level: Fukaya et al., Shifted CholeskyQR for computing the QR factorization of ill-conditioned matrices, arXiv:1809.11085, https://arxiv.org/abs/1809.11085 . It supports the general warning that Gram-based algorithms have conditioning constraints; its floating-point performance and theorems are NOT transferred to the exact BRC model. No full-text novelty-completeness review was performed.

Logical conversation remains chat-stage101-c971348e64294a5882dfc50fcc8217f1. The old start stage101-session-c971348e-02 remains unverified in current Source. Original recovery2539 is provenance; duplicate2541 was rejected and not bypassed. Publication and Drive mirroring do not grant native authority. P000, schedules, permissions and parent research objective remain unchanged.
