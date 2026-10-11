# Reflection fixes the full Hesse carrier boundary without a harmonic lift

Status: NEW_PAPER_STRUCTURE_CONSEQUENCE / OWNER_REVIEW_PENDING.
Derived under this author's same open arithmetic Task while CHECKPOINT23
was writing the already-reviewed16-file primary result. No new computation,
provider query, branch, candidate replacement or change to frozen bytes.

Fix p=6m+1≥7. Consume the proved unit16 quadratic comparison and the
primary finite cutoff-forcing argument; the harmonic boundary proof is not
needed for the following alternate identification of the same full carrier.
Let E=(f_p(q)−L_p)/p² modp only as a proof object, E=x^p K with
degK≤p−2. The independently defined I has I(0)=0 and D_H I=F where
F=−(2/9)Σ_(j=0)^(p−2)x^j. H=L_p modp has degree2m and H(0)=1.
Coefficient recurrence uniqueness gives K=I+B H with B=K(0).

The exact polynomial identity S(x)+S(1−x)=0 for
S=Σ_(j=0)^(p−2)x^j follows by multiplying by x(1−x):
1−x^p−(1−x)^p=0. D_H is reflection invariant and
H(1−x)=H(x), by its even Legendre degree2m. Therefore

    K(x)+K(1−x)=C H(x), C=K(0)+K(1).

Indeed the left side is homogeneous of degree≤p−2; its coefficients are
determined by its constant term because all recurrence denominators are
units. This is a full polynomial statement, not a marked-value fit.

Since q(1−x)=q(x) exactly, the integral difference

    E(x)−E(1−x)=[L_p(1−x)−L_p(x)]/p² modp

has degree≤p−1. But (1−x)^p=1−x^p in characteristicp, so

    E(x)−E(1−x)
       = x^p[K(x)+K(1−x)]−K(1−x)
       = C x^p H(x)−K(1−x).

The second term has degree≤p−2, while if C≠0 the first has degree
p+2m≥p with nonzero leading coefficient. Cancellation is impossible.
Thus C=0, giving the global antisymmetry

    K(1−x)=−K(x).

For I, reflection gives I(x)+I(1−x)=I(1)H(x). Substituting
K=I+B H then implies I(1)+2B=0. Consequently the full candidate can
be defined independently using only residue-field coefficient recurrences:

    A_p(x)=I_p(x)−(I_p(1)/2)H_p(x).

It satisfies A_p(1−x)=−A_p(x), and the all-prime uniform identity is

    f_p(q(x)) = L_p(x)+p²x^p A_p(x) modp³.

This identifies the same already-proved J_p; it is not a new candidate
chosen after a numerical failure. The harmonic expression HB remains an
independently proved identity, now with the consequence

    B_p=−I_p(1)/2 modp.

No Fermat quotient, harmonic sum throughp², p³ boundary beta extraction
or target value is needed to compute this alternate full carrier. Every
operation defining A_p is in F_p, using the independent finite forcing and
H coefficient recurrence. This reduces the precision inputs needed for the
correction itself, without changing the exact-lift precision required by
L_p(x)/p in the target second-digit formula.

This does not delete the boundary from derivatives or ordinary point state.
It reconstructs it from a proved global reflection condition, so the full
derivative still uses A'_p=I'_p−I_p(1)H'_p/2. At CM roots H=0, the
value remains I; the earlier derivative negative for I alone remains valid.
Full branch tags, signed values, Jacobians, lifts and h/omega^r marks remain.
This is an arithmetic normalization certificate, not a raw modular-period
gauge or a native-world collapse. UR/LIFT/raw period inputs remain OPEN.

The direct divided reflection difference above is used solely to prove the
degree constraint. A_p is defined before any target evaluation from I and H,
not by reading a Gauss/Hesse discrepancy. No new numerical campaign was run.
The prospective Owner merge can preserve this supplement alongside the
primary immutable result without rewriting its candidate/proof/history.

Researcher-ID: EM-ENTERPRISE-CB50ED / RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT
Global-Knowledge-Sync: main@5bf798fdb7aae055cde90a9c2338c0f21fee5a04 / GLOBAL_KNOWLEDGE_V1
