# R762GL — Fixed Port incidence breaks the three-STAR all-horizon BRC equivalence

Research date: 2026-11-20 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Frozen scientific P000 input: a72226e2430ffa4786321ac86e7f0c599d5f0389. Frozen taskbook: 857280d1012943290d141d1317179c40ec3cbdf8. Antecedent R762GK: PR #2824 @ 4451b4a4320a9b739008f0f2051d83b99dacefab. Historical Researcher attribution EM-X6-3050F6; this paper does not assert current CLAIM or session possession. Author-side exact proof / finite checks PASS. Review NOT_REVIEWED. This is a CANDIDATE typed gate, not an adopted native TRIADIC_CLOSURE_E permission rule.

## I. Precise model

Retain R762GK's candidate group G = Z^6 semidirect A6 with composition (x,p)(y,q)=(x+p*y,pq). The six axes are tetrahedral edges [01,02,03,12,13,23]. STAR S_v is the ordered triple of edges incident on vertex v. Define H_v as its three-axis indicator, g_v as the three-cycle of that ordered triple, and T_(v,s)=(s H_v,g_v^s) for signed s in {+1,-1}. Since g_v H_v=H_v, the two signed events are inverses. For omitted vertex a, the ungated model uses all six signed letters at the three vertices different from a.

Fix the externally *named* Port/Link edge e={0,1}. Define a deliberately minimal incidence license

    Permit_e(v,s) iff v belongs to e.

Thus a word in omitted-STAR model a is accepted iff each of its letters lies in A_(a,e)={(v,s):v != a, v in e, s=+1 or -1}. The marked edge identity is held fixed across compared omissions; changing the name of e is not equality in this fixed-frame problem. Preserve the complete ordered signed word, Port/Link names, branch multiplicity and provenance; the affine product is only an endpoint observation.

For m>=0 and integer k, let C_(a,e,m)(k) count accepted *ordered* m-letter histories whose complete affine product is (kD,id), with D=(1,1,1,1,1,1).

## II. Fixed-edge two-orbit theorem

For every m>=0 and a in {0,1,2,3}:

(A) If a is an endpoint of e, exactly one STAR survives and the accepted alphabet has 2 signed letters. Otherwise exactly two STARs survive and the alphabet has 4 signed letters.

(B) Every nonzero diagonal-depth coefficient vanishes: C_(a,e,m)(k)=0 for k != 0.

(C) For a in {0,1}, C_(a,e,m)(0) equals binomial(m,m/2) when m is even, and equals zero for m odd.

(D) At m=2, C_(a,e,2)(0)=2*|e\{a}|. It is 2 for omissions 0,1 and 4 for omissions 2,3. At m=1 no full diagonal return exists; thus m=2 is the earliest separating *full-return count* horizon.

(E) The stabilizer of the fixed named edge inside the Klein four group K of R762GK is K_e={id,(01)(23)}. Its two orbits on omitted vertices are {0,1} and {2,3}. The existing affine word automorphism maps the entire accepted language for a=0 to that for a=1, and likewise a=2 to a=3, with sign reversal. Consequently within each orbit the full diagonal-return law is equal at every horizon. Equality *across* orbits is false by (D).

**Proof.** The permitted STARs are subsets of {S_0,S_1}. Their union uses axes {01,02,03,12,13}, never axis 23. Every permitted translation has component 23 equal to zero, and all corresponding cyclic axis permutations fix 23. By induction on the semidirect product the 23 displacement remains zero. Hence (kD,id) requires k=0, proving B. A follows by direct intersection with the endpoints of e. If only one vertex v is allowed, every m-letter word has group product T_(v,+)^j where j is the net number of plus minus minus letters; its translation is j H_v. The identity requires j=0 and there are binomial(m,m/2) such words, proving C. At m=2, each first letter T_(v,s) has exactly one permitted inverse T_(v,-s); no generator at a different vertex is an inverse because its nonzero H_v is distinct. Hence the number of full returns equals the alphabet size, proving D. Finally only id and the double transposition (01)(23) fix the unordered edge {0,1} among K. That double transposition swaps omissions 0<->1 and 2<->3. The previously proved R762GK automorphism sends each T_(v,s) to T_((01)(23)v,-s), preserving the fixed-edge incidence license. It is an invertible letter-by-letter map compatible with the full affine product; since it sends D to -D, it preserves zero-depth full returns, proving E. QED.

