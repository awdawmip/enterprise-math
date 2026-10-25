# Stage140 local author validation
 
Exact author's local checker A performed 680-state Fraction Bellman recursion, 1238 positive gaps, two ties B=(11,0,1) and F=(5,3,0), exact root and full four-observer corner affine law. The derived h∈[0,1] family matched the Stage139 endpoint at h=0 and the exact Stage140 right endpoint at h=1; both errors equal and tP>tQ for the complete interval. PASS.
 
Independent checker B recomputed Bellman decisions by top-down recursion but evaluated the four observers using *literal ordered-prefix integer weights* (3,1,20)/24 and (1,1,10)/12, without Fraction observer propagation. Four corners PASS (672820, 672688, 650290, 650158 visited literal prefixes); B first-hits=11, F first-hits=10; exact P and Q first-hit masses consistent with checker A. Mixed observer defect=0. PASS.
 
GitHub's CHECKER_STAGE140.py is a source-bound portable **adaptation**, not one of the two executed local files and not claimed to have run remotely. Results remain author-level **external finite iid** findings without independent Research Driver review, native owner/CLAIM/Result, Lean proof, or P000/X6 transfer. Native em_control_tasks returned CONTROL_QUOTA.