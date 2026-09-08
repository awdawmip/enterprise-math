# #1162 — exact roughness RG under equal electrical subdivision

Status: RESEARCH_NOTE / EXACT FINITE ROUGHNESS REFINEMENT LAW / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-equal-subdivision-roughness-rg-20260908-b62d
Date: 2026-09-08

## 1. Scope

Continue the user's correction that microscopic differentiation is not a stable/native primitive under a rough discrete relation. Start from the exact arbitrary-weight cycle defect of `research_notes/1162_exact_weighted_cycle_roughness_defect_20260908_b62d.md` and ask what roughness information survives the actual finite operation of equal edge subdivision.

No derivative in N, edge length or interpolation parameter is used.

## 2. Normalized gap and cumulative-error coordinates

Let a positive weighted cycle with N edges have normalized resistive gaps

`g_i=r_i/S >0`,  `sum_i g_i=1`.

Define edge deviations

`delta_i=g_i-1/N`,  `sum_i delta_i=0`.

Choose a cyclic starting vertex and define cumulative discrepancy

`e_0=0`,
`e_(i+1)-e_i=delta_i`,
`e_N=e_0`.

Changing the starting vertex only cyclically reindexes the e_i and adds a common constant, so centered variances below are intrinsic to the cyclic gap data.

The exact roughness defect from the previous note can be simplified to

`D_N = (2/N) sum_i (e_i-e_bar)^2`.

Proof: the arc discrepancy `d_(i,k)` equals `e_(i+k)-e_i`. Summing its square over all ordered pairs i,k is the standard identity

`sum_(i,j)(e_j-e_i)^2 = 2N sum_i(e_i-e_bar)^2`.

Define also the local gap variance

`V_N=(1/N) sum_i delta_i^2
    =(1/N) sum_i(e_(i+1)-e_i)^2`.

## 3. Equal electrical subdivision

Fix integer q>=2. Replace each original resistance r_i by q equal series resistors `r_i/q`. This preserves the total resistance of every original edge and produces qN edges.

At the refined subvertex `(i,a)`, a=0,...,q-1, the cumulative discrepancy is exactly the linear interpolation

`e'_(i,a)=e_i + (a/q)(e_(i+1)-e_i)`.

Because `sum_i delta_i=0`, the refined mean equals the original centered mean.

Direct finite summation over a gives

`V_(qN)=q^(-2)V_N`,

and

`D_(qN)=D_N - (1-q^(-2)) V_N/3`.

A derivation of the second formula uses

`sum_(a=0)^(q-1) a=q(q-1)/2`,
`sum a^2=q(q-1)(2q-1)/6`,

and

`sum_i (e_i-e_bar) delta_i = -(1/2) sum_i delta_i^2`.

Everything is a finite identity.

## 4. Persistent and irrelevant roughness branches

Define

`H_N := D_N - V_N/3`.

Then the subdivision law immediately gives

`H_(qN)=H_N`.

Thus the roughness carrier splits exactly into two refinement branches:

- persistent memory `H`, eigenvalue 1;
- local gap variance `V`, eigenvalue q^(-2).

After n equal q-subdivisions,

`V_(q^nN)=q^(-2n)V_N`,

`D_(q^nN)=H_N + q^(-2n)V_N/3`.

The local variance decays, but roughness does not in general disappear: it converges exactly to H.

Moreover H is strictly positive for every nonuniform cycle. Let `x_i=e_i-e_bar`. The elementary inequality

`sum_i(x_(i+1)-x_i)^2 <= 4 sum_i x_i^2`

gives `V_N<=2D_N`, hence

`H_N=D_N-V_N/3 >= D_N/3 >=0`.

Equality H=0 forces D=0 and therefore all gaps uniform.

So at least one third of the initial quadratic roughness defect is persistent under arbitrary repeated equal subdivision unless the original cycle was uniform.

## 5. Exact rough Basel flow

Recall the scale-free weighted inverse-trace readout

`beta_N = (N^2-1)/(6N^2) - D_N`.