Under independent uniform BRC selection **from admitted letters**, the m=2 full-return probability is 2/2^2 = 1/2 for omissions 0,1 and 4/4^2 = 1/4 for omissions 2,3. Under independent selection of the original six letters with probability 1/6 and **discarding rejected words**, the corresponding accepted-return masses are 2/36 and 4/36, respectively. These are different sampling rules and must not be conflated.

The endpoint fibre has a concrete named relation residue. For omission a=2, the histories T_(0,+) T_(0,-) and T_(1,+) T_(1,-) have the same full product (0,id), but are distinct Port/Link histories. Under omission a=0, only the second remains admissible. An endpoint-only quotient thus loses information needed to test this gate.

## III. Typed-gate equivariance sufficient criterion

Let S be a **complete typed joint state space** that can include Cell chart, signed primitive-force triples, named Port/Link relations, time/order and BRC branch memory. Let L(s,t) be admissibility of signed candidate event t, U(s,t) its deterministic update when admitted, and O:S->Y the scoped observation.

Fix an R762GK symmetry q with its invertible letter map F_q. Suppose there exists a bijective typed-state relabeling Psi_q:S->S and a readout relabeling rho_q on Y such that, for all reachable s and all t,

1. L(Psi_q(s),F_q(t))=L(s,t);
2. when L(s,t)=1, Psi_q(U(s,t))=U(Psi_q(s),F_q(t));
3. O(Psi_q(s))=rho_q(O(s));
4. the initial states are related by Psi_q.

Then **for every finite horizon** the map F_q on ordered signed histories is a bijection of admissible words, transports complete joint states via Psi_q and observations via rho_q, and preserves the exact BRC probability law if per-letter weights are transported under F_q (in particular, equal uniform weights work).

**Proof.** The related initial states give the induction base. If accepted prefix states correspond under Psi_q, condition 1 makes the mapped next letter admissible, and condition 2 maps the next states. Iterate to any finite length; condition 3 transports the observation. Apply the inverse bijections to obtain both directions and preserve the signed histories, multiplicities and products of transported weights. QED.

This is a **sufficient** lift certificate, not a claim that failure to find such a lift *necessarily* causes unequal scalar statistics. The fixed-edge gate above provides an independent exact counterexample when the named relation is not transported by a larger symmetry.

## IV. Exact verification and bounds

The standard-library exact-integer checker R762GL_VERIFY.py implements signed affine multiplication, all four omitted models, the K_e stabilizer and the full word multiplicities. Dynamic programming enumerates accepted event paths through m=10. An independent direct word-by-word enumeration checks the one- and two-STAR branches at m=2,4,6,8.

At m = 0,2,4,6,8,10 the full zero-depth-return counts are:
- Omissions 0 and 1: 1, 2, 6, 20, 70, 252.
- Omissions 2 and 3: 1, 4, 28, 232, 2092, 19888.

All nonzero diagonal-depth counts are zero in this range. The general formulas and orbit statement are proved for **all m**, not inferred from finite checks. Finite verification checks implemented conventions and the declared range only. No independent mathematical review, formalization, or real native license test has been performed.

## V. Relation to P000 and next scientific question

The gate is a hypothetical **named relationship license**, not a primitive physical two-force balance. Each signed STAR event remains a composite three-axis path candidate over native X6, and no statement here replaces P000's primitive arity three, PERP_E=120 degrees, six-axis Cell torsor or separate time dimension. Full BRC path/Port/Link provenance remains available; no universal safe quotient is asserted.

The prior R762GK all-horizon ungated equality survives a native triadic relation only after checking the **actual typed gate lift**, rather than assuming coordinate symmetry alone. Next: read the frozen actual TRIADIC_CLOSURE_E licensing definitions if they exist, type the native Cell/force/Port/Link/time update, find its symmetry stabilizer, and either exhibit an actually licensed minimal distinguishing word or prove a scoped typed all-horizon lift. If the license is still open, compare exact candidate triadic incidence predicates before any canonical promotion. The separate ungated shortest-depth problem L(k) remains open.

Source artifacts: R762GL_VERIFY.py and R762GL_EVIDENCE.json. Review: NOT_REVIEWED.
