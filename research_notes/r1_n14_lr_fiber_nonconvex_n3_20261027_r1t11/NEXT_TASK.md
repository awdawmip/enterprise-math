# Next research: LR-constant quotient, strictly coarser observer, and minimum memory

**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 `main@6190a3375e2e7cf63d5f0c303f9b44956700f960`, P000 original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, EM research base `main@673e3dcb3416f3a033e8978fb2eb421e7f03dd2e`. External model only; no native P000 X6 transfer or Source-native task authority.

**Verified author-level frontier:** `PROOF.md` constructs distinct strictly positive rational P/Q laws at horizon 3 with three symbols and deterministic x such that every compressed x fiber has a constant likelihood ratio, yet the *paired* image of the **same fresh-coin current-x-only policy** under terminal observer `(T,x,D)` is not convex. Strategies U,V are individually achievable, but their midpoint violates an equality required of every real-parameter x-only policy:

`(u_A+u_B)W_0 - R(u_A p_A0+u_B p_B0)=0`.

The exact residual at the midpoint is `-1/144` under P and `-1/72` under Q, forcing P/Q event discrepancies 1/72 and 1/36. The checker verifies all 40 ordered prefixes, both strict positive laws, seven LR fibers, and the midpoint using Fraction. **This is a complete all-real no-go from an algebraic identity, not an exhaustive policy enumeration**. The prior N=2 example lacked LR constancy; the prior N=3 predecessor-kernel result proved only a rank defect, not this nonmembership.

**First open falsifiable question:** For the **same exact N=3 model**, when terminal readout is reduced to `(T,D)` (forget both time-one A/B and time-three y), is the paired quotient image still nonconvex? The current certificate relies on those observer distinctions and **does not** answer this stronger question. Seek an explicit pair of admissible policies, an exact midpoint, and a universal real polynomial/inequality exclusion; otherwise derive a general convexity construction or a tightly scoped feasibility conclusion. Use the quadratic path-flow equations of the preceding PROOF, not a rational-only grid.

**Second question:** Is N=3 the minimum time depth for nonconvexity under LR-fiber constancy for arbitrary strictly-positive rational P/Q finite trees and arbitrary recursively updatable state x and observer? Analyze N=2 mathematically; neither claim nor assume minimality. Separate the case of zero-information P=Q from P != Q.

**Third question:** Does carrying the one-bit origin group A/B through the time-two state make the example strongly lumpable and restore a convex paired occupancy image? Formulate minimal monitor/observer repair; do not confuse persistent ex-ante policy selector with permitted memory of the observation history.

**Proof and status discipline:** positive rational ordered-path BRC carrier only. No signed-phase cancellation, native Heartbeat computation, X6 theorem, independent Driver review, formal CLAIM/Result, or Lean completion. Current Source control owner is unverified (`CONTROL_QUOTA`); native session creation was denied (`STATIC_READONLY_SCOPE_DENIED`, operation_sent=false). Continue only in explicitly labeled author-side research unless authenticated task authority changes.

**Reproduction:** `python VERIFY.py > RESULT.json`; expected `status=PASS`, `compressed_states=7`, `number_of_ordered_prefixes=40`, P/Q residuals `-1/144,-1/72`.
