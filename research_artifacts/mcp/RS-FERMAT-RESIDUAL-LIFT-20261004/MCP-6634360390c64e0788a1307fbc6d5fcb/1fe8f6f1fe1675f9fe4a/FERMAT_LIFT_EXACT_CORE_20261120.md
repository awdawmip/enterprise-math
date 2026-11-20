# Fermat residual higher lift — author draft, 2026-11-20

Task RS-FERMAT-RESIDUAL-LIFT-20261004; immutable publication TP2-D911457ABC4CA018FAB8.
Evidence scope: elementary exact integer algebra + bounded tests; independent review/admission pending; no CLAIM for this task is inferred by staging.

1. Exact transition. For arbitrary q>=2, x=q*A+r, x_next=x*x, r*r=q*c+r_next:
A_next=c+2*r*A+q*A*A (integer equality). With s=k-1 standard q-adic digits a_i of A (0<=i<s), the digits d_i of A_next modulo q^s obey h_-1=0, b_i=(i==0?c:0)+2*r*a_i+sum_{j=0}^{i-1}a_j*a_{i-1-j}+h_{i-1}, d_i=b_i mod q, h_i=(b_i-d_i)/q. Euclidean nonnegative remainder and floor carry work even for negative centered r,c. Expanding the exact polynomial and collecting powers of q proves this for every finite k. Readout r_next+q*sum_i d_i*q^i equals x*x modulo q^k. For k=3: d0=(c+2*r*a0) mod q; h0=floor((c+2*r*a0)/q); d1=(h0+2*r*a1+a0^2) mod q. For a third hidden digit: d2=(h1+2*r*a2+2*a0*a1) mod q.

2. Section-change conjugacy. Given integers t,t_next, r'=r+q*t, A'=A-t, r_next'=r_next+q*t_next, c'=c+2*r*t+q*t*t-t_next. Substitution gives A_next'=A_next-t_next EXACTLY, so every x mod q^k readout is unchanged. For p|F_n and centered r_n=-1, quotient u=F_n/p=A_n. In an arbitrary terminal section r_n'=-1+p*t_n, invariant quotient is A_n'+t_n, so p^k|F_n iff A_n'+t_n is 0 mod p^(k-1). Misidentifying A_n' as an invariant causes false answers.

3. Known-divisor Fermat quotient reduction. For an odd prime p|F_n, ord_p(2)=2^(n+1). Put m=(p-1)/2^(n+1), u=F_n/p and y=2^(2^n)=-1+p*u. Then Q_p(2)=(2^(p-1)-1)/p = -2*m*u + p*binom(2*m,2)*u*u (mod p^2). Since 0<2*m<p, p^2|F_n iff Q_p(2)=0 mod p. This is conditional classical Wieferich-type arithmetic, NOT a blind factor finder or new novelty claim.

4. Precision: k-1 q-base digits of A plus r (O(k log q) bits for centered section); full modular arithmetic gives same result. The map A->c+2*r*A+q*A*A modulo q^s is injective for gcd(2*r,q)=1 because differences factor (A-B)(2*r+q(A+B)) with unit second factor. Nonunits can collapse. Missing q*A^2 fails at q=5,r=2,A=1,c=0: true A_next mod25=9, wrong affine result 4. Visible equal mod5 x=2 and x=7 have (x^2+1) mod25 respectively 5,0.

5. Exact integer test evidence: 630 cases across q=3,5,9,17,25,41,641; k=2,3,4; 10 signed/nonnegative x values; 3 section-shift pairs. All direct x^2 mod q^k, digit lift and exact section change checks passed. Known divisors p=5(n1),17(n2),257(n3),641(n5): terminal u mod p = 1,1,1,44; Q_p(2) mod p = 3,13,225,402. At p641: u mod p^2=126321, Q mod p^2=289493; no p^2 divisibility. The finite tests are checks, not the reason the all-k identity is proved.

Next: exact owner and prior proof dedup; preserve actual test source/results; comparison with classical primary sources; precision costs vs direct modular squaring; independent review. No physical-native/P000 inference.