Using the decomposition above,

`beta_(q^nN)
 = C_rough - q^(-2n)[1/(6N^2)+V_N/3]`,

where

`C_rough := 1/6 - H_N`.

Therefore the finite affine refinement law is exact:

`beta_(qN)=q^(-2) beta_N + (1-q^(-2)) C_rough`.

The usual two-scale Basel projector does not recover 1/6 from a rough family. It recovers

`[q^2 beta_(qN)-beta_N]/(q^2-1)=C_rough=1/6-H_N`.

Thus refinement washes out only the q^(-2) transient. The persistent roughness memory shifts the fixed point.

The universal uniform coefficient is recovered only after carrying the repair coordinate:

`1/6 = C_rough + H_N`.

Equivalently at one scale,

`1/6 = beta_N + H_N + 1/(6N^2)+V_N/3`.

## 6. Observer-relative exact compression

This gives a concrete BRC observer distinction.

### Future language = later equal-subdivision beta readouts only

The pair `(beta_N,beta_(qN))` determines `C_rough`, hence predicts the entire future orbit

`beta_(q^nN)=C_rough+q^(-2n)(beta_N-C_rough)`.

For this future language, the microscopic gap vector is exactly quotientable after two scales.

### Future language also asks for the uniform-model coefficient 1/6

The same two-scale orbit determines only `C_rough=1/6-H`; it cannot distinguish the universal uniform coefficient from persistent roughness. One additional repair coordinate such as H (or equivalently V together with beta and N) is required unless uniformity has been separately proved.

This is not a philosophical distinction: the next section gives a finite rational fiber witness.

## 7. Exact rational witness that one coarse beta value loses refinement information

Take N=4 and epsilon=1/100. Define two positive normalized gap vectors

`g^A=(22,22,26,30)/100`,

`g^B=(22,23,24,31)/100`.

Their deviations from 1/4 are epsilon times

`(-3,-3,1,5)` and `(-3,-2,-1,6)` respectively.

Exact calculation gives the same rough defect

`D_A=D_B=21/20000`,

so the same coarse inverse-trace readout

`beta_A=beta_B=97/625`.

But their local variances differ:

`V_A=11/10000`,

`V_B=1/800`.

Hence their persistent memories differ:

`H_A=41/60000`,

`H_B=19/30000`.

After equal dyadic subdivision,

`D_A'=31/40000`,

`D_B'=59/80000`,

so the refined beta values differ by exactly `3/80000`.

Therefore the scalar coarse beta observer is not fiber-constant for the future refinement operation. Adding the repair coordinate V (or H) suffices to restore exact predictability.

## 8. Relation to the earlier exact defect

The previous identity

`C_rough(N,q)=1/6-[q^2D_(qN)-D_N]/(q^2-1)`

now simplifies under equal subdivision because

`q^2D_(qN)-D_N=(q^2-1)H_N`.

Thus H is exactly the transported roughness defect seen by the Basel refinement projector.

This is stronger than a small perturbation bound and more faithful to the user's roughness objection: the microstructure is not declared negligible; its persistent contribution is retained as an explicit finite state coordinate.

## 9. Prior-art boundary

Kirchhoff indices/effective resistances of subdivision graphs and subdivision networks are established prior art, including general formulas relating subdivided and base networks. No claim is made that graph subdivision or Kirchhoff-index transformation is new.

The candidate project structure to evaluate separately is the exact BRC-style decomposition of a weighted cycle's scale-free Basel defect into a refinement-invariant memory H plus a q^(-2) local-variance mode, together with the observer-relative compression/minimal-repair witness above.

## 10. Next

1. Generalize from equal subdivision of each edge to allowed unequal subdivision rules and identify the additional within-edge repair coordinates.
2. Determine whether H admits a purely local finite formula or a minimal finite port representation that avoids keeping all cumulative discrepancies.
3. Seek higher-m analogues in which roughness decomposes into finitely many persistent/transient tensors under actual integer subdivision, without introducing microscopic derivatives.
