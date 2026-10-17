# Two complete triple matchings can require unbounded transient vacancy

First complete AUTHOR COMPOSE APPENDIX V1 / UNREVIEWED.
Sole new mathematical author: EM-P11-4A56E9, same warm actor/RA/SID.
Root routes and supplies zero mathematical votes.
One bounded conditional RESULT_ONLY / COMPOSE appendix to the
existing typed-exchange family; not a new paper, Tool, native
geometry, force, energy or gateway-contention conclusion.
New author Source, independent technical whole/context, peer
Source and ordinary acceptance are PENDING at creation.

## 1. Literal category, actual new question and complete statement

Use precisely the actual matching-state operations of the pinned
exchange/membership input. A state is a finite disjoint matching
of licensed three-member events. Reserve a licensed triple only
when all its members are free; otherwise the state is unchanged.
Release(x) removes the unique current triple containing x, or does
nothing if x is free. Each is one atomic model command. Release
does not mean deleting just one member, reserve does not overwrite
an old event, and a multi-event exchange is not one primitive.

Fix a finite inventory I and a declared library H. No event outside
H, auxiliary member outside I, outsider occupation, alias release,
new primitive or atomic multi-triple macro is allowed. For any
state J write

    vacancy(J)=|I|-|used(J)|.

This counts free MODEL MEMBERS relative to the declared starting
inventory. It is not energy, physical volume, cost, time, axes or a
native-force observable. The following is a pointwise finite state
theorem, not a claim about weights of histories or their probability.

The old selected cyclic code gives a rolling construction with
peak vacancy9 for a particular one-dimensional family. The new
question is whether some constant independent of library size
works for EVERY pair of complete triple matchings when H consists
only of their two sets of triples. We give a negative answer.

For every integer m>=3, set n=m^2. We explicitly construct I_m with
3n members and two complete triple matchings J_A,J_B such that:

    (i) both endpoints occupy all of I_m;
    (ii) the full-occupancy H-fiber is exactly{J_A,J_B};
    (iii) every finite legal word from J_A to J_B, including
          arbitrary backtracking/re-adding old events, has
          peak vacancy at least3 ceil(m/3)>=m;
    (iv) a legal2n-command word exists, and2n commands is the
         exact minimum length.                               (1)

A simple upper bound on peak vacancy is3n. We do NOT compute the
exact optimal peak vacancy between these bounds. In particular,
(iii) rules out every universal constant bound over this family;
it is not a no-reachability theorem.

## 2. Explicit finite inventory, licenses and endpoint matchings

Let T=(Z/mZ)^2, with e1=(1,0), e2=(0,1). These are finite labels,
not spatial/native axes. Introduce three distinct members x_p^a
for every p=(i,j) in T and a in{0,1,2}. If ordinary integer labels
are desired, use

    x_(i,j)^a = 1+3(mi+j)+a, 0<=i,j<m.

This is an injection into positive integers and supplies exactly
3m^2 members. All additions/subtractions in p are modulo m.

Define the licensed events

    A_p={x_p^0,x_(p-e1)^1,x_(p-e2)^2},
    B_p={x_p^0,x_p^1,x_p^2}, p in T,
    H_m={all A_p and all B_p}.                               (2)

J_A is the matching of all A_p; J_B is the matching of all B_p.
The A events partition I_m: x_q^0 appears in A_q, x_q^1 in
A_(q+e1), x_q^2 in A_(q+e2), exactly once each. The B events
partition it by their own index. Every event has exactly three
distinct members.

No A_p equals a B_q: their0-labeled member would force p=q,
but their1-labeled member would then require p-e1=p, impossible.
Within each family the events are distinct. Thus H_m has exactly
2n events. A_p meets B_q precisely when p is q,q+e1 or q+e2;
for m>=3 these indices are distinct and each such intersection
has one member. No other event is implicitly licensed.

This is a NEW explicitly declared finite conditional library using
the old primitive semantics. It is not a claim that P000 or a native
action law has already supplied these licenses or that an old run
has installed/executed this instance.

## 3. Exactly two full-occupancy states, with no hidden alternatives

