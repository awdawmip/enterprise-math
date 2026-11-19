# R762GG — Exact lattice obstruction and diagonal holonomy for a four-STAR signed triadic BRC candidate

Date: 2026-11-19 (Asia/Shanghai). Research context: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. **Scientific status: AUTHOR-PROVED within the explicitly defined candidate model; NOT_REVIEWED.** Publication type: independent, non-overwriting portable research note. Prior provenance: R762GF@7a86d75bb3bb175b4433183540ffce0fb0548504; previous Researcher EM-X6-3050F6 / RUN-38b39991bc60c4982ac09378 is historical research context, not a new author/session authentication claim.

## Frozen inputs, event type and boundary

Immutable taskbook: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Scientific P000 pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. Current method/preservation rules are read separately from these scientific pins.

Retain six-dimensional affine X6 Cell coordinates relative to a chosen Cell, six signed primitive axis steps, the native PERP_E relation of 120 degrees between distinct axes, and primitive stable-force arity three. A complete triad event also retains three named ports, their ordered Link cycle, equal nonzero force quanta, source label and ordered primitive-step expansion.

Choose the four frozen K4-STAR axis triples (zero-based):
S0={0,1,2}, S1={0,3,4}, S2={1,3,5}, S3={2,4,5}.
For each S define H_S=sum(e_i : i in S). Build the explicit **candidate composite transport language** with an event +S or -S moving its Cell attachment by respectively +H_S or -H_S, with a named equal-quantum three-Port closed relation carried along the event. A negative transport sign describes the displacement direction, **not subtraction of positive BRC mass or cancellation of force quanta**. All primitive steps, event order, port/link/source IDs and multiplicities remain in the uncompressed BRC object. Each composite event has exactly three signed primitive axis steps; it is not a new primitive straight segment.

The existence of the negative event, any particular port-cycle legality gate and future native signed TRIADIC_CLOSURE_E permissions are **candidate choices**. The theorems below are conditional on the eight events being available as declared. The fixed STAR atlas has S4 covariance; full S6 requires retaining/translating the atlas as additional source data.

## Theorem 1 — exact integer image of the STAR-incidence transport lattice

Label the six axes by edges 01,02,03,12,13,23 of an abstract K4, and the four STARs by vertices 0,1,2,3. The six-by-four incidence map B:Z^4→Z^6 has rows

    [1,1,0,0]
    [1,0,1,0]
    [1,0,0,1]
    [0,1,1,0]
    [0,1,0,1]
    [0,0,1,1].

For x=(x01,x02,x03,x12,x13,x23) in Z^6, x lies in B(Z^4) if and only if

(1) x01+x23 = x02+x13 = x03+x12; and

(2) x01+x02-x12 is even.

For such x the unique integer event-count vector is

    n0=(x01+x02-x12)/2,
    n1=x01-n0, n2=x02-n0, n3=x03-n0.

**Proof.** Every transported edge coordinate is x_ij=n_i+n_j, so opposite-edge sums are all sum_i n_i, and x01+x02-x12=2n0. Conversely, the displayed formula reconstructs integers n0..n3; the three edges 01,02,03,12 match by substitution and the two opposite-edge equations force edges 13 and 23 to match. Uniqueness follows from the same reconstruction. Thus B has rank four. This gives a concrete *membership and inverse algorithm*, not only a real-linear span description.

The rational span B(Q^4) is cut out exactly by the two opposite-edge equalities. Within its integral saturation B(Q^4)∩Z^6, the lattice B(Z^4) has index 2: the parity condition above is the remaining obstruction. Equivalently the Smith diagonal is (1,1,1,2). To see the integer index directly, an x satisfying the two opposite-edge equalities has a reconstructed n with all coordinates integral or all half-integral; multiplying its half-integral case by 2 makes n integral. D=(1,1,1,1,1,1) is a representative of the nontrivial class, because B(1,1,1,1)=2D whereas D fails condition (2).

## Theorem 2 — exact relative-loop and holonomy classification

Let D=(1,1,1,1,1,1); let r(x)=x-min_i(x_i)D be the joint three-STAR relative readout from R762GD. For a signed event word w, define n_j(w)= number of +Sj events minus number of -Sj events. Its full Cell displacement is Bn(w). The word returns to the same relative X6 state if and only if

    n0(w)=n1(w)=n2(w)=n3(w)=a, for some integer a.

The full displacement of that relative loop is **exactly 2aD**. Hence the allowed depth holonomy in this candidate event language is 2Z (not Z), the shortest nonzero relative loop uses four events, and its signed event-count vector is (1,1,1,1) or (-1,-1,-1,-1).

