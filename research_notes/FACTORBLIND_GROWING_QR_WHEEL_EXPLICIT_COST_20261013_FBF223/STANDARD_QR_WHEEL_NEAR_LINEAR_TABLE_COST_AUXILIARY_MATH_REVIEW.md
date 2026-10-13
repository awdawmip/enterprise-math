# Standard QR wheel: near-linear explicit-table cost

Status: mathematical PASS under the exact model below.
Auxiliary native identity: UNKNOWN / directed nonblind. No SID, RA, CLAIM, formal native review, experiment, or Source/native write is created.

Let N=pq with odd primes 3<=p<=q, c=ceil(sqrt(N)), T=(p+q)/2-c, and L=T+1. Thus T is a nonnegative integer and (c+T)^2-N=((q-p)/2)^2. Let M be the product of k distinct odd primes ell_i, with gcd(N,M)=1. The filter is exactly the conjunction that (c+t)^2-N is a quadratic residue INCLUDING zero modulo every ell_i; in particular it retains T. No additional selective filter is included. The same instance computes all M explicit table cells at cost at least lambda>0 each, then examines every retained candidate of 0,...,T at cost at least mu>0 each. These charges are distinct and additive. Lambda and mu are uniform fixed constants.

1. Exact local count.
For an odd prime ell not dividing N, pairs (x,y) with y^2=x^2-N are in bijection with (u,v) satisfying uv=N via u=x-y, v=x+y. There are ell-1 pairs because u may be any nonzero residue, and 2 is invertible. Hence
    sum_x chi_ell(x^2-N)=-1.
There are r=1+chi_ell(N) zeros of x^2-N. The number of x for which it is a square or zero is therefore
    a_ell=(ell-1+r)/2=(ell+chi_ell(N))/2.
The zero correction is essential.

2. CRT and density.
The shift x=c+t is bijective on residues. CRT gives exactly S=product_i a_ell_i survivors per full M-period. Thus
    delta=S/M >= 2^(-k) product_i (1-1/ell_i).
After sorting the distinct odd primes, ell_i>=i+2. Consequently
    product_i (1-1/ell_i) >= product_i (i+1)/(i+2)=2/(k+2),
    delta >= 2^(1-k)/(k+2),
    M >= product_i (i+2)=(k+2)!/2.
The empty wheel k=0,M=1 also satisfies these formulas.

3. Correct complete-period endpoint.
The inclusive prefix has length L=T+1 and contains floor(L/M) complete M-periods starting at 0. If M<=L, then floor(L/M)>=L/(2M), giving
    C >= floor(L/M) S >= L delta/2 >= L 2^(-k)/(k+2).
If M>L, the explicit table cost alone exceeds lambda L. Root's floor(T/M) bound for M<=T is valid but weaker; the L formulation covers the endpoint M=T+1 directly.

4. Uniform asymptotic quantifiers.
In the branch M<=L, (k+2)!/2<=L forces
    k=O(log L/log log L).
This uses only an elementary factorial lower bound: with n=k+2, n!>=(n/2)^(floor(n/2)). It requires no prime number theorem and its constants do not depend on N or the chosen primes. Therefore
    2^(-k)/(k+2) >= exp[-O(log L/log log L)].
Combining C with the candidate charge, and the M>L branch with table cost, yields constants A,B>0 and L_0 depending only on the fixed cost model such that, for every permitted instance and wheel with L>=L_0,
    W >= A L exp[-B log L/log log L].
Equivalently, for every epsilon>0 there is a uniform T_epsilon such that W>=T^(1-epsilon) whenever T>=T_epsilon, even if N and M vary with T. This is the precise meaning of W>=T^(1-o(1)).

Boundary.
This excludes fixed-power improvement in this explicit-table QR-wheel model. It does not exclude logarithmic or other subpolynomial compression, prove attainability, or apply to arbitrary periodic filters, additional selective filters, implicit/CRT-compressed tables, batched costs violating the fixed per-cell/per-candidate bounds, free or cross-instance amortized tables, or algorithms avoiding full-prefix examination. A modulus sharing a factor with N is outside the stated coprime model and can expose an immediate gcd factor; no general factorization lower bound follows. The frozen 600-case empirical failure is not used in this proof.

This is a new Root paper-only review derivation with the above limitations, not a modification of RR-C5769D6B237D02BFF025, its raw NEGATIVE_BOUNDARY verdict/target, or the preceding generic period-table review. The mathematical parent remains OPEN.
