// Exact weighted covers on point orbits of the central inversion.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using Mask = std::uint64_t;
using Count = std::uint64_t;
struct Row { Mask bits; int type; int multiplicity; };
using Rows = std::vector<Row>;
std::vector<int> quotas;
Count nodes;

int first(Mask bits) { return __builtin_ctzll(bits); }
Count covers(Mask free, int depth, const Rows& candidates) {
    ++nodes;
    if(depth==1) {
        Count total=0;
        for(const auto& row:candidates) {
            if(quotas[row.type] && row.bits==free) total+=row.multiplicity;
        }
        return total;
    }
    Rows valid;
    std::array<int,63> through{};
    std::vector<int> by_type(quotas.size());
    Mask united=0;
    for(auto row:candidates) {
        if(!quotas[row.type] || (row.bits&free)!=row.bits) continue;
        valid.push_back(row);
        united|=row.bits;
        ++by_type[row.type];
        for(Mask v=row.bits;v;v&=v-1) ++through[first(v)];
    }
    if(united!=free)return 0;
    int minimum=valid.size()+1,anchor=-1,point=-1;
    for(int t=0;t<(int)quotas.size();++t) {
        if(by_type[t]<quotas[t]) return 0;
        if(quotas[t]==1 && by_type[t]<minimum) {
            minimum=by_type[t]; anchor=t;
        }
    }
    for(Mask v=free;v;v&=v-1) {
        const int i=first(v);
        if(through[i]<minimum) {minimum=through[i]; point=i; anchor=-1;}
    }
    Count total=0;
    for(auto row:valid) {
        if(anchor>=0 ? row.type!=anchor : !(row.bits>>point & 1))continue;
        --quotas[row.type];
        total+=row.multiplicity*covers(free^row.bits,depth-1,valid);
        ++quotas[row.type];
    }
    return total;
}
int main() {
    int types;
    std::cin>>types;
    Rows inventory;
    for(int t=0;t<types;++t) {
        int n;
        std::cin>>n;
        for(int k=0;k<n;++k) {
            Mask bits;int mult;
            std::cin>>bits>>mult;
            inventory.push_back({bits,t,mult});
        }
    }
    int jobs;
    std::cin>>jobs;
    quotas.resize(types);
    for(int j=0;j<jobs;++j) {
        int cost,depth=0;Mask free;unsigned weight;
        std::cin>>cost>>free>>weight;
        for(int &t:quotas){std::cin>>t; depth+=t;}
        nodes=0;
        auto count=covers(free,depth,inventory);
        std::cout<<cost<<" "<<weight*count<<" "<<nodes<<std::endl;
    }
}
