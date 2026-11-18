# PREFIX-894 — Time reversal and exact LCM collision coverage of the strict-19-bit modulus square

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6, independent named-source BRC observation auxiliary. Frozen scientific-input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessor: PREFIX-893 (complete 16 first-port rows); supporting source: PREFIX-883 (zero-step collision criterion), PREFIX-890 (disjoint collision types).
Status: AUTHOR_PROVED / TWO_LANGUAGE_EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. Native RS-X6-TIME ownership and physical time-dynamics claims remain separate.

## Exact finite problem and carrier

Let p=32, N=2^p, A=262145, B=524287, Q={A,A+2,...,B}, |Q|=131072. A directed named trajectory is Z_x=(x,x) or F^i_x=(x,x xor 2^i), with 0<=x<N and 0<=i<32. Its observed pair is Phi_(q1,q2)(u,v)=(u mod q1,v mod q2). Name, type, port order, multiplicity and directed source transition remain typed; these constructions assert collision of this exact finite BRC observer.

Write S={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285}. PREFIX-893 has verified one actual colliding pair of trajectories for EVERY ordered (q1,q2) with q1 in S and q2 in Q (16*131072=2097152 inputs). We extend this to a two-sided block and then add an exact, larger, overlap-free zero-step block.

## Theorem 894-A: time-reversal transport of a complete collision certificate

Define R(Z_x)=Z_x and R(F^i_x)=F^i_(x xor 2^i), reversing the two temporal endpoints while preserving the named source i. R is an involutive bijection on the legal trajectory population. For every trajectory T=(u,v),

   Phi_(q2,q1)(R(T)) = swap(Phi_(q1,q2)(T)).

Consequently two distinct trajectories collide for (q1,q2) if and only if their reversals collide for (q2,q1). This is a witness-level bijection, so no assumption about injectivity or collision counts is necessary. It also proves C_p(q1,q2)=C_p(q2,q1) for full named collision multiplicities.

Applying R to the full PREFIX-893 set gives collision certificates for all q2 in S. The union U_S={(q1,q2) in Q^2: q1 in S or q2 in S} has exactly

   |U_S|=2*16*131072-16^2 = 4194048

ordered parameter pairs. The 256 double-membership pairs are counted once. The source witness for an input with q2 in S is obtained by reversing the corresponding original PREFIX-893 witness for (q2,q1); this is a constructive transport, not a fresh 16-column enumeration.

## Theorem 894-B: necessary and sufficient ZZ criterion

For any positive moduli q1,q2, two distinct zero-step trajectories Z_x,Z_y collide if and only if

   lcm(q1,q2) < N.

Indeed their separation |y-x| is a nonzero multiple of both moduli and at most N-1. Conversely, when L=lcm(q1,q2)<N, the explicit witness is Z_0=(0,0), Z_L=(L,L).

Since A^2>16N and B^2<65N, for odd q1,q2 in Q with g=gcd(q1,q2), a ZZ collision requires g>=17, and g>=65 always suffices. The exact intermediate gcds 17,19,...,63 must additionally satisfy g*a*b<N, where q1=g*a,q2=g*b and gcd(a,b)=1.

## Theorem 894-C: full finite ZZ census and disjoint union

Define E_g as the number of ordered (q1,q2) in Q^2 with gcd exactly odd g. For g>=65 all E_g pairs satisfy the ZZ criterion. Let m_g be the number of odd multiples of g inside Q. Descending odd-g divisor inversion gives the exact recurrence

   E_g = m_g^2 - sum_{t>=3 odd:gt<=B} E_(gt).

For 17<=g<=63 odd put a_min=ceil(A/g), a_max=floor(B/g) and T_g=floor((N-1)/g). The additional exact ZZ count at gcd g is

   H_g = sum_{a odd in [a_min,a_max]} sum_{b odd in [a_min,min(a_max,floor(T_g/a))]} 1_{gcd(a,b)=1}.

The inner coprimality test is computed exactly by inclusion/exclusion over squarefree divisors d|a:

   # eligible b = sum_{d|a} mu(d) * # odd multiples of d in [a_min,min(a_max,floor(T_g/a))].

All summands use integer floor/ceil and have an explicit finite domain. This is a proof of coverage of the enumerated input domain, not a probabilistic estimate.

The exact program and independent second-language recalculation give

   sum_{g>=65 odd} E_g = 108769846
   sum_{g=17,19,...,63} H_g = 100280938
   # {(q1,q2) in Q^2: lcm(q1,q2)<N} = 209050784.

