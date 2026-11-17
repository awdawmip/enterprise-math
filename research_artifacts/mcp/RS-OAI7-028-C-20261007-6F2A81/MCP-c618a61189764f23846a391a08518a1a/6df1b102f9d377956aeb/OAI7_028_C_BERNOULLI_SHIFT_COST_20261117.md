# Exact Bernoulli common-shift threshold and information cost
Task RS-OAI7-028-C-20261007-6F2A81, author-side follow-up to OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md (2026-11-17).
For any prime p, 0<beta<1, 0<tau<=3/8 and m=ceil(p^(1-beta))<=p/2, fix Y_j independent uniform on A={m,...,p-1}. Let B be a common Bernoulli(q), h=Bm(1,...,1), Z=Y+h; all coordinates use the SAME B.
Writing A'=A+m mod p, the p residues partition into:
A\A' (m residues, probability (1-q)/(p-m)),
A'\A (m residues, probability q/(p-m)),
A intersect A' (p-2m residues, probability 1/(p-m)).
These are exact probabilities; sign-inverted coordinates have the same multiset.

Put a=tau(p-m)/p. Since m>=p^(1-beta), the strict definition of (tau,beta) coverage is satisfied for every signed coordinate IF AND ONLY IF a<=q<=1-a.
Proof: for q in the interval every probability is >=tau/p, hence zero exceptions. For q<a all m residues of A'\A fall strictly below tau/p; for q>1-a all m residues of A\A' fall below tau/p. Either case has at least p^(1-beta) exceptions and fails the strict bound. At q=a and q=1-a equality Pr=tau/p is allowed.

Within this exact two-shift family the minimum shared data entropy that yields coverage is h_2(a)=-a log a-(1-a) log(1-a) nats, attained at q=a or 1-a. Indeed H(h)=H(B)=h_2(q), and binary entropy is concave with its minima over [a,1-a] at the endpoints. The contribution to the external theorem's normalized common-data entropy budget for n=1, coordinate sizes all p and fixed signed selection size s is kappa=h_2(a)/(s log p). This is only an information-cost calculation; the source theorem additionally requires strong CONDITIONAL next-checkpoint coverage and large sample size.

Exact p=101, m=11, tau=3/8 gives a=135/404, minimum H(h)=0.637084540827282 nats, compared with fair-bit log2=0.6931471805599453. The accompanying rational-arithmetic checker confirms zero exceptions at q=a and q=1-a, and eleven exceptions immediately outside. This quantifies how a single shared shift can repair marginal support without k separately chosen time/shifts.
