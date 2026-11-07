# R446 portable handoff
Parent: signed BRC PF3 frontier, R445 (odd 323..341) author-side checked. R446 is a DIFFERENT infinite-parameter *bounded-window* theorem; do not re-label this as global PF3.

Author-side output: R446_PROOF.zh-CN.md and R446_VERIFY.py, with original R446_RUN_OUTPUT.txt. Execute "python R446_VERIFY.py" (SymPy exact arithmetic); the script generates complete R446_CERTIFICATES.json (72,772 UTF-8 bytes; SHA256 4fb62ae4d2bf6b6945fda0d61d9619bb2c4a58604b811887830e6cd20e994550). This certifies (L=6,r>=9) 63 positive Schur minors and (L=8,r>=99) 129 minors; analytic fixed-edge limit covers every fixed column set. Finite width does NOT certify unbounded Toeplitz PF3.

Next actionable mathematical unit: derive uniform estimates as j/r grows (bulk/edge transition), or find a parameterized 3x3 negative witness if it exists. Maintain raw signed branch cancellation and native-X6 transfer as separate open obligation. Reuse R441-A Schur/LR and R445 coefficient input contract.

Source pins GKV1 main@e1e9409728a16a133670c599579b488a6aa5796f and EM main@1fde72896593e8b10c9abb356983a265d2a4600f. Original signed model: R445 commit d5519896d2b7f65f0dbe83dc1bea80265e8421b3; Schur/LR R441 commit 8fba98f1654ef4050ccc562be1ec197c01f31a47.

Status: AUTHOR_SIDE_ANALYTIC_PLUS_EXACT_SYMBOLIC / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Native authority_granted=false; owner read CONTROL_QUOTA. No CLAIM/Result or independent review. P000/ACTIVE worldview unchanged. Commit only to the existing Draft PR #1708, do not merge or mark Ready on the author's own authority.
