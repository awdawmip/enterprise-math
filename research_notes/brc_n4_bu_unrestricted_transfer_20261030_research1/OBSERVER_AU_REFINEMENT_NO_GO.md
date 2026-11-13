# AU-marked source-provenance refinement: strict exact minimax separation

2026-10-30. AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. Scope: external strictly-positive 16-leaf BRC N4 P/Q probability model, original instantaneous behavioral S2/S23 information sets. Not a P000 native-X6 or physical-time statement.

## Full exact model and theorem

Four time-two nodes have Q masses AU=1/6, AV=1/3, BU=1/4, BV=1/4; their two time-three likelihood ratios are AU=(9/10,11/10), AV=(1/4,1/4), BU=(1/5,9/5), BV=(2,2). Each splits equally again at time four. Every one of 16 P/Q leaf masses is strictly positive, and both laws sum to 1. Target F has stage-one continuation probabilities a=961/1000 on A and b=151/1000 on B, then continues AU only, stopping AV/BU/BV with Q, and deciding P at time three on AU. S2 equates the conditional time-two AU and BU action kernels; S23 also equates actions at later nodes with equal contemporaneous likelihood ratios.

The previously studied observer is O=(T,Decision,Z_BU), where Z_BU=1 only on BU paths reaching T>=3. Refine it to the full terminal quadruple O'=(T,Decision,Z_BU,Z_AU), with Z_AU=1 precisely on AU paths reaching T>=3. Let d'_2,d'_23 denote the infimal maximum of TV'_P and TV'_Q over all original S2/S23 policies with O' as the observable.

THEOREM: For the above a,b and original behavioral policy classes,

d'_2 = d'_23,
(7789-sqrt(50220529))/36000 <= d'_2 <= 151/4000,
d'_2 > 1/60 > sqrt(26521161)/15000 - 413/1250 = d_2 = d_23.

The lower bound equals 0.019509877487817944 approximately; the previously proved coarser observer optimum is 0.012924666557278792, whereas the lawful exact upper strategy gives 0.03775. This is a strict observable-source-provenance obstruction: old four-atom optimum cannot be transferred unchanged to the refined observer. The precise refined optimum between the bounds remains to be solved.

## Pathwise causal reduction survives refinement

On a quadruple o=(t,d,zBU,zAU), let K'(o)=(t,Q,0,0) for t<=2, and K'(o)=(3,Q,zBU,zAU) if t>=3 and zBU=1, otherwise K'(o)=(3,P,zBU,zAU). Target O'_F is K'-fixed under P and Q separately.

For any original S2 competitor G, preserve its stage-one and stage-two CONDITIONAL continuation kernels, replace earlier stopping decisions by Q, and stop every path reaching time three with decision Q on BU and P otherwise. Call the new actual strategy G^K. BU current likelihood ratios {1/5,9/5} at time three are disjoint from nonBU {9/10,11/10,1/4,2}, so the time-three rule is current-ratio-measurable and the resulting policy belongs to S23; the AU/BU time-two equality is unchanged. On each leaf and for L=P,Q,

