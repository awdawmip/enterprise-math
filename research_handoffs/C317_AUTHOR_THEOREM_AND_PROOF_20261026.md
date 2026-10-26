# C317 — Finite-horizon polynomial port gains: exact minimal observer rank

2026-10-26. Status: AUTHOR_EXACT research-branch artifact, NOT_NATIVE_CLAIM, NOT_DRIVER_ADMITTED.

## Immutable source frontier and semantic scope

GLOBAL_KNOWLEDGE_V1: main@8a584051572960ae4823296de3397ffaafbb4b11, with verified P000 and ACTIVE worldview.
Enterprise Math source: main@f52af9bc69937880cca0d3fa5f97cbe9a79e7194, including docs/PORTABLE_RESEARCH_PROTOCOL.md, tool_invocation_policy.json, and definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json.
Immediate author mathematical dependency: C316 proof at commit 694f3de9020dbc6395a5e5743e11b26c75532a87, path research_handoffs/C316_AUTHOR_THEOREM_AND_PROOF_20261026.md.

This theorem concerns a *formal auxiliary signed labelled vector carrier* V=Q^n with rational coefficients. The C316 tagged Laurent principal-part contrast vectors need not correspond to simultaneous physical states. No claim is made about positive BRC mass cancellation, native GF(2)-BRC phase, X6, a physical port action, or the earlier C195/H168 model definitions. P000 and the protected worldview remain unchanged.

## Precise research question

For the C316 invisible two-channel residue difference space, how many linear repair coordinates preserve every scalar observation after a bounded number of diagonal port-gain operations? Does one-step affine port observation preserve two-step affine observations?

## General finite-horizon minimum-rank theorem

Fix integers n>=1, r>=1, and h>=1. Choose r pairwise disjoint ordered port pairs (a_i, a_i+h) in {0,...,n-1}, with distinct a_i, i=1,...,r. In Q^n define v_i=e_(a_i)-e_(a_i+h) and E=span_Q{v_i}. Then dim(E)=r and scalar sum S(x)=sum_j x_j vanishes on E.

For each rational polynomial p(z) define diagonal formal port gain D_p(x)_j=p(j)x_j. Permit up to H>=0 consecutive gains of polynomial degree <=d, where d>=0, followed by the total readout S. Linear combinations of such readouts are available. This is the COMPLETE DECLARED observation family; no other nonlinear, hidden-port or native operations are assumed.

Let mu_k(x)=sum_j j^k*x_j, with mu_0=S, and set q=H*d.

THEOREM: The family of allowed future observations has exact rank

    m = min(r,q)

on E. Hence, relative to S|E=0, an additional rational-linear repair map preserving all declared future observations on E needs at least m coordinates, and m coordinates suffice. An explicit optimal encoder is

    R_(d,H)(x)=(mu_1(x),...,mu_m(x)).

If q>=r the moments determine the entire E state; if q<r the common invisible subspace has dimension r-q. The theorem is exact over Q.

PROOF:

1. A composition of H gains produces the diagonal gain polynomial p_1(z)...p_H(z), degree <=Hd=q. Conversely every monomial z^k, 0<=k<=q, is a product of at most H polynomials of degree <=d (partition exponent k among the H factors, fill the rest with 1). With d=0 or H=0 only the constant polynomial occurs. Thus the linear span of all accessible readouts equals span{mu_0,...,mu_q}. Since mu_0|E=0, only mu_1,...,mu_q matter.

2. With respect to basis (v_i), the k-th moment row has entries

    M_(k,i)=a_i^k-(a_i+h)^k.

The polynomial f_k(z)=z^k-(z+h)^k has degree k-1 with leading coefficient -k*h. Therefore f_1,...,f_q form a triangular polynomial basis of polynomials of degree <=q-1. Evaluation at r distinct integers a_i has rank min(q,r): when q<=r, a polynomial of degree <=q-1 with r distinct roots must vanish identically; when q>=r, degree <=r-1 interpolation separates the r labels. In particular,

    det(M_(k,i)) for 1<=k,i<=r
      = (-h)^r * r! * PRODUCT_(1<=i<j<=r)(a_j-a_i) != 0.

