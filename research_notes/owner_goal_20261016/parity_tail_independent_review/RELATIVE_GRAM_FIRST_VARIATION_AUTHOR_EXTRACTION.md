# Relative Gram first variation with normalization and frame terms

Author of this extraction/extension: EM-PERFECT-9821E2,
RA-B732510114F5248E905450FB. Status: UNREVIEWED_AUTHOR_PAPER_EXTRACTION;
not a new accepted Tool. The author's preceding two nonauthor parity review
verdicts apply only to their exact frozen manuscripts, not to this new note.
No self-review or Native acceptance is claimed for this extraction.

This is a precise reusable interface for classical matrix differentiation,
motivated by the independently reviewed equal-block tail proof of
EM-PARITYREV-12B648 at Source df5869771ff760a0b57a5d757934f0ab9f56f07e.
The signed-Gram, sigma, transfer and beta identities retain the authorship of
their original pinned sources. Neither Jacobi's identity nor the general
first-variation calculation is claimed novel. This note makes normalization,
left/right frame and degenerate-coordinate boundaries explicit.

## 1. General local first-variation lemma

Fix n>=1. Let F(t),J(t),P(t),Q(t) be real n-by-n matrix paths differentiable
at t=0 and continuous nearby, with

    F(0)=J(0)=H, det H!=0, P(0)=Q(0)=I.

Let c(t) be a scalar path differentiable at zero, with c(0)=1. On a sufficiently
small neighborhood, J(t) is invertible. Define the scalar observer

    Phi(t)=c(t) tr[J(t)^(-1) P(t)^T F(t) Q(t)].

Then Phi(0)=n and

    Phi'(0)=n c'(0)+tr[H^(-1)(F'(0)-J'(0))]
                    +tr P'(0)+tr Q'(0).                         (1)

