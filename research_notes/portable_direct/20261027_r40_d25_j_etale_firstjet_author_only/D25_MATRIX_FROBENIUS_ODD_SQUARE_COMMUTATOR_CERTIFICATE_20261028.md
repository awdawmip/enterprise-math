# D25/LIFT — Frobenius matrix odd square: exact commutator and mod-p³ gauge fiber

Date: 2026-10-28. Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 — not rebased.
Author context LOCAL-0bc2a9ec-d1eb-442e-b774-fe1df922abe2: historical shared author context only, not an independent identity or reviewer.

## External, scoped model and question

The prior first-jet auxiliary result found that the square of a semilinear Frobenius forgets the first-order marked odd matrix at modulus p². The precise new question is whether the lost port stays invisible at modulus p³ when matrix coefficients do not commute. The carrier is the *joint marked* matrix-coefficient pair, not scalar positive mass or an averaged norm. This auxiliary arithmetic model is not the native Heartbeat World X6 Cell space or the fixed original H0/B0 CM class.

For odd prime p and n>=2 set R=(Z/p^n Z)[T]/(T²-2), sigma(T)=-T. Let eta=P+TQ be an invertible r-by-r matrix over R; P,Q are matrices over Z/p^n. Define semilinear F(x)=eta sigma(x).

## Theorem A — exact odd commutator at every finite precision

For all p,n,r,P,Q above, F² is the R-linear operator

\[
\boxed{F^2=(P^2-2Q^2)+T(QP-PQ).}
\]

Consequently the marked odd coefficient [T]F² vanishes **if and only if** [Q,P]=0. The scalar rank-one norm formula is a special case. It cannot be imposed in higher rank without proving the coefficient matrices commute.

Proof: sigma²=1 and sigma(eta)=P-TQ, so F²=eta sigma(eta)=(P+TQ)(P-TQ)=P²-2Q²+T(QP-PQ). The basis (1,T) is free over Z/p^n, establishing necessity as well as sufficiency.

## Theorem B — p³ second-jet information, uniform in r

Let A,B,C,D be any matrices over F_p with arbitrary integral lifts, and eta=I+p(A+TB)+p²(C+TD) modulo p³. Expansion of Theorem A gives

\[
\boxed{F^2=I+2pA+p^2(2C+A^2-2B^2+T[B,A])\pmod {p^3},}
\quad[B,A]=BA-AB.
\]

Therefore the normalized odd-square second-jet observer K_A(B):=[T]F²/p² mod p equals [B,A], independently of C,D and all digit-lift choices. Its kernel is the centralizer C(A)={B:BA=AB}. Thus at fixed A the raw odd-square observer has p^(dim C(A)) marked B matrices per reading. At r=1 the whole odd square is zero at all precisions, but already r=2 permits a nonzero odd square at precision p³.

Proof: P=I+pA+p²C and Q=pB+p²D. Modulo p³, P²=I+2pA+p²(A²+2C), Q²=p²B² and [Q,P]=p²[B,A]. Any change of integral lifts shifts eta's first jets only at p², leaving the normalized odd square unchanged modulo p.

## Theorem C — gauge covariance, observer-safe quotient and exact fibers

Under an actually allowed near-identity gauge U=I+p(C_g+TD_g)+O(p²), F'=UFU^-1, the first jets obey A'=A and B'=B+2D_g modulo p. Hence

\[
K_A(B')=K_A(B)+2[D_g,A].
\]

For a subgroup H of 1+p M_r(R), let L(H)={2D_g mod p: U in H}, an additive F_p subspace of V=M_r(F_p). The marked first-jet gauge classes are V/L(H). There is an induced *surjective* map

\[
\boxed{\Phi_{A,H}:V/L(H)\to\operatorname{im}(\operatorname{ad}_A)/\operatorname{ad}_A(L(H)),
\quad B+L\mapsto[B,A]+\operatorname{ad}_A(L).}
\]

Its fibers have exactly

\[
\boxed{p^{\dim C(A)-\dim(C(A)\cap L(H))}}
\]

elements. The odd-square quotient completely determines the marked first-jet gauge class **if and only if** C(A) is a subspace of L(H). If L(H) is contained in C(A), the odd square itself is gauge invariant but can still omit unshiftable centralizer information. Under unrestricted first-order odd gauge shifts it is not an unmarked invariant.

Proof: mod p² multiplication in the first congruence subgroup is additive, so L(H) is a subspace. The first-jet conjugation follows from U eta sigma(U)^-1. The kernel of the displayed linear map is (C(A)+L(H))/L(H); its dimension yields the fiber formula and completeness criterion.

For diagonal A=diag(lambda_1,...,lambda_r) with pairwise distinct lambda_i in F_p, C(A) is precisely the diagonal subspace and K_A(B)_{ij}=(lambda_j-lambda_i)B_{ij}. If the actual allowed odd gauge shifts are all and only diagonal matrices, K_A(B) is a *complete* gauge-class coordinate. No assertion is made that original H0/B0 has such a gauge group.

## Explicit p=373 finite-ring witness (not native)

Take r=2, A=E11, B0=0, B1=E12, C=D=0. Mod q=373³=51,895,117 both F0²,F1² have the same entire even matrix I+139,875 E11, and their full squares agree modulo 373²=139,129. Yet

\[
[T]F_0^2=0,\quad [T]F_1^2=-139129 E_{12}=51755988 E_{12}\pmod {51895117},
\]
so the normalized odd entry is -1=372 modulo 373. These two matrices are distinguished by the odd-square port under diagonal leading gauges, and are not original CM Frobenius representatives.

## BRC/source/acceptance boundary

Source objects: all matrix entries and ordered T-ports (including signs), original basis, provenance and future gauge H. Squaring to a scalar norm first discards [Q,P]; theorems A-C quantify when the quotient is information-preserving. These are scoped auxiliary algebra proofs, not P000 amendments, native X6 transfer, proof of Delta_p-R_p, numerical original-class H0/B0 execution, Source checkpoint or independent admission. The original H0/B0 rank, eta basis, [X]U mod p², signed Green/Hesse/Delta-R ports and genuine H must come from the authorized source path in Issue #1559.

## Author exact verification

The source file d25_matrix_odd_square_compact_reproducer_20261028.py (Python standard library, same author) ran 630 direct p³ algebra identities, 630 independent matrix-gauge conjugation checks, 210 scalar rank-one zero checks, complete p=3/5 rank-two B histograms and the p=373 witness, all PASS. It does not simulate the native H0/B0 CM benchmark. Larger local independent-path checking exists but is not presented as external review.

UR four-file V2 original remains pending exact 94,687-byte SHA-256 check (4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76); its existing mathematics must not be re-proved. The current Source seed/claim/run ownership is unverified. If Source returns CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS then predecessor completed_units must be [] after actual input_artifact readback, not this author file.

Next exact action: native owner #1559 to establish rank, full operator and gauge; check original commutator before scalar-norm transfer; seek the actual UR bytes only for lawful provenance/writer repair.
