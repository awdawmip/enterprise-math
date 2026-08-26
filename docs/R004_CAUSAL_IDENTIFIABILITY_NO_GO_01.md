# R004 / FQ-20260810-007 — Finite Counterfactual-Completion No-Go 01

Status: `PROVED_WIP / EXECUTABLE_CROSSCHECKED / OWNER_LOCAL / NOT CANONICAL`

Owner: `research/r004-causal-identifiability-v1`

Foundation question: `FQ-20260810-007`

Hard block: `NONE`

## 1. Result in one sentence

For every **finite horizon**, unrestricted hidden-state extension can compile a finite A4 relation process, and likewise a finite total rational stochastic intervention process, into an ex-ante finite deterministic **counterfactual master** whose observable finite-horizon behavior is exactly the same.

Therefore finite branching, finite randomness, adaptive intervention syntax, state-extensional observable access, and relation-valued support **do not by themselves make pre-sampling falsifiable**.

What must fail is not finiteness but **closure under arbitrary latent counterfactual extension**.

This is a negative identifiability result. It is not a physical hidden-variable proposal.

## 2. Scope and inherited boundaries

This note preserves the existing owner boundaries.

- FQ-004 continues to own the distinction between exact state, present observation, and declared-future-safe equality.
- FQ-006 continues to own legality-sensitive deterministic partial-operation quotients. Disabledness is not silently identity.
- A4 continues to own multivalued relation/support semantics and witness information.
- R004 only asks whether those finite operational semantics can distinguish ontic online generation from an unrestricted latent completion.

No Bell locality, measurement independence, quantum mechanics, continuum law, cosmology, or physical hidden-variable ontology is assumed here.

## 3. Deterministic counterfactual master

Let

- `X` be a finite state set;
- `A` be a finite declared action set;
- for each `a in A`, let `R_a subseteq X x X` be a finite relation;
- `x in X` be the initial visible state;
- `H >= 0` be a finite horizon.

A depth-`H` **counterfactual master** rooted at `x` is a deterministic tree that stores, at every latent node and for **every** declared action `a`, either

- `None` if `a` is disabled at that visible node, or
- one chosen successor `y` with `x R_a y`, together with a complete depth-`H-1` child master rooted at `y`.

Thus one master contains a complete contingent response for every action that *might* be chosen later. Only the branch selected by the actual intervention word is exposed.

The master is a finite analysis object. Its size can grow rapidly with horizon.

## 4. R004-CI-T01 — finite relation-support completion

Define `M_H(x)` recursively.

At depth zero,

`M_0(x) = { leaf(x) }`.

For depth `h+1`, for each action `a` define the available latent branch choices

- `{None}` if `R_a(x)` is empty;
- `union_(y in R_a(x)) M_h(y)` otherwise.

Then `M_(h+1)(x)` is the Cartesian product of those choices across every declared action, packaged as one action-indexed master node.

### Theorem

For every literal action word `w` with `|w| <= H`,

`raw_support(x,w) = { target(m,w) : m in M_H(x), target(m,w) is defined }`.

In words: the raw A4 reachable support after `w` is exactly the set of targets obtained by executing `w` through all pre-sampled deterministic masters.

### Proof

Induct on the word length.

The empty word returns `x` on both sides.

Suppose `w = a v`.

If `R_a(x)` is empty, every master has branch `a=None`, so the compiled support is empty, exactly as the raw relation support.

Otherwise, the `a`-branch choices appearing among `M_H(x)` are **all** child masters in

`union_(y in R_a(x)) M_(H-1)(y)`.

Executing the suffix `v` therefore yields the union over `y in R_a(x)` of the compiled suffix supports. By the induction hypothesis each such support equals the raw support from `y` under `v`. Their union is exactly ordinary relational composition for `a v`.

No branch outside the raw relation can appear, and every raw branch has a corresponding master choice. Hence equality holds.

## 5. Consequence for A4 relation semantics

A4 multivalued support is operationally genuine as a relation, but finite support branching alone does not certify **ontic generation at intervention time**.

