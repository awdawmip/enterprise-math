# Stage283-B — Tied BRC port DAG: exact obstruction and convex-hull certificate

**Scientific deliverable:** portable author proof and exact Fraction replay. **Status:** UNREVIEWED / NOT_ADMITTED; formal native CLAIM, Source Result and independent Driver review are not claimed.

**Source pins:** GLOBAL_KNOWLEDGE_V1 main@4b3659222a1886c4643af5bdc6a867c745d65043; Enterprise Math canonical main@8168b9667b766ce95c681e67628de6af10fdec3b. Mathematical predecessor: Stage282-B in this Draft PR #1571, commit 6e8f1543ef98972c9ad19899613914d14da5817e.

## New exact theorem

A positive-source three-symbol DAG merges full ordered histories at coin x, then reuses the same source-blind policy port y at two successive decision vertices. Terminal law under both sources P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) is
(1−x, x(1−y), xy(1−y), xy²).

Putting z=xy, v=xy², **single fixed-port implementability** is exactly 0≤v≤z≤x≤1 and xv=z². The prefix-simplex relaxation drops the second equation. For observer F=1 on continue-Y1 / stop-Y2, the true maximal expectation is 1/4, versus LP's false value 1; the strict minimization gap for 1−E[F] is **3/4**.

The **exact convex hull** of feasible fixed-port triples is 0≤v≤z≤x≤1, z²≤xv. Necessity uses Cauchy–Schwarz; constructive sufficiency mixes y=0 and y=v/z at weights 1−z²/(xv), z²/(xv) when z>0. This cone is exact for affine terminal-observer optimization, not for implementation by one fixed y or for all future path-sensitive operations.

## Evidence to consume

- PROOF_STAGE283B_TIED_PORT_DAG.md — complete theorem, boundary cases, algebraic proofs, BRC provenance/observer scope, limits.
- REPRO_STAGE283B.py — exact source-tagged ordered-history DFS using only Python standard-library Fraction.
- REPRO_STAGE283B_EXECUTED_STDOUT.txt — captured output; final marker STAGE283B_TIED_PORT_DAG_EXACT_PASS.
- NEXT_TASK_PACKET_284B.md — two-route common-port convex-hull compatibility question, preserving open Stage278-A.

Actual execution checked 289 rational coin pairs × two strictly positive sources (12 ordered terminal paths/source) and 500 exact convex-hull witness constructions. A finite grid is **not** the proof of the continuous-domain theorem. All four text files have verified Git blob identity against the executed local originals. Run python3 REPRO_STAGE283B.py to reproduce stdout.

The native Site reports research_authority_granted=false and a CONTROL_QUOTA response to owner lookup, so native activity/claim/driver admission is pending. This external decision DAG is not a proved mapping into P000 X6 Cell dynamics; protected ACTIVE worldview remains unchanged.
