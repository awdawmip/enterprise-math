# Two-control identification with an unknown shared reference flip in the literal positive bridge

First complete AUTHOR COMPOSE APPENDIX V1 / UNREVIEWED.
Sole new mathematical author: EM-P11-4A56E9, same warm actor/RA/SID.
This is one bounded conditional-model RESULT_ONLY / COMPOSE appendix
in the existing C27/C28 family, not a new principal paper, Tool,
physical calibration or claim that the upstream sources are accepted.
Root coordinates and supplies zero mathematical votes.
New author Source, independent whole/context review, peer Source and
final Source-bound acceptance of THIS appendix are PENDING at creation.

## 1. Exact original face, observation and new claim

Use the literal restricted face of the original C27 model already
specified and independently checked in my20586 appendix. Retain
the original bridge e0=1--2, with local target y=Y_e0 and reference
z=Z_e0, each in{+1,-1}. In the full old graph these are the original
cycle characters. The other couplings are set to their neutral
off-settings, so other coordinates/bins are still present and
uniform. This is an actual restricted face, NOT a claim about
the open family with all13 target strengths nonzero.

The three active positive factors are the original reference
face, old target-reference interaction and controlled target face.
For configuration u in{A,B}, the exact marginal joint is

    p_u(y,z)=(1+a_u z)(1+b yz)(1+w_u y)/
             [4(1+a_u b w_u)],
    0<a_A,a_B,b,w<1, w_A=w, w_B=cw, c=1/16.                 (1)

The same b occurs in both configurations. The two background
parameters a_A,a_B are unknown and may be equal or different.
The known c is the original target-control relation, not an
estimated control or arbitrary tuning parameter. Each of the
four probabilities is strictly positive; summing the expanded
numerator over the four signs gives4(1+a_u b w_u). No additional
normalization, hidden counting multiplicity or total-mass limit
is suppressed. Equal coordinate-fiber multiplicities of the
original graph were already paid in20586;(1) is the resulting
literal local law, not a freely chosen replacement Q.

Observe the complete two configurations of (Y,Z'), where

    Z'=Z H, H in{+1,-1}, E H=gamma, 0<gamma<=1.             (2)

Within each configuration H is independent of(Y,Z), target Y is
undisturbed, and the bias gamma is the SAME in A and B. There is
no requirement to couple the actual samples across configurations;
only the bias and the indicated conditional independence are
model conditions. Neither gamma nor the true Z is given. There
are no extra independent views in the data required by the theorem.

NEW bounded conclusion: the two complete reported four-cell
distributions uniquely determine ALL FIVE parameters

    (a_A,a_B,b,w,gamma) in the domain(1)-(2).                 (3)

In particular w remains identifiable even when a_A=a_B. The proof
has two observable cases and includes that exact degeneracy;
it does not assume backgrounds must vary. At gamma0 a literal
positive-face nonidentifiability example will show why the
boundary is excluded.

These independence, common-b/common-gamma, known-control,
positive-orientation and non-disturbance assumptions are EXTRA
restrictions. Successful reconstruction within the model does
not prove those assumptions describe an actual instrument.
The C28 general shared-error/latent-state ambiguity is not
contradicted outside this restricted family.

## 2. All actual reported moments and a common-interaction invariant

The full reported four-cell distribution supplies exactly

    m_u=E_u Y, s_u=E_u Z', v_u=E_u(Y Z').

A binary joint is determined by its total1 and these three
moments. Put t=w_u, a=a_u and Znorm=1+abt. Direct four-sign
summation of(1) gives the TRUE moments

    m=(t+ab)/Znorm,
    n=E Z=(a+bt)/Znorm,
    k=E(Y Z)=(b+at)/Znorm.

Independence in(2), with unchanged Y, gives

    s=gamma n, v=gamma k.                                  (4)

Define solely from the report

    e_u=1-m_u^2,
    d_u=v_u-m_u s_u,
    f_u=v_u^2-s_u^2.

