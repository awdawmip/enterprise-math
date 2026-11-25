# T6 p13 q20 split(9,11): c501..520 exact four-residue exclusion

2026-11-25. Own scientific continuation of Driver EM-DVR-DEBB5E, NOT_REVIEWED. Same exact domain and executable as [c451..500 group1](https://github.com/awdawmip/enterprise-math/blob/a51509a74654778f96c8a5f9d77004a1c4bd338a/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget451_500_group1_four_residues.md). Maximal prime13, v=1 after high valuation cancellation, both exponent mass bounds2331, Q9 B=810, c=810-w(P), Q11 B=472, k=4,5,6,1 exact modular signature. Argument and bit filter correctness unchanged. No repeat of previous c0..500.

```
$ /usr/bin/time -v /tmp/q9par 501 520 -1
Q=9 full=8963595909 P=186647 H=164782
band=501..520 expected=759613767 P=5248
Q=11 full=100750914 P=246181 H=87579
targets unique=100750914
group 2 P=1270 profiles=183739777 filter=16455038 hits=0
group 1 P=1302 profiles=187884586 filter=16822495 hits=0
group 3 P=1330 profiles=193147792 filter=17294769 hits=0
group 0 P=1346 profiles=194841612 filter=17449136 hits=0
TOTAL 759613767 filter=68021438 hits=0
wall 28.67s; user 71.94s; system 0.77s; peak RSS 952124 KiB; exit 0.
```

All four original P-index classes partition the band; count checked against independent integer coin DP in executable, full exact target lookup for every filter survivor. New verified exclusion 759613767 profiles; source-backed cumulative 2487158656; historical author reports add 859902502 profiles in c451..500 original groups 0,2,3 (counts revalidated but raw hit-test logs still missing). Author-history cumulative 3347061158/8963595909; fresh remainder c521..810 5616534751; q20(10,10) remains. No native Result/review/task/parent completion.

F7 exact artifact request dvr-20261125-1300-f7-exact-result-artifact-v1 SUCCEEDED (complete artifact verified, SHA256 2a89647a31de47e4ddef17ae61a843ea9a271fe602f8ab60adcca81699022c9b). Same own managed Driver submitted current review flow read using correct result_request_id via dvr-20261125-1300-f7-flow-verified-result-v1; queued on admission. Consume original terminal; no replay of old review write.