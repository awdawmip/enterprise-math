# Euler routing from local first returns: duration–orientation coupling

Status: PROVISIONAL MODEL THEOREMS AND EXACT BRC CERTIFICATES; NOT FORMALLY ADMITTED.
Date: 2026-10-08 (Asia/Tokyo). Same-conversation continuation, not independent replication.
Global read snapshot: 8004ac0e3f369a2ff2f81d53202c56bb20eb1e21.
Source read snapshot: d6169e0d9a19408a677c9a5392dbff3cc1a09f66.
Prior frontier: 0cf19ae302ab4d147f9ef6c27038e4d137707725, research_notes/chatgpt_direct/20261007_EULER_GEOMETRIC_RETURN_SEMILINEAR.md, blob 3daf44d91460f9b80b9add946e20d5113c5fe0ae.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Research activity: UNVERIFIED / REGISTER_PENDING. No borrowed identity, CLAIM or mathematical admission.

## 1. Question, assumptions and actual reuse

The preceding unit selected simple triangular or square comparison returns in advance. This unit instead selects only the next comparison edge and stops an excursion at its FIRST positive return to its base. No target persistence parameter is fitted.

The sourced K4 comparison graph has four vertices; each vertex has three neighbours. Its six edge bits transport the sheet by s_j=s_i XOR e_ij. The comparison vertices are not native X6 positions. Edge count, completed-excursion/contact count and calibrated physical time are distinct types. A two-edge retracing comparison is not a primitive two-force balance. P000, six native spatial axes, independent time and three-dimensional slice typing are unchanged.

Declared new ordinary-walk program: choose each adjacent comparison edge with positive weight 1/3, freshly and independently of channel/sign/history; allow immediate reversal; stop at the first positive return to the fixed base. This equal-neighbour law is equivariant under graph relabelling. It is forced only after assuming a memoryless local choice that distinguishes none of the three neighbours. It is not derived from native force or bare incidence. The return boundary, collision/transport ordering and use of a single comparison walker are also explicit modelling choices.

Before departure apply the unchanged local collision P^chi, where P(a,b,f)=(f,a,b), and then transport the same sheet along the generated path. There are no further channel collisions before the return. At the endpoint the macro is C_h(x,chi)=(P^chi x,(-1)^h chi). The previously proved E=C_0, O=C_1 and their semilinear observers are consumed, not claimed again as new discoveries.

Actual reuse: the supplied prior archive euler_geometric_routing_evidence.zip has SHA256 0775a747f5f38c7c195c6159611c7bf75df52dc1e5b50d193f46bdf331fc0812. All 23 entries of its own manifest were verified. Ten unchanged dependency modules are used. brc_route_memory.py remains SHA256 ce182a5861982d0e43120aeb15da06cf02c774300730975330a85ea86f3c979e. Its contact function executes the existing cyclic update, provenance and positive CWM serial operations. Each new comparison edge executes the inspected source transition_bit and existing cwm_edge/cwm_propagate; aggregation executes cwm_recoalesce. The complete stored brc_weighted.py is Git blob 3f205696709e847909958a153f8fe10d3f6b70f0, equal to current Source. The unchanged inspected chirality excerpt is bound to full Source blob 6f8b147c094720c2749f620a40394c4d7b67a386, not represented as the entire module.

REUSE_EXECUTED / COMPOSE_APPLIED / EXTEND_EXISTING_TOOL. No new accepted BRC family. All explicit paths retain root, positive weight, channel/sign, comparison vertices and contact history. Current/previous vertex are retained when queried by the policy. No numerical pi, trigonometry, roots, matrix exponential or alternative numerical world propagator is used. Finite rational/polynomial calculations below certify the actual BRC rows; signed hitting functions and phase coefficients are not positive mass.

## 2. First-return length and sourced parity

Let L be the number of comparison edges until the first return. The first edge necessarily leaves the base. Thereafter, conditional on not yet returning, exactly one of three choices returns and two remain outside. Hence

Pr(L=l)=(1/3)(2/3)^(l-2), l>=2;
Pr(L>M)=(2/3)^(M-1), M>=1;
E[L]=4.

These are normalized endpoint-mass statements about an unbounded family of finite paths. At each finite l there are 3*2^(l-2) first-return paths of individual weight 3^-l. At cutoff M there are 3*2^(M-1) unfinished paths. The stopped plus unfinished total mass is exactly one. The tail tends to zero, proving almost-sure termination under this program without pretending that all branches finish at a common finite edge count.