Expansion of(4) pays the exact identities

    e=(1-t^2)(1-a^2 b^2)/Znorm^2,
    d=gamma b(1-a^2)(1-t^2)/Znorm^2>0,
    f=gamma^2(b^2-a^2)(1-t^2)/Znorm^2.                      (5)

The letter f here is just this reported scalar invariant,
not a polynomial or a changed parameter in the old graph.
In particular both d_A,d_B are nonzero under the stated domain.

For an individual TRUE four-cell joint, let p++ mean
p(Y=+1,Z=+1), and analogously for the other three signs.
The interaction odds ratio cancels the a and t factors:

    R_b=p++ p--/(p+- p-+)=[(1+b)/(1-b)]^2.                  (6)

To express it through the reports, the moment form of its
numerator and denominator is
(1+k)^2-(m+n)^2 and(1-k)^2-(m-n)^2. Substitute(4) to obtain

    R_b=[gamma^2 e+f+2gamma d]/
        [gamma^2 e+f-2gamma d].                            (7)

The denominator is positive, not merely formally nonzero:
it is16gamma^2 p+- p-+>0. The corresponding numerator is
16gamma^2 p++ p-->0. Thus all cross-multiplication in(7)
is justified on the actual positive probability domain.

Since b is common to A and B, equality in(7) is equivalent to

    gamma^2(d_A e_B-d_B e_A)=d_B f_A-d_A f_B.                (8)

Indeed set X_u=gamma^2 e_u+f_u. Equality of
(X_A+2gamma d_A)/(X_A-2gamma d_A) and its B version
reduces to d_A X_B=d_B X_A; gamma>0 permits cancellation.
No numerical fit, noisy inversion or assumption that an
arbitrary matrix is positive is used.

## 3. Case I: the observable denominator is nonzero

Let

    Dobs=d_A e_B-d_B e_A.

If Dobs!=0, equation(8) uniquely determines

    gamma^2=(d_B f_A-d_A f_B)/Dobs.                         (9)

Gamma>0 fixes its unique positive square root. As the data
are assumed to come from(1)-(2), this value is in(0,1].
One then obtains n_u=s_u/gamma and k_u=v_u/gamma and the
actual TRUE cells

    p_u(y,z)=[1+m_u y+n_u z+k_u yz]/4.

For completeness their full parameter factorization is
unique, not just the target parameter. Define

    R_t=p++ p+-/(p-+ p--)=[(1+t)/(1-t)]^2,
    R_a=p++ p-+/(p+- p--)=[(1+a)/(1-a)]^2,
    R_b=p++ p--/(p+- p-+)=[(1+b)/(1-b)]^2.                  (10)

For a parameter x in(0,1), each relevant R is greater
than1 and the only such x is

    x=(sqrt(R)-1)/(sqrt(R)+1).

Thus the recovered A joint uniquely gives w,a_A,b,
and the B joint gives a_B and the consistent cw. This
proves uniqueness of all five parameters in Case I.

This is exact inverse reasoning on admissible distributions.
If arbitrary supplied reports violate positivity, the
gamma bound, common b or the known-control relation, the
theorem does not label them successful observations.
Clipping negative cells or silently adjusting a parameter
is not a step of the proof.

## 4. Case II: zero denominator has a complete, different resolution

The ratio in(5) is

    e_u/d_u=(1-a_u^2 b^2)/
             [gamma b(1-a_u^2)].

For x=a_u^2 in(0,1), its derivative is

    (1-b^2)/[gamma b(1-x)^2]>0.

Since d_A,d_B>0 and a_A,a_B>0, this proves exactly

    Dobs=0 iff a_A=a_B=a.                                  (11)

Positivity is essential to the implication from equality
of squares to equality of a. No hidden sign choice is made.

Put h=ab in(0,1). The two Y marginals now satisfy

    m_A=(w+h)/(1+hw),
    m_B=(cw+h)/(1+hcw).

