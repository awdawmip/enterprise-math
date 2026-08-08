# Origin of the Research Direction

This document preserves the conceptual path that produced Enterprise Math. It is intentionally not a raw chat transcript. It records the sequence of ideas, mistakes, corrections, and resulting research commitments that materially shaped the project.

## 1. Finite resolution before continuum

The discussion began from a dissatisfaction with treating the infinitely divisible real number line as the literal numerical substrate of nature.

The alternative intuition was that a natural quantity should be described by a finite state together with a scale or resolution, and that there should be no physically meaningful refinement beyond the highest available resolution.

This suggested an integer-first computational model: use integer counts at an explicit scale rather than decimals as primitive values.

## 2. Integer scale instead of floating point

The next step was to notice that a large range of magnitudes can be represented by an integer state plus an integer scale. This can remove ordinary binary floating-point representation errors for operations that remain exact in the integer representation.

At this stage, however, the first interpretation still assumed that operations such as square root ultimately referred to a hidden real value and that the integer system merely represented it at finite resolution.

That interpretation was rejected.

## 3. First decisive correction: the root itself is discrete

The key correction was:

> In this system, the square root operation itself is different. There is no hidden decimal answer behind it.

Thus

\[
R_2(2)=1,
\qquad
R_2(200)=14,
\qquad
R_2(20000)=141
\]

are exact statements of the system, not truncated versions of a real-valued square root.

This moved the project from "integer representation of real arithmetic" to "integer-closed arithmetic with its own operation semantics."

The scale chain

\[
1\leftarrow14\leftarrow141\leftarrow1414
\]

was then understood as a family of compatible integer states across resolutions, rather than decimal digits of a hidden real number.

## 4. Classical identities must be re-earned

Once the root operation became genuinely discrete, classical identities could no longer be assumed. For example,

\[
R_2(2)^2=1
\]

while

\[
R_2(2\cdot2)=2.
\]

The failure of familiar identities is not treated as numerical error. It is evidence that the algebra must be rebuilt from the new definitions.

## 5. Second decisive correction: no hidden remainder

The first attempt to connect irreversible integer operations with time and entropy used the conventional information-theoretic picture: retain a quotient or root together with a remainder, then describe irreversibility as discarding that remainder.

That interpretation was also rejected.

The stronger proposal is ontological:

> If the mathematical system is intended as an abstraction of natural law itself, there is no requirement that a discarded remainder exists anywhere in the post-transition state.

The state transition is allowed to be fundamentally many-to-one.

## 6. Collapse, not approximation

For square-root collapse, define

\[
C_2(n)=R_2(n)^2.
\]

Then

\[
20000\rightarrow19881.
\]

Moreover,

\[
19881,19882,\ldots,20163
\]

all evolve to 19881 under the same collapse map.

The difference between a pre-state and the collapsed state is a relation computed by an external analyst. It is not automatically a surviving physical variable.

This is the point where the project acquired the notion of **ontological collapse**.

## 7. Time as forward-only composition

If natural evolution is built from deterministic many-to-one maps, inverse evolution is not generally defined. The natural algebra of time is therefore closer to forward composition than to a group with inverse elements.

For cumulative evolution \(F_t\), define two initial states to be merged at time \(t\) when they have the same image under \(F_t\).

Once merged, they remain merged under later deterministic function composition. This gives an immediate monotonic structure on preimage classes and suggests a discrete route toward an arrow of time.

## 8. Entropy without hidden information

The project therefore shifted from "how much information was erased?" to a different question:

> How many distinct earlier states have the same current state?

The primitive quantity is the integer preimage multiplicity. Conventional logarithmic entropy is, at most, an external comparison layer until an internally discrete entropy theory is developed.

Existing work on preimage entropy and non-invertible dynamics is relevant prior art because it studies complexity through preimage structure. It does not establish the stronger ontological claim of this project.

## 9. Naming

The Chinese project name was chosen as a term combining forward movement and selection of a valid state. The English project brand was chosen as **Enterprise Math**.

The name is a project identity, not a claim that existing "enterprise mathematics" in education or business literature has the same meaning.

## 10. Methodological lessons

Three research rules emerged directly from the corrections above:

1. Do not reintroduce the real continuum as a hidden "true answer" after defining an integer system.
2. Do not invent hidden state variables merely to preserve reversibility if the theory is explicitly testing ontological irreversibility.
3. When a proposed structure resembles established mathematics, use the established terminology and results as comparison tools, but keep the project's stronger physical interpretation clearly labeled as a hypothesis.
