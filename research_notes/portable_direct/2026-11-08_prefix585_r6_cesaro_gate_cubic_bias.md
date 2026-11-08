# PREFIX-585-R6 — Exact Cesàro bias and accumulated gate-pair cubic coupling

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Source-native researcher session, live task owner and formal CLAIM: unconfirmed.

## Native input, inherited result, observer

Scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d` (frozen, unchanged). Native four-STAR X6-BRC has 96 ports and 576 labeled actions; permitted zero root, uniform initial-port law, six equiprobable ordered actions per step. No projection to another physical space is asserted. This mathematical unit reuses the EXACT all-n result at `research_notes/portable_direct/2026-11-08_prefix583_r6_scalar_gate_pair_cubic_exact_recurrence.md` and the exact algebraic representation in `2026-11-08_prefix584_r6_gate_pair_scalar_sign_oscillation.md` at main@ae40cce2c2c612a8634012af542df3e09fd74cf6.

Let R_i(n) be the six native axis counts, K_n the gate count, P_0=R_1+R_2, P_1=R_3+R_4, P_2=R_5+R_6, and Y_n=K_n-(5R_1-R_2+5R_3-R_4-4R_5-4R_6)/192. Prior proved scalar observer:
```
C^(n)_{ij} = cum(Y_n,P_i(n),P_j(n)) = q_n M_{ij},
M = [[0,1,-1],[1,-1,0],[-1,0,1]]
```
for each n>=0. This is a path-length-indexed signed third-cumulant observer, not a claim about positive path mass. The five initial q values are (0,1/576,-1/864,1/1728,1/1944) and, for every n>=0,
```
9 q_(n+5)+3 q_(n+4)-2 q_(n+3)-6 q_(n+2)-3 q_(n+1)-q_n=0.
```
In particular L=lim q_n=1/5184.

## Theorem 1 — rational transient generating function and two exact sum rules

Define e_n=q_n-L and H(z)=sum_(n>=0) e_n z^n. Then for |z|<sqrt(3),

```
H(z) = (10 z^3 +23 z^2 +60 z -9) / [5184 (z^2+2z+3)^2].
sum_(n>=0) (q_n-L) = H(1) = 7/15552.
sum_(n>=0) n(q_n-L) = H'(1) = 1/7776.
```

Proof: The certified degree-five recurrence and initial values determine
Q(z)=sum q_n z^n = -z(z^3+z^2+3z-9)/[576(1-z)(z^2+2z+3)^2].
Subtract L/(1-z); polynomial cancellation yields the displayed rational H. The denominator roots are -1 +/- i sqrt(2), of modulus sqrt(3)>1, so both series at z=1 and their derivatives converge absolutely. Evaluation at z=1 gives the two rational identities. The infinite-length assertions thus follow algebraically from the inherited exact recurrence, not from extrapolating a finite sample.

## Theorem 2 — exact sign for EVERY partial cumulative bias

For integer N>=1 define
S_N = sum_(n=0)^(N-1)(q_n-L).
Then

```
S_1 = -1/5184 < 0,   S_3 = 0,
S_N > 0 for N=2 and all N>=4.
```

Proof: The exact values S_2=7/5184, S_3=0, S_4=1/2592 establish N<=4. For the unbounded tail reuse PREFIX-584's exact quadratic formula with
```
alpha=(-1+i sqrt(2))/3, rho=|alpha|=1/sqrt(3),
A=-(4+37i sqrt(2))/41472, B=(1-2i sqrt(2))/6912,
q_n-L=2 Re[(A+nB)alpha^n].
```
Since |1-alpha|=sqrt(2), |A|=sqrt(34)/4608 and |B|=1/2304, summing the geometric tail and its first derivative yields
```
S_N = 7/15552 - 2 Re[ alpha^N * ((A+NB)/(1-alpha) + B alpha/(1-alpha)^2) ],
|S_N-7/15552| <= rho^N * [ (sqrt(34)+2N)/(2304 sqrt(2)) + 1/(2304 sqrt(3)) ].
```
Use the strict elementary inequalities sqrt(34)<6, 1/sqrt(2)<5/7 and rho=1/sqrt(3)<3/5. For N>=5 the right side is strictly below the rational majorant
```
U_N=(3/5)^N * [ 5/2688 + 5N/8064 + 1/3840 ].
```
U_5=11367/28000000 < 7/15552, and U_(N+1)/U_N < (3/5)(1+1/N) <= 18/25 < 1 for N>=5. Hence |S_N-7/15552|<7/15552 for every N>=5 and S_N>0. Combine with the four exact cases.

## Corollary — cumulative cross-horizon observer and Cesàro correction

For N>=1,
```
sum_(n=0)^(N-1) C^(n) = ( N/5184 + S_N ) M.
qbar_N := (1/N) sum_(n=0)^(N-1) q_n
         = 1/5184 + 7/(15552 N) + O(3^(-N/2)).
lim_(N->infinity) N(qbar_N - 1/5184) = 7/15552.
```
The mean lies ABOVE the limiting single-length coefficient for N=2 and every N>=4 (equal at N=3, below at N=1), despite infinitely many individual q_n occurring on both sides of L (PREFIX-584). The exact finite-N correction is -[2/N] Re of the tail in Theorem 2. The implied exponential error follows from the explicit O(N rho^N) tail bound divided by N.

## Verification, reuse, and next unit

BRC tool decision: REUSE_APPLIED (the original native 768-state moment-lift all-length recurrence and pair-cumulant observer already certified in PREFIX-582/583, without changing their scientific pin). Independent author-side standard-library Fraction certificate `PREFIX585_R6_cesaro_certificate.py` checks 256 recurrence residuals, 256 rational generating-function coefficients, the exact values H(1),H'(1), strict rational majorant inequalities, and signs of S_1,...,S_255. Actual result: ALL_CHECKS_PASS; universal assertions use the algebraic proof and analytic uniform bound above.

This note is scoped to the specified uniform-port zero-root random path law and signed third-cumulant observer. Remaining native question: seek a labeled-path/cycle mechanism for the exact positive integrated bias 7/15552 and test sensitivity to nonuniform initial-port distributions and the other eight frozen roots, keeping the full native provenance until a scope-typed descent proof is available.
