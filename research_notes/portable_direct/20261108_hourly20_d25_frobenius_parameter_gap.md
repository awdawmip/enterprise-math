# D25 — Frobenius parameter-jet gap and first normalized endpoint correction

Date: 2026-11-08 (Asia/Hong_Kong). Role: TASK_RESEARCH author-side portable result, REGISTER_PENDING, UNREVIEWED / NOT_ADMITTED. Research lane requested: chatgpt-research-hourly-enterprise-math-20260923; maintenance conversation chatgpt-hourly-enterprise-math-20260921 excluded. Source task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Accepted D24 first-digit UR/JT0 remains a frozen input; the original second-digit LIFT Delta_p-R_p=0 mod p is open.

## Universal endpoint factorization (PROVED)

Let p>=5 be prime, let 0<=u<v<=p-2 be integers, and c1,c2 rational and integral at p. Let h be a formal indeterminate. Define

    G(h,z) = sum_{n=0}^{p-1} (-u+c1*h)_n(-v+c2*h)_n/(n!)^2 * z^n,
    D = z*d/dz,
    L_h = D^2-z(D-u+c1*h)(D-v+c2*h).

A direct Gauss coefficient recurrence, including its first omitted z^p coefficient, gives an *exact rational polynomial identity*

    L_h G(h,z) = -N_p(h)*z^p,
    N_p(h) = (-u+c1*h)_p*(-v+c2*h)_p/((p-1)!)^2.          (1)

Reducing the entire endpoint polynomial in F_p[h] gives

    N_p(h) = c1*c2*(h^p-h)^2   (mod p).                    (2)

Indeed the p consecutive residues j-u (0<=j<p) enumerate F_p, so

    (-u+c*h)_p = (c*h)^p-c*h = c*(h^p-h) (mod p),

and Wilson gives ((p-1)!)^2=1 modulo p. In particular, if N_p(h)=sum_r b_r h^r, then b0=b1=0 exactly; b2=c1*c2 modulo p; every b_r for 3<=r<=p vanishes modulo p; b_(p+1)=-2c1*c2 modulo p; and b_(2p)=c1*c2 modulo p. **The cubic and all intermediate parameter-jet endpoints vanish in F_p.**

This strengthens the previously proved D25 second-parameter-jet identity by identifying the *whole* Frobenius boundary polynomial, without introducing any extra Euler, Cartier, or overflow assumption.

## First p-adic correction (PROVED)

The exact quadratic Taylor coefficient is

    b2 = c1*c2*(-1)^(u+v)/[binom(p-1,u)*binom(p-1,v)]
       = c1*c2 * prod_{j=1}^u(1-p/j)^(-1)
                   * prod_{j=1}^v(1-p/j)^(-1).

For H_n=sum_{j=1}^n 1/j with H_0=0, it follows that

    b2 = c1*c2*[1+p(H_u+H_v)] (mod p^2).                   (3)

The h^3 coefficient is divisible by p by (2); all coefficients are p-integral. Substituting h=p in (1) and using (3) therefore proves, coefficientwise in (Z/p^4 Z)[z],

    L_p G(p,z) =
       -p^2*c1*c2*[1+p(H_u+H_v)]*z^p  (mod p^4).          (4)

No independent mod-p cubic boundary charge enters the original parameter deformation. Formula (4) supplies a *specified* next endpoint digit, separate from the task's cutoff-dependent lower injection.

## Specialization and BRC source typing

For the existing 216/Gauss A model: p=6m+1, u=m, v=2m, c1=1/6, c2=1/3. For the 2304/Gauss B3 or Euler B5 model: p=8k+3 or 8k+5, u=k, v=3k+1, c1=1/8, c2=3/8. Thus the normalized top endpoints agree in their leading mod-p charge, while the next source-labelled difference is exactly

    D_p = H_m+H_(2m)-H_k-H_(3k+1) (mod p).                 (5)

D_p records only the *normalized endpoint difference at this precision*. It is not the overall Fricke LIFT residual Delta_p-R_p. The full carrier retains A/B model labels, B3/B5 Euler choice, their integer/p-adic lifts, derivative/Cartier sources, signed conjugate branch, the lower boundary injection, and cutoff overflow. Quotienting all of these to a common -z^p leading charge is not safe for the declared future operator. BRC reuse state: COMPOSE_APPLIED (existing Gauss two-jet + valuation/carry ports); this is a specialization, not a newly accepted global BRC tool or a new P000 ontology.

## Executed exact regression

Accompanying Python standard-library verifier d25_parameter_frobenius_gap_20261108.py computes both complete p-fold Pochhammer products modulo p^4, using independent modular rational arithmetic; then checks equation (4) and harmonic reflection. It covers every prime p<2500 in the two frozen classes p=13,19 (mod 24): 94 primes, two models each, **188/188 PASS**. The additional full formal finite-field p-fold polynomial checks at p=13,19,43,67,373 (both models) establish **10/10 PASS** for the factorization underlying (2). The local executed full verifier additionally compared the complete 2p-degree product at those same primes.

Selected values of N_p(p)/p^2 (A,B) modulo p^2:

    p=13:  (138, 62)        mod 169
    p=19:  (37, 52)         mod 361
    p=43:  (1818, 897)      mod 1849
    p=67:  (2252, 2344)     mod 4489
    p=373: (127421,121464)  mod 139129

All these are p-adic Gauss endpoint tests, distinct from the original native H0/B0, divided-power, Hesse-kappa and independent p=373 benchmark (issue #1559).

## Exact dependency and next action

Reused: D25 Gauss two-jet proof 66125943c08551744135599e160c794a4fdf9a38; the existing signed Fricke/CM source bridge d3478ba59281b4dfaae960ee31197d1704dfc23e; the proven p^3 four-port and reduced scalar residual Gamma_p+E_A-E_B (156dc160fdf808d4c6497f873af436e17dd3c728). Taskbook original blob 53a3ef039325534e3715add837f0eee332289984.

Next research unit is to **derive an exact source-preserving Fricke/Cartier identity for the remaining divided second digit**, or a strictly smaller equivalent certificate for Delta_p-R_p, based on Gamma_p+E_A-E_B and the signed A/B port data. First discriminate at p=13,19,43,67,373 using the already available witnesses (Gamma,E_A,E_B) rather than repeating them. Equation (2) eliminates one speculative high-jet source; the exact lower endpoint and short-overflow/Cartier terms remain. The harmonic port (5) is available if a proposed p-adic transformation requires the next endpoint digit. Neither a higher precision scan nor a re-proof of the accepted first digit is the next target.

## Provenance/control boundary

At 2026-11-07T16:17:42Z, Site diagnostic returned CONFIGURED_NOT_LIVE_VERIFIED with research_authority_granted=false. The native em_status call returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE / operation_sent=false. Unresolved original research-lane requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 remain for original-request receipt/reconcile, with old session/claim/run/staging UNKNOWN_PRESERVE. This author-side artifact is not a native execution checkpoint or a review. Support owner path: https://github.com/awdawmip/enterprise-math/issues/1558. The recovery acceptance condition is authenticated same-subject status, the original receipts and exact Source continuation, then properly authorized claim/open under the current contract.