For every finite horizon, the same visible relation-word supports can be produced by a finite family of deterministic masters selected before the action word is known.

This does **not** collapse A4 into a function. It proves only an observational completion result under unrestricted hidden refinement.

The distinction is:

`raw visible relation is multivalued`

while

`one latent master is deterministic but the hidden master is unknown`.

The family of masters reproduces exactly the visible support language.

## 6. R004-CI-T02 — one policy-independent rational master measure

Now let every action `a` be a **total rational stochastic kernel**

`K_a(y | x) in Q_{>=0}`,

with finite support and row sum exactly one.

Recursively construct a rational probability measure `mu_(x,H)` over deterministic masters.

At a node `(x,h+1)`, and separately for every counterfactual action `a`:

1. sample a successor `y` with weight `K_a(y|x)`;
2. sample a child master from `mu_(y,h)`;
3. take the product of those action-indexed child distributions.

The crucial point is that **all action branches are sampled ex ante**. The resulting measure is fixed before any future policy decides which action to expose.

### Theorem: literal words

For every action word `w` with `|w| <= H`, pushing `mu_(x,H)` through the deterministic master execution map for `w` gives exactly the ordinary rational kernel law

`delta_x K_w`.

### Proof

Induct on word length. At the first selected action `a`, the marginal distribution of the pre-sampled `a`-child is exactly the mixture

`K_a(y|x) * mu_(y,H-1)`.

Unused counterfactual branches integrate out because their product measures have total mass one. Apply the induction hypothesis to the selected child and the remaining suffix.

## 7. R004-CI-T03 — adaptive deterministic interventions do not escape the same master

Let a deterministic policy choose the next action as an arbitrary function of the **visible history so far**.

The same ex-ante measure `mu_(x,H)` from T02, without knowing which policy will later be used, reproduces the exact visible history law generated by the original rational kernels under that policy.

### Proof

Induct on visible history depth.

Conditioned on any visible history reached so far, the policy selects one declared action. The corresponding child branch was already sampled in the master with exactly the kernel conditional law for the current visible state, while all unused action branches remain marginalized out. Therefore the one-step conditional history law agrees. Multiplying through the finite tree gives equality of the complete history law.

Hence adaptive intervention syntax does not by itself defeat finite pre-sampling.

## 8. R004-CI-C01 — latent-extension nonclosure is necessary for falsifiability

Consider any candidate finite causal/intervention primitive `C` whose declared operational behavior through horizon `H` is captured by one of the above finite relation/support or total rational-kernel semantics.

If the admissible model class is closed under adjoining the corresponding finite counterfactual master as hidden state while retaining the same visible projection, then no experiment expressible in that declared finite-horizon operational language can distinguish

`online generated alternatives`

from

`ex-ante finite counterfactual completion`.

Therefore an operational obstruction to pre-sampling requires at least one **additional admissibility law that breaks this hidden-extension closure**.

This is the strongest Foundation-facing conclusion of this checkpoint.

## 9. What happens to the four first candidate primitives

### 9.1 Intervention-local response ownership — insufficient alone

Saying that one intervention reads only its declared local response does not help if the hidden state may contain a separate pre-sampled local response subtree for every possible intervention context.

Local *access* is compatible with global ex-ante storage of all local branches.

To obstruct completion, locality must constrain the **allowed joint latent factorization/correlation structure**, not merely which coordinate is read at runtime.

### 9.2 State-extensional causal accessibility — insufficient alone

Visible future operations can remain completely state-extensional after projection while hidden master coordinates refine the visible state.

Thus

`future operation depends only on current retained visible state`

is not enough unless the theory also forbids the relevant hidden refinement or requires the retained state to be ontically complete by an independent axiom.

### 9.3 Bounded latent capacity — a real obstruction, but it is an extra resource axiom

Historical R004 already showed that a full-support `m`-step, `r`-ary deterministic response language needs at least `r^m` latent seed states for literal pre-sampling.

The new no-go clarifies the role of that result: a capacity bound can make pre-sampling falsifiable **only because the bound itself forbids otherwise valid hidden counterfactual completions**.

