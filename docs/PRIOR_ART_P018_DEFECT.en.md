# P018 Defect / Carry Prior-Art Appendix

Status: `PRIOR-ART APPENDIX`  
Scope: carry cocycles, section defects, and the boundary between established extension theory and P018-specific precision transport

## Carry and cohomology

Daniel C. Isaksen's 2002 paper *A Cohomological Viewpoint on Elementary School Arithmetic* develops a cohomological viewpoint on elementary arithmetic and explicitly places carrying in cocycle/group-extension language. [SRC-ISAKSEN-2002-CARRY]

Enterprise Math therefore does **not** claim as inventions:

- the observation that carrying can be encoded by a cocycle;
- the interpretation of carry through a group extension;
- the fact that changing a section changes the local cocycle by a coboundary-type correction;
- standard nonsplitting/section-obstruction language.

## Project-specific use under test

P018 uses that established algebraic language only as one layer in a larger finite-precision problem. The project-specific questions are whether:

1. an operation/projection noncommutation can be retained as an exact finite defect rather than an error term;
2. representation-dependent local defects can be separated from defects that survive legitimate chart changes;
3. canonical precision-only paths are flat after exact chart transport;
4. genuinely path-dependent operation schedules such as collapse-then-project versus project-then-collapse admit a finite, composable defect transport law;
5. those transported defects can contribute to reusable proof certificates in P017 and other finite-state problems.

The current candidate integration remains `NOVELTY_UNVERIFIED`. Its value is judged by new theorem leverage and cross-problem reuse, not by the vocabulary "cocycle", "holonomy", or "atlas".
