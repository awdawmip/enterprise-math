# RH composite-road: uniform first-order prime-power expansion and o(a) near-field energy

Date: 2026-11-15.
Status: SCOPED DRIVER MATHEMATICAL RESULT, proof below; classical prime number theorem used only for the final o(a) assertion. No native Result admission, full escape-tail bound, audit completion, or RH claim.
Original research program/contribution: EM-FREE-C4A91D, RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD. This independent local Driver derivation builds on the earlier elementary near-field bound at research_notes/driver/2026-11-15_rh_road_small_a_nearfield_primepower_majorant.md, saved at 1668ed1b7830dfd9892d4790563e47567792fdfb. Preserve predecessor audit/kernel and owner separation.

## Definitions

For real a>0 and positive integer N let
```
R_a(1)=1,   R_a(n)=product_(p|n) (1-p^(-a)) (n>=2),
S_a(N)=sum_(n=1)^N R_a(n),
c_a=1/zeta(1+a),
B_(a,N)=S_a(N)-1-c_a*(N+1/2),
psi(N)=sum_(p^k<=N,k>=1) log p
      =sum_(n<=N) Lambda(n)    (prime powers counted once each).
```
Logarithms are natural. The arithmetic road includes *all positive integers*, including composite integers with at least two distinct prime divisors.

## Theorem A: all-a first-order expansion with explicit uniform error

For every real a>0 and integer N>=1,
```
B_(a,N) = a*(psi(N)-N-1/2) + E_(a,N),
|E_(a,N)| <= a^2*N*( (3/4)*(log N)^2 + 1 + 1/(2*N) ).       (A1)
```
In particular, at every fixed integer N>=1,
```
lim_(a->0+) B_(a,N)/a = psi(N)-N-1/2.                         (A2)
```
This is an exact elementary quantitative expansion requiring no prime number theorem.

**Proof.** Set x=a log p>=0. Integration gives
```
0 <= x-(1-exp(-x)) = integral_0^x (1-exp(-t)) dt <= x^2/2.
```
For n=p^k, R_a(n)=1-p^(-a), so its difference from a log p is bounded by (a^2/2)*(log p)^2. Summing over the prime powers not exceeding N contributes at most (a^2/2)*N*(log N)^2.

For n>=2 with at least two distinct prime divisors p,q, the remaining factors are at most 1 and
```
0 <= R_a(n) <= (a log p)*(a log q)
                <= (a^2/4)*(log(pq))^2
                <= (a^2/4)*(log N)^2.
```
These n contribute at most (a^2/4)*N*(log N)^2. Therefore
```
|[S_a(N)-1]-a*psi(N)| <= (3/4)*a^2*N*(log N)^2.              (A3)
```
For every a>0, integral comparison gives
```
1/a <= zeta(1+a) <= 1+1/a,
a/(1+a) <= c_a <= a,
0 <= a-c_a <= a^2/(1+a) <= a^2.                            (A4)
```
Subtracting a*(psi(N)-N-1/2) from B_(a,N) and applying (A3)-(A4) proves (A1), including N=1. Dividing by a for fixed N proves (A2). QED.

## Theorem B: o(a) near-field energy to scale T/a

Let T>0 be any fixed constant, and L_a=floor(T/a). For all sufficiently small a>0 (so L_a>=1),
```
sum_(N=1)^(L_a) B_(a,N)^2/N^2 = o(a)     as a->0+.           (B1)
```
This assertion is unconditional in classical number theory: it invokes the already-proved prime number theorem in the equivalent form psi(N)/N -> 1, and no RH/zero-free-right-half-plane assumption.

**Proof.** Set
```
q_N=(psi(N)-N-1/2)/N,
H(a,L)=(3/4)*(log L)^2+3/2.
```
By the classical prime number theorem, q_N -> 0 as N->infinity, and consequently (1/L)*sum_(N<=L) q_N^2 -> 0 by Cesaro convergence (q_N is bounded).

By (A1), for all 1<=N<=L,
```
|B_(a,N)/N - a*q_N| <= a^2*H(a,L).
```
Hence using (u+v)^2<=2u^2+2v^2,
```
sum_(N<=L) B_(a,N)^2/N^2
 <= 2*a^2*sum_(N<=L)q_N^2 + 2*a^4*L*H(a,L)^2.             (B2)
```
For L=L_a=floor(T/a), the first term is a^2*o(L)=o(a); the second is O(a^3*(log(1/a))^4)=o(a). This proves (B1). Since the summands are nonnegative, the same o(a) assertion holds for any integer L(a) with 1<=L(a)<=T/a eventually. QED.

## Consequence for research routing

The previously established *elementary* estimate is O(a) up to fixed T/a. The present stronger result shows that the fixed-multiple near-field contributes o(a) once the proved classical prime number theorem is used. Therefore any still-uncontrolled order-a contribution to the complete energy D_a must arise from the longer ranges N>T/a for every fixed T. That is a concrete source-faithful reduction of the open large-N task; no new arithmetic cancellation mechanism for the escaping tail is asserted.

Theorem A also identifies the *first derivative at a=0* of the road's centered arithmetic discrepancy as the classical Chebyshev psi(N)-N-1/2. The zero-order collapse R_0(n)=0 for n>1 is compatible with this first-order term, but the expansion is not uniformly summable over all N without additional control.

## Source / checking status

Definitions match the original composite-road full-integer B_(a,N) setup cited by the earlier bound. The proof is a human-verifiable inequality argument; a finite numerical sanity check at a in {0.01,0.1,0.5} and N in {1,2,5,50,200} passed the displayed (A1) bound. No numerical check supplies Theorem B; its mathematical dependency is exactly the standard prime number theorem psi(x)~x. Native Project result/Task acceptance and any independent Reviewer remain separate. Original contributors and owner claims are not reassigned.
