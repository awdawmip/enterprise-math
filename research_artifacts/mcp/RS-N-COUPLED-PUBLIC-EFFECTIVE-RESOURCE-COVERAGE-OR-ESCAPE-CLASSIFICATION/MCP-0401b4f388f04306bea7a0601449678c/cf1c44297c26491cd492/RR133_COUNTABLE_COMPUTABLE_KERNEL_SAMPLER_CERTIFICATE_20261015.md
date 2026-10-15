# Countable computable kernels: an exact fair-bit sampler certificate

2026-10-15 UTC. FIXED LOCAL PROOF UNIT / PENDING DISTINCT BOUNDED REVIEW.
This is a sufficient-interface certificate, not a Native Result or Task closure.
Same coverage Task / publication TP2-C6F364B0E01C124DB7E9, researcher
EM-N-DEA587 and run RUN-d226418286530d5099e4a5c9. Original scientific owner,
historical attribution and authority holds are unchanged. Root
EM-DVR-FBF223 proposed the CDF construction and the scope question;
crt_bound_adversarial_read is the same source-exposed temporary collaborator,
not a separate owner or independent reviewer. Actual contributions are
preserved; source exposure is DIRECTED_SHARED_CONTEXT_NONBLIND.

## 1. Exact input promise and relation to the present Task

The current coverage Task T:87 explicitly permits task-relative stochastic
kernels at a properly declared layer. NSA /strata/N1 and NSA-12 likewise
type them without granting every possible kernel. The frozen
G_effect-dist^eff contract requires a public effective exact sampler; it
does not itself supply one from a description by point probabilities.
This certificate treats a definite sufficient input interface:

* Public input N, a finite effective code z for the **complete state needed
  for the declared kernel and observations**, and public kernel code K.
* Outcomes k are natural numbers. For each promised-valid `(N,z)`,
  `p(N,z,k) ≥ 0` and `sum_(k≥0) p(N,z,k) = 1`.
* There is one public algorithm, uniform in `(N,z,k,n)`, returning a rational
  `q(N,z,k,n)` with `|q-p| ≤ 2^(-n)`. It terminates on every such promised
  input. Pointwise computability with no uniform algorithm is insufficient.

The positivity/normalization conditions are promises on the declared scope;
no algorithm deciding valid kernel descriptions is required. No secret
factor, factor-correlated advice, noncomputable/physical oracle or
asymmetric runtime access is introduced. This interface is conditional:
neither the word "kernel" nor general permission to declare one proves
that any particular Source primitive satisfies these promises.

P000/X6 remains the native spatial basis. The finite code z represents only
the declared operational/observer scope, with a required native-state bridge
where applicable; it is not presumed to encode all native state. Fair-bit
randomness is an N1 operational choice. The real U below is a proof device
for the probability law of an infinite bit tape, not an exact-real oracle
used by the algorithm, a continuum N0 primitive, or a new physical time law.

## 2. Explicit finite-stage algorithm

Fix a promised `(N,z)` and suppress it in the notation. Let

`S_(-1)=0`, and `S_j=sum_(i=0)^j p_i` for `j≥0`.

Read independent fair bits b_1,b_2,... . After s bits, let

`a_s = sum_(i=1)^s b_i 2^(s-i)`,
`I_s=[A_s,B_s]=[a_s/2^s,(a_s+1)/2^s]`.

All these are exact finite integers/rationals. A bit tape supplies fresh fair
bits for this call, independent conditionally on the retained input state.
At stage `s=1,2,...`:

1. Compute `n_s=s+ceil(log2(s+1))+3` using integer arithmetic and
   `epsilon_s=2^(-n_s)`.
2. For all `0≤i≤s`, compute `q_i=q(N,z,i,n_s)`.
3. For `0≤j≤s`, set `Q_j=sum_(i=0)^j q_i`, and form the certified CDF bounds
   `L_(j,s)=max(0,Q_j-(j+1)epsilon_s)` and
   `H_(j,s)=min(1,Q_j+(j+1)epsilon_s)`.
   Put `L_(-1,s)=H_(-1,s)=0`.
4. If there is a `k≤s` such that

   `H_(k-1,s) < A_s` and `B_s < L_(k,s)`,                            (K1)

   output k and halt. Otherwise proceed to the next stage and bit.

Every stage is finite and effective. A uniform bound on its time is not
assumed. Since `(j+1)epsilon_s ≤ 2^(-s-3)` for `j≤s`, these bounds enclose
S_j. More precisely, the center error is at most `(j+1)epsilon_s`,
whereas the one-sided distances `S_j-L_(j,s)` and `H_(j,s)-S_j`
are each at most **`2(j+1)epsilon_s`**. Clipping cannot increase these
distances. They tend to zero and remain valid even if individual rational
approximations q_i fall slightly outside `[0,1]`.

## 3. Exactness and almost-sure termination

**Theorem.** On every promised valid `(N,z)`, this public fair-bit algorithm
halts with probability one and outputs k with probability exactly p_k.

