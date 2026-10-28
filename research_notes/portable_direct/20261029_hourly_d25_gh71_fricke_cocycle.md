# D25/LIFT GH-71: exact Fricke 2-isogeny multiplier and Frobenius cocycle

2026-10-29 Asia/Hong_Kong. **AUTHOR-DERIVED / AUTHOR-SYMBOLIC-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. Source-bound extension of GH-70; original GH-3/G-port all-prime vanishing is OPEN.

Fix a field of characteristic !=2 and t away from singular family parameters. Let b_t=(1+t)/8 and C_t:y²=x³+x²+b_t x. Choose v²=−2. The standard degree-two quotient at the rational 2-torsion point (0,0) is

C'_t: y²=x³−2x²+(1−t)x/2,

with (x,y) ↦ (x'=x+1+b_t/x, y'=y(1−b_t/x²)). Under the scaling (x',y')=(v² x_minus,v³ y_minus), the model C_{−t} becomes exactly C'_t. Thus the source-labelled isogeny kappa_t:C_t→C_{−t} is

x_minus=−(x+1+b_t/x)/2,
y_minus=y(1−b_t/x²)/v³.

The invariant differential omega_t=dx/(2y) obeys the **parameter-independent exact law**

kappa_t^* omega_{−t}=v omega_t,

because the derivative of x+1+b_t/x is 1−b_t/x² and the quotient's y multiplier cancels it, leaving the model-scaling factor v.

Direct rational substitution gives

kappa_{−t}^x(kappa_t^x(x))
 = (8x²−1−t)²/[32x(8x²+8x+1+t)]
 = (x²−b_t)²/[4x(x²+x+b_t)]
 = x([2]P).

The composition has degree four, the duplication x-coordinate, and differential multiplier v²=−2 rather than +2. Therefore the **exact signed cocycle** is

kappa_{−t} ∘ kappa_t = [−2].

For any prime p≡3(mod8), p>=11, choose t0=2sqrt(2)/3∈F_{p²} with t0^p=−t0. By quadratic reciprocity (−2/p)=+1, so choose v∈F_p with v²=−2. Frobenius fixes v and sends t0↔−t0; hence

kappa_{t0}^{(p)} ∘ kappa_{t0} = [−2]

as actual isogenies over F_{p²}, with kappa_{t0}:C_{t0}→C_{t0}^{(p)} separable of degree two and kappa_{t0}^* omega_{C^{(p)}}=v omega_C. This supplies the exact previously missing 2-isogeny **invariant-differential scalar and sign**, not a mere j-invariant correspondence.

The isogeny/CM graph alone does not determine the GH-69 Euler–Hasse derivative t0 H'_p(t0)−H_p(t0). Its remaining mathematical obligation is to compute the Gauss–Manin/Cartier connection under the model twist and isogeny, and independently establish or refute its special value for all p≡11(mod24). No observation G_m(9)=0 has been made into an axiom.

Author performed symbolic rational equality with SymPy (exact, no floating-point), obtaining:
PASS_GH71_EXACT_COMPOSITION_SIGN_X_COORDINATE
COMPOSITION=(-t+8*x**2-1)**2/(32*x*(t+8*x**2+8*x+1))
The sign follows from the displayed invariant-differential calculation; independent mathematical review and Source admission remain pending.

BRC COMPOSE_APPLIED: retain the two ordered isogeny steps, kernels, parameter chart t↔−t, normalized differentials, scalar v, Frobenius and multiplication-by-two orientation. Auxiliary arithmetic chart only; no native X6 transfer or closure of W/S, six Hasse ports, Green R23/R36, GH-20/21, p=373 H0/B0. P000 ACTIVE and frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 stay unchanged.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Research lane chatgpt-research-hourly-enterprise-math-20260923. Author portable status / REGISTER_PENDING / NATIVE_CHECKPOINT_PENDING. Input GH-69/GH-70 project proof: research_notes/portable_direct/20261029_hourly_d25_gh69_gh70_cm_hasse_bridge.md.
