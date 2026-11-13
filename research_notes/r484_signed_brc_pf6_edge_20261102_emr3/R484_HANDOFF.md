# R484 portable research handoff — 2026-11-02

Frozen scientific input: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Subject: signed BRC auxiliary scalar H, right edge s=3, Toeplitz rank m=6. Continues R483; P000, ACTIVE worldview and native X6 unchanged.

Proved exact: for every integer k>=1, D6(2k+1,2k-2)>0 iff 1<=k<=5, and D6<0 for all k>=6. This is a signed BRC auxiliary PF6 obstruction, not native-X6 transfer. General lower-Hessenberg determinant recurrence also proved.

Sources: R484_PROOF.zh-CN.md (whole proof), R484_VERIFY.py (exact, executed Python standard-library checker), R484_EVIDENCE.json (captured output); command: python R484_VERIFY.py > R484_EVIDENCE.json. Exact evidence: 37 rational polynomial coefficients, 12 positive shifted coefficients, five low-boundary values, 560 raw coefficient comparisons, 28 direct integer determinants, 6 full 720-term crosschecks.

Status: AUTHOR_SIDE_EXACT_SYMBOLIC / DRIVER_UNREVIEWED / NOT_ADMITTED. Native session_start was denied STATIC_READONLY_SCOPE_DENIED; control_tasks/dispatch returned CONTROL_QUOTA; owner, CLAIM, Result and Driver acceptance unconfirmed. GitHub author's identity is awdawmip; GitHub publication is source persistence, not native claim.

Next independent problem: m=7 at the same s=3 using the same p_t and recurrence, find the exact first negative k and a universal certificate; alternative: s>=65 Newton certificates for m=4.