Form the bipartite incidence graph with left vertices A_p and
right vertices B_q. Each model member is one edge joining its
unique A-owner to its unique B-owner. B_q has neighbors

    A_q, A_(q+e1), A_(q+e2).                                (3)

This graph is connected: A_q--B_q--A_(q+e1) and the corresponding
e2 path allow both cyclic translations, which generate T.
Every B_q is adjacent to its A_q.

For a matching J in H_m that covers all I_m, let alpha_p
and beta_q be its0/1 indicators for A_p and B_q. For every
incidence edge/member, exactly ONE of its endpoints must
be selected: at least one because the member is occupied,
and at most one because J is a disjoint matching. Hence

    alpha_p+beta_q=1 for every incidence edge.

Along a two-edge path all left indicators are equal.
Connectivity forces every alpha_p to one common alpha
in{0,1}, and every beta_q=1-alpha. If alpha1, J=J_A;
if alpha0, J=J_B. Conversely both are full by Section2.

Thus the full-occupancy fiber really is exactly two states.
The proof uses actual matching identity; static occupancy
equality alone would not justify this enumeration.

## 4. A bound for EVERY intermediate matching, not a monotone-word assumption

Let J be ANY matching of H_m, regardless of how it was reached.
Put S={q:B_q is present in J}. All A-events adjacent to a
present B must be absent. The neighbor index set is exactly

    N(S)=S union(S+e1) union(S+e2).

There are n left events in all, so at most n-|N(S)| A-events
can be present. Since exactly |S| B-events are present and
there are no other licensed types,

    |J|<=n-|N(S)|+|S|.

Every event in a matching occupies three distinct members.
Therefore

    vacancy(J)=3n-3|J|
               >=3(|N(S)|-|S|)
                =3|N(S) minus S|.                           (4)

This holds at each actual legal state, including histories
with any number of failed reserves, old-event reinsertions,
new-event releases or other backtracking. Nothing assumes
a greedy, monotone or shortest word. We will apply it at
one forced intermediate target-event count.

## 5. Complete elementary finite-torus boundary lemma

For S subset T with

    m^2/3<=|S|<=2m^2/3,

we prove

    |N(S) minus S|>=m/3,
    hence |N(S) minus S|>=ceil(m/3).                         (5)

Call a horizontal cyclic row mixed if it is neither empty
nor full in S, and let r be the number of mixed rows.
Each nonempty proper subset of a cyclic row contributes
at least one member to(S+e1) minus S. Otherwise translation
by+1 would preserve that subset, which, since+1 generates
Z/mZ, would make the nonempty subset full. Contributions
from different rows are distinct. Thus if r>=m/3,
the horizontal boundary already proves(5).

If r<m/3, there must be a full row. Otherwise every element
of S lies in a mixed row and

    |S|<=r(m-1)<m^2/3,

a contradiction. There must also be an empty row. Otherwise
every element of T minus S lies in a mixed row and the
same inequality contradicts |T minus S|>=m^2/3.

A full row and an empty row mean every vertical cyclic
column is mixed. Each column contributes at least one
member to(S+e2) minus S by the same cyclic-translation
argument, and different columns give different members.
The vertical boundary then has at least m members,
which is stronger than(5). This exhausts the two r cases.

We only use that N(S) minus S CONTAINS either directional
boundary. We do not add their cardinalities or wrongly
assume the horizontal and vertical boundary are disjoint.
The proof is finite integer counting for every m>=3,
including composite m; no expansion theorem or external
isoperimetric result is imported.

## 6. Forced transient vacancy, finite reachability and exact command length

Consider ANY finite legal reserve/release word beginning
at J_A and ending at J_B. The number of B-events present
begins at0 and ends at n. A single reserve/release changes
that number by at most1: a successful B-reserve adds1,
a release of a B removes1, and all other cases change0.
It must therefore pass through

    |S|=floor(n/2).

For m>=3, this count lies between m^2/3 and2m^2/3.
At that actual intermediate state, (4)-(5) give

    vacancy>=3 ceil(m/3)>=m.                                (6)

