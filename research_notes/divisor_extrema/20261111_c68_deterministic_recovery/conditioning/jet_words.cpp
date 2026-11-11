// Enumerate all m_0+...+m_{r-1} <= budget-r on the original word weights.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using Residue=std::uint64_t;
constexpr Residue prime=(Residue(1)<<61)-1;

void visit(const std::vector<Residue>& weights,int position,int remaining,Residue sum,
           std::vector<Residue>& out) {
    if(position==static_cast<int>(weights.size())) {
        out.push_back(sum);
        return;
    }
    for(int m=0;m<=remaining;++m) {
        visit(weights,position+1,remaining-m,sum,out);
        sum+=weights[position];
        if(sum>=prime)sum-=prime;
    }
}

int main() {
    int r,budget;
    while(std::cin>>r>>budget) {
        if(r<1 || budget<0)return 2;
        std::vector<Residue> weights(r),out;
        for(auto& value:weights) {
            if(!(std::cin>>value) || value>=prime)return 2;
        }
        visit(weights,0,budget,0,out);
        std::sort(out.begin(),out.end());
        const bool distinct=std::adjacent_find(out.begin(),out.end())==out.end();
        std::cout<<r<<" "<<out.size()<<" "<<distinct<<"\n";
    }
}
