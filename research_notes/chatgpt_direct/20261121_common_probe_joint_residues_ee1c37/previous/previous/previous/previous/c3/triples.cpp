// For each residual set of historical cycles, match two disjoint supports and look up the third.
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using Word=std::uint64_t;
struct Row { Word support; int cost; };
constexpr int infinity=100000;
struct Bank {
    std::array<std::vector<Row>,14> by_size;
    std::vector<Word> keys;
    std::vector<std::uint16_t> vals;
    std::size_t mask;
    explicit Bank(int exponent):keys(1ull<<exponent),vals(keys.size()),mask(keys.size()-1){}
    std::size_t slot(Word key) const{
        Word h=key;
        h=(h^(h>>30))*0xbf58476d1ce4e5b9ULL;
        h=(h^(h>>27))*0x94d049bb133111ebULL;
        std::size_t j=(h^(h>>31))&mask;
        while(keys[j] && keys[j]!=key) j=(j+1)&mask;
        return j;
    }
    void add(Word key,int price){
        auto j=slot(key);
        keys[j]=key;vals[j]=price;by_size[std::popcount(key)].push_back({key,price});
    }
    int lookup(Word key) const{auto j=slot(key);return keys[j] ? vals[j]:infinity;}
};
int main(int argc,char**argv){
    if(argc!=7)return 1;
    Bank bank(20);
    std::ifstream input(argv[1]);Word q,l,h;int c;
    while(input>>q>>c>>l>>h)bank.add(q,c);
    for(auto &rows:bank.by_size)
        std::sort(rows.begin(),rows.end(),[](const auto&a,const auto&b){return a.cost<b.cost || (a.cost==b.cost && a.support<b.support);});
    std::ifstream tasks(argv[2]);
    int best=std::stoi(argv[3])+1,offset=std::stoi(argv[4]),step=std::stoi(argv[5]),stop=std::stoi(argv[6]);
    constexpr Word full=(Word(1)<<45)-1;
    int row=-1,solved=0;
    Word used,x1,x2,x3;int fixed,num;
    while(tasks>>used>>fixed>>x1>>x2>>x3>>num){
        ++row;if(row%step!=offset||row>=stop) continue;
        ++solved;
        if(solved%100==0)std::cerr<<row<<" "<<best<<std::endl;
        Word free=full^used;int n=std::popcount(free);
        auto mincost=[&](int s){return bank.by_size[s].empty()?infinity:bank.by_size[s].front().cost;};
        for(int a=8;a<=13;++a)for(int b=a;b<=13;++b){
            int d=n-a-b;if(d<b||d>13)continue;
            std::array<int,3> sz={a,b,d};
            if(fixed+3*(mincost(a)+mincost(b)+mincost(d))>=best)continue;
            std::array<std::vector<Row>,3> active;
            for(int k=0;k<3;++k){
                int maxcost=(best-1-fixed)/3-mincost(sz[(k+1)%3])-mincost(sz[(k+2)%3]);
                for(auto r:bank.by_size[sz[k]]){
                    if(r.cost>maxcost)break;
                    if(!(r.support&used))active[k].push_back(r);
                }
            }
            std::array<int,3> ord={0,1,2};
            std::sort(ord.begin(),ord.end(),[&](int i,int j){return active[i].size()<active[j].size();});
            int i=ord[0],j=ord[1],k=ord[2];if(active[i].empty())continue;
            for(auto x:active[i])for(auto y:active[j]){
                if(fixed+3*(x.cost+y.cost+mincost(sz[k]))>=best)break;
                if(x.support&y.support || (sz[i]==sz[j] && x.support>y.support))continue;
                Word z=free^x.support^y.support;
                if((sz[i]==sz[k] && x.support>z)||(sz[j]==sz[k] && y.support>z))continue;
                int cost=fixed+3*(x.cost+y.cost+bank.lookup(z));
                if(cost<best){std::cout<<"hit "<<row<<" "<<cost<<" "<<x1<<" "<<x2<<" "<<x3<<" "<<x.support<<" "<<y.support<<" "<<z<<std::endl;}
            }
        }
    }
    std::cout<<"end "<<solved<<" "<<best<<std::endl;
}
