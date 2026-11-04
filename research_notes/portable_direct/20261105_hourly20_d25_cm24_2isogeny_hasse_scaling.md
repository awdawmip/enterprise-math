# D25: CM(-24) normalized 2-isogeny to p-Frobenius, differential square class and Hasse scaling

Date: 2026-11-05. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. **AUTHOR-DERIVED / EXACT ALGEBRA / FINITE-EXACT CHECKED / UNREVIEWED / NOT_ADMITTED**. This is an auxiliary CM Legendre observer, not a native p373 H0/B0 crystalline experiment.

## 1. Explicit 2-isogeny to p-Frobenius

Let Q(t)=t^4−140t^3+294t^2−140t+1, p>=5 a prime with p≡5 (mod8), and A_p=F_p[t]/Q. The four roots of Q are distinct and avoid 0,1,−1. For E_t: y²=x³−(1+t)x²+tx, the kernel (0,0) induces the separable degree-two isogeny

    X=x−(1+t)+t/x; Y=y(1−t/x²);
    E'_t: Y²=X³+2(1+t)X²+(1−t)²X,

whose differential is normalized exactly: phi*(dX/(2Y))=dx/(2y). The earlier 2026-11-05 first-unit report proves j(E'_t)=j(E_t)^p in A_p.

From the exact Frobenius-Mobius action on Q, let f=t^p in A_p:

    f=(7−5t)/(5−7t)  if p≡5  (mod24);
    f=(5−7t)/(7−5t)  if p≡13 (mod24).

These denominators are units: Res(Q,7t−5)=Res(Q,5t−7)=576. Define s=−(1+f)/(2(1+t)). It obeys 2(1+t)s=−(1+f) identically, and the second necessary relation s²(1−t)²=f has the following **exact rational polynomial certificates**:

    s²(1−t)²−f = Q(t)/[(1+t)²(7t−5)²], p≡5 (mod24);
    s²(1−t)²−f = Q(t)/[(1+t)²(5t−7)²], p≡13(mod24).

Thus both vanish in A_p. After adjoining v with v²=s, the map

    psi: (X,Y) -> (x_f=sX, y_f=v³Y)

is an exact geometric isomorphism E'_t -> E_f, where E_f: y_f²=x_f(x_f−1)(x_f−f). Consequently psi∘phi:E_t -> E_{t^p} is an explicit degree-two geometric isogeny. The normalized differential pullback is

    (psi∘phi)*(dx_f/(2y_f))=v^(−1) dx/(2y).

The geometric isomorphism depends on the chosen root v. The square class s, twist and differential scaling are retained as observations. They are **not** identified with the frozen native crystalline Frobenius normalization eta.

## 2. Frobenius norm and Hasse scaling

The Frobenius permutation of the roots of Q has order two: f^p=t. Hence

    s^p=−(1+t)/(2(1+f)),    s*s^p=1/4

in A_p. This is the exact norm-like relation for the selected degree-two bridge, retaining semilinear direction.

Set m=(p−1)/2, H_p(t)=sum_{k=0}^m binom(m,k)^2 t^k. Since p≡5 (mod8), m is even, and H_p is the Legendre Hasse coefficient of [x(x−1)(x−t)]^m in the chosen invariant-differential frame. A separable isogeny of degree prime to p whose differential pullback is one preserves this Hasse scalar by functoriality of the Cartier operator. Under x_f=sX, y_f=v³Y, the Hasse coefficient scales by s^m. Therefore

    **H_p(t)^p=H_p(t^p)=s^m H_p(t) in A_p**.

For p≡5 (mod24), the CM elliptic curves have ordinary reduction at every branch, so H_p(t) is a unit; division yields the exact all-prime **split-class unit identity**

    **H_p(t)^(p−1)=s^m, for every prime p≡5 (mod24)**.

For p≡13 (mod24), CM reduction is supersingular, H_p(t)=0 in A_p, and the undivided formula remains valid.

## 3. First-jet source and open target

The rational coefficient defect delta(t)=s(t)²(1−t)²−f(t) has delta(t)=Q(t)/[(1+t)²L(t)²], L=7t−5 or 5t−7, so at any CM root a,

    delta'(a)=Q'(a)/[(1+a)² L(a)²] != 0.

This explicit first-order defect must be included before differentiating the CM-point Frobenius/isogeny equality as a family. Along with the previously proven nonzero j-family tangent defect, it provides a new exact observer for the first-jet question. **The split-class conjecture Q|C_p with C_p=16t(1−t²)H'_p+(1+2t−7t²)H_p remains open.**

Next minimal unit: compute the first derivative of the normalized isogeny/Cartier correspondence, including delta'(a) and differential scale derivative; test if it forces C_p(a)=0 for split primes. Then compare with the established Jacobi-Green-Wronskian p² readout. The frozen D24 original-class task independently still requires authenticated p373 divided-power H0/B0, [X]U mod p², rank, semilinear direction, normalization eta, native kappa and Delta_p−R_p. Native CM experiment NOT_RUN.

## 4. Verification and status

Exact Python stdlib finite quotient-ring checker `d25_cm24_2isogeny_hasse_scaling_20261105.py` ran on 2026-11-05: all 110 primes 5<=p<=3000, p≡5 (mod8); 57 split, 53 inert. PASS for two curve coefficient identities, s*s^p=1/4, undivided Hasse relation, split H unit and inert H zero. Computation is corroborating and not a native p373 crystalline run.

Predecessor author-side proof: `research_notes/portable_direct/20261105_hourly20_d25_cm24_2isogeny_frobenius_firstjet.md` at 9199ea0f69b1e9ad0c2dfa02e88b0343e3fa263f. Canonical continuation `rhourly20-20261105-0220-fresh-continuation` SUCCEEDED Source db5249f603d89ae73e556a411541e90be4add471, persisted checkpoint SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, execution_authorized=false. Previous Source checkpoint, claim, session and contribution history unchanged. No native claim/open/checkpoint/Result/review/admission asserted.
