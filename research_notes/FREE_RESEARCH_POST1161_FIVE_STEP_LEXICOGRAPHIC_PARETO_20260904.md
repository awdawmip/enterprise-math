# Post-#1161 free research — five-step lexicographic Pareto optimum for 256-bit completion

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / OUTER-STEP LOWER BOUND + GLOBAL INNER-DEPTH OPTIMUM / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessors:
- `research_notes/FREE_RESEARCH_POST1161_TWO_INDEX_WHOLE_TRAJECTORY_CERTIFICATE_20260904.md`
- `research_notes/FREE_RESEARCH_POST1161_ADAPTIVE_RETURN_DEPTH_RESOURCE_LAW_20260904.md`

## 0. Result

For the declared `256`-bit completion target, four outer AGM steps are mathematically insufficient even with exact inner return completion. Therefore the minimum outer step count is five.

At this minimum outer count, the rigorous `B=640` integer interval compiler yields exact global inner-depth optima.

For final bracket width

\[
\operatorname{width}<2^{-256},
\]

the unique certified optimum depth sum is

\[
\boxed{80}
\]

with schedule

\[
\boxed{(50,18,8,3,1)}
\]

and total scalar `S4` predictive-state cost

\[
\boxed{1980}.}
\]

For the stronger requirement that both final endpoints lie in one common `256`-bit dyadic cell, the optimum depth sum is

\[
\boxed{81}
\]

with schedule

\[
\boxed{(51,18,8,3,1)}
\]

and total state cost

\[
\boxed{2004}.}
\]

The result is lexicographic: first minimize the mathematically necessary number of outer AGM steps, then minimize total finite first-return predictive depth/state cost.

## 1. Exact completion-bracket width dominates shape defect

At an exact AGM state write

\[
L_n=\frac{V_n^2}{A_n}
=\frac{H_n^2(1-s_n^2)}{A_n},
\]

and

\[
U_n=\frac{H_n^2}{A_n-2\delta_n}.
\]

The #1161 completion theorem gives

\[
L_n\le\Pi_*\le U_n.
\]

Their difference is

\[
U_n-L_n
=H_n^2
\frac{A_ns_n^2+2\delta_n(1-s_n^2)}
{A_n(A_n-2\delta_n)}.
\]

Because

\[
0<A_n-2\delta_n<A_n\le1
\]

and `H_n>1`, one obtains the strict lower bound

\[
\boxed{U_n-L_n>s_n^2.}
\]

Thus no amount of arithmetic/inner-return refinement can make the declared finite completion bracket narrower than the exact shape defect permits.

## 2. Four outer steps cannot reach 256 bits

The standard initial shape is

\[
s_0=3-2\sqrt2.
\]

A purely rational comparison gives

\[
\boxed{s_0>\frac16}
\]

because

\[
17>12\sqrt2
\]

follows from `289>288`.

The exact shape recurrence satisfies

\[
s_{n+1}=\frac{s_n^2}{(1+r_n)^2}
\ge\frac{s_n^2}{4}.
\]

Writing `y_n=s_n/4` gives `y_{n+1}>=y_n^2`, hence

\[
\boxed{
s_n>4\left(\frac1{24}\right)^{2^n}.}
\]

At `n=4`,

\[
s_4^2>rac{16}{24^{32}}.
\]

Since `24<32=2^5`,

\[
24^{32}<2^{160},
\]

so

\[
\boxed{
s_4^2>2^{-156}.}
\]

Therefore

\[
\boxed{
U_4-L_4>2^{-156}>2^{-256}.}
\]

Four outer steps cannot produce a `256`-bit-width completion bracket, even with exact inner first-return completion and arbitrarily fine scalar arithmetic.

A common `256`-bit dyadic cell is also impossible, since two numbers in one such cell necessarily differ by less than `2^{-256}`.

Hence

\[
\boxed{\text{minimum outer AGM steps for the declared target}=5.}
\]

## 3. Five-step optimization problem

Fix

- `B=640` dyadic arithmetic bits;
- exactly five outer AGM steps, now proved minimal;
- inner return depths `N_i>=1`;
- state cost per step
  \[
  C(N_i)=24N_i+12,
  \]
  inherited from the `S4` graded predictive tower;
