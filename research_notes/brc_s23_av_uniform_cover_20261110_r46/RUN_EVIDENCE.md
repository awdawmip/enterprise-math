# R46 exact execution evidence — 2026-11-10

Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor R45: `bae0abd5cb05f129ea91d1624126aa67af22b1b0`.

Current real Researcher-ID `EM-DIRECT-596A9C`, Research-Activity-ID `RA-68871F158B77BAF243835382`, native registration verified on Source main at commit `9a38563fe547a5a78868aa66661522913b91b26f`. This is independent author-side research, not a shared CLAIM or independent mathematical review.

Full local exact executed program (Python stdlib, integer and Fraction arithmetic):
```text
python VERIFY_R46.py
PASS_R46_PINNED_78_STAGE_UNIFORM_SUFFIX_COMPILER
stage_count=78
last_source_labels_checked_at_both_endpoints=9984
positive_updates=9697
run_count=298
final_affine=[-4017401528447,15321634290944]
R46/R32 frozen TSV SHA256: 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6

python VERIFY_R46_COMPACT.py
PASS_R46_389_SUFFIX_298_RUNS 298 updates 9697

python VERIFY_R46_STABILITY.py
PASS_R46_FULL_ENCLOSURE_NO_SOURCE_BOUNDARY_CROSSINGS 2502656 unique_sources 19553 min_numerator_clearance 1538749354821431426904

python VERIFY_R46_BOUNDARY.py
PASS_R46_77_BOUNDARY_RISK_IDENTITIES 51 post-million boundaries
SELECTED_DISTANT_BOUNDARY s=1106743 new_large_kind=u next_long_source_count=630382 missing_owner_count=0 risk_coefficients=(15987713,-60974208)
```

The standalone published `VERIFY_R46_COMPACT.py` reproduces the exact 298-run digest without any input from R32. Full author-side bundle includes the extended executed program, the certified strict-order checker, cross-stage checker, exact 78-stage certificate, generated TSV, and R32's immutable table solely as an independent regression oracle.

Research bundle ZIP validated with Python zipfile.testzip()==None, 10 members, 23,787 bytes, SHA-256: `f1e9ed8555ee72891728a2ee553142202e35b111eac3268b308431b5135066a5`. The ZIP is attached to the current conversation; it is not claimed to be uploaded to GitHub. Formal activity checkpoint and independent review remain pending; current S23 shared owner has not yet been verified.
