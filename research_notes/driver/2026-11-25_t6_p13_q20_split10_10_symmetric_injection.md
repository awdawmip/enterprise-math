# T6 p13 q20 split(10,10): full symmetric four-residue injection

2026-11-25. Existing Driver lane EM-DVR-DEBB5E, author-side mathematics, NOT_REVIEWED. Same p13 valuation-one, cancellation-normalized finite domain and both side mass caps 2331 as previous q20 split notes. q20(9,11) missing evidence independently re-executed by same author [here](https://github.com/awdawmip/enterprise-math/blob/59020934dbaa31bbe361921c687f6864d661af98/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_evidence_closure.md). For (10,10), both sides have Q=10 and B=2331-169Q=641, and are in the same finite multiset domain. Let u=13j+r be positive 13-smooth with 1<=r<=12; vertical sum j=10 and residual mass sum(13r-1)<=641. Define G=(sum u^-4 mod13^4, sum u^-5 mod13^5, sum u^-6 mod13^6, sum u^-1 mod13). The previous necessity reduction requires equal G. An injective G forces the two multisets equal, hence after common cancellation no nonempty unequal pair survives. Do not count diagonal self-pairs as counterexamples. This statement uses the earlier cancellation and observation hypotheses, not a different observer.

Independent Python ascending-u unbounded integer coin DP: P=306988 vertical profiles, H=729803 horizontal profiles, total 1328547997. Grouped by c=641-w(P): 0..200:29135199, 201..300:170862332, 301..400:441316626, 401..500:480870664, 501..641:206363176. Counts sum to full domain. The original exact recursive enumerator separately obtains the same P,H,total. Every profile is enumerated once by nondecreasing atom indices, and each vertical profile is joined with every horizontal multiset with permitted mass. Sorting horizontal profiles by weight permits exact prefix length from DP. Original definitions through hash64: [source](https://github.com/awdawmip/enterprise-math/blob/f7f9693709f9ca2e89870561bd093b16e6786a40/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget301_400_four_residues.md). Replace main by the partition writer below; exact key is injective encoding of the four residues (61 bits), not hash equality. Identical keys always go to same bucket, so cross-bucket collision is impossible. Sorting each bucket and counting repeated runs tests all distinct profiles without retaining identities unless a collision occurs.

```cpp
int main(int argc,char**argv){D d(10,641);assert(d.full==1328547997ULL);constexpr int K=32;constexpr size_t CAP=1<<16;vector<vector<U>> buf(K);vector<FILE*> f(K);vector<U> cnt(K);for(int b=0;b<K;b++){buf[b].reserve(CAP);string name="/mnt/data/t6_driver/bucket"+to_string(b);f[b]=fopen(name.c_str(),"wb");assert(f[b]);}U total=0;for(auto &x:d.p)for(size_t j=0;j<d.hc[d.B-x.w];j++){U k=key(add(x.s,d.h[j].s));int b=hash64(k)>>59;buf[b].push_back(k);cnt[b]++;total++;if(buf[b].size()==CAP){assert(fwrite(buf[b].data(),sizeof(U),CAP,f[b])==CAP);buf[b].clear();}}for(int b=0;b<K;b++){assert(fwrite(buf[b].data(),sizeof(U),buf[b].size(),f[b])==buf[b].size());assert(fclose(f[b])==0);cout<<b<<" "<<cnt[b]<<endl;}assert(total==d.full);cout<<"TOTAL "<<total<<endl;}
```

Separate exact scan program (same hash64 definition, include bits/stdc++.h, using namespace std; using U=uint64_t;):
```cpp
int main(int argc,char**argv){int lo=atoi(argv[1]),hi=atoi(argv[2]);atomic<int> next(lo);mutex mu;U nsum=0,groups=0,pairs=0;vector<thread>t;for(int z=0;z<4;z++)t.emplace_back([&]{for(;;){int b=next++;if(b>hi)break;string path="/mnt/data/t6_driver/bucket"+to_string(b);auto size=filesystem::file_size(path);assert(size%8==0);vector<U> a(size/8);FILE*f=fopen(path.c_str(),"rb");assert(f&&fread(a.data(),8,a.size(),f)==a.size()&&fclose(f)==0);for(U k:a)assert((hash64(k)>>59)==(U)b);sort(a.begin(),a.end());U g=0,p=0;vector<pair<U,U>> dup;for(size_t i=0,j;i<a.size();i=j){for(j=i+1;j<a.size()&&a[j]==a[i];j++);if(j-i>1){g++;p+=U(j-i)*(j-i-1)/2;dup.emplace_back(a[i],j-i);}}{lock_guard<mutex>l(mu);cout<<"bucket "<<b<<" n="<<a.size()<<" groups="<<g<<" pairs="<<p<<endl;for(auto [k,c]:dup)cout<<"DUP "<<k<<" "<<c<<endl;nsum+=a.size();groups+=g;pairs+=p;}}});for(auto &x:t)x.join();cout<<"TOTAL "<<nsum<<" groups="<<groups<<" pairs="<<pairs<<endl;}
```

Actual local g++ -O3 -march=native -std=c++17 -pthread both programs. Partition run exit 0, 14.61s wall, peak RSS 38296 KiB, total 1328547997 keys; all file writes closed successfully. Per-bucket output counts from partition and completed scan match exactly:
```
0 41520586 groups=0 pairs=0
1 41520084 groups=0 pairs=0
2 41523879 groups=0 pairs=0
3 41515877 groups=0 pairs=0
4 41517243 groups=0 pairs=0
5 41516562 groups=0 pairs=0
6 41517592 groups=0 pairs=0
7 41523253 groups=0 pairs=0
8 41529753 groups=0 pairs=0
9 41522780 groups=0 pairs=0
10 41518067 groups=0 pairs=0
11 41508587 groups=0 pairs=0
12 41512787 groups=0 pairs=0
13 41515774 groups=0 pairs=0
14 41510573 groups=0 pairs=0
15 41520645 groups=0 pairs=0
16 41522546 groups=0 pairs=0
17 41518089 groups=0 pairs=0
18 41509496 groups=0 pairs=0
19 41519556 groups=0 pairs=0
20 41520267 groups=0 pairs=0
21 41507890 groups=0 pairs=0
22 41520802 groups=0 pairs=0
23 41504283 groups=0 pairs=0
24 41524787 groups=0 pairs=0
25 41509251 groups=0 pairs=0
26 41528603 groups=0 pairs=0
27 41498883 groups=0 pairs=0
28 41514814 groups=0 pairs=0
29 41513208 groups=0 pairs=0
30 41517191 groups=0 pairs=0
31 41524289 groups=0 pairs=0
```
Scan 0..15 completed exit0, 26.67s, peak RSS1299132 KiB, total 664294042. Scan 16..31 timed out; flushed, fully scanned bucket records 16..23 each show zero groups/pairs and matching count, total 332122929; no credit for unreported buckets in that invocation. Scan 24..31 separately exit0, 24.30s, peak RSS1298844 KiB, total 332131026. Each printed bucket record occurs only after the complete file read, membership assertion, sort and repeated-run count. No partial bucket counted. All 32 disjoint buckets now verified; sum 1328547997, zero repeated full keys and zero unordered off-diagonal matching pairs. Thus G injective on the complete finite Q10 domain. This is a source-backed exact computation, not independent contributor review. Together with already proved scoped split(7,13),(8,12),(9,11), closes the four previously remaining q20 signed splits at the stated valuation-one p13 necessary-residue scope. Global T6, any additional strata, formal review, Result, Task and mother objective remain open.