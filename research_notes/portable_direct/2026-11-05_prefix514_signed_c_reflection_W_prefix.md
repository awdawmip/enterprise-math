# PREFIX-514 — Signed c-axis reflection and exact BRC W-prefixes

2026-11-05. Author-side status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Researcher-ID: EM-X6-2241FD. Research activity: RA-99EFFA0D8F76D92C1E71C86B.
Formal task: RS-X6-NATIVE-ROTATION-DYNAMICS. No formal CLAIM or Result is asserted.

## Sources, objects and exact scope

This continues PREFIX-513 and the predecessor PREFIX-511–512 single-displacement fibers. The task-frozen scientific input remains f42f2906d77f24085c123f3ccfe9667d41caa96d; the separate formal task publication TP2-6A1F9D8C2047E3B51C01 preserves its own scientific refs at a72226e2430ffa4786321ac86e7f0c599d5f0389. Current behavioral rules were read separately from the Global Knowledge and Enterprise Math current-main records.

Study a five-axis **restricted native signed-X6 path family** (ten signed directions a,A,b,B,c,C,d,D,e,E) embedded in the six-axis Heartbeat World, not a replacement of six-dimensional native space. The KMP color word uses a=0, A=4, b=1, B=2, c=C=3, d=D=e=E=4. Gates are aab and aba. Preserve the order-sensitive first-source tag t: first b/B step -> B, first c/C step -> C; preserve final KMP state q. BRC cancellation pairs p_a,p_b,p_c,p_d,p_e record observer coordinates V=p_b+2p_d+p_e and W=p_c+p_e. They do not exhaust native path provenance and do not imply an operation-safe physical quotient.

Let m be any nonnegative integer, n=2m+1, and either target displacement
    y=(0,0,+1,0,0) or y=(0,0,-1,0,0).
There are m cancellation pairs in total. The surplus c/C primitive is the only sign-dependent step.

## Theorem 1: exact sign-reflection involution

For any length and fixed displacements in the four other axes, swap all c and C native steps throughout each ordered word. This is an involution from target y_c to target -y_c and preserves V,W,q,t exactly; in particular the two stated c-single-displacement fibers have identical joint (V,W,q,t) supports for every m and both gates.

Proof: every old c-axis signed coordinate and its increment acquire a minus sign, so the cancellation predicate old_coordinate*increment<0 stays invariant. Pair counts and both BRC readouts therefore stay unchanged. The c and C KMP colors coincide (both 3), hence their entire KMP color sequences and final states coincide. First source is determined by b/B versus c/C, which also does not change. Reflection is invertible, giving equality, not merely equal cardinality. This equivalence is scoped to the stated observer and is not a claim about orientation-sensitive future operations. QED.

## Theorem 2: occupation-support interval with constructive witnesses

For nonnegative integers A,B, imposing p_a>=A and p_b>=B yields precisely the integer points

    0 <= W <= m-A-B,
    B <= V <= 2m-2A-B-W.                                  (1)

An impossible upper bound means an empty fiber. There are no internal V holes. Fix W and write p_a=A+h, p_b=B+u, p_c=W-e, p_d=v, p_e=e, with 0<=e<=W and h+u+v=H=m-A-B-W. For each e, u+2v ranges through every integer 0,...,2H: choose u=z,v=0 when z<=H; otherwise v=z-H,u=2H-z. Adding e=0,...,W yields every integer from B to B+2H+W. Conversely every pair vector satisfies (1). Pair budgets admit signed ordered native paths for either sign of the unpaired c step. QED.

## Theorem 3: complete KMP/first-source threshold table

Each row (q,t) has support exactly (1) for the corresponding (A,B):

| Gate | B:q0 | B:q1 | B:q2 | B:q3 | C:q0 | C:q1 | C:q2 | C:q3 |
|---|---|---|---|---|---|---|---|---|
| aab | (0,1) | (1,1) | (2,1) | (2,1) | (0,0) | (1,0) | (2,0) | (2,1) |
| aba | (0,1) | (1,1) | (1,1) | (2,1) | (0,0) | (1,0) | (1,1) | (2,1) |