- the exact outward interval compiler from the preceding result.

Because increasing a return depth refines the positive first-return mass enclosure and all subsequent interval operations are inclusion-monotone, final certified precision is monotone nondecreasing in each `N_i`.

This permits lower-bound certificates without enumerating every schedule.

## 4. Global optimum for bracket width

Assume for contradiction that a five-step schedule with total return depth

\[
\sum_iN_i\le79
\]

achieves width `<2^{-256}`.

Then every individual depth is at most `79`. To obtain the most favorable possible test for coordinate `i`, set the other four depths to `79` and find the least value of `N_i` that can still meet the target.

The exact interval oracle gives the coordinatewise necessary lower bounds

\[
\boxed{(50,18,7,3,1).}
\]

Their sum is exactly `79`. Thus the **only** schedule that could possibly work at total depth `79` is the boundary tuple itself.

But its final certified pair is

\[
(\text{common-cell bits},\text{width exponent})=(255,255),
\]

so it fails the width target.

Hence every feasible schedule has

\[
\sum_iN_i\ge80.
\]

The schedule

\[
\boxed{(50,18,8,3,1)}
\]

has sum `80` and produces

\[
(255,257),
\]

so the bracket width is strictly below `2^{-257}` and in particular below `2^{-256}`.

Therefore

\[
\boxed{
\min\sum_iN_i=80
}
\]

for the five-step width target.

The total scalar predictive-state cost is

\[
\sum_i(24N_i+12)
=24\cdot80+12\cdot5
=\boxed{1980}.
\]

## 5. Global optimum for a common 256-bit dyadic cell

Now impose the stronger requirement that the two final rational endpoints lie in the same `256`-bit half-open dyadic cell.

Assume total depth at most `80`. Maximizing every other coordinate to `80`, the exact oracle gives necessary coordinate lower bounds

\[
\boxed{(51,18,8,3,1).}
\]

Their sum is already

\[
81>80.
\]

Therefore no five-step schedule of depth sum at most `80` can meet the common-cell target.

The boundary schedule

\[
\boxed{(51,18,8,3,1)}
\]

has sum `81` and gives

\[
(\text{common-cell bits},\text{width exponent})=(261,262).
\]

Thus

\[
\boxed{
\min\sum_iN_i=81
}
\]

and total state cost is

\[
24\cdot81+60=\boxed{2004}.
\]

## 6. Comparison with the conservative whole-trajectory schedule

The earlier safe schedule

\[
(175,43,17,7,3,1)
\]

used six outer steps, return-depth sum `246`, and total state cost `5976`. It intentionally overachieved the target, ending with `544` common binary bits.

The five-step Pareto schedules show that for the declared `256`-bit target the large guard allocation is unnecessary.

For width certification, the lexicographic Pareto cost drops from `5976` to

\[
\boxed{1980},
\]

and for a common 256-bit cell to

\[
\boxed{2004}.
\]

The comparison is within the same scalar first-return state-cost model; it is not a hardware/runtime benchmark.

## 7. Executable certificate

Task-local checker:

`scripts/check_free_research_agm_five_step_lexicographic_pareto.py`

Commit:

`08c40046b99a692ccb32fcec2212b0bb1fb9c086`.

The checker verifies:

- the analytic rational inequality
  `16/24^32 > 2^-156 > 2^-256`;
- five-step width lower-bound tuple `(50,18,7,3,1)` under any hypothetical sum `<=79`;
- failure of that unique sum-79 boundary schedule;
- success of `(50,18,8,3,1)` at depth sum `80`;
- common-cell necessary tuple `(51,18,8,3,1)` under hypothetical sum `<=80`;
- success of that tuple at sum `81`.

The file was fetched from `main`, and the core interval-oracle assertions were independently replayed successfully.

## 8. Scope boundary

The optimization is exact for the declared lexicographic problem:

1. minimum outer AGM steps required by the #1161 finite completion bracket for a 256-bit target;
2. at that outer count, minimum total first-return depth/state cost under the `B=640` outward integer compiler.

It does **not** claim a universal minimum over all conceivable algorithms, alternative completion readouts, arithmetic radices, or hardware cost models.

The result is a finite resource theorem for the specific native-derived first-return reconstruction developed in this successor line.
