# Stage477-B | Variable-k general-fiber support after exact structured family

Date: 2026-11-06. Scientific pins remain GLOBAL main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules are read separately.

Mother objective: exact full-labeled future equivalence, positive BRC population, support and rank/unrank for native X6 dual histories on a complete initial-observation fiber.

Completed unit: Stage476 proved directly (without relying on unreviewed Stage474.1) that for k>=1,u>=0,0<=b<=k+u, m=2k+2,n=3k+2u+4, P=A^m, Q with k visible variable B/C letters at k+3+2i and u hidden variable letters at 3k+5+2j, exactly b B in total, Q-POP=0 and P-POP/APPEND<=k, Q-APPEND<=1, complete future equivalence is equality of the k visible letters. Class mass=binom(u,b-#B(visible)), support=sum_a binom(k,a), raw mass=binom(k+u,b). Dynamic recursion S(0,r)=[0<=r<=u]; S(l,r)=S(l-1,r-1)+S(l-1,r) enables polynomial count and random-access rank/unrank despite exponentially many classes. Evidence and exact Python reproduction: this Stage476 directory in PR #1736.

Next independent question A: Generalize from this structured family to arbitrary Q edge counts where hidden letters interact across non-A boundaries. Find an explicit transfer state retaining last direction, residual directed edges, original match count and future-visible label obligations. Prove or refute polynomial bound when k grows. Start with k=4..7, u=2..4, and distinguish two cases of same Phi but different hidden-word continuation; report exact class mass or minimal counterexample and full transformation costs.

Next independent question B: Inspect Stage474.1 semantic theorem at Q-POP>0 and arbitrary P/Q interleavings, especially popping a newly appended direction and the first overlapping position following both POP histories. Check necessity and sufficiency separately with the full signed 12-direction observer, not only key equality.

Preserve P000, source pins and genuine owner/CLAIM. The Stage476 author-side proof is durable in PR #1736; native task registration and Driver admission remain governed independently.
