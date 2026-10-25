# R288 — Cross-sign positive transfer: scientific handoff

Research-Activity-ID: RA-EM3-20261026-0046-R288CROSS
Local researcher label: EM-DIRECT-R288A1; source-native Researcher-ID/CLAIM not obtained.
Frozen global knowledge read: main@1fe18ba120c1f8f901246acb659589849b7e9147.
Pre-work EM source main: 6589b9d215977657f3efdf09cd0fef9ad17660f0.
P000 original blob: 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.

Completed: In the existing ordered positive-weight six-edge clean BRC auxiliary model, for all m>=1,

F^-_{m+2}(x)=x^2 C(x^2)F^+_m(x),
C(y)=1+y(1-y)/(1-2y-y(1+y)h(y)),
h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2,

all coefficients of C are strictly positive integers. Hence P_n(-,-m-2)>=P_{n-2}(+,-m) for every n, strictly for n>=m+6 and matching parity. In addition, Δ^-_{m+2}=x² C(x²) Δ^+_m. Both statements are exact all-length deductions conditional on previously author-side R283 and R286 kernel identities, not Source-admitted results.

Verification: actually executed exact standard-library Python DP through n=170, 1<=m<=30; 5130 coefficient identities, 2250 strict inequalities, 2280 lower bounds, and 2582 raw clean words through length14, all PASS. The script and exact evidence accompany this note.

Remaining: Four R287 full-length base positivity obligations Δ^+_13, Δ^+_14, Δ^-_11, Δ^-_12. The bridge writes the negative bases as positive convolutions of Δ^+_9 and Δ^+_10, but each of these inputs has a finite negative witness, so stronger compensation is required. Next action: isolate finite negative terms and certify their compensation by later positive mass in C; otherwise attempt R285 rational-cone asymptotics. No claim of 28 candidates, N_peak=81, or B_n=Λ_n as an unconditional theorem.

Native access actual: em_control_tasks CONTROL_QUOTA; em_session_start STATIC_READONLY_SCOPE_DENIED (operation_sent=false). GitHub publication is author-side provenance, not a native control bypass, owner assertion or Driver acceptance. P000, X6 and ACTIVE worldview unchanged.