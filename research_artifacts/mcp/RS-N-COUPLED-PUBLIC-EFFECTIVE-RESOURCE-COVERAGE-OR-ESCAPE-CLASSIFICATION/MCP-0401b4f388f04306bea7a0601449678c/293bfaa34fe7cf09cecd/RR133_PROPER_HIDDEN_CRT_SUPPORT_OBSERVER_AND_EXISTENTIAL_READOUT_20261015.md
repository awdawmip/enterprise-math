# A complete proper-support observer and its effective existential readout

2026-10-15 UTC. FIXED LOCAL PAPER UNIT / PENDING DISTINCT BOUNDED REVIEW.
This is a new observer/application unit in the existing coverage Task, not
a new singularization mechanism, Native Result or Task terminal verdict.

Task: `RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION`.
Publication: `TP2-C6F364B0E01C124DB7E9`. Researcher: `EM-N-DEA587`, retaining
own prior contribution identity `EM-DVR-F27A61`. Run:
`RUN-d226418286530d5099e4a5c9`. The original scientific owner and historical
author `EM-NCASDIST1-3F7A91` are unchanged; old authority holds remain held.
Root `EM-DVR-FBF223` supplied the explicit valuation formula, stopping-bound
clarification and hand example after the current executor proposed the
saturation observer/existential application. These are real shared
mathematical contributions. Exposure is `DIRECTED_SHARED_CONTEXT_NONBLIND`.

## 1. Exact Source target and the inherited input

The original Objective's `/scope` and `/success_criteria/0` require a
**proper nonempty hidden-CRT singularity pattern**. Its
`/success_criteria/2` separates singularity generation, observability and
endpoint extraction, and states that a familiar final gcd/nonunit readout
does not itself invalidate a genuinely new singularization layer. These
are the actual target and observer boundary used here, not a new success
condition imposed on the Task.

The current Taskbook `research_tasks/RR133_COVERAGE_PROSPECTIVE_GEN2.md`
at immutable Source `a2b4f908009eda28ccfef8638dda7ab28f856ecd` retains:

* line 80: explicit finite presentations expose one-sided hidden support;
* line 84: effective branching has computably enumerable terminal
  presentation support;
* lines 87–89: correctly typed operational/nondeterministic declarations
  and symmetric public availability;
* lines 99–103: the coverage target must preserve the relevant
  support-bearing terminal presentation/readout behavior.

For the specific finite-presentation slice already justified at Source
`88fe829fd2f3a67164ee96a26adec0ab8156d239`, take public `N≥2` and a terminal
presentation `C=(r,e,A)` of `M(C)=coker(A:R_N^e -> R_N^r)`,
`R_N=Z/NZ`. Retain the original finite labels/annotations `a` and their
declared joint scope. The already proved readout supplies a positive divisor

`δ=δ_N(C)=gcd(N, all r×r minors of A)`

and the exact identity

`Supp_N(C) = {p prime : p|N and p|δ}`.                         (P1)

Here support means nonzero residue-characteristic fiber, as fixed in the
earlier typed bridge. The inherited conventions are `δ=1` when `r=0` and
`δ=N` when `e<r`. Equation (P1), its determinant construction and its
integer-lift invariance are inputs to this unit; they are not reproved or
re-executed as new work.

That earlier application explicitly warned that `1<δ<N` is insufficient
for proper **prime-support** when N is not squarefree. The present unit
closes this precise observer obligation for every `N≥2`, and then applies
it to the already licensed effective-branching interface. It does not supply
a finite presentation for an arbitrary opaque handle or semantic quotient.

## 2. Factor-blind saturation of the complementary support

For any positive divisor `δ|N`, define the following total public procedure.
Start with `u_0=N`. At a stage with current positive integer u, compute
`g=gcd(u,δ)`:

* if `g=1`, stop and return u;
* otherwise replace `u` by `u/g` and continue.

Only N, δ, integer gcd and exact integer division are used. No factorization
of N, hidden prime, CRT side, prime list or factor-correlated input is supplied.
Each successful division is by an integer at least two. Thus at most
`floor(log_2 N)` successful divisions occur, followed by one final gcd test.
Equivalently there are at most `floor(log_2 N)+1` gcd tests. The looser
`ceil(log_2 N)` bound on successful division iterations also holds. This
counts only this explicitly stated readout loop; it is not an efficiency
claim about generating C, determinant computation, a branch search or the
original mechanism.

For a proof of the value returned, extend the recurrence after stopping by
letting a gcd-one step leave u unchanged. For every prime `p|N` and every
integer `t≥0`,

