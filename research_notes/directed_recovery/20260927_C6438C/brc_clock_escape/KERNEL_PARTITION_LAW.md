# Split kernel labels as a factor observer

Status: PURE_SYMBOLIC / CONDITIONAL_INTERFACE / NOT_EXECUTED / NOT_ADMITTED.
Root derivation, shared research context EM-DIRECT-C6438C.

This extends the concrete two-torsion translated-mark proposal to a finite, explicitly split geometric kernel. The purpose is to retain the label information that a saturated return to the entire kernel erases. It does not provide the exponent that reaches that kernel.

## 1. Declared geometric and BRC scope

Let R=Z/nZ with n odd. Let G and G' be smooth commutative group schemes over R, and let phi:G->G' be an isogeny with finite etale kernel K. Assume, as an actual certificate obligation, that K is a disjoint union of s explicitly given R-valued sections T_1,...,T_s. They must remain distinct in every residue characteristic dividing n. This is stronger than merely knowing that K has s geometric points over an algebraic closure. A split torus or elliptic subgroup is an applicable carrier when the hypotheses hold.

Let Q be a certified R-point. Let I_i be the pullback along Q of the ideal of T_i in G, and J the pullback along phi(Q) of the identity ideal in G'. For any ideal I in R, define its positive integer divisor representative g(I)|n by I=(g(I)) in R. Thus the zero ideal has g=n and the unit ideal has g=1. Actual algorithms must construct the ideals/sections through admitted coordinates and operations; this notation does not supply an oracle.

BRC use is observer-scoped retention of finite geometric fiber labels and their joint divisor witnesses. Collapsing all T_i into one return label is a coarser observer. It is not automatically faithful for factor extraction. This is a theorem-level composition of the existing finite-fiber/retained-provenance discipline, not a new top-level family or a runtime execution claim.

## 2. Exact partition law, including prime powers

Because the scheme-theoretic identity fiber of phi is exactly the disjoint union of T_i, its ideal is the product of the pairwise comaximal section ideals. Pullback along Q gives

`J = product_i I_i`, with `I_i + I_j = R` for distinct i,j.

Writing `g_i=g(I_i)` and `g_phi=g(J)`, this implies

`gcd(g_i,g_j)=1`, and `g_phi=product_i g_i`.

To check the integer formula, localize R at each prime-power component r^a. At most one section ideal can be nonunit; hence at most one g_i has positive r valuation. The product's valuation is that one capped valuation, so it never exceeds a. This proves exact depth, not only squarefree support.

If phi(Q)=O over R, then g_phi=n. Each prime-power component belongs completely to exactly one label. The list of nontrivial g_i therefore partitions n into pairwise coprime full prime-power blocks. If more than one g_i is greater than one, every such g_i is a proper factor. If exactly one equals n, all components occupy the same label and this observer returns no proper factor.

This is a lawful **same global kernel label or factor** alternative. It does not say that a kernel return always factors n, that the labels are cheap to acquire, or that an unsplit kernel is secretly already split over R.

## 3. Conditional probability is separate from reaching the kernel

For n=pq with distinct primes, suppose a declared sampling process, conditional on phi(Q)=O, induces independent label laws alpha_i over p and beta_i over q. Then the probability that label extraction gives a proper factor is exactly

`1 - sum_i alpha_i beta_i`.

For uniform independent laws on all s labels it is `1-1/s`. This follows by counting the same-label event; it is not an unconditional success rate and no such sampler is constructed here. If the process has a shared/global label by construction, the rate is zero. Retaining the original joint law instead gives `1-sum_i Pr(L_p=i,L_q=i)` without assuming independence.

The full cost and probability of obtaining Q in the kernel come first. Multiplying an unknown point by a smooth clock still requires its odd order part to divide that clock. A good conditional label split cannot be substituted for a proof of this reachability event.

## 4. Geometric implementation targets and exact limits

For the existing Montgomery two-torsion translation, the subgroup {O,T} with T=(0,0) is explicitly split when the curve is smooth and 2 is a unit. The proposed translated adjacent readout provides the two primitive g_i without square-depth ambiguity. This is a concrete short section formula, while the general statement here supplies no universal cheap coordinate formula for arbitrary s.

A full rational two-torsion subgroup, when actually certified, can distinguish different nonidentity labels even when the ordinary identity observer gives 1 and doubling gives n. In a ring with two distinct prime factors, CRT supplies such conditional witnesses by placing Q at different nonidentity sections in the two local components. This is an existence proof of a strictly richer observer on certified inputs, not a factor-blind way to generate those inputs.

If the split kernel sections are explicitly enumerated, s section evaluations and their primitive common-gcd readouts are a direct implementation bound. A balanced search over subsets only helps if the subset-union ideals have independently proved cheap representations; the product notation alone is not one. Division, coordinate admission, singular/denominator cases, unsuccessful labels and witness verification remain charged in any native execution.

The next concrete task is to prove and implement the small two-torsion section formula first, under the existing adjacent-pair geometry. A larger-kernel compiler must separately preserve exact ideals and bound its construction cost. The unresolved broad target is still a factor-blind mechanism that reaches useful kernel fibers with sufficient probability and lower total cost; this note does not close native Shor.

No numerical input, prime factor, coefficient, orbit or scientific trace was generated in this unit. Any authorized conversation may continue the symbolic interface and its cost proof.

Global-Knowledge-Sync: main@2450bbb / GLOBAL_KNOWLEDGE_V1
