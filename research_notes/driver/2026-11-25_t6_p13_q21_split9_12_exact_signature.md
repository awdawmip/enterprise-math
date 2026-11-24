# T6 p13 q21 split(9,12): complete exact high-signature exclusion
2026-11-25. Driver historical lane EM-DVR-DEBB5E; author-side computation, not independent decisive review or native admission.

## Proposition
Reuse exact T6 taskbook research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md and p13 higher-valuation cancellation at cd764082e3080198d5df0ecd3a3fcc3ee4a560b7. For maximal prime 13 and side mass <=2331, cancel equal atoms and layers of valuation >=2. For remaining d=13u with u=13q+r, 1<=r<=12, u 13-smooth, residual atom mass w=13r-1 and side budget B(Q)=2331-169Q. Equality of the original moments implies equality of G(U)=(sum u^(-k) mod 13^k) for k=4,5,6, by multiplying reciprocal moment k by 13^k. Lower valuations vanish modulo 13^k. As Q differs, the two nonidentical profiles cannot be identical by common-atom cancellation.

Every profile is uniquely a positive-q multiset P and horizontal multiset H (including repeated atoms), with w(P)+w(H)<=B(Q). Enumerate in nondecreasing atom-index order (q descending, r ascending). Build exact packed high keys of all Q12 profiles, then enumerate all Q9 profiles and check membership. Each lane fits 15/19/23 bits; packed key equality is exact equality of all three residues, not a hash. A 2^28-bit bitmap is a necessary prefilter only; every hit is checked by exact sorted-key binary search. Independent integer coin DP and actual P/H cost convolution agree for both domains. Each interval enumerates all H with permitted mass via upper_bound. The six contiguous intervals cover all positive profiles, and the query sum equals DP. Zero exact matches therefore excludes split(9,12) and reverse. q21 split(10,11) remains, not claimed complete.

## Executed results
Q12 P=58880, H=5989, DP=2583672; Q9 P=186647, H=4298444, DP=8963595909. All H are counted up to the entire residual budget (a superset for positive profiles); the mass cutoff is exact. The first two executions were serial, then the remaining four were launched in parallel, using cumulative mass-feasible query counts to balance intervals. The controlling command timed out while the four child processes were still running; their original logs subsequently each returned exit 0 and complete ranges. No replay, no credit for an unfinished process. Elapsed below is per-process measured wall time, including initialization (parallel times are not summed as total wall).
|P index interval|queries|bitmap hits|exact high matches|wall s|exit|
|---|---:|---:|---:|---:|---:|
|[0,1428)|500654345|4793565|0|9.75|0|
|[1428,6456)|1000297739|9582933|0|23.14|0|
|[6456,24776)|1865897031|17864758|0|64.70|0|
|[24776,44124)|1865878549|17863583|0|63.88|0|
|[44124,87928)|1865455834|17871680|0|68.55|0|
|[87928,186647)|1865412411|17868636|0|72.82|0|
|total|8963595909|85845155|0|—|—|
Peak RSS per process <=188744 KiB. Actual serial measured walls 9.75 and 23.14s; four-process batch max child wall 72.82s. Executed source SHA256 170aadb7656a942229a1fa67b21ee90de7f19ec7853a99ed01e70c83950682fc.

## Reproduction
Use the generator in the prior immutable q21 note e41421b9143287ae1d61ccbc663b2034867d64b6 (research_notes/driver/2026-11-25_t6_p13_q21_split8_13_inverse_high_signature.md), through init(), adding `sort(hor.begin(),hor.end(),[](auto&x,auto&y){return x.w<y.w;});` immediately after hgen(0,0,{}). Replace its struct K and main by the following actual main; compile g++ -O3 -std=c++17. Invocations (start, cap): (0,500000000), (1428,1000000000), (6456,1865897031), (24776,1865878549), (44124,1865455834), (87928,1865412411). No assumption of horizontal signature injectivity or random hash behavior is required.
```cpp
int main(int argc,char**argv){
 U n=init(12);vector<U>keys;keys.reserve(n);constexpr U mask=(1ULL<<28)-1;vector<U>bitmap(1<<22);
 for(auto&p:pos)for(auto&h:hor){if(p.w+h.w>B)break;U k=key(add(p.s,h.s));keys.push_back(k);U b=mix(k)&mask;bitmap[b>>6]|=1ULL<<(b&63);}
 assert(keys.size()==n);sort(keys.begin(),keys.end());U count=init(9);
 size_t start=argc>1?stoull(argv[1]):0;U cap=argc>2?stoull(argv[2]):500000000;assert(start<=pos.size());
 U queries=0,bhits=0,khits=0,check=0;size_t end=start;
 for(;end<pos.size()&&queries<cap;end++){
  auto&p=pos[end];auto last=upper_bound(hor.begin(),hor.end(),B-p.w,[](int b,const P&h){return b<h.w;});check+=last-hor.begin();
  for(auto it=hor.begin();it!=last;++it){queries++;U k=key(add(p.s,it->s));U b=mix(k)&mask;
   if(!(bitmap[b>>6]>>(b&63)&1))continue;bhits++;if(binary_search(keys.begin(),keys.end(),k)){khits++;cout<<"hit P "<<end<<" H "<<(it-hor.begin())<<" key "<<k<<endl;}}
 }
 assert(queries==check);cout<<"range "<<start<<" "<<end<<" queries "<<queries<<" bitmap hits "<<bhits<<" exact high hits "<<khits<<endl;return khits?2:0;
}
```

## Coordination
Original dvr-20261125-0400-t6-current-read-v1: private custody result lookup returned PRIVATE_CUSTODY_REQUEST_NOT_BOUND; this was a public control_task read, and its native em_control_result read returned SUCCEEDED, observed 2026-11-24T20:05:01.075664Z, Source bf6a742b787423c09619371fa5ec6eef9380f019. Mother Task HANDOFF_READY/NEEDS_DISPATCH, claim_id null in that snapshot; protected next action nonauthor p17 q14 model review; preserve separate scope. No new p13 frozen Result admission. Own driver custody remains valid, historical DA source read, no current write authority inferred. Onhour r148 q11 split(1,10) length5 pattern1 author-side complete, preserve ongoing q11. Backlog r476 preserves original DCMP11 selection, no confirmed available worker. No protected native write or duplicate request submitted. Next: q21 split(10,11), memory-bounded exact joins; any high hit needs full residual and lower-prime completion. No global closure or schedule change.
