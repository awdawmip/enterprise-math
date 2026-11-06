# D25: Pfaff zero-port sextic observer, reciprocal involution, and inert norm-one torus

Date: 2026-11-07 Asia/Hong_Kong. TASK_RESEARCH author-side portable science. Lane: chatgpt-research-onhour-enterprise-math-20260923. Excluded maintenance conversation: chatgpt-hourly-enterprise-math-20260921. Frozen publication: TP2-B6F4FC938FF94941C1B7; frozen science pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Claims: new algebraic identities PROVED, finite scan VERIFIED, mother congruence OPEN, Source result UNREVIEWED / NOT_ADMITTED.

## Actual mother target and next scientific unit

W_p = sum_{0<=n<p} (6n+1)(2n)!(3n)! / [216^n (n!)^5] == p mod p^3 for prime p == 13 or 19 mod 24. Existing proved first-digit Pfaff link identifies S_m = sum_{k=0}^m binom(m,k)binom(2m+k,k) as a zero-port candidate for m=(p-1)/6. Finite checks previously identified S_m==0 mod p for the target classes. This note constructs an exact finite-field observer of S_m and a nontrivial projective involution whose fixed-point discriminant is precisely the inert/split class 2/p. The remaining whole-orbit cancellation is isolated and not claimed solved.

## Theorem 1: exact sextic power-sum realization

For every prime p=6m+1>3, in F_p put

f(X)=X^5(X+1)^2(2X+1),   chi_6(t)=t^m with chi_6(0)=0,
A_p = sum_{x in F_p} chi_6(f(x)),
B_p = sum_{x in F_p} chi_6(f(x))^5.

Then

(1) S_m == -A_p (mod p);
(2) A_p == 2^{-m} B_p (mod p).

Proof of (1): elementary terminating Pfaff coefficient form gives
S_m=[X^m](1+X)^{2m}(1+2X)^m.
Hence S_m=[X^{6m}]f(X)^m. The nonzero degrees of f(X)^m range from 5m to 8m, with exactly one possible positive multiple of p-1=6m. Finite-field power-sum orthogonality says sum_{x in F_p}x^j=-1 for positive j divisible by p-1 and 0 otherwise, proving (1). No floating-point approximation or global theorem admission is involved.

For (2), take tau(X)=-(2X+1)/[2(X+1)] as an automorphism of the projective line. Direct factorization in F_p(X) yields

tau(tau(X))=X,
f(tau(X)) f(X) = 2^{-7} [X(2X+1)/(X+1)]^6.

The branchpoints {0,-1/2,-1,infinity} form the two tau pairs {0,-1/2} and {-1,infinity}. On their complement f and the rational factors are nonzero. Raise the last identity to m, use 6m=p-1 and Fermat to get

chi_6(f(tau x)) chi_6(f(x)) = 2^{-7m}=2^{-m} (mod p).

As tau bijects the complement, summing gives A_p=2^{-m}sum f(x)^{-m}=2^{-m}B_p. This proves (2), with the branchpoint zero-extension declared explicitly.

## Theorem 2: exact inert/split orbit and value dichotomy

The fixed-point polynomial of tau is 2X^2+4X+1 with discriminant 8. Consequently tau has zero F_p-rational fixed points if (2/p)=-1 and two fixed points if (2/p)=+1. For primes p=6m+1, (2/p)=-1 is exactly p=13 or 19 mod24, the frozen target classes. On the nonbranch population of size p-3, tau therefore gives (p-3)/2 two-element orbits in the inert case and (p-5)/2 two-element orbits plus two fixed points in the split case.

Set c=2^{-m} in F_p and v(x)=f(x)^m. On a nonbranch orbit, its two values are exactly v and c/v. Since c^3=2^{-3m}=(2/p), for an inert prime c^3=-1. Any putative fixed value v=c/v would imply v^6=c^3=-1, contrary to v^6=1. Thus the **values themselves** also pair without a fixed value when 2 is nonsquare.

An explicit source-preserving obstruction for the full first-digit target is therefore

