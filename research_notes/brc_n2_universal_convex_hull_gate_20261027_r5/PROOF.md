# R5: Universal horizon-two seedless likelihood-ratio convexity gate

**2026-10-27 | Author-level finite-tree theorem; exact rational witness, not a native EM Result or independent review.**

## Frozen sources and scope

GLOBAL_KNOWLEDGE_V1 main `8fda7733a3b4c6d9562de3de67f2e22541c2512a`; Enterprise Math input main `0e47a8e5bf27cee995aa0f6bde93f7767beb2867`. Read both global entry files, project bootstrap, locked P000, ACTIVE residual worldview, current task bootstrap, BRC priority, mathematical/code policies, and `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Direct predecessor: `research_notes/brc_n3_moment_covariance_residual_20261027_r5/PROOF.md` and its `NEXT_TASK.md` at the pinned EM input. Reuse BRC ordered positive Q branch mass and exact likelihood ratios; no native X6 dynamical assertion or physics validation.

A finite rooted strictly positive two-measure tree has observation times t=0,...,T, histories h, Q masses q(h)>0, P masses p(h)>0, and exact likelihood ratio r(h)=p(h)/q(h). At a nonterminal history, the action is stop and decide P, stop and decide Q, or continue. At terminal T it is a decision. A **seedless LR behavioral** policy shares its randomized action probabilities across all histories with the same pair (t,r), with no persistent ex-ante random seed. Full policies can distinguish ordered histories. Let

```
O(pi) = (P(decide Q), Q(decide P), E_P tau, E_Q tau).
```

All randomness here concerns an external finite decision-tree auxiliary model; observation count tau is not Heartbeat/X6 native time.

## Theorem A: a policy-invariant aggregated kernel makes the seedless image a rational polytope

Suppose for each nonterminal (t,r) there exists a fixed stochastic kernel K[t,r](r') such that, under *every* seedless LR policy with positive Q mass continuing from (t,r), the conditional Q distribution of the next likelihood ratio is K[t,r]. It is sufficient that the policy-independent hidden-history posterior within each continued LR class exists; requiring each individual hidden kernel to be identical is stronger than needed.

Define the Q arrival mass a[t,r] and the Q action masses uP[t,r], uQ[t,r], c[t,r] for stop-decide-P, stop-decide-Q and continue. They satisfy the **linear** equations

```
a[0,1]=1; a[0,r]=0 for r != 1,
a[t,r]=uP[t,r]+uQ[t,r]+c[t,r]            (t<T),
c[T,r]=0; a[T,r]=uP[T,r]+uQ[T,r],
a[t+1,r'] = sum_r c[t,r] K[t,r](r'),     (t<T),
a,uP,uQ,c >= 0.
```

Other impossible states have zero mass. Every seedless policy satisfies these relations. Conversely, normalize its nonnegative feasible flows by a[t,r] to obtain local action probabilities uP/a, uQ/a, c/a (choose arbitrary probabilities for a=0). Inductively, the actual arriving Q mass equals the prescribed a: the fixed K condition makes each next-level arrival equation exact. Thus every feasible flow is realized by a seedless LR policy.

Since p(h)=r(h)q(h), and actions are shared within a (t,r) class, the four observers are the following **linear** functions:

```
P(decide Q) = sum_{t,r} r * uQ[t,r],
Q(decide P) = sum_{t,r}     uP[t,r],
E_P tau     = sum_{t<T,r} r * c[t,r],
E_Q tau     = sum_{t<T,r}     c[t,r].
```

Hence the seedless LR observable image is a compact convex polytope, even when individual histories sharing (t,r) have different next-step kernels. With a rational tree and rational fixed K, the flow polytope is rational. Rational feasible observer targets admit rational flow solutions and consequently rational local action probabilities (standard rational linear feasibility). No independent random seed is required to realize a convex combination.

**Proof note:** compactness follows from finite horizon and total Q mass <=1; the converse requires policy invariance of the **pooled conditional next-LR distribution**, not merely equality of the time-wise unconditional arrival histogram.

## Corollary B: no equal-support/different-image counterexample exists at T<=2

Assume the initial root is unique. With at most two observations, before t=1 the only choice was the single root stop/continue action. Conditional on reaching a time-1 LR class r, the Q posterior over its different first-observation histories is independent of that root continue probability. The continue action at (1,r) is common to every hidden history in that class, so conditioning further on continuing cannot bias this posterior. Therefore the pooled next-LR kernel K[1,r] is independent of the LR policy. K[0,1] is trivially fixed. Theorem A applies.

The full-history observable image is likewise compact and convex for *any* finite horizon: use the same exact occupation-flow proof on histories h rather than compressed classes; the physical conditional transition kernel from h is fixed. In particular, for T<=2 both images are compact convex, and the seedless image is contained in the full image. Equality of their **all-signed** four-variable support functions is equivalent to equality of the images, by finite-dimensional separating hyperplanes.

Consequently,

```
T <= 2 AND (forall lambda in R^4, min_H lambda.O = min_LR lambda.O)
  => {O(H)} = {O(LR)}.
