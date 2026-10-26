# R321 Handoff — BRC Newton q=9

Date: 2026-10-27. Activity: RA-EMR3-20261027-R321-Q9-0523.
Role: TASK_RESEARCH, direct author only, locally assigned Researcher-ID EM-DIRECT-0523R3 (not native authenticated session). Authenticated GitHub writer: awdawmip.
GLOBAL_KNOWLEDGE_V1 frozen read: main@8ec98188025f60aafe48055520ba3a57c29cdb2c; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview retained.
Enterprise Math active control/source snapshot: main@dffe386cee25fb9c650d4aa46ff6f501c3745e8a; docs/PORTABLE_RESEARCH_PROTOCOL.md.
Prior author frontier: R320@ff4f2aaa06acecc75f2a57e9bfcb613822e85926.

## New complete unit
For integer s>=9, the ordered positive six-edge BRC auxiliary Newton coefficient a_(s,s-9) = 2^s Q9(s)/19025362944, Q9 defined in R321_TENTH_NEWTON_AUTHOR_PROOF.zh-CN.md, and a_(s,s-9)>=(74489/128)*2^s>0, with equality only at s=9.
The proof uses (Rr) derivatives, exact boundary values, induction identities r=0..9, falling-factorial recovery and an all-positive shift polynomial Q9(9+u). These identities are author-side proved but not independently reviewed.
Tools reused: R320 ordered six-edge BRC polynomial recurrence and moment/Newton observer; no claimed native six-dimensional Cell transfer.

## Evidence
R321_symbolic_identity.py: SymPy exact rational symbolic identities, run locally, PASS.
R321_verify_tenth_edge.js: Node.js BigInt exact finite recurrence s=0..192, 193 degree / 184 moment / 183 difference / 184 Newton direct / 184 recovery / 184 shift / 184 lower-bound checks, PASS.
R321_EXACT_EVIDENCE.json: machine output obtained by re-executing the GitHub-saved JavaScript code; status PASS.
Sample coefficients: a_(9,0)=297956; a_(10,1)=2431296; a_(11,2)=15230108.
Finite checks alone do not prove all s; the symbolic polynomial identities and algebraic positivity supply the universal argument.

## Control and scope
GitHub: awdawmip / repository admin. Native control task listing: CONTROL_QUOTA. Native session start: STATIC_READONLY_SCOPE_DENIED (operation_sent=false); active owner not authoritatively verified, no native CLAIM/Result, independent Driver or admission. This is a source-backed research note, not canonical Working Truth or Foundation.
P000 and ACTIVE worldview were read only. No credentials, tokens, external sharing changes.

## Next nonduplicate unit
Study r=10 and q=10 through the exact same source recurrence. First derive m10(s)=2^s P10(s) for s>=10, then determine a_(s,s-10)'s exact sign and boundary; if shift positivity breaks, find exact counterexample/necessary-sufficient residue. Alongside this, investigate a genuinely uniform central-index positivity method rather than relying indefinitely on finite fixed-q extensions.
Given R313's stated finite certificate s<=128, unresolved Newton region: s>=129, 0<=k<=s-10. The linear defect-fiber bound D_d(n)>0 for n>=4d+4 and N_peak=81 remain open.
