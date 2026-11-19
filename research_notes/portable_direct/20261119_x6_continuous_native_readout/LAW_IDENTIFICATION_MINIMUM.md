# X6: identifying the event law requires two ports, with sharp five/six-read costs

Date: 2026-11-19. Status: `AUTHOR_PROVED / EXACT_FINITE_BRC_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED`.

Native source snapshot:
`awdawmip/enterprise-math@ef720decf4a35a276e509964250571a55421b9f8`.
The four-law classification and ingress-feedback BRC kernel are preserved in
`research_notes/portable_direct/20261119_x6_native_relational_feedback/` at
`5806c80973d881009a755e8b5c922dab758a1032`.

This note concerns a known family of candidate native local laws, not a finding
that the actual TRIADIC_CLOSURE_E permission predicate selects one of them.
It supplies a minimal distinguishing experiment for that family.

## 1. The experiment and its target

Work at a fixed native X6 Cell and a chosen positively oriented cyclic triple
of distinct native axes. Source names and joint III paths remain in the BRC
carrier. There is one token at each selected signed port. Define

    r_i = s_i a_i s_(i+1),       product(a)=product(r)=-1.

The law L is unknown but is fixed over the experiment. The initial signs s and
twist a are also unknown. The first scattering is Q_a; the law sets the next
active twist. Shell observations at times t=0,1,2 give nine possible scalar
queries `(t,j)`, with j in {0,1,2}. A query returns only the radial sign at that
port and shell, not the twist, law label, or a separate calibration bit.

The declared query model permits adaptive choices of these nine coordinates.
For the lower bound it even permits noncausal/offline query order. The achieving
protocols use causal order, so their physical observation order is stricter than
the model used to prove optimality. Repeated queries add no information.

The target is the pair `(initial r, L)`. The main domain excludes r=(---),
leaving three relation states. It contains 24 sign/twist inputs for each law:
each relation state has eight static gauge representatives. We hold the source
assignment fixed when checking these hypotheses; each actual BRC history still
retains the three source names and its two joint III branch operations.

The four candidate laws have the following relation updates:

| Law L | Next relation r'_i |
|---|---|
| Persistent generator P | r_(i-1) |
| Ingress feedback I | r_(i+1) |
| Egress feedback E | -1 |
| Stationary relation S | r_i |

Every one of them satisfies, at each port j,

    y_(0,j)y_(1,j) = r_(j-1),
    y_(1,j)y_(2,j) = r'_(j-1).                         (1)

All observations and constructions are invariant under a static independent
sign-reference change at each axis; no external symbol convention is calibrated.

## 2. Why one port cannot identify the two reversible laws

For either P or I, all fixed-port raw-sign sequences satisfy

    y_(t+3) = -y_t.

With all four initial relation states allowed, every initial triple
`(y0,y1,y2)` occurs under each law. Thus the complete infinite raw-sign languages
of P and I at a fixed port are identical. In the domain r != (---), both laws
give the same six streams, obtained by removing the two strictly alternating
streams. This is an all-horizon obstruction, not a failure of a short test.

The reconstructed relation from the same word depends on the law:

| Known law | r_(j-1) | r_(j-2) | r_j |
|---|---|---|---|
| P | y0y1 | y1y2 | -y0y2 |
| I | y0y1 | -y0y2 | y1y2 |

Consequently a claim that one stream both discovers the law and uses its
three-read decoder is unjustified. The prior three-read theorem assumes the
update law is already known.

## 3. Two reversible laws: exactly five scalar queries

Suppose L is known to be either P or I and r != (---).

1. Read ports 0 and 1 at t=0 and again at t=1: four scalar queries.
2. Set

       r_2 = y_(0,0)y_(1,0),
       r_0 = y_(0,1)y_(1,1),
       r_1 = -r_0 r_2.

   These recover the full initial r without knowing the law.
3. At least one of r_2 and r_0 is +1. Choose k=0 if r_2=+1, and k=1 otherwise.
   Read that port at t=2, making the fifth scalar query.
4. Compare `z=y_(1,k)y_(2,k)` with the known initial relation. Under P,

       z=r_(k-2);

   under I,

       z=r_k.

   The two values are opposite: their product is
   `r_(k-2)r_k=-r_(k-1)=-1`, because the selected r_(k-1) is +1.

This distinguishes L and r on every allowed input. It uses two fixed ports,
three shell times, and five scalar reads. It uses no rotation-edge query.

## 4. All four laws: exactly six scalar queries

Read ports 0 and 1 at each of t=0,1,2. The first adjacent products recover r as
above. The second adjacent products recover r':

    r'_2=y_(1,0)y_(2,0),
    r'_0=y_(1,1)y_(2,1),
    r'_1=-r'_0 r'_2.

For each non-(---) r, its two distinct cyclic shifts, itself, and (---) are
the four different relation states. Thus the four possible r' values in the
table of section 1 are pairwise different. Exactly one law matches the observed
r'. This is a nonadaptive six-query experiment recovering all twelve possible
targets `(r,L)`.

