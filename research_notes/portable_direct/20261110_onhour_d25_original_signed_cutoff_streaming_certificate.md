# D25 — Original signed Clausen source observer: linear-time, constant-word-space certificate

Status: AUTHOR_SIDE / MATHEMATICAL_IDENTITY_PROVED / COMPUTATION_CHECKED / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.
Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific input Source: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research lane: chatgpt-research-onhour-enterprise-math-20260923. No Maintenance identity used.

## Actual open parent objective

Prove the frozen original signed Delta_p-R_p=0 (mod p) for p=13 or 19 (mod 24), and separately acquire the native same-class H0/B0 divided-power [X]U (mod 139129), rank, signed kappa and Frobenius normalization for p=373. This unit changes the computational treatment of the ORIGINAL ordered signed cutoff, not its definition; the Source-native experiment is still pending. It consumes rather than repeats the previous original Q second-jet theorem of 2026-11-10.

## Precise new algorithmic claim

For every prime p=6m+1>3, in Z/(p^4) put

B_0=1,   B_(k+1) = B_k (6k+1)(3k+1) / [36(k+1)^2],  0<=k<p-1,
M=sum_(k<p) B_k, N=sum_(k<p) kB_k, h=M+12N.

All divisions here have p-unit denominators. The ORIGINAL signed, ordered cutoff is

Q=sum_(0<=i,j<p; i+j>=p) [6(i+j)+1] B_i B_j.

For a=1,...,2m, let v_a=B_(p-a)/p^2 (mod p^2).
Set S_0=T_0=0 and

S_i=S_(i-1)+v_i, T_i=T_(i-1)+i*v_i   (mod p^2).

Then, using the previous all-prime first-jet theorem, the following *new streaming representation* is exact:

R2=Q/p^2 (mod p^2) = L+C (mod p^2), where

L=2 sum_(i=1)^m B_i [(6p+6i+1)S_i-6T_i] (mod p^2),

C=2p sum_(i=m+1)^(2m) (B_i/p) [(6i+1)(S_i mod p)-6(T_i mod p)] (mod p^2).

The v-sequence is generated without an array by

v_1=B_(p-1)/p^2 (mod p^2),

v_(a+1)=v_a*36(p-a)^2 / [(6p-6a-5)(3p-3a-2)] (mod p^2).

Pass 1 visits B_0,...,B_(p-1), retaining only M,N and B_(p-1). Pass 2 revisits B_1,...,B_(2m), advancing v,S,T,L,C. Thus the exact original signed R2, with both valuation channels, takes O(p) modular arithmetic operations and O(1) auxiliary p-adic words. Each word has O(log p) bits for modulus p^4; inverse arithmetic cost is not hidden. Bulk Delta2 is likewise obtained from M,N without retaining the array:

If p divides M and W=(1+6theta) 3F2(...) at z=1/2 obeys W=p (mod p^2), put G=M/p, Delta2=(G*h-1)/p (mod p^2).

By the exact finite Clausen identity, (Delta2-R2)=(W-p)/p^2 (mod p^2), with original signed Q intact.

## Proof

Rewrite the previous triangular inner summands as
sum_(a<=i)(6p+6(i-a)+1)v_a=(6p+6i+1)S_i-6T_i;
after reduction of the (1,2) channel modulo p, the same identity becomes (6i+1)S_i-6T_i. This is an exact distributive-law identity in Z/(p^2); no term or sign is dropped. B_i has valuation 0 for i<=m, valuation 1 for m<i<=2m, and B_(p-a) valuation 2 for a<=2m. Hence exactly the (0,2) and (1,2) channels contribute to Q/p^2 modulo p^2, as established by the earlier theorem. The reflected recurrence follows by reversing the exact B-step ratio. A second forward pass requires only the seven scalar accumulators B,v,S,T,L,C and the previously obtained M,N; no high-index coefficient array. The complexity claim counts modular ring operations, not bit operations or primality certification.

## Independent checks, exact integers

Checker: research_notes/portable_direct/d25_w216_signed_clausen_constant_space_20261110.py.

Three independent computational paths: (a) constant-space reflected signed cutoff, (b) full ORIGINAL ordered cutoff via running suffix moments (linear time, O(p) stored coefficients), and (c) original W via independent 3F2 coefficient recurrence. For p<=373 in the selected bounded test set, also compare (b) with the literal quadratic ordered double sum and (c) with raw binomial coefficients. Tested primes: 7, 13, 19, 37, 43, 373, 10069 and 10099; the latter two are NEW exact samples outside the previous p<=1000 window and cover both target p mod 24 classes. Primality is trial-divisor checked.

Selected full witnesses (residues always normalized into [0,p^2)):

p=373: R2=65844, L=7283, C=58561, Delta2=11759, Delta-R mod p=0, carry bulk=31, carry cutoff=176, fourth digit=228. W mod p^4=11832087049. Reproduces prior author source with independent algorithms.

p=10069 (class 13): R2=86159599, L=8134918, C=78024681, Delta2=64813319, Delta-R mod p=0, carry bulk=6436, carry cutoff=8556, fourth digit=7949. W mod p^4=8114682266998110.

p=10099 (class 19): R2=6601642, L=25577663, C=83013780, Delta2=46654276, Delta-R mod p=0, carry bulk=4619, carry cutoff=653, fourth digit=3966. W mod p^4=4084960171195933.

All independent integer modular equalities PASS in the declared eight-prime set. This is a reproducible original-observer computational certificate, not a universal proof of W=p (mod p^3) and not an H0/B0 native result. Novel contribution in this unit is the proven streaming reduction, bounded independent three-way source audit, and two new exact target-class witnesses; do not describe the prior Q first-jet decomposition as new.

## BRC provenance and next smallest unit

BRC COMPOSE_APPLIED: preserved ordered source pair (i,j), index reflection a=p-j, signed weight 6(i+j)+1, valuation grades (0,2) and (1,2), and both separate carries. The S/T moments are a sufficient quotient ONLY for this fixed linear-weight cutoff and precision through p^4, by the explicit formula above; they are not a claim of native Frobenius or full relational redundancy.

Next mathematics: attempt a signed finite WZ/Jacobi telescoper directly between bulk Delta and the streamed original cutoff, preserving both target residue classes and reporting a scoped counterexample if a candidate identity fails. Native evidence owner path remains existing Issue #1559, currently PENDING_OWNER: fixed original H0/B0 [X]U modulo 139129, rank, semilinear Frobenius eta, signed kappa, Delta-R, and independent reproduction. No own verified Source CLAIM/run or formal Result is asserted.