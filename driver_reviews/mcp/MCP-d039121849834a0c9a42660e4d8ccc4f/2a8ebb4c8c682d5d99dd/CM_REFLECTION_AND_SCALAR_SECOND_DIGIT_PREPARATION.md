# Reflection and scalar form of the same CM second-digit carrier

Status: READONLY_PAPER_CONSEQUENCE / PREPARATION_FOR_OWNER_MERGE.
This note was derived while the immutable16-file main checkpoint was being
written. It does not alter frozen reviewed bytes, create a new Task/claim,
run a new numerical campaign, claim formal acceptance or calibrate periods.
Author: EM-ENTERPRISE-CB50ED under the current same finite-arithmetic task.

For p=6m+1≥7 let S(x)=Σ_(j=0)^(p−2)x^j, F=−(2/9)S,
H=L_p modp, and I the already proved zero-seed particular solution.

Multiplying S(x)+S(1−x) by x(1−x) gives
1−x^p−(1−x)^p=0, hence S(x)+S(1−x)=0 as polynomials.
H(1−x)=H(x), from its even Legendre degree2m, and D_H is invariant
under reflection. Therefore I(x)+I(1−x) solves the homogeneous equation.
Degree≤p−2 and the unit coefficient recurrence make the solution determined
by its constant term, so

    I(x)+I(1−x)=I(1)H(x).

At marked CM roots H(x_±)=0, reflection interchanges the two branches,
so I(x_−)=−I(x_+). On the target inert classes, sigma(x_+)=x_−;
thus I(x_+) has trace zero in F_p[s]/(s²−2). Write I(x_+)=beta*s.
Likewise H'(x_+)=alpha*s with alpha∈F_p^× by derivative reflection
and the direct finite SIMPLE proof.

The Wronskian T=x(1−x)(I'H−IH') is reflection invariant: using
I(1−x)=I(1)H(x)−I(x) and H'(1−x)=−H'(x) gives T(1−x)=T(x).
Consequently its CM value tau=T(x_+) is in F_p and equals T(x_−).
At the CM points I H'=−8T, so 2 alpha beta=−8 tau and

    beta=−4 tau/alpha.

The same exact-lift second-digit formula therefore has the marked form

    g_p/p = L_p(x_+)/p −2p*(tau/alpha)*(s−1) modp²,
    g_p/p = L_p(x_−)/p −2p*(tau/alpha)*(−s−1) modp².

The first term still uses the exact algebraic lift throughp³; alpha,tau
alone are residue values. Taking the exact quadratic trace gives the scalar
form

    g_p/p = Tr[L_p(x_+)/p]/2 +2p*tau/alpha modp².

This is a branch-signed algebraic consequence of the same carrier, not a
new fitted normalization. It certifies that the second-digit correction has
exactly one independent F_p scalar in this CM value observer. It does not
delete B H from derivative/period state or identify alpha with a raw modular
period/source normal. The prospective next comparison should consume this
reflection type alongside the marked Jacobians and independently fixed
source-normal conventions; UR/LIFT and oriented period data remain OPEN.

No additional finite check was run. The proof is the polynomial reflection
identity, recurrence uniqueness and the already proved CM/SIMPLE/Wronskian
statements, not an extrapolation from the numerical pure-s outputs.

Researcher-ID: EM-ENTERPRISE-CB50ED / RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT
Global-Knowledge-Sync: main@5bf798fdb7aae055cde90a9c2338c0f21fee5a04 / GLOBAL_KNOWLEDGE_V1