## 5. Structural proof that four/five queries cannot suffice

The proof treats any adaptive binary-query tree over the nine raw coordinates.
It is stronger than a lower bound limited to the two protocols just constructed.

### 5.1 One axis never supplies a terminal answer

At a fixed port j, let

    u=y_(0,j)y_(1,j),       v=y_(1,j)y_(2,j).

Directly from (1), the number of distinct `(r,L)` targets compatible with a
complete three-sign word is:

| (u,v) | Family {P,I} | Family {P,I,E,S} |
|---|---:|---:|
| (+,+) | 2 | 4 |
| (+,-) | 2 | 4 |
| (-,+) | 2 | 2 |
| (-,-) | 0: absent from this domain | 2 |

The first raw sign can always be chosen independently by the static sign
reference at that port. Thus every nonempty full single-axis observation fiber
contains at least two targets. A partial single-axis word cannot improve this.
Every correct terminal branch of any query tree must therefore have visited
at least two distinct axes.

### 5.2 First readings at new axes can be normalized

Static gauge signs epsilon act on every query by

    y_(t,j) -> epsilon_j y_(t,j),

while preserving `(r,L)`. Each target has its full eight-element gauge orbit
in the permitted input population.

Fix an arbitrary adaptive decision tree and one target. Begin with any input
in that target's orbit. When the tree first queries an axis j, choose its
previously unfixed epsilon_j so this response is +1. This cannot change any
earlier answer, because earlier answers were at other axes. It cannot change
the target either. Subsequent answers at j use this now-fixed epsilon_j.
Continue to the leaf and assign arbitrary signs to any never-visited axes.
The final epsilon gives one single static gauge representative realizing this
whole path. The normalization is therefore an actual allowed input, not a
sequence of physical frame changes during the experiment.

Perform this construction for every target. In the resulting normalized tree,
every first query of a new axis has only its + child. Only repeated visits to
an already visited axis can make a binary split. If the original tree uses at
most m queries on every input, each complete normalized path contains at most
m-2 binary splits, because at least two axes must be visited. Removing unary
nodes leaves a binary tree of depth at most m-2, with at most `2^(m-2)` leaves.
Distinct targets must terminate at distinct leaves. Hence

    number of targets <= 2^(m-2).                              (2)

For {P,I}, there are 3 x 2 = 6 targets, so m>=5. For all four laws, there are
3 x 4 = 12 targets, so m>=6. Combined with sections 3 and 4, these bounds are
sharp. The argument includes arbitrary adaptive coordinate selection, even
queries ordered after inspecting later-time data.

## 6. The shared sector is a real dynamical equivalence

At r=(---), all four D rules equal (+++). Therefore every law sets b=a and
uses precisely the same next signed FRAME. The relation remains (---).
Induction gives identical complete named trajectories and identical III path
histories under all four law names, for every horizon.

No observer of these trajectories can identify the four labels in this sector.
This is not an insufficiency of the five/six-query design: the candidate maps
actually agree there. If the input sector is not guaranteed in advance, the
same initial four queries classify r. When they return (---), the correct
report is "shared sector: the candidate laws coincide here". A rule-discovery
experiment needs a non-(---) preparation. It must not infer universal equality
of the laws merely because a shared-sector experiment cannot distinguish them.

## 7. Reproduction and finite certificate

Run `python check_law_identification.py` from the published adjacent-package
layout, or pass the repository root, baseline package directory or exact BRC
kernel path. It imports `check_streaming_state.py` from this package, whose
loader checks the baseline BRC kernel's exact SHA-256 before any scientific
transition.

The program builds all 96 source-labelled BRC hypotheses using actual III
operations and retains their nine observations, initial signs/twist, law,
relation, two-generator word and source labels. The JSON result includes this
complete observation table.

For each family it computes the exact decision-tree optimum on candidate
subsets. A homogeneous target subset has depth zero; otherwise

    depth(B)=1+min_query max(depth(B_+), depth(B_-)),

where constant queries are discarded. Both children are strict subsets, so
the recurrence terminates. This optimizer allows any query order and checks
one optimal tree against every original BRC input. It is an exact finite
fiber calculation over the retained BRC population, not a separate physical
propagator or numerical approximation.

Actual results:

- 48 inputs for {P,I}: optimal worst-case depth 5, 2,383 DP subproblems;
- 96 inputs for all four laws: optimal worst-case depth 6, 6,167 DP subproblems;
- all 48 five-query protocol cases and all 96 six-query cases pass;
- all 768 static-gauge covariance cases pass;
- all eight shared-sector initial sign/twist inputs give identical complete
  named histories across the four laws.

Native event selection and an experimental mechanism to prepare a desired
relation sector remain separate questions. The new result specifies exactly
which port/time observations distinguish the candidates once those declared
inputs and event interfaces are available.