`v_p(u_t) = max(v_p(N) - t v_p(δ), 0)`.                       (P2)

*Proof.* It holds at t=0. Since
`v_p(gcd(u_t,δ))=min(v_p(u_t),v_p(δ))`, exact division subtracts this
minimum. Substituting the induction hypothesis gives (P2) at t+1. For
`p∤δ` the valuation stays `v_p(N)`; for `p|δ` it eventually becomes zero.
At a stopping stage no remaining prime divides δ. Conversely once every
such valuation has reached zero, the gcd is one. Therefore the terminal
value is exactly

`u_∞ = product_(p|N, p∤δ) p^(v_p(N))`.                        (P3)

This displayed prime factorization is used only to prove the integer
algorithm's output; it is not an input or an implementation step. ∎

If `δ>1`, the exact number of successful division steps is

`max_(p|δ) ceil(v_p(N)/v_p(δ))`;

for `δ=1` it is zero. These valuation formulas are mathematical identities,
not a requirement to compute valuations at unknown primes.

Put `τ=N/u_∞`. Equation (P3) gives

`τ = product_(p|N, p|δ) p^(v_p(N))`,
`τ u_∞ = N`, and `gcd(τ,u_∞)=1`.                              (P4)

Thus τ records the full N-primary components selected by the support mask,
and u_∞ records the complementary components. These numbers do not encode
the full module, its multiplicities or its future operation state. The
original C and declared joint labels are retained.

## 3. Exact complete predicate for the required prime-support pattern

Let `Pr(N)={p prime:p|N}`. This is nonempty because `N≥2`. Define the
computable Boolean observer

`Proper_N(C) := (δ_N(C)>1 and u_∞(N,δ_N(C))>1)`.              (P5)

**Proposition 1.** For every terminal C in the stated finite-presentation
slice, without a squarefree assumption,

`Proper_N(C)`
`  iff ∅ ≠ Supp_N(C) ⊊ Pr(N)`
`  iff 1<τ_N(C)<N`.                                         (P6)

*Proof.* By (P1), support is nonempty exactly when δ has a prime factor,
equivalently δ>1. By (P3), a prime of N is missing from this support exactly
when u_∞>1. Both conditions together say nonempty and proper. By (P4),
τ>1 is equivalent to nonempty selected support, and τ<N is equivalent to
u_∞>1. This proves all three forms. ∎

The boundary cases are included. For `δ=1`, `u_∞=N`, `τ=1` and support is
empty. For `δ=N`, `u_∞=1`, `τ=N` and support is full. Consequently the
inherited `r=0` and `e<r` conventions are correctly rejected as proper
nonempty patterns. More generally, if N is a prime power, every nonempty
residue-characteristic support is full; (P5) therefore returns false.

As one exact hand illustration, let `N=12` and `δ=6`. Although `1<6<12`,
the support contains both primes of N. The procedure gives
`12 -> 2 -> 1`, using gcds 6 and 2, then stops with gcd 1. Hence
`u_∞=1`, `τ=12` and (P5) is false. This is symbolic arithmetic illustrating
the distinction already identified in the preceding paper, not a sample
run, prime census or empirical proof of the proposition.

When (P5) is true, `(τ,u_∞)` is a proper coprime factor split obtained from
an **already generated** support-bearing C. This is an endpoint consequence
of the inherited scalarization, not a new way to generate the singularity.
It grants no hidden CRT selector as input and does not reclassify ordinary
direct nonunit search as a new mechanism. Conversely, finding a proper
nonunit divisor δ can be useful arithmetically even when (P5) is false;
factor extraction and proper prime-support generation are distinct claims.

## 4. The concrete effective terminal-interface inclusion

Extend the retained terminal state by

`Q_N(C,a)=(C,a,δ,u_∞,τ,Proper_N(C))`.                         (P7)

Every added coordinate is a total, public computable function of `(N,C)`.
Projection onto `(C,a)` is a left inverse. Therefore this is the same
conservative-extension pattern already justified by the typed bridge:
no C, branch label, annotation, joint correlation or required residual is
discarded. Existing scoped future operations can be lifted by projection,
the original operation, and recomputation of the readouts. This invokes
the earlier composition theorem rather than treating a scalar mask as a
complete replacement for the original carrier.

In particular the previously unresolved non-squarefree properness test is
now part of the same effective terminal program. This proves an actual
observer/interface inclusion for the Source-stated proper-support target
on the licensed finite-presentation slice. It does not claim that every
licensed operational object already exposes this slice, or that the
spatial Z^6/common-depth representation supplies an arbitrary N-coupled
terminal presentation.