Their observable combination cancels h:

    T=(m_A-m_B)/(1-m_A m_B)
      =(1-c)w/(1-cw^2).                                   (12)

All denominators are positive. The right side is strictly
increasing for0<w<1, since its derivative is

    (1-c)(1+cw^2)/(1-cw^2)^2>0.

It therefore determines a unique w. Existence is guaranteed
by the model assumption, without any numerical root
approximation. Recover

    h=(m_A-w)/(1-m_Aw).

The A report then gives two exact quantities

    alpha=(1+hw)(s_A-wv_A)/(1-w^2)=gamma a,
    beta =(1+hw)(v_A-ws_A)/(1-w^2)=gamma b.

These identities follow directly by subtracting the two
expressions in(4), and alpha,beta are positive. Since h=ab>0,

    gamma^2=alpha beta/h,
    a=alpha/gamma, b=beta/gamma, a_A=a_B=a.                 (13)

Again the positive gamma is unique. This resolves all
five parameters in Case II. It does not require a third
configuration, a known background, a nonzero Dobs or
the assumption that background changed.

Cases I and II exhaust the observed Dobs alternatives.
A second admissible parameter set giving the same
two reports must lie in the same case and obey the
same uniquely determined reconstruction. This proves(3)
as an identifiability theorem, not just an algorithm
that happens to find one solution.

## 5. Actual excluded-boundary failure, including original face realization

Gamma0 is genuinely different. Take H uniform and
independent, so Z' is uniform and independent of Y.
The two complete reports reduce to

    P_u(Y=y,Z'=z')=(1+m_u y)/4.

Use the SAME original face, b=1/2 and c=1/16, with
the following two strictly positive active parameter triples:

    (w,a_A,a_B)=(1/16,1/2,4/5),
    (w,a_A,a_B)=(1/32,115/206,526844/655867).                (14)

Substitution into(4) gives in BOTH models

    m_A=4/13, m_B=517/1282.

These are the exact positive-face instances already
fully paid in20586, now used at the actual gamma0
boundary. Each displayed active strength lies in(0,1),
the normalization is the same genuine form(1), and
the old other-coordinate bins remain uniformly present.
They are not arbitrary positive Q examples unrelated
to the old graph. The two w values differ, but ALL
reported bins in BOTH configurations coincide. Thus
target w, and hence the five-tuple, is not identifiable
at this excluded boundary.

The new positive-gamma theorem asserts exact uniqueness,
not uniform stability as gamma approaches0. Its Case I
formula can be ill-conditioned when Dobs is small;
Case II addresses exact degeneracy, not sampling errors.
No finite-sample confidence interval, statistical
efficiency, robust global lower bound or physical
calibration is deduced.

## 6. Relation to the actual C28 input and precise stopping point

C28 distinguishes known-channel correction from unknown
three-view calibration and from shared-H latent ambiguity.
My prior20586 attached interface only addressed a KNOWN
common binary channel, with the singular case demonstrated
inside the true face. Replacing a known error rate by a
different known number would be a closed standard variant;
it is NOT the new question or proof here.

Here gamma is unknown and not supplied by independent
three-view calibration. The net obligation is whether
the C28 shared-reference ambiguity survives the actual
restricted face and its known two-control relation.
The common b invariant and its full degeneracy resolution
settle that conditional question. Both cases are necessary
for the exact all-parameter assertion. No C28 theorem or
computational result about arbitrary reference strings
is silently imported as a premise.

There is no contradiction with C28 Section6: its latent
relabeling applies to a more general class. Here the
positive orientation, common interaction, common
independent flip, unchanged Y and known c impose extra
structure. Nor do we infer these restrictions from
agreement of a recovered model with observations.
That agreement is only a forward consistency check.

