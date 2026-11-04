# EC49FAJ — Close the newly established H9/M5 interval [80,94]

State: PORTABLE_AUTHOR_NEXT_UNIT / NOT_FORMALLY_DISPATCHED. Parent EC49FAI addendum on PR #1730. The parent H8 finite input remains pinned at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; H9 is a newly declared auxiliary extension, not a rewrite of H8, P000 or ACTIVE worldview.

**Verified author-side frontier:** EC49EXJ gives exactly `E8(M4,S<=6)=90`; EC49FAH gives `E8(M5,S<=6)=76`; the new terminal-separation theorem gives `E9(M5,S<=6)>=80`. The explicit eight-horizon 90-edge four-cache witness plus two new h9 words `fegfgfggg,geffgfggg` gives `E9=94,M=5,S=6`, with executed 9-history rank-nine tests at each horizon. Full proof and exact checker: `EC49FAI_HORIZON_ADJUNCTION_TRANSFER/ADDENDUM_H9_TRANSFER.md`, `VERIFY_EC49FAI_H9.js`, `EXACT_REPORT_EC49FAI_H9.json`.

**Concrete next action:** classify all observer-admissible full positive BRC key families for h9 in the same seven-operation language, then inspect H8 five-key candidate schedules attaining or approaching 76 and test if any contains a key feasible at h9 without adding a sixth key. Independently search legal H9 five-key schedules using an exact signed primitive-prefix optimizer for E<94, or give a correct lower-bound certificate ruling that out for a precisely defined family. Try structural prefix-cover bounds and reuse symmetry as appropriate; do not blindly recompute all H8 classes.

**Separate acceptance:** independent Driver audit of the complete EC49EXJ and EC49FAH classifications, observation-rank facts and the new terminal-separation lemma. Existing author-side code/report publication grants no native CLAIM, Result, review or Foundation promotion. Publish new proof/paths/checker and read back in existing PR.
