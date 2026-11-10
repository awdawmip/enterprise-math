# D25 — Original Clausen cutoff second carry at the fourth p-adic digit

At: 2026-11-10 (+08:00). Research classification: AUTHOR_SIDE_PROVED / COMPUTATION_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.
Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source input: c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane only: chatgpt-research-onhour-enterprise-math-20260923.

## Actual unfinished question

The original accepted LIFT observer is Delta_p-R_p modulo p, with the native signed Clausen cutoff retained; the previous original-source port alignment proved R_p = Q_p/p² (mod p). The four-grade W216 p⁴ author certificate yields the fourth scalar digit, but not an observer-faithful breakdown into the original Clausen cutoff and bulk. This unit gives the complete next p-adic digit of that exact original cutoff, and compares the two corresponding signed carries. No claim is made about a native H0/B0 Frobenius readout.

## Definitions and exact theorem

Let p=6m+1>3 be prime, work over Z_(p), and put

  B_n = ((1/6)_n (1/3)_n)/(2^n (n!)²)  (0<=n<p),
  M = sum_(n<p) B_n, N = sum_(n<p) n B_n, h=M+12N,
  W = sum_(k<p) (6k+1) ((1/2)_k(1/3)_k(2/3)_k)/(2^k(k!)³).

The previously established finite Clausen identity is W=Mh-Q, where Q is the ORIGINAL ordered signed cutoff
  Q = sum_(0<=i,j<p, i+j>=p) (6(i+j)+1) B_i B_j.

For 1<=a<=2m define the p-integral grade-two units
  v_a = B_(p-a)/p² (mod p²).

Then v_1 is exactly the p-local quotient B_(p-1)/p² (mod p²) and, for 1<=a<2m,

  v_(a+1) = v_a * 36(p-a)² / ((6p-6a-5)(3p-3a-2))  (mod p²).   (1)

Every denominator in (1) is a p-unit. In particular v_1=1/10 (mod p) and
  v_(a+1)/v_a = 36a²/((6a+5)(3a+2))
     * [1+p(-2/a+6/(6a+5)+3/(3a+2))] (mod p²).               (2)

The complete *original* signed cutoff through its second digit is

  R2 := Q/p² (mod p²)
    = L + C (mod p²),                                         (3)

  L = 2 sum_(i=1)^m B_i sum_(a=1)^i [6p+6(i-a)+1] v_a  (mod p²),
  C = 2p sum_(i=m+1)^(2m) (B_i/p)
          sum_(a=1)^i [6(i-a)+1] (v_a mod p)          (mod p²).

Equation (3) is a theorem for ALL primes p=6m+1>3; it does not presume W=p (mod p³). It simultaneously retains the i-index, reflected a-index, sign and p-carry of the original cutoff. Its reduction modulo p is the pre-existing frozen R_p, since C=0 (mod p), v_a=C_a (mod p) for a<=m, and 6p drops out only at this declared precision.

### Proof

The two rising factorials contain p at factors indexed m and 2m respectively, so v_p(B_n)=0 for n<=m, 1 for m<n<=2m, and 2 for 2m<n<p. No denominator n! contains p. The exact B-step ratio is
  B_(n+1)/B_n=(6n+1)(3n+1)/(36(n+1)²).
Reversing the index n=p-a gives the exact recurrence (1); expansion of its four linear factors gives (2), including the signed first-order correction. The seed v_1 is an unambiguous exact rational product, not a fitted experimental constant. Its mod-p value 1/10 can also be proved without numerical fitting: for n=p-1 the products of the 6j+1 and 3j+1 factors (0<=j<=p-2) contain a unique factor p, respectively at j=m and j=2m. After removing those factors, the remaining numerator residues traverse F_p^* with exactly -5 and -2, respectively, omitted. Wilson's theorem thus gives ((1/6)_(p-1))/p = 1/5 (mod p) and ((1/3)_(p-1))/p = 1/2 (mod p); 2^(p-1)((p-1)!)^2=1 (mod p). Therefore v_1=1/10 (mod p).

