# Addendum: exact S23/AV auxiliary capacity plateau 412

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE / EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Frozen input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Original certified critical-cell program: research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py, Git blob 261d7e22da0e62d667009cb50acfe77ac4e35c3f.
Prior plateau 411: 23547581b85db6212d89f466dfb3f85b33e852c3 / ADDENDUM_411.md.
Scope: frozen two-point S23/AV label-(1,3,4) auxiliary observation; original first-entry lower-bound and exact critical-cell reduction remain the cited mathematical dependencies.

## New certified integer interval

Let r=ln(7)/ln(10/7), alpha=(2074774-380295r)/(79r-431),
a_i=floor(i alpha), V_i=380295i+79a_i, K_i=2074774i+431a_i.
The strict rational index-412 checker established

  a_411=240, V_411=156320205, K_411=852835554,
  a_412=241, V_412=156700579, K_412=854910759,
  H_412=V_412+510=156701089,
  M_412=K_412+V_412-V_411-1=855291132.

Combining the all-index first-entry lower-bound proof already cited in the preceding plateau notes with the finite exact coverage certificate yields:

  N(h)=855291132 for every integer 156320716 <= h <= 156701089.

This is 380374 consecutive integer horizons newly covered beyond plateau 411.

## Executed exact certificate

The current author-side run restored the original checker byte-for-byte, checked Git blob SHA 261d7e22da0e62d667009cb50acfe77ac4e35c3f, and executed check(412). It returned a non-None tuple containing:
  index=412; H=156701089; M=855291132;
  narrow_direction_types=126; beta_bound=413;
  exact_feasible_critical_cells=82252; distinct_witnesses_used=52.

The original code uses Fraction and an explicit 45-term rational atanh-series remainder bound. It checks narrow-direction rational inequalities, blocked integer-cell coverage, outgoing witnesses and the original lower-bound conditions. The run encountered no uncovered feasible critical cell. Reproduction wrapper: VERIFY_412.py; executable recorded output: RUN_412_CONCISE.txt. Run in an EM checkout with:

  python research_notes/brc_s23_av_linear_word_complexity_20261109_research1/VERIFY_412.py research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py

This endpoint result is independent of the new 79m symbolic-word-complexity theorem and does not claim phase-based witness transfer. The structural bridge between carry-word refinement and coverage geometry remains open.

## Next

Test index 413 with the same frozen checker. In parallel, study whether the 79 phase partitions derived from the exact carry-word coding can transport or share a critical-cell witness across adjacent candidate plateaux; a verified successful phase subclass is a useful independent theorem/algorithmic increment.
