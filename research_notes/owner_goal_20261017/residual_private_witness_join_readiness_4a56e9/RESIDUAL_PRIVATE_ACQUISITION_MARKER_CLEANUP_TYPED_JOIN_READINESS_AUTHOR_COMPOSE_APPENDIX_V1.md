# A typed state certificate for private acquisition-marker readiness and cleanup

First complete AUTHOR COMPOSE APPENDIX V1 / UNREVIEWED.
Sole new author of this readiness certificate: EM-P11-4A56E9,
the same warm actor/SID/RA. Root routes and supplies zero math votes.
This is one bounded same-family conditional RESULT_ONLY / COMPOSE
appendix to the actual residual-contention model. It is not a new
paper, Tool, lock, Native observer implementation or physical claim.
New author Source, independent technical whole/context, peer Source
and final ordinary acceptance are PENDING at creation.

## 1. Actual orphan input, literal state operations and limits of this theorem

The actual foreign RESULT introduces workers that store whether
their OWN bridge formed, rather than treating failure to acquire
a bridge as a negative source observation. Its original claim
requires complete markers before an OR join. We address the
state-level readiness obligation using its exact permitted
occupancy observer, without equating readiness with program-counter
termination or supplying a physical completion detector.

A state J is a disjoint matching of three-element events over
the DECLARED finite model inventory. Write used(J) for its
occupied members. Only the original licensed reserve triples
may be proposed. The actual pinned functions step/full_step
implement these deterministic state changes:

    reserve(T):
      if T intersects used(J), leave J unchanged;
      otherwise add T to J.

    release(x):
      if no event contains x, leave J unchanged;
      otherwise remove the unique event containing x.          (1)

An attempted reserve does not overwrite an old event. Release
removes an entire current triple, not just x. No alias release
or external occupation is allowed in the worker-private region.
The exchange wrapper rejects a reserve outside its declared
library; this licensing condition is retained.

For a frozen interface I, the actual membership projection
retains every nonempty trace of each event on I, together
with the count of wholly invisible events. Its typed observed
function returns occupied members in I and the total event count.
Here I already includes all the members of the original source
and the newly DECLARED worker triples. We only use occupied/free
bits of that existing interface, not a hidden partner identity,
a source-sign oracle, a clock or a silently enlarged interface.

Reading this typed mathematical observation is a declared
CONDITIONAL MODEL operation. No native measurement, Cell mapping,
non-disturbing physical instrument, permission or cost for that
observation has been supplied. The theorem below says what an
actual reachable state certifies IF that permitted observation
is available. It does not construct or authorize the physical
observer.

A scalar positive BRC weight is not needed in this pointwise
state proof. We do not replace an executed CWM history law by a
Boolean count or verify any reported history multiplicity.
The new assertion holds for each indicated legal history.

## 2. Source family, stable private interfaces and the exact eight-step word

Use the original source events

    E={1,2,3}, P={2,6,10},
    A={4,5,6}, B={4,5,7},
    Hplus={6,8,9}, Hminus={7,8,9}.

The admissible preparations are disjoint subsets of this
library containing exactly one of Hplus/Hminus. There are
nine: with Hplus one may independently include E and B,
giving four; with Hminus the allowed additional subsets are
empty,E,P,A,E+A, giving five. Define sigma(J)=1 for Hplus
and0 for Hminus. N(J) removes only A/B.

An initial release(4) removes the possible A or B, and
does not touch E, P or the chosen tail. Workers begin
after that opening phase. In the positive case member7
is then free; in the negative case Hminus keeps7 occupied.
E,P and the tail remain stable throughout the worker phase.
This is a model hypothesis, not a claim that an arbitrary
real source or external scheduler meets it.

Let k>=1 and index workers by i=0,...,k-1. Put o=30+20i,
and abbreviate the following PRIVATE, mutually disjoint
members for this worker:

    a=o+1, b=o+2, c=o+3, d=o+4, e=o+5, f=o+6,
    w=o+7, u=o+8, v=o+9.

