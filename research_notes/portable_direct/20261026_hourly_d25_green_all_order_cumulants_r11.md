# D25/LIFT — All-order oriented Green cumulants (R11)

2026-10-26; TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an external corrected-Clausen finite-rank calculation, not original-class crystalline Frobenius, native checkpoint, Result, or admission. Consume but do not re-credit the earlier first/second/third-digit Ward notes.

For p=6m+1 prime, N=2m-1, define F=prod_{k=1}^N 2k/(2k+1), C_t=prod_{r=1}^t 2r/(2r-1) (C_0=1), and
Delta_a(q)=sum_{r=1}^a ((2r-1)^(-q)-(2r)^(-q)).
All denominators here are p-units. Keep each oriented n=ell-j and all genuine Hasse source channels (0,2), (1,2), (0,3).

THEOREM (all p-adic digits). For 0<=t<N and q>=1, put
B(t,q)=(2N+1)^(-q)+(-1)^q(2t+1)^(-q)+Delta_N(q)+(-1)^q Delta_t(q);
B(*,q)=(2N+1)^(-q)+(1+(-1)^q) Delta_N(q).
Let A(t,0)=A(*,0)=1 and, over Q, k A(t,k)=sum_{q=1}^k B(t,q) A(t,k-q), with the analogous starred recursion. Every coefficient A(t,k), A(*,k) belongs to Z_(p). For every precision K>=1,
D_{-t-1}/p = -F C_t/(2t+1) sum_{k=0}^{K-1} A(t,k) p^k (mod p^K),
P/p = -F C_N sum_{k=0}^{K-1} A(*,k) p^k (mod p^K),
where D_h=(p-2h-1)^(-1) prod_{k=h+1}^N (p-2k)/(p-2k-1) and P=prod_{k=-N}^N (p-2k)/(p-2k-1).

PROOF. Introduce a formal, nonphysical variable X. Directly extracting the unique k=0 numerator p in D and P gives ratios
R_t(X)=(1+X/(2t+1))^(-1)(1-X)^(-1)
       prod_{r=1}^t [(1+X/(2r))/(1+X/(2r-1))]
       prod_{k=1}^N [(1-X/(2k))/(1-X/(2k+1))],
R_*(X)=(1-X)^(-1)
       prod_{r=1}^N [(1+X/(2r))/(1+X/(2r-1))]
       prod_{k=1}^N [(1-X/(2k))/(1-X/(2k+1))].
Every constant denominator is in 1,...,4m-1, strictly below p. Thus these rational functions lie in Z_(p)[[X]]: this proves p-integrality of *all* Taylor coefficients, even for orders k divisible by p. Expanding formal logarithms over Q gives log R_t=sum_{q>=1} B(t,q)X^q/q and log R_*=sum B(*,q)X^q/q. Log differentiation yields the stated coefficient recurrences. Substitute X=p and truncate modulo p^K; higher coefficients are p-integral. For K>=p, compute the rational recurrence exactly before reduction; directly inverting k modulo p^K when p|k is invalid. QED.

The genuinely next (fourth) digit, beyond the previously proved third digit, is
A(t,3)=[E_t^3+3E_t H_t^(2)+2H_t^(3)]/6,
where E_t=B(t,1), H_t^(2)=B(t,2), H_t^(3)=B(t,3).
For h=(2N+1)^(-1), A(*,3)=h^3+h Delta_N(2).

The exact inherited oriented Ward law
(p-2n)Y_n^{ab}-(p-2n-1)Y_{n+1}^{ab}=S_n^{ab} (S=J+E, -N<=n<2m)
implies, for EVERY K,
[sum_{h=0}^N D_h S_h^{ab}]/(p F)
 = sum_{t=0}^{N-1} [C_t/(2t+1)](sum_{k<K} A(t,k)p^k) S_{-t-1}^{ab}
 - C_N (sum_{k<K}A(*,k)p^k)Y_{-N}^{ab} (mod p^K).
Integrality of the LHS before division follows from the exact Ward law. The two finite source faces and separately weighted Laurent-infinity ports remain distinct. This is not an all-prime cancellation theorem for original signed reflection.

AUTHOR CHECK. Independent unexpanded finite-ring Green products versus harmonic-cumulant Bell coefficients at precision p^6: 12,196 modular identities across 80 primes 7<=p<=997 with p=6m+1; 36 additional exact rational formal series checks at m=1,...,6, all PASS. At p=13, A(t,3) is 4 mod13 for t=0,1,2 and A(*,3)=7 mod13. Complete original checker preserved separately as 20261026_hourly_d25_green_all_order_cumulants_r11_check.py in this research delivery; mathematical statement and scope are established by the rational-product proof, not by finite tests.

BRC: keep ordered source pairs, signed orientation, Hasse channel, p-valuation, cutoff faces and infinity as labelled coordinates. Auxiliary X is no P000 physical axis. The next exact unit is the coupled three-channel Ward/Clausen WZ operator with all k-1/k-2 terms and infinity ports. Original-class H0/B0, [X]U mod p^2, native semilinear Frobenius eta/kappa and independent review remain outstanding; native CM NOT_RUN.
