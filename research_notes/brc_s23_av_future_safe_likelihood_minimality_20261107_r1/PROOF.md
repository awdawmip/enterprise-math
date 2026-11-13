# S23/AV: exact minimal future-safe likelihood observer on a lawful two-point fiber

Date: 2026-11-07. Status: AUTHOR_SIDE_PROOF_WITH_EXACT_FINITE_CHECKS; independent review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Immediate predecessor: PR #1777 at 2e4b287a045c1e2181de108fe290bba4fd4562e1 (first n=7 sign transition).

## Defined experiment and observer

In the lawful AV parameter box, take theta_0=(1/2,1/2) and theta_1=(5/7,7/8). Their full one-trial laws on ordered labels (1,3,4) are P_0=(1/2,1/4,1/4) and P_1=(5/7,1/4,1/28). The one-bit observer has the same parameter z=1/4 under each hypothesis. For an ordered full-label word w of length n write k=#1, ell=#4, r=#3; its likelihood ratio is

    Lambda(w)=P_0(w)/P_1(w)=7^(k+ell)/10^k=7^ell (7/10)^k.

A deterministic prefix observer T_n is future-sign sufficient for this *fixed two-hypothesis full-label experiment* if a single readout F satisfies

    F(T_n(w),u)=sign(P_0(wu)-P_1(wu))

for every length-n prefix w and every finite common future suffix u (including the empty suffix). The suffix is supplied unchanged, while discarded prefix information cannot be recovered. This is an observer-future-composition criterion; it is not the original minimax decoder problem delta_n.

## Theorem (exact minimal state capacity)

For every integer n>=0:

(1) The joint-count observer T*(w)=(k(w),ell(w)) is future-sign sufficient. Equivalently, its exact positive-rational likelihood Lambda(w) is a one-coordinate injective encoding of this pair.

(2) If any deterministic T_n identifies two prefixes with different (k,ell), it fails future-sign sufficiency: a single common finite suffix changes their two resulting likelihood signs to strictly opposite values.

(3) The minimum number of reachable observer states at prefix length n is exactly (n+1)(n+2)/2. Fixed-length binary encoding requires ceil(log_2((n+1)(n+2)/2)) bits; thus minimum asymptotic memory is 2 log_2 n+O(1) bits. No horizon-independent finite-cardinality state space can satisfy the exact future-sign criterion for all n.

### Proof

Every P_i word probability is positive. Independence gives Lambda(wu)=Lambda(w)Lambda(u). On appending a future symbol, (k,ell) changes by (1,0) for label 1, by (0,0) for label 3, and by (0,1) for label 4. The exact count pair therefore determines the sign after every suffix, proving sufficiency.

The likelihood is injective on nonnegative integer pairs: if
    7^((k+ell)-(k'+ell')) = 10^(k-k'),
unique prime factorization forces k=k' because 2 and 5 occur only in powers of 10, and then ell=ell'. Hence different count pairs give distinct likelihoods.

Let alpha=ln(7)>0 and beta=ln(10/7)>0. Their ratio beta/alpha is irrational: beta/alpha=p/q with positive integers p,q would imply (10/7)^q=7^p and hence 10^q=7^(p+q), impossible by prime factorization. The standard irrational-rotation density lemma says the residues of k beta modulo alpha are dense in [0,alpha), even when k is restricted to arbitrarily large positive integers. Thus the set {ell alpha-k beta: k,ell>=0} is dense in R: given x and epsilon>0, choose arbitrarily large k so x+k beta is within epsilon of a multiple ell alpha; large k ensures ell>=0. Exponentiating proves that the suffix-likelihood semigroup

    S={7^ell(7/10)^k: k,ell>=0}

is dense in (0,infinity). Every element of S is realized by a suffix with k ones, ell fours, and no threes.

Take two length-n prefixes with distinct likelihoods 0<L_1<L_2. By density, choose a common suffix u with 1/L_2<Lambda(u)<1/L_1. Then

    L_1 Lambda(u)<1<L_2 Lambda(u).

Both word laws are positive, so P_0(wu)-P_1(wu) has the sign of Lambda(wu)-1. The two extended words have opposite signs. If T_n had merged those prefixes, a single F(T_n(w),u) would be required to return two different signs, contradiction. This proves necessity.

Exactly sum_{k=0}^n(n-k+1)=(n+1)(n+2)/2 distinct (k,ell) pairs are realizable by length-n words, with r=n-k-ell. The count observer achieves this number and the necessity argument requires at least that many. The bit lower bound and growing-memory conclusion follow. QED.

## Explicit n=6 to n=7 BRC-information-loss witness

At n=6 choose w=111114, with (k,ell)=(5,1), and v=433333, with (k,ell)=(0,1). The Boolean summary "any label 4" is identical and both likelihood signs are positive:

    Lambda(w)=117649/100000>1;   Lambda(v)=7>1.

Append the same future symbol 1:

    Lambda(w1)=823543/1000000<1;  Lambda(v1)=49/10>1.

Therefore the n=6 Boolean observer cannot correctly evolve both prefixes' signs after even this single allowed future operation. This supplies a dynamic observer nonclosure interpretation of the predecessor's first static TV sign transition at n=7.

## Verification and limits

Companion VERIFY.py uses exact standard-library fractions. It checks unique rational count likelihoods at n=1..12; the explicit one-step sign split; and 1,386 pairwise common-suffix separations for all distinct count-state pairs at each n=1..7 using suffix counts <=40. Actual stdout is RUN_EVIDENCE.txt. The proof for every n relies on irrational-rotation density, not the finite regression. It supplies no uniform bound on how long the separating suffix must be.

BRC reuse decision: REUSE_APPLIED, exact joint-count/rational-likelihood observer and future-operation lease; the one-bit "any-4" quotient loses branching composition needed by suffix concatenation. This is the three-label auxiliary model, with no native X6 or heartbeat dynamical claim. It does not decide full-lawful delta_4, transfer to the six-source/ten-label mother model, or establish a formal Source Result/Review/CLAIM.