The six output members a,...,f start free. All private
members start free and no other worker touches them.
Only source member7 is shared between worker bridge proposals.
The declared local triples are

    B_i={7,u,v}, D_i={v,c,w},
    S_i={c,e,f}, T_i={d,e,f},
    X_i={a,b,c}, Y_i={a,b,d}.

These are explicitly added model licenses, inherited from
the orphan input, not derived as Native axioms. Each worker
uses the exact eight instructions

    1 reserve(B_i)
    2 reserve(D_i)
    3 reserve(S_i)
    4 reserve(T_i)
    5 release(w)
    6 reserve(X_i)
    7 reserve(Y_i)
    8 release(u).                                            (2)

The allowed no-fault schedules are all finite interleavings
that preserve each worker's internal order. Atomicity of(1),
private exclusion, stable old source/tails and an opening
completed before workers are explicit preconditions.
We do not assume three-step mutually exclusive windows,
bounded delays, fair scheduling or a unique winning worker.

The two COMPLETE bit encodings are different matchings on
the same six occupied output members:

    P0_i={T_i,X_i}, P1_i={S_i,Y_i}.                           (3)

They are not occupancy-distinguishable bit values. Occupancy
will certify COMPLETENESS only; it will not decode their bit.

## 3. Both literal private traces and every no-fault prefix

First take the branch in which worker i's bridge B_i forms.
It occupies v and u and remains present until this worker's
step8, because no other worker touches either private member.
Thus reserve D_i fails; reserve S_i succeeds; reserve T_i
fails on e/f; release(w) does nothing; reserve X_i fails on c;
reserve Y_i succeeds. Its complete output is P1_i, and only
step8 clears B_i. These conclusions use complete triples,
not an occupancy-only substitute for the actual state.

If its bridge does not form, all its private members are
free when step2 begins. D_i succeeds, S_i fails on c,
T_i succeeds, release(w) removes D_i, X_i succeeds, Y_i
fails on a/b, and release(u) does nothing. Its complete
output is P0_i, and both B_i,D_i are absent.

Here is the complete output-occupancy table after each
local instruction, with step0 before its proposal:

    local step       bridge formed        bridge absent
    0                empty                empty
    1                empty                empty
    2                empty                {c}
    3                {c,e,f}              {c}
    4                {c,e,f}              {c,d,e,f}
    5                {c,e,f}              {d,e,f}
    6                {c,e,f}              {a,b,c,d,e,f}
    7                {a,b,c,d,e,f}        {a,b,c,d,e,f}
    8                {a,b,c,d,e,f}        {a,b,c,d,e,f}       (4)

In the formed branch, before step8 u is occupied by B_i;
after step8 u is free. In the absent branch u is always
free. The only additional private event in the absent
branch is D_i between steps2 and5. The table enumerates
ALL local prefixes; an interleaving merely inserts other
workers' operations, which do not change these private
states. Shared member7 determines acquisition, but the
branch is stable once the worker starts reading v.

Define its acquisition bit c_i to be1 exactly when its own
bridge formed. The complete matching in(3) has that value.
This is the orphan's private-success type, not an assertion
that every worker has independently observed sigma.
We have repaid the complete six-step reader behavior
inside(2), without importing a hidden old reader theorem.

## 4. Exact certificate, equivalence and stability

At an actual model state define the following predicate
using ONLY the permitted occupied/free observation:

    C_i(J) := [all a,b,c,d,e,f are occupied in J]
               AND [u is free in J].                         (5)

For every reachable worker-phase prefix under the
preconditions above, the exact equivalence is:

    C_i holds
    iff the correct complete acquisition encoding
        P_(c_i),i is present AND B_i,D_i are both absent.      (6)

Proof of the forward implication: by(4), six occupied
output members occur only at/after step6 of the absent
branch or step7 of the formed branch. At these points
the complete matching really is P0_i or P1_i. No earlier
prefix has six occupied members; in particular D_i can
temporarily occupy c but cannot fake all six. Both complete
matchings occupy c, so D_i cannot coexist with either,
and the trace also shows its earlier cleanup. Only B_i
uses u anywhere in the licensed worker phase. Therefore
u free is equivalent to B_i absent, giving both cleanups.

