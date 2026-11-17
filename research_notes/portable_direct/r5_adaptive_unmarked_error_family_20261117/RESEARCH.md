# R5 — General adaptive error-count upper bound and 0..20 sharp exact family

Date: 2026-11-17 (Asia/Shanghai). Frozen mathematical input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Scope: frozen 256-mask, 954-event **derived scalar integer observer**, k=214..314. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## New two-part theorem

With `f` arbitrary unmarked corrupted real readings, no marked erasures, normal absolute error bound `eta>=0`, every query budget `k` costing `k`, and

```
0 <= 2 eta < delta = 76289178155959966960189440,
```

the adaptive worst-case total budget `C_f` satisfies:

1. **All-integer constructive result.** For every integer `f>=0`, `C_f <= 731+945*f`.
2. **Sharp finite family.** For *every integer* `0<=f<=20`, the exact value is `C_f=731+945*f`, verified by a complete 4-state finite adversarial Bellman certificate.

The universal equality `C_f=731+945*f` for all `f>20` is a conjectural extension supported by additional limited instances, not a claimed universal theorem in this record. The earlier independently proved `f=1` and `f=2` exact results agree with this family.

For comparison, the previously established fixed-query optimum in the same noise chamber is `731(2f+1)`. Thus the exact adaptive savings for `f<=20` equal `517f`, and the constructive all-f scheme saves at least `517f` relative to the fixed scheme (though an even cheaper adaptive scheme for f>20 is not ruled out).

## All-f upper proof: confidence-threshold adaptive sampler

Choose budgets **294,223,214** in that order. Read each noisy real response through the unique exact scalar count center whose `eta`-interval contains it, or an out-of-alphabet symbol. Distinct exact centers at each of these budgets have gap at least `delta`.

Let `r` be the conservative number of unmarked errors remaining, initially `r=f`. At a budget `k`, repeatedly query until some symbol has occurred **`r+1` times**. As at most `r` nontrue symbols can have occurred, the identified repeated symbol must be the true count. If `t` other symbols were observed, then at least `t` of the error allowance was spent. Continue to the next budget with allowance `r-t`. This procedure takes exactly `r+1+t` readings at that budget and at most `2r+1`. All three recovered true counts determine the mask uniquely.

Let `F(i,r)` be the maximum future cost of this explicit strategy from budget-position `i` with allowance `r`; `k_1=294,k_2=223,k_3=214`. Its finite recurrence is:

```
F(i,r) = max_{0<=t<=r} ((r+1+t)*k_i + F(i+1,r-t)),
F(4,r)=0.
```

Put `S_i=sum_{j>=i} k_j`, and `m=k_3=214`. By backward induction,

```
F(i,r) = S_i + r*(S_i+m).
```

For `i=3` this is `(2r+1)*214`. For the earlier budgets, insert the inductive hypothesis: each candidate expression differs from `S_i+r(S_i+m)` by `t*(k_i-S_{i+1}-m)`. Both coefficients are nonpositive:

```
k_2=223 <= S_3+m = 428,
k_1=294 <= S_2+m = 223+214+214 = 651.
```

Hence the maximum is always attained at `t=0`, and

```
F(1,f) = (294+223+214) + f*(294+223+214+214)
       = 731+945*f.
```

All-f correctness and the upper bound follow, including f=0.

## Exact finite lower proof for f=0..20

The earlier frozen 101-budget table supplies the precise supports of three states relative to base mask 16:

| state | all budgets with a count different from mask 16 | least query budget |
|---|---|---:|
| 17 | 214..221 | 214 |
| 80 | 223..291 | 223 |
| 32 | 294..313 | 294 |

The windows are disjoint. Restrict the 256-state problem to `H={16,17,80,32}`, choose zero normal noise, and permit an adversary to answer using the two genuine scalar count values for any tested window or a third arbitrary value. A query outside the three windows provides no information; each query in one window implements one binary test for its unique alternative and costs at least the minimal window budget `(214,223,294)`.

For any fixed integer `f`, define a mismatch vector `d=(d_0,d_1,d_2,d_3)` capped at `f+1`. Candidate `h` remains feasible iff `d_h<=f`. For test `j=1,2,3` and answer `a in {0,1,2}`, update

```
T_j(d,a)_h = min(f+1, d_h + 1[a != 1[h==j]]).
```

Let `V_f(d)=0` when at most one hypothesis survives. At all other states define the exact minimax recurrence

```
V_f(d) = min_{j productive}
  (c_j + max_{a: some candidate survives T_j(d,a)} V_f(T_j(d,a))),
c=(214,223,294).
```

An action allowing a self-loop on some admissible adversarial response is nonproductive for guaranteed finite termination; it can be discarded. Every productive transition strictly increases a capped discrepancy counter. The recursion is acyclic, over a finite subset of `{0,...,f+1}^4`.

The standard-library exact-integer verifier `VERIFY_R5_ADAPTIVE_FAULT_FAMILY_F0_TO_F20.py` was **executed with `-- f_max=20` (command `python ...py 20`)** and checked all `f=0,...,20`. It returned `PASS_R5_ADAPTIVE_UNMARKED_ERROR_FINITE_F0_TO_F20`, and for each f found

```
V_f((0,0,0,0)) = 731+945*f.
```

The complete computed series and state counts are preserved in `RESULTS_FAMILY_FINITE.json`. For `f=20`: value **19631**, 156331 memoized states. This Bellman recurrence exhausts all productive actions and all distinguishable adversarial output classes for the finite restricted population. Because every full-scale adaptive strategy must handle these four states, `C_f >= V_f(0,0,0,0)`. This lower bound matches the constructive upper for the stated **21 integer instances**.

The finite certificate checks a real scalar observer under the preserved frozen count map, not a native signed-path/BRC/X6 factorization. The exact source witness windows were reverified in the preceding `r5_sharp_adaptive_two_unmarked_errors_20261117` result; that witness and the same input pin are prerequisites for this finite-family specialization.

## Next frontiers

- Find a structural, non-enumerative lower proof for **all** `f>=0`, or find the first `f>20` for which adaptation beats the linear upper.
- Rework the exact adaptive policy when `2eta >= delta`, where the three-budget count-center quantizer loses its guarantee.
- Revisit the R5 optimizer `max-new/min-old` recourse and study full source/signed-path-preserving joint BRC observation bridges.

Researcher origin: `EM-DIRECT-C52C70`; Activity `RA-E56F584D739D86CC48916236`; formal R5 CLAIM not asserted. Mathematical review: NOT_REVIEWED.
