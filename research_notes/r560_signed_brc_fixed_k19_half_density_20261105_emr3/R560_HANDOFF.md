# R560 Handoff｜冻结 signed BRC 标量支线

- Frozen scientific input: R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f；prior immutable frontier R559 @ 7ad50eb20beae927804fd24dde702c2ae7f12665。
- Scoped object: k=19, r=39, 37th-degree characteristic polynomial of frozen signed BRC auxiliary Toeplitz–Hessenberg scalar determinant. Not native heartbeat X6, not a P000/ACTIVE update.
- Author-side mathematical claim: signs ± both have natural density 1/2; only finitely many zero indices.
- Reproduction: python R560_VERIFY.py. Python3 + SymPy. Numerical root finding proposes centers; all acceptance inequalities are exact rational/integer checks.
- Coverage: 38 original coefficient identities; 37 rational disks of radius 1e−22, 666 disjoint pairs; exhaustive 2606 eligible torsion denominators q≤3,548,448 with φ(q)≤1332; 1025 exact recurrence values; raw Berkowitz determinants m=1,…,12.
- Evidence: R560_EVIDENCE.txt actual stdout, R560_PROOF.zh-CN.md complete scoped reasoning, R560_VERIFY.py byte-identical to executed local file (blob cf900884c8651bc31bbec0ff28406984c1f3d8ab).
- Review status: author-side exact certificate PASS; formal CLAIM/Result/independent Driver admission not asserted.
- Next action: independent archived-script replication and independent proof inspection; mathematical continuation k=20 or a uniform k≥5 leading-pair isolation lemma. Keep native RS-X6 task and its source firewall separate.