No monotonicity of |S| or of the word was assumed. Thus
backtracking cannot evade this lower bound. Given any
fixed proposed vacancy bound C, choose an integer
m>=3 with m>C. No legal word in this explicit library
connects its endpoints while staying below that bound.
This is the claimed failure of a size-independent bound.

The endpoints are nevertheless reachable. First release
x_p^0 once for every p, removing the corresponding old
A_p. While doing so, each x_p^0 still has its own A_p
until that removal; all old A events are mutually disjoint.
After these n commands the matching is empty. Reserve
every B_p in any order: these n events are mutually
disjoint, so all are legal. This is a2n-command word
with peak vacancy3n.

Every old A_p is absent from J_B and is distinct from
every B-event. Only a successful release can remove it,
and one release removes at most one current event.
There must be at least n actual successful releases.
Each target B_p was absent initially and only its own
successful reserve can introduce it, requiring at least
n successful reserves. A primitive cannot perform both
jobs. Hence any connecting word has length at least2n,
and the displayed word attains that minimum.

The resource conclusions are therefore precise:

    minimum commands = 2m^2;
    optimal peak vacancy is between
       3 ceil(m/3) and 3m^2.                                 (7)

We assert no sharper vacancy optimum or speed comparison.
The source and target being only two full states does
not mean one atomic event can swap them.

## 7. Coverage, exact actual inputs and real reading boundary

This work followed a genuinely new orphan intake under
the original actor's ordinary read-only/manual permissions.
It did not inherit the foreign run's identity, activity,
science budget or denied operations. Repository is
awdawmip/enterprise-math.

The actual primitive contract was read from two pinned
repository blobs, with complete original tool returns
saved and their new returned byte identities checked:

 exchange wrapper:
 f45165d7144d342d6cf9233ea77a04a51d2b96e3,
 12776 UTF8bytes,
 SHA256cb4bde8daa333d305aa4ec19fcc185123990164f7879e13093bb4d6f05cf6ea6;
 https://api.github.com/repos/awdawmip/enterprise-math/git/blobs/f45165d7144d342d6cf9233ea77a04a51d2b96e3

 membership:
 be1b60446e31c2c8489d1ce0db16cc1e952d11c8,
 13417 UTF8bytes,
 SHA2560436b8c0d283333d3dc3adfc44ca57af77c3c06867cd0471ae8c121d81e81adc;
 https://api.github.com/repos/awdawmip/enterprise-math/git/blobs/be1b60446e31c2c8489d1ce0db16cc1e952d11c8

The actual SEMANTIC reading was:
- exchange top docstring and complete step, lines48-54:
  allowed command names, reserve license check, call to full_step;
- membership top docstring and complete canon/blocks/used/sigma/
  observed/full_step/abstract_step, lines32-67: actual matching
  transitions and frozen-interface observer;
- in this NEW pass, additionally the complete exchange definitions
  cyclic/test_cycles/complete_cases, lines143-177 and208-219,
  honestly read from the already saved actual code, no new API.

This is NOT a claim to have whole-reviewed either full kernel,
its dependency imports, old execution certificate or all old
mathematical publication coverage. The extra selected reading
occurred AFTER the earlier readiness22220 freeze; its earlier
narrow reading history was not retroactively broadened.

The actual selected old code constructs the particular1D cyclic
family and checks n3..12, using a rolling word with peak9.
It also includes small complete-library cases. The present
2D incidence family and all-path resource conclusion are not
literally supplied in those selected definitions. This is
only personal bounded coverage, not a library-wide novelty
or absence theorem. The old family is not contradicted;
the general constant bound would have been an unsupported
extension of it. No old computational count or peer vote
is used as proof of(1).

All four original orphan/source/contract managed-call wrappers
and entire returns, including these two code bodies, are at
 /workspace/enterprise-math/research_notes/owner_goal_20261017/foreign_residual_contention_orphan_intake_4a56e9/FOUR_EXACT_ORIGINAL_SOURCE_AND_NEEDED_CONTRACT_CALLERS_RAW.json.