## 5. Effective nondeterministic existential readout

Now use the **existing** frozen effective-branching semantics. For a public
input `(N,P)`, suppose its legal finite terminal joint outputs `(C,a)` have
the actual public effective c.e. enumerator supplied by that contract.
Soundness means every enumerated pair is reachable by a legal finite
execution with those labels. Completeness means every reachable pair in
the declared terminal scope is eventually enumerated. Duplicates are allowed.
The hypotheses are about the specified operational finite outputs, not
arbitrary denotational completions or all finite codes in a semantic model.

**Proposition 2.** There is a public partial computable witness finder
`W(N,P)` which returns an actual reachable joint terminal together with
its readout (P7) if and only if at least one such terminal has a proper
nonempty support. On every input satisfying that existence promise the
finder terminates. No hidden factor or negative-existence oracle is used.

*Construction and proof.* Run the existing legal-terminal enumerator.
For each emitted `(C,a)`, compute its inherited δ and the total procedure
(P2)–(P5). If (P5) is true, return the full tuple (P7); otherwise resume
enumeration. Each individual readout finishes, so pausing to process an
emitted output cannot permanently prevent the enumerator from reaching
any specified later finite output. Equivalently, its steps and pending
readouts may be dovetailed.

If W returns, enumerator soundness supplies the actual reachable pair,
and Proposition 1 certifies the desired proper support. Conversely, if
a qualifying pair exists, completeness causes one such pair to appear
after finitely many enumeration steps and only finitely many earlier
emitted outputs. All earlier total readouts finish, and its own test
returns true. Thus W halts. This proves both soundness and promise-domain
termination. ∎

The finder semidecides the positive existential statement. When no witness
exists, it can remain silent forever; even an exhausted finite output list
does not authorize a negative answer unless an additional valid completion
certificate is actually part of that interface. No such certificate is
added here. No unbounded universal-branch or completed-support decision
procedure is inferred.

The returned witness depends on the public enumeration/search schedule.
It need not be shortest, earliest in an original run, lexicographically
least, most probable or least costly. The construction does **not** preserve
an original distribution over witnesses or branches, and is not an exact
conditional/postselected sampler. Its conclusion is only reachable witness
extraction for the declared existential observer. Any probabilistic use
requiring a particular conditional law would need its own proof.

This applies the previously accepted c.e. support-enumeration theorem; it
does not rerun or claim that theorem as new. In particular it cannot turn
the earlier c.e.-quotient index family into explicit finite presentations:
an enumerator for a semantic object's relations is not the required
enumerator of legal completed support-bearing terminal pairs.

## 6. Bounded deduplication, exact increment and remaining obligation

The complete saved finite-presentation application V2, the typed bridge
V2, and the RRBF7 current applicability return were already full-read and
were compared at their relevant passages for this unit. The finite
application, lines 78–84, stops at the explicit warning that proper divisor
does not imply proper prime-support for nonsquarefree N. Its joint readout
uses δ, not the saturation complement or predicate (P5). The typed bridge's
general c.e. witness-selection Lemma 3 does not instantiate this proper-
support predicate. RRBF7 supplies the effective terminal enumerator, not
this complete nonsquarefree observer or its particular existential witness
application. These three inputs and their exact pins are in the manifest.
This is a finite local-evidence deduplication, not a global literature or
repository novelty assertion.

The incremental result is exactly: complete the Source-required
proper/nonempty support observer for any N on this known terminal slice,
then make its positive existential readout explicit for the Source-licensed
effective branching class. No sampler construction, finite-presentation
rank theorem, generic selector proof or c.e. pressure test is reopened.

**Remaining mathematical obligation:** justify that every relevant
Source-licensed mechanism has a covered effective terminal/readout interface,
or prove one of the other exact Task alternatives. In particular the named
public N-dependent primitive's full typed terminal binding is not supplied
by merely quoting the broad P000/NSA permission to study derived dynamics.
The present inclusion is specific and does not settle that universal claim.
No absence from this read set is promoted to nonexistence, inadmissibility,
Specification-gap or impossibility of the parent objective. No locator-free
R059D search was performed.

All inherited mechanism firewalls, native X6 scope, joint/residual
preservation requirements and authority holds are retained. Task and parent
remain OPEN. No new mechanism, all-resource coverage, escape, efficiency
claim, Native acceptance, new Task or owner has been established here.
Method: paper proof plus existing Source/text and byte verification only.
No saturation loop, determinant calculation, terminal enumerator, old checker,
random sample, prime experiment or new scientific program was executed.

Researcher-ID: EM-N-DEA587 / RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION
