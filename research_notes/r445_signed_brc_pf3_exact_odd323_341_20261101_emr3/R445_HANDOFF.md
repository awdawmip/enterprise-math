# R445 portable continuation / research handoff

Mother question: signed BRC auxiliary scalar Toeplitz maximal PF order for odd r, continuing R441's Schur/LR reduction and R444's exact-integer frontier through r=321.

Completed scientific unit: r=323,325,...,341 (10 rows), complete PF3 via 61,597,775 exact integer minors; PF4 negated for each by an independently computed 4×4 negative witness. Full coefficient input, all witnesses, four raw execution logs, and SHA256 evidence JSON are in this directory. Source files are byte-identical to independently executed source files from R443/R444, not unexecuted example code.

Reproduce in Python 3 and C++17 with Boost multiprecision (no special service required):

\`\`\`bash
g++ -O3 -std=c++17 R444_PF3_INTEGER.cpp -o pf3_check
python R443_GENERATE.py 323 341
# This writes R443_INPUTS.txt; its 10 lines represent r=323,325,...,341.
sed -n '1,3p' R443_INPUTS.txt > R445_INPUTS_323_327.txt
sed -n '4,6p' R443_INPUTS.txt > R445_INPUTS_329_333.txt
sed -n '7,9p' R443_INPUTS.txt > R445_INPUTS_335_339.txt
sed -n '10p' R443_INPUTS.txt > R445_INPUTS_341.txt
./pf3_check R445_INPUTS_323_327.txt
./pf3_check R445_INPUTS_329_333.txt
./pf3_check R445_INPUTS_335_339.txt
./pf3_check R445_INPUTS_341.txt
python R443_PF4_WITNESS.py
python R444_SPOTCHECK.py
\`\`\`

Expected: 10 rows, 3,310 one-minors, 549,625 two-minors, 61,044,840 three-minors, all strictly positive, each batch returns \`R444_PF3_EXACT_PASS\` with exit 0. Witness script verifies ten original-convolution inputs and 24-term exact integer negative four-minors; spotcheck verifies 1,250 sampled three-minors. Full digests and witnesses are in R445_EVIDENCE_FULL.json.

Source originals: R443 commit \`81f4e314fa9dae6fbde8e0182ff1df4526b8025f\` and R444 commit \`f83969b040d3ab5c005fe1511fb6ff8891a84eed\`. The four source Git blobs are 50411ae1e5ca1bcbce4ca8f66dc2bfe17c487ee5, b72a869c630f8a6ae8f86a220d698ea9d9a4d18e, 7439b96588b9a5d6188e850df149a693ad1c7d62, 6b92ab684387694d813d4a75b212825a16a267f3.

Status: AUTHOR_SIDE_EXACT_INTEGER_EXHAUSTION; REGISTER_PENDING; DRIVER_UNREVIEWED; NOT_ADMITTED. No formal Source owner/claim established because native authority=false and owner lookup was quota-blocked. P000 and ACTIVE worldview unchanged. Proof concerns the signed auxiliary scalar only; native six-dimensional X6 observer bridge remains unproved.

Next science unit: establish a uniform analytic PF3 certificate for all odd r≥99, or test exact r=343 onward for the earliest negative three-minor. Preserve signed provenance and observer scope; do not re-run completed r=323..341 merely to move the frontier.

