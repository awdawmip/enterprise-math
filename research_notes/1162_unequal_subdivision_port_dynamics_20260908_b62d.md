# #1162 — unequal subdivision as a finite driven roughness-port system

Status: RESEARCH_NOTE / EXACT FINITE PORT DYNAMICS / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-unequal-subdivision-port-dynamics-20260908-b62d
Date: 2026-09-08

## 1. Scope

The equal-subdivision note showed that the weighted-cycle roughness state closes on two scalars `H` and `V`, with eigenvalues 1 and q^(-2). This note removes the equal-split assumption.

The purpose is not to average away the new microstructure. It is to identify exactly what new finite information enters the Basel/m=1 inverse-trace readout under one arbitrary positive q-way subdivision step.

## 2. Coarse state

Use normalized coarse gaps `g_i>0`, `sum_i g_i=1`, deviations

`delta_i=g_i-1/N`,

and centered cumulative discrepancies

`x_i=e_i-e_bar`,  `e_(i+1)-e_i=delta_i`.

As before,

`D_N=(2/N)sum_i x_i^2`,

`V_N=(1/N)sum_i delta_i^2`,

`H_N=D_N-V_N/3`.

## 3. Arbitrary positive q-way split and local wobble

Split each coarse gap g_i into positive subgaps

`g'_(i,0),...,g'_(i,q-1)>0`,

`sum_a g'_(i,a)=g_i`.

Separate equal-split transport from new microstructure by defining

`epsilon_(i,a)=g'_(i,a)-g_i/q`,

so `sum_a epsilon_(i,a)=0` for every coarse edge.

Define the within-edge cumulative wobble

`u_(i,0)=0`,

`u_(i,a)=sum_(b=0)^(a-1) epsilon_(i,b)` for a=1,...,q-1.

The refined cumulative discrepancy at subvertex (i,a) is exactly

`e'_(i,a)=e_i+(a/q)delta_i+u_(i,a)`.

Let

`ell_(i,a)=x_i+(a/q)delta_i`.

The average of ell over all qN refined subvertices is zero. Put

`u_bar=(1/(qN))sum_(i,a)u_(i,a)`.

## 4. Exact new ports

Define three finite one-step quantities

`U=(1/(qN))sum_(i,a) epsilon_(i,a)^2 >=0`,

`X=(1/(qN))sum_(i,a) ell_(i,a) u_(i,a)`,

`W=(1/(qN))sum_(i,a)(u_(i,a)-u_bar)^2 >=0`.

Then direct finite expansion gives

`V_(qN)=q^(-2)V_N+U`,

and

`D_(qN)=D_equal+4X+2W`,

where

`D_equal=H_N+q^(-2)V_N/3`

is the defect that would result from equal subdivision of the same coarse cycle.

Hence the persistent state obeys

`H_(qN)=H_N+Gamma`,

with the exact signed input

`Gamma := 4X+2W-U/3`.

Thus one arbitrary subdivision step is the finite driven state system

`H' = H + Gamma`,

`V' = q^(-2)V + U`.

The scale-free inverse-trace output remains

`beta' = 1/6 - 1/[6(qN)^2] - H' - V'/3`.

No derivative, interpolation or small-roughness assumption is present.

## 5. Equal subdivision is the zero-input trajectory

For equal subdivision, every epsilon and u vanish, so

`U=X=W=Gamma=0`.

The driven system reduces exactly to the closed law from the previous note:

`H'=H`, `V'=q^(-2)V`.

This identifies equal subdivision structurally: it is not merely one convenient split, but the zero-input refinement trajectory in the finite port dynamics.

## 6. Why positive unevenness U alone is not an exact repair coordinate

The port U records only the squared size of within-edge subdivision deviations. It loses the signed alignment X between the new wobble and the transported coarse discrepancy.

For q=2 write the split deviations on coarse edge i as `(t_i,-t_i)`. Replacing every t_i by `-t_i` preserves U and W but reverses X. For a nonuniform coarse cycle choose an edge with

`ell_(i,1)=x_i+delta_i/2 !=0`

and take only its t_i nonzero. For sufficiently small positive |t_i|, both choices keep all subgaps positive, while

`Gamma(t)-Gamma(-t)=8X(t) !=0`.

Indeed the linear `4X` term dominates the quadratic U,W terms for sufficiently small t, so the two equal-U refinements can even produce Gamma of opposite sign.

Therefore a positive total unevenness scalar U is not fiber-constant for the future H/beta observer. The signed cross information cannot be collapsed before its effect is evaluated. This is an exact instance of the BRC signed-boundary rule.

## 7. Conservative bound when only U is retained

If an observer intentionally discards the signed port X, a rigorous interval can still be propagated.

For each coarse edge, Cauchy gives

`sum_(a=0)^(q-1) u_(i,a)^2
 <= q(q-1)/2 * sum_a epsilon_(i,a)^2`.

Therefore

`W <= q(q-1)U/2`.

Also the refined equal-transport profile has mean-square

`(1/(qN))sum ell_(i,a)^2 = D_equal/2`.

Hence

`|X| <= sqrt[D_equal*q(q-1)U/4]`.

Consequently

`|Gamma|
 <= 2 sqrt[q(q-1)D_equal U]
    + q(q-1)U + U/3`.

This is conservative but finite. It makes the information trade explicit: retaining only positive unevenness U loses the sign of Gamma, so the output becomes an interval rather than an exact state update.

## 8. Iterated driven refinement

For a sequence of q-way subdivisions with ports `(Gamma_n,U_n)`, the exact recurrence is

`H_(n+1)=H_n+Gamma_n`,

`V_(n+1)=q^(-2)V_n+U_n`.

Thus

`H_n=H_0+sum_(j=0)^(n-1)Gamma_j`,

`V_n=q^(-2n)V_0 + sum_(j=0)^(n-1)q^(-2(n-1-j))U_j`.

All later Basel readouts follow from these two finite state coordinates. Arbitrary subdivision need not converge to the universal uniform fixed point: the accumulated signed Gamma inputs can permanently shift the refinement memory.

## 9. Observer-relative port collapse

For the declared future language consisting only of later `beta` readouts under a supplied subdivision process, the full microscopic refined gap vector can be replaced after each step by the state `(H,V)` plus the next-step ports `(Gamma,U)`.

This is a finite exact port representation for this scalar future language. It is not claimed to reconstruct the hidden gap vector, nor is it safe for a future language that later directly inspects hidden subedge geometry.

Positive-weight recurrent BRC theorems remain NOT_APPLICABLE to the signed Gamma input. The useful BRC rule here is observer-typed compression and preservation of signed provenance until its effect has been reduced to Gamma.

## 10. Prior-art boundary

Subdivision networks with nonuniform conductances and formulas for their Green kernels/Kirchhoff indices are established prior art. The current derivation is used to expose the exact roughness information flow for the #1162 scalar readout; no broad subdivision-network novelty claim is made.

## 11. Next

1. Determine whether the two-port `(Gamma,U)` description is minimal for the declared beta future language under arbitrary q-way subdivision.
2. Extend the construction to higher inverse moments, where additional signed/moment ports are expected.
3. Test native subdivision rules from the project substrate to see whether they force Gamma=0, a sign, or a smaller admissible port family.
