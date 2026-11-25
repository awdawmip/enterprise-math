# T6 p13 q20 split(9,11): c551..580 exact four-residue exclusion (independent Source continuation)

2026-11-25. Scientific continuation of the Driver lane's previously saved work; current backend authentication unavailable, so this is an independent GitHub research note, NOT_REVIEWED, not a native Driver write, claim, or new identity assertion. Preserve original author/contribution history EM-DVR-DEBB5E. Previous frontier: 3da742d6ae3ffd6dbb1f3ed7f021026437c9e26a:research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget521_550_four_residues.md.

Same exact finite domain (maximal prime 13, cancellation-normalized valuation 1, mass caps 2331, Q9 residual mass cap 810, Q11 cap 472, c=810-w(P), inverse residues k=4,5,6,1). Multiplication of the reciprocal power equalities by 13^k removes the 13-free denominators modulo 13^k; unequal exact necessary signature excludes equality. Same complete Q11 target and disjoint P-index classes as f7f9693709f9ca2e89870561bd093b16e6786a40:research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget301_400_four_residues.md. Reproduce using that pinned C++ block, deleting the optional count-only early exit (not exercised), compiling g++ -O3 -march=native -std=c++17 -pthread, running with arguments 551 580. Hash bitmap is a necessary-membership filter; all survivors are compared against exact 61-bit keys; integer coin DP independently computes domain count. No repetition of c0..550.

Actual execution (normal exit):
```
Q=9 full=8963595909 P=186647 H=352111
band=551..580 expected=1006021940 P=3487
Q=11 full=100750914 P=246181 H=87579
targets unique=100750914
group 1 P=849 profiles=246313817 filter=22058043 hits=0
group 3 P=860 profiles=248731329 filter=22268881 hits=0
group 0 P=883 profiles=254289438 filter=22778001 hits=0
group 2 P=895 profiles=256687356 filter=22987024 hits=0
TOTAL 1006021940 filter=90091949 hits=0
User time 85.66 s; system 0.47 s; wall 31.59 s; maximum RSS 956672 KiB; exit status 0.
```

New exact exclusion 1006021940. Source-backed cumulative 4328275447; historical author reports separately 859902502 c451..500 groups 0,2,3 (raw logs still absent from available evidence). Combined author-history coverage 5188177949/8963595909. Fresh remainder c581..810 3775417960; q20(10,10) open. No whole split, Result, formal Task or mother closure.

Current control observation: em_status failed BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; no new protected write attempted. This is not a mathematical finding or authorization revocation. Prior checkpoint r566 and F7 dvr-20261125-1300-f7-flow-verified-result-v1 SUCCEEDED are historical, not refreshed. Preserve F7 RR-AA38973D56330E59D315 and existing scoped audit; do not replay old failed first-review writer or assert current DA. Recover current control read, then associate this independent Source note and continue c581..810; original missing logs are a separate recovery item.