This also supplies an explicit rational exact certificate for the full-rank boundary.

3. Let A:E->Q^t be any supplementary linear encoding from which every declared future scalar readout can be recovered (recovery functions may even be nonlinear). Two states with the same A must have the same readouts. Because the readouts and A are linear, ker(A) is contained in their common kernel. Thus rank(A)>=rank(M)=m. The first m moment functionals are linearly independent on E and span the same restricted observation row space: if q<r they generate the q accessible rows; if q>=r they injectively recover E and all further readouts. Their m coordinates attain the bound. QED.

## Exact C316 specialization

Use n=79, h=2, a_1=75, a_2=76, v_1=e75-e77, v_2=e76-e78. For x=a*v_1+b*v_2,

    (mu_1,mu_2) = (-2*a-2*b, -304*a-308*b).

The matrix of moments is

    [[-2,-2],
     [-304,-308]]

and determinant is exactly 8. Therefore, writing y_1=mu_1(x), y_2=mu_2(x), the unique exact reconstruction is

    a=(y_2-154*y_1)/4,
    b=(152*y_1-y_2)/4.

One-step affine gain H=1,d=1 has m=1. The nonzero x=v_1-v_2 satisfies (mu_0,mu_1,mu_2)=(0,0,4): it is invisible to the total and EVERY one-step affine port-gain readout, yet visible after two sequential affine gains p_1(z)=p_2(z)=z. For H=2,d=1 the minimal repair rank is m=2. A one-step lossless quotient is thus NOT automatically two-step lossless on the same formal residual space.

The special determinant 8 and hidden witness 4 require no floating-point threshold. The index j is an auxiliary branch label, not an Enterprise native spatial axis or declared physical dynamics.

## Exact reproducibility and validation boundary

C317_PORT_MOMENT_HORIZON_REPLAYER.py uses only Python standard-library exact integers and Fraction. The completed independent local run reports:
- 84 determinant-to-Vandermonde integer equality checks, r=1..7 and h=1..4 on three disjoint label patterns;
- 672 rational matrix rank checks, q=0..r+3;
- 1680 composed-horizon exact rank checks, d=0..3, H=0..4;
- 7500 exact two-step port-gain reconstruction checks on 625 signed coefficient pairs and 12 gain pairs;
- exact special matrix determinant 8 and hidden-witness moment tuple (0,0,4).
All PASS. These finite checks corroborate the separately given mathematical proof. They do not provide Source-native execution, Lean formal proof, independent Driver review, or physical empirical validation.

## Existing-method reuse and open boundary

Existing T0_BRC typed provenance/observer discipline and the observer-lease lattice are REUSE_APPLIED, explicitly conditional on allowed future operators and information retained. The already documented signed group completion method is REUSE_APPLIED only as a signed auxiliary typing analogy; positive masses are not retyped as signed weights. The BRC affine-effect transport executable has different fixed-weight affine I/O semantics, so it is NOT_APPLICABLE as the checker for this declared polynomial label-diagonal operator. No new top-level BRC family is claimed.

Open C318: define a genuinely Source-native typed BRC labelled carrier and allowed composable port operators, then either provide a commuting map from the auxiliary signed principal-part difference data preserving relevant observations, or construct a typed impossibility witness. Also independently reconcile earliest C195/H168 text definitions against C275's constants, indexes and floor semantics. Do not promote this formal auxiliary theorem to native X6 or full 79-port equivalence without that bridge.

## Control/status provenance

Connected GitHub identity: awdawmip, project repository push=true. The native em_control_tasks and em_control_dispatch calls returned CONTROL_QUOTA. Native em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false, so actual formal owner, session, CLAIM and native Result remain unverified/unobtained. Repository research-branch storage is AUTHOR provenance, not native admitted scientific state.
