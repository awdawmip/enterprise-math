# R5 observer separation — smallest exact radius-two counterexample

Date 2026-11-14. Scope: derived ordered-integer radius-2 center cover. Mathematical status: author-side proof with fully enumerated finite certificate; NOT_REVIEWED. This is a new **general observer comparison**, not an empirical claim that one of the particular 13 R5 D-inert gaps changes its fixed-budget cost.

Let D(X) be the minimum size of a selected center subset S⊆X such that every x∈X has |x-s|≤2 for some s∈S. Let J_X(K) minimize the sum over x∈X of the distance to its closest selected center, among feasible |S|=K.

**Counterexample (five event coordinates).** Take

~~~
X=(0,1,2,4,7)  with gaps (1,1,2,3).
Y=(0,1,2,4,6)  with gaps (1,1,2,2).
~~~

Y is obtained by shortening only the final gap 3→2. Exact center-subset enumeration yields

~~~
D(X)=D(Y)=2.
J_X(2)=5, attained by S={2,7} (unique).
J_Y(2)=4, attained by S={1,4} or S={1,6}.
J_X(3)=J_Y(3)=2; J_X(4)=J_Y(4)=1; J_X(5)=J_Y(5)=0.
~~~

Thus a gap can be **inert for the minimum center count** yet change the minimum total correction cost at the *same fixed budget*, even though no feasibility threshold changes. Center-count factorization is therefore not, by itself, a lossless observer for the full fixed-K cost spectrum or optimal center witnesses.

**Smallest size in the general integer model.** Five event points are necessary for such a one-gap 3→2 witness. To prove it, first note a radius-2 separation lemma: any adjacent gap at least 3 separates the two sides for every feasible center assignment, because no point across that gap can serve as a radius-2 center. Replacing any *non-target* gap greater than 3 by 3 does not change feasibility, D or fixed-K total costs before or after the designated target gap is shortened; the separated blocks and their intrablock coordinates are unchanged. Hence, for n≤4, it suffices to enumerate all gap strings in {1,2,3}^{n-1}, each possible gap=3 as the target, and every K. The attached exhaustive script lists exactly 1+6+27=34 gap-target pairs for n=2,3,4; 10 of those have unchanged D, and **none** changes any existing fixed-budget J_K. The displayed n=5 witness realizes the obstruction. QED.

This no-cross-gap argument relies on the declared radius bound and center candidates being event points; it does not assert that all arbitrary metrics have the same five-point minimality.

**Evidence:** VERIFY_OBSERVER_INERT_GAP_COUNTEREXAMPLE.py is standard-library-only, enumerates every center subset for each case and prints PASS_EXACT_R2_MINIMUM_OBSERVER_SEPARATION. The local run passed. This new lemma is independent of the frozen R5 numeric source; for the frozen R5 **specific 13 D-inert gaps**, whether they affect J_K under some multi-gap closure remains an open question.

**Next:** test R5's actual frozen source with at least two cut closures and a low feasible budget K, or derive a general interval min-plus transfer preserving both D and J_K without assuming the 15-effective-bit D quotient extends to it.