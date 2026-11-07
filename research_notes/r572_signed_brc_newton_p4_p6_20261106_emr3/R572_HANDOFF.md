# R572 research continuation · 2026-11-06
- Frozen source: signed BRC R462@18783e01e3646c72b7aab3b16d3f565e83e6446f, R570@106520099fb0e554080f6a4b46b482ebe7c7040d, R571@37b6cd3bdd09d84ebb89af6a62a8bcb207d350e2.
- New exact author-side lemmas: p4=−(k+2)P4(k)/218295000<0 for each integer k≥5; p6=(k+2)P6(k)/8939180250000>0 for each integer k≥2.
- Therefore at least one complex-conjugate root pair with cos(4 arg λ)<0 exists for every k≥5. For all k≥2, ρ_k^6≥p6/(2k−1), giving liminf ρ_k/k^(11/6)≥(7491584/17878360500000)^(1/6).
- Artifact: R572_PROOF.zh-CN.md (full mathematical proof and positivity certificates), R572_VERIFY.py (exact symbolic plus int/Fraction checks), R572_EVIDENCE.txt (actual stdout, 999 k inputs). Status AUTHOR_SIDE_EXACT_SYMBOLIC; Driver review pending.
- Next scientific question: derive p8 and compare signs and root-radius bound; distinguish fixed-order p_{2m} from uniform m→∞ to avoid an invalid interchange. Keep X6 native task owner/CLAIM separate; author-side auxiliary scalar work makes no CLAIM.
