#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using Mask=std::array<std::uint64_t,17>;
std::vector<Mask> masks(int q,std::vector<int> phases){
    std::vector<Mask> rows(q);
    for(int t=0;t<q;++t)for(int c:phases){
        int j=(c-t)%q;if(j<=0)j+=q;
        for(;j<=1028;j+=q)rows[t][(j-1)/64]|=std::uint64_t(1)<<((j-1)%64);
    }
    return rows;
}
int main(){
    auto a=masks(257,{0,88}),b=masks(271,{4,11,116}),c=masks(277,{78,97,243});
    int best=1029,ba=-1,bb=-1,bc=-1;long long count=0,hist[40]={};
    for(int i=0;i<257;++i)for(int j=0;j<271;++j){
        Mask ab;for(int w=0;w<17;++w)ab[w]=a[i][w]|b[j][w];
        for(int k=0;k<277;++k){
            int n=0;for(int w=0;w<17;++w)n+=__builtin_popcountll(ab[w]|c[k][w]);
            ++count;++hist[n];if(n<best){best=n;ba=i;bb=j;bc=k;}
        }
    }
    std::cout<<"{\"coordinate_tuples\":"<<count<<",\"minimum_union_size\":"<<best
             <<",\"alpha_maximum_for_three_period_subgraph\":"<<(1028-best+8)
             <<",\"minimizing_coordinates\":["<<ba<<","<<bb<<","<<bc<<"],\"union_size_histogram\":{";
    bool first=true;for(int n=0;n<40;++n)if(hist[n]){if(!first)std::cout<<",";first=false;std::cout<<"\""<<n<<"\":"<<hist[n];}
    std::cout<<"}}\n";
}
