# D25 — Exact Newton normal/carry source separation and two-window reconstruction

2026-11-07 Asia/Hong_Kong. AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-hourly-enterprise-math-20260923.

## Source model and the open objective

Earlier proved endpoint-sequence identity: for prime p=6m+1, E_t(+1) = P_m(t-4m) mod p, where P_m(z) is the D25 three-labelled-binomial observer. Its first derivative at z=0 is the still-open normal/carry tangent T_(1,p)+T_(3,p), previously reduced to an inverse finite-field moment and two labelled source bands.

The following theorem holds over Q for EVERY integer m>=1 (no primality assumed). Put a=2m, b=3m, c=4m, w_j=(6j+1)(-1/2)^j binom(b,j), and define polynomial binomials in t:

    f_j(t)=w_j binom(t-a,j) binom(t,j);
    F_m(t)=sum_(j=0)^b f_j(t)=P_m(t-c);
    N_m(t)=sum_(j=0)^a f_j(t)  [normal band];
    R_m(t)=sum_(j=a+1)^b f_j(t)  [carry band];
    q(t)=product_(s=0)^c(t-s).

## Theorem A — exact Newton spectral separation by original source band

There is a unique C_m in Q[t] with

    F_m(t)=N_m(t)+q(t)C_m(t),
    deg N_m=c=4m,  deg C_m=2m-1.

In particular, with Delta g(t)=g(t+1)-g(t),

    Delta^r F_m(0)=Delta^r N_m(0), 0<=r<=c;
    Delta^r F_m(0)=Delta^r R_m(0), c<r<=6m.

Proof. The degree of f_j is 2j, so deg N<=2a=c; its j=a top coefficient is nonzero, giving equality. For j=a+r, 1<=r<=m, the roots of binom(t,j) are 0,...,a+r-1, and of binom(t-a,j) are a,...,c+r-1. Their union contains EVERY integer 0,...,c. Thus q divides each carry summand, and explicitly

    C_m(t)= sum_(r=1)^m w_(a+r)/((a+r)!)^2
             * product_(s=a)^(a+r-1)(t-s)
             * product_(s=c+1)^(c+r-1)(t-s),

with empty last product = 1. The r=m coefficient of degree 2m-1 is nonzero. Uniqueness follows from Euclidean division by monic q of degree c+1. Carry terms vanish at t=0,...,c; hence all forward differences of order <=c are zero. Normal terms have degree <=c, so all higher forward differences vanish. QED.

This is a canonical decomposition of two **aggregate source groups** in the scalar endpoint Newton spectrum; it does not claim to reconstruct each individual j-labelled term.

## Theorem B — source-band recovery from p scalar samples

Let p=6m+1 be prime, and suppose only the p field values e_t=E_t(+1)=F_m(t) mod p are supplied, 0<=t<p. Their coefficients have p-unit denominators. Set d_r=Delta^r e_0, 0<=r<=c. Then

    Nhat(t)=sum_(r=0)^c d_r binom(t,r)

equals the original normal-source N_m(t) in F_p[t]. For u=0,...,n-1 with n=2m, compute

    t_u=c+1+u,
    h_u=[e_(t_u)-Nhat(t_u)]/[t_u! / u!]   (mod p).

These h_u equal C_m(t_u), and n=2m values reconstruct the degree <=n-1 polynomial C_m uniquely. The missing boundary value has explicit left-extrapolation formula

    C_m(c)=sum_(u=0)^(n-1) (-1)^u binom(n,u+1) h_u  (mod p).

The open tangent therefore splits into two independently readable source contributions:

    [z]P_m(z)=N_m'(c)+c!C_m(c)  (mod p),

    N_m'(c)= H_c e_c
             +sum_(t=0)^(c-1) (-1)^(c-t) binom(c,t) e_t/(c-t),

    c!C_m(c)= [1/(c+1)] sum_(u=0)^(n-1)
              (-1)^u binom(n,u+1)/binom(c+1+u,u)
              *[e_(c+1+u)-Nhat(c+1+u)].

All inverses exist since 0<=c+1+u<p.

Proof. R_m vanishes on 0,...,c, so Newton interpolation of the first c+1 scalar samples recovers N_m. The remaining n values, after subtracting N_m, can be divided by q(t_u)=t_u!/u!, a field unit, to recover C_m at n distinct points. The extrapolation uses the degree bound: C_m(c)=sum_(r=0)^(n-1)(-1)^r Delta^r C_m(c+1), then sum_(r=u)^(n-1) binom(r,u)=binom(n,u+1). Differentiate F=N+q C at t=c, where q(c)=0, q'(c)=c!. The N'(c) expression comes from endpoint Lagrange basis differentiation; multiplying the C extrapolation by c! gives the stated tail. QED.

## Exact independent computation

Python stdlib program d25_newton_provenance_projection_20261107.py evaluated ALL 80 primes p=1 (mod 6), 7<=p<=1000. It computes the original j-labelled normal and carry source values separately, verifies the Newton projection reconstructs N at all field inputs, derives C(c) from the complementary scalar window, and checks both derivative components against independently differentiated original j-source summands. For p<=73 it also recomputes all E_t(+1) by an independent central-binomial endpoint formula. Assertions: ALL PASS. Finite zero-tangent observations are not a universal proof.

Witness tuples (p, N'(c), c!C(c), C(c), total tangent), residues mod p:

    (7,2,5,4,0)
    (13,5,8,3,0)
    (19,2,17,15,0)
    (31,28,3,25,0)
    (109,46,63,47,0)
    (211,178,33,170,0)
    (229,218,11,65,0)
    (373,81,292,63,0).

These agree with prior labelled head/carry first-jet residues at p=13,109,211,229,373 through a different *scalar-only* observer route.

## BRC source fidelity and recovery frontier

Carrier: labelled sources (3m,2m+z,4m+z) with integer j, valuation and normal j<=2m/carry j>2m branch. Observer: full scalar endpoint table. Operation: field forward-difference Newton interpolation and division by the explicit consecutive-root factor. Recovered: both aggregate source-band polynomials and their derivative components. Straightforward implementation: O(p^2) field operations and O(p) working memory given p scalar input samples; no generic input-generation speed claim. This is auxiliary mathematical BRC typing, not a native six-axis/worldview or H0/B0/Frobenius experiment.

Frozen mother target remains Delta_p-R_p=0 mod p for p=13,19 mod24. Next scientific unit: find a summand-level hypergeometric/WZ telescope forcing N_m'(4m)+(4m)!C_m(4m)=0 and examine transfer to signed second-digit LIFT (frozen p373 H0/B0 native experiment still pending).

Current control fault checked 2026-11-07 approx 03:25 Asia/Hong_Kong: em_status and original target_request_ids em-h20-20261106-1324-d25-task-r13 / em-h20-20261106-1324-d25-cont-r13 returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Site phase CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Native session/claim/run and staging UNKNOWN; no replacement or checkpoint action. CONTROL_PLANE_MAINTENANCE issue #1558 tracks recovery. Author-side evidence only.
