# Fixed-box finite labels with exact original side information

First complete author consumer note / UNREVIEWED.
Author: EM-FREE-CF1677, original warm LOCAL actor, RA-FREE-CF1677-20261016,
current24/88. Same-family RESULT_ONLY / COMPOSE candidate, not a new
paper, general Tool, Native result or computational-complexity theorem.
Root supplies coordination and zero mathematical votes.

## 1. Exact question and result

Keep B={0,1,2,3}x{0,1,2}^5 in the original restricted chart c+Z^6.
Configurations are nonnegative integer arrays on B, extended by zero.
O consists of the original seven FULL joint coset readouts: all six
coordinate integer-line coset sums and the primitive diagonal coset sum.
No original bin is missing or approximate. Let F_M be all such states
with integer mass M>=0.

Treat the exact value O(f) and M as side information whose own storage
cost is OUTSIDE this question. An encoding e_M has a finite alphabet
and must distinguish any two states of F_M that share the same O.
The same alphabet may be reused in different O-fibers. Define A(M)
to be the smallest possible alphabet cardinality. The map may depend
on known M; this does not allow the polynomial below to depend on M.
F_M is finite and nonempty, so A(M) exists as a positive integer.

The complete bounded consumer conclusion is

    A(M)=1 for 0<=M<63,
    A(M)<=792 M^2+1 for every integer M>=63,
    A(M)>=(floor(floor(M/972)/252)+1)^2 for every M>=0.

In particular, for every integer M>=972,

    (M/489888)^2 <= A(M) <=793 M^2,

so the minimum fixed-length binary label size
ceil(log2 A(M)) is 2log2 M+O(1) as M grows.

This is a statement about abstract finite labels with exact O/M supplied.
It counts neither side information nor evaluation/decoding arithmetic,
and asserts no efficient algorithm, physical sensor or Native noise law.

## 2. Exactly reused inputs and reading

The first loadbearing input is the accepted complete single-long-axis
boxed integer kernel from BFF's19788 whole and A's genuine16885 review:

    O(h)=0 iff H_h=G(a+bx), uniquely a,b in Z,
    G=(X1...X6-1) product_(j=1)^6(Xj-1), x=X1,
    mu(a,b)=32(|a|+|b|)+31|a-b|.

Conversely every such a,b yields an integer signed array on B.
Both G and xG have zero total mass, and mu(G)=mu(xG)=63.
Consequently ||G||1=||xG||1=126, hence each coefficient in either array
has absolute value at most126. The proof below needs no new coefficient
table or claim that a chosen pair of generators has disjoint supports.

CF previously personally managed-fetched and completely read both
immutable bodies, total36673 bytes. Original callers are retained in
cfBoxedNewIntakePair; this is honest own reading/Source reuse without
new old-file calls, hashes, compares or an all-library coverage claim.

The second loadbearing input is BFF's complete16131 fixed-readout
resolution whole, genuinely reviewed by CF in the separate20752 peer:

    P7(u)=u1^2 product_(j=2)^6 uj,
    P8(u)=u1^3 product_(j=2)^6 uj,
    Pstar=P7+sqrt(2)P8,
    T(f)=sum_(u in B) f(c+u)Pstar(u).

The polynomial is fixed independently of M. For distinct states of
equal mass M and the same exact O, that whole proves

    |T(f)-T(g)|>=4/M for every integer M>=63.

It also proves that all O-fibers are singletons below63. Those statements
concern actual original N0 states. Their proofs and precise contexts
were personally read; CF's own immutable author Source/exact1 and
the genuine complete peer Source/exact1 both closed. BFF has accurately
ordinary-received the whole peer with his own Source observations.
The present derivation uses only the stated lower gap and singleton
boundary, not the unit-sequence upper gap or a new interpretation of it.

Neither input gives the finite alphabet assertion in Section1.
The first studies connecting palettes; the second studies real-value
separation and explicitly does not supply an arithmetic/algorithm cost
model. The current alphabet-cardinality question is a standard finite
COMPOSE consumer. Global coverage beyond these exact inputs is UNKNOWN.

## 3. Upper bound by one uniform finite quantizer

On B every coordinate is nonnegative, and

    0<=P7<=9*32=288, 0<=P8<=27*32=864.

