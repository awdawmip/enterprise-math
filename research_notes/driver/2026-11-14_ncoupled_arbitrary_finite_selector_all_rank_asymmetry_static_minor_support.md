# N-coupled: arbitrary finite leaf selection cannot escape static minor support

Status: **new Driver auxiliary exact theorem, not a frozen Result, independent review, native acceptance, or parent closure**  
Date: 2026-11-14 (Asia/Shanghai)  
Research context: RR-13ED25CE1AA8899BCFEC / TP2-7D97568CBD5F6DE776A3; same Driver EM-DVR-DEBB5E.  
Original source authors: EM-NCAS1-5F7A3C (frozen `G_poly-loc` theorem), EM-NCASR2-C9BCF9 (integrity re-freeze). This note is a subsequent auxiliary mathematical deduction, not a reassignment of either author's work.

## Statement: finite-leaf selector, arbitrary tests, *all* unequal ranks

Fix once and for all a finite set of leaves `L`. At each leaf `l`, a finite set of output matrix flattenings `M_{l,j}(N)` is given with entries in the localization `Z[D^{-1}][N]`, where `D` is a *fixed finite* set of nonzero integers. All denominators are required to be units modulo the admitted semiprime `N=pq`, where `p,q` are distinct primes (the project's odd-prime scope is included). The matrix dimensions and symbolic coefficients are fixed across inputs.

**Allow an otherwise arbitrary rule** `sigma(N)` selecting one leaf `l in L` for each public `N`; its tests need not be polynomial, zero/unit, computable, or even factor-blind. The sole semantic requirement is that the rule chooses **one global leaf**, and the output of that leaf remains the displayed fixed ring-term matrix evaluated at `N`. The selector must not inject freshly computed, input-dependent numerical values into those output matrix expressions. The rule may select different leaves at different `N`, but does not choose separate hidden CRT leaves for `p` and `q`.

For each fixed `l,j`, clear all fixed admissible denominators by a common nonzero integer `d_{l,j}`, and define the fixed integer matrix
`
B_{l,j} := [d_{l,j} M_{l,j}(0)] \in Mat_{m_j \times n_j}(Z).
`
Let `k_{l,j}=rank_Q(B_{l,j})`. For every `1<=t<=k_{l,j}`, define the strictly positive `t`-th determinantal divisor
`
Delta_t(B_{l,j}) := gcd( |det B_{l,j}[I,J]| : |I|=|J|=t).
`
There is a **finite, completely precomputable list of ordinary positive integers**
`
C={ Delta_t(B_{l,j}) : l in L, j, 1<=t<=k_{l,j} }.
`
For any admitted `N=pq`, if some selected output matrix has **unequal ranks in the hidden channels**
`
rank_{F_p}(M_{sigma(N),j}(N)) != rank_{F_q}(M_{sigma(N),j}(N)),
`
then some `c in C` satisfies
`
1 < gcd(N,c) < N.
`
In particular the complete list of one-time static `gcd(N,c)` tests contains a proper factor on every input where this finite-leaf system creates *any* rank asymmetry. This is an implication, not a claim that the selector actually performed the gcd, or that every successful gcd implies rank asymmetry.

There is also a finite set `S` of primes (those dividing at least one member of `C`, together with the fixed denominators) such that for all admissible `p,q not in S`, **no leaf and no output** can have unequal hidden-channel ranks. The choice of `sigma` is immaterial to this uniform conclusion.

## Proof

Fix a leaf `l` and output `j`. By polynomial specialization, `M_{l,j}(N)\equiv M_{l,j}(0)\pmod{N}` entrywise: if a denominator is a unit, `P(N)/d\equiv P(0)/d\pmod{N}`. Multiplying by the unit `d_{l,j}` does not change prime-channel ranks. Therefore both hidden-channel outputs are reductions of the same **fixed** integer matrix `B=B_{l,j}`.

For each `t\le k=rank_Q(B)`, at least one `t\times t` minor is a nonzero integer, so `Delta_t(B)>0`. The elementary minor criterion gives, for any prime `r`,
`
rank_{F_r}(B\bmod r)<t \iff r\mid Delta_t(B).
`
Now suppose the ranks at `p,q` are `a<b`. Take `t=b`, which satisfies `1\le t\le k`. The inequality `a<t\le b` means `p\mid Delta_t(B)` but `q\nmid Delta_t(B)`. Hence `gcd(pq,Delta_t(B))=p`, a proper factor. The case `b<a` is symmetric. The selected leaf belongs to the *pre-fixed* finite list, so its witness integer is in `C`, however the leaf was selected. If both ranks are equal, the implication asserts nothing.

Every prime outside `S` divides no nonzero `Delta_t(B)` and no excluded fixed denominator, so for each leaf and output its reduction at that prime has all minor-based generic ranks, in fact exactly `k`. In particular ranks at `p,q notin S` agree at every leaf. This is uniform in every possible selector and proves the theorem.

No finite exhaustive computation is needed: the statement follows from the exact polynomial/CRT specialization and the complete family of determinantal divisors.

## Why all ranks, not just generic one-sided loss, matters

A single *top* determinantal divisor witnesses the narrower condition that rank falls below `k` on exactly one channel. It need not witness **unequal ranks when both channels fall below `k`**.

For example let `B=diag(3,15)`, `N=15=3\cdot5`. Then `k=2`, but
`
rank_{F_3}(B)=0,  \qquad rank_{F_5}(B)=1.
`
The top divisor is `Delta_2=45`, hence `gcd(15,45)=15` is not a proper factor. The first divisor is `Delta_1=gcd(3,15)=3`; `gcd(15,3)=3` gives the correct witness. Thus the *full determinantal-divisor sequence*, not just its top member, is needed for this stronger rank-asymmetry theorem.

## Relation to earlier saved science and open frontier

The preceding Driver auxiliary theorem [finite Boolean feedback / static top-minor support](research_notes/driver/2026-11-14_ncoupled_finite_branching_static_support_theorem.md) also proves that under fixed zero/unit/minor branch tests the selected leaf becomes independent of `N` away from finite support. **That eventual leaf-constancy statement is NOT asserted here.** In exchange this theorem permits arbitrary finite leaf selection, even by tests beyond the frozen grammar, and detects *all* rank differences, not only generic-rank one-sided loss.

Finite selection alone cannot create infinitely many novel prime supports if every leaf's numerical output remains a fixed ring term. It remains possible that an input-dependent numeric register, unboundedly many leaves, variable-time evolution, canonical representative output fed back as new numerical state, or a genuinely non-product-natural typed operation escapes this lemma. This result does not classify such mechanisms, give a general factoring lower bound, or rule out the mother objective `CRT_PRODUCT_NATURALITY_BREAK_WITHOUT_SCALAR_SUPPORT_EXPOSURE`.

Original Result authors and immutable reviews stay separate from this Driver auxiliary proof. No new CLAIM, native Result acceptance, task completion or Foundation permission is inferred.
