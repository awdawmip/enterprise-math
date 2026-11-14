# EC49FOL reproduction / execution evidence

Scientific source (unchanged): original frozen 24-label, four-root signed-prefix input from EC49FOK PR #2393, commit \`ba72605fed95280371a262362997e5aceee2564c\`. Exact input SHA256 \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`. Original 84 edge file SHA256 \`db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41\`. Prior FOJ table in that parent evidence, \`FOJ_EDGE_FIRST_SEPARATION_84.csv\`.

## Executed C++17 exact census

\`\`\`bash
g++ -std=c++17 -O2 VERIFY_EC49FOL.cpp -o verify_fol
./verify_fol FIRST_NEUTRAL_EDGES_EC49FNS.txt FOJ_EDGE_FIRST_SEPARATION_84.csv EC49FOL_CANCELLATION_84.csv < master_and_radius3_cases.txt
g++ -std=c++17 -O3 VERIFY_EC49FOL.cpp -o verify_fol_O3
./verify_fol_O3 FIRST_NEUTRAL_EDGES_EC49FNS.txt FOJ_EDGE_FIRST_SEPARATION_84.csv EC49FOL_CANCELLATION_84_O3.csv < master_and_radius3_cases.txt
cmp EC49FOL_CANCELLATION_84.csv EC49FOL_CANCELLATION_84_O3.csv
\`\`\`

Observed author-side result (2026-11-14):

\`\`\`text
DOMAIN_CHANGE_EXACT_PASS 32315->32279 domain_A=648 domain_B=1944 first=156
DOMAIN_CHANGE_EXACT_PASS 32318->32279 domain_A=648 domain_B=1944 first=156
CANCEL_WITNESS 32318->32274 roots=-1:0:0:1 exact_cost=180
CANCEL_WITNESS 32318->32287 roots=-1:0:0:1 exact_cost=180
EC49FOL_EXACT_PASS stable_domains=82 all_budget_equal=32 differing=50 domain_changes=2 assignments=53136 changed_assignments=3795 canceled_components=4 edges_with_cancellation=2 edges_with_mixed_delta=5 cached_root_profiles=168
\`\`\`

The O2 and O3 result CSV files were byte identical. The CSV in this PR has 84 data rows. The implementation uses exact signed-prefix trie DP and integers, no floating-point.

## Independent Python exact reproduction

Download the original \`VERIFY_EC49FOK_INDEPENDENT.py\` from the immutable EC49FOK commit above into the same folder as \`VERIFY_EC49FOL_INDEPENDENT.py\`. Run:

\`\`\`bash
python VERIFY_EC49FOL_INDEPENDENT.py master_and_radius3_cases.txt
\`\`\`

Observed:

\`\`\`text
PY_INDEPENDENT_PASS 32318->32274 full_assignments=648 nonzero_component=244 exact_cancellations=2 first_sep=156
PY_INDEPENDENT_PASS 32318->32287 full_assignments=648 nonzero_component=244 exact_cancellations=2 first_sep=156
EC49FOL_INDEPENDENT_EXACT_PASS
\`\`\`

Independent Python also enumerated the exact two named assignments per edge with costs 180 and 182 and component delta (-1,0,0,+1). Python does not read any C++-produced costs or classification CSV.

Scope: frozen 51 configurations, exactly 84 original directed edges, 82 shared-domain edges with 648 complete assignments each, and 2 changed-domain exact graph comparisons. Research state NOT_REVIEWED. No formal CLAIM, Result or independent Driver review is implied.
