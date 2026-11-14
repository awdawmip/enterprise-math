# EC49FOK executable evidence and provenance

Frozen exact original input at scientific source pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab:
- master_and_radius3_cases.txt (SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e)
- FIRST_NEUTRAL_EDGES_EC49FNS.txt (SHA256 db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41)
- FOJ_EDGE_FIRST_SEPARATION_84.csv, immutable parent PR #2390 (blob 8f081749d47c318239bc37f4384a9794b1452cea).

Run the included C++17 program with the original input bytes and edge list:
g++ -std=c++17 -O2 VERIFY_EC49FOK.cpp -o verify_fok
./verify_fok FIRST_NEUTRAL_EDGES_EC49FNS.txt FOJ_EDGE_FIRST_SEPARATION_84.csv FOK_ROOT_PROJECTION_84.csv < master_and_radius3_cases.txt

The original local implementation was checked with C++17 -O2 and -O3; the complete output CSV was byte-identical. Exact asserted summary:
HIDDEN_PROFILE 32315->32308 full_root_mask_diffs=443 projected_diffs=0 projected_masks=168
HIDDEN_PROFILE 32315->32324 full_root_mask_diffs=10 projected_diffs=0 projected_masks=168
EC49FOK_EXACT_PASS stable_edges=82 projection_equal=32 projection_different=50 domain_change=2 hidden_profile_edges=2 projected_root_comparisons=13776 cached_root_profiles=168

Independent Python:
python VERIFY_EC49FOK_INDEPENDENT.py master_and_radius3_cases.txt
INDEPENDENT_PASS 32315->32308: full_root_dp_changes=443, projected_changes=0, projected_masks=168, complete_assignments=648, exact_cost_maps_equal=1
INDEPENDENT_PASS 32315->32324: full_root_dp_changes=10, projected_changes=0, projected_masks=168, complete_assignments=648, exact_cost_maps_equal=1
EC49FOK_INDEPENDENT_EXACT_PASS

The 84-row FOK_ROOT_PROJECTION_84.csv preserves the full observed per-root comparison counts. The local evidence package also includes immutable original inputs and logs. Local C++ run is the directly tested original implementation; GitHub reproduction should be executed against the published copy before using this as independent project mathematical review. Neither publication nor compilation alone admits a theorem.