*Proof.* In the standard fair-tape probability space, let
`U=sum_(i≥1)b_i 2^(-i)`. It is uniform on `[0,1]`; binary endpoint
ambiguities have probability zero. The algorithm only uses the finite
intervals I_s, which contain U and have length `2^(-s)`.

If (K1) holds, then `S_(k-1)<U<S_k`. Consequently a certified output cannot
be wrong or belong to two distinct positive-probability CDF intervals.

Because `S_j ↑ 1`, every U in `(0,1)` except the countable set of CDF
boundaries belongs to an open interval `(S_(k-1),S_k)` for some finite k.
Fix such a U and k. Its distances from both endpoints are positive. For
all sufficiently large s≥k, the binary interval width plus the
CDF-bound error is smaller than both distances, since

`2^(-s)+2(s+1)epsilon_s ≤ (5/4)2^(-s) → 0`.

Thus `H_(k-1,s)<A_s` and `B_s<L_(k,s)`; (K1) holds. Thus the
algorithm eventually halts on every tape outside a null set. Zero-mass
intervals are never selected. Finally the probability of
`S_(k-1)<U<S_k` is `S_k-S_(k-1)=p_k`; the excluded endpoints have measure
zero. This proves the exact output law and almost-sure termination. ∎

The theorem does not claim termination for every bit tape. In particular
dyadic or CDF-boundary tapes need not terminate. It supplies the exact
almost-sure promise required by the frozen effective probabilistic class,
not an approximation in total variation and not a finite truncation of an
infinite distribution.

## 4. No pre-given tail rate or expected-time bound is required

The algorithm does not need a supplied rate for `S_j→1`: at stage s it
inspects only finitely many probabilities and can certify the particular
random interval when appropriate. Normalization guarantees the needed
interval exists almost surely.

Under these hypotheses an effective tail modulus can nevertheless be
*derived*, so it would be incorrect to claim that no computable modulus
exists. For a rational `eta>0`, search for s with

`L_(s,s) > 1-eta`.

Such a stage eventually occurs by normalization and vanishing error. Its
index m=s certifies `sum_(k>m)p_k < eta`. The search is uniform in the public
kernel code and `(N,z,eta)` on the promised domain. Known total mass 1 is
used here; this does not silently normalize computable weights whose
positive total mass is unknown or noncomputable. This is not a pre-given
complexity bound and gives no uniform finite expected number of fair bits
or arithmetic steps for the sampler. The coverage Task has no efficiency
hard target, and none is added here.

## 5. Full-state conditional law and the terminal pipeline

Suppose the declared update uses outcome k through a public effective map
`F(N,z,k)`, total on the reachable state/outcome pairs in scope, and p is
the conditional kernel given the **whole retained z**. Start with the same
state or the same publicly effectively generated initial joint state law.
Replace that kernel call with the sampler above. Its conditional outcome
law is exactly p at each reachable z, so the conditional law of the next
retained state is unchanged. Induction/iterated conditioning therefore
preserves the joint finite state/history law, not just isolated marginals.

This requires the promised p to be the correct full-state conditional law.
If aliases, shared latent randomness, past choices, ports, provenance or
future-relevant residuals are omitted from z, the premise has not been
proved. Fresh independent calls to a marginal sampler cannot substitute
for a correlated process by fiat. One may retain the needed finite history
or another certified sufficient representation; neither a universal finite
native state nor a blanket Markov assumption is inferred from P000.

Different calls use new bits; equivalently a public computable pairing of
bit positions supplies independent fair tapes from one fair tape. This is
not fresh resampling of persistent latent state already represented in z.
Each individual call fails to halt with conditional probability zero.
The countable union of such call-failure events has probability zero.
Accordingly, if the original kernel process terminates almost surely after
a finite number of calls and its remaining steps/readouts are effective,
the inlined process also terminates almost surely with the same declared
joint terminal behavior. There is no claim about an unselected infinite
limit observer.

If that terminal type is a finite explicit C with the required presentation
interpretation, the inlined process is now a concrete member of the old
G_effect-dist^eff class. If an effective terminal readout/compilation is
required, apply the already fixed typed bridge V2 and its exact observer
scope. For the finite-module interface, the actual C/annotations/divisor
pipeline from the separate application can be retained in the same Q.
The unchanged finite presentation C is the output required by the frozen
class. Any additionally retained labels or observations keep their
separately declared types; no arbitrary tuple is silently relabelled a
module presentation. Their joint-law preservation follows from the same
full-state coupling, rather than a claim that C alone determines them.
No new simulation of hidden CRT factors is needed. If the terminal object
is only a relational index lacking a justified effective readout, this
sampler certificate does not solve that separate representation problem.

## 6. Completed bounded deduplication and precise new obligation

This is a positive realization certificate for all kernels satisfying the
explicit uniform-computability/countable-normalization interface. It goes
beyond merely assuming that an exact effective sampler has been provided.
It does not show that every currently admitted stochastic resource has
this interface, that all semantic output probabilities must be supplied
this way, or that this sufficient condition is necessary for sampling.
No particular new kernel is admitted by this document.

