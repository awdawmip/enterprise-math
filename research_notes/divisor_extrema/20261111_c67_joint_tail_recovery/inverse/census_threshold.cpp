#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
using Count=std::uint64_t;
struct Edge {double a,b,h,det;bool flip;};
struct Tail {double px,py,qx,qy,det;};
struct Pair {double x,y;};
using Table=std::vector<std::vector<std::vector<Edge>>>;
static_assert(std::numeric_limits<double>::is_iec559 && std::numeric_limits<double>::digits==53);
class Search {
    const Table& table;
    const std::vector<Tail>& tails;
    double threshold;
    public:
    Count above=0,below=0,ambiguous=0;
    Search(const Table& tab,const std::vector<Tail>& ts,double t):table(tab),tails(ts),threshold(t){}
    void count(int r,int c,Pair lo,Pair hi,double det) {
        if(r==0) {
            const auto& t=tails[c];
            double left=(t.px*lo.x+t.py*lo.y),right=(t.qx*hi.x+t.qy*hi.y);
            double den=left*right*threshold,num=det*t.det;
            if(num>den*(1.0+0x1p-38)) ++above;
            else if(num<den*(1.0-0x1p-38)) ++below;
            else ++ambiguous;
            return;
        }
        for(int m=0;m<=c-2;++m) {
            auto& e=table[r][c][m];
            Pair l{e.a*(lo.x+lo.y),e.b*lo.x+e.h*lo.y};
            Pair h{e.a*(hi.x+hi.y),e.b*hi.x+e.h*hi.y};
            if(e.flip) count(r-1,c-m,h,l,det*e.det);
            else count(r-1,c-m,l,h,det*e.det);
        }
    }
};
int main(){
    int limit;double threshold;std::cin>>limit>>threshold;
    std::vector<Tail> tails(limit+2);
    for(int c=2;c<=limit+1;++c) {auto&t=tails[c];std::cin>>t.px>>t.py>>t.qx>>t.qy>>t.det;}
    Table tab(limit,std::vector<std::vector<Edge>>(limit+2));
    for(int r=1;r<limit;++r) for(int c=2;c<=limit+1;++c) for(int m=0;m<=c-2;++m){
        Edge e;std::cin>>e.a>>e.b>>e.h>>e.det>>e.flip;
        tab[r][c].push_back(e);
    }
    for(int k=2;k<=limit;++k) {
        Search s(tab,tails,threshold);
        for(int c=2;c<=k+1;++c) s.count(k-1,c,{0.,1.},{1.,0.},1.);
        std::cout<<k<<" "<<s.above<<" "<<s.below<<" "<<s.ambiguous<<"\n"<<std::flush;
    }
}
