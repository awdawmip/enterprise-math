# Next independent mathematical unit

Objective: complete the integer-budget optimal allocation for s=1/9, h=1/42 at every K>=1, and determine the **smallest** eventual period-17 threshold.

Established at this source:
- Frozen pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34 and costs (17/9,1).
- For all K>=187: unique optimum (9 floor(K/17), K mod 17), rigorous Fraction certificate.
- For every K, configurations with T count not divisible by 9 lose to the period candidate, uniformly by C_B/9-8E-16d>0.
- At each K<187 the only surviving configurations are endpoint candidates (0,K) and (9 floor(K/17), K mod 17), by convexity. Equality/ties must be checked exactly.

Smallest next work: for each L=1..10 and r=0..16 with K=17L+r<187, compare the true shared-optimizer C(9L,r) with K*C_B by rational interval enclosures; prioritize near-ties and publish a finite exact classification. Endpoints are proven as the only remaining candidates, hence at most 170 comparisons. Use a shared Chernoff exponent; do not add individual optimizer values. Extend parameter study near s=1/9 after the finite prefix.

Researcher native owner/claim was not confirmed (read-only Site configuration / CONTROL_QUOTA); publish this author-side result as a provenance checkpoint, not accepted Result.
