# Complete technical review of the shortest torus word with linear vacancy peak

NONBLIND_INDEPENDENT_TECHNICAL_WHOLE_PASS_BOUNDED / RESULT_ONLY_COMPOSE.
Identified mathematical must-fix: 0. Actual author construction/repair by reviewer: 0.
Reviewer: CF1677 / EM-FREE-CF1677, same original warm execution.
New upper construction and proof: 4A / EM-P11-4A56E9.
Root routes and controls custody, with zero mathematical vote.

## 1. Exact whole, result and dependency boundary

I personally read the complete actual 14144-byte author artifact, including
its opening, sections 1-6, equations (1)-(8), all input history and the entire
context, in one untruncated local output. I independently checked every new
upper-bound step. The immutable author body was subsequently bound by my own
full-file/GitData/exact comparison before this final review was frozen.

The whole is
RESIDUAL_TORUS_SHORTEST_WORD_LINEAR_VACANCY_SWEEP_AUTHOR_COMPOSE_APPENDIX_V1.md
under research_notes/owner_goal_20261017/residual_torus_matching_linear_peak_sweep_4a56e9/.
Its actual identity is 14144 UTF8 bytes,
SHA256 9bc3ba7429ed6c04194a59367847e75a3334b527047bf7e784d59595a7907436,
Git blob 3df64fa3c1eac5fc5d700e86d6b432cc49693fc7.

The result is restricted to the stated square family m>=3, n=m^2:
one and the SAME legal primitive word uses exactly 2m^2 commands and
has peak vacancy at most 3(m+1). Together with the genuinely accepted
all-word lower 3 ceil(m/3) on this identical carrier, the optimal peak
is Theta(m), equivalently Theta(sqrt(|I|)) since |I|=3m^2.
This is a simultaneous shortest-word and upper-resource result, not
a short word and a different low-vacancy path. No exact optimal peak
or optimal leading constant is claimed.

I already genuinely whole-reviewed the 17242-byte lower author at
12eed3f75373264c6dbf87451f2a37c3a69a399a, with my own immutable full
body, exact one ADD/one commit/sole parent binding. My separate complete
15907-byte technical peer is 07cac90821fb24111e7b5c4bed31d3e5ea6118e9,
with actual own Source posterior and the author's ordinary acceptance
closed. Those old mathematical and custody results are honestly reused.
The lower proof is an actual dependency; its older vote does not check
the new word, and the new proof is checked independently below.

The two original primitive blobs were already actually fetched by me:
f45165d7144d342d6cf9233ea77a04a51d2b96e3 (12776 bytes) and
be1b60446e31c2c8489d1ce0db16cc1e952d11c8 (13417 bytes).
Only the necessary complete reserve/release/matching/observation definitions
and selected old coverage definitions were semantically read. They were not
whole code reviews, imports or scientific executions. No new old-code call,
old-body read, hash inventory or borrowed API is needed in this upper review.

## 2. Actual saturated intermediate matching and safe ownership

The inventory is exactly the 3m^2 distinct members x_p^a, where
p in (Z/mZ)^2 and a in {0,1,2}. The only licensed events remain
A_p={x_p^0,x_(p-e1)^1,x_(p-e2)^2} and
B_p={x_p^0,x_p^1,x_p^2}.
Each family partitions the inventory; the three A-owners of B_q
are A_q,A_(q+e1),A_(q+e2). All modular indices are finite member labels,
not Native axes or a change to the original X6 chart.

For any S of present B-indices, the proposed state
J(S)={B_q:q in S} union {A_p:p outside N(S)}
with N(S)=S union(S+e1)union(S+e2)
is an actual disjoint matching. The A/B ownership criterion rules out
every cross-family intersection; intra-family disjointness is unchanged.
There are |S| selected B-events and n-|N(S)| selected A-events, hence
vacancy(J(S))=3(|N(S)|-|S|). Both endpoints are correct:
J(empty) is all A, J(T) is all B.

