# BRC finite LCM-atom quotient and exact global clean-repair budget

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note consumes the class-19 debt-poset absorption theorem and the clean-subcone dirty-capacity theorem. The preceding causal closure used one fresh suppressor atom per clean row and correctly stopped short of global optimality because one arbitrary port may lie on several class-13 cancellation progressions at once. The present unit closes exactly that shared-support gap: every admissible arbitrary port has a canonical finite LCM core, and global p-neutral / class-19-neutral repair is equivalent to a finite integer cone over those cores.

No D24 owner, Result, review, Working Truth, Foundation status, or LIFT/JT2 status is changed.

## 1. Parity simplification on the class-13 side

Fix a target prime

`p == 13 (mod24)`.

For every class-13 target `q<=p`, write

`ord_q(4)=2 s_q`

and

`c_q=v_q(1+4^{s_q})>=1`.

Because `q == 5 (mod8)`, `(2/q)=-1`. Since `v_2(q-1)=2`, the 2-part of `ord_q(2)` is exactly 4; hence

`ord_q(2)=4 s_q`

with `s_q` odd, and therefore `ord_q(4)=2s_q`.

Thus every q-cancellation port is

`j=s_q u`, `u odd`,

so every negative class-13 carrier is odd.

Also

`h_q=(q-1)/2`

is even for `q ==13 (mod24)`. Therefore an odd port can never be a class-13 endpoint. On any odd singleton port j the exact class-13 defect simplifies to

`delta_q(j) = -c_q` if `s_q|j`,

and otherwise

`delta_q(j)=v_q(j)>=0`.

The denominator valuation cancels inside the coefficient-cancellation event, exactly as in the previous net-valuation theorem.

This parity simplification is specific to the current observer and is not a global deletion of endpoint provenance: class-19 endpoints remain odd and remain active.

## 2. Class-19-neutral odd ports

For every earlier class-19 target `r<p`, put

`h_r=(r-1)/2`.

Class 19 has no negative coefficient-cancellation channel. Hence an odd singleton port j is exactly class-19-neutral below p iff

`r does not divide j`

and

`h_r does not divide j`

for every such r.

Call such j **19-neutral**.

If a whole added repair cloud is required to be class-19-neutral, every class-19 contribution is nonnegative, so exact neutrality forces every occupied negative-helpful port to be 19-neutral and forbids positive class-19 factorial residue. Repeated work can therefore be split onto distinct fresh ports without losing a negative class-19 mechanism, because none exists.

## 3. Canonical LCM core of an arbitrary repair port

Let j be any odd 19-neutral port. Define its class-13 cancellation support through the target by

`A_p(j)={q<=p : q==13 (mod24), s_q|j}`

and define

`L_p(j)=lcm {s_q : q in A_p(j)}`,

with `L_p(j)=1` when the support is empty.

### Theorem 3.1 — exact cancellation-support preservation

For every such j,

1. `L_p(j)|j`;
2. `A_p(L_p(j))=A_p(j)`;
3. `L_p(j)` is again 19-neutral.

Proof.

Every `s_q` in the defining set divides j, so their lcm divides j. If `s_q|L_p(j)`, then `s_q|j` because `L_p(j)|j`, giving the reverse inclusion of cancellation supports. Finally every class-19 forbidden divisor of `L_p(j)` would also divide j, contradicting 19-neutrality.

Thus no negative cancellation provenance is lost by replacing j with its LCM core.

### Theorem 3.2 — coordinatewise defect domination

For every class-13 target `q<=p`,

`delta_q(L_p(j)) <= delta_q(j)`.

Moreover equality holds on every cancelled row.

Proof.

If `s_q|j`, Theorem 3.1 gives `s_q|L_p(j)` and both defects are exactly `-c_q`.

If `s_q` does not divide j, it does not divide the core either. Both ports are odd, so no class-13 endpoint exists, and

`delta_q(L_p(j))=v_q(L_p(j)) <= v_q(j)=delta_q(j)`

because `L_p(j)|j`.

So arbitrary extra factors outside the cancellation-support lcm can only add nonnegative denominator residue. They never improve the repair observer.

## 4. Finite canonical atom library

A class-13 step `s_q` is 19-clean below p exactly when it is itself 19-neutral. By the proved debt-poset monotonicity, a 19-neutral port cannot be divisible by any dirty `s_q`.

Define the finite library

