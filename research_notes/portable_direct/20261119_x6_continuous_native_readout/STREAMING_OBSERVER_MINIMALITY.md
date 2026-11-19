# X6 ingress feedback: minimal continuing observers and exact sampling condition

Date: 2026-11-19. Status: `AUTHOR_PROVED / EXACT_FINITE_BRC_CHECK / NOT_INDEPENDENTLY_REVIEWED`.

This is a scientific continuation of the entrance-feedback construction in
`research_notes/portable_direct/20261119_x6_native_relational_feedback/`.
That baseline package is preserved at
`awdawmip/enterprise-math@5806c80973d881009a755e8b5c922dab758a1032`.
It does not grant native event permission, mathematical admission, a formal
Review, a Task claim, or control-plane execution authority.

## 1. Carrier, sources, and future language

The fixed scientific source is `awdawmip/enterprise-math@ef720decf4a35a276e509964250571a55421b9f8`.
The native background is Heartbeat X6, one selected Cell anchor, and an ordered
cyclic triple of distinct native axes. These are a restricted state/observer in
the six-axis world. Event indices count declared atomic scatterings, not
calibrated physical heartbeats.

The source-preserving carrier is the existing `NamedTriadBRC` of
`check_relation_updates.py`: three named unit tokens, original signed ports,
current signed ports, joint III branch words, and ordered event history. Its
source SHA-256 is
`83175b298bb8d18b43e2936043cf42f73efb476fa8b6581d4c9cdcd147af2ee0`.
Each scientific transition in the new checker calls its actual `apply` method.
The previously proved tokenwise correspondence is

    s'_i = a_(i-1) s_(i-1).

We inspect the finite *current internal skeleton* `(s,a,p)`, where `p_i` is the
source name presently at selected axis i, `s_i` its radial sign, and `a` the
active twist with product -1. It has 8 x 4 x 6 = 192 states for the fixed
support and cyclic orientation. The original Cell, initial-source records and
unbounded appended BRC history remain in the carrier. The number 192 is not a
cardinality claim about unrestricted native states or full recorded history.

