# R92: parity-separated cubic ports, hidden quartic residual

2026-10-17. Author-side unreviewed research note; not a formal Enterprise Math Result or Driver acceptance.

Frozen research inputs: GLOBAL_KNOWLEDGE_V1 main@2e5c01ba0a33cc2239eef80c1cc8ff48904b3f38; Enterprise Math main@5e0fa4bc221de057bdef6fb03e027f6d9cebd67a; P000 ACTIVE_LOCKED. All paths use six native spatial axes, with support on axes 1,2,3 only.

Define A=(1,2,3,-1,-2,-3), B=(1,-2,3,-1,2,-3), W1=A+B, W2=B+A. Both 12-step CYCL paths have the same signed occupancies, boundary, net displacement, complete area, and positive-rational BRC path mass. For a fixed rational reference choice, mass is 64/11025.

For every axis word u of length at most 3, both the positive and negative counts of increasing subsequences with axis word u (sign parity of selected steps) are equal for W1 and W2, even without imposing Xi^2=0. Yet in the ordered square-zero path algebra, the degree-four coefficient difference at X1X2X1X3 is +2.

Proof: A and B have identical unsigned axis order, hence the unsigned generating product is identical under concatenation AB and BA. Their signed first-order signatures vanish; their signed commutator begins in degree 4 and equals [T2(A),T2(B)] there.

Exhaustive C++17 integer enumeration of all net-zero nonbacktracking native CYCL words of lengths 2,4,6,8,10 (canonical axis names only) checked 4,950,414 signed permutations and 1,325,428 valid paths. It found 16 same-port duplicates, none with a quartic difference. Consequently the witness length 12 is shortest within this specified parity-port, boundary, occupancy, CYCL and quartic-observer protocol. Hash grouping was followed by exact integer signature comparisons.

Local evidence includes PROOF_R92.md, verify_r92.py, exhaust_10.cpp, exhaustive10.txt, R92_CERTIFICATE.json, and BRC frozen reference modules; coldstart verified. R92 is not a statement that fully labeled source identities or physical sensors lose the same information.

Control: owner/dispatch queries returned CONTROL_QUOTA; native session start denied STATIC_READONLY_SCOPE_DENIED. Formal CLAIM, Result, Driver review pending.

Next: refine the observer to fully signed 12-direction-labeled subsequence counts and establish whether quartic ambiguity survives.
