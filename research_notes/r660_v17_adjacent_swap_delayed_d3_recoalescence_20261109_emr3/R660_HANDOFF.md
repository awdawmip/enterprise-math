# R660 researcher handoff — adjacent swap, delayed D3 recoalescence

Date: 2026-11-09 Asia/Shanghai. TASK RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW; publication TP2-47D65B35A7D48082EFBB. Researcher EM-X6-D9BFC8 / RA-7E34CF3D279F24C511D2E91E, registered by native service. Owner at 2026-11-09 11:22:41 +0800: READY/NEEDS_DISPATCH, taskbook/unassigned. No formal CLAIM; all mathematics author-side, independent Driver unreviewed.

Frozen science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f and V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d. Predecessor R659@9052cfa0f025719ea1e531fa81bd775e739308a1. Full proof R660_PROOF.zh-CN.md; exact Python verifier R660_VERIFY.py; output R660_EVIDENCE.json.

New theorem: an adjacent event swap e,f can create transiently different V27 triads; after a later common event produces ledger+triad recoalescence, the non-Abelian relative labelled-slot permutation Delta=slot_B * slot_A^-1 is retained under every subsequent common strict valid event word.

Strict three-event witness: x PASS seed (2,0,0,0); y PASS (3,3,3,3); e2=(2,2), e3=(3,3), e0=(0,0). A=(e2,e3,e0), B=(e3,e2,e0). Both end triads x=345,y=012; signed and full ledgers, pair histograms equal. x slots (0,2,1) vs (1,0,2), both odd; relative Delta=(1,2,0), y identical. Strict gaps x=(1,1,1),y=(3,1,9). Triads differ after second event and agree after third.

Finite exhaustive domain: 256 x PASS seeds (0..3)^4, fixed y=(3,3,3,3), diagonal TRANSFER four-letter alphabet, all ordered event words of lengths 0..3. Total words [256,1024,4096,16384]; all-strict [256,560,1634,5501]; unordered same-ledger/triads/parity different-full-slot word-pairs [0,0,0,21]. Thus length 3 is minimum in this *bounded domain*.

Next: inspect genuine V28 permission and V30 time semantics, determine whether the witness events are native permitted and how D3 defects couple under three or more Cells; calculate rotation-covariant cycle memory and smallest complete network state. No P000 change, Result, independent review or canonical theorem admission.