`L_p = { lcm(T) : T is a subset of {s_q : q<=p, q class13, s_q 19-clean}, lcm(T) is 19-neutral } \ {1}`,

with duplicate lcm values identified.

This library is finite, with the trivial bound

`|L_p| <= 2^(number of clean class-13 steps <=p)-1`.

It can be generated exactly by starting from `{1}` and repeatedly adjoining

`lcm(L,s_q)`

for a clean step `s_q`, retaining the new value only when it stays 19-neutral.

Theorem 3.1 shows something stronger than finiteness: **every arbitrary 19-neutral negative-helpful odd port maps to one member of this finite library.**

This is the BRC safe quotient for the present observer. It is not a heuristic port cutoff and does not depend on a numerical search bound.

## 5. Fresh-prime realization and factorial removal

Let `L in L_p`. Choose a fresh prime `ell>p`, distinct from every auxiliary prime already used, and realize the core at

`j_L=L ell`.

Because every relevant `s_q`, class-19 `h_r`, and target prime is smaller than ell and coprime to ell,

- `s_q|j_L` iff `s_q|L`;
- every class-19 endpoint/denominator incidence is unchanged;
- every class-13 denominator valuation below or at p is unchanged.

Hence `j_L` has exactly the L-core signature.

Use a distinct fresh ell for every repeated copy. Then every physical port has multiplicity one and every factorial term vanishes. Thus a nonnegative integer atom count is realized by an actual cloud with the exact linear signature; linearity is not obtained by silently deleting factorial provenance.

## 6. Exact target-p compensation

Because every L-core is odd and `h_p` is even, there is no p-endpoint event. Also `p` cannot divide L because every generating step is smaller than p. Therefore

`delta_p(L)` is either `0` or `-c_p`,

the latter occurring exactly when `s_p|L`.

For a target-cancelling atom choose another fresh prime `ell'>p` and put

`k=p^(c_p) ell'`.

Then

`delta_p(k)=c_p`

and every earlier target branch sees k neutrally:

- no earlier target prime divides k;
- no earlier even class-13 endpoint divides the odd port;
- no earlier class-13 cancellation step divides `p^(c_p) ell'`;
- no earlier class-19 endpoint or denominator divisor divides it.

Therefore each L-core with `s_p|L` has a provenance-preserving target-only compensator, and every atom can be realized with

`Delta_p=0`

and exact class-19 neutrality.

More generally `p^a ell'` gives any required positive target-only integer compensation a. Thus dropping an arbitrary port's useless positive p-denominator/factorial residue during canonicalization never obstructs restoration of exact p-neutrality.

## 7. Exact global repair cone

Let the initial defects on the earlier class-13 rows be

`b_q`, `q<p`, `q==13 (mod24)`.

For `L in L_p`, define its compensated atom coefficient on an earlier class-13 row q by

`a_q(L) = -c_q` if `s_q|L`,

and

`a_q(L) = v_q(L)` otherwise.

The p-compensation from Section 6 is invisible on these earlier rows.

### Theorem 7.1 — arbitrary-port repair iff finite LCM-atom repair

There exists an arbitrary finite added cloud which

1. is exactly p-neutral;
2. is exactly neutral on every earlier class-19 target;
3. makes every earlier class-13 defect nonpositive,

iff there are integers

`x_L >= 0`, `L in L_p`,

such that for every earlier class-13 q,

`b_q + sum_{L in L_p} a_q(L) x_L <= 0`.

Proof, forward direction.

Class-19 exact neutrality has no negative channel, so occupied helpful ports cannot spend positive class-19 defect. Even ports have no class-13 cancellation channel and can only add nonnegative earlier residue; discard them, replacing any target-p compensation they supplied by the target-only coordinates of Section 6.

For each remaining odd helpful port j, replace every occupied copy by a distinct fresh-prime lift of `L_p(j)`. Theorems 3.1 and 3.2 preserve every cancellation support and weakly decrease every earlier class-13 defect. Splitting multiplicities removes only nonnegative factorial residue. If target p becomes more negative after dropping positive residue, restore p exactly with target-only compensation. Collect equal L cores to obtain the integers x_L.

Proof, reverse direction.

For each of the finitely many requested atom copies, choose distinct fresh auxiliary primes and realize `L ell`. If `s_p|L`, attach its target-only compensator. Section 5 removes factorial interactions, Section 6 makes each atom p-neutral, and every L in the library is class-19-neutral. The displayed inequalities then give the required earlier class-13 closure.

