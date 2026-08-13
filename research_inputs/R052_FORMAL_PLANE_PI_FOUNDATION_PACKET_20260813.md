# R052 Formal Plane Pi — Foundation Packet

Status: `PURE_FORMAL_MATHEMATICS / ENGINEERING_TARGET_ISOLATED / CLASSICAL_PI_NUMERIC_FORBIDDEN / NOT_CANONICAL`

This packet defines the only problem-side content that R052 may assume at startup beyond current project-level Foundational Logic and Native-Semantics Admissibility Gate V3.

## 1. Mother question

Study the following without assuming the classical Euclidean definition of pi:

> What is the weakest formal notion of a plane under which one or more internally defined `pi-role` objects become well-typed, and what additional axioms force independently defined pi-roles to coincide?

A successful outcome is not required to produce a numerical constant. Valid outcomes include:

- `PI_ROLE_NOT_WELL_TYPED` under a weak signature;
- existence but non-uniqueness of pi-role objects;
- multiple inequivalent pi-roles in the same formal plane;
- a no-go theorem showing that a proposed role secretly requires extra structure;
- a minimal axiom package forcing two or more previously independent roles to coincide;
- a finite/refinement theorem producing stable symbolic role limits;
- proof that a broad formal plane class cannot carry one universal pi-role.

## 2. Definition is not inherited

Do not begin with any of the following as a native definition unless a later formal signature explicitly adds and types it:

- circle;
- center;
- radius;
- equidistance locus;
- Euclidean distance;
- circumference;
- Euclidean area;
- angle measured in radians;
- `2π` per turn;
- sine/cosine/Fourier normalization;
- Gaussian/integral normalization;
- classical pi as a named scalar constant.

The classical Euclidean object may be used only in the final identification stage after all relevant role definitions, dependencies and theorem statements are frozen.

## 3. Formal plane is itself part of the research problem

R052 must not silently identify `plane` with `R^2` or with one textbook axiom system.

Researchers may generate and compare formal signatures using, for example, some subset of:

- finite carriers;
- point/line or cell/incidence language;
- adjacency/contact;
- betweenness/order;
- orientation/cyclic order;
- translation or affine composition;
- congruence;
- metric or norm structure;
- valuation/measure structure;
- boundary operators;
- group actions;
- path/winding/homology-like finite data;
- refinement/coarsening systems;
- finite transformation semigroups or groups.

This list is exploratory, not a startup checklist and not a requirement to use every item. Researchers may introduce other precisely typed structures. Every added structure must be declared and its logical strength audited.

## 4. Pi-role discipline

A `pi-role` is not 'anything numerically close to classical pi'. It is a formally typed object satisfying a role predicate stated entirely in the current formal language.

Before any classical comparison, every role must freeze:

1. formal signature;
2. object/codomain type;
3. exact construction;
4. role predicate;
5. dependency graph;
6. invariance/equivariance or choice-dependence claim;
7. existence status;
8. uniqueness/non-uniqueness status;
9. countermodels or degeneracies;
10. whether it is native, operational, quotient/readout, or limit-derived.

Possible role families may include rotation-like, winding-like, boundary/valuation-like, refinement-limit, recurrence/group-action, curvature/turning, isoperimetric, or spectral roles, but none is mandatory and none may be defined by copying a classical pi formula.

## 5. Typability before value

For every formal signature, ask in this order:

1. Is the candidate role language well-typed?
2. Does a role object exist?
3. Is it invariant under the signature's automorphisms/equivalences?
4. Is it unique?
5. If multiple roles exist, are they provably equal?
6. Which additional axioms are exactly used by each implication?

A proof that a role is not well-typed or not unique is a first-class result.

## 6. Multiplicity is allowed

R052 must actively search for models in which independently defined role objects differ.

Do not assume

`pi_rotation = pi_winding = pi_measure = pi_spectral = ...`.

If equality is claimed, provide a theorem with explicit assumptions. If equality fails, preserve the countermodel rather than repairing it away.

## 7. Finite/refinement arm

R052 should seriously investigate finite or discrete plane-like systems and refinement towers when mathematically natural.

A valid scheme may have formal systems

`P_0 -> P_1 -> P_2 -> ...`

and internally defined role objects `p_n^(i)`.

The primary questions are symbolic/structural:

- does the role stabilize or converge in an exactly defined sense?
- is the limit independent of refinement path/choices?
- do independently defined role sequences have the same limit?
- what axioms force or prevent this coherence?

Do not select a refinement scheme because its output approaches a known decimal expansion.

## 8. Classical identification is sealed until the end

Only after a role registry and theorem/counterexample ledger are frozen may R052 use a classical Euclidean plane as a comparison model.

The final identification stage may prove statements such as 'the frozen formal role corresponds to the standard symbolic Euclidean pi under interpretation I'. It may not:

- use decimal digits of classical pi to choose a role, refinement or axiom;
- revise earlier role definitions after seeing the classical identification;
- treat successful identification as proof that the classical definition was native.

Any post-identification repair is a new generation.

## 9. Isolation from engineering-success work

Before the R052 formal role/theorem freeze, do not consume:

- R046 engineering-success atlas/kernel/interface;
- R047 calibration target/results;
- R048 G2 candidate definitions or scores;
- R049 engineering holdout protocols;
- R050 calibration matrices/debts/Pareto observations;
- R051 quantitative-data targets or source-selection outcomes.

R052 is not an engineering calibration task and must not be optimized against those surfaces.

Project-level Foundational Logic and Gate V3 may be consumed only as semantic/type discipline.

## 10. Research posture

- Preserve multiple serious routes.
- Do not force a single winner early.
- Keep productive failures and countermodels.
- Separate theorem from bounded computational evidence.
- Exact finite computation is welcome when it proves/checks a declared finite claim.
- Numerical approximation to classical pi is not a research objective in the foundation stages.

Core slogan for this task:

> `TYPABILITY -> MULTIPLICITY -> COHERENCE -> IDENTIFICATION`, not `KNOWN PI -> RECONSTRUCT ITS DEFINITION`.
