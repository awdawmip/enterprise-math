#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using U=std::uint64_t;
using Wide=__uint128_t;
constexpr U prime=(U{1}<<61)-1;

U add(U a,U b) {U v=a+b;return v>=prime?v-prime:v;}
U mul(U a,U b) {
    Wide v=Wide(a)*b;
    return add(U(v)&prime,U(v>>61));
}
U inverse(U a) {
    assert(a!=0);
    U x=1;
    for(U p=prime-2;p;p>>=1) {if(p&1)x=mul(x,a);a=mul(a,a);}
    return x;
}
U ratio(U a,U b) {return mul(a,inverse(b));}

struct Pair {U low,high;};
struct Block {U rho,tau;};

std::vector<std::vector<Block>> blocks(int k,int limit) {
    std::vector<std::vector<Block>> table(limit+1);
    for(int stock=2;stock<=limit;stock++) {
        auto& row=table[stock];
        row.resize(stock+1);
        U rho=ratio(k+4*stock,k+stock);
        U tau=mul(28,ratio((k+4*stock)*U(k-1+4*stock),(4*k+stock)*U(k-1+stock)));
        row[stock]={rho,tau};
        if(stock>2) {
            U f=ratio(k+4*stock,4*(k+stock)),g=ratio(k+4*stock,4*(4*k+stock));
            for(int v=2;v<stock;v++) {
                auto prev=table[stock-1][v];
                row[v]={mul(f,prev.rho),mul(g,prev.tau)};
            }
        }
    }
    return table;
}

std::vector<Pair> terminal_points(int limit) {
    U y=1;
    std::vector<Pair> result(limit+1);
    constexpr int A[]={3,48,192},B[]={15,60,96};
    for(int v=2;v<=limit;v++) {
        if(v>2)y=mul(y,ratio(4*v+1,4*v+4));
        const U d=U(v+2)*(v+3)*(v+4);
        auto z=[&](int i){return ratio(mul(y,add(840*A[i],mul(d,B[i]))),add(mul(32,d),mul(840*A[i],y)));};
        result[v]={z(0),z(v<4?1:2)};
    }
    return result;
}

std::vector<U> batch(const std::vector<U>& nums,const std::vector<U>& den) {
    size_t n=nums.size();
    std::vector<U> products(n+1,1),out(n);
    for(size_t i=0;i<n;i++)products[i+1]=mul(products[i],den[i]);
    U acc=inverse(products[n]);
    for(size_t i=n;i>0;) {
        --i;out[i]=mul(nums[i],mul(acc,products[i]));
        acc=mul(acc,den[i]);
    }
    return out;
}

std::vector<std::vector<Pair>> children(const std::vector<std::vector<Block>>& map,
                                       const std::vector<Pair>& terminal,int limit) {
    std::vector<std::vector<Pair>> result(limit+1);
    for(int v=2;v<=limit;v++) {
        std::vector<U> nums,den;
        for(int w=2;w<=v;w++) for(U z:{terminal[w].low,terminal[w].high}) {
            auto b=map[v][w];U q=mul(b.tau,z);
            nums.push_back(add(b.rho,q));den.push_back(add(1,q));
        }
        auto points=batch(nums,den);
        for(size_t j=0;j<points.size();j+=2)result[v].push_back({points[j],points[j+1]});
    }
    return result;
}

int main(int argc,char**argv) {
    int limit=argc>1?std::atoi(argv[1]):1080;
    if(limit<2 || limit>10000)return 2;
    auto after=children(blocks(3,limit),terminal_points(limit),limit);
    auto first=blocks(5,limit);
    for(int c=2;c<=limit;c++) {
        std::vector<U> values;
        values.reserve(U(c)*(c-1)/2);
        for(int v=2;v<=c;v++) {
            auto b=first[c][v];
            std::vector<U> nums,den;
            for(auto pt:after[v]) {
                U l=mul(b.tau,pt.low),h=mul(b.tau,pt.high);
                U x=mul(add(l,b.rho),add(h,1)), y=mul(add(h,b.rho),add(l,1));
                nums.push_back(add(mul(x,x),mul(y,y)));den.push_back(mul(x,y));
            }
            auto row=batch(nums,den);
            values.insert(values.end(),row.begin(),row.end());
        }
        std::sort(values.begin(),values.end());
        if(std::adjacent_find(values.begin(),values.end())!=values.end()) {
            std::cerr<<"Ambiguous residue at stock "<<c<<"\n";return 1;
        }
        std::cout<<c<<" "<<values.size()<<" "<<values.front()<<" "<<values.back()<<"\n";
    }
}
