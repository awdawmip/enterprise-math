# Recovery: fixed moments plus finite observation history do not close the X6 candidate

Event: `NS-NATIVE-JOINT-HISTORY-20260909-D5C00D-13`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Status: **Recovered prior ordinary proof and executed-result record; not re-executed as new research, not independent review, not force/NS admission.**

This is the separately delivered JOINT-HISTORY event13, NOT the already recorded EVENT-CAPACITY event13. The mounted package was checked before recovery. Its original proof SHA256 is `8ace719ce11bc595ff0f922b371b39c419bde0f2fd4e9df4c3b4d55cd47c91fe`; original checker SHA256 is `d6eb4468a5ccc16f3b3570041ff94f958aef94ea78f6f2947998512a2747382c`; original result SHA256 is `b043d70c8ae72c0289d1ddde77b1b4af4c08aff692db28f992335330a04c8070`. This readable recovery preserves the mathematical frontier, while the original full checker/dependency package remains in the delivered download. This record does not claim that its three previously missing standalone code files were remotely installed.

## 1. Exact law and observer

Keep X6-DENSITY-PORT-1 and the fixed-Gamma veto unchanged: local state C_l(j,s)={s e_j,+e_l,-e_l}, j!=l, proposes the unique largest neighbor-total axis among the four axes outside {j,l}; only then accept it when {j,l,m} belongs to Gamma. Ties/vetoes do nothing; every particle then streams one signed native unit step. Gamma is a declared constitutive candidate parameter, not a primitive-force certificate.

Let

    B=[[1,1,1,1,0,0],[1,-1,0,0,1,1],[0,0,1,-1,1,-1]],
    r=Bz, h(z)=(z4,z5,z6).

Full z is native Cell identity; r is a lossy carrier readout. For finite channel fields define O_p to retain every array

    M_{v,alpha}(r;n)=sum_{Bz=r} h(z)^alpha n_v(z), |alpha|<=p.

This keeps all carrier positions and signed channels, not just one global statistic.

## 2. The finite-history obstruction, including its proof

For every nonempty fixed Gamma and integers p,H>=0 there exist two finite initial fields x,y, each with 3+2^p particles and initial slot occupancy<=1, such that

    O_p(F_Gamma^t x)=O_p(F_Gamma^t y), 0<=t<=H,

but

    ||O_0(F_Gamma^(H+1)x)-O_0(F_Gamma^(H+1)y)||_1=4.

Both systems use the same Gamma, time and update; their total counts and global additive directional first moments are equal and conserved. No deterministic predictor from a fixed number of these moment-history frames can therefore work for all finite states.

Choose a legal triple {j,l,m} in Gamma and any nonzero integer q in ker B. Set L=4(H+1). Put the three core particles with channels +e_j,+e_l,-e_l at positions -H times their respective channel vectors. They first meet at 0 at tick H. Put markers of channel +e_j at

    z_a=e_m-H e_j+L a q, a=0,...,2^(p+1)-1.

Give x the a with even binary popcount and y the a with odd popcount. Each has exactly 2^p markers. All markers are distinct. For t<H the core positions are distinct. The a=0 marker remains one transverse step from the +e_j core. For a>=1 the graph norm lower bound L||q||_1-1-(H-t)>H-t separates it from every core. There is no three-particle Cell, so the asserted prehistory really is free streaming, by induction; it has not been imposed as a desired solution.

For every polynomial P of degree<=p,

    sum_a (-1)^popcount(a) P(a)=0.

The left side is, up to sign, p+1 commuting finite differences with increments1,2,4,...,2^p. Each lowers polynomial degree, so the identity follows from finite algebra. At every t<=H the markers share the carrier position B(e_m-(H-t)e_j), and their hidden coordinates are h_0(t)+L a h(q). Each required monomial is therefore a polynomial in a of degree<=p; all observed moments agree. Identical core contributions cancel separately, including when carrier positions coincide.

