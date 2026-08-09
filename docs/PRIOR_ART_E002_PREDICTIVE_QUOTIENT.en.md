# Prior Art — E002 Predictive Quotient Compiler

Status: `ACTIVE PRIOR-ART NOTE`

## 1. Scope

E002 Stage 6 compiles a finite deterministic state system into the coarsest partition that preserves a declared observation language under future action words. The minimization idea is not historically new.

## 2. Sequential machines

Edward F. Moore's 1956 chapter develops deterministic finite sequential machines whose present state is determined by earlier state/input and whose output depends on state. It is direct prior art for behavioral state distinction through experiments and future input/output behavior. [SRC-MOORE-1956-SEQUENTIAL-MACHINES]

E002 adopts that finite behavioral viewpoint. It does not claim Moore machines, finite-state observability, or behavioral equivalence as Enterprise Math inventions.

## 3. Automaton minimization and partition refinement

Hopcroft's 1971 report studies minimization of finite automata and gives an efficient state-minimization algorithm based on refining state classes until behavior is separated. [SRC-HOPCROFT-1971-AUTOMATON-MINIMIZATION]

E002's generic compiler intentionally uses the established finite partition-refinement pattern rather than presenting a new minimization algorithm.

## 4. What E002 adds

The project-specific question is narrower:

- the fine states are explicit finite-resolution world states;
- actions are the declared future physical/control operations;
- observations are the declared future questions;
- finite horizon is itself part of the language;
- the resulting minimal finite-state quotient is interpreted as the precision state that may safely replace the finer world state for that declared future language;
- the compiler is used as a generic falsification oracle for the hand-derived E002 arithmetic formulas and the P023 future-compatible quotient program.

No claim is made that this interpretation establishes historical priority. Status remains `NOVELTY_UNVERIFIED`.
