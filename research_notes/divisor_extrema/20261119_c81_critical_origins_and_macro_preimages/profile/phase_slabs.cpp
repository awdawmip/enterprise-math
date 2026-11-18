#include <algorithm>
#include <array>
#include <iostream>
#include <cstdint>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>

using I=std::int64_t;
using Wide=__int128_t;
std::string decimal(Wide a) {
    if (!a) return "0";
    bool negative=a<0; if(negative) a=-a;
    std::string s;
    while(a){s.push_back(char('0'+a%10)); a/=10;}
    std::reverse(s.begin(),s.end()); return negative?"-"+s:s;
}
using GroupKey=std::pair<int,int>;
using Group=std::multiset<int>;
struct Word {int x,y,xt,yt;};

class RangeExtrema {
    std::vector<int> mn,mx,shift;
    int size;
    const std::vector<I>& boundaries;
    const std::vector<std::pair<I,I>>& roots;
    Wide edge_re=0,edge_im=0;
    std::vector<Wide> first,second;
    void add(int t,int l,int r,int a,int b,int v) {
        if(a<=l && r<=b){
            Wide weight=boundaries[r]-boundaries[l];
            second[t]+=2*v*first[t]+v*v*weight;
            first[t]+=v*weight;
            mn[t]+=v; mx[t]+=v; shift[t]+=v;
            return;
        }
        int m=(l+r)/2;
        if(a<m) add(t*2,l,m,a,b,v);
        if(m<b) add(t*2+1,m,r,a,b,v);
        Wide weight=boundaries[r]-boundaries[l];
        Wide inner=first[2*t]+first[2*t+1];
        first[t]=inner+weight*shift[t];
        second[t]=second[2*t]+second[2*t+1]+2*shift[t]*inner+
                  weight*shift[t]*shift[t];
        mn[t]=shift[t]+std::min(mn[2*t],mn[2*t+1]);
        mx[t]=shift[t]+std::max(mx[2*t],mx[2*t+1]);
    }
public:
    explicit RangeExtrema(const std::vector<I>& cuts,const std::vector<std::pair<I,I>>& phases):
        mn(4*cuts.size()),mx(4*cuts.size()),shift(4*cuts.size()),
        size(cuts.size()-1),boundaries(cuts),roots(phases),first(4*cuts.size()),second(4*cuts.size()){}
    std::pair<Wide,Wide> moments() const{return {first[1],second[1]};}
    std::pair<Wide,Wide> edges() const {return {edge_re,edge_im};}
    void add(int a,int b,int v) {
        if(a>=b) return;
        edge_re+=v*(roots[b].first-roots[a].first);
        edge_im+=v*(roots[b].second-roots[a].second);
        add(1,0,size,a,b,v);
    }
    std::pair<int,int> bounds() const {return {mn[1],mx[1]};}
};

class Assignment {
    int end;
    std::map<GroupKey,Group> groups;
    const Group empty;
    RangeExtrema tree;
    const Group& find(int x,int y) const {
        auto i=groups.find({x,y});
        return i==groups.end()?empty:i->second;
    }
    // For fixed actual cell (x,j), calculate all y-phases yielding one occupant.
    // The only possibilities are one not-yet-moved from j or one already-moved
    // from j-1. The two extreme jumps on either side suffice.
    void contribute(int x,int j,int sign) {
        const auto& future=find(x,j);
        const auto& past=find(x,j-1);
        auto a=future.rbegin();
        int t1=(a!=future.rend()?*a++:0),t2=(a!=future.rend()?*a:0);
        auto b=past.begin();
        int s1=(b!=past.end()?*b++:end),s2=(b!=past.end()?*b:end);
        tree.add(t2,std::min(t1,s1),sign);
        tree.add(std::max(t1,s1),s2,sign);
    }
public:
    explicit Assignment(const std::vector<I>& cuts,const std::vector<std::pair<I,I>>& phases):end(cuts.size()-1),tree(cuts,phases){}
    std::pair<Wide,Wide> edges() const{return tree.edges();}
    std::pair<Wide,Wide> moments() const{return tree.moments();}
    void alter(int x,int y,int yt,bool insert) {
        contribute(x,y,-1);
        contribute(x,y+1,-1);
        auto &group=groups[{x,y}];
        if(insert) group.insert(yt);
        else {
            auto i=group.find(yt);
            if(i==group.end()) throw std::logic_error("missing word");
            group.erase(i);
            if(group.empty()) groups.erase({x,y});
        }
        contribute(x,y,+1);
        contribute(x,y+1,+1);
    }
    std::pair<int,int> bounds() const{return tree.bounds();}
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n,nx,ny;
    if(!(std::cin>>n>>nx>>ny)) return 1;
    std::vector<Word> words(n);
    std::vector<I> xcuts(nx+1),ycuts(ny+1);
    std::vector<std::pair<I,I>> roots(ny+1);
    for(auto &v:xcuts) if(!(std::cin>>v)) return 1;
    for(auto &v:ycuts) if(!(std::cin>>v)) return 1;
    for(auto &v:roots) if(!(std::cin>>v.first>>v.second)) return 1;
    Assignment state(ycuts,roots);
    for(auto &w:words){
        if(!(std::cin>>w.x>>w.y>>w.xt>>w.yt)) return 1;
        state.alter(w.x,w.y,w.yt,true);
    }
    auto [low,high]=state.bounds();
    std::sort(words.begin(),words.end(),[](const auto& a,const auto& b){return a.xt<b.xt;});
    int last=0;
    auto emit=[&](int phase){
        auto [m1,m2]=state.moments();
        auto [re,im]=state.edges();
        std::cout<<xcuts[last]<<" "<<xcuts[phase]<<" "<<decimal(m1)<<" "<<decimal(m2)
                 <<" "<<decimal(re)<<" "<<decimal(im)<<"\n";
        last=phase;
    };
    for(int i=0;i<n;){
        int j=i,phase=words[i].xt;
        if(phase==nx) break;
        emit(phase);
        while(j<n && words[j].xt==phase){
            const auto &w=words[j++];
            state.alter(w.x,w.y,w.yt,false);
            state.alter(w.x+1,w.y,w.yt,true);
        }
        auto [lo,hi]=state.bounds();
        low=std::min(low,lo); high=std::max(high,hi);
        i=j;
    }
    emit(nx);
    std::cout<<"bounds "<<low<<" "<<high<<"\n";
}
