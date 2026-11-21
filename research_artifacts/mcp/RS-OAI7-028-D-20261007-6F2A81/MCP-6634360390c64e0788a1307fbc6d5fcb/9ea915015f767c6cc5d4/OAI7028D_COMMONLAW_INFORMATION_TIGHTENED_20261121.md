# OAI7-028-D: improved continuity cost for the common-law information telescope
2026-11-21. Status: NOT_REVIEWED; exact conditional-entropy lemma. Task RS-OAI7-028-D-20261007-6F2A81. External frozen source: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/information.tex (common-law budget), build/schedule.tex (smoothing). External claims are research inputs, not admitted Enterprise Math theorems.

## Lemma A: conditioning-alphabet-free continuity
Let P and R be joint laws of a finite word X and an arbitrary finite conditioning variable Y, with TV(P,R)=delta<=eta<=1/2; assume X has at most m>=2 possible values. Then
|H_P(X|Y)-H_R(X|Y)| <= h(eta)+eta log(m)
with natural logarithms. No bound on the alphabet of Y is needed.

Proof: maximally couple (X,Y) and (X',Y') under P and R and set E=1 when the pairs differ, with Pr(E=1)=delta. Conditional on E=0, the two joint pairs coincide. H(X|Y)<=H(X,E|Y)<=h(delta)+(1-delta)H(X|Y,E=0)+delta log(m), while H(X'|Y')>=H(X'|Y',E)>=(1-delta)H(X'|Y',E=0). The E=0 terms cancel. Reverse the roles and use monotonicity of h(delta)+delta log(m) on delta in [0,1/2]. For m=1 the conditional entropy is zero.

## Lemma B: common-law telescope
Fix a deterministic lattice walk whose each increment has at most K>=2 symbols. Let Q_j(t) be nested residue vectors, j=0,...,n, Q_0 empty, with Q_j(t+a) determined from Q_j(t) and the first a increments. Choose common time t* such that TV(Law(t*+a),Law(t*))<=eta<=1/2 for 0<=a<L_n. Let positive lengths L_1,...,L_n satisfy L_j | L_(j+1). W_L(t) denotes the next L increments. Define the batch charge c_j=I(Q_j(t*);W_(L_j)(t*)|Q_(j-1)(t*))/L_j. Then
sum_(j=1)^n c_j <= log K + (n-1)[eta log K + h(eta)].

Proof: Set a_j=H(W_(L_j)|Q_(j-1))/L_j and b_j=H(W_(L_j)|Q_j)/L_j at t*. Then c_j=a_j-b_j. Partition W_(L_(j+1)) into L_(j+1)/L_j successive L_j-blocks. The chain rule and additive update of Q_j give
H(W_(L_(j+1))(t*)|Q_j(t*)) <= sum_{a: L_j|a,0<=a<L_(j+1)} H(W_(L_j)(t*+a)|Q_j(t*+a)).
For each a, this pair is a deterministic pushforward of the time variable, so its joint law is TV-close by at most eta to the pair at t*. Lemma A, using only the word alphabet of size at most K^(L_j), bounds each conditional entropy by H(W_(L_j)(t*)|Q_j(t*))+h(eta)+eta L_j log K. Divide through to get a_(j+1)<=b_j+eta log K+h(eta)/L_j, then telescope over j, using a_1<=log K and b_n>=0.

## Scope and research value
For the pinned schedule, eta=T_+^(-9), n=O(log T_+), K=K_D, so error is o(1). This recovers the manuscript's common-law entropy telescope without the separate full nested-residue-alphabet size estimate in the continuity step. The frozen manuscript already contains the main telescope, so this is a *tightening of one proof component*, not a claim to have independently resolved its one-batch information lower bound, conditional coverage, Gaussian moat theorem, or an X6-native path translation. A typed X6 observer/residue representation must be proved separately before that transfer.

Next: inspect actual selected residue vector update and test one-batch lower bound with identical probability space and fixed auxiliary prime choices. Maintain NOT_REVIEWED until an independent review.