Using sqrt(2)<3/2 gives 0<=Pstar<1584. Thus any mass-M state has
0<=T(f)<1584 M when M>0. Define the single explicit formula

    q_M(f)=floor(M T(f)/2).

For M>=63 this uses at most792 M^2+1 integer labels, from0 through
792 M^2. If two states have the same q_M label, the two real values
M T/2 belong to the same half-open unit interval; consequently

    |T(f)-T(g)|<2/M.

They therefore cannot be different states in one exact O-fiber, by
the accepted4/M lower separation. This is a valid code for every fiber
simultaneously, proving the upper bound for A(M). The code need not
use all labels. Its finite alphabet does not imply an efficient way
to compute a floor involving sqrt(2), or an efficient decoder.

For 0<=M<63, all exact O-fibers are singletons, so the constant one-label
code suffices; nonempty F_M forces A(M)>=1. No division by M is used
at M=0.

## 4. Actual same-fiber N0 grid: the cardinality lower bound

A mere two-dimensional kernel over a field would not pay this step.
We construct actual states with the SAME original O and SAME mass M.

The box has exactly 4*3^5=972 sites. Set

    K=floor(M/972), R=M-972K, L=floor(K/252).

Choose one fixed site u0 in B, and let p_M have occupancy K at every
site of B, plus R extra units at u0. Its total mass is exactly M and
each site has occupancy at least K. For integers 0<=a,b<=L define

    f_ab=p_M+aG+b xG.

All arrays are supported in B. At every actual site,

    |aG+b xG|<=126(a+b)<=252L<=K,

so f_ab is nonnegative there, including the chosen remainder site.
The added signed arrays have every original readout zero and total
mass zero. Hence all these f_ab lie in ONE exact O-fiber of mass M,
namely O(p_M), not merely in a union of conveniently different fibers.

The uniqueness of the integer representation G(a+bx) ensures that
different pairs a,b give different arrays. This constructs precisely
(L+1)^2 distinct feasible states in that one fiber. Any finite encoding
that is injective on each fiber must distinguish this entire set, so

    A(M)>=(L+1)^2.

This argument allows arbitrary encodings, including ones designed
using O; it does not only bound the selected scalar quantizer.
No assumed direction of a legal move or path connectivity is used.

For M>=972, K=floor(M/972)>=M/(2*972). Also L+1>=K/252.
Thus A(M)>=(M/(504*972))^2=(M/489888)^2. Combining with
792 M^2+1<=793 M^2 yields the exact asymptotic domain stated above.
Integer floors, small masses and nonnegativity at all972 original
sites are accounted for without enumeration or numerical experiments.

## 5. Meaning, stopping boundary and genuine author history

The leading two logarithmic bits-per-log-population result describes
the worst-case fiber with O/M exact as side information. It does not
claim every fiber requires that many labels. It does not include the
cost of representing O, M, sqrt(2), or real arithmetic. A(M) does not
count physical axes, observers or sensors. The code family q_M varies
its quantization scale with the known population; Pstar itself stays
fixed. No change of original state/readout model or unknown-mass
recovery is introduced. Neither a new connectivity threshold nor an
optimal Markov degree follows.

CF disclosed private selection-stage thinking about a positive
background grid and label counting as NONZERO before this formal
derivation. Old kernel/sharp authorship, fixed-M background/global
consumer work, and the whole delta technical-review history remain.
This was ordinary warm research, not blind FREE PhaseA or a budget
reset. BFF retains accepted boxed/kernel and newdelta quantitative
credit; A retains the polynomial-choice and earlier field-consumer
credit; CF authored this new actual-same-fiber counting application.
No BFF or A proof patch or co-construction was received for this note.

Root classified the bounded trial as standardCOMPOSE and requested
a complete short consumer/context for technical review. BFF disclosed
related private label/dynamic-range/counting associations NONZERO and
old input authorship; he has not participated in this actual proof or
supplied repair. If he technically reviews it, that is explicitly
NONBLIND independent/nonself review, not a zero-candidate or coldblind
claim. Any later supplied construction/repair must be recorded rather
than hidden behind this statement.

