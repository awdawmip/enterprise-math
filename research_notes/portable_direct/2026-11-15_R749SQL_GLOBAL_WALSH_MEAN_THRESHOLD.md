# R749SQL — Global resolution-39 sign threshold for the frozen Walsh source mean

Date: 2026-11-15. Status: AUTHOR_EXACT_NOT_REVIEWED. Independent auxiliary 16-atom Walsh source-fiber model; no native X6/Cell or formal shared CLAIM assertion.

## Exact input and previous frontier

Scientific pin (unchanged): awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior R749SQK: PR #2502, commit 4b6967f8eff7b6dca1ed00560372ffdd3a386dd7. The 23 labeled positive-source weights have multiplicities (m_1,...,m_7)=(3,4,6,4,3,2,1). One labeled optional source has weight h=3.

For integer r>=1 define Omega_r = {n in Z_>=0^23 : sum_i s_i n_i < r}. Under the uniform law on Omega_r, C_r=|Omega_r| and K_r is the optional source's count. Define X_r=3 K_r/r; set C_t=0 for t<=0.

## Theorem (sharp global threshold)

For every integer r>=1,

E[X_r] < 1/24 when 1<=r<=38, and E[X_r] > 1/24 when r>=39.

Thus the crossing at r=39, previously observed by R749SQK for r<=2400, is the unique crossing over all integer resolutions.

## Exact proof

Define F(z)=sum_{r>=1} C_r z^(r-1)=(1-z)^(-1)*prod_{s=1}^7(1-z^s)^(-m_s).

The source-deletion bijection gives C_r E[K_r] = sum_{k>=1} C_{r-3k}. Introduce the integer bias

B_r = 72 sum_{k>=1} C_{r-3k} - r C_r = 24*r*C_r*(E[X_r]-1/24).

Its coefficient generating function is the rational function

H(z)=sum_{r>=1} B_r*z^(r-1)
=F(z)*[72*z^3/(1-z^3) - 1 - z/(1-z) - sum_{s=1}^7 m_s*s*z^s/(1-z^s)].

Every pole lies at a 420th root of unity (each weight 1,...,7 divides 420). At z=1, F has pole order 24 and the simple-pole coefficient in the bracket cancels exactly: 72/3=24=1+sum_s m_s. The bracket has finite limit 3. Consequently H has pole order at most 24 at 1. At another 420th root, at most ten weight factors vanish (the ten even weights, 4+4+2); the bracket adds at most a simple pole, so order at most 11. Partial fractions therefore show, for each a=1,...,420, the exact integer sequence

P_a(j):=B_(a+420j), j>=0

is a polynomial in j of degree at most 23. In particular, for all j>=0 its Newton expansion is

P_a(j)=sum_{k=0}^23 D_(a,k)*binom(j,k), with D_(a,k)=Delta^k P_a(0).

The companion pure-Python certificate computes every C_r and B_r for 1<=r<=10500 by integer DP and checks the following finite statement exhaustively:

(1) B_1,...,B_38 are all strictly negative; B_39,...,B_420 strictly positive.
(2) For every a=1,...,420 and k=1,...,23, D_(a,k)>0 (9660 exact inequalities).
(3) For every a=1,...,420, D_(a,24)=0 (420 exact degree diagnostics).

Minimum first difference: 17472673285547538578923515581; minimum 23rd difference: 68937718103359214342814649958400000000000000000000. B_38=-87935832; B_39=34517412. Canonical compact JSON SHA256 of all 420x25 difference entries is d4d8578ca90824fd1458689f08932bc131430cff6e2bae3a4ae699042da755de.

For a>=39, every Newton coefficient is positive (including k=0), giving P_a(j)>0 for all j>=0. For a<=38, D_(a,0)<0 while all positive-order differences are positive. For j>=1,

P_a(j)>=D_(a,0)+D_(a,1)=P_a(1)>0,

the last strict inequality follows by the same integer DP (P_a(1) is among the computed values, and positivity also follows from the all-positive higher-difference certificate). Hence B_r>0 for every r>=39, and B_r<0 for 1<=r<=38. Since C_r>0, the theorem follows.

## Reproduction, evidence and scope

Run: python3 R749SQL_WALSH_MEAN_THRESHOLD_CERT.py > R749SQL_WALSH_MEAN_THRESHOLD_RESULTS.json. All arithmetic uses Python standard-library arbitrary-precision integers. Results were executed in this turn with status PASS. The symbolic cyclotomic degree bound plus exact finite coefficient inequalities proves the infinite assertion; no asymptotic extrapolation is used. Independent mathematics review remains pending. P000 and the ACTIVE worldview are unchanged. This source-fiber auxiliary statement does not claim native signed Cell/Link/Port equivalence.

Next: derive an analytic/injection proof of positivity that compresses the residue-class certificate; determine the earliest second-order-moment divergence of different weighted alphabets having the same (d,D,h).
