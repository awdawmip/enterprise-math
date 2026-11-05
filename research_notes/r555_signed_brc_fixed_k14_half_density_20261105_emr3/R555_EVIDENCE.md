# R555 精确执行证据与复现

2026-11-05, Python3/SymPy 1.14 equivalent local executions (code path in source derived from R554; original local runner used mathematically identical routines).

- Rational Rouché: 27 circles, 351 strict disjointness inequalities, max rhs/lhs approximately 0.004860425288765455 < 3/500, unique dominant non-real conjugates modulus>18; others <7.
- Exact recurrence m=0..1024: plus=515,minus=510,zero=0,sign_changes=304.
- Root-ratio E degree729 and R degree702, R(1) nonzero modulo 65537, two out-of-grid independent SymPy resultant checks passed.
- Candidate sieve q<=985608: 1356 valid q, maximum2940, complete phi(q)<=702.
- Cyclotomic checks partitions: [0,800) PASS; [800,1000) PASS; [1000,1150) PASS; [1150,1356) PASS. All use the same R: SHA256 c84af0f4ea7c4cb3f40087cac608edbeb118893d1def03dbffe79e53e57824bc. Total verified: 1356/1356.
- Original H independent convolution and 16 Berkowitz determinants: PASS (m=1..16); 28 t=2..29 H identities.
- Repro: in this directory `python R555_VERIFY.py && python R555_MODULAR.py && python R555_INDEPENDENT.py`; full modular check may run longer than isolated chunks. The published modular file is mechanically adapted from R554, and local equivalent implementation used bounded chunks; exact published bytes remain to be rerun independently.
- Frozen science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; upstream R554@4bd18834e62eec2067db351c5794a9b58e79b8e3. This is author-side proof evidence, not native Driver review.
