# R1/N14 Stage123 — exact affine full-real theorem (author proof only)

Model: external iid 3-symbol sequential test N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), arbitrary randomized stopping and decisions depending on the entire literal ordered history. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=minimum of max(tP,tQ) subject to eP,eQ<=alpha. This is NOT a P000/native-X6 theorem or an independently accepted Research Driver Result.

Starting AUTHOR-proved Stage122 frontier:

alpha122=80432667641168459255/231610973507417014272
V122=377878058477915699662445/29646204608949377826816

Choose K123=15175912302/20129609, L123=14232343848/20129609, S123=29408256150/20129609. Write eta123=37340424695/274501894527309053952.

**THEOREM**: FOR EVERY REAL delta in [0,eta123],

V14(alpha122+delta) = V122 - S123*delta.

Exact new endpoint:
alpha123=2573845365525582162925/7411551152237344456704
V123=377878052586265662571445/29646204608949377826816.

This support line is right-sharp: for any alpha>alpha123, V14(alpha)>H123(0)-S123*alpha. Larger alpha itself is not infeasible.

## Universal Bellman support over full ordered histories

A count state s=(n,a,b) records length and numbers of symbols 0 and 1. The likelihood ratio of any ordered prefix at s is Q(prefix)/P(prefix)=2^(a+b)/3^a. Exact backward recursion is the minimum of K*2^(a+b)/3^a (declare P), L (declare Q), and at n<14 continuation cost 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b). The finite domain contains 680 states. Exact rational evaluation yields 1238 strictly positive nonchosen gaps, NO negative gaps, minimum strictly positive gap 5078657746807/641138030936064, and precisely two ties:

A=(9,3,0), P/continue; J=(10,5,4), Q/continue.

Root H0=286757541275625427937177135/551355235823978532569088 = V122+S123*alpha122.

Every literal ordered prefix at given counts has the same likelihood ratio and conditional iid suffix; thus induction does not restrict policies to counts. For every full-history randomized policy,

H0 <= tP + L*eP + K*eQ <= max(tP,tQ)+S*alpha.

Consequently V14(alpha)>=H0-S*alpha universally.

## Ordered provenance, affine moments and attainment

At A, declare P with probability y, otherwise continue; at J declare Q with probability r, otherwise continue; all other states choose their unique Bellman minimizer, including the previously saturated F=(3,0,2) now strictly declare Q.

The literal FIRST-HIT ordered histories and P/Q positive rational masses are:

A: 84 words, P=109375/1990656, Q=109375/6718464.
J: 371 words, P=1855/65229815808, Q=1855/30958682112.

Their path cones cannot overlap: A has depth 9 and (a,b)=(3,0), while J has depth 10 and (a,b)=(5,4); the latter needs 2 extra zeros plus 4 extra ones in only one observation. The reverse is impossible by depth monotonicity. Therefore the four-observer moment vector M=(eP,eQ,tP,tQ) has no y*r term:

M(y,r)=M00+y*dA+r*dJ, with

M00=(
9514370164165379/27390260577042432,
222863562470405/641959232274432,
349750993637573887/27390260577042432,
646990466251291/53496602689536).

dA=(
-1921609375/7925422620672,
259765625/835884417024,
-20758609375/330225942528,
-1476453125/69657034752).

dJ=(
1834595/2404631929946112,
-142835/213986410758144,
-3626525/100192997081088,
-46375/660451885056).

Error balance eP=eQ is equivalent to

y(r)=2367785183471/6494178000000 + (14328709/5541698560000)*r.

For ALL real 0<=r<=1, 0<y(r)<=151539326395319/415627392000000<1, hence strategies are legal; both errors equal alpha122+eta123*r. At r=0, tP=V122; at r=1, tP=V123. Both endpoints strictly satisfy tP>tQ, with respective exact gaps

19564553826414832986221/29646204608949377826816
and
19564551641189828171621/29646204608949377826816.

Those gaps are affine and positive for every intermediate real r. Every chosen action attains the Bellman minimum, both error constraints are tight, and max(tP,tQ)=tP. Thus the lower bound is attained throughout the entire real interval, proving the theorem.

## Right-sharpness

The finite ordered-history randomized policy domain is compact, so an optimal policy exists. Equality to the same positive-multiplier support for alpha>alpha123 would force both errors to equal alpha and every positively reached action to Bellman-minimize. There are only two ties A and J, and count-fiber word-specific randomization may be averaged without altering the four declared iid observables. Disjoint first-hit cones imply observer equivalence to some (y,r) in [0,1]^2 on the unique balance line above. Its common error increases strictly with r and r<=1 forces alpha<=alpha123, contradiction. This proves sharpness of the present support line, not global impossibility beyond this endpoint.

## Actual exact verification / limitations

Local Fraction Bellman + separately implemented integer-weight literal ordered-word DFS using P=(3,1,20)/24, Q=(1,1,10)/12 were actually run. Four corners (y,r)=(0,0),(0,1),(1,0),(1,1) visited 823333, 815542, 818293, 810502 DFS nodes. Every corner exactly matched all four moment components and the A/J first-hit counts and P/Q masses. Two distinct author implementations passed; there is NO claim of independent Driver mathematical review or remote code execution.

BRC reuse: REUSE_APPLIED — positive rational weighted ordered paths with branch identity, multiplicity and separate P/Q probabilities; count quotient only justified for these four iid observers. No faithful P000/native six-dimensional Cell readout map established.

Native task inventory responded CONTROL_QUOTA. Attempted native Researcher session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. The live Owner, native CLAIM, frozen Result and independent review remain unverified. Ordinary authorized GitHub persistence does not change this.

Pinned inputs: GLOBAL_KNOWLEDGE_V1 canonical main@28719731af88def01da147f49d19fb0a91474b5d, Enterprise Math main@6974c5530449705a1105bbadf5349c90ee65f574, Stage122 source research_notes/n14_aux_iid_affine_122_20261026/PROOF_STAGE122.md, GLOBAL P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.

Next scientific candidate Stage124 is DUAL_ONLY; see NEXT_TASK_PACKET_124.md.
