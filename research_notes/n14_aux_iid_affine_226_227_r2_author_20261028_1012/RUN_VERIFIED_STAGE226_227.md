Observed actual local execution, 2026-10-28 Asia/Shanghai.
VERIFY_STAGE226.py => STAGE226_EXACT_PASS 22636 (corner visits 6079,6079,5239,5239); next K227=45953726534712/538227241171.
VERIFY_STAGE227.py => STAGE227_EXACT_PASS 20128 (corner visits 5239,5239,4825,4825); next K228=22177458672696/263038955731.
Independently coded REPRO_STAGE226_227.py => STAGE226_COMBINED_REPRO_PASS 22636 ; STAGE227_COMBINED_REPRO_PASS 20128 ; STAGE228_DUAL_ONLY_PASS 22177458672696/263038955731.
Both algorithms use exact rational arithmetic and full unordered-state enumeration for Bellman, plus unmerged full ordered-path integer-mass DFS for each primal corner. Each stage: 680 states, 1238 positive action gaps. Mixed coefficient exactly zero, and exact equal-error/time-dominance identities checked. Two code implementations do not equal independent researcher review.
Source global main 2bccd0522d7ed724311b3ed1c85842b95cdeba8d; EM main 65a18bbfac5e5f304f12ca62f4c5529f29a1675f; P000 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
Native author permissions research_authority_granted=false; owner control_tasks CONTROL_QUOTA, no native Source writes.
