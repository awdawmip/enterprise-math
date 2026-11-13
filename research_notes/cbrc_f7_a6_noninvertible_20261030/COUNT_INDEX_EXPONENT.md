# F7 A6 fixed-scalar injective models: exact multiplicity by index and exponent

**AUTHOR_SIDE / EXPOSED_SHARED_CONTEXT / NOT_INDEPENDENT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** This is an unadmitted corollary added to existing Draft PR #1753, not an independent Driver review, canonical Result or task publication. The frozen F7 GL4(Z) no-go is unchanged.

Frozen source: Task RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION; Result RR-AA38973D56330E59D315, Git blob 3366edeae347e76b1f6a50bc45a6c6e4cd2dd472; return blob 69265a0fadfd9fcd0be9354ff74f33e5e825fe84.

## Precise mathematical scope

Work with G=Z^4 ⊕ (Z/3Z)^2, C=[[1,1],[1,-1]], D=diag(C,C), and Q(w,t)=(#supp(Dw))/2. The earlier author-side classification assumes injective additive F:G→G, globally conserved Q, and balanced marked elementary input of scalar 1/2 in each output slot, and derives the unique form

F(w,t)=(Aw,Kw+Bt), A=D P diag(k1,k2,k3,k4) D,

where P is one of 16 admissible split permutations, each k_i is a nonzero integer, K is any 2×4 matrix mod 3, and B∈GL2(F3). The earlier Smith theorem gives index I=16⋅Π|k_i| and cokernel exponent E=4⋅lcm_i |k_i|.

**Exact joint multiplicity theorem (within that fixed model):** For m,L positive, put e_p=v_p(m), t_p=v_p(L). Define N4(e,t) as the coefficient of x^e in [(1+x+...+x^t)^4 − (1+x+...+x^(t−1))^4], interpreting the second term as zero when t=0. Then the number H(m,L) of distinct maps with I=16m, E=4L is

H(m,L)=80,621,568 × Π_{p|m} N4(e_p,t_p), if L divides m; otherwise H(m,L)=0.

An empty product is 1, giving H(1,1)=80,621,568. For positive e, N4(e,t)>0 exactly when 1≤t≤e≤4t. Thus H(m,L)>0 exactly when L|m|L^4, strengthening the previously established existence criterion by giving exact multiplicities.

Summing over the exponents, the number of maps of index 16m is exactly

H_index(m)=80,621,568 × d4(m), where d4(m)=Π_{p^e || m} binomial(e+3,3).

Equivalently Σ_{m≥1} H_index(m)/m^s = 80,621,568 ζ(s)^4 for Re(s)>1.

## Unrestricted proof

Since D is rationally invertible, A uniquely determines the monomial matrix D A D^(-1)=2P diag(k): both the split permutation and all four signed multipliers can be recovered. Different P,k cannot denote the same A, and the prior classification asserts that all allowed A are of this form. For each ordered positive multiplier quadruple there are independently 2^4 choices of signs, 16 split P, 3^8 torsion couplings K and |GL2(F3)|=(9−1)(9−3)=48 invertible B. Their product is precisely 80,621,568 distinct injective endomorphisms, with no overcount.

Unique prime factorization makes the product constraint Π|k_i|=m and the lcm constraint lcm|k_i|=L equivalent, independently at each prime, to four labeled nonnegative valuations r_i with Σr_i=e_p and max(r_i)=t_p. Bounded-sum generating polynomials count these as N4(e_p,t_p), proving the joint formula by multiplication over primes. For e>0 the permitted values of max are exactly ceil(e/4) through e. The stars-and-bars count for four nonnegative valuations of sum e is binomial(e+3,3); multiplying over primes yields d4(m). Its standard Euler product yields ζ(s)^4 on Re(s)>1. These arguments are general and exact, not inferred from finite testing.

## Finite evidence and example

The companion deterministic Python regression COUNT_INDEX_EXPONENT.py exhaustively enumerates 5,137 ordered positive quadruples with product m≤128, checks every index-total and all possible lcm multiplicities against the coefficient formula, and sees 221 nonempty (index,exponent) pairs. Recorded machine output is COUNT_INDEX_EXPONENT_RESULT.json, PASS. The test only verifies that finite domain; the above prime-factorization argument supplies the universal proof.

For m=32 (I=512), the respective positive-tuple counts at L=4,8,16,32 are 16,24,12,4. The associated exponent values are E=16,32,64,128 and the *endomorphism* multiplicity at each is 80,621,568 times that count. Total 56 positive quadruples = binomial(8,3).

## Non-admission and model boundaries

The derivation depends on the earlier author-side classification and Smith theorem, neither of which is newly independently audited here. It applies only to the stated fixed four-channel scalar and injective endomorphisms. It does not establish claims for arbitrary scalar conservation, surjectivity, extra F7 operator-equivariance of all torsion couplings, native X6 geometry, or a complete three-dimensional research slice. These GitHub files do not effect native Review, Reference, Synthesis, Follow-up, P000/Foundation/Working Truth changes or any formal task publication. The original invertible F7 Result remains NO_GO.