At H the unshifted marker belongs only to x and is at the actual native neighbor e_m. It gives a unique score one on m. All other markers are at least three native graph steps from 0. Thus x has one accepted core collision and y none. After streaming, the signed core pair occupies axis m versus axis l. Those four signed-channel differences cannot cancel; marker readouts still agree. This proves the result.

The quantifiers are forall p,H exists a finite pair. Support and population may grow with the chosen p,H. This does not exclude reconstruction on a known bounded support, a different sufficient encoding, or deterministic evolution of the full native state.

## 3. A positive dichotomy and the event-rate caution

If Gamma is empty the law is pure streaming. With eta_v=h(v), binomial expansion gives

    M'_{v,alpha}(r)=sum_{beta<=alpha} binom(alpha,beta)
                   eta_v^(alpha-beta) M_{v,beta}(r-Bv).

No higher moment is required. Hence a fixed finite moment/history closure for the stated entire class exists exactly for the empty palette. This is law- and observer-specific, not a prohibition on useful reduced models in general.

Actual current event rates plus current carrier counts determine the next carrier counts by the exact event balance. They do not automatically update themselves. Set the above meeting time to H+1: through frames0..H both moment histories and all actual event records agree (the events are empty), but at H+1 the event records differ. Treating future event rates as supplied inputs is not autonomous closure.

Conversely, complete native data on the graph-radius2T neighborhood of a target Cell determine its state T ticks later. One step reads a collision one streaming step away, and that collision reads one-neighbor totals; induction gives the radius bound. This is a finite-horizon sufficient observation, not a minimality claim. Keeping the lossless (Bz,h) coordinates is equivalent; no added force or reservoir is needed.

## 4. Distinct nine-incidence result

For spectator j, let L_j(Gamma) have the other five axes as vertices and edge l--m iff {j,l,m} is allowed. The source incidence-family theorem establishes that all links connected requires at least eight triples. At equality, each vertex lies in four triples; every pair degree is at most two. The latter follows by excluding degree4 (a disconnected leaf link) and degree3 (three triples12a plus the forced completions again leave an isolated12 edge). Connected links alone still do not imply same-trajectory reachability.

For the canonical single-particle move in homogeneous C_l(j,+), pair degree<=2 confines every later deviation to {j,l} plus the initially allowed new axes. At least two outside score axes keep tying, and exterior proposals are vetoed. Thus all eight-triple, all-link-connected sets confine such seeds to at most four axes for all time.

Nine is attained by

    {123,124,125,126,134,135,146,356,456}.

All links are connected and pair12 has all four possible new axes. The canonical seed has eight first collisions, count-distance2->34, and actual spatial/channel deviation in all six axes. The parent uniform theorem gives D_t>=32t+2. Together with the eight-triple obstruction this proves the sharp minimum of nine incidences for all-link connectivity PLUS some canonical seed's all-six-axis activity. It is NOT a minimum particle count, nor a full reciprocal-feedback theorem: the canonical seed still has a conserved spectator and independent-layer decomposition.

## 5. Prior execution record and next obligation

The original supplied result records49 p,H pairs (0..6),360 oriented triple/delay cases,26 nonzero kernel directions,66 finite-difference identities, seven event-rate-history contrasts,40 streaming-closure examples,4368 fixed-root nine-sets with144 valid first steps,720 transported-palette symmetries, and finite causal-cone controls. A finite free-boundary pair contains46,875 particles each and changes distance2->34; its2,400 versus2,408 collision counts retain boundary activity. These are prior executed values, not a claim of re-running them during this recovery.

The original code reuses the prior signed-coordinate, density-port, microscopic and atlas programs unchanged. Its bounded exploratory probes and a45-second timeout were not premises of the theorems. Current source work should consume these results, not rediscover them or infer primitive force legality from a three-label event.

Next: independently specify admissible native joint-event/exchange evolution and recurrent encounters. Preserve all positional, signed-channel, phase and provenance data needed to determine it. No force-law selection, P000 change, Foundation promotion, viscosity, physical f=0 or classical NS result is supplied here.
