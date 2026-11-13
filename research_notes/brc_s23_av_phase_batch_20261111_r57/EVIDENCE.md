# R57 exact validation record (2026-11-11)

Frozen input ref: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. All computations in `VERIFY_R57.py` and `CHECK_R57.py` are integer-only rational arithmetic, independent event replay vs direct endpoint classification.

Full local run: `PASS_R57_GROUPED 1440 39295`. Compact independent run: `PASS_R57 1440 39295 frozen_cases 14 half_events 14418 full_events 28800`.
Small tests: 1,440 cases, m=1..12, H=1..15, 8 deterministic coprime p/1009 values per pair, 39,295 individually replayed events; all grouped and direct classifications agree.
Frozen S23: m=128,H=225,K=352, p_low=262204504569236716045286, p_high=262204504569236716045287, D=10^24.
Both endpoints: k in {1,4,32,88,176,264,352}; upper Farey bracket (43/164, 59/225). Identical cut ordering across endpoints.
k=176: 14,418 individually replayed events, 352 delta-endpoint additions + 225 prefix steps, all 225 source labels changed, all 128 youngest-age entries changed. Resulting youngest vector sha256 (JSON with Python default spaces): `f06d174e361bd5ecd1c8834e4c26ad0f59c59d388b9e5dd682c6350ef2993831`.
k=352: 28,800 individually replayed events, 704 delta-endpoint additions + 225 prefix steps, zero source-label/youngest-age differences between initial and final states; endpoint youngest vector sha256 `bd064540337953bf133aff1bdb81824c50aa7d725a251e32e4b2828ec73a7333`.
Source timestamps ±10^18 and 10^12+128 were independently rephased at both endpoints with exact modular arithmetic. This tests equality of the two coordinate descriptions, not universal stability at distant j under the parameter enclosure.
Full local evidence: `/mnt/data/em_r57/R57_CERTIFICATE.json`, `/mnt/data/em_r57/VERIFY_R57.py`, `/mnt/data/em_r57/RUN_LOG.txt` retained in run bundle. Scientific status: author proof/finite exact checks, independent review pending. Final source package not yet admitted to canonical results.
