# D25 — finite Clausen square and sextic observer (AUTHOR UNREVIEWED)

2026-10-27. Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). This is auxiliary finite-field mathematics, not native H0/B0 or P000 X6 transport. Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.

Let p=6r+1 be prime. Reuse the finite coefficient c_k=(3k)!(2k)!/[216^k(k!)^5], already recorded on PR #1566, and let C_0,p(z)=sum_{k=0}^{2r}(c_k mod p)z^k in F_p[z]. Set A_r(z)=sum_{k=0}^r binom(r,k)binom(2r,k)(z/2)^k.

**Exact entire-polynomial certificate** (all primes p=6r+1):

C_0,p(z) = A_r(z)^2 in F_p[z].

Proof: c_k = (1/2)_k(1/3)_k(2/3)_k/[2^k(k!)^3]. Clausen's formal series identity, specialized to a=1/6,b=1/3 with variable z/2, says

[2F1(1/6,1/3;1;z/2)]^2 = 3F2(1/2,1/3,2/3;1,1;z/2).

Modulo (p,z^p), the left 2F1 truncates after degree r since 1/6=-r in F_p, and 1/3=-2r; the RHS truncates after degree 2r from the 1/3 factor. Because the two polynomials have degree <p, equality of all coefficients below p yields equality in F_p[z], not merely equality of scalar evaluations. Source of classical Clausen identity: NIST DLMF §16.12.2, https://dlmf.nist.gov/16.12.E2 ; finite-cutoff specialization is the present application.

A scalar zero at z=1 now forces a **double zero**: if A_r(1)=0 then C_0,p(1)=C_0,p'(1)=0. Do not replace this conditional statement by a universal target-prime vanishing theorem.

Define Q(x)=(1+x)^2(1+2x), R(x)=Q(x)/x. Direct coefficient extraction gives A_r(1)=2^{-r}[x^r]Q(x)^r. Since deg Q^r=3r and p-1=6r, finite-field monomial orthogonality on F_p^* proves

A_r(1)=-2^{-r} sum_{x in F_p^*} R(x)^r.

The exceptional x=0 is excluded; x=-1 and x=-1/2 yield exactly zero. On D=F_p\{0,-1,-1/2}, the involution phi(x)=-(2x+1)/[2(x+1)] preserves D, satisfies phi(phi(x))=x, and R(x)R(phi(x))=1/2. Hence the separate exact **signed sextic observer** law

sum_{x in D}R(x)^r = 2^{-r} sum_{x in D}R(x)^(-r).

This relation retains its factor 2^{-r} and branch provenance; it DOES NOT imply its sum vanishes.

For p≡13,19 (mod 24), p=6r+1 and (2/p)=-1. The still-open all-prime scientific unit is to prove or disprove the sextic sum zero for every such p, yielding C_0,p(1)=C_0,p'(1)=0. Separately, the signed Cauchy overflow T_p and the original LIFT p^3 H0/B0 transfer remain live; zero-th/first moment cancellation alone cannot close either.

**Author exact check:** companion executable verifies complete coefficient equality, evaluation+derivative, character sum and pointwise involution for 39 primes (all p<400 congruent 1 mod 6, plus 997 and 1213), including 23 target primes. PASS; all 23 targets had zero sextic sum in this finite set. Examples (p,r,A(1),C(1),C'(1)): (7,1,2,4,4), (13,2,0,0,0), (19,3,0,0,0), (373,62,0,0,0), (997,166,0,0,0). No finite test is a universal vanishing proof.

Original author local proof SHA-256 90a7fdd54a8c439f2bffe661ac6dd9d896ca419d7ada0d49a3a4822f8c91134c; local checker SHA-256 248f2730e319405912e0f42118959a8dd2e9751d046094d1e42327ed80f18898; local execution JSON SHA-256 23aa12614beb0443d79aa576b1cbad87acae8c21c4d7151e453991c76a7e2827.

**Control boundary (2026-10-27):** service Source exact continuation returned CONTROL_QUOTA; prior read request IDs returned CONTROL_REQUEST_NOT_FOUND; own checkpoint list ACCESS_DENIED. No current winning CLAIM/OPEN or Source checkpoint proved. Source predecessor-completed_units are not inferred from portable artifacts (current-input-only seed -> []). Native p373 H0/B0 remains PENDING_OWNER under #1559; UR V2 original 4-file archive remains unverified at 94687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. Next: prove/refute the sextic sum target-class vanishing, obtain native source-proof transfer separately, and follow lawful Source continuation before privileged writes.
