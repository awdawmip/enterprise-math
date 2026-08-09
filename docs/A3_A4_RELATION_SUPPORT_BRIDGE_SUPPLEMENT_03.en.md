# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 03

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact fine-support threshold coordinates and task-minimal repair of an A3 partition quotient for A4 MAY/MUST support queries

## 1. Motivation

Stage 01 showed that an A3 partition quotient can hide fine support through signed cancellation. Stage 02/03 showed that staged support can also depend on intermediate witnesses.

P023 asks the next precise question:

> if a future query needs fine support information, what is the minimum detail that must be retained?

This note answers that question exactly for the A4 **MAY/MUST radius-query language**.

Work on the A3 zero-relation quotient `X0` with integer metric

\[
\rho(x,y)=\min\{r:xR_ry\}.
\]

Let `P={A,B,...}` be any partition of `X0` into coarse blocks.

## 2. B10 — pairwise MAY/MUST threshold interval

For two coarse blocks `A,B`, define

\[
\boxed{
d^-_{AB}=\min_{x\in A,y\in B}\rho(x,y),
\qquad
d^+_{AB}=\max_{x\in A,y\in B}\rho(x,y).
}
\]

These are finite non-negative integers.

For radius `r`, define:

- `MAY_r(A,B)`: at least one fine pair across `A,B` is `r`-supported;
- `MUST_r(A,B)`: every fine pair across `A,B` is `r`-supported.

Then

\[
\boxed{
MAY_r(A,B)\iff d^-_{AB}\le r,
}
\]

and

\[
\boxed{
MUST_r(A,B)\iff d^+_{AB}\le r.
}
\]

Thus the complete all-radius MAY/MUST behavior is encoded by the integer interval

\[
\boxed{I_{AB}=[d^-_{AB},d^+_{AB}].}
\]

The interval has an exact three-zone semantics:

1. `r<d^-`: no fine witness exists;
2. `d^-<=r<d^+`: MAY is true but MUST is false;
3. `r>=d^+`: every fine pair is supported.

Define the **support uncertainty width**

\[
\boxed{W_{AB}=d^+_{AB}-d^-_{AB}.}
\]

This measures the radius range in which the coarse block pair has mixed fine support behavior.

## 3. B11 — task-minimal P023 repair coordinates

Let `q_P` be the A3 coarse partition state map. Consider a fixed coarse block pair `A,B` as part of the declared future query language.

### MUST-only language

The truth sequence

\[
(MUST_0,MUST_1,MUST_2,\ldots)
\]

is completely determined by `d^+`, and conversely determines `d^+` as the first radius where MUST becomes true.

Therefore, up to relabeling of quotient classes,

\[
\boxed{(q_P,d^+_{AB})}
\]

is the P023 coarsest one-step repair for the full all-radius MUST query on that pair.

### MAY-only language

Likewise,

\[
\boxed{(q_P,d^-_{AB})}
\]

is the coarsest repair for the full all-radius MAY query.

### Combined MAY/MUST language

The pair

\[
\boxed{(d^-_{AB},d^+_{AB})}
\]

is a complete and task-minimal coordinate for the full MAY/MUST radius language. For an entire coarse partition, use the corresponding finite threshold matrices.

For one fixed radius only, P023-T02 reduces the repair further to the single required truth bit. The integer thresholds are minimal for the **whole radius family**, not for one preselected query.

### Exact future-safety criterion

The original quotient `q_P` is already future-safe for one of these query languages exactly when its required threshold coordinate is constant on every `q_P` fiber. B03 shows that this constancy fails in general.

## 4. Coarse A3 support threshold

The A3 partition quotient itself produces aggregated capacities and relation

\[
m'_A=\sum_{i\in A}m_i,
\qquad
Z'_{AB}=\sum_{i\in A,j\in B}Z_{ij}.
\]

Define its direct coarse threshold