**Proof.** r(x+Bn)=r(x) is equivalent to Bn=kD. Since all six coordinates of Bn are n_i+n_j, the equations n0+n1=n0+n2=n1+n2, etc. force n0=n1=n2=n3=a. Therefore k=2a. Conversely those equal signed counts give 2aD. A word of length m must have m≥sum_j|n_j|=4|a|. Four events of distinct STAR types, all same transport sign, attain a=±1. These are ordered composite paths of 12 primitive steps, consistent with the earlier six-step primitive-coordinate D loop (R762GF) but living in a more restrictive event alphabet.

**Separation from rotation generation.** If the candidate transport alphabet includes only three of the four STARs, then its signed event-count vector has a zero component. The above relative-loop condition forces a=0. Thus *three STARs can generate A6 in the prior permutation-rotation candidate* (R762FY), while **no nonzero diagonal holonomy is achievable with only three STAR translations** in this independent composite-transport model. Rotational group generation and spatial event-lattice reachability are different properties.

## Theorem 3 — exact BRC return coefficients at all word lengths

Let every one of the eight signed STAR events have the same positive BRC weight 1/8, independently at each step. For integer m≥0 and a∈Z, let N_m(a) count ordered length-m source words with relative return and depth change 2a. Put u=max(a,0), v=max(-a,0). Then

    N_m(a)=0  unless m≥4|a| and m-4|a| is even;

and otherwise, with t=(m-4|a|)/2,

    N_m(a) = m! * sum_{t0+...+t3=t, tj≥0}
                    product_{j=0}^3 [1 / ((tj+u)! (tj+v)!)].

This is an integer multinomial count, and the exact BRC probability of that event is N_m(a)/8^m. Equivalently N_m(a) is the coefficient of x0^a x1^a x2^a x3^a in (sum_j(xj+xj^{-1}))^m.

**Proof.** For each STAR j, a signed count a requires n_j^+=t_j+u and n_j^-=t_j+v. Summing their eight letter multiplicities gives 4|a|+2sum t_j=m. Each valid allocation contributes the multinomial coefficient m!/product(n_j^+! n_j^-!). Theorem 2 identifies these and only these words as relative returns. No probability/sign cancellation enters this enumeration.

Exact values from the independent integer DP:

| m | depth Δh | ordered words for each Δh | all relative-return words |
|---:|---|---|---:|
| 2 | 0 | 8 | 8 |
| 4 | 0:168; +2:24; -2:24 | indicated separately | 216 |
| 6 | 0:5120; +2:1440; -2:1440 | indicated separately | 8000 |
| 8 | 0:190120; ±2:73920 each; ±4:2520 each | indicated separately | 343000 |
| 10 | 0:7939008; ±2:3729600 each; ±4:302400 each | indicated separately | 16003008 |

In particular P(Δh≠0 | relative return, m=4)=2/9 and for m=6 it is 9/25. All odd m have zero relative-return words.

## Exact native-relation interpretation and limits

This calculation supplies an **operator-scope counterexample** to reducing the candidate event dynamics to only the geometric rotation subgroup. Although the three-STAR rotation generators already cover A6, the four signed STAR translation types are needed for a nonzero diagonal holonomy in this explicit transport language. And a relative Cell observer loses the even-valued common-depth change of a four-event closed relative trajectory. Keeping the time-labelled signed BRC word and its event/source labels recovers it exactly; dropping those data requires a future-operation descent certificate.

The incidence lattice does not itself determine TRIADIC_CLOSURE_E, legal Link/Port updates or a general native force-balance law. The local cycle predicate is one P000-compatible candidate, not a Foundation/Working Truth promotion. If future native rules forbid any -S or constrain event order, Theorem 1 remains an integer *necessary lattice* statement, while the exact eight-branch BRC counts must be re-evaluated under the legal alphabet. Equally, the group-theoretic A6 result is about axis-label permutations, not a certificate of port legality.

## Validation and next research question

Companion R762GG_VERIFY.py uses Python standard-library exact integer arithmetic. It verifies all event-count vectors n∈[-2,2]^4, checks the opposite-edge/parity inverse against all x∈[-1,1]^6 satisfying the equations, checks the maximal-minor parity/index witness, and exactly enumerates the 8-branch BRC state distributions for m=0,...,10. Independent DP comparisons establish Theorems 2–3 on that finite range. Theorems 1–3 are proved for their stated infinite integer domains in the preceding arguments. Companion R762GG_EVIDENCE.json records full checked counts. **Independent review: NOT_REVIEWED**.

**Next question:** Obtain the frozen native TRIADIC_CLOSURE_E incidence and Port/Link transition predicate if it has been specified; otherwise develop a typed sign-and-orientation-sensitive legal gate as an explicit competing candidate. Test whether its admissible composite displacement lattice is B(Z^4), a sublattice, or something else, and whether the parity obstruction survives permitted link interactions. Independently preserve the q9 full-vector period/lift frontier, without inferring it from this signed candidate.