So the shared-cancellation problem is not an infinite arbitrary-port search. It is an exact finite integer cone.

## 8. Exact clean-credit / dirty-capacity budget

For a clean class-13 q define

`N_q(x)=sum_{L: s_q|L} x_L`

and

`D_q(x)=sum_{L: s_q does not divide L} v_q(L) x_L`.

Then Theorem 7.1's q inequality is exactly

`c_q N_q(x) - D_q(x) >= b_q`.

Thus the remaining clean-row repair budget has two provenance-separated terms:

- cancellation coverage credit `c_q N_q`;
- denominator spill debt `D_q`.

A shared L atom may contribute cancellation credit to several clean rows simultaneously. This is precisely the synergy that the earlier one-row causal basis deliberately did not claim to optimize globally.

Now let d be a 19-dirty class-13 row. No 19-neutral L can satisfy `s_d|L`; otherwise the upward-closed debt theorem would make L class-19-dirty. Hence every atom has

`a_d(L)=v_d(L)>=0`.

Therefore the dirty row constraint becomes the exact capacity ledger

`sum_L v_d(L) x_L <= -b_d`.

Consequences:

- if `b_d>0`, infeasibility is immediate;
- if `b_d<=0`, `-b_d` is the exact available dirty denominator capacity;
- one shared atom spends `v_d(L)` once even if it simultaneously suppresses several clean rows, so separate single-q lower bounds must not be blindly summed.

Combining clean and dirty rows gives the exact global budget system

`c_q N_q(x)-D_q(x) >= b_q` for every clean q,

`sum_L v_d(L)x_L <= -b_d` for every dirty d,

`x_L in Z_{>=0}`.

This closes the global-optimality gap left by the causal clean-subcone theorem: the causal self-atoms are one feasible basis inside this larger finite LCM cone, while any globally better shared-support repair must appear as another integer point of this same finite system.

## 9. BRC interpretation

The safe quotient is

`arbitrary physical ports`
` -> cancellation-support LCM core`
` -> finite compensated atom signature`.

What is discarded:

- auxiliary prime identity;
- redundant factors that produce no additional cancellation;
- repeated physical-port identity after fresh-port splitting.

What is retained:

- every class-13 cancellation source `s_q|L`;
- integer cancellation depth `c_q`;
- integer denominator valuations `v_q(L)`;
- class-19 neutrality as a forbidden-divisor condition;
- target-p compensation provenance;
- shared-support structure through the LCM itself.

A quotient that keeps only a Boolean set of cancelled rows but drops L can lose denominator capacity data. A quotient that keeps separate q atoms but drops shared LCM atoms can falsely declare a globally feasible shared suppression infeasible.

## 10. Independent falsification/regression

Paired checker:

`research_checks/check_brc_clean_lcm_atom_repair_budget_20260924.py`.

Local exact validation reported:

- exhaustive 19-neutral odd ports `j<200000` at horizon `p=397`: `73,271`;
- canonical-support / divisor / class-19-neutrality / coordinatewise-domination failures: `0`;
- deterministic exact random 19-neutral ports across `p=157,277,397,733,1021`: `1,756`;
- atom-coordinate budget checks: `19,664`;
- full finite atom library at `p=397`: `23` distinct nontrivial cores;
- shared integer-budget vector checks on that full library: `5,500`;
- total failures: `0`.

Finite computation is falsification/regression only. The proof is Theorems 3.1, 3.2 and 7.1 plus the fresh-port realization.

## 11. Do not repeat / next

Do not search arbitrary port integers after this reduction when the observer is exact p-neutral / class-19-neutral repair. Generate the finite LCM library instead.

Do not identify the earlier descending causal vector with the global optimum; global shared-support feasibility is the integer system above.

Do not erase L after recording only its cancellation set: `v_q(L)` is active dirty-capacity provenance.

If formal D24 control remains blocked, the next nonredundant auxiliary unit is to exploit the finite LCM cone itself: derive structural dominance rules between L-atoms (same cancellation support with larger denominator vector is dominated), then determine whether the finite budget system admits a smaller antichain/Hilbert-basis carrier without changing exact repair feasibility.

If the canonical lossless staging-disposition/session-rollover operation becomes live, stop auxiliary work and return immediately to the Source-native D24 continuation path.
