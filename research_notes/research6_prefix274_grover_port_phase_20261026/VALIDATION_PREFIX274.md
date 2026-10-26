# PREFIX-274 validation ledger

Frozen global main: a307e21a64150ced71df99120a1a14f0487946e9; EM scientific source: 1a7e2a95db1d16921e71ccb7968f836bda83d6ac; local Stage46 candidate note blob: eab89d5f8ff71127eb70492d8ee5f047c9b46ef7; P000 original global blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.

1. `python verify_prefix274.py` locally executed with the same rational signed labelled path-pair algorithm and returned checks PASS. Full d=1..8, 255 global-sign orbits. `RESULTS_PREFIX274.json` records exact class counts and a four-port label witness. Scope: semantic reimplementation of Stage46 candidate; not original Stage46 import.
2. `g++ -O2 -std=c++17 verify_prefix274.cpp -o verify_prefix274 && ./verify_prefix274` independently executed. Full d=1..12, 4095 sign orbits, all signed ordered (i,k) source pairs, integer scaled normalization and exact class counts; output returns INDEPENDENT_CPP_SIGNED_ORDERED_PAIR_BRC_PASS.
3. d=12 counts checked: 2048 input sign orbits; 1586 one-setting signatures; 463-orbit uniform fibre; 2048 two-setting signatures. Universal theorem has complete analytic proof; finite check does not substitute for proof.

Original Stage46 cumulative source executable module NOT imported here; no full native model_law_id, Cell/Port/field/time/triadic experiment or native admission. em_session_start=STATIC_READONLY_SCOPE_DENIED, operation_sent=false; em_control_tasks=CONTROL_QUOTA; active Owner/CLAIM unverified. No Drive backup used because GitHub author-side publication works and an authorization denial cannot be bypassed.
