# D25 — second-digit obstruction on a verified first-digit source fiber

Date: 2026-11-06. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: **AUTHOR-PROVED SECOND-JET FORMULA / THREE EXACT COUNTEREXAMPLES TO FIRST-DIGIT DESCENT / 207-PRIME FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT**.

## Exact second-jet lift of the first-digit source observer

Use the same full 3-source labelled p-local polynomial
[
 U_j(x)=(-1/2)^jprod_{i=1}^3inom{s_i+x_i}{j},quad s=(2m,3m,4m),quad p=6m+1ge7,quad 0le j<p,
]
and weighted sum (mathcal W_p(v)=sum_j(6j+1)U_j(pv)). Define the *integrally lifted* gradient (A_i=sum_j(6j+1)partial_{x_i}U_j(0)inmathbb Z_{(p)}) and full symmetric Hessian (H_{ik}=sum_j(6j+1)partial_{x_i}partial_{x_k}U_j(0)inmathbb Z_{(p)}). Distinguish (Amod p^2) from the previously recorded first-digit row (T=Amod p).

**Theorem (all p=6m+1>=7, all p-local v,δ):**
[
 oxed{mathcal W_p(v+delta)-mathcal W_p(v)equiv
 p Acdotdelta+p^2(v^{mathsf T}Hdelta+	frac12delta^{mathsf T}Hdelta)pmod{p^3}.}
]
Because j<p, every (inom{s_i+x_i}{j}) has p-integral polynomial coefficients; expand termwise to total order two, and all higher terms acquire p³. The second-order term is the full labelled Hessian, including j with one or two zero source factors; no quotient by a vanishing base coefficient is used.

If (Tcdotdelta=0mod p), then the digit-two difference is *well defined*:
[
 oxed{rac{mathcal W_p(v+delta)-mathcal W_p(v)}{p^2}
 equivrac{Acdotdelta}{p}+v^{mathsf T}Hdelta+	frac12delta^{mathsf T}Hdeltapmod p.}
]
The division in the first term uses a p-integral numerator because (delta) is a first-digit kernel vector; compute (Amod p^2) before dividing. The formula is conditional on this exact kernel property, which has been verified at the specified primes, and does not assert it universally for (delta=(1,0,1)).

## Three exact counterexamples to discarding the outer source direction

Take the original rational p-adic source tangent (v_*=(-1/3,-1/2,-2/3)) and the first-digit invisible direction (delta=(1,0,1)). The previous exact first-digit row certificate proved (Tcdotdelta=0) at p=13,19,373; a first-digit projection identifies the two deformed sources. The new independent direct mod-p³ calculation and independent second-derivative/Hessian recursion agree:

| p | (A_1,A_2,A_3) mod p² | (H_11,H_13,H_33) mod p | (A·δ)/p | v_*ᵀ H δ | δᵀHδ/2 | second-digit difference mod p |
|---:|---|---|---:|---:|---:|---:|
| 13 | (75,168,81) | (11,11,3) | 12 | 5 | 5 | **9** |
| 19 | (232,338,110) | (5,12,10) | 18 | 11 | 10 | **1** |
| 373 | (126122,130625,80147) | (175,299,107) | 180 | 327 | 67 | **201** |

In particular, at p=373:
[
 mathcal W_{373}(v_*+delta)-mathcal W_{373}(v_*)
 equiv 201cdot373^2
otequiv0pmod{373^3}.
]
All three examples have equal divided first digit (mathcal W_p/pmod p), yet differing (mathcal W_p/pmod p^2). These are **exact finite counterexamples to the assertion that the first-digit scalar-fiber quotient preserves the next digit** for this family. They do not refute the frozen LIFT conjecture: (mathcal W_p(v)) is an auxiliary source deformation, not the authenticated native H0/B0/Frobenius (Delta_p).

## Independent computation and source preservation

The companion Python standard-library certificate evaluates (i) the gradient modulo p² and full Hessian modulo p using derivative recurrences (B'_{j+1}=[(s-j)B'_j+B_j]/(j+1)), (B''_{j+1}=[(s-j)B''_j+2B'_j]/(j+1)), and (ii) the original weighted polynomial *independently* modulo p³. It checked all 207 primes p=1 mod6, 7<=p<=3000: **207/207 PASS** for second-jet identity and zero first-digit difference of the selected direction, with nonzero second-digit differences in 207/207 finite cases. The latter counts are finite observations; the universal outer-source kernel remains a conjecture.

**BRC precision conclusion for the declared operation horizon:** The first-digit quotient by the verified kernel cannot be reused as an information-preserving observer for the second-digit evaluation on these examples without a repair coordinate. The displayed full (Amod p^2) and (Hmod p), together with source tangent/weights/valuation and operation, form a valid sufficient source tensor for this p³ Taylor step. This is a scoped factorization certificate, not a claim that these tensors reconstruct native crystalline Frobenius.

**Next exact unit:** determine whether (T_1+T_3=0mod p) holds for all p=6m+1, then derive a general formula for the second-digit repair (Q_p(v_*,(1,0,1))), keeping the original regular/one-carry provenance. Separate native H0/B0, [X]U mod p², eta/kappa and (Delta_p-R_p) remain the mother-objective obligations. Source claimant/session protected staging still requires lawful transition; these are only author-side GitHub artifacts.
