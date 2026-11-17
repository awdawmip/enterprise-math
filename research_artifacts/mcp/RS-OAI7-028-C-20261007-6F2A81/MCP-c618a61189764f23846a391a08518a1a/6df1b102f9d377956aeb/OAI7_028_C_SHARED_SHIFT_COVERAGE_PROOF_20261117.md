# Shared-bit repair of marginal residue coverage: exact finite obstruction
Date: 2026-11-17. Task: RS-OAI7-028-C-20261007-6F2A81.
Source under inspection: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex. Status: author-side construction and finite check; independent review pending.

## Exact model
Fix integers k>=2 and 1<=s<=k, 0<beta<1, 0<tau<=3/8 and a prime p large enough for m=ceil(p^(1-beta))<=p/2. Work in Lambda=Z^k with signed homomorphisms phi_(j,+)(y)=y_j mod p, phi_(j,-)(y)=-y_j mod p. Let Y_j be independent uniform variables on A={m,m+1,...,p-1}, and let S select s distinct indices with independently fair signs, independently of Y.

For every S, the selected output is a product of s independent uniform distributions on sets of size p-m. Hence
H(F_S(Y))=s log(p-m)=(1-epsilon)s log p,
epsilon=log(p/(p-m))/log p ->0 as p->infinity.
For every signed marginal, precisely m residue classes have probability zero. Since the coverage definition in coverage-transfer.tex is
#{u:Pr[X=u]<tau/p}<p^(1-beta),
and m>=p^(1-beta), every signed marginal fails (tau,beta)-coverage despite near-maximal joint entropy.

## Shared displacement
Let B be one independent fair bit and h=Bm(1,...,1). Put Z=Y+h. For every coordinate j,
supp(Z_j) = A union (A+m mod p) = Z/pZ,
where the equality follows from 2m<=p. All residues have probability >=1/[2(p-m)]>=1/(2p)>tau/p. Sign inversion preserves this lower bound. Therefore all 2k signed coordinate marginals have zero exceptions and attain (tau,beta)-coverage. The joint displacement has H(h)=log2 nats, not k log2 nats.

The resulting joint vector is not fully supported: (m,0) for the first two coordinates lies in neither A^2 nor (A+m)^2. Thus the shared bit repairs every marginal but cannot be silently replaced by independent coordinate-wise shifts, nor used to claim full joint-vector coverage.

## Exact finite witness
p=101, beta=1/2, m=11, |A|=90, tau=3/8.
There are exactly 11 zero-probability residues before shifting; 11>sqrt(101). The entropy deficit ratio equals log(101/90)/log(101) ~0.02498544644505. One shared displacement bit yields minimum probability 1/180>3/(8*101), and zero deficient residues. The attached standard-library checker verifies every residue and the missing pair (11,0).

## Relation to the external transfer theorem
This example satisfies its finite lattice/signed-coordinate/entropy definitions, but does not claim its conditional next-checkpoint coverage premise, sample-size bounds or entropy budget. In particular, choosing A=Y as the conditioning variable makes a two-point conditional displacement law, not the near-complete conditional coverage required by Theorem "One-step coverage transfer." Its common data is H=(h_1,...,h_n), formed from conditionally iid displacements given the same checkpoint A. The source's hypotheses additionally require:
eta'<=eta*delta/100; epsilon+kappa<=eta*delta*beta'/16;
p exp(-delta^2 n p^(-beta)/2)<=delta/100;
delta^(-1)<p^(beta'/2);
log(2e/delta)<(beta'/4)log T.
For p=101 and delta<=1/64 the inequality delta^(-1)<p^(beta'/2) fails for all beta'<1, so this finite witness is an obstruction to entropy-alone reasoning, not a counterexample to the theorem.

## Open unit
Audit the transfer argument with the common A and the entire shared displacement sequence H, retain exact quantifier order and conditional independence, and determine the weakest reusable coverage threshold/conditional information cost. Any translation to native X6 needs its separately typed carrier and provenance-preserving BRC/observer interface.
