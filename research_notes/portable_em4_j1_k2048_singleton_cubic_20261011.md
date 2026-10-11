# J1 k=2048: exact conditional cubic moments and observer information loss

Scientific status: AUTHOR_DRAFT / EXTERNAL FINITE-FIELD AUXILIARY / UNREVIEWED / NOT_ADMITTED. This is not a formal CLAIM, Result, independent Driver review, native P000 theorem, or a Task ownership transfer.

Sources read in this run: GLOBAL_KNOWLEDGE_V1 main@3e81097a0bb357ed68616ae590e22b4876992e66, Enterprise Math main@358b66d4931bba4d459162d393b68cbbf761e70e. P000 and ACTIVE residual-fidelity worldview retained.

## Frozen problem
For 1<=j<=2048 set D_j=(2j-1)^2+32768. The inherited 69 verified disjoint odd square-product relations cover U of 499 labels; T has 1549 labels. Among exact T character observations with precisely one positive index there are 1528 feasible singleton positions, each of natural prime density 2^-1546 (the finite set of primes dividing a D_j is excluded). Work with Y=4P, where P counts all positive Legendre symbols; reading Y as original J1 escape E uses the earlier nonexceptional E=4P identity, not re-proved here.

## New finite character theorem
The squarefree exponent row vectors are in F2^1656. The T span has rank 1546. Among U rows modulo T, 86 classes vanish and 413 labeled rows form 227 distinct nonzero residual classes r. Given a feasible T observer O, let d_r(O) be the signed sum of the character baselines of the U rows in quotient class r. Algebraic signs are character phases, not cancellation of positive branch mass. On the uniform 109-dimensional conditional character ensemble,

    Y - E[Y|O] = 2 sum_{r!=0} d_r(O) X_r

where X_r is the binary Walsh character. Consequently

    E[(Y-E[Y|O])^3 | O]
      = 48 sum_{r<s<t, r xor s xor t=0} d_r(O)d_s(O)d_t(O).

There are exactly 143 unordered (858 ordered) zero-XOR triples among the 227 distinct residual classes. This formula follows from E[X_r X_s X_t]=1 iff r xor s xor t=0. It preserves the full quotient-class correlations and does not assume independent U signs.

## New explicit witness
Exact feasible singleton T observers O_{488} and O_{1528} satisfy respectively

    O_488:  mean=954; variance=2684; third central moment=-21072
    O_1528: mean=954; variance=2684; third central moment=-18960.

The third moment differs by 2112 although the first two moments are identical. Thus compression to (mean,variance) is NOT sufficient for a future cubic-central-moment query; retained labeled residual relations carry indispensable information.

Exhausting all 1528 feasible singleton T observers, the third central moment takes exactly 39 different integer values, from -89136 to -11376, and is STRICTLY NEGATIVE in every case. Four distinct (mean,variance) signature classes have differing third moments. This is a finite statement for k=2048, not a general k-uniform result or P000 six-dimensional Cell transfer.

## Verification and evidence boundary
Local bundled evidence: em4_j1_k2048_third_moments_20261011.zip, SHA256 0e3a87671770645112ce70ec2c5be5054f328f82a39ebf55005ca43cd6eb9d1b. Contains PROOF.md, BASE_RELATIONS.json, RESULTS.json (full histogram), stdlib derive.py, independent SymPy/high-pivot audit_independent.py, AUDIT.json and SHA256 manifest. Both implementations refactor original 2048 D_j integers and recheck original 69 odd + 3 even square-product relations. Generator counts 143 unordered XOR triples; independent audit counts 858 ordered triples, matches full 1528-entry histogram, status PASS.

The native Enterprise Math MCP is read-only for the current connection (STATIC_READONLY_SCOPE_DENIED), and current J1 owner was not confirmed. Source note publication, if verified, records only an author draft, NOT formal execution, Result, Driver acceptance or full local evidence publication.

## Next exact unit
Compute fourth conditional centered moments using C_z=sum_r d_r d_{r xor z}, M4=16 sum_z C_z^2 (d_0=0), then test whether even (mean,variance,M3) suffices for downstream polynomial queries. In parallel seek certified weighted parity dual bounds for the unresolved singleton escape minima; do not promote a stronger unconditional minimum based on moments.
