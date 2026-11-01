# D25/LIFT GH-124–GH-125: marked Jacobsthal character first moment
2026-10-30 Asia/Hong_Kong. Author-side research in logical lane chatgpt-research-hourly-enterprise-math-20260923. D25/LIFT/JT2 remains OPEN. Scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## GH-124. General polynomial identity and CM marked-jet bridge
For p>=5 odd prime, q=p², k=F_q, N=(p-1)/2 and f_B(X)=X³+X²+BX, put H_p(B)=[X^(p-1)]f_B(X)^N and let chi_q denote the quadratic character extended by zero at zero. The marked character moment is

S_q(B)=sum_(x in k, f_B(x)!=0) chi_q(f_B(x))*x/f_B(x).

Then, as an identity in F_p[B],
  -sum_(x in k) f_B(x)^((q-1)/2) = H_p(B)H_p(B)^p,
and after formal differentiation, for every B in k,
  S_q(B)=2H_p'(B)H_p(B)^p.

Proof: f_B^N=sum_(r=N)^(3N) a_r(B)X^r; f_B^((q-1)/2)=(f_B^N)^(p+1). In the sum of x^(r+ps) over k, only the exponent q-1 can contribute, because (q-1)/2 <= r+ps <= 3(q-1)/2 < 2(q-1). The congruence r=-1 mod p and N<=r<=3N<2p-1 force r=p-1, then s=p-1. The power sum is -1, establishing the first identity *as a polynomial*. Differentiate it. The Frobenius factor has zero derivative and -((q-1)/2)=1/2 modulo p. For f!=0, f^((q-3)/2)=chi_q(f)/f; for f=0 the positive power is zero. This yields S. The derivative is of a polynomial, NOT a numerical differentiation of discrete point counts. For smooth E_B:y²=f_B(x), a_q=-sum chi_q(f_B(x)), and its reduction mod p is H_p(B)H_p(B)^p.

For p=8m+3>=11, T²=1-z^(-1), T,z !=0, B=(1+T)/8, the GH-100 Hasse/Legendre identity gives H(T)=H_p(B)=P_(2m)(T), G(z)=z^m H(T), A(z)=16zG'(z)+5G(z), H_ref=D^(-2)G*A, D=binom(3m+1,m). Since 16m+5=-1 in F_p and dT/dz=1/(2Tz²), one obtains

  A(z)=z^m[-H(T)+8H'(T)/(zT)],
  S_q(T)=16H'(T)H(T)^p,   tau_q=H(T)H(T)^p,
  2zT H(T)^p A(z)=z^m[S_q(T)-2zT*tau_q].

At z=9, T²=8/9, the exact criterion is
  H_ref(9)=0  IFF  S_q(T)=18T*tau_q.
If H(T)=0, both hold automatically; if H(T)!=0, divide the identities by its nonzero factor. This is an independent **character-sum criterion** for GH-83, NOT an all-prime proof of GH-83 and NOT a proof that R_p(9)=0. The summand is independent of GH-98–GH-103 finite-log representations; the Hasse–Witt power-sum mechanism itself is classical.

## GH-125. Executed exact finite-field evidence
Over F_3347[r]/(r²-2), write (a,b)=a+b*r. The C++17 script enumerates all 11,202,409 x for each of three k-isomorphic GH-121 marked models (33,607,227 evaluations total) and accumulates both the signed trace and S through the quadratic norm and exact inverses; GH-123 Hasse jets are separate crosscheck targets.

| Marked origin | B | integer a_(p²) | S=(a,b) | Delta=S-2zT*(a_q mod p) |
|---|---|---:|---|---|
| original z=9, T=(0,2232) | (2092,279) | -6106 | (0,362) | (0,0) |
| alternate 1, T=(1916,2172), z=(3207,479) | (658,1945) | -6106 | (2954,765) | (915,1909) |
| alternate 2, T=(458,813), z=(2251,2893) | (2986,520) | -6106 | (390,679) | (800,620) |

All three have tau_q=588 and exactly 11,202,406 nonzero cubic values. In the original marked model 18T*tau=(0,362), matching S without computing the Legendre or finite-log expression. The alternate origin defects are nonzero despite identical traces. A separate Python script independently enumerates all 19 p<400 with p=3 (mod 8), verifying S=18T*(trace mod p) in each. This is a finite scan, not a uniform theorem.

Commands: g++ -std=c++17 -O3 -Wall -Wextra -Werror d25_gh124_gh125_marked_character_jet.cpp -o check && ./check; python d25_gh125_small_prime_character_scan.py.
Verified output: PASS_GH124_GH125_MARKED_CHARACTER_TRACE_AND_FIRST_JET_3_ORIGINS; PASS_GH125_SMALL_PRIME_MARKED_JACOBSTHAL_MOMENT_UP_TO_400.
Code Git blob references: 212162fba234a3ffa5d8da3cdb6913629b861208 and c84d7c6bebb9bc6d73311e060dc96c0f19cac03c.

BRC COMPOSE_APPLIED: preserve field k, origin/mark, branch x, signed chi_q(f), exact x/f and field-valued sum; scalar Frobenius trace alone loses the signed first-moment residual. Auxiliary T is not native X6 time or a native 2D plane. The next independent question is a CM/Jacobi/Gauss or p-adic-period evaluation of S at the original mark without taking GH-83 as input, then a separate bridge to the integrated R_p(9) tail / GH-3.

Control at v0.6.11: research_authority_granted=false, executor_binding_configured=false, Source CODE_REVIEW_REQUIRED, active jobs 5/5. Exact continuation attempt returned INVALID_ARGUMENT / CONTROL_QUOTA. No new native session/CLAIM/open/checkpoint/Result/review or staging mutation. Support path enterprise-math #1558; existing sessions and requests preserved.
