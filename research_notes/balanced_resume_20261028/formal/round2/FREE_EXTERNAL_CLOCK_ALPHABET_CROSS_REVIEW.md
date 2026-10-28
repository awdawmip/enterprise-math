# Independent check of the external-clock fixed-alphabet clarification

Reviewer: EM-DIRECT-099801.
Activity: RA-BALANCE-FORMAL-20261028-099801.
Date: 2026-10-28 (Asia/Shanghai).
Finding: LOCAL_NONAUTHOR_BRIDGE_CHECK_NO_MUSTFIX_FOUND.

The exact clarification read is
`free/post_freeze_clock_alphabet_clarification.md`, SHA256
6ad6a465fc2e98ea3ceeb38c9f98b4b98bf172683c6873b14bc1cad4f210a2ea.
I also read the frozen original contract in `free/phase_a_candidate.md`,
SHA256 ca2dd60ed65ea3fe6222dafadd4cc2cb5d09a769e2771ced294f4894b39df03a.
This review checks only the fixed-alphabet implementation bridge against that
contract. It does not reprove the whole counting theorem, adjudicate novelty,
or supply formal Driver acceptance.

The original contract explicitly fixes H in advance and supplies the external
step clock t to both update and readout, without allowing it to retain input
history. It charges only the runtime internal memory. Thus the clarification
does not add a previously forbidden time-dependent update or readout.

For each reachable time t, the established quotient Q_t is finite with size
N(H,t)<=M. An injection i_t into the same fixed alphabet {1,...,M} is enough.
The clarification chooses a bijection onto the first N(H,t) symbols, so its
inverse is well-defined on exactly the valid symbols for that time. These
finite maps may be precompiled for the fixed H; the quotient sets are given
explicitly by bounded integer displacements and the optional bottom class,
so there is no hidden undecidable codebook or enumeration-completion problem.

For every legal update time 0<=t<H, the encoded transition

    i_(t+1) o delta_t o (i_t^(-1), identity_input)

maps a valid current symbol to a valid next symbol. Starting from the encoded
initial class, induction keeps every actually reached internal symbol inside
the corresponding valid image. The readout composed with i_t^(-1) therefore
equals the established quotient readout at every prefix time. How a total
transition table treats symbols unreachable at that time has no effect on any
legal run. No transition beyond the declared horizon is needed.

The same physical internal symbol may name different quotient classes at
different times because both interpretation and transition access the clock.
This is exactly why a union of all displacement labels across times is not
the memory lower bound in this model. For example, at H=1 the single symbol
can represent the initial return class at time zero and the unreachable-return
class at time one; the clock-dependent readout distinguishes them without
storing the input history. This is compatible with zero runtime internal bits
and would not be a valid argument for an unclocked stationary-readout model.

Conversely, at a time where N(H,t)=M, the already established pairwise
distinguishable histories share the same t and H. If a fixed alphabet had
fewer than M symbols, two such histories would collide. Their common clock
cannot distinguish them, and the distinguishing common suffix contradicts
exact output. Therefore the fixed alphabet needs at least M symbols, matching
the construction. Encoding that alphabet takes ceil(log2 M) fixed-length
bits, with unused binary strings treated as unreachable codes.

The accounting limits are essential and stated correctly: precompiled code
tables/update rules and the supplied external clock are outside the charged
runtime state. The bridge is not a time/space implementation bound including
table storage, computational workspace, or the clock. Charging any of those
requires a separate model. No physical erasure of the underlying full X6
walker state is asserted.

I did not request or construct this clarification and did not participate in
the author's proof before the quoted freeze. Reviewer EM-REVIEW-58D6A2's
earlier request for a bridge is disclosed; this check is a different reader's
assessment of the resulting frozen text. Shared owner/source context is
disclosed, and I do not claim clean-blind status. No computation, enumeration,
proof kernel, novelty search, new tool family or formal state change occurred.

Researcher-ID: EM-DIRECT-099801 / TASK_RESEARCH
