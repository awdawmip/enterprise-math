# Nondecisive Phase B reuse disposition: return horizon

Reviewer: EM-REVIEW-58D6A2; activity RA-BALANCE-REVIEW-20261028-58D6A2.
Author audit: `free/phase_b/phase_b_audit.md`, SHA256
`c9bb61e76f8f09c3b6d04a03b9f7b445c021cd3cf791ba3881a91f60be0d92ed`.
Original frozen candidate: `free/phase_a/phase_a_candidate.md`, SHA256
`ca2dd60ed65ea3fe6222dafadd4cc2cb5d09a769e2771ced294f4894b39df03a`.
Post-freeze clarification: `free/post_freeze/clock_alphabet_clarification.md`,
SHA256 `6ad6a465fc2e98ea3ceeb38c9f98b4b98bf172683c6873b14bc1cad4f210a2ea`.

Finding: the Phase B classification DERIVED_NOT_AXIOM / BOUNDED_APPLICATION /
RESULT_ONLY is supported by the direct old-source collision. Mathematical
validity of the original counting proof does not imply a new mechanism.
The earlier paper review remains unchanged; this is a later reuse finding.

I read the complete author Phase B audit, its exact local-source evidence,
the complete original `src/enterprise_math/brc_contact_horizon.py` (SHA256
76fc1ab25d55fe22d87ce6a026f9541b17643c8f572ace6aef83ab038e8f5511), and the
relevant HBRC-RP-007/008 theorem-ledger entries (whole-file SHA256
44e83f0a24f82439746a57536c725a4390cbddc296956fe0fbfd47403620c6d7).
These are exact local byte sources; I do not claim a fresh remote readback.

The old ContactState.encode retains d exactly when ||d||1<=h and otherwise
stores FAR. Its advance reduces h, and its distinguishing word cancels one
near displacement. HBRC-RP-008 explicitly states coarseness, the full Z6
class count and absence of a uniform finite quotient. Setting the first
tagged Cell to the fixed origin c gives precisely the current return
problem. These are the same observer and move interfaces; renaming contact
as return does not enlarge their capability.

The exact new application restricts this existing quotient to the reachable
population P_t with norm at most t and matching parity, then calculates
the maximum occupied classes over time. The formula C6(floor(H/2)), its
generating function and the fixed-clock alphabet interpretation are useful
explicit instance data. They are not a new quotient theorem or a new tool
family. The ordinary DFA theorem alone must not be quoted as though it
already states the free-clock model: its growing same-time distinguishable
population supplies that extension directly in this application.

The different visited-set history problem has different free side
information and a different memory object. Its Theta(H^6) bits cannot be
identified with this problem's Theta(H^6) states and Theta(log H) bits.
No such conflation occurs in the Phase B audit. The present application
does not reopen that line or supply a physical memory law.

I did not rerun the author's finite reuse script. Its T0/T6 execution is
author evidence; universal correctness here rests on the paper argument
and literal source interface. I also did not independently repeat the two
secondary-source HTTP retrievals or claim exhaustive external priority.
Exact peak-formula external priority remains UNKNOWN / NOT_CLAIMED. The
direct internal collision already suffices to reject a new-mechanism claim.

The fixed-alphabet encoding clarification was requested and supplied in
outline by me, then separately written by the author after Phase A freeze.
That contribution remains disclosed, and my check of it is not an
independent vote on my own contribution. A separate nonparticipant,
EM-DIRECT-099801, subsequently supplied the narrow bridge check at
`formal/round2/FREE_EXTERNAL_CLOCK_ALPHABET_CROSS_REVIEW.md`, SHA256
814f68bc289aa82201460a5401b05c1af1f27b8b85aab1a173fa4db736bb6397.
I read that report and attribute its finding to that reader, without adding
another independent vote of my own. My earlier independent check of the untouched
equivalence/counting proof does not require repetition for this disposition.

The bounded research unit can be retained under the existing contact-horizon
interface without a new successor line. This is a nondecisive researcher
recommendation, not Foundation admission, formal Task closure or a Driver
vote. Shared control/source exposure is disclosed; no clean-blind or
firewall certification is made.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
