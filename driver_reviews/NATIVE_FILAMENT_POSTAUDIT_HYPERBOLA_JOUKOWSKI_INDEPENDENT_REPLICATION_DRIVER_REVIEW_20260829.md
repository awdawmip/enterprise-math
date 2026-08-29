# Native Filament Post-audit Hyperbola/Joukowski Independent Replication — Driver Review

Status: `ACCEPTED / PASS_WITH_NARROWING / RESULT_ONLY`

Driver-ID: `EM-DVR-P8H4Q2`
Driver authority: `DA-FADB5B44A384B8C3F3F5`
Source authority comment: `5458931979`

Task: `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`
Publication: `TP2-7022EC048DC373BFA4CB`
Result: `RR-680C6257EEF10F6F1C16`
Researcher: `EM-NFHJREP-5C72A1`
PR: `#819`

## Driver verdict

`ACCEPTED_WITH_EXACT_NARROWING`.

The independent replication reaches the registered hard target. The accepted payload is:

- `J1 = VERIFIED_EXACT`;
- `J2 = VERIFIED_EXACT`;
- `C1 = VERIFIED_EXACT`;
- `H1 = VERIFIED_WITH_NARROWING`;
- `H2 = VERIFIED_WITH_NARROWING`;
- `C2 = VERIFIED_WITH_NARROWING`.

No stronger statement is accepted.

## Decisive mathematical audit

### H1

H1a, H1b and H1c are algebraically exact in characteristic different from 2 with `B != 0` and `d_0 != d_1`.

For the tangent-concurrence quotient, however, the distinct-tangent hypothesis `u != v` becomes `a != b` under

`a=w-u`, `b=w-v`.

Therefore the quotient of distinct-tangent concurrence triples by simultaneous translation is

`H_(B,C_i) \ Delta_(B,C_i)`

rather than the whole split hyperbola whenever the diagonal locus

`Delta_(B,C_i)={(a,a): B a^2=C_i}`

is nonempty. The `F_5`, `B=C=1` witness with diagonal points `(1,1)` and `(4,4)` is a valid minimal counterexample to the unconditional final torsor sentence. The narrowed H1 wording is accepted.

### H2

The map to `Bab=C` gives `|R|=q-1`. The common-value fibers are exactly the independent-sign orbits, and Burnside gives

`|R/G| = [q+1+eta(BC)+eta(-BC)]/4`

for the quadratic character `eta` of an odd finite field. The packet's Legendre-symbol notation is literally correct for odd prime fields; for general odd prime powers it must be read as the finite-field quadratic character. The orbit-capacity implication `|R/G|=1 => q<=5` is exact and does not depend on the character formula. The narrowed H2 wording is accepted.

### J1

For `Lambda_s(a)=-sa-1/(2a)` and `q` odd with `q ∤ 2s`,

`Lambda_s(a)=Lambda_s(b)`

holds exactly when `a=b` or `ab=(2s)^(-1)`. Hence the fibers are the orbits of `a -> c/a`, `c=(2s)^(-1)`, and the image size is

`[q+eta(c)]/2`.

The central-packet saturation criterion is exactly `Im Lambda_s subseteq J_s`; the return also correctly keeps the `q|s` boundary outside the formula. J1 is accepted exactly.

### J2

The independent second-moment reconstruction is valid.

At `q=2s-1`, saturation plus the two fixed points of `a -> a^(-1)` gives the congruence forcing `q|25`, hence the prime case is `q=5`, `s=3`.

At `q=2s+1`, the fixed-point-free involution `a -> -a^(-1)` gives the congruence forcing `q|7`, hence the prime case is `q=7`, `s=3`.

Thus `s=3` is the unique nontrivial odd-sector parameter saturating both extremal boundaries under the packet hypotheses. J2 is accepted exactly.

### C1

The two boundary equations are both equivalent to `q_b=s+2`. Using only the packet-authorized premise that an odd universal breaker satisfies `q_b<=5`, with odd `s>=3`, the unique nontrivial solution is

`(s,q_b,k_*)=(3,5,9)`.

Then `M_9=35`, `3M_9=105`, and `3M_9+1=106=2*53`. The accepted result correctly keeps breaker-coprime capacity `9` typed separately from the unrelated native typed-Cell incidence cap `9`. C1 is accepted exactly.

### C2

The three `s=3` lane polynomials are exactly

`6m^2-2m+1`, `6m^2+1`, `6m^2+2m+1`,

and the two named quantities both evaluate to the integer `105`. The statement-only packet is sufficient for exact numerical coherence, but not for the stronger claim that the two occurrences have a proved common causal/provenance mechanism or are known not to be independently fitted constants. The narrowed C2 wording is accepted.

## Independence and evidence envelope

The execution used the frozen statement-only packet and produced a fresh checker importing only the Python standard library. The PR changes contain only the independent checker, execution record, immutable Result record and frozen return. No source proof/checker comparison is needed to accept this artifact as independent evidence, and this Driver review deliberately does not convert the blind replication into a source-consistency review.

The Result envelope is structurally coherent: the task/publication/claim/execution bindings match the server-authenticated Issue #240 CLAIM, and the return/checker Git blob pins match the Result manifest at the frozen owner frontier.

## Scope and routing consequence

The replication task is terminal at its classification scope. There is no mathematical-continuation residue created merely by PASS.

Accepted theorem consumption is restricted to the exact row statuses above. In particular:

- do not restore the unconditional H1 full-torsor sentence;
- do not use Legendre notation for general nonprime `F_q` without replacing it by the quadratic character;
- do not turn C2 numerical coherence into a common-provenance theorem;
- do not infer Working Truth, Foundation status, physical semantics, or novelty.

Because this is an `ACCEPTED` post-cutover review, the external-prior-art/duplication gate remains required. A separate follow-up audit should classify classical antecedents and exact duplication boundaries for the accepted H/J/C statements without rewriting this independent result.

`DISPOSITION = ACCEPTED`
`DESTINATION_CLASS = FOLLOWUP_TASK`
`TERMINAL_AT_TASK_SCOPE = true`
`WORKING_TRUTH_GRANTED = false`
`FOUNDATION_AUTHORITY_GRANTED = false`
`CANONICAL_PROMOTION_GRANTED = false`
