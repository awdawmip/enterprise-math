# Fixed R₄: sharp order at budgets 16 and 17

Both the root-residue observer and the full-future observer have exact maximal necessary orders 161,280 and 322,560, respectively, at budgets 16 and 17. With the preceding results, exact doubling holds at budgets 11–17. This sharp-order theorem does not enumerate the minimal sufficient support or determine root densities.

## Reduction and lower bound

The [compulsory-pair proof through 17](https://github.com/awdawmip/enterprise-math/blob/4e697e7f251c5609589eca00ff07d2ee61709e09/research_notes/portable_direct/riesel_r4_fifteen_sharp_20261125/REPORT.md) retains 5 and 13. In an inclusion-minimal residual cover using dedicated modulo-three phases on $v=(n-8)/12$, each phase must have a dedicated class: a phase without one would be covered by the shared classes alone, and CRT would transfer that cover to all phases. Substitute the fixed 19 and 73 on the first two phases. This leaves 12 or 13 tail classes at $n=32+36w$. In the all-shared case do not impose this substitution. The [ordinary-root CRT switch construction](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md) provides the matching lower bound $5040\cdot2^{b-11}$ for both observers.

## Upper bound and reproducibility

The residual mask in $w$ is $B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\bmod35$ with optional fixed classes $2:1,3:1,4:2$. Split over the fixed classes and allowed complete mod-seven rows. For every remaining class $h$, the private-point digit cost on the progression of the branch common base period $L$ is $\sum e(p-1)\le k-1$ for $m=h/\gcd(h,L)$ and $k$ remaining slots. Form the integer capacity upper bound using the distinct witnesses for each digit and leaving the remaining slots unconstrained. This calculation relaxes actual prime inventory, so does not miss an available phase. It includes every permissible relative period, not a numerical truncation on the underlying primes.

For the high candidate class $h$ and each private point representative $x$, translate by multiples of $L$ to put $x$ in the base interval. All other classes must avoid $x$. Start with finitely many residual points and enumerate covers of these points in $k-1$ slots; only add points if the candidate fails on the complete joint period. A hit on another point contributes its entire sampled mask. Removing duplicate/dominated masks preserves a possible finite cover because only slot count constrains the relaxed model. An impossible finite cover is an obstruction for the infinite cover. The budget-17 replays use the widened key encoding for all branches, not only the two wide branches.

At 16 there are 17,916 rejections across 232 branches for $h>4480$; at 17, 22,685 across 233 branches for $h>8960$. Both give raw order bounds $36h$. The parallel all-common capacity calculation applies the same private-point weight to $f/\gcd(f,35)$, with $3\nmid f$, at most 14 or 15 slots, and raw order at most $12f$. Maximal surviving $f$ equals 5600 and 11200, hence common raw orders are at most 67,200 and 134,400, both strictly below the split bounds. This is an upper-bound screen, not a claim that those periods occur.

For any relevant odd prime, an observed future value $a^2 2^n-1$ determines $a^2$ modulo that prime, because $2^n$ is a unit; the covering tests use only $a^2$. Knowing the root residue also determines it. Combined with the lower switch this proves both exact orders.

Run the paired high-exclusion scripts with threshold 4480 or 8960 and `forward` / `reverse`, and run both shared-order-capacity companions. The receipts record all counts. This is a reproducible mathematics archive, not a new official claim, task acceptance or independent third-party review.

Validated finite-search node counts: budget 16, 740049 forward and 739611 reverse; budget 17, 1090518 forward and 1029485 reverse. The largest branch joint periods are 558835200 and 33530112000, both exactly representable in the arithmetic used. The receipt records both full replays.