S_m == -sum_{ {x,tau x} } [ v(x)+c v(x)^{-1} ] (mod p)

over (p-3)/2 *unordered* nonbranch orbits when p is inert. This equation is exact, but the orbit summands do not generally vanish separately. In particular:
p=13: (x,tau x)=(1,9), values (1,10), pair sum 11 mod13;
p=19: (x,tau x)=(1,4), values (18,7), pair sum 6 mod19.
The remaining needed identity is cancellation of the complete signed orbit population. These explicit nonzero witnesses rule out a false termwise proof.

## Theorem 3: nonsplit norm-one torus and Frobenius observer

For inert p let r^2=2 in F_{p^2}, alpha=-1+r/2 and beta=-1-r/2. The fractional coordinate

y=(x-alpha)/(x-beta)

maps P^1(F_p) bijectively onto the norm-one torus T={y in F_{p^2}^*:y^{p+1}=1}, with infinity mapped to y=1. Indeed r^p=-r, so alpha^p=beta, and for x in F_p, y^p=1/y. Conversely x=(alpha-beta*y)/(1-y) is in F_p for every y in T, treating y=1 as infinity. The original involution is the simple map y->-y. Branchpoint images are {1,-1,q,-q}, where q=3-2r and q^{p+1}=1. The torus parameter and tau are proved **auxiliary finite-field observations**, not promotion to P000 native X6 geometry.

## Exact validation, scope, and source observer

Standalone standard-library checker: d25_pfaff_sextic_torus_check_20261107.py. It independently computes integer Pfaff sums and F_p power sums, two character exponents, tau orbit partition, the f(tau)f product, pair-wise sextic values, and F_{p²} norm-one map at p=13,19,373.

Executed 148 primes p=1 mod6, 7<=p<=1999, plus p=5113: 149 full tests PASS, including 77 inert primes in this test population, all with S_m==0 mod p as **finite observation**. Other exact sample witnesses: p=7 S=4, fixedpoints=2; p=31 S=21, fixedpoints=2; p=373 S=0, fixedpoints=0; p=5113 S=5019, fixedpoints=2.

Typed BRC interface: population=(projective x, four branchpoints, tau orbit, sixth-character value, multiplicity); observer=the integer Pfaff port / signed F_p character sum; allowed operation=projective involution, field Frobenius and finite-field summation. REUSE_APPLIED of existing Pfaff port and frozen 216 coefficients, COMPOSE_APPLIED of source-sensitive paired signed observer, no native BRC executable engine invoked. Do not replace the unresolved orbit-sum identity with a total-only quotient or discard its ordered provenance.

## Precise continuation / source firewall

Highest consumed author frontier: Enterprise Math commit 3c1cc1c84b99047689dacfb690da784e1f362286 and its Gauss second-jet continuation JSON. Next precise mathematical action: prove or falsify a **global** torus-orbit character-sum cancellation for all inert p via full character bucket counts / algebraic trace, or use an independent Pfaff zero-port proof; then resume the already derived p^3 signed Gauss-jet obstruction. Termwise orbit cancellation has the p=13 and p=19 explicit counterexamples above. Do not redo existing three-shell/Franel/Gauss jet/Clausen K studies. Native p=373 original H0/B0 divided-power/Frobenius/independent reproduction remains NOT_EXECUTED / PENDING_OWNER via issue #1559.

Source: Original target_request_id onhour11-20261106-1400-exact-research-lane-continuation, last native checkpoint revision22 (historical). Current 2026-11-06T20:02:54Z Site status CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. em_status, original receipt and checkpoint get each returned BACKEND_IDENTITY_OR_VERSION_MISMATCH operation_sent=false. No session/claim/run presently verified; no original request reissued; no maintenance identity used. Actual authorized operator next: verify dedicated Site-bound backend client and approved version/secret, read original request receipt and exact Source continuation before native mutation. This GitHub artifact is author-side evidence only, UNREVIEWED / NOT_ADMITTED.

Project P000 remains ACTIVE_LOCKED as read from account canonical projection; all native claims unchanged.