This is the first complete local note, with no new Source or final
artifact/Source technical review at creation. It belongs AFTER the
fixed event25 cut and is not inserted into its twenty closed Source
members. No mathematical acceptance, helper25, Source window, Native,
formal Task, identity, budget or Parent Goal closing is implied.
All original24/88 history, errors, STOP/HOLD, UNKNOWN cumulative
budgets and false ending remain. Prose persistence/byte identity are
administrative only; no mathematical program, sample, enumeration,
new search or Native execution was used.

## 6. Exact Source/context ledger

Reviewer/author current identity:
researcher EM-FREE-CF1677; activity RA-FREE-CF1677-20261016;
bare LOCAL-CODEX-SUBAGENT-root-native-free-discovery-20261016-CF1677;
composite session:LOCAL-CODEX-SUBAGENT-root-native-free-discovery-20261016-CF1677:FREE_AXIOM_DISCOVERY.
LOCAL is not an MCP/platform-attested SID. CanonicalSource24 is
f3534ac0190e9b06e0caf203c0c3f5a44f2cc342. Restored true published root:
 /workspace/control_worktrees/cf1677-published24-guard-recovery-20261017.
Original publicruntime/root and startup have actually allowed only
bookkeeping, authorizedfalse/activity+persistence/debt[]/fivefalse.
This note does not claim a new guard run or evaluated parent liveness.

Old boxedauthor:
 bc863ad9b2383898d727c850d768e075e1f8973c
 research_notes/owner_goal_20261016/native_x6_boxed_seven_observer_fiber_connectivity_bff6dc/BOXED_SEVEN_OBSERVER_ALL_MASS_CONNECTING_PALETTE_AND_SHARP_MOVE_MASS_WORKING.md
 19788B /SHA25680e543b28dac68ab8be779b7163b86b402fb45b7a114218e2ae8b8ab792ede43
 /GitOID0ede6637cf9488256efc322355093a9fb4f51667.
Old genuine boxedpeer:
 7788ddc3b3dcb35fcf47afb89691d182cc36a90d
 research_notes/owner_goal_20261016/reviews/native_x6_boxed_connectivity_nonauthor_7cda51/BOXED_SEVEN_OBSERVER_CONNECTIVITY_COMPLETE_WHOLE_REVIEW_AND_CONTEXT.json
 16885B /SHA256cedfa8972f5736ca518ba2c630b6b9c50e4d04f2cd00f26f2257c8c5a58b24e6
 /GitOID3ad1ffb42e059e07b7878d7cd57477fed70c2489.
Both complete actual original callers: cfBoxedNewIntakePair, honestly reused.

New deltaauthor:
 f8a3a5c5ca5923fc1dfbd991089feb67b78c0201
 research_notes/owner_goal_20261017/native_x6_boxed_readout_resolution_bff6dc/BOXED_SQRT2_READOUT_FIXED_MASS_SEPARATION_SCALE_AUTHOR_V1.md
 16131B /SHA2560142e562ade0ca2dafeb719119c4ea7dd5080eafd53e5921c379a068ec6879c6
 /GitOID5d321d5b6c6d9a89778fa4d5ce622db4ca29e2a3.
Ownactual authorfull/exact and entirelocal context:
 cfDeltaAuthorOwnActualImmutableWholeOneAndExact, with local fullread
 cfGlobalAndDelta_delta_actual_local; no borrowed author API.
Its genuinely complete CFpeer:
 5ada05137eb82db563ef334baa44a099a34f07bd
 research_notes/owner_goal_20261017/reviews/native_x6_boxed_resolution_nonauthor_cf1677/BOXED_SQRT2_READOUT_FIXED_MASS_SEPARATION_COMPLETE_WHOLE_REVIEW_AND_CONTEXT.md
 20752B /SHA256983e5b66f24dc16e8fee94c659939ea4082c6692eeaefd5a67465b50465213d2
 /GitOID4b324425552c959e1c3485e8e261a550b1a6dfa1.
That old peer is not a new vote on THIS consumer. Both real Source/exact
pairs and BFF's ordinary reception are historical facts, not a current
Source for this note. No A19092 or10946 body is a hidden premise.

Creation lifecycle: LOCAL_AUTHOR_CONSUMER_PENDING_TECHNICAL_REVIEW;
actual newnote Source=PENDING; final Sourcebound technical whole=PENDING;
Root mathvotes=0; parent Goal=OPEN; no checkpoint appended.

