#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <string>
#include <iostream>
#include <utility>
#include <vector>
#include <gmpxx.h>

using Z=mpz_class;
using Count=std::uint64_t;
constexpr int bits=100;
struct Range {Z lo,hi;};
struct Matrix {Z a,b,h,d;Z det;bool increasing;};
struct Edge {Matrix M;Range image;};
struct Cell {Range span,width;std::vector<Edge> edges;std::pair<mpq_class,mpq_class> ends;};
struct Node {int r,c;Matrix M;Range span,width;};
struct Counts {Count split=0,exact=0,depth=0;};
std::vector<std::vector<Cell>> table;

Z down(const Z& a,const Z& b){assert(b>0);Z out;mpz_fdiv_q(out.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());return out;}
Z up(const Z& a,const Z& b){assert(b>0);Z out;mpz_cdiv_q(out.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());return out;}
bool disjoint(const Range& a,const Range& b){return a.hi<b.lo||b.hi<a.lo;}

Matrix compose(const Matrix& x,const Matrix& y) {
    return {x.a*y.a+x.b*y.h,x.a*y.b+x.b*y.d,x.h*y.a+x.d*y.h,x.h*y.b+x.d*y.d,
        x.det*y.det,x.increasing==y.increasing};
}
Range map_range(const Matrix& m,const Range& q) {
    const Z &l=m.increasing?q.lo:q.hi, &u=m.increasing?q.hi:q.lo;
    return {down((m.a*l+(m.b<<bits))<<bits,m.h*l+(m.d<<bits)),
            up((m.a*u+(m.b<<bits))<<bits,m.h*u+(m.d<<bits))};
}
Node node(int r,int c,Matrix m) {
    auto &cell=table[r][c];
    auto span=map_range(m,cell.span);
    const Z left=m.h*cell.span.lo+(m.d<<bits),right=m.h*cell.span.hi+(m.d<<bits);
    const Z num=m.det<<(2*bits);
    Range width{down(cell.width.lo*num,right*right),up(cell.width.hi*num,left*left)};
    return {r,c,std::move(m),std::move(span),std::move(width)};
}
std::pair<mpq_class,mpq_class> leaf(const Node& n) {
    auto eval=[&](mpq_class z)->mpq_class {
        return (n.M.a*z+n.M.b)/(n.M.h*z+n.M.d);
    };
    auto [x,y]=table[0][n.c].ends;
    auto a=eval(x), b=eval(y);
    return a<=b?std::make_pair(a,b):std::make_pair(b,a);
}
Range inverse_clip(const Node& u,const Range& target) {
    const auto& m=u.M;
    const Z& L=target.lo;const Z& H=target.hi;
    Range cut=table[u.r][u.c].span;
    // Exact real preimage inequalities on the dyadic grid, rounded outwards.
    if(m.increasing) {
        if(L>u.span.lo) {
            Z a=(m.a<<bits)-m.h*L;
            if(a<=0)return {1,0};
            Z v=down((m.d*L-(m.b<<bits))<<bits,a);
            if(v>cut.lo)cut.lo=std::move(v);
        }
        if(H<u.span.hi) {
            Z a=(m.a<<bits)-m.h*H;
            if(a>0) {
                Z v=up((m.d*H-(m.b<<bits))<<bits,a);
                if(v<cut.hi)cut.hi=std::move(v);
            }
        }
    } else {
        if(H<u.span.hi) {
            Z a=m.h*H-(m.a<<bits);
            if(a<=0)return {1,0};
            Z v=down(((m.b<<bits)-m.d*H)<<bits,a);
            if(v>cut.lo)cut.lo=std::move(v);
        }
        if(L>u.span.lo) {
            Z a=m.h*L-(m.a<<bits);
            if(a>0) {
                Z v=up(((m.b<<bits)-m.d*L)<<bits,a);
                if(v<cut.hi)cut.hi=std::move(v);
            }
        }
    }
    return cut;
}
void search(const Node& x,const Node& y,int r0,Counts& stats) {
    if(disjoint(x.span,y.span)||disjoint(x.width,y.width))return;
    const Z required=std::max(x.width.lo,y.width.lo);
    const Z overlap=std::min(x.span.hi,y.span.hi)-std::max(x.span.lo,y.span.lo);
    if(required>(overlap<<(512-bits)))return;
    if(!x.r&&!y.r) {
        ++stats.exact;
        if(leaf(x)==leaf(y)){std::cerr<<"Equal leaf pair\n";std::exit(2);}
        return;
    }
    ++stats.split;
    stats.depth=std::max(stats.depth,Count(r0-std::min(x.r,y.r)));
    bool swap=!x.r || (y.r && y.span.hi-y.span.lo>x.span.hi-x.span.lo);
    const Node& u=swap?y:x;const Node& v=swap?x:y;
    Range cut=inverse_clip(u,v.span);
    if(cut.lo>cut.hi)return;
    // Check each precomputed one-edge local cylinder before building its prefix matrix.
    const auto& options=table[u.r][u.c].edges;
    for(size_t i=0;i<options.size();i++) {
        const auto& e=options[i];
        if(disjoint(e.image,cut))continue;
        auto child=node(u.r-1,u.c-int(i),compose(u.M,e.M));
        search(child,v,r0,stats);
    }
}
Range grid(mpq_class z,int shift) {
    const Z value=z.get_num()<<shift;
    return {down(value,z.get_den()),up(value,z.get_den())};
}
Count control(int r,int c) {
    Count checked=0;
    for(unsigned seed=1;seed<=9;seed++) {
        unsigned state=seed*1234567u;
        int v=c;
        Matrix combined{1,0,0,1,1,true};
        std::vector<Node> chain;
        std::vector<int> digits;
        for(int j=r;j>0;j--) {
            chain.push_back(node(j,v,combined));
            state=1664525u*state+1013904223u;
            int m=seed==1?0:(seed==2?v-2:(seed==3?(j==1?v-2:0):int(state%unsigned(v-1))));
            digits.push_back(m);
            combined=compose(combined,table[j][v].edges[m].M);
            v-=m;
        }
        auto actual=leaf(node(0,v,combined));
        auto left=grid(actual.first,bits),right=grid(actual.second,bits);
        auto width=grid(actual.second-actual.first,512);
        for(size_t i=0;i<chain.size();i++) {
            const auto& n=chain[i];
            assert(n.span.lo<=left.lo && n.span.hi>=right.hi);
            assert(n.width.lo<=width.lo && n.width.hi>=width.hi);
            const auto& image=table[n.r][n.c].edges[digits[i]].image;
            for(const auto& b:{left,right}) {
                const auto cut=inverse_clip(n,b);
                assert(cut.lo<=cut.hi && !disjoint(image,cut));
                ++checked;
            }
        }
    }
    return checked;
}
int main(int argc,char**argv) {
    int cap,start,maxr;std::cin>>cap>>start>>maxr;
    if(start<3 || start>cap || maxr!=cap-2)return 3;
    table.resize(cap+1,std::vector<Cell>(cap+1));
    for(int r=0;r<=maxr;r++)for(int c=2;c<=cap;c++) {
        auto& z=table[r][c];
        std::cin>>z.span.lo>>z.span.hi>>z.width.lo>>z.width.hi;
        if(!r){std::cin>>z.ends.first>>z.ends.second;continue;}
        for(int m=0;m<=c-2;m++) {
            Edge e;auto& q=e.M;
            std::cin>>q.a>>q.b>>q.h>>q.d;
            Z det=q.a*q.d-q.b*q.h;
            assert(det!=0);
            q.increasing=det>0;q.det=abs(det);
            e.image=map_range(q,table[r-1][c-m].span);
            z.edges.push_back(std::move(e));
        }
    }
    assert(std::cin.good());
    int r,c;
    while(std::cin>>r>>c) {
        if(argc==2 && std::string(argv[1])=="--controls"){
            std::cout<<r<<" "<<c<<" "<<control(r,c)<<"\n";continue;
        }
        std::vector<Node> roots;
        for(int m=0;m<=c-2;m++)roots.push_back(node(r-1,c-m,table[r][c].edges[m].M));
        Counts count;
        for(size_t i=0;i<roots.size();i++)for(size_t j=0;j<i;j++)search(roots[i],roots[j],r,count);
        std::cout<<r<<" "<<c<<" "<<count.split<<" "<<count.exact<<" "<<count.depth<<"\n"<<std::flush;
    }
}
