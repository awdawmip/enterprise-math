# A mass-weighted error contract for the native single-walker sampler

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC. This is a specialization of the
amplitude-query simulation approach, with Bravyi, Gosset and Liu (2022) as
direct prior art. It is not a construction of an efficient approximate
oracle, and no new approximate native execution is claimed in this note.

The exact-row-to-order reduction concerns a uniform exact answer at every
prefix. It does not exclude a sampler that spends a controlled total error
budget on low-mass histories. The following contract makes that distinction
precise without assuming a positive lower bound on every parent mass.

## Defined approximation, including zero answers

For each actual bit prefix h of length i, let v_h(w) be the exact raw full
row and let u_h(w) be an approximate raw full row. These functions are
defined on the same entire work carrier, including residual coordinates.
The approximation must be determined by h and w, not by the private latent
trajectory. A randomized oracle can be handled by first conditioning on
its independently selected seed and proving/averaging the same contract.

Use the exact existing proposal: from latent W, a fresh fair coin sets
Z=W or P_i W. For this proposal, put

    x~=u_h(Z), y~=T_h u_h(P_i^-1 Z), S~=||x~||^2+||y~||^2.

If S~>0, draw the next bit with p~0=||x~+y~||^2/(2S~). If S~=0, use a
fresh fair bit. In either case the next latent label is Z. This defines a
finite stochastic kernel even when the approximate row is zero at a
possible exact proposal. Exact denominators/sampling, or separately charged
rounding error, are required. No exact marginal mass is evaluated online.

Let M_h=sum_w ||v_h(w)||^2 and E_h=sum_w ||v_h(w)-u_h(w)||^2. At depth i,
sum_h M_h=1 for the complete raw actual instrument. Define

    eta_i = sqrt(sum_(|h|=i) E_h).

## Local and global bounds

At a proposal z under the exact reference process, set a_z=(x,y) with
x=v_h(z), y=T_h v_h(P_i^-1 z), S=||a_z||^2>0, and let
e_z=||a_z-(x~,y~)||. Both bit scores are probabilities of the same orthogonal
plus/minus measurement on the normalized two-arm vector. If B=(x~,y~) is
nonzero, decompose a_z=alpha B/||B||+r with r orthogonal to B. The trace
distance between the two normalized pure states is ||r||/sqrt(S), and
||r||<=||a_z-B||=e_z. A measurement cannot increase this distance. Thus

    delta(h,z)=|p0-p~0| <= min(1, e_z/sqrt(S)).

If the approximate vector is zero, e_z=sqrt(S), so the same bound holds
for the specified fair fallback. There is no small-denominator exception.

Under the exact invariant, q_h(z)=S(z)/(2M_h). Orthogonality of T_h and
bijectivity of P_i give sum_z S(z)=2M_h and sum_z e_z^2=2E_h. Applying
Cauchy-Schwarz yields

    sum_z q_h(z) delta(h,z) <= min(1, sqrt(E_h/M_h)).

The two samplers use identical label-proposal kernels; only this local bit
kernel differs. A telescoping comparison that follows the exact process
up to the differing step, then the approximate kernels thereafter, bounds
terminal total variation by the sum of local kernel distances averaged
over exact reference states. At each depth, Pr_exact(h)=M_h. Consequently,

    TV(final exact joint(h,W), final approximate joint(h,W))
       <= sum_i sum_(|h|=i) min(M_h, sqrt(M_h E_h))
       <= sum_i eta_i.

The terminal bit string and any common deterministic classical
postprocessing obey the same bound by data processing. The bound preserves
the full noncommuting temporal feedback order and complete internal rows.
All final bounds may also be truncated at 1. Only M_h>0 and S(z)>0 enter
the ratios. Zero-mass exact histories contribute zero to the first bound; approximation
on histories reached only after divergence is handled by kernel contraction.

## Research use and what is still missing

For a chosen set H_i of prefixes, setting u_h=0 on H_i contributes at most
sum_(h in H_i) M_h to the tighter bound. Thus an independently certified
small total mass can justify a cheap fallback on that whole set. Counting
prefixes or calling them rare is insufficient: their mass must be bounded.

More generally, if a declared bad set B_i has certified exact total mass
beta_i, arbitrary totalized local kernels on it cost at most beta_i. For
consistent approximations on the remaining histories, the mixed bound is

    TV <= sum_i [beta_i + sum_(h not in B_i) sqrt(M_h E_h)]
       <= sum_i [beta_i + sqrt(sum_(h not in B_i) E_h)].

This can be stronger than placing zero approximations on bad histories and
paying sqrt(beta_i) in the looser aggregate norm bound.

This avoids requiring uniformly small relative error for every conditional
state. It does not supply E_h, eta_i, the low-mass certificate or a cheap
point-query implementation. Proving and computing such certificates must
be charged. Independently choosing inconsistent values for repeated
queries at the same (h,w), hidden dependence on the sampled latent path,
and omitting an oracle failure event all invalidate this contract unless
covered by an additional argument. A reported numerical experiment or
small empirical error cannot replace the global error certificate.

The trajectory-independence assumption has a sharp symbolic counterexample.
On a cyclic work carrier of size L=4^r, let v_z=2^(-r), P shift by one, and
T=I. The exact next bit is always plus. If a private-path approximation
u^W flips only the sign at the current latent W, its complete-row squared
error is 4/L, yet either proposal Z=W or PW always sees opposite signs and
the approximate next bit is always minus. Thus TV=1 while that conditional
error tends to zero. This is a local-kernel assumption counterexample, not
an assertion that the standard work=1 Shor program reaches that prefix.
It rules out applying the bound to latent-dependent approximations.

The local estimate, adaptive-kernel telescoping and this counterexample
were independently checked by another shared-context author. This is
mathematical review rather than an independent admission or an executed
approximate-scientific benchmark.

The general exact oracle remains order-finding-powerful. The open, less
demanding route is a compact approximation with this global error control
and a provable total construction/query cost.

Primary antecedent: [How to simulate quantum measurement without computing
marginals](https://arxiv.org/pdf/2112.08499), especially the approximate
sampling construction and supplementary stability proof. This note derives
its constants directly for the project's actual two-arm adaptive kernel;
it does not attribute the displayed formulas verbatim to that paper.