If gamma differs across configurations, H depends on
Y or Z, Y is disturbed, b varies across configurations,
the control relation is unknown, or the active strengths
are outside the stated positive face, this proof does
not apply. No claim of impossibility or sufficiency
in those categories follows. In particular a full
target-reference instrument, physical readout disturbance,
original all-strength graph fitting and independent
experimental calibration remain separate obligations.

The exact bounded trial would have stopped if the
observable invariant did not constrain gamma, if its
degenerate case retained a positive-parameter ambiguity,
or if the boundary counterexample required arbitrary Q.
Equations(8)-(14) pay these literal tests. No broad
search or exhaustion of all other noise models is
claimed. This unit stops at a conditional same-family
COMPOSE result, not a new neighboring parameter series.

## 7. Exact inputs, actual reading, authorship and unreviewed status

Repository: awdawmip/enterprise-math. The three records
below have different roles. Their status and personal
custody are not collapsed into one independent vote.

Original C27 model input, personally previously whole:
 Source2aec4cec863fdea638d6ac4f286be0c6342d2c90
 research_notes/divisor_extrema/20261017_c27_reference_cycles_conditional_separation.md
 10084 UTF8bytes
 SHA2563c8f250745990b943ab8f56113c9cd803af3cbcf9ab18e80cf9d68d2254a1e50
 Gitblob530c2f6305b5a4068852f330cc050df35559673b.

Only its actual model definitions/finite conditional
face are consumed. Original SELF_CHECKED_UNREVIEWED,
NONE_ALLOCATED/REGISTRATION_PENDING and the earlier
STATIC_READONLY_SCOPE_DENIED are preserved. I do not
proxy its author, allocate identity, revive execution,
write its ledger or accept its upstream C22/23,
calculation packages or physical mechanism.

My already independently reviewed conditional-model appendix:
 Sourcee4a2e86e5a8692a7446d0047b8cbe3ab43a1376f
 research_notes/owner_goal_20261017/c27_reference_character_compression_4a56e9/C27_ORIGINAL_CYCLE_REFERENCE_COMPRESSION_AND_LOCAL_TARGET_CHARACTER_CRITERION_COMPOSE_APPENDIX_V1.md
 20586 UTF8bytes
 SHA256a1e37184783fa394b69e9d6fd8f1350524d6f1b0cc4c6edabc602ccde0f080e6
 Gitblobdba60820b57a9c63b782469d18b4cf6dd666d4a4.

This is MY actual earlier author whole and Source;
its CF17939 genuine NONBLIND technical peer is
Sourcef96a5f2a097eb92bb2d18f2d969eda60d2de1c5c.
My full ordinary reception and own peer full/exact1
closed2/38525. That accepted scope is conditional
model only. It supplies the literal face realization
and exact old boundary instance, not a prior vote on
the NEW unknown-shared-flip theorem. Old whole/Source
evidence is honestly reused, without new old APIs,
body hashes, comparisons or duplicate independent votes.

New bounded C28 intake, personally one actual managed
full file read BEFORE this construction:
 Source8a912dc062e195cbe8c9d2afd0a7bc5fef1e5ed0
 research_notes/divisor_extrema/20261017_c28_reference_readout_calibration.md
 10829 UTF8bytes
 SHA25657ab46d57f110ce094ce4c789060eb047e067456489748ea25965d8fbfe35af2
 Gitblob750f87216985dc9e935a5065bc916982bf1ea7d9.
 Immutable URL:
 https://github.com/awdawmip/enterprise-math/blob/8a912dc062e195cbe8c9d2afd0a7bc5fef1e5ed0/research_notes/divisor_extrema/20261017_c28_reference_readout_calibration.md

Its complete opening and Sections1-9 were personally
read as an intake/coverage task. Original arguments
and entire result are preserved at
 /workspace/enterprise-math/research_notes/owner_goal_20261017/c28_bounded_source_intake_4a56e9/C28_ONE_EXACT_ORIGINAL_SOURCE_CALLER_RAW.json
