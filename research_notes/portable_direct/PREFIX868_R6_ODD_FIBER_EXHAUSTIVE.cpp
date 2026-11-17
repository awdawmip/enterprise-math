// PREFIX-868 full ordered-transition zero-fiber exclusion.
// Usage: ./check p b [min_q1 max_q1] ; exact integers; p=27,b=16 or p=29,b=17.
#include <bits/stdc++.h>
using namespace std;
static bool safe(int q,int p) {
    long long x=1;
    for(int d=1; d<p; ++d) {
        x=(x*2)%q;
        if(x==1 || x==q-1) return false;
    }
    return true;
}
int main(int argc,char**argv) {
    if(argc!=3 && argc!=5) { cerr<<"usage: check p b [min_q1 max_q1]\n"; return 2; }
    int p=atoi(argv[1]),b=atoi(argv[2]);
    if(!((p==27 && b==16)||(p==29 && b==17))) return 2;
    uint64_t N=1ULL<<p, M=(1ULL<<b)-1, T=N*(p+1);
    vector<int> good;
    for(int q=3;q<=(int)M;q+=2) if(safe(q,p)) good.push_back(q);
    vector<int> stamp(M+1,0);
    vector<uint32_t> fiber;
    uint64_t eligible=0, first_count=0, survivors=0;
    int epoch=0;
    for(int q1:good) {
        if(argc==5 && (q1<atoi(argv[3])||q1>atoi(argv[4]))) continue;
        uint64_t m=(N+q1-1)/q1;
        if(uint64_t(q1)*M<T || m*(p+1)>M) continue;
        vector<int> second;
        for(int q2:good) {
            if(uint64_t(q1)*q2<T || uint64_t(q2)<m*(p+1)) continue;
            if(uint64_t(q1)*q2/std::gcd(q1,q2)<N) continue;
            second.push_back(q2);
        }
        if(second.empty()) continue;
        ++first_count;
        eligible+=second.size();
        fiber.clear();
        fiber.reserve(m*(p+1));
        for(uint64_t u=0;u<N;u+=q1) {
            fiber.push_back((uint32_t)u);
            for(int i=0;i<p;++i) fiber.push_back((uint32_t)(u^(1ULL<<i)));
        }
        for(int q2:second) {
            ++epoch;
            bool injective=true;
            for(uint32_t v:fiber) {
                int r=v%q2;
                if(stamp[r]==epoch) { injective=false; break; }
                stamp[r]=epoch;
            }
            if(injective) ++survivors;
        }
    }
    cout<<"{\"p\":"<<p<<",\"excluded_width\":"<<b
        <<",\"safe_moduli\":"<<good.size()
        <<",\"first_count\":"<<first_count
        <<",\"eligible_pairs\":"<<eligible
        <<",\"zero_fiber_survivors\":"<<survivors<<"}\n";
    return 0;
}
