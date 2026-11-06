# D25 — second-digit re-coalescence of distinct signed source directions

Date: 2026-11-06. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; scientific frozen pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Scope: author-side exact p-local source-polynomial observer, **NOT native crystalline LIFT**. Status: AUTHOR-PROVED / EXACT THREE-PRIME CERTIFICATES / UNREVIEWED / NOT_ADMITTED.

## The quadratic fiber law

Use the unchanged 3-source coefficient (U_j(x)=(-1/2)^jprod_iinom{s_i+x_i}{j}) for (s=(2m,3m,4m)), prime (p=6m+1ge7), and its weighted sum (mathcal W_p(v)=sum_{j<p}(6j+1)U_j(pv)). Let (A=sum_j(6j+1)
abla U_j(0)inmathbf Z_{(p)}^3), (H=sum_j(6j+1)
abla^2U_j(0)in M_3(mathbf Z_{(p)})). These are the exact labelled jets established in the preceding second-digit theorem.

**Theorem.** For any p-local vector (delta) satisfying (Acdotdeltaequiv0pmod p), any p-local base (v) and any p-local (lambda), the second-digit difference has the explicit quadratic form
[
 oxed{rac{mathcal W_p(v+lambdadelta)-mathcal W_p(v)}{p^2}
 equiv lambda k_p+lambda^2c_ppmod p,quad
 k_p=rac{Acdotdelta}{p}+v^{mathsf T}Hdelta,quad
 c_p=	frac12delta^{mathsf T}Hdelta.}
]
This follows by substituting (lambdadelta) in the proved p³ Taylor formula. For each fixed (delta,v), if (c_p
e0) and (k_p
e0), there is an explicit distinct nonzero second-digit **re-coalescence** parameter (lambda_*=-k_p/c_p). It preserves the full weighted scalar modulo p³, although it need not preserve the labelled source coefficients.

## Exact original-path tests and information-loss witness

For the original input (v_*=(-1/3,-1/2,-2/3)) and the observed first-digit kernel direction (delta=(1,0,1)), both (Acdotdeltaequiv0mod p) and the following triples are verified independently using the previously published p³ integer sum and the Hessian recursion:

| p | k_p | c_p | nonzero λ_* | W_p(v_*+λ_*δ)-W_p(v_*) mod p³ | labelled j=1 change /p mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 4 | 5 | 7 | 0 | 8 |
| 19 | 10 | 10 | 18 | 0 | 5 |
| 373 | 134 | 67 | 371 | 0 | 187 |

In all three examples, the complete weighted scalar agrees **through p³** for two distinct parameterized source inputs. The original labelled j=1 term responds as (lambda_*,partial_delta U_1=lambda_*b/2
e0mod p), so those inputs differ already at precision p² coefficientwise. This is an exact bounded certificate that two scalar digits do not reconstruct the full labelled source. It does not say that the authentic LIFT conjecture fails, nor that two scalar digits are insufficient for a separately proved smaller observation horizon.

The attached independent check reuses the published `d25_source_second_jet_lift_20261106.py` implementation and asserts the six exact modular relations. A symbolic proof of the outer kernel relation (T_1+T_3=0mod p) for *all* p=6m+1 is still open (207/207 finite checks in the preceding result). The next mother-objective action is to retain the necessary source information when deriving the compensated Theta telescope, then obtain same-original-class native H0/B0, [X]U mod p² and Frobenius eta/kappa for the frozen (Delta_p-R_p) target.
