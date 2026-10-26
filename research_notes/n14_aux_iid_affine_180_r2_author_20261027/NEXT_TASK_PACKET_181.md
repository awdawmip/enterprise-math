# Stage181 — exact first primal discriminator

Mother problem: the external N14 ternary IID full ordered-history randomized test with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), minimizing max(tP,tQ) with eP,eQ<=alpha. This is NOT a P000-native Cell theorem.

Stage180 author-verified full real frontier (do not reprove without contradiction):
    alpha180 = 1571047311779133836077/4497734146660704976896
    V180 = 25552058910086071560277/2248867073330352488448
    Delta180=77025390625/13556538588266496
    V14(alpha179+delta)=V179-(34167779/78874)*delta, 0<=delta<=Delta180.
S=(9,0,1) Q/C and W=(11,2,2) Q/C; exact balance s(w)=1999608121070003/9458452800000000-(30855/656837)*w. The right endpoint has w=1 (W coin saturated). Full author proof is PROOF_STAGE180.md, exact corners/crosscheck certificate180_summary.json; complete executed code/logs are in Stage180 portable pack.

Stage181 DUAL ONLY: hold S Q/C tie, force W=Q. Exact tangent (dK,dL)=(-1,-297152/359685), step 876512243052954766485/162830362841556584294, new tie V=(3,1,2) Q/C. Candidate:
    K181=441833535662847516/2064436478960831
    L181=432175273775571832/2064436478960831
    H181=1125553520578610530737003874877705/7068181637936142179391844122624
680 states, two ties S and V, 1238 strict positive gaps with min 812296169382427/99092950990119888. Evidence dual181.json, SCAN_STAGE181_REFERENCE.py. No primal Stage181 theorem yet.

**First unfinished unit:** Compute four deterministic S/V corner observables (eP,eQ,tP,tQ) by exact suffix DP and independent nonmerged P/Q integer-numerator ordered DFS. Prove whether first-hit cones can overlap; note a V=(3,1,2) history cannot be an ancestor of S=(9,0,1) because V_a>S_a and V_b>S_b, and S cannot be ancestor by depth. Solve the exact error balance, legal two-coin range, endpoint continuity and P-time dominance. If all hold, prove full REAL next optimality interval and strict support-line sharpness; otherwise preserve exact obstruction.

BRC: retain labeled ordered histories and separate positive P,Q weights. P000 fixed. No formal Source CLAIM or Driver review is represented by this author packet. Native access for this execution returned CONTROL_QUOTA / STATIC_READONLY_SCOPE_DENIED.