and functions store
 C28_bounded_intake_one_exact_original_Source_caller.

This is ONE actual new Source GET. No new own compare
of that source's creation or false old comparison is
claimed. The original actual wrapper has no supplied
call_id; absent is not an observed explicit null.
C28's state is SELF_CHECKED_UNREVIEWED /
CONDITIONAL_OBSERVER_THEOREMS / NO_PHYSICAL_FIT,
Research-Activity-ID NONE_ALLOCATED; REGISTRATION_PENDING.
Its own earlier refusal history remains untouched.
The source calls itself an independent summary of
expanded notes/code; I did not read those full packages,
reproduce its counts or consume its cited experimental
papers/raw records. Its numerical checks, upstream
scope and physical claims are NOT independently
accepted by this intake.

C28 supplies the motivation and distinction of
shared-reference error from independent calibrated
readout. The theorem in Sections1-5 is fully derived
here from its stated finite law and extra assumptions;
C28's theorem proofs or computation package are not
hidden logical premises. A reviewer can identify
exactly which literal input/model facts are inherited
and which new finite algebra is self-contained.

Sole NEW author of the common-b calibration invariant,
observable two-case analysis, exact degeneracy
resolution and resulting five-parameter uniqueness
is EM-P11-4A56E9. New manual/private construction was
NONZERO before the full author chat sent to Root.
No formula, witness or repair was supplied by Root,
A, BFF or CF. Original C27/C28 model, readout framing,
general recovery/latent-alias observations and my
prior face/boundary construction retain their own
credits. No prior independent vote is migrated.

The complete proof was sent to Root before this first
persistence. This artifact is newly authored, not
restoration of old missing bytes and not a correction
to either original C28 or the already frozen
free-subgroup manuscript. It has not yet received
an independent complete artifact/context technical
whole review. A prospective NONBLIND reviewer must
state its actual history and personally ground any
needed Source; no input whole or zero-exposure
qualification is prefilled for it.

## 8. Same actual actor, chronology and exact remaining obligations

Actor EM-P11-4A56E9 retains
 SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9,
 RA RA-C193E2AA39B9A6A6DDBB69B3.

Actual current36/175 remains Source
aa206ce72426db583d71a66e5b7a453695936c5e with root
/workspace/control_worktrees/4a56e9-published36-source-aa206ce-20261017.
Its original startup and sameevent checkpoint genuinely
closed0, debt[], five formal flags false. That is
prior actual binding REUSE, not a new guard run.
The most recent protected free-subgroup publication
freshly observed the same SID/RA36 and exact175 directory
identity, without rewriting this authority history.
Public Source identity is not a platform-attested
MCP session; original attestationfalse/KNOWN state,
formal budget UNKNOWN, all STOP/HOLD/errors and warm
contribution history remain. Parent Goal is OPEN.

The distinct free-subgroup23443 author artifact now
has actual Source21773ee829ddaa7d4a8148e45cd098ef878ac80b,
own full/exact1 closure and independent review pending.
That is a different mathematical scope. Nothing from
this appendix is inserted into its fixed body,
publication transaction, verdict or original context.

This new work is after event36's fixedcut and is NOT
captured as a hidden checkpoint37 or extra readback.
No helper/RA append, new ID/session, budget reset,
main/Source write, scientific program, enumeration,
external query, fitting or physical experiment was
performed for this new proof. Text tools only write,
read and pin this one new document. Manual four-state
algebra is not a claimed execution of the original
C28 numerical package or upstream denied task.

After actual complete self-reading, new UTF8bytes,
SHA256 and Gitblob will freeze this single V1 once.
At creation its new Source and independent whole
review/peer Source/ordinary acceptance remain PENDING.
A later actual Source binding and genuine technical
whole review must follow their true chronology.
This is AUTHOR-PROVED / UNREVIEWED conditional COMPOSE,
not a new paper/Tool, physical result or ParentGoalFINAL.

