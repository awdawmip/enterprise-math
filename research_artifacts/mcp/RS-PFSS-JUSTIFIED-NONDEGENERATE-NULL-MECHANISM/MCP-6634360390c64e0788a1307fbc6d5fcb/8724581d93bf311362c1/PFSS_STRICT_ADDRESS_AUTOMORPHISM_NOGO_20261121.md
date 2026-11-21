# PFSS strict address-preserving exchangeability: exact no-go
Date: 2026-11-21. Task: RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM, TP2-CED1A3712793223C0ABE.
Research mode: EXPLORATION, scoped exact lemma; NOT_REVIEWED. Original same-session Researcher: EM-X6-C7A253.

## Typed setting and statement
Let Q be a finite set of globally shared arithmetic q-addresses, with an injective native address map i:Q -> N. The deterministic arithmetic field x:Q -> {0,1} may be the prime/semiprime indicator, and C is a finite cell incidence family. A strict address-preserving permutation g:Q -> Q must satisfy i(gq)=i(q) for every q (plus any other incidence/readout-preservation requirements).

**Lemma 1.** Every strict address-preserving permutation is the identity. Therefore any proposed exchangeability null formed solely by randomizing one fixed, fully address-labeled arithmetic carrier over these permutations is a point mass; every deterministic shell observable has variance zero under that randomization.

Proof: Since i is injective, i(gq)=i(q) implies gq=q for every q. All group orbits of the full labeled state are singletons, so their induced observables are constant. This includes shared-q consistency automatically.

**Lemma 2.** Allowing a compensating automorphism of (N,0,1,+,*) does not change Lemma 1: every unital semiring automorphism alpha fixes 1 and all n=1+...+1; hence alpha is the identity. An arithmetic automorphism that truly preserves the full number labels and their operations cannot produce a nontrivial null orbit.

## Discriminating toy case
Take Q={q4,q5}, i(q4)=4 and i(q5)=5; use x(q)=1 if i(q) is a semiprime (prime factors counted with multiplicity). Then x(q4)=1 and x(q5)=0. A uniformly random transposition of the two **unlabeled** positions gives a Bernoulli(1/2) value at the first position and variance 1/4. But this transposition exchanges the exact integer addresses 4 and 5 and is not an automorphism of the typed labeled carrier. The apparent nondegeneracy is produced by changing the observer/source model.

## Exact boundary and next work
This is a no-go only for strict full-address-preserving automorphism-orbit randomization, NOT for independently randomized sampling designs, external arithmetic ensembles, or a quotient with a proven observer-safe equivalence relation and a nontrivial remaining action. For a proposed quotient, explicitly state whether the required shell observables descend, whether native q-address sharing survives, and whether nonzero support variance is established without residual fitting. The next useful test is to search an independently specified experiment/invariance with actual nontrivial support, not to add cell-wise iid noise.

No protected PFSS holdout at X=300000000 or X=1000000000 is accessed. Prior Results RR-9F084B92BE8261F3A8D7 and RR-4760E87D1D3AD2F6AFFA remain frozen, and their Driver reviews remain independent. This note is not a terminal ACCEPTED_MECHANISM or NEGATIVE_BOUNDARY.
