#!/bin/sh
# Deterministic, local-only exact finite reproduction. Requires python3, g++ and unzip.
set -eu
cd "$(dirname "$0")"
if [ ! -e REFERENCE_PREFIX179/EM_PREFIX179_HANDOFF_20261022/audit_prefix179.py ]; then
  mkdir -p REFERENCE_PREFIX179
  unzip -q REFERENCE_PREFIX179.zip -d REFERENCE_PREFIX179
fi
if [ ! -e REFERENCE_PREFIX179/EM_PREFIX179_HANDOFF_20261022/reference_unpacked/EM_PREFIX178_HANDOFF_20261022/audit_prefix178_extended.py ]; then
  mkdir -p REFERENCE_PREFIX179/EM_PREFIX179_HANDOFF_20261022/reference_unpacked
  unzip -q REFERENCE_PREFIX179/EM_PREFIX179_HANDOFF_20261022/REFERENCE_PREFIX178.zip -d REFERENCE_PREFIX179/EM_PREFIX179_HANDOFF_20261022/reference_unpacked
fi
python3 generate_180.py
printf '%s\n' '7f302feb732c704e383d2aaf1df690ef62508364e75f6262612a4bd1222517ef  distance3_remove1264_180.bin' | sha256sum -c -
g++ -std=c++17 -O3 exact_180.cpp -o replay_exact180
g++ -std=c++17 -O3 independent_180.cpp -o replay_independent180
g++ -std=c++17 -O3 classify_uncoverable_180.cpp -o replay_classify180
g++ -std=c++17 -O3 exact_all_180.cpp -o replay_exact_all180
g++ -std=c++17 -O3 independent_k12_180.cpp -o replay_independent_k12_180
./replay_exact180 distance3_remove1264_180.bin 67525 11 200000 > replay_primary_180.log
./replay_independent180 distance3_remove1264_180.bin > replay_second_180.log
./replay_classify180 distance3_remove1264_180.bin > replay_classify_output_180.txt
python3 independent_support_obstruction_180.py > replay_independent_support_180.txt
./replay_exact_all180 eligible_no_support_obstruction_180.bin 646 12 200000 > replay_k12_180.log
./replay_independent_k12_180 eligible_no_support_obstruction_180.bin > replay_second_k12_180.log
cmp replay_primary_180.log primary_180.log
cmp replay_second_180.log second_180.log
cmp replay_classify_output_180.txt classify_output_180.txt
cmp replay_k12_180.log eligible_k12_results_180.log
cmp replay_second_k12_180.log independent_k12_180.log
python3 audit_prefix180.py
python3 audit_k12_180.py
python3 verify_witness_180.py
printf '%s\n' 'PREFIX180_LOCAL_FULL_REPLAY_PASS'
