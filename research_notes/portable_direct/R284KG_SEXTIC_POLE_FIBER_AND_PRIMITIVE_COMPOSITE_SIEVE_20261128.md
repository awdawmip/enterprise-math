# R284KG - Sextic pole fiber and strengthened whole-composite sieve

2026-11-28. Author proof and executed exact computation; NOT_REVIEWED. Auxiliary arithmetic of R284, no native spatial attribution. Own recovery r1-20261128-1101-own-recovery confirms original open RESEARCHER registration r1-20261124-0256-r284gd-session-v1 and no own formal runs; EM-DIRECT-0C386E / TASK_RESEARCH, RA-B82240E8488EF5A1DA5186C4. Current LEASED inventory r1-20261128-1101-owner-inventory-v1 SUCCEEDED, no LEASED tasks at 2026-11-28T03:02:34.637713Z, source cc7b91b35cef446f24f57d7d95d3081a9aeb799b (head advanced during read). No shared task acquisition or ownership mutation. Global entries verified at immutable main c8650923c9d74240589c7d3f4ff2c43409966901. P000 V4/V5, ACTIVE worldview, joint observer/residual contracts, portable protocol and current research method consulted.

Frozen scientific inputs: KF dffdb8e6221f1f4820189dfeac8ab40ca704f850:research_notes/portable_direct/R284KF_NEGATIVE_DOUBLE_FIBERS_AND_COMPOSITE_SIEVE_20261128.md; JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md; KE c0709a6e3bbbc1112f61f4e41285e97a25bd6142:research_notes/portable_direct/R284KE_AFFINE_ZERO_FIBER_AND_SIGNED_JET_SIEVE_20261128.md; KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md (as carried by KF). JO 81cc0f06a4cf0209733a50284362f9bb1e8aded9:research_notes/portable_direct/R284JO_FULL_JOINT_BLOCK_TRANSFER_20261127.md checked for overlap: its block covers offsets 3<=r<=d, not the r=2 fiber u=q+d=0. The new proof treats a singular coordinate via the full integer carrier, not by applying JO outside its hypotheses.

## 1. Exact second jet at u=0; a fixed-degree observer

Use JR's notation u=q+d, n=2q+d, l=d-k; D_v=prod_{i=0}^{d-1}(v+i+3), S_v(k)=prod_{i<k}(v-i) prod_{k<=i<d}(v+i+3). Put a_k=(k+1)(l+1)S_u(k)S_n(l), b_k=(k+1)l S_u(k)S_n(l-1) for l>=1 and 0 otherwise. Write v=sum a_k, b=sum b_k, a=sum (u-k)(u+k+2)(a_k+b_k); J=2u(2u+1), L=4n+2. The full integer carrier is
Wn=L a+u S_u(d) D_n (u-d)(2d+3)(n+2),
Qn=JL b,
Zn=L(q a+J(b+v)),
P=3q(4q+3d+1)^2 Wn Qn-32(3q+d+1)Zn^2 = D^2 C,
D=JL D_u D_n.
Legal positive q has D>0. These are cleared observations, not the original rational values at a pole.

Theorem A (all integers d>=3). P has exactly a double zero at q=-d, and with
B=((d+2)!/2)(-1)^d (2d-1)!/(d-1)!,
L0=2-4d,
f(d)=64d^6-61d^5+13d^4+61d^3-29d^2+16,
one has
    (P/u^2)(-d)=8 L0^2 B^2 f(d)/(2d-1)>0,
    0<f(d)<64d^6.
In particular, the entire factorial-scale second jet reduces to a sextic after known factors are removed.

Proof. Use h=u=q+d as the local variable, n=-d+2h. At h=0, S_0(0)=(d+2)!/2; all S_0(k) with k>=1 vanish. In the n branch S_{-d}(l)=0 for l<=d-3, because its tail includes i=d-3; S_{-d}(d)=(-1)^d (2d-1)!/(d-1)!, and the ratios S_{-d}(d-1)/S_{-d}(d)=-2/(2d-1), S_{-d}(d-2)/S_{-d}(d)=1/((d-1)(2d-1)). Thus v0=(d+1)B, b0=-2d B/(2d-1), a0=0. All three cleared observations vanish at h=0.

