# D25/LIFT — finite adjoint Green flux, Jacobi signed original-cutoff residual

Date 2026-10-25. Author-side TASK_RESEARCH proof; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Mother `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. This is *not* a Source checkpoint, native benchmark, formal Result/freeze or independent review.

## Input and typed boundary

For every prime p=6m+1>=7 define rational hypergeometric coefficients

- r_n=(1/6)_n(1/3)_n/[2^n(n!)²].
- s_n=(5/6)_n(2/3)_n/[2^n(n!)²].
- f(z)=sum_{n=0}^{p-1}r_n z^n; g(z)=sum_{n=0}^{p-1}s_n z^n.
- M=f(1), N=f'(1), S=g(1), U=g'(1);
  H_r=sum_{n=1}^{p-1}r_n/n; H_s=sum_{n=1}^{p-1}s_n/n.

These are original rank-labelled p-local moment and adjoint moment ports. The excluded coefficients r_p,s_p are *boundary forcing coefficients only*, never inserted into frozen W_p.

Reuse previously proved exact original signed Clausen-cutoff identity
W_p=M(M+12N)-Q_p, Q_p=p² T_p (mod p³).
Its signed corner T_p uses v_1=1/10, v_{h+1}/v_h=36h²/[(6h+5)(3h+2)] mod p and
T_p=2 sum_{j=1}^m r_j[(6j+1)V_j-6I_j],
V_j=sum_{h<=j}v_h, I_j=sum_{h<=j}h v_h. This is *not* an infinite convolution substitute.

## Theorem A: exact rational finite Green identity

Let theta=z d/dz, L=theta²-(z/2)(theta+1/6)(theta+1/3), L*=theta²-(z/2)(theta+5/6)(theta+2/3). The star is a formal adjoint for residue pairing dz/z: theta*=-theta, NOT a native geometric dimension.

The exact coefficient recurrences give Lf=-p² r_p z^p, L*g=-p² s_p z^p. Set

B(z)=(1-z/2)[g theta f-f theta g]+(z/4)fg.

Then, **in Q[z] with no modular truncation**,

theta B=p² z^p(s_p f-r_p g),
B(z)=p² sum_{n=0}^{p-1}(s_p r_n-r_p s_n) z^{p+n}/(p+n).

Proof: Write L=A theta²+B0 theta+C with A=1-z/2 and B0=-z/4. Algebraic integration by parts gives gLf-fL*g=theta[A(g theta f-f theta g)+z fg/4]. All coefficients below rank p are killed by the respective hypergeometric recurrence, leaving precisely the first omitted term. The flux constant coefficient is zero; integrate each monomial in Q[z]. The n=0 denominator p is cancelled **before** reduction in Z_(p).

In particular the exact observed B_p=B(1)=(SN-MU)/2+MS/4 satisfies the third-digit congruence

B_p = p(s_p-r_p)+p²(s_p H_r-r_p H_s) (mod p³).

## Theorem B: complementary source normalization through p²

For every p=6m+1>=7,

r_p=1/36 (mod p), s_p=5/18 (mod p), **s_p=10r_p (mod p²)**.

Proof: For a=1/6 or 1/3, the unique index i in 0..p-1 for which a+i is p-divisible equals m or 2m and a+i=p/6 or p/3. The remaining p-1 residues run over Fp^×, whose product is -1 and whose reciprocal sum is zero. Wilson and 2^{-p}=1/2 (mod p) give r_p=1/36; for a=5/6,2/3 the zero indices are 5m,4m with p-factors 5p/6,2p/3, giving s_p=5/18. Factor reflection i->p-1-i yields the exact rational ratio

s_p/r_p = 10 prod_{0<=i<p,i!=m}(1-p/(i+1/6))
             prod_{0<=i<p,i!=2m}(1-p/(i+1/3)).

Each product equals 1 (mod p²) because all its nonzero denominator residues exhaust Fp^×. Every displayed denominator is a p-unit.

Consequently the new all-prime signed Green flux is

**B_p = 9p r_p + p² r_p(10H_r-H_s) (mod p³),**
hence B_p=p/4 (mod p²).

Now consume the **distinct prior unreviewed author** Jacobi forcing port J_p=K_p 2^{-p}, with prior exact r_p=-J_p E_p/72 and E_p=1 (mod p²). We obtain the provenance-preserving composition

**B_p = -p J_p/8 - p² J_p(10H_r-H_s)/72 (mod p³).**

Here K_p z^p is a polynomial source, while J_p is its z=1/2 evaluation; neither is exchanged for the other before differentiation.

## Theorem C: finite-field Euler polynomial and conditional dual p² moment lift

The classical formal-series Euler identity for 2F1, reduced through degree p-1, gives an exact *polynomial* identity in Fp[z]:

**g(z) = (1-z/2)^{3m} f(z) (mod p).**

Proof: r_n=0 mod p for n>m, s_n=0 mod p for n>4m. The RHS has degree at most 4m<p. The Euler exponent -1/2 equals 3m modulo p and n! is invertible for all n<p, so coefficientwise Euler equality below p becomes full polynomial equality.

Let epsilon=(2/p)=2^{(p-1)/2}. At z=1 this gives
S=epsilon M (mod p), U=epsilon(N+M/2) (mod p).

For D25 target primes p=13,19 (mod 24), epsilon=-1. The following deductions explicitly **assume M=0 mod p**, which remains an unproved all-target CM/Legendre zero in this author route. Then S=0, U=-N (mod p), and B_p=p/4 (mod p²) yields

**(S+M)N/p=1/2 (mod p).**

If additionally the independently accepted original first-digit premise 12(M/p)N=1 (mod p) applies, then

**S=5M (mod p²).**

The ratio 5 is a dual hypergeometric moment port, not a claimed Source-native kappa or Frobenius direction.

## Theorem D: new *original* W third-digit signed residual

Retain the preceding explicit premises and the previously proved original Clausen signed corner. All expressions here belong to Z_(p) before mod-p readout:

a=M/p mod p; e=(U+N)/p mod p; d=(S-5M)/p² mod p;
h=10H_r-H_s mod p; t=T_p mod p.

Because M,S are p-divisible, U+N is p-divisible, and S-5M is p²-divisible, all divisions are legal. Elementary algebra applied to exact B_p yields

W_p = 4B_p-4M²+2pMe-2p²dN-p²t (mod p³).

Substitute the already proved Jacobi-adjoint Green flux:

**W_p = -pJ_p/2 + p²[-J_p h/18 -4a² +2ae-2dN-t] (mod p³).**

Since J_p=-2 (mod p), the all-prime D25 hard target *under the stated target-class premises* is now exactly equivalent to a **single original-cutoff signed residue**

**R_adj(p)=(-J_p/2-1)/p - J_p h/18 -4a²+2ae-2dN-t = 0 (mod p).**

The p-division is performed in Z_(p), not by modular inversion. This reduction retains original W_p, the signed Clausen corner, Jacobi evaluated forcing, both moment derivatives, boundary strata/valuations and harmonic readout. It is an exact conditional equivalence, **NOT an all-prime proof of R_adj=0**.

## Actually executed, independently cross-checked author evidence

Program `d25_adjoint_green_dual_moment_check_20261025.py` was run with Fraction for every exact polynomial Green coefficient at p=7,13,19,31, and independent unit-modular recurrences over 94 primes p<1200, p=1 (mod 6), plus p=19963. **95/95 passed**: terminal ratio mod p², r_p/J_p mod p³, Green/Jacobi flux mod p³, Euler value and derivative mod p. At all 53 target primes, checked dual lift mod p², *independently recomputed frozen-original W_p*, and verified that new signed R_adj equals (W_p-p)/p² mod p (zero in those finite cases). This is finite author checking, not the native same-original-class CM/Hasse/[X]U/Frobenius experiment.

Representative p:(a,d,e,R_adj) = 13:(11,4,9,0); 19:(8,16,16,0); 211:(193,69,175,0); 19963:(11730,2257,3497,0). The full proof, executable checker and output are in the attached portable research bundle for this run.

## Live obstruction and next exact action

No universal target-class Legendre zero M=0 mod p or universal cancellation of R_adj has been proved. The original p³ JT2/LIFT and Source-native Δ_p-R_p observer remain OPEN. Next math: directly obtain CM/Hasse/Frobenius data for the **frozen original class**, proving/falsifying all-prime Legendre zero and the signed R_adj cancellation while preserving d,e,h,t. No substitute implementation counts as native benchmark. No new scheduler or Actions.

The research lane is `chatgpt-research-onhour-enterprise-math-20260923`, disjoint from maintenance `chatgpt-hourly-enterprise-math-20260921` and from the *other* Research lane discussed in issue #1558. The private Gateway 0.6.11 Site client reports research_authority_granted=false; one bounded exact continuation read yielded CONTROL_QUOTA. No Source-native session/claim/run/checkpoint, Result, review or admission is asserted. #1539 remains the original onhour lane's support path. Prior staging is not relabeled as Result; original scheduler/notifications left unchanged.
