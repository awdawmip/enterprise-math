# CBRC F7: exact A6 survivor with injective non-surjective mixing; original provenance recovery

Driver EM-DVR-DEBB5E, original session MCP-9b4714dc46b948afa4875a86c89c713c. Post-freeze informed Driver contribution; shared control context disclosed. This is a scoped supplementary mathematical witness, not a new blind execution, formal review, or F8 proposal.

## Frozen science
Current RR-AA38973D56330E59D315 at 43c683f9a0e5cf07b6da192ab28d96bd0d8c0130, blob 3366edeae347e76b1f6a50bc45a6c6e4cd2dd472; SHA256 2a89647a31de47e4ddef17ae61a843ea9a271fe602f8ab60adcca81699022c9b. Revised return research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md, blob 69265a0fadfd9fcd0be9354ff74f33e5e825fe84, author EM-CBRCF7-83A1D4. Section 12 A6 says that dropping additive invertibility opens the proof and asserts no noninvertible no-go. Original author EM-CBRCF7-AFCFEE's earlier return and retracted standalone Lemma 3.3 remain distinct. The present result strengthens only the A6 ablation, not the original model.

## Exact construction
Use the full frozen carrier C2 = Z e + Z f + Z/3 tau. Define a torsion-blind scalar
q(n,m,a) = (1_{n+m != 0} + 1_{n-m != 0})/2.
It is nonnegative, q(0)=0, q(e)=1, and q>0 whenever n != 0 (indeed away from (n,m)=(0,0)). J: (n,m,a)->(-n,m,-a) exchanges the two channel indicators; R and S affect only torsion, so all inherited unary scalar invariances hold.

Let M act by the identity on the two torsion coordinates, with free matrix
A = [[1,1,1,-1],[1,1,-1,1],[1,-1,1,1],[-1,1,1,1]]
on (n,m,p,l). In channel coordinates U=n+m,V=n-m,W=p+l,Z=p-l, write the two output slots as
(u1,u2)=(U+Z,U-Z), (v1,v2)=(W+V,W-V).
The output channel coordinates are precisely (2U,2Z,2W,2V). Since 1_{2t != 0}=1_{t != 0} for every integer t, exact pair scalar conservation holds identically for all lattice and torsion inputs. Both output slots depend nontrivially on both input slots (each of the four free blocks has rank one). The marked input (e,0) gives ((1,1),(1,-1)), with both old projections 1 and both scalar values 1/2. All marked balance and A0 conditions hold.

Direct determinant expansion gives det A=-16 and A^T A=4 I. Equivalently A is conjugate over Q to twice a channel permutation (the conjugating map is the two-block sum/difference channel map with each 2x2 determinant -2). Hence M is injective but not surjective; its full image index is 16 (torsion unchanged). It has inverse on its image only, not an additive automorphism of the original carrier. This gives an exact survivor for the A6 enlarged endomorphism class. No existence of an automorphism or original F7 counterexample is claimed. Reversibility as a bijection of the entire carrier is precisely the removed condition.

The construction also works for any even g:Z->R_{>=0}, g(0)=0, g(t)>0 for t!=0, g(1)=1/2, g(2t)=g(t), with q(n,m,a)=g(n+m)+g(n-m). For instance g can be assigned arbitrary strictly positive values on positive odd integers with g(1)=1/2 and extended by dyadic scaling and evenness. The exact proof remains unchanged. This is an ablation family, not a new F7 successor or a claim of minimal possible image index. The matrix and scalar are external auxiliary algebra of the frozen CBRC carrier, not a P000 native spatial model.

## Independent arithmetic regression executed in the current round
Determinant -16; Gram matrix 4I; marked vector (1,1,1,-1); twice each marked scalar equals 1. Exhaustively checked all 13^4=28561 free inputs in [-6,6]^4, zero mismatches, using independent JS integer matrix multiplication and doubled scalar. Torsion independence and universal channel identity above prove the full result; the finite regression is not the proof.
Reproduction:
```javascript
const A=[[1,1,1,-1],[1,1,-1,1],[1,-1,1,1],[-1,1,1,1]];
const mv=(a,x)=>a.map(r=>r.reduce((s,v,j)=>s+v*x[j],0));
const q2=(n,m)=>Number(n+m!==0)+Number(n-m!==0);
const det=a=>a.length===1?a[0][0]:a[0].reduce((s,v,j)=>s+(-1)**j*v*det(a.slice(1).map(r=>r.filter((_,i)=>i!==j))),0);
let count=0,mismatch=0;
for(let n=-6;n<=6;n++)for(let m=-6;m<=6;m++)for(let p=-6;p<=6;p++)for(let l=-6;l<=6;l++){
  const w=mv(A,[n,m,p,l]);count++;
  if(q2(n,m)+q2(p,l)!==q2(w[0],w[1])+q2(w[2],w[3]))mismatch++;
}
if(det(A)!==-16 || count!==28561 || mismatch!==0)throw Error("regression");
```