Law_L(O'_(G^K)) = K'_push Law_L(O'_G).

Crucially K' retains BOTH surviving source bits on the collapsed time-three event; the time-four part is sent to the time-three target-compatible event, without erasing AU/BU provenance. Deterministic data processing and target fixity therefore yield

TV'_L(O'_F,O'_(G^K)) <= TV'_L(O'_F,O'_G), L=P,Q.

Since S23 subset S2, their minima coincide, and a lower bound over collapsed strategies is a lower bound over ALL original strategies.

## Four legal full-observer events yield a quadratic lower certificate

Write A,B in [0,1] for a collapsed competitor's first-stage rates and c in [0,1] for its shared *conditional* stage-two AU/BU continuation rate. The other AV/BV stage-two rates are arbitrary legal values. Let e=max(TV'_P,TV'_Q). Direct 16-leaf aggregation on four genuine full-observer events gives:

(1) Q event {T=1}: signed difference (a+b-A-B)/2, so |A-a+B-b|<=2e.

(2) P event {T=1}: signed difference (a+3b-A-3B)/4, so |A-a+3(B-b)|<=4e.

(3) P or Q event {T=3,Decision=P,Z_BU=0,Z_AU=1}: target mass a/6, collapsed candidate mass A*c/6; thus |a-A*c|<=6e.

(4) P or Q event {T=3,Decision=Q,Z_BU=1,Z_AU=0}: target mass zero, candidate mass B*c/4; thus B*c<=4e.

All four events are observable in O', with no hidden-label conditioning after the observation. Events 1-2 give by triangle inequality |B-b|<=3e, hence B>=b-3e. Event 3 gives Ac>=a-6e, and A<=1, c>=0 imply c>=Ac>=a-6e.

Suppose e<min(b/3,a/6). Then b-3e>0 and a-6e>0, so event 4 yields

4e >= Bc >= (b-3e)(a-6e),
18e^2 - (6b+3a+4)e + ab <=0.

At the exact a,b above the quadratic is

q(e)=18e^2-(7789/1000)e+(961*151)/1000000,

with discriminant 50220529/1000000 and smaller root

L=(7789-sqrt(50220529))/36000.

Exact radical order checks give 1/60<L< b/3 < a/6. If e<L, then the assumption e<min(b/3,a/6) is automatic but q(e)>0 (below the smallest real root), contradiction. Therefore every collapsed and every original legal competitor satisfies e>=L. This is an all-real-policy bound, not a sampling extrapolation.

For a direct rational contradiction, if e<=1/60, then B>=b-3/60=101/1000 and c>=a-6/60=861/1000. But B*c/4 >=86961/4000000>1/60>=e, contrary to event (4). Consequently d'_2>1/60. The coarser exact optimum E* satisfies E*<517/40000<1/60, so the strict observer separation is entirely exact.

## Matching a legal finite upper witness

Choose A=a, B=b, AU=BU conditional continuation c=1, AV=BV rates zero, stop at time three, decide P on AU, Q on BU. The stage-two AU/BU conditional kernels coincide, so this is lawful original S23. Under O' relative to target F, the only difference is BU mass b/4 moved from (T=2,Decision=Q,Z_BU=Z_AU=0) to (T=3,Decision=Q,Z_BU=1,Z_AU=0). Under both source laws its mass is b/4, hence

TV'_P=TV'_Q=151/4000.

This proves d'_2=d'_23<=151/4000.

## Executed certificate, sources and boundaries

The accompanying executable VERIFY_OBSERVER_AU.py uses exact Fraction arithmetic on all 16 strictly positive source leaves, verifies P/Q normalization and time-three ratio disjointness, both-law target K'-fixity, 40 generated lawful rational S2 policies x two source laws (80 exact pushforward and TV contraction comparisons), the 4 event inequalities, symbolic quadratic discriminant/root/order checks, and the exact P/Q upper strategy. Its actual console output is saved as VERIFY_OBSERVER_AU_EVIDENCE.txt; tests are implementation checks, while the universal argument is above.

The preceding same-PR PROOF.md composes two earlier author-side theorems at exact commits 1a4898a57e952245eeacb38be7adf109faa49f49 and d626df0a971cd19518303dd5bf4728daf478fcc6 to obtain the **coarser** full-original-policy value. For O', the deterministic K' remains a lawful lower-bound reduction, but the four old atoms split because AU source is now observed. No post-hoc minimax equality between observers is assumed.

Frozen GLOBAL_KNOWLEDGE_V1 main@f2889be41a071bfaea238c10d71e9a63915d4ebb; Enterprise Math main input@e69c62b9fbad1edb4cfc5cfeaad33b7a0e4de2a3; P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. GitHub actor awdawmip. Site returned research_authority_granted=false and current active owner is unverified; publication is source preservation, not CLAIM, native Result, independent review, admission or native X6/3D-slice/physical-time transfer.

Next exact problem: determine the sharp d'_2=d'_23 within [L,151/4000] using full five-observer-atom P/Q Farkas events or an attained algebraic S23 strategy; then test future readouts where stopping at T=4 participates in a new operation and K' may fail sufficient-state fidelity.