Conversely a correct complete matching occupies all
six members, and absence of B_i makes its unique private
u free. This gives C_i. The equivalence is asserted only
on the reachable contracted prefixes, not arbitrary
matchings that an unauthorized outsider might create.

The certificate is stable under every remaining original
worker instruction and every other worker's instructions,
until a separately licensed join begins. Indeed:
- In the absent branch C_i already holds after step6.
  The remaining Y_i reserve fails because a/b are occupied,
  and release(u) is a no-op.
- In the formed branch C_i first holds after step8.
  No local instruction remains.
- Other workers touch none of these private members.

Thus ready does NOT mean the program counter already
terminated: a failed-bridge worker can be genuinely
ready before its last two harmless instructions.
This is a state-level completion/cleanup condition,
rather than an invented program-position clock.

Occupancy alone does not decode c_i: P0_i and P1_i
both occupy the same six outputs. The second conjunct
u free matters independently: in the formed branch
after step7 the full correct marker is already present
but its bridge still holds7. Omitting that conjunct
would certify a dirty workspace. This distinguishes
both pieces of the obligation.

## 5. Safe OR consumption, exact source statement and remaining join contract

Suppose a single actual state satisfies C_i for every
worker. Equation(6) then supplies simultaneously:
all raw acquisition registers are complete and correct,
all worker bridges/probes are absent, and no remaining
worker action can disturb them. The shared member7 is
no longer held by a worker. E,P and the chosen tail were
unchanged, and the old A/B were removed by the opening.
The old-source component is N(J), with only the complete
private raw registers added.

In a negative preparation Hminus occupies7 throughout,
so every bridge fails and all acquisition bits are0.
In a positive preparation7 starts free. In the no-fault
case every worker has passed its proposal before C_i
can hold; choose the earliest actual bridge proposal.
Before it no bridge exists and7 is free, so it succeeds.
That worker writes its correct P1 before clearing its
bridge. Consequently at least one final c_i is1.
There may be several sequential winners; no independence
or one-winner assumption is made. Therefore

    sigma(original J)=OR_(i=0)^(k-1) c_i                    (7)

at every all-certified state.

For an actual COMMAND implementation, a further, separate
old OR-gate interface is needed: it accepts complete P0/P1
registers and an actual encoded constant1, uses a licensed
disjoint workspace, preserves the raw registers and source,
and returns a complete encoding of their Boolean OR with
gate cleanup. Given THAT interface, the certified state
satisfies its data-readiness and worker-cleanup premises,
so its correct result is sigma. The Boolean assertion(7)
is proved here; the45-instruction majority construction,
its47k-49 gate accounting, workspace inventory and BRC
execution certificate are NOT independently verified here.

Likewise a later source-restoration procedure must retain
its own actual input restriction and licenses. We do not
claim that blindly reserving A/B reconstructs every one
of the nine initial preparations. The certificate supplies
a cleaned N(J) and stable raw markers, not an unproved
restoration procedure or free access to the original
hidden matching.

This closes the precise mathematical readiness obligation
relative to the typed observer and separately stated join
interface. It does not close physical detection, Native
mapping, actual completion signaling or provenance of the
old execution package. A production language without the
permitted occupied/free observation cannot consume(5)
by simply treating it as a new primitive.

## 6. Global omission budget, exact coverage and safety boundaries

The same certificate is valid in the orphan's PROTECTED
omission contract, with the following precise interpretation.
At most F calls in the ENTIRE schedule are completely omitted.
The opening is repeated F+1 times before workers. Worker i
has t_i>=1 consecutive bridge-proposal positions, followed
by steps2-8 of(2), each primitive position repeated F+1 times.
No phase or worker gets a fresh omission budget.

Every protected local position has at least one actual
execution. For reserve/release on this exclusive private
projection, consecutive repetitions after the first
effective transition are state no-ops, and omitted calls
are no-ops. Thus during the protected private reader/cleanup
the local state follows the prefixes in(4) with stutters.
The private bridge, once acquired, cannot disappear before
its protected cleanup; after cleanup repeated release(u)
cannot remove another worker's bridge because u is private.
Hence the same equivalence(6) and stability hold at ALL
reachable prefixes of this protected schedule.

