# D25: ordinary valuation-two three-port factorization and finite S tail (2026-11-02)

**AUTHOR-DERIVED / CONDITIONAL EXACT ALGEBRAIC PROOF / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0_B0.**

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` distinct from maintenance. This note consumes the immutable previous source-port theorem at commit `3dd822d95da90d9ffa48a344f6c8ada46b8ffcb5`. Mother goal remains original `Delta_p-R_p=0 mod p` for p≡13,19(mod24).

## Exact theorem

Use the original coefficients `alpha_W(k)=(2k)!(3k)!/(216^k(k!)^5)`, `alpha_S(k)=(4k)!/(2304^k(k!)^4)`; weights `lambda*k+1` with lambda=6 for W, 8 for S. For any prime p≡13,19(mod24), write k=ap+b, 0≤a,b<p. Define j*=3 (W), 4 (S), h=floor((p−1)/j*), H=(p−1)/2, E=2(p−1)/3 (W) or E=floor((3p−1)/4) (S). Put I0=[0,h], I1=[h+1,H], I2=[H+1,E]. Define p-free unit U(a)=alpha(ap)/p^v(alpha(ap)) and V(b)=alpha(b)/p^v(alpha(b)) modulo p; v=v_p.

Let M_t=sum_{a in I0}a^t alpha(a) (t=0,1,2), B2=sum_{b in I2}(lambda*b+1)V(b), A1=sum_{a in I1}(j*a+1)U(a), B1=sum_{b in I1}(lambda*b+1)V(b), A2=sum_{a in I2}U(a), all in F_p.

Let T2 be the weighted sum of **ordinary** terms with v_p(alpha(ap+b))=2 and all extra high-digit carry flags delta_j=0, preserving the exact source-tagged population. Then

`T2/p² ≡ Q*B2 + A1*B1 + A2*(M0+lambda*M1) (mod p)`

where `Q=6*M2+5*M1+M0` for W, `Q=8*M2+6*M1+M0` for S. The formula holds without CM premises. Under independently justified `M0=M1=0 mod p`, it reduces to `T2/p² ≡ 6*M2*B2+A1*B1` (W) or `8*M2*B2+A1*B1` (S).

## Proof and provenance

Legendre's original factorial valuation law gives `v(alpha(ap+b))=v(alpha(ap))+v(alpha(b))+sum delta_j`. On delta=0, valuation two lies exactly in the disjoint rectangles `I0×I2`, `I1×I1`, `I2×I0`. The already established p-free unit law is `u(ap+b)=u(ap)u(b)*product_j binom((ja mod p)+floor(jb/p),floor(jb/p)) mod p`. First rectangle gives `(2a+1)(3a+1)=6a²+5a+1` for W and `binom(4a+2,2)=8a²+6a+1` for S; middle gives `(j*a+1)`, final gives 1. Extra high carry at a rectangle boundary gives a zero factor mod p, correctly excluding that source from this readout. Original weight is `lambda*b+1 mod p`. The sum therefore factors into the three displayed one-dimensional source moments. CM M0=M1=0, when separately established, kills the high-only port and the first/zeroth parts of Q.

## Executed exact finite check and p373 five-source refinement

The executed independent source-unit checker `d25_ordinary_v2_moment_reduction_20261102.py` compared **59,428** original source terms across p=13,19,37,43,61,67,109,139,373; every factor and three-port sum matched a separately coded original weighted recurrence modulo p³. The local proof and executable/JSON checks are preserved with this run; the remote note is an author-side record, not a Source Result.

At p=373, three ports `I0×I2,I1×I1,I2×I0` have W digits (88,177,0) total **265**, S digits (0,61,0) total **61**; signed source =`265−2*61=143` mod373. Combining separately checked original sources gives the fifth-digit decomposition:
`ordinary v0 143 + ordinary v1 second digit 82 + ordinary v2 first digit 143 + anomaly>=2 4 + baseline p² 1 = 373 ≡ 0 (mod373)`. First digit of ordinary v1 vanishes separately under the two CM moments, as shown in prior theorem.

A second actually executed checker `d25_s_tail_107prime_20261102.py` found the S2304 **B2=0 mod p for each of all 107 target primes ≤3000** (53 class13; 54 class19), using original factorial-unit arithmetic. This is a scoped finite pattern and an unproved universal candidate.

## Exact next actions / constraints

Seek a finite-field hypergeometric / WZ certificate of S2304 B2=0 over the full target prime classes, and lift ordinary v1 rectangles to the next p-digit using p² factorial units; combine all five original source ports into the frozen `Delta_p-R_p` observer. Native benchmark at issue #1559 remains PENDING_OWNER/NOT_EXECUTED: actual original p373 `[X]U mod139129`, H0/B0 rank, real semilinear Frobenius/eta, signed Green/Hesse, κ and independent check. Researcher session/claim/run/checkpoint and independent admission are unverified/unavailable for this client. The historical failed request `research-onhour-20261031-0205-dispatch-r15` is not reissued. BRC: retain signed (model,a,b,carry,valuation,unit) source branches. Pre-existing precision family `T5_PRECISION_REFINEMENT` reused at its exact finite readout law; no new tool family or native-X6 equivalence claimed.