It is therefore a candidate physical/ontic resource axiom, not a consequence of finite operational semantics.

### 9.4 Composition/factorization locality — potentially obstructive only when substantive

A factorization law can obstruct pre-sampling if it forbids arbitrary joint counterfactual masters or arbitrary correlations between contexts/regions.

But then the factorization/independence law is exactly the extra causal admissibility content doing the work. It must be independently justified and testable; it cannot be smuggled in as a restatement of “no global pre-sampled table”.

Bell-locality plus measurement independence is one prior-art example of such a substantive restriction, but it is not adopted here as a Foundation axiom.

## 10. What FQ-007 can now say

This checkpoint supports a **negative answer for a broad candidate class**:

> Finite project-native relation/support, state-extensional accessibility, and finite rational intervention semantics remain operationally compatible with finite ex-ante counterfactual completion at every fixed finite horizon whenever arbitrary latent refinements are admissible.

Therefore current Foundation semantics cannot infer ontic online generation from those structures alone.

The minimum *type* of additional input is now sharper:

`an independently justified causal/physical admissibility axiom that makes the model class non-closed under arbitrary counterfactual-master extension`.

Examples of such axiom types include

- an ontic latent-capacity/resource bound;
- a cross-context independence/factorization restriction;
- a prohibition on specific hidden common causes or inaccessible counterfactual coordinates;
- another experimentally grounded restriction that excludes at least one otherwise valid master completion.

This theorem does **not** identify one unique weakest such axiom. Different restrictions can be logically incomparable.

## 11. Exact executable evidence

Owner-local implementation:

- `src/enterprise_math/r004_causal_identifiability_completion.py`
- `tests/test_r004_causal_identifiability_completion.py`

Independent construction/checks performed for this checkpoint include:

1. all `16 x 16` pairs of relations on a two-state set, both sources, through horizon two: **512/512** source-family cases satisfy exact raw-support = master-support equality for every word;
2. exact disabled-word preservation;
3. a hidden-branch reactivation relation witness;
4. an exact two-state, two-action rational kernel family through horizon three: one policy-independent master measure reproduces every literal word law;
5. the same master measure reproduces an adaptive history-dependent intervention policy exactly;
6. all stochastic checks use `fractions.Fraction`; no floating approximation is needed.

These are executable cross-checks of the finite constructions, not replacements for the proofs above.

## 12. Prior-art boundary

No generic novelty is claimed for randomization by complete contingent plans, functional/random-seed representation, finite product coupling, or latent-variable determinization.

Relevant established lines include:

- H. W. Kuhn, *Extensive Games and the Problem of Information* (1953): extensive-form pure/behavioral contingent strategy structure and realization equivalence under its game-theoretic hypotheses;
- functional representation lemmas in probability/information theory; a modern strong form is C. T. Li and A. El Gamal, *Strong Functional Representation Lemma and Applications to Coding Theorems* (2017, arXiv:1701.02827).

The Enterprise Math contribution at this checkpoint is narrower: an explicit project-native finite no-go routing that connects those standard completion ideas to FQ-004/FQ-006/A4 ownership and identifies **latent-extension nonclosure** as the missing kind of causal/physical input for FQ-007.

Bell/CHSH and measurement-dependence theory remain prior-art pressure tests from historical R004, not Foundation axioms.

## 13. Recommended FQ-007 return status

Recommended steward-facing return:

`NEGATIVE_CHECKPOINT / BROAD NO-GO CLASS PROVED_WIP / ADDITIONAL AXIOM TYPE IDENTIFIED`.

Do **not** close FQ-007 as a positive primitive discovery.

A steward may decide that the broad no-go already answers the Foundation-level question in the negative, or may keep FQ-007 open only for the narrower follow-up:

> Which independently motivated latent-extension-nonclosure axiom, if any, belongs in Enterprise Math rather than in an application/physical model?

That second question is a modeling/foundation-selection question and must not be answered by strengthening R004 assumptions ad hoc.
