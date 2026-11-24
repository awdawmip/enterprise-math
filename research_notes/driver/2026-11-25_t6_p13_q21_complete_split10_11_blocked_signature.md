# T6 p13 q21 complete: split(10,11) exact high signature join
2026-11-25. Historical Driver lane EM-DVR-DEBB5E; author-side contribution, not independent decisive review.

## Proposition and exact domain
Reuse T6 taskbook research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md and higher-valuation cancellation cd764082e3080198d5df0ecd3a3fcc3ee4a560b7. For maximal prime 13 and side mass <=2331, cancel common atoms and valuation >=2 layers. Remaining valuation-one denominators d=13u, u=13q+r (1<=r<=12, u 13-smooth), residual mass w=13r-1. For side Q, residual budget B=2331-169Q. H0..H6 imply reciprocal moments 0..6 by triangular binomial transformation. Multiplication of kth reciprocal moment by 13^k and reduction mod 13^k removes lower valuation terms. Thus G=(sum u^-k mod 13^k) for k=4,5,6 must match. Every side uniquely decomposes into positive-q multiset P and q0 multiset H with w(P)+w(H)<=B. Q10 vs Q11 have different total Q, so zero matching keys excludes the split and its reverse.

Use the exact generator in e41421b9143287ae1d61ccbc663b2034867d64b6:research_notes/driver/2026-11-25_t6_p13_q21_split8_13_inverse_high_signature.md through init(), with horizontal profiles sorted by mass after hgen. The 15/19/23-bit lanes encode the actual three residues injectively. No hash assumption is used for correctness. Exact target keys all sorted. Each query checks a necessary bitmap condition then exact binary search; the blocked variant sets all three bits of the same 64-bit word for every target, so cannot reject a genuine target. Enumerate each P index once by its residue mod 4; for each P all H with permitted mass (upper_bound). DP on the original atom types and independent generated P/H mass convolution agree. No exclusion is claimed for a high-key collision; full six residues and lower-prime completion would then be required.

## Execution evidence
Q11 P=246181 H=87579 full=100750914, no duplicate target keys in both builds. Q10 P=306988 H=729803 full=1328547997. First run used two 2^30-bit maps; timed out after two complete worker reports, other two not credited. Each report is printed only after that worker's full loop. Rebuilt the same target domain, retained completed worker groups, resumed only residues 1 and 2 with the blocked bitmap and thread-local counters (no new mathematical assumptions).
|P index mod 4|complete queries|first bitmap passes|exact membership checks|exact hits|run|
|---|---:|---:|---:|---:|---|
|0|336066191|30099054|2696049|0|initial completed worker|
|3|332844999|29812839|2668200|0|initial completed worker|
|1|331113667|1406207|1406207|0|remaining exit 0|
|2|328523140|1393808|1393808|0|remaining exit 0|
|total|1328547997|62711908|8164264|0|all four disjoint groups|
Combined queries equal DP exactly. Second run wall 28.44 s, max RSS 1073536 KiB, exit 0; no full-run wall claim for interrupted initial attempt. Source SHA256 initial 954b141a215abcfc94db4af6129f9954fb936a7061ed11e9e8673e837a505d09, resumed d2d01b827a6ec072bdbda9122684279fd9b8ad8d29e33eb1a0bcd310ad511a02. Initial log lines: thread 3 n 332844999 b1 29812839 b2 2668200 exact 0; thread 0 n 336066191 b1 30099054 b2 2696049 exact 0. Resumed log lines: thread 2 n 328523140 b1 1393808 b2 1393808 exact 0; thread 1 n 331113667 b1 1406207 b2 1406207 exact 0; total 659636807 b1 2800015 b2 2800015 exact 0.

## Reproduction
Use generator referenced above, with sort(hor.begin(),hor.end(),[](auto&x,auto&y){return x.w<y.w;}); after hgen(0,0,{}). Replace main with the following compact equivalent blocked variant (all four groups; run one or more groups by passing group arguments). Compile g++ -O3 -std=c++17 -pthread. No reliance on earlier reported target injectivity.
```cpp
U block(U z){return z&((1ULL<<25)-1);}
U bits(U z){return (1ULL<<((z>>25)&63))|(1ULL<<((z>>31)&63))|(1ULL<<((z>>37)&63));}
int main(int argc,char**argv){
 U n=init(11);vector<U> keys;keys.reserve(n);vector<U> bitmap(1ULL<<25);
 for(auto&p:pos)for(auto&h:hor){if(p.w+h.w>B)break;U k=key(add(p.s,h.s));keys.push_back(k);U z=mix(k);bitmap[block(z)]|=bits(z);}
 assert(keys.size()==n);sort(keys.begin(),keys.end());cout<<"target duplicates "<<(adjacent_find(keys.begin(),keys.end())!=keys.end())<<endl;
 U count=init(10);vector<size_t>lim;U expected=0;
 for(auto&p:pos){auto l=upper_bound(hor.begin(),hor.end(),B-p.w,[](int b,const P&h){return b<h.w;})-hor.begin();lim.push_back(l);expected+=l;}assert(expected==count);
 struct C{U n=0,passes=0,hit=0;};array<C,4>result{};array<bool,4>selected{};if(argc==1)selected.fill(true);else for(int j=1;j<argc;j++){int t=stoi(argv[j]);assert(t>=0&&t<4);selected[t]=true;}
 mutex out;vector<thread>ts;
 for(int t=0;t<4;t++)if(selected[t])ts.emplace_back([&,t]{C c;for(size_t i=t;i<pos.size();i+=4){auto&p=pos[i];for(size_t j=0;j<lim[i];j++){c.n++;U k=key(add(p.s,hor[j].s)),z=mix(k),b=bits(z);if((bitmap[block(z)]&b)!=b)continue;c.passes++;if(binary_search(keys.begin(),keys.end(),k)){c.hit++;lock_guard<mutex>lk(out);cout<<"hit "<<i<<" "<<j<<" "<<k<<endl;}}}result[t]=c;lock_guard<mutex>lk(out);cout<<"group "<<t<<" n "<<c.n<<" passes "<<c.passes<<" exact "<<c.hit<<endl;});
 for(auto&t:ts)t.join();U actual=0,check=0,hits=0;for(size_t i=0;i<lim.size();i++)if(selected[i%4])check+=lim[i];for(auto&c:result){actual+=c.n;hits+=c.hit;}assert(actual==check);cout<<"total "<<actual<<" exact "<<hits<<endl;return hits?2:0;
}
```

## Synthesis and coordination
q21 (8,13) e41421b9143287ae1d61ccbc663b2034867d64b6 and (9,12) bda94f5f1efc2ee6f58be791287d7eb4188ce762 plus present (10,11) cover all unordered signed splits since Q<=13. q21 complete, q10 and q21..26 excluded under stated assumptions, q>=27 impossible by budget. q20 and other remaining q/lower prime/H0 remain; T6 global OPEN. No native review or result admission. Original prior read dvr-20261125-0400-t6-current-read-v1 SUCCEEDED; new read dvr-20261125-0600-t6-current-read-v1 SUCCEEDED as of 2026-11-24T22:03:28.974832Z, HANDOFF_READY/NEEDS_DISPATCH, claim null. Preserve p17 q14 nonauthor scope. Onhour r151 continues q11, backlog r477 retains existing selection and pending owner read; no confirmed free worker. No protected write or replacement identity. Next: q20 split(7,13) exact inverse join with mass restriction or smaller lattice, preserve high-key collision completion.
