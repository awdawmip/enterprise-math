# Foundations Under Test

This document records the current mathematical core of Enterprise Math. The statements below are not all established theorems of nature. They are separated into definitions, immediate mathematical consequences, and research hypotheses so that the project can be falsified or revised without losing provenance.

## 1. Primitive state space

The initial numerical state space is the set of nonnegative integers

\[
\mathbb N_0=\{0,1,2,\ldots\}.
\]

Integers are not encodings of hidden real numbers. They are primitive states of the theory.

A scale may be attached to an integer state when comparing different resolutions, but scale is metadata of the state system, not permission to assume an infinitely refinable continuum.

## 2. Exact integer inverse operations

For an integer power \(p\ge2\), define the integer root

\[
R_p(n)=\max\{k\in\mathbb N_0:k^p\le n\}.
\]

This is an exact operation in the theory. It is not defined as an approximation to a hidden real root.

For \(p=2\):

\[
R_2(2)=1,
\qquad
R_2(200)=14,
\qquad
R_2(20000)=141.
\]

The defining relation is

\[
k^p\le n<(k+1)^p
\quad\Longleftrightarrow\quad
R_p(n)=k.
\]

## 3. Collapse operators

Define the power-collapse operator

\[
C_p(n)=R_p(n)^p.
\]

For squares,

\[
C_2(20000)=19881.
\]

Because

\[
141^2=19881,
\qquad
142^2=20164,
\]

we have

\[
19881\le n\le20163
\quad\Longrightarrow\quad
C_2(n)=19881.
\]

Therefore the state 19881 has 283 direct preimages under this collapse map.

### Immediate properties

For every \(p\ge2\), \(C_p\) is:

- reductive: \(C_p(n)\le n\);
- monotone: \(n\le m\Rightarrow C_p(n)\le C_p(m)\);
- idempotent: \(C_p(C_p(n))=C_p(n)\).

Its fixed points are exactly the perfect \(p\)-th powers.

This is structurally close to an interior operator on an ordered set. That mathematical similarity is useful prior art; it does not by itself establish the physical interpretation proposed here.

## 4. No hidden remainder axiom candidate

The current physical interpretation under test is stronger than ordinary quantization or coarse-graining.

If

\[
n\rightarrow C_p(n),
\]

the difference

\[
n-C_p(n)
\]

is not assumed to remain in nature as a hidden state variable. It can be computed externally by comparing two states, but it is not part of the post-transition state unless a separate law explicitly carries it forward.

Thus the map is ontologically many-to-one, not merely observationally many-to-one.

This is a research hypothesis, not a theorem derived from the arithmetic definition alone.

## 5. Scale compatibility

Let \(B\ge2\) be an integer scale base. A refined square-root query may be represented by

\[
R_{2,s}(n)=R_2(nB^{2s}).
\]

The states are integers at every scale. No decimal expansion is introduced.

A desired compatibility condition is

\[
Q_B(R_{2,s+1}(n))=R_{2,s}(n),
\]

where the integer quotient operator is defined directly by

\[
Q_B(a)=\max\{q\in\mathbb N_0:qB\le a\}.
\]

For example,

\[
1\leftarrow14\leftarrow141\leftarrow1414
\]

is a compatible family of integer states for progressively refined square-root queries based on the state 2.

If nature has a maximum resolution, this chain terminates. No infinite completion is required inside the theory.

## 5A. Represented precision and future-safe precision

A represented precision is an explicit many-to-one partition of the current fine state space. It says which current states are represented as the same state at the declared resolution.

That partition is not automatically sufficient for every future computation.

Given a declared family of future operations and observations, define the **future-safe precision** to be the coarsest refinement of the represented precision for which all required future behavior descends to the retained state.

Therefore Enterprise Math distinguishes

\[
\boxed{
\text{represented precision}
\neq
\text{future-safe precision in general}.
}
\]

P023 gives the generic quotient/congruence criterion for this distinction. P024 gives an exact integer-translation specialization: when observations are cut by integer boundaries `B` and the declared future action language has reachable cumulative translations `M`, the present distinctions that can still be read by the future are the pulled-back boundary orbit

\[
\boxed{B-M.}
\]

The resulting precision cells need not be globally uniform. A uniform scale is one possible precision geometry, not a foundational requirement.

In particular, action language and state topology can change the minimal safe precision even when the nominal measurement scale is unchanged. This is a mathematical statement about predictive sufficiency, not by itself a claim that nature selects a task-dependent physical ontology.

## 5B. Four structural principles of future sufficiency

Cross-route work in P007/P008/P018/P023/P024 and P017/E002 compresses the abstract definition in 5A into four directly usable mathematical principles. These are principles of proof state and quotient sufficiency; they are not automatically physical-ontology axioms.

### 1. States move forward; boundaries and proof obligations move backward

If a forward action `F` has a left adjoint `lambda_F`,

\[
\lambda_F(b)\le x
\iff
b\le F(x),
\]

then the exact present obligation induced by a future threshold `b` is `lambda_F(b)`.

Forward dynamics and query obligations therefore compose in opposite directions:

\[
\boxed{
\lambda_{G\circ F}
=
\lambda_F\circ\lambda_G.
}
\]

The integer-root and integer-quotient adjunctions of P008 and the P024 boundary-pullback calculus are consequently two views of one structure: arithmetic states evolve forward while future query boundaries are transported backward.

### 2. A noncommutation defect is an exact repair state, not approximation error

If a coarse representation `q` and a future action `F` cannot satisfy

\[
q\circ F=\bar F\circ q,
\]

the correct response is not to call the discrepancy an “error,” nor to restore the entire fine state by default. One should retain only the minimum repair inside each coarse fiber that determines `q(F(x))`.

