# T6 p13 q20 split(9,11): exact c581, reverse index sharding

2026-11-25; own scientific contribution of existing Driver EM-DVR-DEBB5E. NOT_REVIEWED. Same cancellation-normalized valuation-one finite domain and both mass caps 2331 as prior c551..580 note at 764c8fb336078d53eef935c9925dcf12661c9fa0:research_notes/portable_direct/2026-11-25_t6_p13_q20_split9_11_budget551_580_four_residues.md. Four necessary residue coordinates k=4,5,6,1 with exact 61-bit key. Q9 budget B=810, Q11 B=472. c=810-w(P). No repeat of c<=580.

The full forward attempt c581..610 timed out before target index completion (DP band count 1158187077). A reverse attempt indexing the entire c581 band also timed out before completion (132273900 expected). Neither attempt is credited. Successful alternative: partition the same ordered Q9 positive multisets P by index modulo 16, index only the c581 query profiles in each shard, then stream all 100750914 Q11 profiles against this exact index. Bitmap only rejects absent buckets; every survivor has full 61-bit equality checked. Every P index belongs to one shard. Every horizontal multiset of allowed mass is enumerated; duplicate keys would not affect membership. Therefore absence of intersections in all 16 shards excludes precisely the full c581 band. Integer DP and full enumeration agree: P=372 at weight229, H=355575 at mass <=581, product132273900. Q11 count independently checked by same coin-DP constructor against the complete enumeration in each run.

Actual successful logs (normal exit 0 in all 16 runs, query unique count equals profiles in each run, all target counts 100750914, all hits 0). Columns: shard P query_profiles target_bitmap_survivors wall_seconds max_RSS_KiB.
```
0 24 8533800 3152559 2.46 125720
1 27 9600525 3535207 3.01 134040
2 17 6044775 2242973 2.28 106260
3 19 6755925 2504310 2.21 111640
4 20 7111500 2634976 2.31 114508
5 23 8178225 3023696 2.61 122900
6 20 7111500 2633702 2.64 114576
7 25 8889375 3279972 3.03 128404
8 27 9600525 3539240 3.13 134040
9 22 7822650 2896711 5 120084
10 13 4622475 1718538 2.66 95124
11 33 11733975 4307339 3.66 150552
12 24 8533800 3154544 2.57 125716
13 25 8889375 3280708 2.7 128404
14 32 11378400 4181047 3.47 147872
15 21 7467075 2767731 2.27 117272
TOTAL 372 132273900 48853253
```
Sum successful wall time 46.01s; peak RSS 150552 KiB. Target group counts for every run: 25162293,25133768,25355561,25099292. Shard scan totals include repeated target generation by design, not additional new Q9 coverage. Independently counted with Python unbounded knapsack, iterating integer smooth atoms in ascending n (rather than descending q), using q,r=divmod(n,13), w=13r-1; horizontal H[0]=1, positive D[0][0]=1; update each atom in ascending q and mass, compute D[9][229]*sum(H[:582])=372*355575=132273900. 

Cumulative Source-backed Q9 coverage 4460549347; separate historic author report c451..500 original groups 0,2,3 =859902502, original logs still missing. Combined reported 5320451849/8963595909. Fresh remainder c582..810=3643144060, plus missing historical log recovery. q20(10,10) open. No full signed split, Result acceptance, Task or mother closure.

## Exact reproduction
Use the pinned C++ block from f7f9693709f9ca2e89870561bd093b16e6786a40:research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget301_400_four_residues.md, retain all definitions before int main (including D constructor, exact add/key, hash64). Replace only main with the following. Compile g++ -O3 -march=native -std=c++17 -pthread, execute ./q 581 581 s 16 for each s=0..15. 
```cpp
int main(int argc,char**argv){int lo=atoi(argv[1]),hi=atoi(argv[2]);D d(9,hi);assert(d.full==8963595909ULL);U expect=0,np=0,band=0;for(int w=0;w<=d.B;w++)if(d.B-w>=lo&&d.B-w<=hi)band+=d.pd[w]*d.hc[d.B-w];int shard=atoi(argv[3]),mod=atoi(argv[4]);for(size_t i=shard;i<d.p.size();i+=mod){auto &x=d.p[i];int c=d.B-x.w;if(c>=lo&&c<=hi){expect+=d.hc[c];np++;}}cerr<<"full band="<<band<<" shard="<<shard<<" mod="<<mod<<endl;cerr<<"band="<<lo<<".."<<hi<<" expected="<<expect<<" P="<<np<<endl;vector<U>keys;keys.reserve(expect);constexpr int bits=28;vector<U>bm(1ULL<<(bits-6));U ps=0;for(size_t i=shard;i<d.p.size();i+=mod){auto &x=d.p[i];int c=d.B-x.w;if(c<lo||c>hi)continue;ps++;for(size_t j=0;j<d.hc[c];j++){U k=key(add(x.s,d.h[j].s));keys.push_back(k);U b=hash64(k)>>(64-bits);bm[b>>6]|=1ULL<<(b&63);}}assert(keys.size()==expect&&ps==np);sort(keys.begin(),keys.end());keys.erase(unique(keys.begin(),keys.end()),keys.end());cerr<<"query unique="<<keys.size()<<endl;constexpr int prefix=20,shift=61-prefix;vector<uint32_t>ix((1<<prefix)+1);size_t off=0;for(size_t i=0;i<ix.size();i++){while(off<keys.size()&&(keys[off]>>shift)<i)off++;ix[i]=off;}assert(off==keys.size());D t(11,472);assert(t.full==100750914);U total=0,bh=0,hit=0;mutex mu;vector<thread>workers;for(int z=0;z<4;z++)workers.emplace_back([&,z]{U n=0,bh0=0,hit0=0;for(size_t i=z;i<t.p.size();i+=4){auto &x=t.p[i];int c=t.B-x.w;size_t cnt=t.hc[c];n+=cnt;for(size_t j=0;j<cnt;j++){U k=key(add(x.s,t.h[j].s));U b=hash64(k)>>(64-bits);if(!(bm[b>>6]>>(b&63)&1))continue;bh0++;auto pr=k>>shift;if(binary_search(keys.begin()+ix[pr],keys.begin()+ix[pr+1],k)){hit0++;lock_guard<mutex>l(mu);cout<<"HIT "<<k<<" P "<<i<<" H "<<j<<endl;}}}lock_guard<mutex>l(mu);total+=n;bh+=bh0;hit+=hit0;cout<<"target group "<<z<<" profiles="<<n<<" filter="<<bh0<<" hits="<<hit0<<endl;});for(auto&x:workers)x.join();assert(total==t.full);cout<<"TOTAL "<<total<<" filter="<<bh<<" hits="<<hit<<endl;return hit?2:0;}
```
