# D25: branch-sensitive Fricke local weighted-jet transport at the common CM fiber (2026-11-07)

Status AUTHOR-SIDE PROVED ALGEBRA / SYMBOLIC EXACT CHECKED / UNREVIEWED / NOT_ADMITTED. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; science frozen at c47e13e4aba0e006366f989d6334d443f6333ae3. This follows the same-lane low-degree weighted jet theorem at fbe820347866f8b8f8ae6d48da534f0889203672, and reuses without claiming authorship the independent onhour explicit X0(6) Fricke maps at 6ffcf3e8e7a2876fdd4e35ddd7b1ca4d35754e07.

## Exact two-legged input and domain

For a prime p=13 mod24 (so 2 is nonsquare in F_p) let T be a root of T^2=72 in F_{p²}. The two roots T_+=+6sqrt(2), T_-=-6sqrt(2) are interchanged by Frobenius. The independently proven rational two-leg maps are

  z(t)=108 t²(t+9)(t+8)²/(t+12)^6,
  w(t)=256 t³(t+8)(t+9)³/(t²+36t+216)^4.

For both t=T_±, z=1/2, w=1/9. The map denominators and both derivatives are nonzero in F_{p²} for all p>3 in the class. In the actual finite-field weighted polynomial observers P_A(z), P_B(w) from the immediately prior same-lane result, both special values vanish simply. Their normalized second jets (derivatives with respect to their own variables) are 4/3 and -99/16. These are mod-p polynomials, not their original p³ coefficients.

## Theorem: necessary branch-resolved local gauge jets

At T_ε=ε6sqrt(2), ε in {+1,-1}, exact rational differentiation gives in Q(sqrt(2)) and hence after reduction in F_{p²}:

  z'(T_ε)=-1+ε(3sqrt(2)/4),
  w'(T_ε)=4/9-ε(8sqrt(2)/27),
  z'(T_ε)/w'(T_ε)=ε(27sqrt(2)/16),
  z''(T_ε)/z'(T_ε)=-2/3+ε(5sqrt(2)/12),
  w''(T_ε)/w'(T_ε)=13/4-ε(9sqrt(2)/4).

Suppose a nonvanishing formal local scalar gauge gamma_ε(t) achieves, up to Taylor order 2 around T_ε,

  P_A(z(t)) = gamma_ε(t) P_B(w(t)) + O((t-T_ε)^3).

Then gamma_ε is constrained at the point by

  **gamma_ε(T_ε) = ε(6561sqrt(2)/1024) * (F_m'(1/2)/H_k'(1/9))²**, and

  **gamma_ε'(T_ε)/gamma_ε(T_ε) = -5/4+ε(11sqrt(2)/12)**.

Here p=6m+1=8k+5; F_m and H_k retain their **distinct 216 and 2304 source labels**. The first formula follows from matching first derivatives:
  gamma(T)=P_A'(1/2)z'(T)/[P_B'(1/9)w'(T)]
           =(6F'^2)/(128H'^2/81)*(z'/w').
The second formula follows from matching second derivatives divided by first:
  2gamma'/gamma=[(P_A''/P_A')z'+z''/z']-[(P_B''/P_B')w'+w''/w']
               =(4/3)z'+z''/z'+(99/16)w'-w''/w'.
Substitution of the five exact Fricke derivative values simplifies to the claimed expression. All required first derivatives are units by the earlier source CM0 and Hasse squarefree theorems, under the same frozen input. The two equations are **necessary and locally sufficient to match Taylor coefficients through degree two** (taking any gamma with the prescribed value/derivative); they do not establish a global polynomial or p-adic identity.

## New branch-provenance invariant

Under Frobenius T_+^p=T_- (since (2/p)=-1). Hence gamma_+(T_+)^p=gamma_-(T_-), and the first-jet gauge **has trace zero** in the quadratic extension. The two logarithmic derivatives form a conjugate pair

  ell_±=-5/4 ± 11sqrt(2)/12,

with exactly

  **Trace_{F_{p²}/F_p}(ell)=-5/2; Norm_{F_{p²}/F_p}(ell)=-17/144.**

This is a scope-exact BRC certificate: collapsing the two Fricke branches to the shared scalar coordinates (z=1/2,w=1/9) loses a sign-sensitive gauge value, even though the trace and norm of the logarithmic jet survive in F_p. These are algebraic finite-field observations, not native-X6 cell equivalences or a p-adic source redundancy certificate.

## Exact validation, limits and continuation

A companion SymPy checker symbolically differentiated the exact rational z(t),w(t), substituted both ±6sqrt(2), checked the five derivative identities and both ell conjugation invariants; it executed PASS. Earlier same-lane exact independent original-3F2 checker passed 52 target primes p<1200, including 26 with p=13 mod24 for the underlying weighted jets. No floating evaluation, no native p373 experiment and no current Source admission.

The current candidate gauge is only a **2-jet local necessity**. The next smallest scientific step is to compute the **third** and p-adic **second-digit** discrepancy under the nonlinear two-leg Fricke map, preserving ordered Cauchy ports, sign branch, ramification and p² cutoff. A successful p³ transport could advance the frozen W_p=p mod p³ / Delta_p-R_p=0 mod p mother objective. A failed local lift will give a precise obstruction and a correction term, not a global impossibility declaration. The independently authored complex analytic principal-branch multiplier 3sqrt(2)/4 belongs to a different, infinite-period observer; it is not substituted for the finite-field weighted gamma here.

Control status checked on 2026-11-07: Site CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false, em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Research execution session/claim/run/staging UNKNOWN_PRESERVE, original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 untouched; activity REGISTER_PENDING; native checkpoint, Result, freeze, review and admission not claimed. Controller support awdawmip/enterprise-math#1558.