The three complete saved inputs were compared without executing their
checkers: (i) the old machine-readable contract, 1,569 bytes, lines 6–8,
assumes a public effective sampler; (ii) the 20260904 return, 10,492 bytes,
lines 26–30 assumes an exact sampling algorithm and lines 49–59 inline it;
(iii) the current RRBF7 applicability return, 19,104 bytes, lines 56–65
and 69–81 uses the same assumption. Its line 97 explicitly avoids an
unjustified noncomputability claim about point probabilities. None of these
three texts constructs a sampler from the normalized uniformly computable
point-probability interface. The temporary collaborator independently read
these bytes as an **author-side** check, not a distinct final review.

The new completed obligation is therefore the implication

`uniformly computable normalized countable kernel interface`
`  -> public fair-bit exact a.s. sampler`
`  -> old effective transition contract at the declared complete state`.

The first arrow is proved above; the second instantiates the old contract
and its full-state observer bridge. This finite document comparison is not
an exhaustive literature search. No originality claim is made for the
classical CDF/finite-approximation method itself. No RRBF7 theorem/checker
or saved finite experiment has been rerun.

## 7. Actual Source application and the remaining universal obligation

The following are the actual admitted-language and theorem interfaces,
not newly invented grants. Full byte pins and saved connector envelopes
are linked by the accompanying manifest.

| Source / precise locator | What it supplies | What this unit establishes or still requires |
| --- | --- | --- |
| `research_tasks/RR133_COVERAGE_PROSPECTIVE_GEN2.md` at Source `a2b4f908009eda28ccfef8638dda7ab28f856ecd`, lines 87–89 | Task-relative stochastic kernels may be declared; the same public resource must be available to runtime and interpreter. | A concrete representation interface for such kernels and an exact effective implementation when its promises hold; permission to declare a kernel is not proof that every kernel has computable probabilities. |
| Same Task, lines 99–103 | Coverage requires all licensed mechanisms and preservation of support-bearing terminal presentation/readout. | This unit proves coverage of the specified kernel subclass plus effective complete-state updates and the already justified terminal interface. It does not quantify over an unstated stronger external observer. |
| `native_semantics_admissibility.json`, `/strata/N1_DERIVED_OPERATIONAL_SEMANTICS` and `NSA-12-TASK-RELATIVE-BASE-PRECEDENCE` | Proper derived typing, and task-relative base declarations. | N1 fair-bit implementation here; no new base stochastic or continuum primitive, no blanket prohibition of kernels. |
| `effect_dist_public_emulator_contract.json` at Source `91165f4ca76d211bbdac98bed4073d89c4259a5e`, `/probabilistic_semantics` | Public effective sampler, a.s. termination, finite explicit presentation output. | The sampler promise is now derived for this explicit input interface. Required terminal type and scope remain unchanged. |
| Bridge V2 and finite-presentation application, actual checkpoint Source `88fe829fd2f3a67164ee96a26adec0ab8156d239` | Typed support relation, effective readouts, complete joint data and finite-presentation scope. | The kernel code can be composed with these verified public maps in one Q; inherited determinant/gcd readout is not a new mechanism or new mathematical experiment. |
| P000/X6 and joint/residual contracts, frozen in the preceding evidence manifest | Native basis and preservation of declared joint relations/residuals. | z must encode the whole declared effective state/observer scope, with its native bridge if needed. This is not a universal finite encoding of X6. |

More formally, define `G_K` to consist of the public finite-code state
programs satisfying Sections 1 and 5, whose kernel calls have the stated
uniform approximation algorithm, whose control/update rules are public
effective maps, whose whole computation terminates a.s., and whose final
C and selected observations satisfy the typed terminal interface above.
The single constructive transformation replacing each call proves

`G_K -> G_effect-dist^eff`

with preservation of the declared full joint terminal behavior. This is
an upper-class implementation theorem and needs no enumeration of the
programs in `G_K` or decision procedure for their promises. If a Source
interpretation proves `A ⊆ G_K`, composition immediately covers that A.
Alternatively, already supplied effective samplers can be included through
the old class directly; uniform point-probability descriptions are not
asserted to be a necessary admission test.

**Exactly what remains:** Source justification that every actually
licensed mechanism has either this effective implementation/terminal
interface or another already covered one, with all required observations.
The conditional theorem does not prove that universal inclusion. Nor does
failure to have proved it certify specification ambiguity. A single absent
Phi locator, unenumerated admission inventory or unproved kernel premise
is neither an admitted escape nor a proof that the objective is impossible.
The c.e. quotient-index stress test remains a distinct, not-shown-admitted
representation separation, and the sampler does not grant its completed
support readout. All three Task terminal outcomes remain unclaimed.

The inherited oracle/secrecy/asymmetric-privilege and mechanism firewalls,
the full Task target and the OPEN parent remain unchanged. This is paper
reasoning only: no probability sample, simulation, scientific checker,
Native/Source publication of this kernel unit or new research ownership
occurred in preparing this fixed paper unit. The earlier six-file progress
checkpoint is a separate, successful preservation step; it is not Native
acceptance of this new unit.

Researcher-ID: EM-N-DEA587 / RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION
