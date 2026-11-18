#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using I = std::int64_t;
using W = __int128_t;
using Point = std::array<I,2>;

struct Event {
    I x;
    int l, r, delta;
    bool operator<(const Event& other) const { return x < other.x; }
};

std::string decimal(W value) {
    if (value == 0) return "0";
    std::string result;
    while (value > 0) {
        result.push_back(char('0'+value%10));
        value /= 10;
    }
    std::reverse(result.begin(),result.end());
    return result;
}

struct Node {
    int cover=0;
    std::array<I,3> length{};
};

class Coverage {
    const std::vector<I>& ys;
    std::vector<Node> tree;

    void pull(int node, int l, int r) {
        int base=tree[node].cover;
        for (int k=0;k<=2;++k) {
            I len=0;
            if (k>=base) {
                if (r-l==1) len=(k==base ? ys[r]-ys[l]:0);
                else len=tree[2*node].length[k-base]+tree[2*node+1].length[k-base];
            }
            tree[node].length[k]=len;
        }
    }
    void init(int node, int l, int r) {
        if (r-l>1) {
            int m=(l+r)/2;
            init(2*node,l,m);
            init(2*node+1,m,r);
        }
        pull(node,l,r);
    }
    void modify(int node, int l, int r, int a, int b, int delta) {
        if (a<=l && r<=b) tree[node].cover+=delta;
        else {
            int m=(l+r)/2;
            if (a<m) modify(2*node,l,m,a,b,delta);
            if (m<b) modify(2*node+1,m,r,a,b,delta);
        }
        pull(node,l,r);
    }
public:
    explicit Coverage(const std::vector<I>& y):ys(y),tree(y.size()*4) {
        init(1,0,ys.size()-1);
    }
    void modify(const Event& e) { modify(1,0,ys.size()-1,e.l,e.r,e.delta); }
    I length(int k) const { return tree[1].length[k]; }
};

// Mark every point with a preceding neighbor in an open square of radius width.
// The second pass reverses the x order to account for every following neighbor.
void mark_directed(const std::vector<Point>& pts,I width,std::vector<bool>& hit,bool reverse) {
    std::multiset<I> ys;
    int n=pts.size(), first=0;
    auto idx=[&](int i){ return reverse?n-1-i:i; };
    for(int j=0;j<n;++j) {
        auto q=pts[idx(j)];
        while(first<j && std::abs(q[0]-pts[idx(first)][0])>=width) {
            ys.erase(ys.find(pts[idx(first)][1]));
            ++first;
        }
        auto pos=ys.upper_bound(q[1]-width);
        if(pos!=ys.end() && *pos<q[1]+width) hit[idx(j)]=true;
        ys.insert(q[1]);
    }
}

int robust(const std::vector<Point>& pts,I width) {
    std::vector<bool> hit(pts.size());
    for(bool reverse:{false,true}) mark_directed(pts,width,hit,reverse);
    return std::count(hit.begin(),hit.end(),false);
}

int main(int argc, char** argv) {
    bool axial=argc==2 && std::string(argv[1])=="--axis-jumps";
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    I unit, error;
    if (!(std::cin>>n>>unit>>error) || n<1 || error<0 || 2*error>=unit) return 1;
    std::vector<Point> pts(n);
    std::vector<I> ys;
    for(auto &q:pts) {
        if (!(std::cin>>q[0]>>q[1])) return 1;
        ys.push_back(q[1]); ys.push_back(q[1]+unit);
    }
    std::sort(ys.begin(),ys.end());
    ys.erase(std::unique(ys.begin(),ys.end()),ys.end());
    std::vector<Event> ev;
    for(auto [x,y]:pts) {
        int l=std::lower_bound(ys.begin(),ys.end(),y)-ys.begin();
        int r=std::lower_bound(ys.begin(),ys.end(),y+unit)-ys.begin();
        ev.push_back({x,l,r,1});
        ev.push_back({x+unit,l,r,-1});
    }
    std::sort(ev.begin(),ev.end());
    Coverage tree(ys);
    I prev=ev[0].x, span=ys.back()-ys.front();
    W occupied=0, singles=0, doubles=0;
    for(auto e:ev) {
        I before=tree.length(1);
        I w=e.x-prev;
        occupied+=(W)w*(span-tree.length(0));
        singles+=(W)w*tree.length(1);
        doubles+=(W)w*tree.length(2);
        tree.modify(e); prev=e.x;
        if(axial && tree.length(1)!=before)
            std::cout<<e.x%unit<<" "<<tree.length(1)-before<<"\n";
    }
    if(axial) return 0;
    std::sort(pts.begin(),pts.end());
    std::cout<<decimal(singles)<<" "<<decimal(occupied)<<" "<<decimal(doubles)<<" "
             <<robust(pts,unit+2*error)<<" "<<robust(pts,unit-2*error)<<"\n";
}