Proof. The derivative of the inverse is -H^(-1)J'(0)H^(-1). The product
rule at zero gives four trace terms. The metric terms combine as shown;
cyclicity gives

    tr[H^(-1)P'(0)^T H]=tr P'(0),
    tr[H^(-1)H Q'(0)]=tr Q'(0).

The scalar product contributes c'(0)tr I=n c'(0). This proves (1).
Symmetry, positive definiteness, a positive real generalized spectrum and
entrywise signs are not hypotheses. P and Q can differ; the congruence case
is P=Q=U and contributes 2 tr U'(0).

If both physical forms have a common invertible change C(t) for t>0,

    A_phys(t)=a(t) C(t)^T P(t)^T F(t) Q(t) C(t),
    B_phys(t)=b(t) C(t)^T J(t) C(t),

then their complete relative trace equals Phi(t) whenever a(t)/b(t)=c(t).
This follows by cancellation and similarity BEFORE taking the limit. The
individual scalars and C(t) need not extend invertibly to zero; the ratio c
and the normalized matrices appearing in (1) must extend as stated. Thus a
singular confluent coordinate change is not itself an inverse at t=0.

## 2. Endpoint-motion and determinant specialization

Let H(t,v) be differentiable at (0,0), continuous nearby and nonsingular at
(0,0). Let u(0)=v(0)=0, and put

    F(t)=H(t,u(t)), J(t)=H(t,v(t)),
    kappa=tr[H(0,0)^(-1) partial_v H(0,0)].

The chain rule cancels the common partial_t H term. Thus (1) becomes

    Phi'(0)=n c'(0)+(u'(0)-v'(0))kappa
                    +tr P'(0)+tr Q'(0).                         (2)

Locally kappa=partial_v log|det H(0,v)| at v=0, by Jacobi's identity.
The absolute value accommodates a negative determinant. If

    det H(0,v)=K(1+v)^nu, K!=0,

near v=0 with real nu, then kappa=nu. In particular, if c is identically1,
P=Q=U, u(t)=0, v(t)=b t and U'(0) is trace-free,

    Phi'(0)=-b nu.                                               (3)

The equal-block parity application has t=epsilon, b=m,
nu=1-m^2 and U'(0)=-(m/2)D on polynomials of degree<=m-2. Since D is
nilpotent, its trace is zero. Formula (3) reproduces m(m^2-1), and the actual
t=1/[m(S+1)] scaling reproduces (m^2-1)/(S+1) for the gap. This is reuse of
the already reviewed application, not another independent acceptance vote.

## 3. What the first derivative does and does not give

If A=Phi'(0)>0, differentiability alone gives Phi(t)-n=A t+o(t), hence a
strictly positive gap for all sufficiently small positive t. This is a local
existence conclusion. It does not by itself yield a computable threshold,
an m-uniform radius, positivity for a compact strip or a numerical error bound.
An invertible H at zero and the exact common normalization are essential.

For an effective algebraic interface, reuse the coefficient construction from
R2's tail proof. Suppose, additionally, that the gap is exactly N(t)/D(t)
with rational polynomials, N(0)=0, N'(0)=a>0 and a proved D(t)>0 for
0<=t<=rho, where 0<rho<=1 is rational. Put

    B=sum_(j>=2)|[t^j]N|,
    R=max{1/rho,2B/a}.

For 0<t<=1/R, |N(t)-a t|<=B t^2 and therefore

    Phi(t)-n>=a t/[2D(t)]>0.                                    (4)

This includes B=0 and needs no division by B. It is a finite algebraic
certificate, not an empirical fit. Positivity of D is a separate necessary
input; its sign cannot be assumed merely from a successful derivative test.
This effective clause is credited reuse of the reviewed parity construction.

## 4. Proposed reuse and deduplication disposition

The actual current curated registry enterprise_toolbox_registry.json was read
in full at Source ecd5c3e0677c613f99345eef27ca6858992e6607: 21617 bytes, Git
blob 3889506451091ebcfbf7a58cda6517c4af8c3597. A narrow query through the
existing tool-suggestions scorer was made for
`Gram determinant logarithmic derivative signed relative trace first variation`.
The full query output is preserved in
FIRST_VARIATION_NARROW_TOOL_REUSE_QUERY_ACTUAL.json.

The lexical matches were T3_TYPED_INCIDENCE_CIRCUIT, T0_BRC,
T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN, T2_BLOCK_FINITE_CERTIFICATE,
T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA and T7_FINITE_SYMMETRY_EQUIVARIANCE.
Their typed circuit, provenance composition, path closure, finite-certificate,
capacity and equivariance interfaces do not implement the C1 matrix-path input
and derivative output (1). In particular their occurrence of 'trace', 'signed'
or 'determinant' does not justify assigning this lemma to them. T0_BRC remains
relevant to observer/provenance typing, not to performing this differential.

This was a bounded query of one actual current curated registry. It is NOT an
exhaustive method-addenda, source-module or literature search and proves no
global absence or novelty. No new family is needed to state classical matrix
calculus. Proposed disposition: REUSE_CLASSICAL_MATRIX_DIFFERENTIATION and retain
a TASK_LOCAL_REUSABLE_LEMMA, with any eventual index entry explicitly labeled as
a classical interface/extraction. Acceptance as a canonical Tool would require
its own review and the existing distinct-family reuse gate; neither is claimed.
No registry, method inventory, Tool registration, Foundation or Working Truth
record was edited.

Failure boundaries for reuse are explicit: do not omit a nonzero normalization
derivative n c'(0); do not discard frame traces unless actually proved zero;
do not substitute a singular H(0,0) into inverse differentiation; do not change
the endpoint-motion rates or drop their difference; do not infer an effective
threshold from an unbounded o(t); and do not use this scalar observer to erase
joint branch data needed by later operations. In arbitrary-gap applications,
the correct common frame and normalization must be rederived before (2) applies.

These are external static algebraic observers within fixed Heartbeat X6
semantics, not a native plane or physical-time law. Computer work comprised
full Source reading, custody hashes, text writing, own activity bookkeeping
and the existing metadata-only registry scorer. There were zero mathematical
numeric/symbolic program runs, parameter scans, matrix enumerations, checker
replays, claims, Tasks, Native reviews or Tool writes.

New Source publication and a SEPARATE own semantic RA event for this extraction
are pending. The completed earlier RA event records the two independent reviews
only and must not be relabeled as covering this later authored extension.