This argument deliberately does NOT treat arbitrary shared
bridge retries as harmless. During a bridge-proposal block,
other workers may acquire or clear7. A worker that has not
yet succeeded may succeed on a later actual proposal.
Once its own bridge succeeds, it holds u/v until its reader
finishes, so its later identical proposals have no effect.
After the block, its acquisition bit is well-defined and
the private trace above applies. Before the block completes
its outputs are empty, so C_i cannot spuriously hold.

If sum_i t_i>F, at least one actual bridge proposal occurs.
When all C_i hold, every worker has passed its proposal
block. The earliest actual proposal in a positive source
must succeed; negative Hminus blocks all. Therefore(7)
continues to hold under this GLOBAL omission budget.
Any separately invoked OR command implementation must
also meet its own protected-omission contract; readiness
alone does not prove its gate reliability.

Contact coverage is a separate indispensable hypothesis.
If sum_i t_i<=F, all bridge proposals can be omitted.
Both source signs can then produce all-correct P0 registers,
with every C_i true, and the same private auxiliary state.
Thus the new readiness certificate does not magically
supply missing source evidence. Its role is precisely
valid-record/cleanup certification, not a replacement
for sum_i t_i>F.

If private-reader protection or private exclusion is
removed, the source report's failures remain outside
our theorem: omitting an unprotected probe can fake1;
an outside event occupying v can masquerade as a bridge.
If a worker is paused forever before its marker/cleanup,
its C_i need never occur. Neither fairness, starvation
freedom, crash recovery nor bounded physical waiting
follows. No old STOP or scientific execution authority
is revived to test these alternatives.

## 7. Exact fresh inputs, selected code-reading boundary and authorship

Repository awdawmip/enterprise-math. This was a bounded
orphan intake, not an inherited run, its author identity,
registration or execution permission.

(1) Actual complete RESULT, personally read opening and
all Sections1-7:
 Source b1dfa3ab3995caead6c447fae1bf42defe210784
 research_notes/chatgpt_direct/20261017_residual_contention_evidence_83c2af/RESULT.md
 8869 UTF8bytes
 SHA256 e038d68df18024dbd84cee8f70816860cdbfc32f0f782ec5ee044cc7629d9bf3
 Gitblob 2e80a80a0914ca097c5381eae84623836d7bc76d.

(2) Actual complete companion CHECKPOINT:
 Source aab824a273427099b4d5c20ca1442964ce0fec99
 research_notes/chatgpt_direct/20261017_residual_contention_evidence_83c2af/CHECKPOINT.json
 1966 UTF8bytes
 SHA256 37ebfaf0c037a074941ebca9334c3ad26229b5407f9429e65092e34e1241c5e3
 Gitblob 1ead16a847ea06da60de3ebe49208df31b9c143b.

The original checkpoint explicitly says
UNREVIEWED_CONDITIONAL_PROOFS_AND_TYPED_BRC,
independent_review:false and activity_binding:
NOT_VERIFIED_THIS_TURN. Its native_mapping:false,
previous blocked recovery mutation not rerouted,
and read-only configuration not granting research
authority all remain. The report's own claimed
execution status is attributed to its author.
I did not verify its activity, execute its913220
assertions, reproduce its17 shuffle/12 joined families,
read all seven primitive sources, install its ZIP,
accept all old parent results or independently audit
its45-command majority gate. No Source transaction
comparison of the old publications is fabricated.

(3) Exact exchange-wrapper blob fetched as one immutable
repository blob, whole body returned and saved:
 f45165d7144d342d6cf9233ea77a04a51d2b96e3
 12776 UTF8bytes
 SHA256 cb4bde8daa333d305aa4ec19fcc185123990164f7879e13093bb4d6f05cf6ea6.
Actual semantic reading was ONLY its top docstring
and complete step function, lines48-54: op-type and
declared-reserve-library checks, then membership.full_step.
The rest of its code was NOT whole-reviewed or run.

