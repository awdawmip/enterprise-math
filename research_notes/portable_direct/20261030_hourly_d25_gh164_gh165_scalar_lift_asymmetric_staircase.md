# D25/LIFT GH-164–GH-165: asymmetric p-adic staircase and lossless second-digit observer

2026-10-30. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**.
Author-side logical Research lane: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Actual task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; P000 ACTIVE_LOCKED and frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Correct frozen target (not the GH-163 reflected polynomial)

Primes p=6m+1 with p modulo 24 in {13,19}. Define B_0=1, B_(k+1)/B_k=(6k+1)(3k+1)/(36(k+1)^2), and
g=sum_(0<=k<p) B_k, h=sum_(0<=k<p) (12k+1) B_k, G=g/p, Delta_p=(Gh-1)/p mod p.
The accepted parent supplies p|g and UR: Gh=1 mod p. The **unproved** second-digit hard target is Delta_p=R_p^(original) mod p in both residue classes. In particular the previous GH-163 reflected R_p(z) and exceptional p=3347 (3347 mod 24=11, OUTSIDE this Task) do NOT establish this target. Preserve the original R_p and the frozen p-adic/Frobenius/eta/experimental obligations.

## GH-164: exact valuations and strictly lower-precision equivalent carrier

Exact rational expression:
B_k=(1/6)_k (1/3)_k / ((k!)^2 2^k).
For 0<=j<=p-2, denominators are p-units. The **only** numerator multiples of p occur at 6m+1=p (j=m) and 3(2m)+1=p (j=2m), each exactly once. Therefore
v_p(B_k)=0 for 0<=k<=m; =1 for m<k<=2m; =2 for 2m<k<p.

Set g_< = sum_(k=0)^(2m) B_k, h_< = sum_(k=0)^(2m) (12k+1)B_k, and
T_p=sum_(k=2m+1)^(p-1) (B_k/p^2) mod p.
The exact congruences g=g_<+p^2*T_p (mod p^3), h=h_< (mod p^2) imply the **theorem**
    Delta_p = [((g_</p) h_< -1)/p] + (h_< mod p) T_p  (mod p).   (A)
The divided fractions are p-integral: p|g_< and (g_</p)h_<=1 mod p, by the parent UR.

Moreover if U_0=sum_(0..m)B_k, V_0=sum_(0..m)(12k+1)B_k, U_1=sum_(m+1..2m)B_k/p, V_1=sum_(m+1..2m)(12k+1)B_k/p, then
    g=U_0+p U_1+p^2*T_p (mod p^3),
    h=V_0+p V_1 (mod p^2).
Thus mod p^3 arithmetic only on the first m+1 raw terms, mod p^2 on the middle block AFTER dividing by p, mod p on the tail AFTER dividing by p^2. This is a strict reduction of required precision and retained observations; it is NOT an all-prime LIFT proof.

## GH-165: explicit finite-field hypergeometric tail and exact safe-quotient criterion

Let k0=2m+1. Removing the two exact p numerator factors gives the nonzero finite-field seed
    c0 = [product_(j=0..2m,j!=m)(6j+1) * product_(j=0..2m,j!=2m)(3j+1)] / [36^(2m+1) * ((2m+1)!)^2] mod p.
The shifted normalized tail obeys c_(r+1)/c_r = ((r+5/6)(r+1))/(2(r+5/3)^2), hence
    T_p = c0 * sum_(r=0)^(4m-1) [(5/6)_r(1)_r / ((5/3)_r^2*2^r)] mod p.   (B)
This is an EXACT TERMINATING finite-field expression; all denominators up to r=4m-1 are units. Do not extend the range: the next factor of the denominator vanishes at r=4m.

If Delta_p^< = [((g_</p)h_<-1)/p] mod p, then
    Delta_p-Delta_p^< = (h_< mod p)*T_p mod p.
Because UR proves h_< mod p is a UNIT, the exact observer-preservation law is
    Delta_p = Delta_p^<   IF AND ONLY IF   T_p=0 mod p.   (C)
Deleting the p^2 tail symmetrically from g and h is generally UNSOUND after the operation divide g by p and then read the second digit. This is a concrete BRC COMPOSE_APPLIED carrier: (p, residue class, original k, exact p-valuation, numerator/denominator provenance, g_< mod p^3, h_< mod p^2, T_p mod p, divided-digit operation). The result is auxiliary p-adic mathematics and not a native six-axis/three-dimensional-slice theorem.

## Executed exact evidence / falsification boundary

Python standard-library checker d25_gh164_asymmetric_lift_cutoff_check.py performed four cross-checks at every target prime below 5000: whole 0..p-1 recurrence mod p^3, prefix+Fp tail, independently partitioned three-level recurrence, shifted hypergeometric tail. All 166 target primes passed; p|g and UR were checked at each. Exact representative (p: full Delta; prefix Delta; T; hbar; lost Delta):
13: 0;4;8;6;9
19: 12;6;10;12;6
37: 11;1;8;29;10
109: 50;97;40;7;62
157: 82;82;0;80;0.
Of these 166, T was nonzero for 165, zero at p=157 only. No infinite nonvanishing/density conclusion. An additional exploratory check found the related weighted hypergeometric W_p=p mod p^3 for these 166; this is NOT a theorem or a LIFT proof, and is not used in (A)-(C).
Actual program terminal: PASS_GH164_ASYMMETRIC_SECOND_DIGIT_CUTOFF_EXACT. Exact universal statements (A)-(C) are algebraic proofs; the finite test verifies implementation and instances only.

## Next smallest unfinished science / process boundary

Read the exact Source-original R_p definition from the canonical frozen target, transform its terms into (U_0,V_0,U_1,V_1,T_p), and either prove R_p equals expression (A) for BOTH p mod24 classes or find an independently checked counterexample. Distinguish this from the earlier reflected R_p(9). Preserve phi_xx, H0/B0 divided-power, [X]U mod p^2, semilinear Frobenius/eta and native p373 proof and experiment obligations. No current native Researcher CLAIM/OPEN/checkpoint, independent review, task completion or mathematical admission is claimed. Historical sessions/uploads/requests and maintenance identity untouched.