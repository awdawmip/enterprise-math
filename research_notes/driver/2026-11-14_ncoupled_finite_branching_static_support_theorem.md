# N-coupled: finite Boolean feedback retains static determinantal support

Status: **driver auxiliary mathematical proof; NOT a new frozen Result or native review acceptance**  
Date: 2026-11-14 (Asia/Shanghai)  
Review context: original `RR-13ED25CE1AA8899BCFEC`, `TP2-7D97568CBD5F6DE776A3`, task `RS-N-COUPLED-ASYMMETRIC-SINGULARIZATION-PRIMITIVE`.  
Provenance: the frozen `G_poly-loc` no-go and its original author `EM-NCAS1-5F7A3C`; integrity re-freeze author `EM-NCASR2-C9BCF9`. This extension is a supplementary driver-context deduction, not a claim of independent review of those authors.

## Proposition (bounded branching extension)

Fix a **single finite decision tree** (finite depth, finitely many registers and output flattenings per leaf). Along every root-to-leaf path, initial registers are fixed integers/rational constants and the public integer parameter `N`; register updates use fixed ring terms, fixed matrices/tensor products/contractions and denominators from a **fixed finite integer set**, all units for the admitted moduli. Every branch predicate is a fixed Boolean formula of tests
`x=0 in Z/NZ` or `x is a unit of Z/NZ`, where `x` is a scalar register or a fixed minor/determinant of a register matrix. The tests are permitted to change the chosen path; they are *not* used as additional numerical inputs to ring operations. No unrelated `N`-dependent initial data, unbounded loop, factor oracle, representative/floor operation or variable-denominator inversion is allowed.

For every chosen leaf `l` and output matrix flattening `j`, clear its fixed denominators and let `B_lj` be the **integer matrix obtained by setting N=0 in that leaf's ring expressions**. Define `k_lj=rank_Q(B_lj)`; when `k_lj>0`, let `Delta_lj` be the positive gcd of its nonzero `k_lj`-minors (top nonzero determinantal divisor). All these matrices and integers are fixed, independent of the semiprime input.

There is one **finite set of primes S** depending only on the entire syntactic tree such that, for all `N=pq` with *distinct* primes `p,q not in S` and admissible fixed denominators:

1. Every branch test has a fixed truth value independent of `p,q`; hence the program follows one fixed leaf.
2. Every output matrix has its generic rational rank on **both** prime channels, so no one-sided rank singularization occurs.

More strongly, for **any** admitted distinct-prime semiprime `N=pq`, including inputs containing primes of `S`, a one-sided output rank loss implies that **one of the finitely many precomputable leaf constants** satisfies
`
1 < gcd(N, Delta_lj) < N.
`
Thus a fixed finite list of ordinary scalar gcds already detects every successful one-sided rank-loss input for the entire finite-branch program (possibly also other inputs). There is no claim that the program itself computed these gcds or chose the same leaf as the gcd scan.

## Proof

**Step 1: symbolic path specialization.** Freeze any syntactic path, whether or not reachable for a particular `N`. Before applying its Boolean tests, structural induction on fixed ring operations expresses each register entry/minor as `F(N)/d` with `F in Z[N]` and fixed denominator `d` a unit modulo all admitted `N`. Since `F(N)-F(0)` is divisible by `N`, the register entry equals `F(0)/d` in `Z/NZ`. The denominator may be cleared without changing zero/unit status or prime-channel rank.

**Step 2: finite test support.** For each syntactic test scalar `F(N)/d`, place into `S_test` all prime divisors of nonzero `F(0)`, as well as all primes dividing the fixed denominators. If `F(0)=0`, its value modulo `N` is always zero, hence nonunit; if `F(0) != 0` and `p,q not in S_test`, its value is a unit and is not zero. Therefore all primitive tests—and their Boolean formulas—have a constant outcome on such semiprimes. The finite tree follows one fixed leaf.

**Step 3: finite output rank support.** For every leaf and output `B_lj`, `k_lj=0` implies zero rank in every prime reduction. If `k_lj>0`, the standard minor criterion gives
`
rank_{F_r}(B_lj mod r) < k_lj  iff  r | Delta_lj.
`
Add the prime divisors of the finitely many nonzero `Delta_lj` to `S_test` to obtain `S`. For `p,q not in S`, all output prime-channel ranks equal their common generic rank `k_lj`. This proves (1)–(2).

**Step 4: static scalar certificate on the actual leaf.** For any admitted semiprime `pq`, choose the actual leaf `l`. If one selected output has rank drop on exactly one channel, the same minor criterion says one of `p,q` divides `Delta_lj` and the other does not. Consequently `gcd(pq,Delta_lj)` is exactly that one prime. Because the tree has finitely many leaves and outputs, all `Delta_lj` can be enumerated without knowing the actual path. This proves the stronger implication.

The proof is symbolic for the whole declared finite tree. It does not infer a universal obstruction for arbitrary stateful/history-dependent, variable-time, representative-based, external-input or non-ring mechanisms.

## Scope and actionable consequence

This theorem **enlarges** the frozen `G_poly-loc` result from *no outcome-dependent branching* to **finite zero/unit/minor-test branching**. It does not revise the original frozen return or reassign its author's contribution. In this strictly specified class, adaptive Boolean control changes paths but does not create unbounded hidden-prime support: every successful one-sided rank-loss case is already witnessed by a fixed candidate gcd constant.

The still-open `CRT_PRODUCT_NATURALITY_BREAK_WITHOUT_SCALAR_SUPPORT_EXPOSURE` mechanism question should therefore target a genuinely different data source or operation (for example, input-dependent state, unbounded evolution, or typed history) and assess it on its own evidence. None of those alternatives is ruled out here.

## Evidence and review status

Proof: complete under the stated finite-tree/operand conditions, using elementary polynomial specialization and the top-minor rank criterion; no numerical enumeration is needed for the universal quantifiers. Existing pinned Result envelope `RR-13ED25CE1AA8899BCFEC` and its five manifest entries were individually checked against GitHub blob identities at `ff66e79c94a85457fbb51af37f47a2fb3c1c832c` during this driver-context inspection. Historical `ACCEPTED` review is quarantined for original authority mismatch, so this note conveys **no native Result acceptance, Task completion, CLAIM, or Objective closure**.
