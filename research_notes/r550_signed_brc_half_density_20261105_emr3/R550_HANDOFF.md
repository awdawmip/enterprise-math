# R550 research handoff | 2026-11-05 Asia/Shanghai

Scientific pin R462 18783e01e3646c72b7aab3b16d3f565e83e6446f. Direct predecessor R549 bf6f1d4b7c766108664491eb223cb0d9cbca67dc.
Researcher EM-DIRECT-90D5E6; activity RA-101E034ABA9A9B44EFB0F1B9. Only public session ID MCP-fe27e320eec24dc296ec8eb90e98a213; no session credential.

**Result:** Exact cyclotomic resultant certificate excludes every root-of-unity ratio of distinct characteristic roots for k=5,6,7. Together with already stored R543--R545 dominant-pair certificates, the natural densities of strictly positive and negative Toeplitz-Hessenberg determinant orders are both exactly 1/2.

**Reproduce:** In this directory run python3 R550_VERIFY.py using Python 3.10+ and SymPy. Expect R550_EXACT_HALF_DENSITY_CERT_PASS. The script performs 662 exact polynomial gcd checks, 36 direct H checks and 21 Berkowitz matrix determinant checks. Math and domain in R550_PROOF.zh-CN.md.

**Scope:** Author-side exact computer-assisted proof; R543--R545's prior Rouché certificates are used by precise statement, independent Driver review open. No CLAIM/Result or native X6 promotion. P000/ACTIVE worldview and scientific pin unchanged.

**Next:** Construct a more efficient elimination certificate for k=8 (direct SymPy resultant exceeded 200s this run); follow with k=9,10. Retain parallel m=63 sign-classification route.