For the ordered cutoff i+j>=p, two indices both <=2m cannot contribute, since i+j<=4m<p. Two indices both >=2m+1 have total p-valuation at least 4 and therefore vanish modulo p⁴. Each surviving ordered pair has one index i<=2m and the other j=p-a>=2m+1, with 1<=a<=i, and the symmetric swap contributes the factor 2. For i<=m, B_i has grade 0, hence the grade-two product survives with its full p² jet and the EXACT weight 6p+6(i-a)+1; this is p² L. For m<i<=2m, B_i has grade 1, so its product with grade two is divisible by p³, requiring only leading units and weight modulo p; this is p² C. These are all possibilities. Division of Q by p² before reduction proves (3) coefficientwise. No sum is changed to an unsigned count.

## Original source-port fourth-digit identity

Only on the frozen target classes p=13 or 19 (mod 24), consume the existing CM0/UR premise p | M and Gh=1 (mod p) where G=M/p. Define
  Delta2 = (Gh-1)/p (mod p²), R2=Q/p² (mod p²).
Then the EXACT rational identity W=pGh-Q gives
  Delta2-R2 = (W-p)/p² (mod p²).                               (4)
Its mod-p reduction is the frozen old Delta_p-R_p observer, with R_p=R2 mod p. In any case with W=p (mod p³), choose canonical residues 0<=Delta2,R2<p² and define
  dDelta=(Delta2-(Delta2 mod p))/p, dR=(R2-(R2 mod p))/p.
The observed fourth scalar digit is
  (W-p)/p³ = dDelta-dR (mod p).                                 (5)
This is conditional on the actual third-digit congruence, not a new universal proof of it. Equation (5) preserves two distinct bulk/cutoff carries. It neither replaces the original R_p by zero nor identifies a normal 3F2 scalar with a native odd Green/Hesse operator.

## Exact executable checks (author, not independent review)

Checker: research_notes/portable_direct/d25_original_Q_second_carry_20261110.py.
Executed finite check: 80 primes p<=1000, p=1 (mod 6), all (1) and (3) PASS. Independent original integer-binomial W and direct ordered double cutoff Q were additionally checked at p=13,19,37,43,373,997. Computations are exact integer modular arithmetic, with p-unit inverses and division by p² BEFORE reduction; no float.

Selected p=373 modulo p²=139129:
  v1=28460;
  L=7283 =196+19*373;
  C=58561 =157*373;
  R2=65844 =196+176*373; Delta2=11759 =196+31*373.
Thus the frozen first observer agrees, Delta=R=196, but the new second carries differ: dDelta=31 and dR=176; (31-176) mod 373=228. The independent W216 sum gives W_373=11832087049 (mod 373⁴), with (W_373-373)/373³=228. This p⁴ boundary residual is NONZERO; it is not a counterexample to the target modulo-p LIFT (whose residual is zero).

Another control p=19: L=183, C=38, R2=221=12+11*19, Delta2=88=12+4*19, fourth digit 4-11=12 (mod 19). Nonzero middle-grade contributions prove a low-high-only truncation is unsafe at p⁴ precision.

## BRC and continuation

BRC resolution: COMPOSE_APPLIED. Carrier: labeled ordered (i,j), valuation pair (0,2) versus (1,2), reflected a=p-j, p-local units, original signed weight, and jet horizon p⁴. Future observable: (Delta2,R2,dDelta,dR), then the original Delta-R and the native class. The quotient R_p alone loses the nonzero cutoff carry 176 at p373. Preserve the proven reflection recurrence (2) rather than replacing it with an unsigned convolution or merely an absolute norm. This is external rational-number arithmetic; no native X6 plane or three-dimensional slice is inferred.

Next science unit: seek a signed WZ/Jacobi telescoper for the **difference of the bulk jet and this original cutoff second jet**, not a fifth auxiliary coefficient atlas. The highest native p373 H0/B0 divided-power [X]U mod139129, rank, Frobenius direction/eta, odd signed kappa, Delta-R and independent reproduction remain NOT_RUN / PENDING_OWNER under Issue #1559. This proof/finite certificate is AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED; no own verified CLAIM, run, Source-native checkpoint, Result or independent Driver acceptance is inferred.
