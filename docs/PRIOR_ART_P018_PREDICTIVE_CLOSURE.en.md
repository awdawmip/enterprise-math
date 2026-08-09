# Prior Art Boundary — P018 Predictive and Contextual Closure

Status: `PRIOR-ART NOTE`  
Scope: future-observation equivalence, finite deterministic state distinguishability, algebra congruences, syntactic/contextual congruence, quotient algebras, congruence refinement, and minimal exact quotient states

## Established neighboring mathematics

Finite deterministic machines and the problem of distinguishing internal states from observable behavior have classical roots in Moore's sequential-machine framework. Nerode's automaton transformations and the later Myhill–Nerode tradition establish the use of behavioral congruences and minimal quotient automata. [SRC-MOORE-1956-SEQUENTIAL] [SRC-NERODE-1958-AUTOMATON]

The multi-ary generalization belongs to classical universal algebra. Standard congruences and quotient algebras are mature machinery; Burris and Sankappanavar provide a standard reference. [SRC-BURRIS-SANKAPPANAVAR-1981-UA]

More specifically, Słomiński studied the greatest congruence relation contained in an arbitrary equivalence relation. Clark, Davey, Freese, and Jackson formulate the same object as the syntactic congruence `Syn(theta)`, explicitly stating that it is the largest algebra congruence contained in `theta`, and develop term/context criteria for determining it. [SRC-SLOMINSKI-1974-GREATEST-CONGRUENCE] [SRC-CLARK-DAVEY-FREESE-JACKSON-2004-SYNTACTIC]

Accordingly, P018 does **not** claim as inventions:

- future-output / behavioral equivalence of deterministic states;
- partition refinement by observable futures;
- algebra congruences or quotient algebras;
- the criterion that a quotient operation is well-defined when the identifying equivalence is operation-compatible;
- one-hole term / polynomial contexts and elementary translations as congruence tests;
- the greatest congruence contained in an arbitrary equivalence relation;
- syntactic congruence or term-context indistinguishability;
- minimal equivalent finite-state realization in the automata-theoretic sense;
- the general principle that behaviorally or algebraically indistinguishable states may be quotiented.

## Enterprise Math-specific research interface

The project-specific question is narrower and remains `NOVELTY_UNVERIFIED`:

> given a finite-precision observation whose kernel is not closed under the operations that a precision state is supposed to support, can the exact greatest compatible refinement be expressed as a finite integer/state procedure, equipped with explicit finite stopping and information-size bounds, and integrated with P005 typed precision, P009 type-erasure warnings, P010/P011 irreversibility observables, and the P018 carry/defect calculus?

Supplement 18 treats the unary deterministic case as an adopted Moore/Nerode-style behavioral refinement. Supplement 19 adopts the universal-algebraic syntactic-congruence machinery for finite finitary operation signatures and studies only the finite-precision consequences and exact information accounting.

## Important boundary around carry

Universal algebra answers **which state distinctions must survive** for exact operation descent. It does not imply that every useful implementation or transport law must store the entire quotient-refinement label in the same form.

For radix quotient addition, P018 separately studies the exact remainder/carry representation. The claim that the full remainder is minimal per-state detail for arbitrary exact addition is derived from contextual distinguishability; the carry itself remains a derived interaction/transport term once operand detail is retained. This distinction prevents ordinary congruence theory from being mislabeled as a new cocycle theory and prevents the carry cocycle from being overgeneralized to every operation signature.

## Claim discipline

Even if the Enterprise Math integration proves useful or unusually compact, no claim of historical priority is made without a dedicated novelty review. Theorems proved from the project's definitions may be marked `PROVED`; their novelty remains separately `NOVELTY_UNVERIFIED`.
