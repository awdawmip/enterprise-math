# Prime-BRC Heyman Prior-Art Correction

Status: `L3 OWNER-LOCAL / PRIOR-ART CORRECTION`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`

## Correction

The owner-local note

`PRIME_BRC_FLOOR_PRIME_SET_ODD_JUMP_THEOREM_20260823.md`

must **not** be interpreted as establishing first priority for a proof of Heyman's three-prime conjecture.

A web prior-art audit on 2026-08-23 located the non-peer-reviewed 2023 preprint

**Amir Moattar Tehrani, “Heyman Conjecture: A Graph Theoretical Proof”**

(ResearchGate DOI `10.13140/RG.2.2.29953.02402`). The surfaced full-text claims a proof of the conjecture and states a broader theorem based on whether a prime factor crosses the square-root frontier.

Therefore freeze:

`HEYMAN_CONJECTURE_PROOF_PRIORITY = NOT_CLAIMED`.

`MOATTAR_2023_PREPRINT_IS_RELEVANT_PRIOR_ART = true`.

## What remains independently useful in Prime-BRC

The Prime-BRC work should be evaluated for the following stronger/different formulations, whose historical novelty remains separately unaudited:

1. the exact all-integer signed entry/exit identity
   `G(x)-G(x-1)=E(x)-L(x)`;
2. exact finite branch lifetime `a` for a branch entering at `ap` with `a<p`;
3. the arbitrary-observable signed jump theorem for `C_A(x)=|F(x) cap A|`;
4. the full floor-quotient birth theorem
   `F(n)\F(n-1)={d|n:d^2>=n}`;
5. the birth-tree/max-child/min-child interpretation and its BRC consequences.

These are not declared novel merely because the current search did not locate identical statements.

## Database mismatch warning

MathDB was still surfaced as listing Heyman's conjecture as open, but that database status cannot override directly found prior-art manuscripts. Database “open” labels are therefore insufficient novelty evidence.

Freeze:

`EXTERNAL_OPEN_DATABASE_STATUS != NOVELTY_OR_PRIORITY_CERTIFICATE`.
