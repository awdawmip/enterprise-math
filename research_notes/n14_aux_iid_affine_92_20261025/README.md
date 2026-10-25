# N14 auxiliary iid — Stage92 exact affine result (2026-10-25)

**Scope:** author-side exact rational proof for finite iid N=14 sequential testing, not native P000, X6, Heartbeat, an independent Driver review, or a formal task result.

Read PROOF.en.md for complete mathematics. The published scripts derive92.py and crosscheck92.py were actually run locally with Python standard-library fractions.Fraction; their verified immutable Git blobs exactly match the locally executed bytes: a18f86e6e327f4004d952ac663ff1a88a49ad6f2 and 0520e42075d97a5ec63f0e50cc694fe93a1f6e9d. They import the unchanged predecessor derive91.py, which in turn imports derive90.py -> derive89.py -> derive88.py. The immutable predecessor proof/source is at awdawmip/enterprise-math@966d52251166b4d17ea861ea4374639669abbee9/research_notes/n14_aux_iid_affine_91_20261025/.

Reproduce with the predecessor Python files in the same directory:

~~~sh
python derive92.py > derived92.json
python crosscheck92.py > crosscheck92.json
~~~

Computed exact theorem:
- eta92 = 104725/103474317735493632
- Gamma92 = 1062252/295
- alpha92 = 5172457130453937143/14900301753911083008
- V92 = 24277747388885024249/1862537719238885376
- new action tie A92=(12,8,3), C~P, in addition to B=(12,0,1), C~Q.
- 680 states, 1240 alternatives, 1238 strict positive gaps, 0 negative gaps, 2 ties.
- 852 genuine A92 first-hit ordered prefixes, 5 old suffixes, 4260 truncated full histories.

certificate92.json contains the detailed rational audit; NEXT_TASK_PACKET_93.md is the next candidate (not a proof). Tests share the inherited deterministic stopping table and therefore do not establish an independent audit. Full interval follows mathematically from the exact disjointness/affinity argument in PROOF.en.md rather than numerical grid tests.

Input GLOBAL_KNOWLEDGE_V1 main 50e22254dac1b15435eed58a6ad87a3e9b8627f0; pinned project read 0c20646ad4d9fa5345dcdbc28c35fdf52a2bc5d7. Native control/owner unverified, no CLAIM or freeze.