```

This rules out the prior mother-question counterexample for every strictly positive finite rational horizon-two model, including models with strongly different hidden-history terminal kernels. It does **not** establish that full and compressed images are always equal.

## Corollary C: what a persistent seed buys at any finite horizon

For any horizon, a seedless time-LR policy has finitely many local action tables. Independently sample each table action once at time zero, and then use the resulting deterministic table. Every trajectory visits each (t,r) at most once; therefore this ex-ante mixture reproduces the behavioral policy's path law exactly. Thus the seedless behavioral image lies inside the convex hull of the finite compressed deterministic images, and all signed linear extrema are already attained at deterministic policies.

If all-signed support functions of full and compressed policies coincide, the full-history compact convex polytope equals the convex hull of compressed deterministic O-vectors. Carathéodory's theorem in R^4 implies that **at most five** deterministic compressed policies, selected by one persistent ex-ante seed, recover any given full-history four-vector. This is a seed-augmented conclusion only; at T>=3 it does not supply a seedless realization. The five-point bound is standard convex geometry, not a claim of new Carathéodory theory.

## Strict-positive rational witness: convex compressed image can coexist with a strict support gap

Use two time-1 histories a,b with P(a)=Q(a)=P(b)=Q(b)=1/2, so both have r=1. Final ratios are y=(1/4,1,7/4). Conditional Q kernels are

```
K_a=(2/5,1/5,2/5),     K_b=(1/20,9/10,1/20).
P(Y=y|h)=y Q(Y=y|h).
```

Every edge has positive rational P/Q probability. The two kernels differ, but the pooled time-1 kernel remains policy-independent, Kbar=(9/40,11/20,9/40). For J=eP+eQ+(1/16)E_Q tau, if a kernel is (s,1-2s,s), its optimal terminal Bayes error per incoming unit Q mass is 1-3s/4 (decide Q for y<1 and P for y>1).

At time 1 the immediate minimum error is 1. Continuing adds cost 1/16, so the a and b continuation costs are 61/80 and 82/80, respectively. Full-history policy continues at a and stops at b; the optimal root objective is 1/16 + (61/80+1)/2 = **151/160**. A seedless policy must treat a,b alike: continuing both costs at time 1 143/160 and stopping both costs 1. Root continuation yields 1/16+143/160 = **153/160**, better than root stopping at 1. Thus

```
min_LR J - min_full J = 1/80 > 0.
```

This shows why convexity alone does not imply compression fidelity.

For a constructive convexification certificate, take compressed A: root continue 1, time-1 continue 1, final decide Q at y in {1,7/4}; and compressed B: root continue 1/2 (otherwise decide P), time-1 continue 2/3 (otherwise decide Q), final decide Q only at y=7/4. Averaging O(A),O(B) equally can be achieved by the **single seedless** C: root continue 3/4, time-1 continue 8/9 (otherwise decide Q), terminal decide-Q probabilities (0,3/4,1) at y=(1/4,1,7/4). Direct exact calculation:

```
O(A)   = (151/160, 9/40,   2,     2)
O(B)   = (143/480, 91/120, 5/6,   5/6)
O(C)   = (149/240, 59/120, 17/12, 17/12)
       = (O(A)+O(B))/2.
```

## Actual verification, boundary and successor

The executed `VERIFY.py` uses `fractions.Fraction`, checks P/Q normalization and strict positivity, enumerates **all 1728** full-history deterministic action descriptions and **all 72** compressed deterministic descriptions, recovers the two exact extrema 151/160 and 153/160, and checks the convexification witness exactly. Their deterministic global minima cover **all real local randomizations** by backward optimization/multiaffinity of the finite acyclic expected objective. The finite program tests this particular model; universal convexity and the general T<=2 no-go follow from the independent flow argument above. No CAD/QE, Lean proof, external novelty search, or native Driver review was performed.

Last durable frontier: this T<=2 theorem and full rational output; unresolved task: perform the exact N=3 ternary-kernel convex-hull prefilter and, only if passed, prove/exclude a rational four-vector hole in the all-real seedless image. See NEXT_TASK.md. Activity registration `RA-EMR5-20261027-HULLGATE-0741` is local-session identity only, not a Task claim, Result or independent review.
