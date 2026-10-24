# Research3 / BRC strict K3 predecessor witness — handoff

Date: 2026-10-24. Status: AUTHOR_SIDE_UNREVIEWED / EXACT_BIGINT_VERIFIED / NATIVE_OWNER_UNVERIFIED / NOT_ADMITTED.

## Source pins
- GLOBAL_KNOWLEDGE_V1 main cfd9080253a6fcc9baa0cd15c7ff0f7472e209c3; P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE world semantics unchanged.
- EM chosen current Source main 356b3997d463f5ed56c2f8a62323ada071a4b925; portable protocol blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c.
- Prior author-side theorem fe33e3fbc100587f0e6bd0a1b43eb851928d854a established K_infinity=S for general finite positive BRC and asked for K3 witness.

## New exact result
V=0,1,2,3; good edges 01,02,03,23; q_alpha=(1,22,2,3)/28; q_beta=(1,22,2,4)/29. Strictly different positive kernels.
K0={n>=5}; K1={n>=4}; K2={n>=3}; K3=S={n>=2}. Real alpha-alpha history (2,0) is in K3 but not K2; every future action under arbitrary alpha/beta alternation strictly decreases good-pair occupancy.
All early delta signs exact; K0 n<=4 excluded by single-vertex cut; all n=5 states have explicit strictly feasible cross-action spectral flow, with hereditary extension to infinity.

## Evidence
- STRICT_K3_PREDECESSOR_AUTHOR_PROOF.zh-CN.md: full analytic proof.
- verify_k3_predecessor.js: the exact JS BigInt function executed to obtain evidence.
- EXACT_EVIDENCE.json: full signed integer table, K0 cut deficits, strict flow margins, independent support-mask DP counts.
- Actual independent Python 16-mask DP local reproduction: 510 word probabilities and 60 increment comparisons.

## Unfinished and authority
GitHub actor awdawmip confirmed. Native em_control_tasks: CONTROL_QUOTA; em_session_start: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No Source Researcher session/activity, live Owner, CLAIM, frozen Result, or independent review; author-side branch storage is not formal publication/admission. Never transfer this theorem into P000 X6 without a faithful embedding and observer map.

## Next scientific question
Find strict K4\K3 witness with two different positive kernels, or prove sharp depth bound for this four-label four-edge graph under a specified parameter family. Retain exact lower-layer flow-cut obstructions, early delta signs and terminal strict flows.