For a1=[h]a, only k=0,1,2 survive: at k>=3 both branch factors vanish; at k=0 the weight (u-k)(u+k+2) has derivative 2; at k=1,2 its values are -3,-8 and [h]S_u(k)/S_u(0)|_{h=0}=1/3,-1/12 respectively. The three normalized contributions are
2(d+1-2d/(2d-1)),
-2(-2d+1)/(2d-1),
2/(2d-1).
Their sum is exactly 2(d+1). Hence a1=2(d+1)B. Endpoint retained: u S_u(d) D_n has order at least 3 (each factor vanishes), so its first jet is zero; this is a proved local omission, not an assumption on E.

Consequently [h]Wn=2(d+1)L0 B, [h]Qn=-4d L0 B/(2d-1), [h]Zn=L0 B[-2(d^2-1)-4d/(2d-1)]. Substituting into the second jet of P gives the formula, with both terms positive: at q=-d the Wn/Qn first jets have opposite signs, the first prefactor is negative, and -32(1-2d)>0. The upper bound follows from 13/d+61/d^2+16/d^5<61 for d>=3. The exact positive coefficient proves multiplicity two.

Corollary (large-prime pole certificate). For p>2d+2 and p|q+d, any legal integer zero of C requires p|f(d); more precisely v_p(q+d)<=v_p(f(d)). Indeed P/u^2 is an integer polynomial (monic division), so q+d divides its value at -d if it vanishes at q. All factors of L0,B,2d-1 are p-units; the valuation of the displayed value equals v_p(f(d)). Also D/u^2 is a p-unit at q=-d: J has one factor u, D_n has the factor 2u at i=d-3, all other factors are units at this residue (L0=-2(2d-1)). If p does not divide f(d), P/u^2(q) is a unit and the exact valuation v_p(C(q,d))=-2v_p(q+d) follows. The rational remaining observer has a genuine pole at the formal fiber; the legal integer nonzero certificate retains it.

## 2. Additional integer factors and a uniform content divisor

KF's G_d=prod_{(d+1)/3<j<=d/2, j integer}(q+j)^2 divides P. Besides u^2, the primitive linear factor ell=4q+2d+1=L/2 divides P because Qn and Zn contain L. If d is odd, put q0=-(d+1)/2, u=(d-1)/2, n=-1. All original denominators are nonzero, R_{-1}(l)=(-1)^l/(l+1); the two original a_k+b_k cancel exactly for l>=1, and l=0 vanishes since R_u(d)=0. Therefore A=E=W=0, Q+V=Z=0 and C=0, giving the monic factor q+(d+1)/2. KE supplies q+(d+1)/3 for d=2 mod 3 (d>=5). Denote the optional factors by F_odd and F_KE (else 1). All new factors are pairwise coprime over Q with G_d, primitive over Z.

A uniform scalar divisor follows from the n branch's coefficient parity, not just its integer values. In S_n(k), each of the d factors has slope 2; even constants alternate as i moves. Starting at k=0 there are floor(d/2) even constants for even d and ceil(d/2) for odd d. Replacing tail factors by falling factors changes this number by alternating +1,-1 (even d) or -1,+1 (odd d). Hence every S_n(k) belongs to 2^m Z[q], m=floor(d/2). The endpoint product D_n(n+2) belongs to 2^(m+1) Z[q] for both parities: n+2 is even as a polynomial for even d, while D_n has m+1 even factors for odd d. Therefore Wn and Zn are in 2^(m+1) Z[q] and Qn in 2^(m+2) Z[q]. The first term of P has another factor 4 when d is odd because 4q+3d+1 has even coefficients. The second term is in 2^(2m+7) Z[q]. Thus
    2^kappa | content(P), kappa=2m+3+2*(d mod 2).
This is a lower bound, not an exact content formula.

Define the strengthened quotient
    H_d=P/[2^kappa G_d (q+d)^2 ell F_odd F_KE] in Z[q].
