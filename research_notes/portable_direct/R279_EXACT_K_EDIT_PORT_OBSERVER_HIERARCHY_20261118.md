# R279 — Exact k-edit Port-observer hierarchy and arbitrary-depth hidden-cycle witnesses

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK / NOT_REVIEWED.
Scientific provenance: R278 at commit 341a500ebebe408d64d84735c4015b59c97c65ce, R275–R277 at fae3d3cf66a7bc294f9c5a854764bb14ab174030; science freeze 43ec6098b1330ae86d0a7863be336c5d97f6ef34. The input setting is the stable finite positive-rational **labeled visible Port** interface of WBRC-T30/T31/T32.

## Exact finite-horizon observation theorem

Fix baseline-stable W, a scalar visible star observer at Port r, and m labeled edge types e_1,...,e_m. Each elementary operation adds a positive rational weight to **one** named edge, provided the resulting matrix remains stable. Repeat edits to a named edge may be aggregated; intermediate observations are allowed and adaptive programs may select their next edits using earlier star readouts.

Define the k-edit observation language L_k as all such programs with at most k elementary additions. Let F_W(x) be the exact rational response function from R278, where x is the vector of total inserted edge weights.

For any two baseline-stable W,W' with the same Port labels and edit alphabet, the following are equivalent:

1. Every common admissible program in L_k has the same sequence of scalar readouts.
2. F_W(x)=F_W'(x) on every sufficiently small positive rational coordinate face with at most k nonzero components.
3. For every subset J of the m edge labels with |J|<=k, the restricted rational functions F_W(x_J,0_outside_J) and F_W'(x_J,0_outside_J) are identical in Q(x_J).
4. The normalized reduced numerator/denominator polynomial pairs from R278 coincide after restriction and reduction to each face J of size at most k.

Proof: After at most k edits, the support of the total update vector contains at most k distinct edge types. If all the relevant restricted rational functions agree, every intermediate readout agrees and induction gives equality of adaptive choices/readouts. Conversely, choose any such J, apply one arbitrarily small positive rational increment for each edge in J, and observe the final scalar. Agreement for all these admissible programs gives equality of the two rational functions on a rational grid in a nonempty open box in the J coordinates, hence polynomial identity. The R278 reduced-pair uniqueness gives statement 4. This characterizes the largest future-safe equivalence for L_k, rather than only a sufficient state.

The quotients form a monotone hierarchy L_0 <= L_1 <= ... <= L_m. They stabilize by L_m: any finite sequence over the fixed m-edge alphabet ends at some x with support <=m, so all-horizon indistinguishability equals L_m indistinguishability. No assumption about a uniform bound on the number of repeated edit calls is made after this stabilization.

## Strictness at arbitrary edit depth: labeled Port cycle

For every m>=2 let the visible Ports be 0,...,m-1. Let the initial W_c have a single self-loop c at Port 1, where c in {0,1/2}, all other original weights zero. Allow exactly the m named edge types

~~~text
0->1, 1->2, ..., (m-2)->(m-1), (m-1)->0,
~~~

with addition weights x_0,...,x_(m-1)>=0, and read only S_00. The two modules have the exact response

~~~text
F_c(x_0,...,x_(m-1))
  = (1-c) / ((1-c)-prod_i x_i)
  = 1 / (1-prod_i x_i/(1-c)).
~~~

Proof: The full determinant is (1-c)-prod_i x_i, because its only possible nontrivial directed cycles are the internal Port-1 self-loop and the full m-edge ring, which intersect. Deleting Port 0 breaks the ring, leaving a triangular principal minor with determinant 1-c. The inverse cofactor formula proves the identity.

For every proper subset of the m edge types, the product vanishes and F_c=1 for both c=0 and c=1/2. Consequently these two systems are indistinguishable by **every** L_(m-1) program, even one with arbitrary repetitions and rational edit weights. After one edit of each type with x_i=1/4, both final matrices have row sums below 1, while

~~~text
F_0 = 1/(1-4^(-m)),
F_(1/2) = 1/(1-2*4^(-m)).
~~~

They are distinct. Thus, for every k>=1, some strictly stable positive-rational labeled BRC Port models are observationally equal through k edits and distinguishable after k+1 edits. There is no fixed k, independent of the declared edge alphabet, that captures all finite-future joint residuals.

For m=2 the witness recovers R278's 16/15 versus 8/7; for m=3 it gives 64/63 versus 32/31. This is the precise future-language reason that separately harmless Port additions can jointly reveal otherwise hidden structural information.

## Exact computation and evidence

The stdlib-only R279_cycle_probe_horizon_checker.py uses fractions.Fraction and exact rational Gaussian determinant elimination. It enumerates **all 508 subset choices** for m=2,...,8, testing both c=0 and c=1/2 at fixed positive edge weight 1/4 and checking every tested row-sum stability inequality. All 1,016 direct response evaluations agree with the symbolic formula; every proper subset matches and every complete ring differs. R279_verification.json records all seven cases. The arbitrary-m theorem is proved algebraically above.

## Limits and next work

The scalar observer language reads one visible star and permits only the fixed named edge operations. Full WBRC-T32 future contexts may query other Port stars, loop-zeta, new external Ports and additional interactions; their safe signature remains the appropriate native typed carrier. The current classification does not discard genuine branch provenance when that provenance is observed.

Next investigate the polynomial coefficient support required for multiple output Ports and multi-step staged readouts, and compare the worst-case 2^m coefficient signature to smaller graph-structural cycle-cover signatures. Quantify prime-adic pole-depth/leading-residue stratification of these mixed-cycle coefficients under the R270–R277 models.
