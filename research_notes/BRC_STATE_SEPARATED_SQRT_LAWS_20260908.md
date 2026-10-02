# Separate the state population before projecting square-root BRC

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Status: research note with proofs and bounded executable checks; no canonical theorem promotion.  
Global context: `18b20e346491fdbb47f2c99da19b1a63198fc107`.  
Primary definition: [BRC multiplier basin theorems, pinned snapshot](https://github.com/awdawmip/enterprise-math/blob/c5d6e6ed4aa4c899706e2a895f55733dc2eb3cb8/research_notes/BRC_MULTIPLIER_BASIN_THEOREMS_20260906.md).

## 1. Definitions and the operation being observed

For positive integers, write

\[
N=J^2+R,\qquad J=\lfloor\sqrt N\rfloor\ge1,\quad 0\le R\le2J.
\]

Canonical square-root BRC is always the floor collapse
\(B(N)=J^2\). It is idempotent: \(B(B(N))=B(N)\). In particular, a literally strict downward collapse means **every nonsquare**. This note does not replace that definition with nearest-square rounding.

A separate and useful population classifier compares subtraction cost \(R\) with next-square addition cost \(2J+1-R\):

\[
Z_J:\ R=0;\qquad D_J:\ 1\le R\le J;\qquad U_J:\ J+1\le R\le2J.
\]

Here `D` means down-cost-cheaper and `U` means up-cost-cheaper. All members of both `D` and `U` still collapse downward under canonical BRC. The midpoint has no tie because the width \(2J+1\) is odd.

The observer choice is a **second**, independent decision: keep `(J,R)`, keep only `J`, or keep only `R`. First restrict the population, then project. Do not infer a property of the restricted observer from a pooled observer with its conditioning forgotten.

The nontrivial update results below concern **input translation** \(N\mapsto N+t\), not repeated application of the idempotent collapse. Under collapse itself, root-only updates as \(J\mapsto J\), and residual-only updates as \(R\mapsto0\).

## 2. Direction-only population: exact paired laws

Each complete basin \(\{J^2,\ldots,(J+1)^2-1\}\) has one stationary state, \(J\) down-cost-cheaper states, and \(J\) up-cost-cheaper states.

The reflection

\[
R\longmapsto 2J+1-R
\]

pairs `D_J` and `U_J`. Downward edit costs in `D_J` are exactly \(1,\ldots,J\); upward edit costs in `U_J` give the same multiset. Therefore both conditional smaller-cost means are \((J+1)/2\) under uniform sampling from their respective integer populations.

These are counting laws for a complete integer basin. The same balance has not been asserted for a prime, semiprime, or any other arithmetic subset.

## 3. Discard residual: an optimal uniform root-stability window

Suppose the initial population is `D_J`, and thereafter the observer retains only \(J\). For **every** initial number in that population,

\[
\boxed{\lfloor\sqrt{N+t}\rfloor=J\quad\text{for all integers }0\le t\le J.}
\]

Proof: \(1\le R\le J\), hence \(1\le R+t\le2J\). Translation remains inside the original basin.

This uniform stability window is sharp. Initial \(N=J^2+J\) reaches \((J+1)^2\) at \(t=J+1\). For \(J\ge2\), initial \(N'=J^2+1\), with the same observed root and the same initial direction, still has root \(J\) at that time. Thus the next root is no longer uniquely specified by the conditioned root-only observation. At \(J=1\), the initial down-cost-cheaper population is a singleton; constancy still ends at the stated boundary, but nonuniqueness does not apply.

Pooling all states destroys even a one-step guarantee: \(4\) and \(8\) have the same observed root \(2\), whereas \(5\) and \(9\) have roots \(2\) and \(3\).

Root-only observation also retains exact interval size and basin support information. The existing `square_multiplier_law(J,s)` supplies the already-established support count \(\min(s,2J+1)\) for multiplication by \(s^2\). Reusing a set/count transport law does not give the individual destination root when residual has been discarded. That support theorem is a dependency, not a new result of this note.

## 4. Keep residual only: fibers and an optimal update window

For a fixed observed residual \(r\ge0\), the full fiber of positive integers is

\[
F_r=\{J^2+r:J\ge\max(1,\lceil r/2\rceil)\}.
\]

For \(r\ge1\), precisely \(\lfloor r/2\rfloor\) members of this infinite fiber belong to `U`: their roots run from \(\lceil r/2\rceil\) through \(r-1\). All roots \(J\ge r\) belong to `D`. For \(r=0\), the fiber consists of stationary squares.

Successive members \(n_J=J^2+r\) have gaps \(2J+1\) and constant second difference \(2\). For example, \(F_3=\{7,12,19,28,39,\ldots\}\); only \(7\) is up-cost-cheaper. This transition to down-cost-cheaper states follows from the fiber inequalities.

Now retain only \(r\ge1\) **after restricting the initial population to `D`**. Define the residual function \(\rho(n)=n-\lfloor\sqrt n\rfloor^2\). Then

\[
\boxed{\rho(N+t)=r+t\quad\text{for all integers }0\le t\le r.}
\]

Proof: initial membership in `D` implies \(J\ge r\), so \(r+t\le2r\le2J\). The first basin boundary has not been crossed.

The window is sharp for **every** \(r\ge1\). The two initially down-cost-cheaper numbers

\[
N_1=r^2+r,\qquad N_2=(r+1)^2+r
\]

have identical observed residual \(r\). At \(t=r+1\), their residuals become \(0\) and \(2r+1\). Thus residual-only translation ceases to be uniquely determined at the first step beyond the guarantee.

For example, starting with \(12,19,28\) gives residual \(3\). Their residuals agree at \(t=0,1,2,3\), taking values \(3,4,5,6\). At \(t=4\), they give \(0,7,7\).

Without direction conditioning, even \(+1\) is ambiguous: \(3\) and \(6\) both have residual \(2\), while \(4\) and \(7\) have residuals \(0\) and \(3\).

**Both translation windows are measured from the initial state.** The retained conditioning says that the initial state was in `D`; it does not say every translated state remains in `D`. Increasing the observed residual does not renew the guarantee. At time \(t\), the residual-only guarantee has at most \(r_{\mathrm{initial}}-t\) steps remaining. These finite statements are not a globally closed recurrence.

## 5. A necessary baseline for residual histograms

When pooling complete basins \(J=1,\ldots,K\), i.e. all positive integers through \((K+1)^2-1\), the frequency of residual \(r\ge0\) is exactly

\[
f_K(r)=\max\bigl(0,K-\max(1,\lceil r/2\rceil)+1\bigr).
\]

Thus residuals \(0,1,2\) each occur \(K\) times; residuals \(3,4\) each occur \(K-1\) times; and subsequent pairs continue the staircase. Within `D` alone,

\[
f^D_K(r)=\begin{cases}K-r+1,&1\le r\le K,\\0,&\text{otherwise}.\end{cases}
\]

The triangular residual histogram in the down-cost-cheaper population is consequently a domain-counting effect. Any claim about an arithmetic subset must compare against its declared, direction-conditioned sampling baseline. Partial endpoint basins also require their own truncation correction.

## 6. Independent research lanes and what is complete

1. **Direction-conditioned lane:** establish paired distributions and compare arithmetic subsets only within the same root basin and declared population. The exact full-integer baseline is complete here.
2. **Root-only lane:** study interval, support, and finite root-stability statements with residual absent. The exact translation window is complete here; a count/support identity must remain distinguished from an individual-state update.
3. **Residual-only lane:** study fixed-residual fibers and finite translation windows with root absent. Fiber shape and the optimal conditioned window are complete here.

These lanes need separate observations and separate negative controls. A later combination must explicitly record any information that is reintroduced. The smallest remaining research question is whether a specified arithmetic subset shows a deviation from these exact conditioned baselines; no such deviation or hidden-factor extraction is claimed by this note.

## 7. Reproducible bounded verification

Companion experiment: `experiments/brc_state_separated_sqrt_laws_20260908.py`. It imports only `point_cost_state` and `square_multiplier_law` from the existing module. The executed local source had SHA-256 `6fe4551f053e6427c67aef1e70e837615d75aa5a52b7477bf6c9cb96fb9a7d3a`; its text matches Git blob `4d03ded19b38f5aa13d3e873e911205d35be5c5f` on this research branch after line-ending normalization.

From the repository root:

```powershell
python experiments/brc_state_separated_sqrt_laws_20260908.py --enterprise-root . --output-dir experiments
```

The run verifies 1,088 existing point states through \(N=1088\), 11,968 conditioned root-update instances, 6,512 conditioned residual-update instances, all 32 basin partitions, 31 root-ambiguity boundary pairs, 32 residual-fiber/boundary cases, 65 pooled residual counts, and 128 existing support-law calls. These bounded checks validate implementation and boundary examples; the proofs above establish the unbounded statements.

Output: `experiments/brc_state_separated_sqrt_laws_20260908.json`; verdict `PASS_EXACT_STATE_SEPARATION_LAWS_AND_SMALL_CHECKS`. The numerical scope is small positive-integer geometry. No factorization procedure or large-number scan is executed.