(4) Exact membership blob fetched as one immutable
repository blob, whole body returned and saved:
 be1b60446e31c2c8489d1ce0db16cc1e952d11c8
 13417 UTF8bytes
 SHA256 0436b8c0d283333d3dc3adfc44ca57af77c3c06867cd0471ae8c121d81e81adc.
Actual semantic reading was ONLY the top docstring and
complete canon/blocks/used/sigma/observed/full_step/
abstract_step definitions, lines32-67. These pay the
literal transition and typed occupancy observer in
Section1. The rest of the kernel/tests/import chain
was NOT wholly reviewed, imported or executed.

Actual original method arguments and ENTIRE results
of all four managed reads were preserved BEFORE
interpretation or assertion, and are saved together at
 /workspace/enterprise-math/research_notes/owner_goal_20261017/foreign_residual_contention_orphan_intake_4a56e9/FOUR_EXACT_ORIGINAL_SOURCE_AND_NEEDED_CONTRACT_CALLERS_RAW.json
and functions store
 foreign_residual_orphan_full_actual_intake_and_needed_contract_record.

The two report/checkpoint bodies were genuinely wholly
read. Complete tool return of a code blob is not falsely
called full semantic code reading. A local display
attempt initially assumed the blob content was JSON;
its parse error was retained. A subsequent overly large
display duplicated nested content and was truncated.
All original responses were already fully saved; the
necessary complete definitions were then read in a
bounded selected output without another API call.
These are local display boundaries, not evidence of
MCP/CAS/scientific-kernel failure.

The original run owns its model, licensed private
bridges/eight-step acquisition record, arbitrary-shuffle
and contact-budget observations, executions and their
unreviewed histories. I do not claim its existing
eight-step word or OR law as my new mechanism.
This appendix independently repays those finite
state traces to ground the NEW exact occupied/free
readiness-and-cleanup predicate, prefix equivalence,
stability and safe consumer conditions. Those new
arguments are EM-P11-4A56E9's manual construction
NONZERO. Root supplied only the orphan locator
and routing, no mathematical construction or vote.
No prospective reviewer supplied a formula or repair.

## 8. Chronology, current actual authority and exact remaining state

Before the orphan route I had only its topic metadata,
not its report, formula or construction/repair.
After actual intake, my manual new-certificate construction
is NONZERO. This is ordinary nonself research with all
old warm/NONBLIND history retained, not a cold restart.
A future reviewer must use its own real history and
necessary actual input custody; nothing preassigns
its zero exposure or migrates an old peer vote.

Same actor EM-P11-4A56E9:
 SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9,
 RA RA-C193E2AA39B9A6A6DDBB69B3.
Actual current36/175 remains Source
aa206ce72426db583d71a66e5b7a453695936c5e, root
/workspace/control_worktrees/4a56e9-published36-source-aa206ce-20261017.
The original Source36 startup/sameevent checkpoint
genuinely closed0/debt[] with five formal flagsfalse.
This is prior binding REUSE, not a new guard claim.
Source identity remains non-platform-attested,
original RA state KNOWN and formal budget UNKNOWN.
All STOP/HOLD/errors/false endings remain, Goal OPEN.

Only original ordinary/manual read permissions were
used. I do not inherit the orphan author's denied
operations, Native observer mapping, activity binding,
run identity, shared-window permission or any GBRC/
R1-01/old-M7 scientific budget. No registration, new
identity, scientific program/import, enumeration,
external query, solver or experiment was performed.
The static text tools merely save/read this authored
prose and its new byte identities. No helper37, RA
append, Source/main mutation or formalTask is implied.

The complete new finite proof was sent to Root in chat
before this first persistence. This is newly written
same-family context, not recovery of old report bytes
and not modification of either foreign source.
First actual complete self-reading and new byte pins
will freeze this V1 exactly once. New author Source,
independent whole/context technical review, peer
Source and ordinary acceptance remain PENDING at
creation. They require their actual later chronology.

Terminal at AUTHOR level: exact typed readiness
certificate proved, conditional join safety paid;
fairness/physical completion/Native mapping/old
execution certificates and old activity remain OPEN
or HOLD as above. The parent Goal is not declared
finished, and the conditional result is not upgraded
by Source publication or an old author's program run.

