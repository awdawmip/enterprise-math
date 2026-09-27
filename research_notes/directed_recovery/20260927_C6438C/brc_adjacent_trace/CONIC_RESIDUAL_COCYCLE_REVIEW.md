# Conic residual transport: symbolic review

Status: **PASS / PURE SYMBOLIC / SHARED CONTEXT / NO EXECUTION / NOT ADMITTED**.

Complete source reviewed: `CONIC_RESIDUAL_COCYCLE.md`, SHA-256 `2bda2beb4ef90fbc93078c1c52efe1b23872379cca3b53cdd1414a550cddd491`. Its geometric dependency remains `ADJACENT_TRACE_HBW_GEOMETRY.md` at `3b8083eb0ecddc1c12406cd64113ce3e2bb88ee676a0e7b8fd3f7c6289511e14`.

Both residual identities are correct integer-polynomial identities. Expanding F after D0 cancels the constant and vw terms, leaving `v^4-k*v^3*w+v^2*w^2+(k^2-4)*v^2`. The interchange symmetry gives the D1 identity. They require no membership hypothesis or division. Induction along the declared bit word then gives `F_t=F_0*J_t^2`, with the selected **pre-update** coordinate in each factor; no branch population or normalization enters.

The Jacobian matrices and determinants are also correct. Identifying the residual multiplier with half the determinant requires 2 to be a unit, as the note explicitly states. Even on the valid conic the bit maps are distinct from the original unimodular one-step companion map; the note does not conflate their operation languages.

Over a composite ring, only a unit selected coordinate supports backward inference of conic membership from the output. The family D0(0,w)=(-2,-k) is an exact symbolic witness that output membership alone need not certify input membership. A proper gcd of a selected coordinate is a valid paid factor certificate, while a zero residue gives a saturated gcd. This correctly distinguishes defect annihilation from a correctness certificate or a physical interpretation.

If F_0 is a unit, multiplication by it does not change the principal ideal, so the displayed terminal gcd equality with J_t squared follows at every prime-power depth. An accumulated J records all selected-coordinate hits, with repetitions and possible CRT saturation; it is not the terminal primitive return ideal and is not automatically a first-hit witness. The separate provenance, cost and observer obligations are preserved.

No defect was found. The proposed J register and runtime defect observer remain unimplemented and uncharged. This review requests no change to the already specified adjacent-trace program and no added fixture or scientific run. It used no scientific import, numerical oracle or external query.

Global-Knowledge-Sync: shared-author reuse of already read canonical context; no new independent handshake is claimed.
