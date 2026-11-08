# D25 — Original W216 grade-1 p-adic jet and explicit cross-grade LIFT certificate

Date: 2026-11-09 (Asia/Hong_Kong). Classification: TASK_RESEARCH / AUTHOR_SIDE_PROVED_DERIVATION / EXACT_FINITE_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-onhour-enterprise-math-20260923. This note grants no Source CLAIM or Result status.

## 1. The actual remaining question

For primes p congruent 13 or 19 mod 24, the previously proved source crosswalk reduces the frozen LIFT/JT2 conjectural target to W_p = V_p modulo p^3, where

- W_p = sum(n=0..p-1) (6n+1) binom(2n,n)^2 binom(3n,n) / 216^n;
- V_p = sum(n=0..p-1) (8n+1) binom(4n,2n) binom(2n,n)^2 / 2304^n.

The prior author-side grade-2 theorem shows a nonzero W contribution at p=373, making a term-by-term valuation-grade match false. The new object below retains the next p-adic digit of W's grade-1 block so cancellation across grades can be studied without losing information.

## 2. New theorem: exact grade-1 first jet for every prime p=6m+1>3

Set A_n=binom(2n,n)^2 binom(3n,n) / 216^n, n0=2m+1=(p+2)/3, and
T1 = sum(n=2m+1..3m) (6n+1) A_n.
All terms A_n of this range have p-adic valuation one. Define the p-unit K1=A_{n0}/p modulo p^2, and for j=0..m-1 set

U_j = (7/6)_j (1)_j (4/3)_j / (2^j (5/3)_j^3),
H_j(a)=sum(r=0..j-1) 1/(a+r), H_0(a)=0,
D_j=(H_j(7/6)+H_j(1)+H_j(4/3)-3H_j(5/3))/3,
S0=sum(j=0..m-1)(6j+5)U_j modulo p^2,
S1=sum(j=0..m-1)[2+(6j+5)D_j]U_j modulo p.

Each denominator is a p-unit for 0<=j<m. The uniform theorem is

**T1 = p K1 (S0+p S1) (mod p^3).**

Proof. In the original, source-labelled coefficient sequence, for n=n0+j the exact rational term ratio simplifies to

A_{n+1}/A_n =
 [(2n+1)(2n+2)(3n+1)(3n+2)(3n+3)]/[216(n+1)^5]
 = [(j+7/6+p/3)(j+1+p/3)(j+4/3+p/3)]/[2(j+5/3+p/3)^3].

Consequently A_{n0+j}/p = K1 U_j(p), where U_j(p) has the same Pochhammer expression as U_j but every numerator and denominator parameter is shifted by p/3. First-order expansion of the finite products gives U_j(p)=U_j(1+p D_j) (mod p^2); the exact original weight is 6(n0+j)+1=6j+5+2p. Summation gives T1/p=K1(S0+p S1) (mod p^2). The omitted second-order shift vanishes after multiplication by p modulo p^3. All operations are p-integral and preserve the original cutoff.

## 3. Source-preserving, precision-stratified equivalent certificate

Let W0=sum(n=0..2m)(6n+1)A_n. Reuse (rather than reprove) the previous exact grade-2 identity from
research_notes/portable_direct/20261109_onhour_d25_w216_grade2_terminating_companion.md:

T2=p^2 K2 S2 modulo p^3,
K2=(3m+2)! / ((3m+1)!)^5 * 216^(-(3m+1)) modulo p,
S2=sum(j=0..m-1)(6j+4)(1)_j(5/6)_j(7/6)_j/[2^j(3/2)_j^3] modulo p.

Terms with n>=4m+1 in W_p are divisible by p^3. Therefore

**W_p = W0 + p K1(S0+pS1)+p^2 K2 S2 (mod p^3).**

By the published Guo–Zudilin full/half-truncation theorem for V_p, V_p equals Vhalf=sum(n=0..3m)(8n+1)binom(4n,2n)binom(2n,n)^2/2304^n modulo p^3. Thus the *existing* D25 W_p-V_p proof target is equivalent to the explicitly shorter and precision-stratified congruence

**C_p := W0 - Vhalf + p K1(S0+pS1) + p^2 K2 S2 = 0 (mod p^3).**

This is a reduction of the target, NOT a proof of its vanishing for all p. In contrast to the full original p-1 cutoffs, the two unexpanded sums end at 2m and 3m, with remaining contributions expressed via m-term p-adic precision-graded companions. This retains the BRC/provenance labels for grades, original signed weights and both source denominators; S1 is the repair coordinate lost by mod-p-only reduction of grade 1.

## 4. Executed exact evidence

A fully independent direct-oracle path computes the original integer-binomial W_p and V_p modulo p^3; a second path uses the K1/S0/S1 shifted-Pochhammer recurrence and the old K2/S2 companion. All paths agree for 18 primes:
7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373.
These finite checks are regression evidence, not a universal LIFT proof.

For p=373, m=62, p^2=139129, p^3=51895117:
K1=93197 mod p^2; S0=11471 mod p^2; S1=269 mod p;
T1/p=103721 mod p^2, so T1=38687933 mod p^3.
Reuse K2=290 and S2=217 mod p, so T2=37008314 mod p^3.
Original independent sums give W0=28094360 and Vhalf=373 mod p^3.
The cross-grade certificate is **28094360 - 373 + 38687933 + 37008314 = 2*51895117**, hence C_373=0 exactly modulo p^3. This explicitly requires cancellation among different valuation grades.

Reproducer: research_notes/portable_direct/d25_w216_grade1_jet_cross_grade_20261109.py
Results: research_notes/portable_direct/d25_w216_grade1_jet_cross_grade_results_20261109.json
Original source/liveness evidence: historical Source continuation onhour11-20261108-2202-current-task-continuation (SUCCEEDED, read-only); native current session capability unavailable.

## 5. Open frontier and responsibility

Highest-priority native benchmark remains #1559: genuine original p=373 H0/B0 divided-power [X]U mod139129, rank, actual semilinear direction/eta, signed Green/Hesse kappa, Delta-R and independent reproducer. An assigned authorized native evaluator remains unverified; the new algebraic certificate does not replace that experiment. Historical Source Researcher EM-ENTERPRISE-4DEB43 is provenance, not a current authenticated CLAIM. No maintenance conversation identity was used.

Next discriminating mathematical unit: seek a creative-telescoping/Fricke relation between W0-Vhalf and the *combined* grade-1 jet plus grade-2 companion, preserving all denominators, cutoffs and signed observer. No further generic finite-prime scan is needed to re-establish the existing 18/611-prime facts.

Status: AUTHOR_SIDE_THEOREM_DERIVED / EXACT_18_PRIME_CHECK_PASSED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE / NATIVE_CHECKPOINT_NOT_WRITTEN.
