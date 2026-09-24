# BRC target-blind LCM dominance and exact monotone carrier reduction

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note consumes the finite LCM-atom quotient theorem and the strict shared-LCM capacity witness already present on Enterprise Math main. It does not reopen arbitrary-port search and does not change D24 ownership, Result/review status, Working Truth, Foundation, or LIFT/JT2. The new unit asks the next exact compression question: after global repair has been reduced to a finite LCM library, which atoms are genuinely distinguishable by the repair observer?

## 1. Observer and inherited exact atom law

Fix a target prime

`p == 13 (mod24)`.

Let

`Q_p={q<p : q prime, q==13 (mod24)}`.

For each `q in Q_p`, write

`ord_q(4)=2s_q`, `c_q=v_q(1+4^{s_q})`.

The inherited finite-LCM theorem supplies a finite library `L_p`. After the already-proved fresh-prime realization and exact target-p compensation, each atom `L` acts on an earlier row `q in Q_p` by

`a_q(L)=-c_q` if `s_q|L`,

and

`a_q(L)=v_q(L)` otherwise.

The observer in this note is exactly:

`EXACT_TARGET_P_NEUTRAL + EXACT_EARLIER_CLASS19_NEUTRAL + EARLIER_CLASS13_REPAIR_FEASIBILITY`.

The target-p coordinate is not discarded globally. It is quotiented only because the preceding theorem proved a target-only compensator which is invisible on every earlier tracked row. Denominator valuations on earlier rows remain active provenance and are not collapsed to Boolean support.

## 2. Target-blind canonical core

For any full LCM atom `L in L_p`, define its earlier cancellation support

`A^<(L)={q in Q_p : s_q|L}`

and define

`E_p(L)=lcm{s_q : q in A^<(L)}`,

with `E_p(L)=1` when `A^<(L)` is empty.

### Theorem 2.1 — safe target-blind quotient

For every `L in L_p`:

1. `E_p(L)|L`;
2. `E_p(L)` is class-19-neutral below p;
3. `A^<(E_p(L))=A^<(L)`;
4. on every earlier class-13 row,

   `a_q(E_p(L)) <= a_q(L)`.

Proof.

Every generator in the definition of `E_p(L)` divides L, so `E_p(L)|L`. Any forbidden earlier class-19 divisor of `E_p(L)` would therefore divide L, contradicting admissibility of L. If `s_q|E_p(L)`, then `s_q|L`, giving the reverse inclusion of earlier cancellation supports; the forward inclusion is by construction.

On a cancelled row both signatures are exactly `-c_q`. On an uncancelled row neither core contains `s_q`, and divisibility gives

`v_q(E_p(L)) <= v_q(L)`.

Thus the replacement weakly improves every earlier-row repair coordinate while preserving exact class-19 neutrality. Any target-p cancellation/denominator difference introduced by deleting target-only structure is repaired by the already-proved target-only p compensator, which is invisible on the observer's earlier rows. Therefore replacing every full atom by its nontrivial `E_p` core preserves exact repair feasibility for this declared observer.

Let

`L_p^<={E_p(L): L in L_p, E_p(L)>1}`.

This is the target-blind fixed-point library.

### Corollary 2.2 — support uniqueness after canonicalization

If `L,M in L_p^<` and

`A^<(L)=A^<(M)`,

then `L=M`.

Indeed both are the lcm of the same set of `s_q`. Therefore, after target-blind canonicalization, the previously tempting category “same cancellation support but different denominator vector” disappears. Any remaining redundancy must compare different supports or use several atoms jointly.

This is a BRC safe quotient: the target-only coordinate is removed only after an explicit repair coordinate has been proved; earlier denominator valuations and shared LCM provenance remain.

## 3. Exact pairwise dominance criterion

For atoms `L,M in L_p^<`, say that M dominates L for the repair observer when

`a(M) <= a(L)`

coordinatewise on `Q_p`. One copy of M can then replace one copy of L in every residual state without worsening any constraint.

### Theorem 3.1 — pairwise dominance iff support extension has no outside denominator cost

For `L,M in L_p^<`,

`a(M) <= a(L)`

if and only if both conditions hold:

1. `A^<(L) subseteq A^<(M)`;
2. for every `q notin A^<(M)`,

   `v_q(M)=v_q(L)`.

Proof.

Assume `a(M)<=a(L)`. If `q in A^<(L)`, then `a_q(L)=-c_q<0`. An uncancelled M has `a_q(M)=v_q(M)>=0`, impossible. Hence every row cancelled by L is also cancelled by M, proving support inclusion.

Because both atoms are target-blind fixed points, support inclusion implies

`L=lcm_{q in A^<(L)} s_q` divides `M=lcm_{q in A^<(M)} s_q`.

For `q notin A^<(M)`, both rows are uncancelled, so

`v_q(M)=a_q(M)<=a_q(L)=v_q(L)`.

Divisibility `L|M` gives the reverse inequality, hence equality.

Conversely, on every row in `A^<(L)` both atoms give `-c_q`; on a newly cancelled row of M, M gives `-c_q` while L gives a nonnegative denominator valuation; outside `A^<(M)` the assumed valuations are equal. Thus `a(M)<=a(L)` coordinatewise.

So a support extension is a free dominance extension exactly when all new tracked denominator exponents occur on rows which the extension itself turns into cancellation rows. Boolean support alone is not sufficient; the equality condition is the retained integer provenance.

The pairwise-undominated atoms form a finite antichain which is sufficient under one-for-one replacement. It need not be the smallest exact integer carrier.

## 4. Exact monotone-semigroup redundancy

