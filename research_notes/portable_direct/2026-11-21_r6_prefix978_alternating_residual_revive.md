# PREFIX-978 — Alternating residual revival and a uniform finite-horizon theorem

Date: 2026-11-21. Research lane: independent portable auxiliary positive source-port BRC observer.
Source provenance retained: EM-DIRECT-FBEA5D; SID MCP-45ad6d29cd534c1aad25595a72e3c532; RA-3FB2D033BE6048D8712FF056. These historical identifiers do not by themselves authenticate a new privileged operation.
Frozen scientific foundation: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Parent: PREFIX-973--977. Status: AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.
Native X6/TRIADIC_CLOSURE_E correspondence: not established. No shared task CLAIM, formal Result, Review, or P000 promotion.

## Typed model

For integer p>=3, D_p consists of all c=2^i-s*2^j with 0<=i,j<p and signed source s in {+1,-1}. P_c and M_c record allowed source ports j for s=+1 and s=-1. For odd residues x modulo 2^p, allowed ports lie in A={1,...,p-1}, and

V_c(x)=((P_c AND NOT x) OR (M_c AND x)) AND A.

Choose one valid port j, record the named source (i,j,s), and flip x_j. In this experiment the prescribed residual schedule alternates c,C,c,C,... (first c). A fixed pair of numerical residuals is not collapsed into one residual; the pair and time-order are retained. For a fixed c,j,s, i is uniquely recovered from 2^i=c+s*2^j.

Define the individually reusable-port count
r(c)=popcount(P_c AND M_c AND A)
and the new cross-residual revival mask
J_p(c,C)=((P_c AND M_C) OR (M_c AND P_C)) AND A.

All counts below concern source-labelled positive paths with a single port choice per time step, not signed-amplitude cancellation.

## Theorem 978.1 — exact criterion for revival of individually terminating observers

Fix p>=3 and c,C in D_p with r(c)=r(C)=0. The following are equivalent:

1. There exists an odd initial x and a valid infinite path under the alternating schedule c,C,c,C,...
2. There exist valid paths of arbitrarily large finite length (initial x may vary).
3. J_p(c,C) is nonempty.

If J_p(c,C)=0, every path, for every odd initial x, has length at most
|support(P_c OR M_c OR P_C OR M_C) AND A| <= p-1.
If J_p(c,C) is nonempty, each j in this mask gives a two-step fixed-port cycle for every odd initial x whose j-th bit equals 0 in the P_c AND M_C case, or 1 in the M_c AND P_C case.

Proof. Since r(c)=r(C)=0, at a given nonzero port each residual separately admits at most one input-bit value. If no cross mask port exists, the two residuals together admit at most one bit value at each port. Its first flip makes that port permanently unavailable, irrespective of subsequent time phase or choices at other ports. Hence at most one use per port and the support bound. Conversely, if j belongs to the P_c AND M_C term, choose x_j=0: the first c step flips it to 1, and the C step flips it back to 0, both valid. If j belongs to M_c AND P_C, choose x_j=1. Repeating the two steps constructs an infinite named path. An infinite path implies arbitrarily large finite prefixes. This proves all claims.

This theorem gives an observer-specific joint-residual invariant: the individual persistence flags r(c),r(C) are insufficient to determine persistence after prescribed composition.

## Theorem 978.2 — uniform four-step bound away from zero residual

Under Theorem 978.1, suppose c and C are nonzero and J_p(c,C)=0. Then every valid history has length <=4, independent of p. The bound is sharp for p>=6.

Proof of the support lemma. For nonzero residual t, 2^i-2^j=t with i!=j has at most one solution (i,j), because the 2-adic valuation of |t| fixes min(i,j) and the remaining odd factor fixes the exponent difference. The positive sum 2^i+2^j=t has at most two ordered solutions: a binary two-one pattern gives the two orders, a binary one-one carry (i=j) gives one, and all other patterns give none. If a nonzero t has both a plus difference source and two minus sum sources, elementary binary arithmetic forces t=3*2^j; when j>=1 this is precisely a reusable port, excluded by r(t)=0. When j=0, only one of these two ports is in A. Thus every nonzero t with r(t)=0 has at most two nonzero source ports. The union for c,C has size <=4, so Theorem 978.1 applies.

Sharp example: p>=6, c=4 and C=16. Both have no reusable port, and J_p(4,16)=0. Start x=11 and choose ports (1,3,2,4) in that order under c,C,c,C. The successive x values are 11,9,1,5,21; all four steps are valid. A fifth step is impossible by the theorem.

## Explicit revival despite two individually finite observers

For every p>=3, choose c=0, C=4, j=1 and x=1. The alternating states are
1 --(c=0,j=1,plus)--> 3 --(C=4,j=1,minus)--> 1,
repeated indefinitely. Neither c=0 nor C=4 has a reusable odd-preserving port: r(0)=r(4)=0. The transition works through the *joint signed port relation* J_p(0,4), not through either individual persistence flag.

The source symbols at the repeating port are (i=1,j=1,+1) for c=0 and (i=1,j=1,-1) for C=4. The cycle is therefore a fully specified source-labelled witness, not an unsigned numerical equality.

## Exact finite enumeration

Exhaustive mask construction at p=19 gives |D_19|=499; exactly 483 individual residuals have r=0. Among their 483^2=233,289 **ordered** pairs, 10,960 have nonempty revival mask:
- 10,686 pairs with exactly one cross port;
- 274 pairs with exactly two cross ports;
- 222,329 pairs with no cross port.

The 11,234 labelled (ordered residual pair, port) cycle patterns each constrain exactly one of the 18 free bits of an odd 19-bit input, so the exact number of (pair, port, odd initial x) two-step repeat witnesses is 11,234 * 2^17 = 1,472,462,848. This counts labelled witnesses; it is not a count of distinct states or independent amplitudes.

Validation: the attached Python program independently constructs the signed source masks from the full (i,j,s) population. It checks all individually nonpersistent ordered pairs at p=3..8 and p=19, tests 25 cycle repetitions for each labelled cross port, and for all *no-cross* pairs at p=3..6 checks every odd initial state via an independent finite-state reachability algorithm at horizon p. The p=3..6 no-cross/state cases total 58,572. The p=19 full pair classification and the sharp four-step example are exact integer computations. No complete p=19 state-graph search is claimed.

## Preservation and next unit

The new two-residual mask J is an interaction observer. Replacing the ordered pair by either marginal persistence count r, or by initially active port counts, erases a future-relevant distinction. The masked provenance retains the residual pair, source sign, port, ordered path and multiplicity for the declared positive observer; native signed X6 events and TRIADIC_CLOSURE_E remain a separate transfer obligation.

Next: classify alternating pairs when one or both residuals contain fixed-residual reusable ports. Determine an exact condition and minimal sufficient signed carrier for a cycle involving different ports, then test longer prescribed residual words with proven state compression. Parent B_fix,odd(32) in {19,20} remains open.