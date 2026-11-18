#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

using Narrow = std::int64_t;
using Wide = __int128_t;
struct Word { int x0,x1,y0,y1; };
struct Event { int at,id; bool enter; };
struct Record {
    int start=0, low=0,high=0;
    Wide area=0;
    bool active=false, possible=false, loses=false;
};

std::string decimal(Wide a) {
    if (a==0) return "0";
    std::string t;
    while(a>0){ t.push_back(char('0'+a%10)); a/=10; }
    std::reverse(t.begin(),t.end()); return t;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n,nx,ny;
    if(!(std::cin>>n>>nx>>ny)) return 1;
    std::vector<Narrow> xs(nx),ys(ny);
    for(auto& x:xs) std::cin>>x;
    for(auto& y:ys) std::cin>>y;
    std::vector<Word> words(n);
    std::vector<Event> events;
    for(int i=0;i<n;++i) {
        auto &w=words[i]; std::cin>>w.x0>>w.x1>>w.y0>>w.y1;
        events.push_back({w.x0,i,true}); events.push_back({w.x1,i,false});
    }
    std::sort(events.begin(),events.end(),[](Event a, Event b){return a.at<b.at;});
    std::set<std::pair<int,int>> active;
    std::vector<Record> rec(n);
    auto flush=[&](int i,int now) {
        if(i<0) return;
        auto &a=rec[i]; auto w=words[i];
        if(a.active && a.start!=now) {
            if(a.low<a.high) {
                a.possible=true;
                a.area+=Wide(xs[now]-xs[a.start])*(ys[a.high]-ys[a.low]);
            }
            if(a.low>w.y0 || a.high<w.y1) a.loses=true;
        }
        a.start=now;
    };
    auto update=[&](int i) {
        if(i<0 || !rec[i].active) return;
        auto w=words[i];
        auto it=active.find({w.y0,i});
        if(it==active.end()) throw std::logic_error("missing square");
        auto after=std::next(it);
        rec[i].low=it==active.begin()?w.y0:std::max(w.y0,words[std::prev(it)->second].y1);
        rec[i].high=after==active.end()?w.y1:std::min(w.y1,words[after->second].y0);
    };
    for(auto e:events) {
        const auto key=std::make_pair(words[e.id].y0,e.id);
        auto it=active.lower_bound(key);
        int pred=it==active.begin()?-1:std::prev(it)->second;
        auto following=!e.enter?std::next(it):it;
        int succ=following==active.end()?-1:following->second;
        flush(pred,e.at); flush(e.id,e.at); flush(succ,e.at);
        if(e.enter) active.insert(key);
        else active.erase(it);
        rec[e.id].active=e.enter;
        update(pred); update(e.id); update(succ);
    }
    for(auto a:rec) std::cout<<decimal(a.area)<<' '<<a.possible<<' '<<!a.loses<<'\n';
}
