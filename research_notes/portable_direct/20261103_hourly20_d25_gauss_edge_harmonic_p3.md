# D25 — finite-Gauss boundary unit through p³ by short harmonic sums

**2026-11-03 (Asia/Hong_Kong)**. Author-derived, algebraically proved, finite exact-checked, **unreviewed/not admitted**; native activity REGISTER_PENDING. Logical research lane: \`chatgpt-research-hourly-enterprise-math-20260923\` (separate from CONTROL_PLANE_MAINTENANCE). Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Mother target: Delta_p-R_p=0 mod p for p mod24 in {13,19}; this note concerns an auxiliary finite-Clausen source component.

Let prime p=6r+1>=7, c_k=(1/6)_k (1/3)_k/(k!)², U_p=c_(p-1)/p² in Z_(p), H_n^(m)=sum_(j=1)^n 1/j^m, H_n=H_n^(1). The previous U1 result gave U_p=1/10 mod p, and previous C3 used the **full** U_p mod p³ in the six-prefix-moment plus high/high Clausen reconstruction. Here is a closed form for the two further boundary digits.

## H5. Exact product identity

For every such prime,

U_p = 1/[(p+5)(p+2)]
 × product_(j=1)^(r+1) (1-p/j)^(-1)
 × product_(j=1)^(2r+1) (1-p/j)^(-1)
 × product_(j=1)^r (1-p/(6j))
 × product_(j=1)^(5r-1) (1+p/(6j))
 × product_(j=1)^(2r) (1-p/(3j))
 × product_(j=1)^(4r-1) (1+p/(3j)).

This is **an exact rational identity**, not merely a congruence. Proof: in (1/6)_(p-1) the sole p factor is j=r; in (1/3)_(p-1) it is j=2r. After removing both, shift j to m=j-r and m=j-2r:

U_p = [(-1)^(3r) r!(5r-1)!(2r)!(4r-1)!]/[18((p-1)!)²]
 × product_(m=-r..5r-1,m≠0) (1+p/(6m))
 × product_(m=-2r..4r-1,m≠0) (1+p/(3m)).

Use the **exact** factorial complement identity (p-1-m)!=(p-1)!/[(-1)^m m! product_(j=1)^m(1-p/j)] for m=r+1,2r+1. The signs/factorials cancel, and 18(r+1)(2r+1)=(p+5)(p+2). Split negative and positive m. All denominators are p-units. QED.

## H6. Two-digit harmonic lift

Put h=H_(r+1)+H_(2r+1), t1=H_(r+1)^(2), t2=H_(2r+1)^(2). Then, for **every** prime p=6r+1>=7,

**10 U_p = 1 + p h + p² (h²/2 + 2t1/3 + 5t2/6) (mod p³).**

In particular U_p=(1+p h)/10 mod p².

Proof: take the p-adic log of 10U_p in H5. The p and p² coefficients before complementary-harmonic simplification are respectively

A1 = -1/5-1/2+H_(r+1)+H_(2r+1)+(H_(5r-1)-H_r)/6+(H_(4r-1)-H_(2r))/3,

A2 = [1/25+1/4+H_(r+1)^(2)+H_(2r+1)^(2)]/2
 -(H_r^(2)+H_(5r-1)^(2))/72
 -(H_(2r)^(2)+H_(4r-1)^(2))/18.

Pairing j with p-j and using sum_(j=1)^(p-1)j^(-2)=0 mod p yields H_(p-1)=0 mod p² and H_(p-1)^(2)=0 mod p. Therefore H_(5r-1)=H_(r+1)+p t1 and H_(4r-1)=H_(2r+1)+p t2 modulo p², whereas H_(5r-1)^(2)=-t1 and H_(4r-1)^(2)=-t2 modulo p. Since 6(r+1)=p+5 and 3(2r+1)=p+2, these reduce to

A1 = h + p(-1/25-1/4+t1/6+t2/3) (mod p²),
A2 = 1/25+1/4+(t1+t2)/2 (mod p).

Hence log(10U_p)=p h+p²(2t1/3+5t2/6) mod p³. Exponentiate; the extra h²/2 gives H6. QED. All logarithmic truncations are p-adically justified for p>=7.

### All-order source generator

H5 itself works at every finite precision. More explicitly let

A_m=(-1)^m(5^(-m)+2^(-m))+H_(r+1)^(m)+H_(2r+1)^(m)-6^(-m)H_r^(m)-3^(-m)H_(2r)^(m)+(-1)^(m+1)[6^(-m)H_(5r-1)^(m)+3^(-m)H_(4r-1)^(m)].

Then log(10U_p)=sum_(m>=1) p^m A_m/m converges p-adically. To extract modulo p^q, retain every potential contribution with m-v_p(m)<q; for q>=p do not blindly truncate after m=q-1.

### C3 observer-safe transport and actual checks

The C3 low/middle source factor -2 U_p 2^(-(p-1)) may now be replaced, *mod p³*, by

-2^( -(p-1)) /5 × [1+p h+p²(h²/2+2t1/3+5t2/6)].

The distinct C3 high/high triangular port and all original ordered-index/valuation/signed-weight provenance remain retained. This is an exact precision-typed factorization for the stated scalar observer, not a claim that the harmonic coordinates recover the whole Gauss polynomial.

Two actually executed independent standard-library modular paths—direct original numerator after stripping exactly the two p factors, and separate short harmonic sums—matched on all 148 primes p<=2000 with p≡1 mod6; prior leading digit and new p² congruence also matched. For p=373, r=62: U_p mod 373³ = **36237435=112+171×373+260×373²**; (h,t1,t2) mod373=(221,21,83); 10U_p mod373³=51003648. These are finite checks, not a native H0/B0 run or independent review.

**Next**: analyze coupling of this p³ edge correction with the existing H3 Gauss Hensel second digit and C3 original-216 signed ports; seek a sourced certificate for 12*j*h_Gauss=1 mod p in the target classes, or an in-hypothesis counterexample. Derive an exact map to frozen Delta-R before asserting mother closure. The harmonic h above is distinct from h_Gauss=G(1/2)/p.

BRC: original parameter-line labels (1/6,1/3), two extracted p factors, prime, index/valuation, ordered pair provenance and signed C3 observer are retained. The (h,t1,t2) quotient is certified only at declared U_p mod p³. Reuse: COMPOSE_APPLIED (existing U1/H4/C3).

Native Gateway 0.6.11 read only: UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active quota 5/5. No new native CLAIM/OPEN/checkpoint/Result or review. Historical #6637/#6638/staging are not replayed. Control #1558 and original-373 H0/B0 #1559 retain their scopes.
