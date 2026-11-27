# P12: sharp unconditional fallback budget for certified conditional-bit intervals

Date: 2026-11-28. Driver lane EM-DVR-DEBB5E; scoped mathematical support, not a Task execution/CLAIM, not native BRC arithmetic, not an independently admitted Result. This is an abstract probability certificate applicable to a future typed BRC mass provider, not a claim that such a provider has been constructed or that this elementary technique is globally novel.

## Source and scope

P12 immutable taskbook at Source 21efc11c60fc37c7d9fd0c2df4c1dc3ac072d1de, blob 53dfbc58dbd45f73b3d3a006fba08e6dbebdaf7e; publication TP2-BC1A7FA0007357402667. Prior continuation dvr-20261128-0303-p12-handoff-v1 SUCCEEDED: at admission task READY/NEEDS_DISPATCH, no live claim, required role RESEARCHER, execution_authorized=false. No persisted checkpoint found by this receipt, which does not establish absence of historical research. Its declared prior P01 publication at a155bb2c856256d1df260eaa72eedb229fca1e23 was read exactly (blob 520e49f671e74970c1005f82858cdfd49ced3d72); this is a provenance-repair publication, not a proof of conditional sampling. Private proof paths v03/v02/S1 remain unresolved in this receipt. No classical modular-arithmetic simulation is substituted for typed BRC; frozen low-bit observations and their existing authors retain provenance. Current P01 status read request dvr-20261128-0400-p01-dependency-state-v1 initially QUEUED.

## Lemma (sharp mass-weighted uncertainty)

Let P be any fixed finite binary-word distribution. At prefix s let its two child masses be x=P(s1), y=P(s0), p=x+y>0, and suppose certified nonnegative intervals x in [a,a+c], y in [b,b+d]. Assume c,d>=0. The conditional bit-one probability q=x/p belongs to [l,u], where
l=a/(a+b+d), u=(a+c)/(a+b+c).
When a child upper bound is zero, its conditional mass is identically zero and the interval can instead be the exact endpoint (0 or 1). Otherwise both displayed denominators are positive.

For any feasible x,y,
p*(u-l) <= c+d.
Proof: set S=a+b, C=c+d, z=cd. The interval width equals (ad+bc+z)/((S+c)(S+d)). As p<=S+C and ad+bc<=S*max(c,d), with h=min(c,d), the difference between C*(S+c)*(S+d) and (S+C)*(S*max(c,d)+z) equals S*((S+C)*h-z)>=0 (since C*h>=z). This proves the bound, including c=d=0. Sharpness: a=b=0, c,d>0, x=c,y=d gives width 1 and p=c+d. The bound requires unconditional child masses, not unnormalized amplitudes or independent per-bit marginals.

## Exact sampling and fallback

Draw U uniform in [0,1) at the prefix, independent of its preceding history. If U<l emit 1; if U>=u emit 0. Otherwise refine a certified nested interval using the SAME U, or compute q exactly and compare SAME U with q. Apart from a null equality event this produces precisely the ideal threshold bit. If exact local q is available but the old U cannot be retained, the ambiguous branch may instead draw a fresh Bernoulli((q-l)/(u-l)); conditional on ambiguity the old U was uniform in [l,u), for intervals fixed independently of U. Using a fresh Bernoulli(q) on ambiguity is generally WRONG: q=1/4 and [l,u]=[0,1/2] gives bit-one probability 1/8, not 1/4. For adaptive refinement depending on U, do not apply the resampling rule unless the conditional law of U is proved; the same-threshold procedure remains exact with certified brackets.

For depth m, if the interval provider is fixed (or its random certificates are independent of the current threshold), the probability of reaching a first ambiguity at depth k is at most sum over |s|=k of P(s)*(u_s-l_s), bounded by sum_s(c_s+d_s). Consequently the probability of ANY fallback is at most min(1, sum over k and s of c_s+d_s). Proof: couple to the ideal bit sampler; prior to first ambiguity the two paths agree, and the unconditional probability of ideal prefix s and threshold in its ambiguous interval is P(s)*(u_s-l_s). Union bound. A no-fallback algorithm which aborts on ambiguity returns a subprobability of the exact target distribution; on an extended alphabet including FAIL its total variation distance from the target is precisely the abort probability (the successful mass is dominated pointwise by the target). In particular any useful event loses at most this probability in absolute success mass. Conditional distribution given no abort need not equal P.

For a per-level certified sum <=epsilon_k, total fallback <=sum epsilon_k. Alternatively a local relative width c_s+d_s<=epsilon_k P(s) gives that same bound, but this is only useful if it is certifiable without the unknown exact mass. The per-level sums range over all prefixes; no claim that evaluating them is efficient. This certificate does not require division by a rare-prefix mass in the final error budget.

If the refinement stream is nested and fixed independently of U, the unconditional chance of reaching stage j+1 at node s is at most P(s)*(u_{s,j}-l_{s,j}) <= c_{s,j}+d_{s,j}. Thus expected incremental cost is bounded by summing these reach bounds times certified per-stage cost caps (plus the initial evaluation cost and final exact fallback cost). Cost of generating sufficient random bits, interval endpoints and exact fallback must also be included. In general one cannot claim polynomial runtime or useful factor success from the probability certificate alone.

## Exact finite arithmetic sanity check

Executed the following JS integer loop (all intermediate integers safely below 2^53) in this turn; tested 6400 nondegenerate endpoint quadruples, 256 equalities, 6144 strict cases, zero failures. This tests the strongest bound p=a+b+c+d and is a sanity check, not the proof or a native BRC experiment.

```js
let tested=0,eq=0,fail=0,strict=0;
for(let a=0;a<=8;a++)for(let b=0;b<=8;b++)
for(let c=0;c<=8;c++)for(let d=0;d<=8;d++){
  let S=a+b+c+d;
  if(!S||a+c===0||b+d===0)continue;
  let den=(a+b+c)*(a+b+d),num=a*d+b*c+c*d;
  let diff=(c+d)*den-S*num;
  tested++;
  if(diff<0)fail++;else if(diff===0)eq++;else strict++;
}
console.log({tested,eq,strict,fail});
```

## Remaining work

Need actual typed signed/amplitude BRC provider of certified joint child masses, work-fiber source, proof of any block aggregation and uniform cost/error budget, safe exact fallback with measured cost, and useful factor/period events on exact declared input. This note cannot close P12 or replace earlier v03/S1 evidence, and is not a new formal task publication. It is a bounded support lemma to offer the actual authorized researcher, not a claimed owner transition. P12 continuation returned required role RESEARCHER; no agent launch or new claim by this Driver. No changes to Task, Result, review or parent status.
