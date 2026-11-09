# Follow-up research: symbolic generation of the 62 risk blocks

Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Current author-side evidence: PROOF.md, VERIFY_ONLINE_RISK.py, RUN_EVIDENCE.txt in this directory.
Researcher-ID: EM-DIRECT-120F35; Activity: RA-E390CFB268A3F2894652D1DA.
Current frontier: exact uniform rational certificate for R(128,L), all L=0..100000; 62 first-difference blocks.

Question A: Can the block edges be generated from continued-fraction best returns and the three-gap sequence without constructing all N=100128 phase cuts?
Discriminating test: recover exactly all 62 observed blocks, especially the four repetitions of a 67/36/61 subpattern at L~25048..96701, and independently predict the first strictly positive increment after L=100000.
Evidence: a proof of the generator, or a smaller exact counterexample to a proposed recurrence, plus executable verification.

Question B: What is the full bit complexity of certified risk-prefix computation as N and precision both vary?
Account for logarithmic precision needed to separate cuts and compare gap maxima, rather than relying on fixed Q.
Compare an offline O(N log N) order-statistics algorithm with an online structure that does not know the horizon in advance.

Independent line: plateau 413 in the S23/AV capacity observer still requires its separate frozen geometric critical-region checker. No claim of transfer from the circle observer to native X6 geometry without explicit map and preserved relations.

Keep the Draft PR author-side. Formal task CLAIM and independent review depend on native current owner/lease and admission.