Let t=# {(s,q):s in S,q in Q,lcm(s,q)<N}=15250, and d=# {(s1,s2) in S^2:lcm(s1,s2)<N}=22. By set inclusion/exclusion, the number of ZZ-positive pairs with BOTH ports outside S is

   209050784 - (2*t-d) = 209020306.

That set is disjoint from U_S by its definition, hence the certified collision-positive union has

   |U_S union ZZ_(Q\S)| = 4194048 + 209020306 = 213214354

different ordered 19-bit modulus pairs, or 213214354/17179869184 of the whole Q^2 domain (about 1.2411%). In particular, this is an exact independently usable bound on the total number of observation-injective pairs in Q^2: at most 16966654830 remain, before other earlier exclusions. The count does not assert that the remaining inputs are injective.

The count t=15250 independently matches the PREFIX-893 first-success zero-step class. In this 19-bit range ZZ requires noncoprime moduli, while ZF and the dyadic positive-completion family both require coprimality; therefore those three families are disjoint at the parameter-pair level.

## Verification and representation scope

The Python3 script PREFIX894_R6_LCM_REVERSE_COVERAGE.py recomputes both gcd census sums, the complete 16-by-Q overlap, the 16-by-16 correction, and the exact union; it checks gcd-partition completeness, arithmetic assertions, a direct brute-force comparison on small finite sample domains, and the published PREFIX-893 row total. An independently implemented JavaScript exact-integer checker gave identical 25 H_g values, E_g sum, t, d and union. All integers remain within binary64's exact integer range; no floating-point approximation participates in summation. The 67 actual FF witnesses in PREFIX893_R6_FULL_PANEL_CERTIFICATE.json were independently checked for range, XOR legality, modular collision and legality after reversal; zero violations.

Time reversal is an operation on the declared directed finite transition carrier with two ordered observation ports; it is not a claim that a native six-axis temporal process is physically reversible. The source/branch types remain distinct and no source provenance is erased. This is an exact mathematical auxiliary theorem over the frozen scientific observer, retaining P000 as the separate native research premise.

## Reproduction and next scientific question

Run Python3 PREFIX894_R6_LCM_REVERSE_COVERAGE.py in any Python3 standard-library environment. It emits a complete JSON certificate with all 25 small-g exact counts and checks. The static result file PREFIX894_R6_LCM_REVERSE_RESULTS.json holds the exact expected values and original immutable source path references. Upstream scientific frontier is PREFIX-893 at research_notes/portable_direct/2026-11-18_r6_prefix893_closed_16_row_ff_coverage.md and the two PREFIX893 JSON inputs at the same directory.

Next: incorporate U_S and the ZZ block into a deduplicated exclusion manifest, then classify new q1 rows outside S and the ZZ domain with PREFIX-891 endpoint and PREFIX-893 general FF witness construction. The wider frozen objective B_fix,odd(32) in {19,20} remains unresolved. Only a canonical live claim may authorize changing a shared X6 time-dynamics run; independent science is source-preserved separately.


## Corollary 894-D: combine the independently proved single-axis family

PREFIX-887 gives an additional exact parameter family: if q1 or q2 lies in A_32={odd q in Q: q divides 2^h-1 or 2^h+1 for some integer 1<=h<32}, then the original named observer has an axis-aligned FF collision. A complete exact divisibility pass gives |A_32|=24 and S intersect A_32 is empty; the 24 values are listed in the JSON certificate. Two implementations (iterative modular doubling and direct integer divisibility of 2^h±1) agree.

Let T=S union A_32, so |T|=40. Every pair with at least one port in T has a collision, using either PREFIX-893/894-A time reversal or PREFIX-887 axis witnesses. The two-port union now contains 2*40*131072-40^2=10484160 pairs.

The number of ZZ-positive pairs touching T in the first port is 108342, and the T×T ZZ-positive intersection is 142; thus the ZZ-positive block with neither port in T has 209050784-(2*108342-142)=208834242 inputs.

**The stronger, disjoint certified total is**

   10484160 + 208834242 = 219318402

ordered pairs, leaving at most 16960550782 unexcluded by THIS combined certificate. This supersedes the earlier U_S-only count as the latest PREFIX-894 coverage total. The 219318402 parameter pairs each have an explicit certificate construction or a cited earlier certified witness; global uniqueness/exhaustion of the remaining 19-bit domain is still the next science frontier. The project-native verification code and result JSON have been extended and read back at a new immutable Git commit.