Let `B subseteq L_p^<`. The actual global repair problem allows arbitrary nonnegative integer atom counts, so the correct notion of complete compression is not merely pairwise dominance.

### Theorem 4.1 — universal repair preservation criterion

The sublibrary B preserves repair feasibility for every integer residual vector `b in Z^{Q_p}` if and only if, for every omitted atom `L in L_p^<\B`, there are nonnegative integers `x_M`, `M in B`, such that

`sum_{M in B} x_M a(M) <= a(L)`

coordinatewise.

Proof, sufficiency.

Take any feasible solution in the full library. Replace every copy of each omitted L by the corresponding B-combination. The replacement signature is coordinatewise no larger, so every inequality

`b + total_signature <= 0`

remains valid. Iterating over the finitely many omitted atoms yields a B-only feasible solution.

Proof, necessity.

Fix an omitted L and choose the residual state

`b=-a(L)`.

The full library is feasible using one copy of L, with final residual exactly zero. If B preserves feasibility for every residual, some nonnegative B-combination must satisfy

`-a(L)+sum_M x_M a(M) <= 0`,

which is exactly the displayed criterion.

Thus the smallest exact carrier is a monotone integer-semigroup domination problem. It should not be called a Hilbert basis without separately specifying the signed cone, order cone/slack variables, and the intended notion of minimality. Pairwise antichain reduction and semigroup reduction are distinct operations.

## 5. Exact p=397 separation

The paired checker reconstructs the finite library from multiplicative orders and the exact class-19 forbidden-divisor condition at

`p=397`.

It finds:

- full compensated LCM library: `23` nontrivial atoms;
- target-blind fixed-point library `L_397^<`: `19` atoms;
- pairwise-undominated atoms:

  `{23, 299, 175305}`.

Their nonzero earlier-row signatures are exactly

`a(23)={277:-1}`,

`a(299)={13:+1,157:-1,277:-1}`,

`a(175305)={13:-1,61:-1,157:-1,349:-1,373:-1}`.

Two exact semigroup inequalities then hold:

`a(23)+a(175305) <= a(299)`,

and

`a(299)+a(175305) <= a(23)`.

Therefore the three-element pairwise antichain is not semigroup-minimal. Either

`{23,175305}`

or

`{299,175305}`

preserves every one of the 19 target-blind atom effects, hence every residual repair feasibility decision under this observer.

No singleton can do so. Any positive multiple of a singleton capable of simulating `a(23)` must cancel row 277. Any positive multiple capable of simulating `a(175305)` must cancel rows 13, 61, 157, 349 and 373. Multiplicity cannot create a missing cancellation support coordinate, so a one-atom universal carrier would require cancellation support containing

`{13,61,157,277,349,373}`.

The exact finite target-blind library contains no such atom. Hence the minimum carrier cardinality at p=397 is exactly two.

This minimum is not unique. Therefore the observer itself does not select a unique “canonical minimum basis”. Choosing between the two exact size-two carriers would require an additional declared observer or cost, for example physical-port complexity, bit size, auxiliary-prime cost, or a provenance preference. Adding such a tie-breaker without declaring it would be information injection, not mathematical simplification.

## 6. BRC interpretation

The compression chain now has three proved levels:

`arbitrary physical ports`

` -> full finite LCM cores`

` -> target-blind fixed-point cores`

` -> pairwise dominance antichain`

` -> exact monotone-semigroup carrier`.

Each arrow has a different information contract.

The first quotient preserves shared cancellation support and denominator vectors. The second removes only target-only structure after exact compensation has been proved. The third is a one-copy monotone replacement order. The fourth allows integer combinations and is strictly stronger, as p=397 demonstrates.

The strict shared-LCM witness from the preceding unit and the present p=397 semigroup witness point in the same direction: the scientifically relevant object is a provenance-carrying hyperedge/semigroup, not a list of independent scalar repairs. Premature decomposition can duplicate dirty cost; premature selection of a single pairwise antichain can retain atoms which are jointly redundant.

## 7. Exact checker

Paired checker:

`research_checks/check_brc_target_blind_lcm_dominance_20260924.py`.

It uses exact integer arithmetic to reconstruct:

- class-13 multiplicative orders and cancellation steps;
- the 23 full LCM atoms at p=397;
- all 19 target-blind fixed points;
- target-blind quotient support and coordinatewise domination;
- all `19^2=361` ordered pairwise dominance comparisons and Theorem 3.1's criterion;
- the exact three-element pairwise antichain;
- the two semigroup redundancy inequalities;
- both exact size-two universal carriers;
- impossibility of a singleton carrier from the required cancellation-support union.

The checker reports zero failures. It is a finite certificate for the p=397 example; Theorems 2.1, 3.1 and 4.1 are structural proofs and do not depend on this finite computation.

## 8. Do not repeat / next

Do not again search arbitrary physical ports for this observer; the finite LCM theorem already removed that infinity.

Do not retain target-p-only LCM structure inside the earlier-row carrier after target-only compensation has been invoked; use `E_p`.

Do not equate pairwise undominated with semigroup-minimal. The p=397 certificate is a strict counterexample.

Do not name a unique canonical minimum carrier when several minimum carriers exist under the same observer.

If formal D24 control remains blocked, the next nonredundant auxiliary unit is to characterize the monotone-semigroup carrier uniformly in p: derive structural incompatibility/cover relations among cancellation supports and determine whether minimum carrier size or a canonical cost-refined carrier admits an arithmetic bound without enumerating all subsets. If a canonical lossless old-session -> successor-session rollover becomes live, stop this auxiliary line and return immediately to the Source-native D24 continuation path.
