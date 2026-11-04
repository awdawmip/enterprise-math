# D25 / CM−24: exact Frobenius-norm and 2-isogeny bridge

Date: 2026-11-05. Author-side portable theorem, **UNREVIEWED / NOT_ADMITTED**. Scientific input pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Native H0/B0 and the canonical authenticated checkpoint remain separate.

## Theorem 1: four exactly labelled CM Legendre parameters

Let a²=2, b²=3 in K=Q(a,b). For signs e,d∈{−1,+1} set

  t(e,d) = 35+24 e a+20 d b+14 e d a b.

These four numbers are the roots of

  Q(T)=T⁴−140T³+294T²−140T+1,

and under the Legendre j-invariant j(t)=256(1−t+t²)³/[t²(1−t)²],

  j(t(e,d))=2417472+1707264 e a.

In addition t(e,+)t(e,−)=1.

*Proof.* Put u(e)=3+2e a and v(e)=2b+e ab. Then v²=u²+1 and t(e,d)=(u+d v)²; reciprocal pairing follows from (u+v)(u−v)=−1. The two roots of each quadratic have sum 70+48 e a and product 1. Multiplying both quadratics gives Q. Direct substitution into the rational Legendre j-formula (clearing its nonzero denominator) yields the displayed j expression. The attached exact checker evaluates these integer identities in Z[a,b] with a²=2,b²=3.

## Theorem 2: explicit Frobenius trace and norm

For every prime p≥5, p≡5 (mod 8), the reductions of all four t(e,d) have degree exactly 2 over Fp. Their absolute p-Frobenius acts by

  t(e,d)^p = t(−e, d (3/p)).

For p≡5 (mod 24), write s=ab=√6 and note (3/p)=−1. Then

  Tr(t(e,d))=70+28 e d s,
  Nm(t(e,d))=49+20 e d s=(5+2 e d s)².

For p≡13 (mod 24), write b=√3 and note (3/p)=+1. Then

  Tr(t(e,d))=70+40 d b,
  Nm(t(e,d))=97+56 d b=(7+4 d b)².

All indicated square-root signs are **branch labels inherited from K**; their replacement by an unlabelled numerical root would lose the observer provenance.

*Proof.* Euler's criterion gives a^p=(2/p)a=−a, b^p=(3/p)b. These actions give the Frobenius permutation. Multiply t by its p-conjugate and add them to obtain the formulas. For p≡5 mod24 a fixed t would force 24 e a+20 d b=0, hence p|[(24²·2)−(20²·3)]=−48. For p≡13 mod24 fixed t would force 48+28 d b=0, hence p|[48²−28²·3]=−48. Since p≥5, neither is possible; thus t has degree 2 and these are genuine Fp²/Fp norms and traces.

## Theorem 3: exact cyclic 2-isogeny certificate

Set j±=2417472±1707264√2. Then

  Φ₂(j+,j−)=0

over Z, where the classical level-2 modular polynomial is

  Φ₂(X,Y)=X³+Y³−X²Y²+1488XY(X+Y)−162000(X²+Y²)
           +40773375XY+8748000000(X+Y)−157464000000000.

*Proof.* Use S=j++j−=4834944 and P=j+j−=14670139392. Substitution reduces the claim to the exact integer identity

  S³−P²+1485PS−162000S²+41097375P+8748000000S−157464000000000=0.

The checker computes it exactly. The classical defining property of Φ₂ yields a cyclic 2-isogeny over an algebraic closure between curves with these j-values, also after reduction at p≥5. Since (2/p)=−1, Frobenius swaps the two j-branches. This identifies an **isogeny-existence / CM Frobenius branch bridge**; the isogeny's differential pullback, twist and normalization needed for the Hasse first-jet identity remain the next mathematical question.

Polynomial coefficients and 2-isogeny interpretation: A. Sutherland, *Classical Modular Polynomials*, https://math.mit.edu/~drew/ClassicalModPolys.html ; SageMath reference https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_poly.html .

## BRC / representation / verification

Carrier: the four labels (e,d), the two distinct j-formulas, and branchwise Frobenius/isogeny. Observer: (p mod24,e,d,Tr,Nm,j,j^p,Φ₂). Preserve sign labels across coordinate change; Tr/Nm alone can forget the original embedding. This scalar CM bridge is not the task's original native divided-power H0/B0 Frobenius or odd Hesse Green observer.

An independent Python 3 standard-library test computed Q(t)=0 and the j formula exactly for four branches, Φ₂(j+,j−)=0 in integers, and 2276 branchwise Frobenius congruences over all 569 primes p≤20000 with p≡5,13 mod24 (281 split, 288 inert), all PASS. With the smallest positive square root, examples are p=29: √6=8, Tr=4, Nm=6 (mod29); p=373: √3=131, Tr=88, Nm=346 (mod373). These are finite checks supplementing the general proof.

## Next exact action

Construct the normalized cyclic 2-isogeny E_t→E_(t^p) including its differential and possible twists, then test/prove the split-class Hasse first-jet target

  16t(1−t)(1+t) H_p'(t)+(1+2t−7t²)H_p(t)=0

for p≡5 mod24. Consume the existing Jacobi–Green–Wronskian p² formula after the first-jet proof. Preserve original fixed-p=373 H0/B0, [X]U mod p², source eta/kappa and Δ_p−R_p obligations and Source-verified checkpoint. No native experiment or independent review is asserted here.
