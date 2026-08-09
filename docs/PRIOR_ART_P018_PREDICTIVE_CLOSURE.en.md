# Prior Art Boundary — P018 Predictive Dynamic Closure

Status: `PRIOR-ART NOTE`  
Scope: future-observation equivalence, finite deterministic state distinguishability, congruence refinement, and minimal dynamically closed quotients

## Established neighboring mathematics

Finite deterministic machines and the problem of distinguishing internal states from observable behavior have classical roots in Moore's sequential-machine framework. Nerode's automaton transformations and the later Myhill–Nerode tradition establish the use of behavioral congruences and minimal quotient automata. [SRC-MOORE-1956-SEQUENTIAL] [SRC-NERODE-1958-AUTOMATON]

Accordingly, P018 does **not** claim as inventions:

- future-output / behavioral equivalence of deterministic states;
- partition refinement by observable futures;
- congruence-compatible quotient dynamics;
- minimal equivalent finite-state realization in the automata-theoretic sense;
- the general principle that behaviorally indistinguishable states may be quotiented.

## Enterprise Math-specific research interface

The project-specific question is narrower and is currently `NOVELTY_UNVERIFIED`:

> given an explicit finite-precision observation whose kernel is not dynamically closed, can the coarsest exact dynamically closed refinement be derived as a finite integer/state construction and then integrated with the existing P005 typed precision lattice, P009 type-erasure warnings, P010 deterministic kernel irreversibility, P011 collision spectra, and P018 carry/defect calculus?

Supplement 18 treats the classical automata machinery as adopted prior art and studies only this exact interface.

## Claim discipline

Even if the Enterprise Math combination proves useful or unusually compact, no claim of historical priority is made without a dedicated novelty review. Theorems proved from the project's definitions may be marked `PROVED`; their novelty remains separately `NOVELTY_UNVERIFIED`.