For q outside S and S'=S union{q}, the indices of newly conflicting
A-events are exactly D=N(S') minus N(S). Each p in D is outside N(S)
and therefore its A_p is actually present in J(S). In particular
p is outside S, so B_p is absent. The release at the literal member
x_p^0 removes A_p, rather than an already selected B_p.
Earlier releases of other A-events do not change this ownership,
because the A-family is disjoint. No selected B is touched.

After all these releases, every A-neighbor of B_q is absent. Existing
B-events are disjoint from B_q, so reserve(B_q) succeeds. The surviving
A-events are precisely those outside N(S'), making the result J(S').
This also handles D empty: all B_q members are already free, and the
reserve alone is legal. There is no hidden atomic exchange or auxiliary
member in this construction.

## 3. Every deletion state and every wrapped row prefix

I checked the transient bound at the point BEFORE each reserve.
Every successful A-release increases vacancy by three. Starting from
J(S), after |D| releases the vacancy is exactly
3(|N(S')|-|S|)=3(|N(S')|-|S'|+1).
Intermediate releases give no higher vacancy; the succeeding successful
reserve reduces it by three. If D is empty, this same displayed expression
is the initial vacancy. Thus it covers every primitive state, not merely
the completed stages J(S').

The row-major prefixes have full rows j<a and the first b sites in row a,
where 0<=a,b<=m-1; the final prefix is T. I checked all cases of the boundary
calculation with modular shifts:

- Empty prefix: the boundary is zero.
- First partial row, a=0 and b>0: the horizontal shift adds (b,0);
  the vertical shift adds b points in row 1. They are disjoint, and
  the boundary is b+1<=m.
- Middle rows, 1<=a<=m-2: shifting the last full row fills row a,
  supplying m-b missing points there. Shifting the partial row adds
  b points in row a+1. These rows are distinct. Any horizontal new
  point is already among the missing row-a points. The boundary is
  exactly m, including b=0.
- Last row, a=m-1: the upward shift of the partial row wraps into the
  already full row 0. The preceding full row fills only the m-b
  missing sites of the last row; horizontal additions are contained
  in that same set. The boundary is m-b<=m.
- Final prefix: N(T)=T and the boundary is zero.

No overlapping directional boundaries have been added twice. The
last-row and first-row cases do not use an infinite-plane approximation.
The argument works for all m>=3, regardless of primality.

Every successor S' is again one of these prefixes, so its boundary
is at most m. The exact pre-reserve expression therefore bounds
EVERY intermediate vacancy by 3(m+1), while every completed stage
has vacancy at most 3m. The final stage is included: it can still
have free members just before the last reserve, and the formula
retains the required extra one rather than silently omitting it.

## 4. Exact shortest command length and quantitative conclusion

The neighborhoods increase monotonically along the prefixes. Their
successive increments D are disjoint and have union
N(T) minus N(empty)=T. Thus exactly n old A-events are released,
each once, and exactly n target B-events are reserved, each once.
All commands succeed. The resulting actual word has exactly 2n commands
and the bound of section 3 simultaneously.

The minimum command count is independently justified in the same
primitive model. Each of n initially present A-events is absent
at the target and can disappear only through a successful release.
One release removes at most one current event. Every one of the
n final B-events begins absent and requires its own successful reserve.
A single primitive cannot do both jobs, so at least 2n commands
are necessary even with arbitrary failed commands or backtracking.
The constructed word attains this lower bound.

The old lower concerns EVERY word in exactly the same licensed
inventory and operation set, so it applies to this word as well.
Its use yields
3 ceil(m/3)<=p_m<=3(m+1).
Both sides are constant multiples of m for m>=3, giving the stated
Theta(m) conclusion. I found no gap in this combination and no need
for an author patch. The statement does not calculate p_m exactly,
prove a row sweep's optimal constant, or classify all shortest words.

## 5. Scope, history, independent contribution and actual limits

This review is ordinary NONBLIND independent nonauthor technical whole.
My old lower review, original Native-cycle background and related private
warm reasoning remain. At the occupation topic I had an unexpanded
row-sweep/linear-upper association NONZERO; it was not developed into
the author's actual word, formula or proof and was not supplied to 4A.
My earlier reply about no topic-triggered derivation was not a declaration
that all private associations were zero. I disclosed that distinction to
Root before this final review. Nothing requires or claims cold status.

I did not participate in the actual 4A construction or repair.
The new saturated-prefix realization, owner-safe primitive word, wrapped-row
boundary count and simultaneous resource/command theorem belong to 4A.
My calculations above are independent review reconstruction after formal
routing. Root supplies zero mathematical vote. The old lower whole is
a dependency, not a substitute peer vote on this new upper.

The author context correctly preserves that private upper work began
after the old peer was frozen, while the author's older ordinary Source
duty was still being finished; the complete new proof/persistence followed
that ordinary closure. The author reports an initial 13968-byte context
wording correction and the final complete 14144-byte self-reading/freeze.
That reported author-side exposition history is not my API observation
or a mathematical patch from me. The fixed 14144 body is the whole reviewed.

The mathematical result remains conditional on exactly these licensed
A/B triples, this finite inventory and single-triple primitives. It
does not establish the exact optimal vacancy, an arbitrary complete
matching-library theorem, behavior with extra events/members or atomic
swaps, a probability law, scheduling/latency, energy or Native dynamics.
The finite torus indexes members; it does not become spatial or temporal
axes. Old foreign-result computations, BRC weights, readiness certificates
and upstream registration status are not new accepted premises.

The scope's own kill is appropriate: this fills the actual m versus m^2
resource gap. Merely changing m or relisting another sweep order does not
create another research unit. This is a same-family finite COMPOSE result,
not a new generic Tool or principal paper.

## 6. Own immutable Source binding and final review context

My own actual managed full-file read is the exact 14144-byte author body at
Source 0a340bb77a3a1ed241c3ef09e2e8461afe7ff111,
sole parent c1c633fec98a2e5ce02e93972045551ec662b33f,
tree ac9fa9c0fa3252550eed4b566184cef048b5e89b.
My own GitData and compare calls establish exact one ADD of its author path,
one commit, ahead 1 / behind 0, no other changed file.
Returned Git blob: 3df64fa3c1eac5fc5d700e86d6b432cc49693fc7.
Actual local/source-identical SHA256: 9bc3ba7429ed6c04194a59367847e75a3334b527047bf7e784d59595a7907436.

Immutable author URL:
https://github.com/awdawmip/enterprise-math/blob/0a340bb77a3a1ed241c3ef09e2e8461afe7ff111/research_notes/owner_goal_20261017/residual_torus_matching_linear_peak_sweep_4a56e9/RESIDUAL_TORUS_SHORTEST_WORD_LINEAR_VACANCY_SWEEP_AUTHOR_COMPOSE_APPENDIX_V1.md

Original managed arguments and entire results are preserved beside this
review in OWN_ACTUAL_AUTHOR_ONE_FULL_SOURCE_GITDATA_COMPARE_RAW.json.
OWN_ACTUAL_TORUS_LINEAR_PEAK_AUTHOR_SOURCE_COMPLETE_GATE.json records the
own observation boundary. These are three new read-only Source/commit/compare
calls; the older lower and primitive contracts are reused without new calls.

The actual 14144-byte local author whole was genuinely read before this
binding; its returned immutable UTF8 is identical, so that complete
semantic reading is honestly reused without claiming another proof whole.
My own raw arguments and entire results were saved before assertions.
No author or Root API substitutes for the observations recorded above.
The author's original Source/peer pending creation words are unchanged.

This complete review/context is then personally read and frozen on its
actual bytes. Its later Source publication and the author's ordinary
acceptance are separate observations, not prospective facts supplied
by a draft. Same original CF execution remains canonical25/108 and
the work is after that fixed activity cut. Original LOCAL/composite,
STOP/HOLD/UNKNOWN, historical error/CAS receipts, five false formal
flags and Goal OPEN remain. These prose/byte administrative operations
and managed immutable reads are not scientific execution, Native
authority, formal Task, a helper26 append or an identity/budget reset.
Own current policy snapshot is main@67a02007c854705c3a2ffcf1858997163962420c;
unchanged CodeV2/ENV/POSIX were honestly reused.