The source report and CHECKPOINT were actually whole-read,
respectively8869 and1966 bytes:
 b1dfa3ab3995caead6c447fae1bf42defe210784:
 research_notes/chatgpt_direct/20261017_residual_contention_evidence_83c2af/RESULT.md;
 aab824a273427099b4d5c20ca1442964ce0fec99:
 research_notes/chatgpt_direct/20261017_residual_contention_evidence_83c2af/CHECKPOINT.json.

Their worker-readiness question motivated opening this old
typed family, but their private-worker mechanism, OR circuit,
execution counts or complete source-history claims are NOT
logical premises of the torus theorem. No whole scientific
program was imported or executed. Original
UNREVIEWED_CONDITIONAL_PROOFS_AND_TYPED_BRC,
independent_review:false, activity_binding NOT_VERIFIED,
native_mapping:false and blocked-recovery history stay
unchanged. We do not promote that run, its BRC weights,
913220 assertions,45-command gate or a physical measurement.

The prior readiness appendix is a DIFFERENT bounded theorem.
Its state certificate/Source/review is not used to prove
the present vacancy obstruction. Neither C27/C28 calibration
nor the finite-chain free-group work is a hidden input here.

## 8. Authorship, limits, kills and current actual state

The new finite torus library, exact full-fiber proof,
all-intermediate-state neighbor inequality, elementary
boundary lemma and all-word barrier application are
EM-P11-4A56E9's independent manual construction NONZERO.
Root supplied only a previous orphan locator and routing,
zero mathematical construction or votes. Other actors
did not supply a formula, witness or repair for this proof.
A prospective NONBLIND technical reviewer must retain its
real history; no zero-private-candidate qualification is
prefilled and no selected-source read is called its whole.

The trial would have stopped REUSE if the actually read
old interface already stated the complete general result;
would have stopped if the bound only applied to monotone
words; and would not claim a primitive theorem if it
needed an atomic multi-event exchange. The explicit
construction and Sections3-6 pay the genuine finite
obligation without those shortcuts.

The license restriction is indispensable. If extra
triples, auxiliary members, outside occupancy/release,
a different macro primitive or an enlarged interface
are allowed, the inequality using only A/B event types
need not apply. This proof neither rules out nor proves
a low-vacancy route in such altered models. In particular
it is not a universal no-go for an unrestricted complete
triple library or an original Native mechanism.

The torus labels are bookkeeping for a finite incidence
graph, not FCC/120-degree geometry, six axes, physical
space or an allowed original source operation. Vacancy
counts missing inventory members only. Minimum command
length is a model count, not physical time. No statements
about history weights, scheduling probabilities,
starvation, fault tolerance, material response, force
or gateway/backend contention follow.

Same original actor EM-P11-4A56E9 retains
 SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9,
 RA RA-C193E2AA39B9A6A6DDBB69B3.
Actual current36/175 remains Source
aa206ce72426db583d71a66e5b7a453695936c5e and root
/workspace/control_worktrees/4a56e9-published36-source-aa206ce-20261017.
Its original startup/sameevent checkpoint actual0/debt[]
and five formal flagsfalse are honest prior binding
REUSE, not a new guard. Original non-attestation,
RA state KNOWN, formal budget UNKNOWN and all
STOP/HOLD/errors/false endings remain, parent Goal OPEN.

No helper37, RA append, new identity/budget, scientific
program/import, solver, enumeration, external search,
Source/main mutation or formalTask permission occurred
for this new proof. Existing code was read as text only.
Text tools merely write/read this one complete prose
artifact and its new byte identities. It is not a new
paper or generic Tool, and it does not close Native,
old missing caller or original denied-operation debts.

The complete new proof was first sent to Root in chat.
This is its first new persistence, not restoration of
old bytes and not a patch to readiness22220 or another
frozen author file. An actual complete self-read and
new UTF8length/SHA256/Gitblob will freeze this V1 once.
New author Source, independent complete technical
whole/context, peer Source and ordinary Source-bound
acceptance remain PENDING at creation and must follow
their true later chronology. Until then the result is
AUTHOR-PROVED / UNREVIEWED conditional COMPOSE.

