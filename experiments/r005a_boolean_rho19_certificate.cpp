#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using i64 = std::int64_t;

static i64 cyclic_unit_gap_from_factors(i64 modulus, const std::vector<int>& factors) {
    std::vector<unsigned char> unit((size_t)modulus,1);
    for(int p:factors) for(i64 n=0;n<modulus;n+=p) unit[(size_t)n]=0;
    i64 first=-1,prev=-1,best=0;
    for(i64 n=0;n<modulus;++n) if(unit[(size_t)n]){
        if(first<0) first=n;
        if(prev>=0) best=std::max(best,n-prev);
        prev=n;
    }
    assert(first>=0);
    return std::max(best,modulus+first-prev);
}

static std::pair<i64,i64> separator_gap_count(
    i64 Q, i64 d, const std::vector<int>& relevant_positions
) {
    i64 first=-1,prev=-1,best=0,count=0;
    for (int ni : relevant_positions) {
        i64 n=ni, nd=n+d; if(nd>=Q) nd-=Q;
        bool u=(n%17!=0 && n%19!=0);
        bool v=(nd%17!=0 && nd%19!=0);
        if(u==v) continue;
        ++count;
        if(first<0) first=n;
        if(prev>=0) best=std::max(best,n-prev);
        prev=n;
    }
    assert(first>=0);
    best=std::max(best,Q+first-prev);
    return {best,count};
}

int main(){
    // Fixed theorem instance P={2,3,5,7,11,13,17,19}; no prime enumerator is owned here.
    const std::vector<int> P={2,3,5,7,11,13,17,19};
    i64 Q=1; for(int q:P) Q*=q;
    assert(Q==9699690);
    const i64 candidate_gap=366;

    // Jacobsthal branch-and-bound: if q*j(Q/q) <= candidate_gap, any improving
    // shift must keep that q-coordinate fixed and hence be divisible by q.
    i64 forced_divisor=1;
    std::vector<std::pair<int,i64>> qj;
    for(int q:P){
        std::vector<int> factors; for(int r:P) if(r!=q) factors.push_back(r);
        i64 j=cyclic_unit_gap_from_factors(Q/q,factors);
        qj.push_back({q,q*j});
        if(q*j<=candidate_gap) forced_divisor*=q;
    }
    assert((qj==std::vector<std::pair<int,i64>>{{2,34},{3,54},{5,110},{7,154},{11,264},{13,338},{17,442},{19,494}}));
    assert(forced_divisor==30030);

    // After pruning only 17 and 19 coordinates can change. Mismatch positions
    // must already be units modulo the fixed-coordinate modulus 30030.
    std::vector<unsigned char> base_unit((size_t)forced_divisor,1);
    for(int q: {2,3,5,7,11,13}) for(int r=0;r<forced_divisor;r+=q) base_unit[(size_t)r]=0;
    std::vector<int> residues; for(int r=0;r<forced_divisor;++r) if(base_unit[(size_t)r]) residues.push_back(r);
    assert(residues.size()==5760);
    std::vector<int> relevant; relevant.reserve((Q/forced_divisor)*residues.size());
    for(i64 block=0; block<Q/forced_divisor; ++block)
        for(int r:residues) relevant.push_back((int)(block*forced_divisor+r));
    assert(relevant.size()==1860480);

    i64 best_gap=0,best_d=0,best_count=0;
    for(i64 k=1;k<Q/forced_divisor;++k){
        i64 d=k*forced_divisor;
        auto [gap,count]=separator_gap_count(Q,d,relevant);
        if(gap>best_gap){best_gap=gap;best_d=d;best_count=count;}
    }
    assert(best_gap==366);
    assert(best_d==4564560 || best_d==Q-4564560);
    assert(std::gcd(best_d,Q)==Q/17);
    assert(best_count==207360);

    // The sparsest largest-prime-only family has fewer mismatches but a smaller radius.
    i64 sparse_best=0;
    for(int c=1;c<19;++c){
        i64 d=(Q/19)*c;
        auto [gap,count]=separator_gap_count(Q,d,relevant);
        assert(count==184320);
        sparse_best=std::max(sparse_best,gap);
    }
    assert(sparse_best==342);

    std::cout<<"rho19 exact: gap="<<best_gap<<" rho="<<best_gap-1
             <<" d="<<best_d<<" mismatch_count="<<best_count
             <<" sparse_q19_gap="<<sparse_best<<"\n";
}