The initial future language is arbitrary repetitions of ingress feedback

    T: (s,a,p) -> (Q_a s, b, p'),
    b_i = -s_i s_(i+1),       p'_i = p_(i-1).

The stronger composition certificate in section 3 permits any declared sequence
of the four already classified local update laws. The action chosen at a step
is a common known input to compared states. It is not selected by an omitted
hidden variable. Observations occur at shell boundaries at one fixed axis j.

Applicable source constraints were read before this projection:
`p000_reality_foundation.json`, `HEARTBEAT_WORLD_NATIVE_X6_TIME.json`,
`RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json`,
`ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`,
`docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`, and its machine companion.

## 2. An exact three-bit continuing reader

Write `r_i=s_i a_i s_(i+1)`, so product r=-1. Ingress feedback obeys

    r'_i = r_(i+1),       y' = y r_(j-1),       y=s_j.       (1)

Consequently

    y_(t+3) = -y_t.                                           (2)

This follows either from three applications of (1), whose three ratio factors
multiply to -1, or from the established identity `T^3(s,a)=(-s,a)`.

**Theorem 1 (minimal continuous sign observer).** For all future repetitions of
T, the exact smallest deterministic state of the fixed-axis raw-sign observer is

    U_j = (y,r),

with 2 x 4 = 8 states. It needs three binary storage bits. No separate active
twist, event-count phase or source permutation is required by this particular
observer. This is an observer machine; those fields remain in the underlying
carrier when their stronger observations are in scope.

**Sufficiency.** Equation (1) gives a closed successor on `(y,r)` and output y.
Induction proves equality of all future fixed-axis sign observations for equal
observer states, at arbitrary finite horizons.

**Minimality.** Every combination `(y,r)` occurs. Under two future T steps its
three-read word determines it exactly:

    r_(j-1)=y0 y1,   r_(j-2)=-y0 y2,   r_j=y1 y2.

Therefore two distinct `(y,r)` states have a distinguishing sign word of length
at most three. Any sufficient deterministic summary needs at least eight values.
One or two consecutive raw reads give only two or four distinguishable states;
three give eight. These are sharp read-count bounds for this observer.

Equivalently, the three-read register `w=(y_t,y_(t+1),y_(t+2))` has successor

    w -> (w1,w2,-w0).

After receiving an actual three-read window, it predicts the next symbol as
`-w0`; the operational register then shifts. Its eight states consist of one
two-cycle and one six-cycle. The shorter observer cycle does not shorten the
six-event period of a complete named FRAME.

**Corollary (minimal relational reader).** If only the adjacent products
`z_t=y_t y_(t+1)` are observed, the exact minimum is four states, represented by
r or by `(q1,q2)=(z_t,z_(t+1))`. Under T,

    (q1,q2) -> (q2,-q1 q2).

Two adjacent products, equivalently three raw signs, identify all four states.
The additional one bit of y is necessary precisely when future *raw signs* are
also required: the two states `(y,r)` and `(-y,r)` have opposite raw-sign words
for all time. The relation alone cannot choose between them.

The phase claim is about a *current*, axis-labelled r, updated after every
declared event. Keeping a historical r unchanged while discarding how many
events occurred is a different encoding and does lose phase information. The
known shell/window completion schedule is not absorbed into these data-bit counts.

## 3. The same minimal states are safe under all four known update laws

For each of the previously classified rules write

    b_i = a_i D_i(r),

where D is respectively `1`, `-r_i`, `-r_(i-1)`, or `-r_(i+1)`.
All four share the exact induced transition

    y' = y r_(j-1),
    r'_i = D_i(r) r_(i-1),
    p'_i = p_(i-1).                                           (3)

Thus r and `(y,r)` are closed under every chosen action separately. They are
therefore safe under every finite composition in this four-action language,
not just under a fixed action repeated forever. The same argument covers any
explicitly specified gauge-invariant D(r) with product +1 on this carrier;
the four-law restriction is the source's cyclically covariant classification.

The eight- and four-state lower bounds still hold, because the language contains
the ingress-feedback continuation used to distinguish all such states. This
is an exact action-and-observer descent certificate, rather than an inference
from a finite fitted trajectory.

## 4. What changes when the observer reads source names?

Let the fixed-port observation be `(p_j,s_j)`: the name of the token at the port
and its sign. It does not read all three names at once. Since every scattering
advances every token by one selected axis, three consecutive observations read

    p_j, p_(j-1), p_(j-2).

These distinguish all six assignments of the three distinct source names.

**Theorem 2.** The exact minimal state for the named fixed-port sign observer is

    V_j = (p,y,r),

with 6 x 2 x 4 = 48 states. The lower bound is attained under arbitrary known
sequences of the four update laws. In a fixed-width binary encoding it needs six
bits, whereas the unnamed raw-sign observer needs three.

**Proof.** Equation (3) is a closed successor. For minimality use three ingress
observations: their names recover p and their signs recover `(y,r)`. All 48
combinations occur. One, two, and three such observations distinguish respectively
6, 24, and 48 states. QED.

The exact four-state fiber of the 192 -> 48 map is the residual static
sign-reference group

    K_j = {epsilon in {+1,-1}^3 : epsilon_j=+1}.

It acts by `s_i -> epsilon_i s_i`,
`a_i -> epsilon_i a_i epsilon_(i+1)` and leaves p unchanged. It fixes y and r.
Conversely, if two skeletons have the same p,y,r, the unique
`epsilon_i=s'_i s_i` lies in K_j and carries one skeleton to the other.
This proves exact fibers of size four. The unnamed 192 -> 8 fibers additionally
contain the six source assignments, hence have size 24.

In particular, continuous fixed-port observations cannot recover the signs on
the other two axes or choose a unique active twist. Each `(y,r)` sign/twist
fiber contains all four admissible twists. Two off-axis sign bits recover the
entire sign/twist skeleton, since

    a_i = r_i s_i s_(i+1).

Two bits are necessary because the hidden fiber has four elements. If names are
also part of the required state, their assignment must additionally be retained
or observed; the named observer already retains it.

## 5. Sharp sampling theorem: event residues matter

Consecutive reads are sufficient, but are not required. Assume T is repeated,
the first event is known, and raw readings are taken at a specified set of
nonnegative integer event offsets N. By (2),

    y_n = (-1)^floor(n/3) w_(n mod 3),
    w=(y0,y1,y2).                                              (4)

The offsets in this formula count the source's declared atomic scatterings.
They are not raw V39 loop counts or elapsed calibrated physical time.

**Theorem 3 (exact sampling criterion).** The sampled raw signs recover the
initial four-state relation if and only if N meets all three residue classes
modulo three.

**Proof.** When all classes occur, correct the known signs in (4) and recover
w, hence r. If a residue class is missing, flip that unobserved component of w.
Every w in `{+1,-1}^3` is realizable by the underlying BRC population. All sampled
signs remain the same, but one or two of the initial pair products change, so
the initial relation changes. This works for finite and infinite sampling sets.
QED.

If N meets m=1,2,3 residue classes, every nonempty observation fiber contains
exactly `2^(3-m)` initial relation states. With no reads it contains all four.

For equally spaced samples `0,d,2d,...`:

| Known stride d | Fixed-port information |
|---|---|
| 3 does not divide d | Three samples recover the full relation and raw observer state |
| 3 divides d | Every sample is determined by y0 and d; no relation state is distinguished, even at infinite horizon |

For instance, sampling every third event yields only `y0,-y0,y0,-y0,...`,
independent of all four r values. More samples of that schedule cannot replace
a missing event-residue observation. An arbitrary known initial offset gives
the corresponding relation at that offset; recovering a historically labelled
initial relation additionally requires the known offset modulo three.

For nonoverlapping windows beginning at events 0,3,6,..., each three-read word
is the previous word's overall negative. The adjacent-product pair q is the
same in all these windows. Sliding the window forward by one event instead
updates q by `(q2,-q1q2)`.

## 6. Concrete boundary of the compression certificate

The fixed-port quotient does not authorize arbitrary future observations.
Take j=0 and the two sign/twist states

    s=(+,+,+), a=(-,+,+),
    s'=(+,-,+), a'=(+,-,+).

They have the same y0=+ and the same r=(-,+,+). Every permitted fixed-port sign
continuation in section 3 agrees. A single read at axis 1 distinguishes them.
The second state is exactly the first reframed by epsilon=(+,-,+).

Thus allowing a detector-axis change requires repair coordinates; the two
off-axis sign bits provide them. Queries of the active twist, original source
ports or full event path likewise require their declared carrier data. No
statement above deletes these data from the BRC carrier or gives 8/48 states
the status of a complete native world state.

## 7. Reproduction and evidence

Run `python check_streaming_state.py` after placing this package beside
`../20261119_x6_native_relational_feedback/`, or supply the baseline package,
repository root, or exact kernel path as its single optional argument.
The checker validates the imported BRC source bytes and uses its actual named
III transitions. It checks all 192 internal skeletons, all three fixed axes,
all four update actions, exact stable observation partitions, the gauge-fiber
certificate, every sampling subset of six consecutive event offsets, strides
1 through 12, and the explicit change-of-observer witness.

The arbitrary-horizon and arbitrary-composition claims are proved by (3) and
(4). Finite checks verify their complete finite input carrier; they are not
used to infer an unproved limit. The result is an exact observer-relative
compression certificate with zero ambiguity at its stated sufficient states,
and explicit structural ambiguity when a necessary coordinate is omitted.