Integrality follows from Gauss's lemma for the product of primitive factors after the scalar division. Every removed factor is positive at legal q, so H preserves sign and zero set. At each KF index j in J_d, write M_j=(P/G_d)(-j). The new entire-composite constraint is
    q+j | H_d(-j)
    = M_j/[2^kappa (d-j)^2 ell(-j) F_odd(-j) F_KE(-j)].
All denominators in the displayed expression are nonzero, and the quotient is exactly integer. It is at least as restrictive as KF's original test and can be evaluated with its existing T_{d,j} observer; no factoring of M_j is required. There is an additional q+d | H_d(-d) constraint. The latter is computed by Theorem A divided by the other retained known factors. Those extra factors at -d have no prime divisor >2d+2, so the sextic large-prime constraint is unchanged. Keep all removed factors and original carrier in the representation for exact reconstruction. The exact degree is 4d+9-2|J_d|-3-I_odd-I_KE.

## 3. Uniform exception count on the new coordinate

In KD's bracket for d>=81, q in [4d^2/5,4d^2/3], set N=q+d. Then N<(2d+2)^2. Hence at most one prime p>2d+2 divides N, and its exponent is one. A possible zero with such a factor must have p|f(d). Since f(d)<64d^6 and the product of six distinct such primes exceeds (2d+2)^6>64d^6, there are at most five exceptional large primes per d, independent of d. All budgets having a large prime factor in this coordinate that can survive the new necessary sieve are in at most five arithmetic progressions, and their number is at most
    5*( (8d^2/15)/(2d+3)+1 ) = O(d).
If N itself is prime, there are at most three surviving candidate budgets, since four distinct prime values N>=4d^2/5 have product greater than 64d^6 for d>=81. These are necessary conditions, not an assertion that any remaining candidate is a root. Smooth N (all prime factors <=2d+2) still requires other constraints, including the complete composite quotient of section 2.

## 4. Executed exact computation

Certificate: 8d6a334b0713e70e2267dbe0a71ba7bdfa853651:research_notes/portable_direct/R284KG_sextic_fiber_certificate.py; Git blob 72d24756b06b16eb28ad25dc3f1ee0cd37c44214, SHA256 22b2e3a9c0e1edfe3fd2029d7cf633abdb7e7e67665957cdb20fb32e3c7625eb. Executed local file matched remote blob and full readback. Exact integer dual-number propagation mod h^2 of all cleared observers independently verifies the first jets and resulting second jet on d=3..300 (298 cases). No floating point.

New finite sieve domain d=3001..3100, all integer q in KD bracket, 496,340,491 distinct (d,q) pairs. Count all N with eligible large prime by exact prime sieve to maximum N and sum over t>=1 of prime counts in [ceil(a/t), floor(b/t)] intersected with p>2d+2; uniqueness p and t from N<p^2 makes this a disjoint count. For each such prime p<=b evaluate f(d) mod p by integer Horner; NumPy int64 multiplication is exact since d*max_b+64<2^63. The script prints all per-d rows. Actual output summary:
    exact integer jet identities: d=3..300 (298)
    {'domain': [3001, 3100], 'initial': 496340491, 'large_prime_budgets': 321577913, 'excluded': 321570221, 'remaining_large_prime_budgets': 7692, 'max_remaining_per_d': 718, 'max_eligible_exception_primes': 3}
Thus 321,570,221 budgets rigorously excluded by this new coordinate alone; 7,692 large-prime budgets remain under this test, and 174,762,578 smooth-coordinate budgets remain. The numbers count the entire bracket, not pointwise root candidates. The prior KD all-budget interval 3..3000 remains unchanged. The content/factor theorem in section 2 is proved algebraically, not claimed to have an additional executed exhaustive sieve test. No independent review or formal Result.

## Next

Use the closed sextic arithmetic and whole-composite normalized M_j simultaneously. Investigate the smooth q+d population and the intersection with other branch coordinates without independence assumptions. Compute sharper content using the integer carrier's parity and fixed divisors; test whether new whole-composite constraints or a second small-degree pole observer close additional families. Do not repeat KD bridge or KF finite tests as a substitute for the open unbounded problem.
