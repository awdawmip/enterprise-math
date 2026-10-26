# Local exact verification 2026-10-26

Executed Python 3 standard library fractions.Fraction on the separately retained author program and VERIFY_PORTABLE.py. The program written as VERIFY_PORTABLE.py in this commit is the exact intended portable source.

POSITIVE LR-MINIMAL NONLUMPABLE MODEL: PASS
1728 full deterministic tables, 85 distinct observer vectors: PASS
72 LR deterministic tables, 12 distinct observer vectors: PASS
7 exact 3D convex-hull facets, all 85 vectors contained: PASS
625 signed real-linear integer-coefficient cross-checks: PASS
Witness O=(1/16,7/8,3/2,3/2), nonzero Q defect=(-1/48,1/24,-1/48): PASS
Universal quantifier requires accompanying analytical support and convexity proof.

7 facets on x=(48eP,48eQ,48t), given as n dot x>=c:
(-96,-96,7,-4608)
(-2,-3,0,-144)
(-2,-1,0,-96)
(0,0,-1,-96)
(2,1,0,48)
(2,3,0,96)
(96,96,7,4608)

Computational coverage: complete finite deterministic tables under specified two-step tree; not a formal proof checker, native computation or independent Driver review. Real-coefficient universal scope is justified by exact analytic theorem in PROOF_LR_ROOT_MASKING_N2.md, not sampling 625 quadruples. No online runner/remote execution claimed.
