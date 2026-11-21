#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using Mask = __uint128_t;
using u64 = uint64_t;
constexpr int count = 250;
constexpr int size = 13;
int bits(Mask x) { return std::popcount(u64(x)) + std::popcount(u64(x >> 64)); }
std::array<Mask, count> parents;
std::array<int, 16> selected{};
std::array<long long, 16> visits{};
int target = 0;
bool found = false;
bool list_all = false;

void search(Mask covered, int have, int left, const int* pool, int n, int depth) {
    ++visits[depth];
    if (have >= target) {
        for (int i=0; i<depth; ++i) std::cout << selected[i] << " ";
        std::cout << '\n';
        found = !list_all;
        return;
    }
    if (n < left || left == 0) return;
    int need = target-have;
    int min_best = (need+left-1)/left;
    int threshold = std::max(1,need-size*(left-1));
    std::array<int, count> gain, order, sorted_gain;
    std::array<int, size+1> hist{}, pos{};
    for (int i=0; i<n; ++i) {
        int v=bits(parents[pool[i]] & ~covered);
        gain[i]=v;
        if (v>=threshold) ++hist[v];
    }
    int m=0, best=0, slots=left;
    for (int v=size; v>=threshold; --v) {
        pos[v]=m;
        m+=hist[v];
        int take=std::min(slots,hist[v]);
        slots-=take;
        best+=v*take;
    }
    if (slots>0 || best<need) return;
    for(int i=0; i<n; ++i) {
        int v=gain[i];
        if(v>=threshold) {
            int j=pos[v]++;
            order[j]=pool[i];
            sorted_gain[j]=v;
        }
    }
    // Among the chosen rows enumerate first the one with largest current
    // gain, breaking ties by their order in the current pool.
    for(int i=0; i+left<=m && best>=need && sorted_gain[i]>=min_best; ++i) {
        int row=order[i];
        int v=sorted_gain[i];
        selected[depth]=row;
        if (left==1) {
            if(v>=need) search(covered|parents[row],have+v,0,nullptr,0,depth+1);
        } else search(covered|parents[row],have+v,left-1,order.data()+i+1,m-i-1,depth+1);
        if(found) return;
        if(i+left<m) best+=sorted_gain[i+left]-v;
    }
}

int main(int argc,char** argv) {
    if(argc!=4 && argc!=5) return 2;
    list_all=argc==5;
    int k=std::atoi(argv[1]);
    target=std::atoi(argv[2]);
    int use=std::atoi(argv[3]);
    for(auto& m:parents) {
        u64 a,b;
        if(!(std::cin>>a>>b)) return 2;
        m=(Mask(b)<<64)|a;
    }
    std::array<int,count> ranks{};
    
    // Input then supplies the orbit rank of each unordered pair (0,i).
    for(int i=1;i<count;++i) if(!(std::cin>>ranks[i])) return 2;
    for(int j=1; j<count; ++j) if(ranks[j]==j && (use<0 || j==use)) {
        int first_loss=bits(parents[0]&parents[j]);
        int pool[count],n=0;
        for(int i=1; i<count; ++i) if(i!=j) {
            int loss=bits(parents[0]&parents[i]);
            if(loss>first_loss || (loss==first_loss && ranks[i]>=j)) pool[n++]=i;
        }
        selected[0]=0;selected[1]=j;
        search(parents[0]|parents[j],26-first_loss,k-2,pool,n,2);
        if(found) break;
    }
    std::cout << k << " " << target << " " << found;
    for(int i=2;i<=k;++i) std::cout << " " << visits[i];
    std::cout << '\n';
}