Carry, borrow, crossing bits, and commutation defects already appearing in P018/P023 are such **exact finite witnesses**.

The foundational research default is therefore

\[
\boxed{
\text{defect}=\text{explicit finite information obligation},
}
\]

rather than a continuous discrepancy between a hidden truth and an approximation.

### 3. Prefer actual images to candidate supersets

Suppose a state carries a shell label `i` and an internal coordinate in `W_i`. After a later map `G`, the shell label is recoverable from the retained coordinate exactly when distinct realized shell images are pairwise disjoint:

\[
\boxed{
G(W_i)\cap G(W_j)=\varnothing
\qquad(i\ne j).
}
\]

Replacing the realized image by a strict candidate superset can therefore manufacture collisions and multiplicities never realized by the original state system.

Coarse representation does more than “see less” when implemented as uncontrolled over-approximation: it can actively manufacture false structure.

### 4. Finiteness may be task-local first

Future-safe calculus does not require the whole state universe to be finite.

It is enough that the state orbit, boundary orbit, quotient window, guard slice, or fixed interval actually reachable by the declared task lies in a finite closure.

For example, a P019 collapse orbit on the natural numbers is trapped in

\[
[C_L(n_0),n_0],
\]

while P024 needs only the relevant boundary orbit to close finitely.

A weaker and more appropriate foundational research target is therefore

\[
\boxed{
\text{task-local finite closure},
}

rather than a globally finite world.

## 5C. A number-theory example: coarsening can manufacture false collisions

The P017 consecutive-square basin gives the clearest current pure-integer example.

For least prime `p`, the exact stripped cofactor window is

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

The P007 quotient-window mother theorem together with P017 L054 gives

\[
\boxed{k\ge4\Longrightarrow W_p(k)\text{ are pairwise disjoint across prime shells}.}
\]

Thus the exact cofactor `q=n/p` already encodes the least-prime shell label.

If each exact window is first enlarged, after square-root projection, to the candidate pair `{j_p,j_p+1}`, L052 needs

\[
k\ge15
\]

to make those coarse candidate pairs pairwise disjoint.

But retaining the exact window and then computing the realized root image, new L055 proves that actual lower-band shell images are already pairwise disjoint from

\[
\boxed{k\ge9},
\]

with `k=8,p=2,r=3,root=5` as a sharp witness.

The three thresholds describe three different retained precisions:

\[
\boxed{
\text{exact quotient}:4,
\qquad
\text{actual root image}:9,
\qquad
\text{enlarged candidate pair}:15.
}
\]

They do not conflict. Instead they show rigorously that

> **lower structural precision can manufacture collisions absent from the realized system, while retaining the relevant exact subwindow can eliminate those false collisions.**

This is a mathematical statement about proof-state sufficiency, not a claim that physical ontology changes with the research task.

## 6. Classical identities are not assumed

Because integer root is not a two-sided inverse of exponentiation, classical real identities must be re-proved rather than imported.

For example,

\[
R_2(n^2)=n
\]

for nonnegative integers \(n\), but generally

\[
R_2(n)^2\ne n.
\]

Likewise, generally

\[
R_2(a)R_2(b)\ne R_2(ab).
\]

These are not numerical errors. They are algebraic features of a different operation.

## 7. Forward dynamics

Let a state evolve through maps

\[
X_{t+1}=T_t(X_t).
\]

The maps are allowed to be non-injective. No inverse map is required.

Define the cumulative map

\[
F_t=T_{t-1}\circ\cdots\circ T_0.
\]

For two initial states, define

\[
x\sim_t y
\quad\Longleftrightarrow\quad
F_t(x)=F_t(y).
\]

If \(x\sim_t y\), then necessarily \(x\sim_{t+1}y\). Once two histories merge under deterministic forward evolution, later function composition cannot separate them again.

Therefore the equivalence class

\[
[x]_t=\{y:F_t(y)=F_t(x)\}
\]

can only remain the same size or grow.

## 8. Integer irreversibility measures

The primary internal quantity should remain integer-valued:

\[
M_t(x)=|[x]_t|.
\]

Then

\[
M_{t+1}(x)\ge M_t(x).
\]

This gives a discrete monotone measure of historical merging without introducing logarithms or real-valued entropy as primitive objects.

If a logarithmic entropy is useful for comparison with conventional information theory, it should initially be treated as an external derived representation, not as part of the primitive arithmetic.

An integer information level can instead be defined, for example, by

\[
L_B(m)=\min\{\ell\in\mathbb N_0:m\le B^\ell\},
\]

which remains an integer map.

## 9. Open foundational questions

1. Which operations should be primitive and which should be derived?
2. Should signed integers be primitive, or should direction/sign be a separate state component?
3. What is the correct discrete replacement for division, ratios, and dimensional analysis?
4. Which notion of distance produces a useful geometry without silently restoring real-valued Euclidean distance?
5. Which families of collapse maps generate nontrivial forward dynamics rather than reaching fixed points immediately?
6. Can the monotonic growth of preimage classes be connected to thermodynamic entropy under explicit physical assumptions?
7. Which observed physical laws contradict an ontologically non-invertible foundation?
8. Which parts of calculus can be reconstructed as finite-scale difference and accumulation operators?
9. Which future-safe precision objects admit compact structured representations, and when must a nonuniform boundary/detail layer be retained?
10. Which infinite state systems have declared tasks with finite boundary/orbit closure and therefore admit completely finite exact compilation?
11. How should the false-collision / false-multiplicity cost created by candidate supersets relative to actual images be quantified systematically?

## 10. Status discipline

A proposed physical interpretation must not be promoted to a theorem merely because the integer mathematics is consistent. The repository should keep the following categories separate:

- definition;
- theorem;
- computational observation;
- conjecture;
- physical hypothesis;
- external analogy.
