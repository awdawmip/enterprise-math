#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <unordered_set>
#include <vector>

using U64=std::uint64_t;
using U128=__uint128_t;
constexpr U64 prime=(U64(1)<<61)-1;

U64 add_mod(U64 x,U64 y) {
    U64 sum=x+y;
    return sum>=prime ? sum-prime : sum;
}
U64 mul_mod(U64 x,U64 y) {
    U128 product=U128(x)*y;
    return add_mod(U64(product)&prime,U64(product>>61));
}
U64 inverse(U64 x) {
    assert(x);
    U64 result=1;
    for(U64 e=prime-2;e;e>>=1) {
        if(e&1) result=mul_mod(result,x);
        x=mul_mod(x,x);
    }
    return result;
}
struct Point {U64 x,y;};
struct Edge {
    U64 b,c,d;
    bool decreasing;
    int cost,stock,lower_cost;
    Point apply(Point p) const {
        return {mul_mod(b,p.y),add_mod(mul_mod(c,p.x),mul_mod(d,p.y))};
    }
};
struct Leaf {
    U64 a,b,g,h;
    std::pair<U64,U64> odds(Point p) const {
        return {add_mod(mul_mod(a,p.x),mul_mod(b,p.y)), add_mod(mul_mod(g,p.x),mul_mod(h,p.y))};
    }
};
using Layer=std::vector<std::vector<Edge>>;

class Search {
    const std::vector<Layer>& layers;
    const std::vector<Leaf>& leaves;
    const std::unordered_set<U64>& targets;
    std::array<U64,512> numerators,denominators,products;
    int total_pending=0;
    void flush() {
        if(!total_pending) return;
        U64 prod=1;
        for(int i=0;i<total_pending;++i) {
            products[i]=prod;
            prod=mul_mod(prod,denominators[i]);
        }
        U64 inv=inverse(prod);
        for(int i=total_pending-1;i>=0;--i) {
            U64 value=mul_mod(numerators[i],mul_mod(inv,products[i]));
            hits+=targets.count(value);
            inv=mul_mod(inv,denominators[i]);
        }
        total_pending=0;
    }
public:
    U64 prefixes=0,candidates=0,hits=0;
    Search(const std::vector<Layer>& layers,const std::vector<Leaf>& leaves,
           const std::unordered_set<U64>& targets):layers(layers),leaves(leaves),targets(targets){}
    void walk(int r,int c,Point x,Point y,bool flipped,int budget) {
        ++prefixes;
        if(r==0) {
            ++candidates;
            auto lx=leaves[c].odds(x), ly=leaves[c].odds(y);
            U64 num=mul_mod(ly.first,lx.second),den=mul_mod(lx.first,ly.second);
            if(flipped) std::swap(num,den);
            assert(num && den);
            numerators[total_pending]=num;
            denominators[total_pending]=den;
            if(++total_pending==512) flush();
            return;
        }
        for(const Edge& e:layers[r][c]) {
            if(e.lower_cost>budget) break;
            walk(r-1,e.stock,e.apply(x),e.apply(y),flipped!=e.decreasing,budget-e.cost);
        }
    }
    void finish(int k) {
        flush();
        std::cout<<k<<" "<<prefixes<<" "<<candidates<<" "<<hits<<"\n"<<std::flush;
    }
};

int main() {
    int mx; std::cin>>mx;
    std::vector<Leaf> leaves(mx+2);
    std::vector<Layer> layers(mx,Layer(mx+2));
    std::vector<std::vector<int>> min_cost(mx,std::vector<int>(mx+2));
    for(int c=2;c<=mx+1;++c) {
        auto& leaf=leaves[c];
        std::cin>>leaf.a>>leaf.b>>leaf.g>>leaf.h;
    }
    for(int r=1;r<mx;++r) for(int c=2;c<=mx+1;++c) {
        auto& list=layers[r][c];
        for(int m=0;m<=c-2;++m) {
            Edge e;std::cin>>e.b>>e.c>>e.d>>e.decreasing>>e.cost;
            e.stock=c-m;e.lower_cost=e.cost+min_cost[r-1][e.stock];
            list.push_back(e);
        }
        std::sort(list.begin(),list.end(),[](const Edge& a,const Edge& b){return a.lower_cost<b.lower_cost;});
        min_cost[r][c]=list.front().lower_cost;
    }
    int count;std::cin>>count;
    std::unordered_set<U64> targets;
    for(int i=0;i<count;++i) {U64 v;std::cin>>v;targets.insert(v);}
    int k,reference;
    while(std::cin>>k>>reference) {
        Search search(layers,leaves,targets);
        for(int stock=2;stock<=k+1;++stock) {
            int budget;std::cin>>budget;
            if(reference) budget=std::numeric_limits<int>::max();
            if(budget>=min_cost[k-1][stock])
                search.walk(k-1,stock,{0,1},{1,1},false,budget);
        }
        search.finish(k);
    }
}
