# T6 p13 q20 split(9,11): c451..500, original P-index class 1 completed

2026-11-25; same Driver EM-DVR-DEBB5E, own scientific contribution, NOT_REVIEWED. Existing c401..450 immutable record: 3ce1d0abe914b9b15091664ad1455defefdccec0:research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget401_450_four_residues.md. Reuse domain and exact arithmetic of f7f9693709f9ca2e89870561bd093b16e6786a40:research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget301_400_four_residues.md: maximal prime 13, cancellation-normalized valuation 1, both exponent mass caps 2331, Q9 residual budget B=810, c=B-w(P), Q11 target budget 472, four necessary inverse-power residues k=4,5,6,1. Multiplying full reciprocal power equalities by 13^k eliminates all 13-free denominators modulo 13^k. The result is a finite exact exclusion in this profile domain.

## Actual executed result

One original single-thread group-1 run c451..500 timed out after constructing all 100750914 distinct target keys, with no completed group-1 output; credited zero. Then divided c451..500 into two disjoint intervals and distributed the original i mod4=1 class over four workers, with each worker z enumerating i=1+4*z mod16. No change to atom enumeration, mass, hash, exact comparison or target set. Built g++ -O3 -march=native -std=c++17 -pthread /tmp/q9par.cpp -o /tmp/q9par. Both completed normally.

```
$ /usr/bin/time -v /tmp/q9par 451 475 1
Q=9 full=8963595909 P=186647 H=91209
band=451..475 expected=512716234 P=7112
Q=11 full=100750914 P=246181 H=87579
targets unique=100750914
group 0 P=410 profiles=29559230 filter=2648517 hits=0
group 1 P=426 profiles=30692815 filter=2747723 hits=0
group 2 P=453 profiles=32978701 filter=2953813 hits=0
group 3 P=485 profiles=34771497 filter=3114980 hits=0
TOTAL 128002243 filter=11465033 hits=0
wall 15.16s; user 21.91s; system 0.49s; peak RSS 952792 KiB; exit 0.

$ /usr/bin/time -v /tmp/q9par 476 500 1
Q=9 full=8963595909 P=186647 H=128402
band=476..500 expected=642453119 P=6272
Q=11 full=100750914 P=246181 H=87579
targets unique=100750914
group 0 P=395 profiles=40274817 filter=3607158 hits=0
group 2 P=413 profiles=42233335 filter=3785154 hits=0
group 3 P=423 profiles=43610145 filter=3904615 hits=0
group 1 P=402 profiles=41146311 filter=3686811 hits=0
TOTAL 167264608 filter=14983738 hits=0
wall 16.50s; user 24.84s; system 0.81s; peak RSS 953556 KiB; exit 0.
```

New exact exclusion: 295266851 profiles, 26448771 bitmap survivors, zero exact hits. Four worker classes in each new log are the subdivision of original group 1, not original groups 0..3. Independent Python integer count enumerated positive P weights and computed H via unbounded coin DP (then cumulative sums); the group table is:

| c | original 0 | original 1 | original 2 | original 3 |
|---|---:|---:|---:|---:|
|451..475|120606231|128002243|132494869|131612891|
|476..500|160659984|167264608|157624250|156904277|
|451..500|281266215|295266851|290119119|288517168|

Prior turn reported zero hits for original groups 0,2,3 in c451..500, total 859902502, but its raw computation logs were not saved remotely and are not available in the present local runtime. Their counts were reproduced here, not their match tests. Preserve those as historical author-reported evidence, not newly verified exclusions. No repeat of those three groups in this run. If original logs cannot be recovered, exact targeted replay is a future evidence-repair option after checking in-flight work. c0..450 previously saved =1432278038; plus newly completed group 1 =1727544889 with source-backed logs. Including prior author reports, coverage =2587447391 of 8963595909; unsearched according to author history 6376148518 in c501..810; additionally 859902502 have unverified historical logs. Do not mark split complete.

## Reproduction delta

Take the exact C++ source in f7f9693709f9ca2e89870561bd093b16e6786a40 (above). Replace `if(argc>3)return 0;` by nothing; introduce `int group=atoi(argv[3]);` after lo,hi. Replace worker loop header `for(size_t i=z;i<d.p.size();i+=4)` by `for(size_t i=(group<0?z:group+4*z);i<d.p.size();i+=(group<0?4:16))`. Replace final `assert(total==expect&&ps==np);` by `if(group<0){assert(total==expect&&ps==np);}else{U a=0,b=0;for(size_t i=group;i<d.p.size();i+=4){int c=d.B-d.p[i].w;if(c>=lo&&c<=hi){a+=d.hc[c];b++;}}assert(a==total&&b==ps);}`. In the actual local variant group was declared together with lo,hi; no semantic difference. Actual local source SHA256 ea7849ed0bfd101410869685205aa02188ae120707cf5cf42622112123235bbf. No new formal admission.

## Control

Original dvr-20261125-1100-t6-current-read-v1 SUCCEEDED, and fresh dvr-20261125-1300-t6-current-read-v1 SUCCEEDED: HANDOFF_READY/NEEDS_DISPATCH, claim null; next action still old p17 q14 preflight nonauthor review. Retain stronger p17 source refs in prior c401..450 note, no redundant affine rerun. Original own managed SID recovered, not revoked/closed; no new registration, no current write authority inferred. Driver checkpoint was r563 at entry; onhour r166 and backlog r484 observed. No Result acceptance, native Review, formal Task or parent closure in this unit.