# R1/N14 — Sharp minimax total-variation cost of a coarse two-law BRC observer

**2026-10-27. Author proof + exact BigInt and independent Python Fraction finite certificates.** This is an external finite strictly-positive weighted-path probability model, not a native P000/X6, independent Research Driver or Foundation result.

## Frozen sources and provenance

GLOBAL_KNOWLEDGE_V1 canonical \`main@3a8fabc201b48c4becd46d9aa16504c2d6247860\`: 00_BOOTSTRAP, OPERATING_MANUAL, project router, P000 original, matching P000 startup projection blob SHA1 \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\`, ACTIVE worldview, BRC/math/code/activity policies. Enterprise Math science input \`main@cda176e1a7f322e774553d0f3f89751cf5c3371b\`: AGENTS, PORTABLE_RESEARCH_PROTOCOL, joint-observer contract and original N=2 nonrepresentability witness \`research_notes/r1_n14_brc_observer_only_n2_sharp_20261027_r1/PROOF.md\`. The inherited gap \`1/36\` is prior input; the new result is the **sharp approximate error**, rather than another exact-impossibility claim.

Connected GitHub writer \`awdawmip\`, local author activity \`RA-R1-20261027-1256-TV72\`. Native task listing and dispatch: \`CONTROL_QUOTA\`; native researcher enrollment: \`STATIC_READONLY_SCOPE_DENIED\`, \`operation_sent=false\`. Active native owner and formal CLAIM unverified. This is independent author work, not a claimed task, accepted Result, or review.

## Scope and exact model

Let \`I,J\` be time-ordered symbols in \`{0,1,2}\`. Their first-symbol marginal is \`P(I=i)=Q(I=i)=1/3\`. The conditional P-rows for \`J=0,1,2\` are

    I=0 : 1/4,  1/4, 1/2
    I=1 : 1/12, 3/4, 1/6
    I=2 : 1/6,  1/2, 1/3

and \`Q(J=j|I=i)=r_j P(J=j|I=i)\` with \`r=(2,1,1/2)\`. All path weights are strictly positive; terminal likelihood ratio is \`r_j\`. The unconditional last-symbol rows are \`barP=(1/6,1/2,1/3)\` and \`barQ=(1/3,1/2,1/6)\`.

An unrestricted **common** history policy may stop and decide \`D∈{0,1}\` at times \`T=0,1,2\`. The fixed quotient has a root, one time-1 state forgetting \`I\`, and time-2 state \`J\`. Its common strategy uses only current state and fresh local coins (no persistent hidden selector). The observer is only \`(T,D)\`. The target full policy continues after \`I\` precisely when \`I=0\`, stops otherwise with \`D=0\`, and at \`T=2\` outputs \`D=1\` exactly when \`J=0\`. Thus, in outcome order \`(T1D0,T2D0,T2D1)\`, the full P law is \`(2/3,1/4,1/12)\` and the full Q law is \`(2/3,1/6,1/6)\`; all other categories have zero mass.

Define the two-law minimax approximation error (finite-distribution total variation)

    eps* = inf_{one common compressed strategy pi}
           max(TV(L_P^pi(T,D), L_P^full(T,D)),
               TV(L_Q^pi(T,D), L_Q^full(T,D))).

### THEOREM (sharp)

**For every allowed real randomized compressed strategy, eps >= 1/72. Equality is attained by a single rational common compressed strategy. Consequently eps* = 1/72 exactly.**

## Proof: all-policy lower bound

Write \`A={T=2,D=1}\` and \`B={T=2}\`. For any compressed policy, let \`a\` be its probability of continuing at the root and \`c\` its continuation probability at the single time-1 state, so \`m=ac=P(B)=Q(B)\`. Its time-2 decision probabilities are \`d_j∈[0,1]\`. Since reaching the second symbol is independent of the forgotten first-symbol identity,

    Q(A)-P(A) = m * sum_j (barQ_j-barP_j)d_j
              = (m/6)(d_0-d_2) <= m/6.

This includes **arbitrary root decisions and first-time decisions**. Therefore the observable linear functional

    F(P,Q) = Q(A)-P(A) - P(B)/6

is at most zero for every compressed policy. For the full target, \`F*=1/6-1/12-(1/3)/6=1/36\`.

We next prove a useful general **common-reach total-variation lemma**. Take arbitrary pairs of laws \`(P*,Q*)\` and \`(P,Q)\` on one finite observable space and events \`A⊂B\`, with \`P(B)=Q(B)\` and \`P*(B)=Q*(B)\`. Let

    eP=P(A)-P*(A), eQ=Q(A)-Q*(A),
    s=P(B)-P*(B)=Q(B)-Q*(B),
    eps=max(TV(P,P*),TV(Q,Q*)).

The TV characterization as maximum error over events, applied both to \`A\` and \`B\\A\`, yields

    |eP|<=eps, |s-eP|<=eps, |eQ|<=eps, |s-eQ|<=eps.

For any \`k∈[-1,1]\`, we claim \`eP-eQ+k*s<=2eps\`. If \`s>=0\`, then \`eP<=eps\` and \`eQ>=s-eps\`, giving \`eP-eQ+k*s<=2eps-(1-k)s<=2eps\`. If \`s<=0\`, then \`eP<=s+eps\` and \`eQ>=-eps\`, giving \`eP-eQ+k*s<=2eps+(1+k)s<=2eps\`. These two cases prove the lemma for **all** real law pairs, not for an enumerated strategy grid.

Apply the lemma with \`k=1/6\` and the above full/compressed law pairs. Since

    0 >= F(P,Q) = 1/36 + eQ-eP-s/6,

we get \`1/36 <= eP-eQ+s/6 <= 2eps\`, hence

    eps >= 1/72.

The use of common reach \`P(B)=Q(B)\` is essential here; applying unrelated single-law TV estimates would yield a weaker bound.

## Proof: exact rational attaining policy

Always continue at the root; at the unique time-1 state continue with probability \`1/3\`; if stopping there, output \`D=0\`. At time 2, use the common state-local terminal decision vector

    (d_0,d_1,d_2)=(1,1/4,0).

The two observer laws are precisely

    P_compressed=(2/3,17/72, 7/72)
    Q_compressed=(2/3,13/72,11/72).

Relative to their targets, each law changes two category probabilities by opposite \`1/72\` increments. Thus

    TV_P = TV_Q = 1/72.

Moreover \`Q(A)-P(A)=4/72\` exactly equals \`P(B)/6\`: this policy lies on the separating halfspace boundary. Equality proves minimax optimality among **all** allowed compressed policies. QED.

## Reproducible evidence and constraints

\`VERIFY.js\` uses exact reduced BigInt rational arithmetic, checks the strictly positive normalized 3x3 rows, all 13 labelled prefixes, terminal likelihood-ratio fibre, exact P/Q marginal distributions, full and attaining compressed observer laws, exact support gap and both TV values. It also checks all eight terminal decision cube vertices (complete for that **affine** contrast functional); universal stochastic optimization comes from the analytical argument above, not from vertex enumeration. \`RESULT.json\` is the literal output of the verifier as executed during this publication.

The independent local \`Python fractions.Fraction\` certificate checked the same values and yielded \`PASS_EXACT_FRACTION\`; extended PROOF/VERIFY.py/RESULT/NEXT_TASK and SHA256 manifest are also in the conversation evidence package. The GitHub \`VERIFY.js\` is independently executed BigInt code with its own reproducible source/output, not a claim that it has the same bytes as the Python program.

BRC resolution: \`REUSE_APPLIED\` to positive-weighted, port-labelled ordered mass flow and exact likelihood-ratio observer separation. Probability differences in F are not signed/complex physical amplitudes or cancellation claims. The result is only the stated fixed observer/model/horizon/class: no theorem about actual P000 six-axis Cell evolution, three-dimensional research slice, Heartbeat time, native triadic force balance, or RH. Native transfer requires an explicit full-X6 embedding, required third-coordinate semantics, readout, and preserved future operations. Review, formalization and prior-art novelty are unverified.

## Unfinished parent question

The broader structural problem (N>=3 uniqueness versus two incomparable minimal universally observer-sufficient recursive partitions) remains open. Quantitatively extend this sharp-TV dual method to the existing 40-prefix N=3 non-IID model, with true global joint-kernel feasibility rather than a finite grid; see NEXT_TASK.md.
