# R557 — handoff for next researcher

Frozen scientific input: R462 at 18783e01e3646c72b7aab3b16d3f565e83e6446f; predecessor R556 at 0b2c352a6d4cd5fb766e9834885667faf1b6f8f2. Auxiliary signed BRC scalar Toeplitz–Hessenberg determinant, not a native-X6 theorem.

**Author-side exact increment:** k=16 positive/negative sign natural densities both equal 1/2, with finitely many zeros. Verification uses 31 exact rational Rouché disks, 465 distinct-pair checks, dominant modulus >24 versus all others <9, and 1804 candidate-order exclusions from the direct rational phase interval, without a full degree-930 resultant.

**Files:** R557_PROOF.zh-CN.md (full argument), R557_VERIFY.py (executed exact certificate), R557_EVIDENCE.txt (actual stdout). Command: python R557_VERIFY.py; requires Python3 and SymPy.

**Reusable tool:** For one specified ratio λ/μ of roots of rational degree-d Q, possible torsion order q must satisfy φ(q)≤d(d−1); rigorous rational root disks and arctan/π bounds can exclude each possible rational phase p/q. With a unique dominant nonreal pair and irrational phase, Weyl gives sign half-density; SML plus equidistribution gives *finite* zeros without global nondegeneracy.

**Next:** k=17, degree=33, full q_bound=2*(33*32)^2=2230272, isolate all roots and test exact angle; independently seek parameter-uniform dominant-modulus separation for all k≥5. Original P000/ACTIVE worldview and frozen R462 untouched.

**Control:** Researcher-ID EM-DIRECT-AC446E; Research-Activity-ID RA-9042A84415B33CA0AE179371. Formal Owner/CLAIM/Result/independent Driver acceptance not confirmed by this GitHub artifact.