Necessity: KMP final states require suffixes q1=a, q2=aa (aab) or ab (aba), and q3=the complete gate. Required positive a letters each demand a paired a/A occurrence; required positive b letters each demand a b/B pair, because the b displacement is zero. For source B at least one b/B pair is needed, while source C is always available from the unpaired c/C step. These give the threshold pairs.

Sufficiency: To realize C as first source, place the surplus c/C step first. To realize B as first source, put a negative B first (available when p_b>=1) and the surplus c/C step later. Put all unreserved primitives ahead of the desired KMP suffix. For q2 and q3 reserve the required positive-letter suffix aa, ab, aab, or aba; for q1 reserve an a and use the paired negative A or the surplus c/C before it to avoid the aab aa suffix. For B:q0 finish with surplus c/C, which is KMP non-prefix color. For C:q0 with m>0, finish with any negative paired primitive, also a non-prefix color, after the initial c/C; for m=0 the lone surplus c/C itself gives q0,C. This realizes every occupation vector satisfying the listed thresholds, while preserving exact first-source order. No provenance classes are merged. QED.

## Corollary: constant arithmetic W-prefix

For an integer W prefix cut j, counting W<j, define

    J=max(0,min(j,m-A-B+1))
    P_AB(j)=J*(2m-2A-2B+1)-J*(J-1)/2.                     (2)

For a gate, sum the eight P_AB terms of Theorem 3. This is the exact count of distinct joint states (W,V,q,t) below W<j, using O(1) exact integer arithmetic operations for fixed gate, not O(1) bit complexity. Indeed each W row has 2(m-A-B)-W+1 integers and sum (2) is an arithmetic progression.

Set Phi(h)=(h+1)(3h+2)/2 for h>=0, otherwise Phi(h)=0. The total number of joint states for **each** c sign is

    S_c(aab,m)=Phi(m)+2*Phi(m-1)+2*Phi(m-2)+3*Phi(m-3);
    S_c(aba,m)=Phi(m)+2*Phi(m-1)+3*Phi(m-2)+2*Phi(m-3). (3)

The eight (q,t) populations remain distinguishable. At m=4 (n=9), totals are 118 (aab) and 125 (aba) for either sign. At m=6 (n=13), totals are 308 and 321.

## Exact executed verification

The accompanying Python 3 program prefix514_signed_c_prefix_certificate.py is an executable exact-integer certificate. It independently generates native ten-direction ordered-step DP states, preserving signed position, KMP and earliest source, for n=1,3,5,7,9,11,13, BOTH target c signs and BOTH gates. It compares each (W,V,q,t) support and full prefixes. It also independently enumerates every five-occupation composition for 0<=m<=12, checking each threshold row, and checks m<=100 prefix equalities.

Observed output: PREFIX514_EXACT_EXECUTION.json, status ALL_CHECKS_PASS; native_rows_checked=112; native_joint_state_memberships=2942; native_prefix_equalities=252; native_sign_reflection_equalities=14; occupancy_composition_checks=208; long_range_formula_checks=11312. Each count is a defined exact finite test, not universal numerical inference. The universal claim uses the three constructive arguments.

## Four-sign family / retained mother question

PREFIX-512 treats y_b=+1, PREFIX-513 treats y_b=-1. This paper resolves y_c=+1 and y_c=-1, closing the four cases |y_b|+|y_c|=1 **inside the declared restricted BRC/KMP model**. The broader X6 native signed triad C6 generator, group closure and operation-safe path-composition problem remains open in the formal task.

Next PREFIX-515: select a nontrivial allowed native operation on ordered paths (composition, reversal, or a typed triadic update) and test whether the c-sign reflection commutes with it after the stated observer. Produce either a precisely typed operation-preserving lift or a minimal counterexample showing information discarded by the quotient. Preserve the exact signed-source provenance and frozen task science.

References: applicable current P000/ACTIVE and docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; docs/PORTABLE_RESEARCH_PROTOCOL.md; research_priorities/research_method.json; previous PREFIX-508, 509, 511, 512 and 513 notes under research_notes/portable_direct.