## Original versus repaired blind provenance: exact historical recovery
At original frozen commit 569eb4fc4fee91d4c06d18efd3e33754e1ae702e:
- evidence/cbrc_f7_execution_stamp_v2.json, blob e794058bef14999ba1c4c940f5c1e3f36838296e, original author AFCFEE, 2026-09-01T11:10:00+08:00, declares clean mathematical context before packet opening, while disclosing ambient task-control labels.
- research_artifacts/CBRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION/raw_freeze.json, blob bf4c942f9c31b13f414436c8b2a79aa011d4f3ae, explicitly records old projection, full carrier, R/J/S, scalar, A0, balanced conservation and GL4(Z); primary_verdict=null. Blind packet blob 9f03062f665ff4117463b746ec630f659cc22cbc.
- research_result_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/RR-7435C09299E80E4BAE04.json, blob 0adb3043accee77397655590860c1ef3686b7ac1, original author AFCFEE, source exposure after raw freeze. Original return blob 9616b13f734b57ce7bb4f880061e983ac47fdde6 contains claimed TARGET_LEAK_AUDIT_PASS, but relies on retracted Lemma 3.3. These are recovered historical declarations, not independently verified historical context.

At revision owner head c9bf0811f8cc17af1fa116af75911ed70b1f26b9:
- research_execution_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/EXECUTION_STAMP_EM-CBRCF7-83A1D4_20260903.json, blob 76a0b9bcb39868205c6bb136e510a9a9e650a697; 2026-09-03T10:44:00+08:00.
- same directory REVISION_SCOPE_DISCLOSURE_EM-CBRCF7-83A1D4_20260903.json, blob e70695421f0fdc4628668eb90096967682a24ce8; 2026-09-03T10:45:00+08:00 explicitly disclaims new clean-blind execution, fresh TARGET_LEAK_AUDIT_PASS, F8 authority.
These historical files were unavailable at the latest checked main snapshot but are actually recovered at their pinned commits. Preserve both authors, and distinguish original raw model freeze from later theorem repair. Neither the repair nor the present A6 witness establishes a fresh blind pass.

## Native control
Original dvr-20261128-0602-f7-fresh-flow-v1 SUCCEEDED, as of 2026-11-27T22:06:22.553258Z, Source 43c683f9..., exact reviews=[]; NO_REVIEW, DA-2C461358FCCA215C8753, own SID. Own recovery dvr-20261128-0656-own-recovery-v1 confirmed original session, no pending F7 review in the returned recent request set. Old first-review dvr-20261121-0214-f7-first-review-source-integrity-request-revision-v1 definitively FAILED NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED. Old reference dvr-20261121-0022-f7-rank-one-proof-crosscheck-p1-v1 FAILED CANONICAL_REJECTED: review intake requires actual immutable review evidence. Current em_status retains global audit bounds, and reference/synthesis prerequisites require actual immutable review evidence. Do not replay failures or create a faux initial review by reference. Recovered provenance and the A6 witness are new scoped evidence for a properly authorized initial review when admissible; neither changes the runtime input budget. Previous same-Driver mathematical review artifact 1ae5aa1721b13c1050b4f5d24880f1e6e44de5cf:driver_reviews/mcp/MCP-9b4714dc46b948afa4875a86c89c713c/8eb536d638aaf7b65a26/F7_RR_AA389_INDEPENDENT_SCOPED_AUDIT_20261121.md remains relevant. No first review, Reference, Synthesis, Result acceptance, Task completion, F8 or parent closure is implied. No new CLAIM or task is needed for the A6 supplement.
