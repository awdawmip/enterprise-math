// R254 independent C++17 positive-integer dynamic validation.
// Mathematical six-axis affine subalgebra F(eps,k): diag(eps,eps,1,1,1,1)z+k*e1.
// Here stored coordinate p=-eps*k is the inverse anchor. No native module import.
#include <boost/multiprecision/cpp_int.hpp>
#include <map>
#include <tuple>
#include <vector>
#include <string>
#include <iostream>
#include <stdexcept>
#include <algorithm>
using boost::multiprecision::cpp_int;
using Key=std::tuple<int,int,int>; // control state, holonomy eps, anchor p
using Dist=std::map<Key,cpp_int>;
struct Edge {int target,eta,b;};
static const Edge edges[3][2]={
    {{2,-1,-1},{2, 1,-1}},
    {{0,-1,-1},{0, 1,-1}},
    {{1, 1, 1},{2, 1,-1}}
};
static void ensure(bool ok,const std::string &msg){if(!ok)throw std::runtime_error(msg);}
static Key next_key(Key s,int branch){
    auto [q,eps,p]=s;
    auto e=edges[q][branch];
    const int eps2=eps*e.eta;
    return {e.target,eps2,p-eps2*e.b};
}
static Dist step(const Dist &in){
    Dist out;
    for(const auto &[key,count]:in){
        for(int branch=0;branch<2;++branch){out[next_key(key,branch)]+=count;}
    }
    return out;
}
static cpp_int central(int m){
    cpp_int c=1;
    for(int j=1;j<=m/2;++j)c=c*(m-j+1)/j;
    return c;
}
static cpp_int pw2(int m){cpp_int n=1;return n<<m;}
static int bits_needed(cpp_int x){
    ensure(x>=1,"multiplicity must be >= 1");
    // ceil(log2(x)) = bit_length(x-1)
    --x;
    int bits=0;
    while(x>0){x>>=1;++bits;}
    return bits;
}
static Dist brute(int src,int m){
    Dist out;
    cpp_int lim=pw2(m);
    ensure(m<=12,"brute only through 12");
    for(unsigned long long mask=0;mask<(1ULL<<m);++mask){
        Key s={src,1,0};
        for(int pos=m-1;pos>=0;--pos)s=next_key(s,int((mask>>pos)&1ULL));
        out[s]++;
    }
    return out;
}
int main(){
    try{
        const std::vector<int> chosen={0,1,2,3,8,12,24,40,48,64,96};
        Dist d[2] = {{{Key{0,1,0},cpp_int(1)}},{{Key{1,1,0},cpp_int(1)}}};
        std::cout<<"{\"status\":\"PASS\",\"verified_depth\":96,\"native_source_executed\":false,\"selected\":[";
        bool first=true;
        for(int m=0;m<=96;++m){
            cpp_int C=central(m);
            for(int j=0;j<2;++j){
                cpp_int total=0,M=0;
                std::map<int,cpp_int> anchor;
                for(const auto &[key,count]:d[j]){
                    auto [q,eps,p]=key;
                    ensure(q>=0 && q<3 && (eps==1||eps==-1),"invalid internal state");
                    ensure(std::abs(p)<=m && ((p-m)%2)==0,"invalid anchor parity/support");
                    total+=count;
                    anchor[p]+=count;
                    if(M<count)M=count;
                }
                ensure(total==pw2(m),"paths total mismatch");
                cpp_int all=0;
                for(int p=-m;p<=m;p+=2){
                    cpp_int ex=1;
                    int r=(m+p)/2;
                    for(int h=1;h<=r;++h)ex=ex*(m-h+1)/h;
                    ensure(anchor[p]==ex,"anchor marginal mismatch");
                    all+=ex;
                }
                ensure(all==total,"anchor total mismatch");
                ensure(M<=C && 6*M>=C,"central-fiber theorem violated");
                if(m<=12)ensure(brute(j,m)==d[j],"brute enumeration mismatch");
                if(j==0 && std::find(chosen.begin(),chosen.end(),m)!=chosen.end()){
                    if(!first)std::cout<<",";
                    std::cout<<"{\"m\":"<<m<<",\"max_fiber\":\""<<M
                             <<"\",\"central_binomial\":\""<<C
                             <<"\",\"tag_bits\":"<<bits_needed(M)<<"}";
                    first=false;
                }
            }
            if(m<96){d[0]=step(d[0]);d[1]=step(d[1]);}
        }
        auto x=brute(0,3);
        ensure(x.at(Key{0,1,1})==2,"expected path collision at inverse anchor +1");
        for(int m=0;m<=2;++m){for(const auto &[s,c]:brute(0,m))ensure(c==1,"early collision");}
        std::cout<<"],\"first_collision_depth\":3}"<<std::endl;
    }catch(const std::exception &ex){
        std::cerr<<"FAIL: "<<ex.what()<<std::endl;return 1;
    }
}
