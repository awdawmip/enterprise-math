# D25/LIFT: source-preserving first-order p-adic Dwork block lift of original weighted A216

Date 2026-10-29; AUTHOR-SIDE / EXACT HAND PROOF / INTEGER EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE H0/B0 NOT EXECUTED. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science Source c47e13e4aba0e006366f989d6334d443f6333ae3 (not rebased). Ordinary Research lane chatgpt-research-onhour-enterprise-math-20260923, not maintenance lane. Source claim/session/run/request IDs not established by this read-only Site.

## Original input and theorem

Use the original coefficients a_n=binom(2n,n)^2*binom(3n,n)/216^n=(1/2)_n(1/3)_n(2/3)_n/[2^n(n!)^3], with original signed weight w_n=(6n+1)a_n. Fix any prime p>=5 and integers u>=0, 0<=r<=floor((p-1)/3). Let the Fermat quotient q_p(216)=(216^(p-1)-1)/p modp. Let D_r=sum_{j=0}^{r-1}{1/(j+1/2)+1/(j+1/3)+1/(j+2/3)-3/(j+1)} modp (D_0=0). Every displayed denominator is a p-adic unit in this exact range.

**Proved universal supported-digit first-order block lift:**
a_{pu+r} = a_u*a_r*[1+p*u*(D_r-q_p(216))] mod p^2.
**Proved original signed-observer companion:**
w_{pu+r} = a_u*a_r*[(6r+1)+p*u*(6+(6r+1)*(D_r-q_p(216)))] mod p^2.

At r=0 these become a_{pu}=a_u(1-pu q_p) and w_{pu}=a_u[1+pu(6-q_p)] modulo p^2. The 6pu signed-observer contribution must not be dropped.

## Proof

For arbitrary integers A>=B>=0, write (1+x)^p=1+x^p+pG_p(x), where G_p is integral and supported only at degrees 1..p-1. Mod p^2, (1+x)^(Ap)=(1+x^p)^A+Ap(1+x^p)^(A-1)G_p(x). The correction has no x^(Bp) term, hence binom(Ap,Bp)=binom(A,B) modp^2, for all A,B without a nonunit division. Apply this twice, to the original integer factors binom(2pu,pu)^2 and binom(3pu,pu), to get a_{pu}=a_u*216^{-u(p-1)}=a_u*(1-pu q_p) modp^2, even when a_u itself is nonunit.

Use the exact recurrence a_{n+1}/a_n=f(n)=[(n+1/2)(n+1/3)(n+2/3)]/[2(n+1)^3]. For each 0<=j<r<=floor((p-1)/3), all factors in f(j),f(pu+j) are p-units. Thus f(pu+j)/f(j)=1+pu*[1/(j+1/2)+1/(j+1/3)+1/(j+2/3)-3/(j+1)] mod p^2. Multiplication over j<r gives a_{pu+r}/a_{pu}=a_r(1+pu D_r) mod p^2, and composition gives the coefficient lift. Multiplying by the *original* 6(pu+r)+1=(6r+1)+6pu proves the weighted statement. This does not rely on Dwork as an unproved black-box axiom.

## Reproduction

The accompanying exact stdlib Python guard computes original integer binomial coefficients and independent right-hand predictions, including signed weights, 45 primes p<220, u=0..4 and every supported r; it also independently checks binom(Ap,Bp)=binom(A,B) modp^2 for A=1..7, B<=A, and six p=373 witnesses. Actual output:
PASS_A216_FIRST_ORDER_P2_WEIGHTED_DWORK_BLOCK_LIFT 7506 instances 45 primes p<220 and p373
PASS_BINOM_AP_BP_MOD_P2 1575 combinations
P373_FERMAT_QUOTIENT_216 23
P373_WEIGHTED_WITNESSES (u,r)=(1,0): a30441/w123318/D0; (1,1): a87792/w86376/D190; (1,62): a74441/w2238/D119; (2,62): a6168/w135026/D119; (3,62): a103242/w135772/D119; (4,124): a53700/w108182/D49.
All p373 figures are modulo p^2=139129 except D_r modulo373.

## Exact continuing scope

The theorem holds only for first-digit-supported r<=floor((p-1)/3); higher r have their own one-/two-hit valuations and must remain distinct. This is an original-ratio *auxiliary* result, not a proof of the frozen five-port p^3 identity, not a native six-dimensional P000/BRC dynamics claim, and not a H0/B0 divided-power execution. Consume prior authors' exact Theta_p reflection and the six-port original A216 ledger without re-derivation or re-attribution. The outstanding hard target for ALL primes p=13,19 mod24 stays T00+T01+T02+T10+T11=p-p^2 Theta_p modp^3; next mathematical step is a p^3 digit-block lift retaining the one- and two-hit branches, or direct finite WZ/CM character-sum cancellation.

Native capability request #1559 OPEN and unassigned at this run: original p373 same-original-class H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius, odd Green/Hesse signed observer, kappa, Delta-R and independent acceptance witnesses require authorized native executor. The v0.6.11 Site read-only connection has Researcher authority false and write relay false, original request/claim/run/session UNKNOWN, so this is only GitHub author-side evidence, not Source checkpoint, Result, review, admissibility or identity grant. No maintenance conversation operation or new scheduler. P000/ACTIVE worldview/source pin unchanged.
