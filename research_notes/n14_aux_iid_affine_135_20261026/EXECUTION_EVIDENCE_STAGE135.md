# Stage135 actual execution evidence (2026-10-26)

This is author-side locally executed verification, not independent Research Driver review or GitHub-hosted code execution. Both programs were written as different algorithms.

* `python CHECKER_STAGE135.py` -> local `checker_run.json`: PASS, complete 680-state rational Bellman minimization, two ties, 1238 strictly positive alternatives, exact affine observer moments and endpoints.
* `python INDEPENDENT_ORDERED_STAGE135.py` -> local `ordered_run.json`: PASS, separately implemented recursive Bellman + complete top-down integer-prefix DFS, four corners, first-hit A 35/B 11 words, and exact coefficients. DFS visits 704938/691078/704806/690946 prefix nodes.
* `python SCAN_STAGE136.py` -> local `scan136_run.json`: DUAL_CANDIDATE_ONLY, first closure at (10,6,2); no Stage136 primal claim.
* Three GitHub source Git Blob SHA1 values have been verified against the exact locally executed files:
  * CHECKER_STAGE135.py = 344dc8bd2c28e7c9ae6e11cc9ece27033391fd90
  * INDEPENDENT_ORDERED_STAGE135.py = 62dcdda7cf89ac9c5c098aa07c322d0685bd0903
  * SCAN_STAGE136.py = 18332eca1f6385d6e0d33672e1df8cfa25f0a867
* Source: fixed global main 7b33f8066e9993e7c941959a9d738ed405248eb8, initial EM pin e27e64dfe4803804ff84c9ca75d83da4cc38459b, live Stage134 proof Git blob a3617b8862c92ef97090babe549309642f748597.
* Native control listing failed CONTROL_QUOTA and service native researcher session creation was expressly refused STATIC_READONLY_SCOPE_DENIED / operation_sent=false. No native owner or claim is asserted; author calculations do not establish a Result/Review/Working Truth or native X6 theorem.