In the sourced all-negative class, e_ij=1 on every edge. Therefore h=L mod2. The formal LENGTH generating functions for even/odd returns are

R_0(u)=3u^2/(9-4u^2),
R_1(u)=2u^3/(9-4u^2).

They sum to u^2/(3-2u). Their variable u records comparison-edge length, not phase or a physical time coordinate. Summing positive BRC path masses gives

Pr(h=0)=3/5, Pr(h=1)=2/5.

Thus the completed-excursion channel/sign mass law is exactly the old contact(p) endpoint law at the DERIVED value p=3/5, rather than p=0 from the previous equal-simple-triangle program. Under fresh independent local edge choices, successive excursions have this law conditional on the retained input sign. The signs themselves are correlated; they are not independently fair at each contact.

The conditional mean lengths are

E[L|h=0]=18/5, E[L|h=1]=23/5.

Consequently return duration and orientation action are not independent. A single p, even supplemented with mean duration four, loses operative information.

For the preceding relational phase y, the exact length-resolved first-return observer is

B(u)y=R_0(u)*omega*y+R_1(u)*omega^2*conjugate(y),

where omega^2+omega+1=0. Evaluation at u=1 preserves completed-macro endpoint masses but discards their length relation. This is a semilinear observer of actual path transport, not an extra native plane or complex mass.

## 3. Complete ordinary-walk parity classification on the sourced graph

For any edge assignment and base b, fix a comparison gauge with all three base edges zero. Let k be the number of negative edges among the other three vertices; equivalently, k is the number of odd triangular faces incident to b. Only this k matters for the rooted ordinary-walk return ratio.

A signed hitting certificate r_j, with r_b=1, satisfies

r_j=(1/3) sum_(v != j) (-1)^e_jv r_v, j != b.

Its right-hand side uses the actual generated BRC edge rows. On the three nonbase variables its sup-norm contraction factor is at most 2/3. Hence a bounded certificate is unique and equals the expected return-parity sign. The first-edge expectation is (1/3) sum_(j != b) (-1)^e_bj r_j. Positive even probability is one half of one plus this expectation.

In the gauge with zero base edges, the solution is:

k=0: all three values 1;
k=1: values 2/5 at the endpoints of the negative edge, 3/5 at the other vertex;
k=2: value 0 at the vertex incident to both negatives, 1/2 at each other vertex;
k=3: all three values 1/5.

Therefore the exact p_even values for k=0,1,2,3 are

1, 11/15, 2/3, 3/5.

Across all 64 source assignments and four bases, their counts are 32,96,96,32. Each certificate was checked through actual edge rows and by stopped-prefix plus pending-hitting-mass identities. All sixteen vertex gauge changes preserve the return ratio. A gauge transformation changes the nonbase hitting signs by the appropriate endpoint factor, not the closed-return probability.

This classifies this local WALK policy, not every physically admissible path family. It does not infer source comparison bits from bare incidence and does not tune them to reproduce an externally selected p.

## 4. Incoming-edge memory is a real alternative assumption

Compare the ordinary policy with a nonbacktracking policy: after the first edge, choose equally among the two neighbours OTHER than the vertex just left, and stop at the first return. The previous vertex must be retained. This is a distinct local, relabelling-symmetric law, not an optimization of the same dynamics. Only this single-excursion comparison is asserted; no hidden reset of arrival memory between repeated nonbacktracking excursions is assumed.

A return cannot occur before edge three. After the second edge, one of the two allowed choices returns to the base and the other stays outside. Thus

Pr_NB(L=l)=2^(-(l-2)), l>=3;
Pr_NB(L>M)=2^(-(M-2)), M>=2;
E_NB[L]=4.

In the SAME all-negative comparison field,

R_0^NB(u)=u^4/(4-u^2), R_1^NB(u)=2u^3/(4-u^2),
p_even^NB=1/3,
E_NB[L|even]=14/3, E_NB[L|odd]=11/3.

Both policies have the same graph, the same comparison bits and the same mean return length four, but p_even is 3/5 versus 1/3. Thus symmetry and average length do not choose a routing law. Whether an incoming relation allows immediate retracing is a concrete remaining native obligation. The ordinary-walk state key (current,sign) is insufficient for the nonbacktracking policy, which queries the previous vertex.

## 5. Completed contacts and primitive comparison-edge observations differ

