# OAI7-023A — exact cubic conjugate pairing and moment normalization
Date: 2026-11-19
Task: RS-OAI7-023-A-20261007-6F2A81 / TP2-015DC762EF197B716138
Status: independent elementary derivation; analytical first-moment theorem remains an external, unreviewed input.
Predecessor: research_notes/chatgpt_direct/20261007_oai7_6f2a81/RESEARCH.md (2026-10-07) already identifies 6/5 and 1/2 factors and states the pairing; this note expands the exact coefficient and exceptional-prime proof, not a new general first-moment result.
External source pin: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex (normalization subsection).

## Exact domain and conventions
Let O=Z[ω], ω²+ω+1=0. Let p>3 be an ordinary rational prime with p≡1 (mod 3). Choose conjugate primary Eisenstein primes π and barπ with π barπ=p and π≡barπ≡1 (mod 3). The residue maps O/(π), O/(barπ) are each F_p. Let χ_π, χ_barπ be the multiplicative cubic residue characters, extended by 0 at 0, normalized by the respective primary denominators. Put e_p(t)=exp(2πit/p) and
G(π)=p^(-1/2) Σ_{v mod π} χ_π(v) exp(2πi Tr(v/π)).
Set S_p=Σ_{x mod p} e_p(x³).

## Lemma A: additive coefficient is a removable cube
For integral v, Tr(v/π)=v/π+barv/barπ=(v barπ+barv π)/p. Its numerator is a rational integer; modulo the prime ideal (π), it equals v barπ. The embedding Z/pZ→O/(π) is an isomorphism. Therefore
G(π)=p^(-1/2) Σ_{t∈F_p} χ_π(t)e_p(barπ t),
where barπ denotes its nonzero class mod π.
By cubic reciprocity for primary π,barπ and the conjugation compatibility of the cubic symbol,
χ_π(barπ)=χ_barπ(π)=overline{χ_π(barπ)}.
The value is a cubic root of unity and also real, so χ_π(barπ)=1. Substitute u=barπ t in F_p; because χ_π(barπ)=1,
G(π)=p^(-1/2) Σ_{u∈F_p} χ_π(u)e_p(u).
The identical argument with π and barπ exchanged gives G(barπ)=p^(-1/2)Σ_u χ_barπ(u)e_p(u). Conjugation of denominators conjugates cubic residue character values on rational integer representatives, hence χ_barπ(u)=overline{χ_π(u)}=χ_π(u)^2, including both zero values.

## Lemma B: cube-root count
For u∈F_p define N₃(u)=#{x∈F_p:x³=u}. Since p≡1 (mod 3), for u≠0 the cube map on F_p× has a kernel of cardinality 3. Thus N₃(u)=3 for cubes and 0 for noncubes. For u=0, N₃(0)=1. Consequently, including u=0 with χ_π(0)=0,
N₃(u)-1=χ_π(u)+χ_π(u)^2.
Because Σ_{u∈F_p} e_p(u)=0, sum against e_p(u) and exchange sums:
Σ_u [χ_π(u)+χ_π(u)^2]e_p(u)
=Σ_u[N₃(u)-1]e_p(u)
=Σ_x e_p(x³).
Together with Lemma A this proves the *exact* equality for every p≡1 mod3:
G(π)+G(barπ)=S_p/√p.
No asymptotic limit, fitting parameter or analytical first-moment theorem is needed for this identity.

## Prime classification and constants
For p≡2 mod3, cubing is bijective on F_p because gcd(3,p-1)=1, so S_p=0 exactly. The sole ramified p=3 contributes at most one finite exception to either asymptotic convention.

For a primary Eisenstein prime sum up to norm X, every split p≡1 mod3 contributes *two* primary primes π,barπ of norm p. For inert p≡2 mod3, the unique primary prime has norm p², hence all inert primes appearing have p≤√X; the normalized nontrivial cubic Gauss sum has absolute value 1, so their aggregate is O(√X). Therefore, defining
A(X)=Σ_{Nπ≤X, π primary prime}G(π),  R(X)=Σ_{p≤X,p≡1 (mod3)} S_p/(2√p),
we have the exact decomposition A(X)=2R(X)+I(X)+E_3(X) with |I(X)|≤π(√X), E_3(X)=O(1); consequently A(X)=2R(X)+O(√X).
In particular, *conditional solely on the unreviewed external statement*
A(X)=(6/5)c_*X^(5/6)/log X+o(X^(5/6)/log X),
we obtain
R(X)=(3/5)c_*X^(5/6)/log X+o(X^(5/6)/log X).
This factor 1/2 comes from *two* primary Eisenstein primes above each split rational prime, not from partial summation.

Independently, for the elementary model c_* (Nπ)^(-1/6), prime ideal counting and partial summation yield
Σ_{Nπ≤X} c_* (Nπ)^(-1/6)
~ c_* ∫₂^X t^(-1/6)dt/log t
~ (6/5)c_* X^(5/6)/log X.
The 6/5 factor is reciprocal to 1−1/6=5/6 and originates from summation of the decaying norm power against prime density. This calculation establishes only the model's coefficient; it cannot establish that G(π) has that first moment without additional analytic estimates.

## Exact small-field check (independent, hand-checkable)
p=7: cubes of x mod 7 comprise 0 once, 1 three times and 6 three times. Hence S_7=1+3e_7(1)+3e_7(6)=1+6 cos(2π/7). The character side has weights 0 at 0; +2 at u=1,6; −1 at u=2,3,4,5, agreeing termwise with N₃(u)-1. For every split prime the character argument applies verbatim.

## Scope, provenance and next frontier
The pairing and prime-normalization algebra is complete in the declared conventions. This note does not independently check cubic reciprocity's proof, the external dispersion/large-sieve estimates, or its unconditional first-moment asymptotic; the externally claimed analytic theorem remains NOT_ADMITTED. Historical report already listed the two constants; this is an independently spelled-out elementary proof with an explicit O(√X) inert term and clear conditional moment inference.
Next useful step under current Task: verify source sign/primary representatives of the cubic symbol at the same pinned source, check any p=3 term and verify the original theorem's analytical input only if independently delegated; avoid replacing phase/cancellation by positive mass. Any native X6/BRC mapping requires an explicit typed observation, not a name substitution.
