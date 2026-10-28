# D25 finite Cauchy second jet: three signed p³ overflow layers (author-only)

2026-10-27. AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, taskbook blob 53a3ef039325534e3715add837f0eee332289984. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Same shared author context as this PR, NOT independent. Auxiliary hypergeometric model, NOT native H0/B0.

## All-prime theorem

Let p>=5 be prime; m=(p-1)/2, a=floor((p-1)/3), b=ceil(2p/3), c_k=(3k)!(2k)!/[216^k(k!)^5], C(z)=sum_{k<p}c_k z^k, W=sum_{k<p}(6k+1)c_k, u_j=binom(2j,j)/8^j, S=sum_{j+k<p}(3j+3k-1)u_j c_k.
Set P(z)=(1-z/2)^m, L(z)=sum_{1<=i<p}z^i/(i*2^i), C0=sum_{k<=a}c_k z^k, C01=sum_{k<=m}c_k z^k, C2=sum_{m<k<b}c_k z^k, T_p(F)=sum_{n>=p}(3n-1)[z^n]F(z) (SIGNED high-degree cutoff). Put rho=2^(-m-1), ell=L(1), d=L'(1)=1-2^(-(p-1)), E=1+(p/2)ell+(p²/8)ell².

Then in Z_(p) modulo p³, **for every prime p>=5**:

S = rho*[(W-3p C(1))*E+3p C(1)*d] - T_p(P C2) - (p/2)T_p(P C01 L) - (p²/8)T_p(P C0 L²).

The three signed tails need precision p³, p², p respectively. There is no legitimacy to discard them or replace the triangular cutoff by full evaluation. The zero-th tail is supported only on the narrow valuation strip m<k<ceil(2p/3).

## Proof

The formal identity (1-z/2)^(-1/2)=P(z)exp((p/2)*[-log(1-z/2)]) yields, coefficientwise in degrees n<p,
sum_{j<p}u_j z^j = [P(z)(1+(p/2)L(z)+(p²/8)L(z)²)]_{<p} (mod p³,z^p).
All logarithmic denominators i<p and exponential factorials up to degree n<p are p-units. All omitted exponential terms have p³ factor. Applying the finite operator O_{<p}(F)=sum_{n<p}(3n-1)[z^n]F recovers the original triangular S.

Legendre factorial valuation, for k<p, gives v_p(c_k)=floor(3k/p)+floor(2k/p), taking respective values 0 for k<=a, 1 for a<k<=m, 2 for m<k<b, and 3 for b<=k<p. Since deg P=m, any degree >=p coefficient of PC has k>m. Thus, exactly to the required powers, the three high-degree tails reduce to T_p(PC2), T_p(PC01 L), and T_p(PC0 L²) respectively.

For the *full* polynomials, product differentiation at z=1 and 6m+3=3p give
(3theta-1)(PC)(1)=rho(W-3p C(1)),
(3theta-1)(PCL)(1)=rho[ell(W-3p C(1))+6 C(1)d],
(3theta-1)(PCL²)(1)=rho[ell²(W-3p C(1))+12 C(1)ell d].
Here theta=z*d/dz. By Fermat d=1-2^(-(p-1)) is divisible by p, so the final ell*d term, multiplied by p²/8, is zero modulo p³. Subtract the three high-degree tails. QED.

## Verified finite arithmetic, limits, BRC

The author-side standard-library checker evaluates both the original triangular sum and second-jet polynomial identity, all three valuation support equalities, and the derived full-expression formula, over 17 primes: 5,7,11,13,19,31,37,43,61,67,73,79,103,109,211,373,997. PASS. Among checked primes with p²|(S-W), the *finite*, not all-prime, residues (S-W)/p² mod p are 13:0,19:9,37:11,43:22,61:42,67:29,109:25,211:172,373:61,997:490. The quotient is undefined for control cases p=7,31,73,79,103 (p² does not divide S-W). No target-class universal p² divisibility or LIFT p³ proof follows from finite checks.

BRC carrier: signed index-pairs (j,k), labeled valuation strata C0/C01/C2, observer the degree-<p (3theta-1) operation at z=1, exact horizon p³; source labels retained in each tail. This is precise reuse of preceding finite Cauchy and first-jet proofs, not a new original-source identity or independent mathematical review. External auxiliary z is NOT a P000 native X6 coordinate.

## Real remaining frontiers

Prove/disprove target-class universal p² tail cancellation and derive the third-digit residual law; separately obtain genuine original H0/B0 and Frobenius transfer (native p=373 benchmark on issue #1559). UR V2 exact original 94687-byte bundle with SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains unrecovered; do not reprove UR or assign provenance to a different bundle. Gateway 0.6.11 currently reports quota 5/5 active and no executor binding; old request receipts return CONTROL_REQUEST_NOT_FOUND; own Source CLAIM/OPEN/checkpoint unverified. Not a native Result, formal publication, independent review, or admitted theorem. For CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS seed preserve predecessor completed_units=[]; author proof is current staged evidence, not predecessor completion. Reconcile only lawful exact Source continuation when access returns, with same task and frozen pins; no identity/channel bypass.