For ordinary first-return excursions in the all-negative class, the endpoint phase at completed contact index n satisfies the previous local law evaluated at derived p=3/5:

zeta_(n+2)=-(3/5)zeta_(n+1)-(1/5)zeta_n.

With an initially fixed channel triple and independent fair sign, the normalized first factors are 1,-1/2,1/10,1/25,-11/250. This is an embedded completed-contact clock, not physical time and not the number of comparison edges.

Define instead one primitive EDGE update: if currently at the base, first execute the existing collision with the carried sign; then choose and traverse one comparison edge. Away from the base, only traverse one comparison edge. Upon arriving at the base, no extra collision occurs until the NEXT departure. Every edge is a supported sourced comparison relation. The finite full-state key is (binary channel triple,carried sign,current comparison vertex). In the unit-count sector it has at most 24 states. There is no alternating recipient scheduler; the collision/departure boundary is nevertheless a specified programme, not a calibrated heartbeat.

Let G_+(u),G_-(u) generate the laboratory phase multiplier for initially positive/negative signs, starting at the base before a collision. Let S(u)=sum_(t>=0) Pr(L>t)u^t=(3+u)/(3-2u). First-return decomposition of actual BRC paths gives

G_chi=1+omega^chi*[S-1+R_0 G_chi+R_1 G_-chi].

The first-contact phase remains unchanged during an unfinished excursion; R_0/R_1 route the returned sign. This equation retains the duration–parity dependence. It uses formal generating polynomials for exact path counting, not a numerical propagator or trigonometric series.

Elimination gives the common denominator 9-u^2+u^4. More explicitly, the numerator of G_+ is

9+9omega*u+(-1+9omega)*u^2+(2omega-3)*u^3,

and G_- is its conjugate. Consequently, for ANY normalized initial joint channel/sign preparation AT THE BASE, each phase coefficient obeys

9*zeta_(t+4)=zeta_(t+2)-zeta_t, t>=0.

For an initially fixed triple and fair independent sign, zeta_t=c_t*zeta_0, where

sum c_t u^t=(18-9u-11u^2-8u^3)/(18-2u^2+2u^4),
c_0=1, c_1=c_2=c_3=-1/2.

The first factors are

1,-1/2,-1/2,-1/2,-1/6,0,1/27,1/18,11/486,...

Thus a nonzero initial phase gives EXACT zero at edge five and nonzero phase again at edge six. Replacing the random return length by its mean gives the wrong result already at edge four: the actual factor is -1/6, not the one-completed-contact factor -1/2.

There is also a simple uniform convergence certificate without numerical roots. For either parity subsequence, s_(n+2)=(s_(n+1)-s_n)/9. If |s_n| and |s_(n+1)| are at most B, the next two values are at most 2B/9 and 11B/81. Therefore the paired sup norm contracts by at most 2/9 every four comparison edges. Since every binary triple has phase coefficients bounded by one, for total positive mass W and initial support at the base,

||zeta_t||_infinity <= W*(2/9)^floor(t/4).

This proves convergence of THIS phase even though a finite zero is not absorbing. It does not erase path history or identify positive mass with amplitude. At each finite edge count, a single unit branch has CWM=(3^t,1,3^-t), including unit-weight boundary contacts.

## 6. Same complete waiting distribution and same p still do not suffice

Make a deliberately different renewal preparation with the SAME distribution of L and the SAME parity marginal p=3/5, but choose the parity independently of L. This is an auxiliary BRC countermodel, not a sourced transport law: the real all-negative source requires h=L mod2.

At primitive edge three, only the paths whose first excursion had length two have begun a second contact. Their weight is 1/3. In the real source, all these returns are even, so both one-contact and this two-contact subpopulation have fair-initial factor -1/2. The actual total factor remains -1/2.

The independent-duration countermodel gives the two-contact factor 1/10 to that subpopulation. Its edge-three factor is

(1/3)(1/10)+(2/3)(-1/2)=-3/10,

differing by zeta_0/5 from the true phase. This finite witness was checked with actual old BRC contact outputs and the generated first-return masses. Matching the complete marginal waiting-time law and the marginal endpoint kernel still does not match their JOINT law.

## 7. Truncation, unfinished mass and the infinite-path type boundary

At cutoff M the unreturned positive mass q_M=(2/3)^(M-1) must remain explicitly unresolved, not be silently interpreted as disappearance or an already completed contact. The eventual even mass lies between the stopped-even mass and stopped-even plus q_M. More refined signed hitting certificates close this interval exactly in the mass-only interface.

