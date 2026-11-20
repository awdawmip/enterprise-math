// Fix a symmetry type and the first large class orbit. Cover every class of size
// at least eleven in descending size order. The tail is saved as an unrestricted
// exact-cover problem on the remaining histories with a maximum class size of ten.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using Mask = __uint128_t;
using Word = uint64_t;
constexpr int Impossible=1000000;
constexpr Mask All=(Mask(1)<<125)-1;
const int single_minimum[]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};

int first(Mask m) {
    return Word(m)?__builtin_ctzll(Word(m)):64+__builtin_ctzll(Word(m>>64));
}
int cardinality(Mask m) {
    return __builtin_popcountll(Word(m))+__builtin_popcountll(Word(m>>64));
}
int action[125],budget;
Mask fixed_plane=0;
Mask transform(Mask m) {
    Mask out=0;
    for(;m;m&=m-1) out|=Mask(1)<<action[first(m)];
    return out;
}
struct Orbit {
    Mask support;
    int labels,size,cost,fixed;
};
std::vector<Orbit> by_size[14];
std::ofstream tails;
long long nodes[14],residuals;
int bound[14][12][126][26][3];

int lower(int max_size,int k,int points,int fixed,int thirteens) {
    if(std::min({k,points,fixed,thirteens})<0 || points<fixed || points>max_size*k)
        return Impossible;
    return bound[max_size][k][points][fixed][thirteens];
}
void cover(Mask free,int k,int n,int h,int thirteens,int spent,int size,size_t start,
           const std::vector<Orbit>* family=nullptr) {
    ++nodes[size];
    if(k==0) {
        if(!free) { std::cerr<<"Full feasible cover at "<<spent<<"\n"; std::exit(3); }
        return;
    }
    if(spent+lower(size,k,n,h,thirteens)>budget) return;
    if(size<11) {
        ++residuals;
        tails<<Word(free)<<" "<<Word(free>>64)<<" "<<k<<" "<<spent<<"\n";
        return;
    }
    if(n<=(size-1)*k) cover(free,k,n,h,thirteens,spent,size-1,0);
    std::vector<Orbit> filtered;
    if(!family) {
        for(const auto& r:by_size[size]) {
            if(r.labels>k || (r.support&~free)) continue;
            int t=thirteens-(size==13?r.labels:0);
            if(spent+r.cost+lower(size,k-r.labels,n-r.labels*size,h-r.fixed,t)<=budget)
                filtered.push_back(r);
        }
        family=&filtered;
        start=0;
    }
    for(size_t i=start;i<family->size();i++) {
        const auto& r=(*family)[i];
        if(r.labels>k || (r.support&~free)) continue;
        int t=thirteens-(size==13?r.labels:0);
        if(spent+r.cost+lower(size,k-r.labels,n-r.labels*size,h-r.fixed,t)>budget) continue;
        cover(free^r.support,k-r.labels,n-r.labels*size,h-r.fixed,t,spent+r.cost,size,i+1,family);
    }
}

int main(int argc,char**argv) {
    if(argc!=7) return 2;
    std::ifstream perm(argv[1]),anchors(argv[4]);
    for(int i=0;i<125;i++) {
        perm>>action[i];
        if(action[i]==i) fixed_plane|=Mask(1)<<i;
    }
    const int total_fixed=cardinality(fixed_plane);
    budget=std::stoi(argv[5]);
    tails.open(argv[6]);
    std::map<std::array<int,3>,int> min_cost;
    for(int r:{1,2}) {
        std::ifstream f(argv[1+r]);
        int size,h,cost;Word a,b;
        while(f>>size>>h>>cost>>a>>b) {
            std::array<int,3> key={r,size,h};
            if(!min_cost.count(key) || min_cost[key]>r*cost) min_cost[key]=r*cost;
            if(size<11) continue;
            Mask seed=(Mask(b)<<64)|a;
            Mask q=(r==1?seed:(seed|transform(seed)));
            by_size[size].push_back({q,r,size,r*cost,h});
        }
    }
    for(int s=1;s<=10;s++) min_cost[{2,s,0}]=2*single_minimum[s];
    for(int s=1;s<=13;s++) {
        std::sort(by_size[s].begin(),by_size[s].end(),[](Orbit a,Orbit b) {
            if(a.labels!=b.labels) return a.labels>b.labels;
            if(a.cost!=b.cost) return a.cost<b.cost;
            return a.support<b.support;
        });
        for(int n=0;n<=125;n++) for(int h=0;h<=total_fixed;h++) for(int t=0;t<=2;t++)
            bound[s][0][n][h][t]=(n||h)?Impossible:0;
        for(int k=1;k<=11;k++) for(int n=0;n<=125;n++)
            for(int h=0;h<=total_fixed;h++) for(int t=0;t<=2;t++) {
                auto& best=bound[s][k][n][h][t];
                best=Impossible;
                for(auto [key,price]:min_cost) {
                    auto[r,size,d]=key;
                    int u=size==13?r:0;
                    if(size<=s && r<=k && r*size<=n && d<=h && u<=t)
                        best=std::min(best,price+bound[s][k-r][n-r*size][h-d][t-u]);
                }
            }
    }
    std::set<std::pair<Mask,int>> reps;
    int r;Word a,b;
    while(anchors>>r>>a>>b) reps.insert({(Mask(b)<<64)|a,r});
    int id=0;
    for(int s:{13,12}) for(const auto& x:by_size[s]) {
        if(!reps.count({x.support,x.labels})) continue;
        std::fill(std::begin(nodes),std::end(nodes),0);
        residuals=0;
        cover(All^x.support,11-x.labels,125-x.labels*s,total_fixed-x.fixed,
              2-(s==13?x.labels:0),x.cost,s,0);
        std::cout<<id++<<" "<<s<<" "<<x.labels<<" "<<residuals;
        for(int i=10;i<=13;i++) std::cout<<" "<<nodes[i];
        std::cout<<"\n";
    }
}
