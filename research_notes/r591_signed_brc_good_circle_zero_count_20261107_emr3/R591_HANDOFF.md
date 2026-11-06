# R591｜Research handoff

Frozen scientific input: R462 @18783e01e3646c72b7aab3b16d3f565e83e6446f. Previous frontier: R590 @88406fcfe23c2c23c2c27887b87613f8dcd6031a. P000/native signed twelve-branch semantics remain unchanged.

**New mathematics:** The auxiliary entire function F admits a good circle in every R<rho<2R (R>=1) with min_|z|=rho |F(z)| >= exp(-144 sqrt(R)). Proof: Jensen N_F(r)<=12 sqrt(r), genus-zero Hadamard product, radial log-average. For c=1/40000, R590 then yields an unconditionally selectable growing radius rho_k in (c log² k,2c log² k) where F_k and F have identical zero counts. Their common count goes to infinity and is O(log k).

**Exact check:** R591_VERIFY.py uses raw Catalan H_k and Fraction with strict tail bounds; eight exact finite Rouché certificates (k=8,16,32,64; r=1,2), output R591_EVIDENCE.txt.

**Status:** Independent mathematical Driver review pending. GitHub writer identity is not native research/owner/CLAIM authority; gateway status currently denied a backend version/identity match, operation_sent=false.

**Next:** Explicit algorithm for good radii; sharper effective c; positive-energy tail and original twelve-branch observation fidelity as separate problems.