\[
\boxed{
\bar\rho_{AB}
=
\left\lceil\frac{|Z'_{AB}|}{m'_A m'_B}\right\rceil.
}
\]

B02 implies

\[
\boxed{\bar\rho_{AB}\le d^+_{AB}.}
\]

Therefore define the **hidden MUST defect**

\[
\boxed{H^+_{AB}=d^+_{AB}-\bar\rho_{AB}\ge0.}
\]

`H^+` measures how far the direct coarse support radius can understate the radius required to certify all fine pairs.

## 5. B12 — there is no analogous order relation with MAY threshold

No universal inequality relates `bar rho` and `d^-`.

### Coarse threshold can be smaller than MAY threshold

Take unit fine values:

- coarse block `A={0,10}`;
- coarse block `B={5,5}`.

Every fine cross distance is `5`, so

\[
d^-_{AB}=d^+_{AB}=5.
\]

But both coarse averages are `5`, hence

\[
\bar\rho_{AB}=0.
\]

Thus `bar rho < d^-`.

### Coarse threshold can be larger than MAY threshold

Take

- `A={0,100}`;
- `B={0}`.

A fine zero-distance witness exists, so `d^-_{AB}=0`, while the aggregate state of `A` has normalized value `50`, giving

\[
\bar\rho_{AB}=50.
\]

Thus `bar rho > d^-`.

Hence the coarse A3 support predicate is neither a MAY summary nor a MUST summary. It is a different aggregate observable.

## 6. Exact sufficiency statements

For a fixed coarse pair `A,B`:

- coarse support alone answers all-radius MUST exactly iff `bar rho=d^+` **and** the value is invariant across the relevant coarse-state fiber;
- coarse support alone answers all-radius MAY exactly iff `bar rho=d^-` with the same fiber-invariance obligation;
- coarse support alone answers the combined MAY/MUST language only when
  \[
  \bar\rho=d^-=d^+
  \]
  throughout the quotient fiber.

Within one fine state, equality of the numbers is only an observation. P023 future safety remains a fiber-level statement across all fine states represented by the same coarse quotient.

This distinction prevents a common error: matching one example does not prove that the quotient representation is closed under the future query.

## 7. Relation to A4 MAY/MUST semantics

A4 already distinguishes possible support from guaranteed support. B10 shows that in the A3-generated metric subclass these logical modalities have canonical finite integer coordinates:

\[
MAY\leftrightarrow d^-,
\qquad
MUST\leftrightarrow d^+.
\]

So the interval `[d^-,d^+]` is a compact bridge object between:

- A3 structured relation state;
- A4 modal support semantics;
- A2/P023 task-relative precision repair.

## 8. Relation to staged/common-target queries

The threshold interval is sufficient for one-step MAY/MUST radius questions, but not generally for staged/common-target queries. Stage 02/03 already shows that intermediate-state availability is additional information.

Therefore the repair hierarchy is now explicit:

\[
\text{endpoint MAY/MUST}
\quad\Rightarrow\quad
(d^-,d^+),
\]

while

\[
\text{staged/common-target composition}
\quad\Rightarrow\quad
\text{interpolation/geodesic witness data as additionally required}.
\]

This is a concrete example of the P023 principle that the minimum legitimate state depends on the declared future operation language.

## 9. Prior-art discipline

Min/max distances between sets, existential/universal relation lifting, abstract interpretation MAY/MUST semantics, and quotient repair are established mathematical/computer-science patterns.

The project-specific target is their exact integer integration with the A3 weighted relation quotient, the A4 support family generated in Stage 01, and P023's task-relative legal-collapse discipline.

## 10. Executable reference

The bridge reference implementation adds:

- coarse-partition MAY/MUST threshold matrices `(d^-,d^+)`;
- direct coarse A3 threshold matrix `bar rho`;
- support uncertainty width `W`;
- hidden MUST defect `H^+`;
- regression examples proving both directions of B12.
