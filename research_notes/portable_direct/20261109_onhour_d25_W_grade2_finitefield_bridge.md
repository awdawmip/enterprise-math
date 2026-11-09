# D25 / Original 216 grade-2: exact finite-field polynomial bridge

Date: 2026-11-09. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923.
Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Status: AUTHOR-SIDE PROVED ALGEBRAIC LEMMA; FINITE EXACT REGRESSION; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

## Theorem (original 216 second valuation layer; p=1 mod 6)

Let p=6m+1 be prime, m>=1, and N=m-1. Preserve the original rational coefficient and signed weight

A_n = binom(2n,n)^2 binom(3n,n) / 216^n = (2n)!(3n)! / ((n!)^5 216^n),
W_{2,p} = sum_{n=3m+1}^{4m} (6n+1) A_n.

All displayed A_n lie in the SECOND p-adic valuation layer: v_p(A_n)=2.
Define in F_p

F_N(z) = sum_{j=0}^N [(-N)_j (N+2)_j (1)_j / ( (3/2)_j^3 )] z^j,
H_N = (4 + 6 z d/dz) F_N(z) at z=1/2,

and

K_p = (3m+2) / ( ((3m+1)!)^4 216^(3m+1) ) in F_p^*.

Every denominator is a nonzero residue modulo p, including the factorial and each (3/2)_j.
Then the exact finite-field identity is

(W_{2,p}/p^2) mod p = K_p * H_N mod p.

In particular the signed original 216 third-digit grade-2 readout is reduced to a length-m terminating polynomial with unit denominators, preserving every original weight and grade boundary.

## Proof

For 0<=n<p, Legendre's formula gives
v_p(A_n)=floor(2n/p)+floor(3n/p). For p=6m+1,
n in [3m+1,4m] gives floor(2n/p)=1 and floor(3n/p)=1.
Let n0=3m+1=(p+1)/2 and set U_j=A_{n0+j}/p^2 in Z_(p).
At n0, 2n0=p+1 and 3n0=p+(3m+2). Wilson's theorem gives
(p+1)!/p == -1 (mod p),
(p+3m+2)!/p == -(3m+2)! (mod p),
hence U_0==K_p modulo p.

The exact recurrence for the ORIGINAL A coefficients is
A_{n+1}/A_n = (2n+1)(3n+1)(3n+2) / [36(n+1)^3].
For n=n0+j reduce modulo p, obtaining
U_{j+1}/U_j ==
[(j+1)(j+5/6)(j+7/6)] / [2(j+3/2)^3] (mod p).
Because p=6m+1, 5/6==m+1=N+2 and 7/6==1-m=-N (mod p).
For 0<=j<N, all denominators are p-units and U_j/U_0 equals the j-th
coefficient of F_N(1/2). Finally
6(n0+j)+1=3p+4+6j==4+6j (mod p),
which produces (4+6zD)F_N(z) at z=1/2. QED.

## Direct D25 application and observer accounting

The preceding author-side Guo--Zudilin theorem gives for ALL primes p>3,
V_{2,p}==0 (mod p^3), in the original 2304 model.
Thus on the present p=1 mod6 branch, the actual AF4 second-grade observable
b_0=(W_{2,p}-2V_{2,p})/p^2 mod p is explicitly

b_0=K_p H_N.

This is a true original-weight/valuation reduction, not a surrogate Hesse
operator or a proof of the full AF4/LIFT target. For the fourth p-adic digit,
one must separately retain the jet of A_{n0+j}/p^2 mod p^2 and Q2=V2/p^3;
the projected H_N carries the THIRD digit only. The previous original
low-high carry coordinate and signed cancellation must remain intact.

BRC / residual-fidelity application: carrier = indexed signed grade-2
terms (n, A_n, 6n+1, v_p=2); observer = sum/p^2 mod p; map from the
original index to j=n-(p+1)/2 is bijective. The finite-field U_0 and
successive rational recurrence preserve this declared observer exactly.
The fourth-digit, native H0/B0 operator, Frobenius direction, eta, kappa and
full Delta-R are separate future observers and are not quotiented out.

## Executed exact regression and independent arithmetic

The included portable Python script executes three separate paths for each
prime p=1 (mod 6) up to 1000: original integer binomials modulo p^3;
original coefficient recurrence modulo p^3; and reduced terminating
finite-field polynomial. ALL 80 primes passed exact equality.

p | m | K_p | H_N | b_0
7 | 1 | 3 | 4 | 5
13 | 2 | 10 | 1 | 10
19 | 3 | 17 | 5 | 9
37 | 6 | 4 | 5 | 20
43 | 7 | 24 | 14 | 35
73 | 12 | 65 | 60 | 31
373 | 62 | 290 | 217 | 266
379 | 63 | 337 | 28 | 340
997 | 166 | 443 | 754 | 27

All arithmetic is exact integer modular arithmetic, no floating point.
Finite regression audits the proved recurrence rather than serving as its
universal proof.

## Continuation and unexecuted native benchmark

Main parent objective remains exact original Delta_p-R_p==0 (mod p)
for p=13,19 (mod 24), preserving cutoff-sensitive signed observers.
AF4 fourth-digit cancellation remains conjectural. The smallest next
mathematical unit is to extend this grade-2 bridge to FIRST p-adic jet and
couple it with the previously proved 2304 grade-2 Q2 and actual low-high
carry, testing p=13,19,373 before a uniform cancellation claim.

Native p=373 same-original-class H0/B0 divided-power [X]U mod139129,
rank, Frobenius direction, eta, signed kappa/Delta-R and independent check
remain UNEXECUTED, tracked by existing issue #1559 (PENDING_OWNER).
This note is an author-side GitHub evidence artifact, not a Source task
checkpoint, registered activity, review, or accepted Result. Neither this
logical Research lane nor its files authenticate the maintenance lane.