An especially deceptive cutoff is M=3. The completed masses are 1/3 at length two and 2/9 at length three; unfinished mass is 4/9. Renormalizing completed paths produces the CORRECT parity ratio 3/5 but the WRONG conditional mean length 12/5 instead of four. Indeed every odd cutoff M>=3 has exactly the same 3/5 conditional parity ratio. Endpoint agreement at such a cutoff does not certify the return-time law or intermediate trajectory.

For a general bounded phase observer with coefficient magnitude at most one, conditioning on completion by M differs from the full completed-excursion expectation by at most 2q_M per coefficient. This follows from full law=(1-q_M)*conditional_completed+q_M*conditional_tail. For N freshly chosen ordinary excursions, a pathwise coupling gives total-variation error at most 1-(1-q_M)^N <= N q_M for their completed word law. These are stated horizon bounds, not an all-time guarantee and not authority to drop fields or history-sensitive controls. The all-negative parity endpoint may agree exactly despite nonzero full-path error.

There are infinitely many distinct finite first-return paths, although their total weight is one. Their all-return path count is therefore infinite and is NOT stored as an ordinary finite CWMState. The effective p=3/5 contact representation preserves the specified endpoint mass/phase law only; its finite one/two alternative counts and largest branch weights are not the original loop multiplicities. Actual code keeps finite stopped prefixes plus finite pending states, and the exact infinite result is justified by the finite harmonic identities and the vanishing tail. No infinite execution is claimed.

## 8. Executed evidence and remaining obligation

Final suite passed 136488 exact assertions, including 23 prior-manifest integrity checks. Coverage: all 64 edge assignments at all four bases; all 16 vertex gauges; exact harmonic and prefix/pending certificates through 16 edges; all 16 binary channel/sign atoms at four bases with explicit first-return paths through six edges; all-negative nonbacktracking paths and return laws; generating certificates through 50 edges; all 64 base/atom starts through 48 primitive edges; four-base explicit full-history/finite-state CWM equality; recorded inverse-channel recovery; contact-index/edge-clock discrepancy and cutoff witnesses.

Actual existing source calls: cwm_edge 289619, cwm_propagate 394508, cwm_recoalesce 262267; old contact 8960; sourced transition_bit 245829, face_holonomy 768, gauge_action 4096. These are assertion/function counts, not independent experiments. The first complete suite already passed; only the prior-integrity read was changed from an extracted workspace path to the bundled archive so the final package runs standalone. The unchanged scientific suite was then rerun and passed. This is packaging revalidation, not independent replication. An unrelated terminal-environment warning in the developmental log is retained.

Run python check_first_return.py with standard-library Python3.10+ from the supplied directory. The package includes the new extension and checker, exact ten-module dependency tree, finite certificates and prior archive for integrity verification. Source publication of this proof records its scientific frontier; it is not a claim that every executable attachment byte is also stored there or formally admitted.

Primary background: Grünbaum and Velázquez, A generalization of Schur functions: applications to Nevanlinna functions, orthogonal polynomials, random walks and unitary and open quantum walks, arXiv:1702.04032 (official abstract on first-return generating functions and renewal equations); Lev-Ari et al., Analytical results for the distribution of first return times of non-backtracking random walks on configuration model networks, arXiv:2412.12341 (official abstract on the incoming-edge exclusion rule). No theorem from an unread paper is used to derive the finite K4 formulas, no numerical reference propagator is run, and no literature-wide novelty is claimed.

Own read-only control request is private bridge #3005, status-20261008-euler-first-return-21. The reply was obtained. It establishes no new verified Source-bound activity, mathematical acceptance or final-guard success. The prior failed registration remains provenance only; no duplicate registration, rejected-prerequisite replay, old safety-blocked payload, borrowed CLAIM or new role identity was used.

Completed new unit: local rather than whole-loop choice; exact rooted first-return parity classification; incoming-edge-memory comparison; duration–orientation joint kernel; primitive-edge Euler recurrence and zero/reappearance; explicit unfinished-mass and cutoff bounds. The next native obligation is to determine whether the actual incoming-channel grammar permits immediate retracing, and where its contact boundary lies. Equal local weights and independent edge choices also need that source. The finite comparison graph alone does not determine these assumptions. These results are not yet an X6 force, length or physical-time law.
