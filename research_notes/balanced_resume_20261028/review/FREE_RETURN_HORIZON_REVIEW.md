# Nondecisive mathematical review: finite-horizon X6 return memory

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Candidate: AC-FREE-20261028-4B72C1-RETURN-HORIZON.
Finding: the exact time-layer equivalence classes, peak state count,
asymptotic and uniform finite-memory impossibility are valid in the stated
clocked deterministic return-observer model. One explicit fixed-alphabet
attainment clarification was requested and supplied separately after the
raw freeze. No unresolved mathematical defect remains in that scope.

Frozen raw candidate: `free/phase_a_candidate.md`, SHA256
`ca2dd60ed65ea3fe6222dafadd4cc2cb5d09a769e2771ced294f4894b39df03a`.
Post-freeze clarification: `free/post_freeze_clock_alphabet_clarification.md`,
SHA256 `6ad6a465fc2e98ea3ceeb38c9f98b4b98bf172683c6873b14bc1cad4f210a2ea`.
The raw candidate was rehashed after the clarification and remained unchanged.
This report is mathematical review only. It does not certify the claimed
Phase-A source firewall beyond the supplied disclosure, complete Phase-B
deduplication, or grant Driver acceptance/novelty.

## Exact mathematical checks

After exactly t signed coordinate steps, the reachable positions are
precisely norm_1(x)<=t with norm_1(x)=t modulo two. The necessity follows
from step length and parity; the converse pads a shortest coordinate word
with immediate inverse pairs. This accounts for all words, including
cancellation and repeated paths. The norm is the graph word length of
the declared native steps, not an imported Euclidean distance assumption.

At fixed t, every reachable x with norm_1(x)<=H-t is distinguished from
every different y by the same suffix taking x to zero. The suffix may
have any length up to the remaining horizon, because all prefixes are
observed; the empty suffix correctly distinguishes x=0. This is a lower
bound for arbitrary history-dependent compression: identical internal
states at the same external clock cannot answer that same suffix in two
different ways.

Every position outside the remaining radius is unobservable as a return
under all permitted suffixes. Its distance can shrink by at most one
per next letter while the budget also shrinks by one, so the single dead
class descends safely. It exists exactly when t>H-t. This gives the exact
classes claimed, with no erased distinction relevant to the stated future
return language.

The generating function for exact signed six-coordinate distance is
((1+z)/(1-z))^6. Summing distances of the same parity divides by 1-z^2,
yielding (1+z)^5/(1-z)^7. The binomial coefficient formula follows. The
parity-adjusted radius can be -1 only in the stated final odd-time case,
correctly covered by C_6(-1)=0.

For H=2a, later layers have C_6(H-t)+1 states; for H=2a+1 they have
C_6(H-t-1)+1. Their largest possible count is C_6(a-1)+1. Since the
coefficients of (1+z)^5/(1-z)^6 give
C_6(r)-C_6(r-1)>1 for every r>=1, the peak is C_6(a). The degenerate
H=0 and H=1 cases both have one internal state, using the known external
clock to distinguish their different time-indexed outputs.

The leading coefficient of C_6(r) is 32/6!=2/45. Substitution of
r=floor(H/2) gives H^6/1440. The fixed-time distinguishability bound
therefore defeats any fixed internal alphabet for sufficiently large H,
even if the clock and H are externally supplied. They are identical
across the compared histories and cannot carry their difference.

## Fixed runtime alphabet clarification

The raw proof constructs a time-indexed quotient whose coordinate symbols
across different layers have a larger union than the maximal layer size.
To justify the exact fixed-alphabet and bit-cost wording, I requested the
standard explicit clock-dependent recoding bridge. The separate addendum
now maps each Q_t bijectively into an initial segment of one alphabet of
size M=max_t|Q_t|, and uses i_(t+1) composed with the quotient transition
and i_t inverse. The current external clock supplies the layer. Unreachable
alphabet symbols can be totalized arbitrarily, so this attains a fixed
M-symbol storage space and ceil(log2 M) bits.

This is a proof elaboration supplied in response to reviewer feedback,
and is not represented as part of the original blind raw construction.
The reviewer independently checked the original equivalence/counting
claim but also contributed this explicit clarification; a later decisive
review must preserve that contribution disclosure rather than describe
the combined package as untouched clean-independent review.

The cost counts runtime internal state only. The clock, horizon parameter,
transition description/tables and implementation cost are outside that
count, as the addendum now explicitly states. A different cost convention
would require a different result.

## Scope and verification grade

I read the full frozen candidate and its checker, but did not rerun its
author discovery enumeration. Validation here is a paper proof check,
not a Lean/kernel certificate or an independent empirical replication.
No current-project source or unrelated research was sent into the frozen
Phase-A record during review. Mathematical methods such as future-word
distinguishability and generating functions are standard; tool coverage,
repository deduplication and prior-art classification remain Phase B
obligations, so no novelty or new tool family is endorsed.

The six-axis torsor, signed steps, separate clock and observer-only
compression remain exactly typed. The safe dead class does not compress
full native Cell identity, an enlarged horizon, other target hits or
weighted joint-path observations. This does not prove an axiom or a
physical erasure/propagation law.

Reviewer has shared portfolio/control context and is not a clean-blind
agent. The candidate was received only after its original freeze. This
is nondecisive research evidence, with the specific clarification
contribution disclosed, not formal Driver admission, Working Truth,
Foundation or Task/parent closure.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
