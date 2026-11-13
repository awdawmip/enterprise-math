# Frozen R5: full nesting-phase classification survives each of 28 gap closings

Date: 2026-11-14. Author-side mathematical corollary. Scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Scope: R=2, integer event-boundary coordinates, candidate centers chosen from the coordinates. This note uses the exact single-cut optimum spectra in `R5_28_CUT_SPECTRUM.md` and previously certified 741-step optimal nesting classification / minimum edit distances in immutable PR #2335 at `48d57e95ff64cb3f69361dd85d26e9dda0d9445e`.

## Theorem

Independently close **any one** of the 28 original gaps of length three to length two (shift the suffix by one integer unit). Label the resulting instance `Y_c`; `c` is its zero-based cut index, 0..27. Define `Opt_c(K)` as the radius-two optimal center-index sets at budget K, and

`rho_c(K) := min{|S\\T|: S in Opt_c(K), T in Opt_c(K+1)}`,

where `S\\T` means the old centers removed. Then the *exact nesting classification* on all 741 originally feasible consecutive budgets is invariant:

- For every cut c, **`rho_c(K)>0` exactly for `K=213,...,291`** (79 nonnested transitions).
- For every cut c, **`rho_c(K)=0` exactly for `K=292,...,953`** (662 transitions admitting nested optimal sets).
- Five cuts c in {5,6,8,9,16} create a new minimum feasible budget K=212. For each of these five, the additional transition **`212→213` is also necessarily nonnested**.

Furthermore the *exact* edit distances survive unchanged for the 732 transitions `K=222,...,953`:

`rho_c(K)=1` for `222<=K<=291`; `rho_c(K)=0` for `292<=K<=953`.

For `214<=K<=221`, the saved optimum witnesses imply `1<=rho_c(K)<=2`; determining which cuts may reduce 2 to 1 is open. For `K=213`, the present theorem proves nonnesting but does not yet give every cut's exact minimum positive removal count.

## Proof

**Optimal-set persistence lemma.** The general gap bridge theorem in `RESEARCH.md` shows that every originally radius-two-feasible center set S remains feasible after one gap closes **with its exact cost unchanged**. Therefore, at any budget K whose *optimal cost* also stays unchanged, every old optimal S remains a new optimal solution. This statement applies simultaneously to pairs (K,K+1) whenever both old optimal costs persist.

**High-budget nesting.** The exact 28-cut spectrum shows `J_c(K)=J_X(K)` for every cut and **all K>=214**. The previous immutable R5 proof gives a nested optimal pair `S⊂T` for each K=292,...,953. By the persistence lemma both sets remain optimal on Y_c; hence `rho_c(K)=0`.

**Nonnesting below 292.** The sharp radius-two integer-coordinate single-center insertion bound from the earlier R5 research is: adding any one center to a feasible set can lower its nearest-center total cost by at most **three**. For K=214,...,221 the exact postclosure marginal improvement is 5, and for K=222,...,291 it is 4, because both costs stay unchanged. For K=213 the marginal improvement is 6 on 26 cuts and 5 on cuts 8 and 9, because only those two reduce the K=213 optimum from 1070 to 1069; the K=214 optimum remains1064. Every such marginal is greater than three, which rules out a nested pair of optimal center sets. Hence all 79 transitions still have `rho_c(K)>0`.

**Exact edit distances for K>=222.** For K=222,...,291, earlier optimal pairs had exactly one old-center deletion. Their two costs are unchanged on each closure, so the same pair remains optimal and achieves `rho_c(K)<=1`; preceding nonnesting proves the reverse bound. For K>=292 exact zero was already established. For K=214,...,221, old exact-two-removal witnesses remain optimal and yield upper bound two, while nonnesting yields lower bound one.

**Five newly feasible transitions.** The new `K=212` optimum costs for cuts {5,6,8,9,16} are respectively {1077,1077,1075,1075,1076}. Corresponding `K=213` optima are {1070,1070,1069,1069,1070}. The extra transitions have marginal gains {7,7,6,6,6}, each exceeding the maximum single-center insertion improvement three. They therefore require reconfiguration. QED.

## Consequences and next question

Among **28×741=20,748** previously feasible adjacent-budget transition instances, exactly **28×79=2,212** are necessarily nonnested and **28×662=18,536** admit a nested optimum pair, despite the unit change in coordinate spacing and the two K=213 optimum cost reductions. The extra five newly feasible K=212→213 transitions add five nonnested cases.

This determines *all nesting yes/no answers* without an additional optimal-path-product run. The next exact computation should focus on the narrower unresolved `rho_c(K)` values for K=213..221 and the five K=212→213 cases, then on their compact center-set witnesses. The native full-chain seed/28-coordinate/8192-query benchmark remains an independent objective.
