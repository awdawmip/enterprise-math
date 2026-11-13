// Exact modular certificate for all landing stocks v, one visible block.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using U=std::uint64_t;
const U p=(U(1)<<61)-1;
U add(U a,U b){U s=a+b;return s>=p?s-p:s;}
U mul(U a,U b){
    __uint128_t product=__uint128_t(a)*b;
    return add(U(product)&p,U(product>>61));
}
U inv(U x){
    assert(x && x<p); U acc=1;
    for(U n=p-2;n;n>>=1,x=mul(x,x)) if(n&1) acc=mul(acc,x);
    return acc;
}
U frac(U n,U d){return mul(n,inv(d));}
void batch_inverse(std::vector<U>& v){
    std::vector<U> prefix(v.size()+1,1);
    for(size_t i=0;i<v.size();++i){assert(v[i]);prefix[i+1]=mul(prefix[i],v[i]);}
    U last=inv(prefix.back());
    for(size_t i=v.size();i-->0;){U old=v[i];v[i]=mul(last,prefix[i]);last=mul(last,old);}
}

int main(int argc,char** argv){
    if(argc<2 || argc>3) return 2;
    const int cap=std::stoi(argv[1]);
    const bool dump=argc==3;
    std::vector<std::array<U,3>> tails(cap+1);
    std::vector<U> step_rho(cap+1),step_tau(cap+1);
    const std::array<U,3> u{frac(3,32),frac(3,2),6}, b{frac(15,32),frac(15,8),3};
    U y=1,words=0,columns=0;
    for(int v=2;v<=cap;++v){
        if(v>2)y=mul(y,frac(4*v+1,4*v+4));
        U x=frac(840,mul(U(v+2)*(v+3),v+4));
        for(int j=0;j<3;++j)
            tails[v][j]=frac(mul(y,add(mul(x,u[j]),b[j])),add(1,mul(mul(x,u[j]),y)));
        step_rho[v]=frac(4*v-1,4*v+8);
        step_tau[v]=frac(mul(U(4*v-1)*(v+2),4*v-2),mul(U(4)*(v+11)*(4*v+2),v+1));
    }
    std::vector<U> n,d,sig,pairs;
    std::vector<std::pair<U,int>> cols;
    for(int c=2;c<=cap;++c){
        n.clear();d.clear();pairs.clear();cols.clear();sig.clear();
        U rho=frac(3+4*c,3+c),tau=frac(U(28)*(4*c+3)*(4*c+2),U(c+12)*(c+2));
        for(int v=c;v>=2;--v){
            for(int j=0;j<3;++j){
                U tz=mul(tau,tails[v][j]);
                n.push_back(add(rho,tz));d.push_back(add(1,tz));
            }
            rho=mul(rho,step_rho[v]);tau=mul(tau,step_tau[v]);
        }
        batch_inverse(d);
        for(size_t i=0;i<n.size();++i){n[i]=mul(n[i],d[i]);assert(n[i]);}
        for(int v=c;v>=2;--v){
            size_t i=3*(c-v);
            for(int j=0;j<3;++j)cols.emplace_back(n[i+j],v);
            U a=n[i],b=n[i+(v<=3?1:2)];
            pairs.push_back(mul(a,b));sig.push_back(add(mul(a,a),mul(b,b)));
        }
        batch_inverse(pairs);
        for(size_t i=0;i<sig.size();++i)sig[i]=mul(sig[i],pairs[i]);
        if(dump){
            for(int v=c;v>=2;--v){
                size_t k=c-v;
                std::cout<<c<<' '<<v<<' '<<n[3*k]<<' '<<n[3*k+1]<<' '<<n[3*k+2]<<' '<<sig[k]<<'\n';
            }
        }
        std::sort(cols.begin(),cols.end());std::sort(sig.begin(),sig.end());
        for(size_t i=1;i<cols.size();++i)assert(cols[i-1].first!=cols[i].first || cols[i-1].second==cols[i].second);
        assert(std::adjacent_find(sig.begin(),sig.end())==sig.end());
        words+=c-1;columns+=cols.size();
    }
    if(!dump)std::cout<<cap<<' '<<words<<' '<<columns<<'\n';
}
