# P025 Supplement 66 — Standard Arithmetic Derivative Behind Projective Orientation

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplement 65  
Hard block: `NONE`

## 1. Prior-art identification

Supplement 65 introduced

\[
U(n)=\sum_{p\mid n}v_p(n)\frac np.
\]

This is not a new derivative-like quantity. It is exactly the standard arithmetic derivative

\[
\boxed{U(n)=D(n)=n',}
\]

defined by

\[
p'=1
\]

for every prime and the Leibniz rule

\[
(xy)'=x'y+xy'.
\]

The identity

\[
n'=n\sum_{p\mid n}\frac{v_p(n)}p
\]

and classical size bounds for this derivative are established prior mathematics [SRC-MERIKOSKI-HAUKKANEN-TOSSAVAINEN-2019-ARITHMETIC-SUBDERIVATIVES].

Therefore P025 does not claim the quantity `U`, its formula, or generic bounds on it.

## 2. P025-T133 — projective orientation is a triangle test in one fixed prior-art derivative

The Stage-65 orientation theorem can now be written without new notation:

\[
\boxed{
\rho_c\ge\rho_b
\iff
a'+c'\ge b',
}
\]

\[
\boxed{
\rho_c\ge\rho_a
\iff
b'+c'\ge a'.
}
\]

Hence

\[
\boxed{
b'>a'+c'\Longrightarrow\text{unique b-oriented projective maximum},}
\]

\[
\boxed{
a'>b'+c'\Longrightarrow\text{unique a-oriented projective maximum},}
\]

and otherwise the c-oriented term is a maximizer, with equality producing ties.

The orientation of the entire relation-adapted projective optimum is therefore selected by evaluating **one fixed arithmetic derivative on the three integer blocks**.

No relation-adapted derivative search is required for this future query.

## 3. Relation to the derivative family used by Pasten

Pasten's arithmetic-derivative framework allows prime-coordinate derivations adapted to a chosen equation `a+b=c`. The standard arithmetic derivative corresponds to the fixed prime-coordinate choice

\[
x_p=1
\]

for every prime.

It is generally not additive for the chosen equation. P025-T133 uses it only as a selector for which cyclic projective term dominates; it does not replace the relation-adapted witness family in the Small Derivatives problem.

Thus two very different derivative roles must remain separate:

1. **relation-adapted derivatives:** certificates satisfying the declared additive relation;
2. **the standard derivative `D`:** one fixed external observable whose three values determine projective orientation.

## 4. Classical size bounds do not by themselves improve the Stage-64 tail

If

\[
n=q_1\cdots q_r
\]

with primes repeated according to multiplicity, classical arithmetic-derivative bounds include

\[
\boxed{
r n^{(r-1)/r}\le n'\le\frac{rn}{2}.}
\]

[SRC-MERIKOSKI-HAUKKANEN-TOSSAVAINEN-2019-ARITHMETIC-SUBDERIVATIVES].

These bounds constrain the derivative-mass triangle, but they do not force side superdominance to come from repeated prime powers.

The exact example

\[
1+30=31
\]

has

\[
30'=31>1'+31'=1,
\]

so the `b` orientation is uniquely superdominant although `30` is squarefree.

Therefore the orientation condition alone cannot be routed into the Stage-50/61 large-residual counting mechanism.

## 5. Negative routing consequence

High projective threshold still forces paired residual pressure by Stage 61, regardless of orientation. But the additional statement

\[
\text{``the failing side is derivative-superdominant''}
\]

does not, from the currently imported standard bounds alone, provide another independent large-square or small-radical coordinate.

Accordingly:

> do not claim an improved exceptional exponent from Stage 65 merely because the maximizing side is arithmetic-derivative superdominant.

Any stronger side-oriented tail would require a genuinely additional arithmetic theorem about solutions of

\[
a+b=c
\]

with one standard arithmetic derivative larger than the sum of the other two.

## 6. Precision interpretation

This prior-art collision strengthens rather than weakens the architecture lesson.

A complicated relation-conditioned projective system exposes a tiny selector state

\[
\boxed{
\operatorname{sign}(a'-b'-c'),
\quad
\operatorname{sign}(b'-a'-c')
}
\]

built from a single classical arithmetic function.

Thus the project can reuse an old observable as the exact minimal-looking interface for a new future query, without claiming the observable itself as new.

## 7. Prior-art discipline

The standard arithmetic derivative, its formula, Leibniz rule, logarithmic derivative, and general size bounds are prior mathematics. P025 owns only the exact reduction of its projective-orientation query to the triangle defects among `a',b',c'`; historical novelty of that application remains `NOVELTY_UNVERIFIED`.

## 8. Next frontier

No hard block exists. Continue with:

1. treat the derivative-triangle selector as a task-specific quotient node, not a new arithmetic derivative;
2. search specifically for prior work on inequalities such as `b'>a'+c'` under `a+b=c` before attempting a side-superdominant counting theorem;
3. use Stage 64 rather than generic derivative bounds for current PCC tail estimates;
4. extract the `old theorem -> theorem-native coarse interface` pattern for A2/P023 backflow.
