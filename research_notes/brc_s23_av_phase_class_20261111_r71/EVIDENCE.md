# R71 execution evidence and limits

Source model: auxiliary circle-source observer only. Native Enterprise Math X6/BRC execution was not attempted. Input pin carried unchanged: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Parent R70 commit: 1ca0973af8bdc9af1283c003265110d53aa8c85f.

Exact local commands executed with Python 3 and fractions.Fraction:
python check_r71.py
python check_r71_min.py
python check_r71_full_interval_cost.py
python check_r71_cost.py

Locally observed:
- R71_MIN_PASS 8_family_sizes 3_observers 3_arcs.
- Extended deterministic R71 assertions passed, including per-branch deletion and a stable-latest witness.
- 179 valid exact randomized models, seed 20261111; 11 complete grouped exclusions were certified, 6 of those failed a whole-subtree single-hull certificate. 39 exact critical-point/midpoint checks on certified complete sets; 51 certified groups included source wrap crossings. Additionally 75 query comparisons matched observer-rebased grouping and directly rebuilt grouping.
- Exact infinite-family construction checked N=1,2,4,8,16,64,256,1024 (up to 2048 source events) with two anchor phase groups and exact interval certificate.
- Independent full-interval comparison on favorable two-phase-class family: at 256 source events and 8 repeated queries, median of 3 local runs was 172.794 ms for R70-style per-source finite-event interval certification versus 0.857 ms for R71 index construction plus grouped interval certification. This comparison certifies the same all-real OUT conclusion for this family. Tree construction, update, cache reclamation, alternative distributions and formal bit complexity are NOT covered.

Extended local checks and raw JSON:
R71_VALIDATION.json, R71_FULL_INTERVAL_COST.json, R71_COST.json, check_r71.py, check_r71_full_interval_cost.py and check_r71_cost.py are in the same-turn local delivery bundle. The compact standalone check_r71_min.py is published in this GitHub research branch and verifies the main mathematical witnesses.

Reproducibility caveat: wall times vary across machines; count claims are tied to the specified scripts, input distributions, and exact arithmetic. Mathematical proof is the scope-specific argument in PROOF.md, not execution logs alone.

Project native identity: Researcher-ID EM-DIRECT-F6E9BD; Research-Activity-ID RA-21993D058A901C7791A9270D; session source canonical main commit 6ca3bf57e3e6319d2c2309154f37a4cf74c0f48d. No formal CLAIM/Result/Review admitted for this author-side continuation. No safety refusal or GitHub connection fallback occurred.
