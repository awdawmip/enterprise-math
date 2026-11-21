// Independent exact check for R762HQ. Named Port walk, three-axis supports.
// Compile: g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HQ_PORT_LATTICE_SMITH_CHECK.cpp -o r762hq && ./r762hq
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct DSU {
    array<int,6> parent{};
    DSU(){iota(parent.begin(),parent.end(),0);}
    int root(int x){while(parent[x]!=x)x=parent[x]=parent[parent[x]];return x;}
    void join(int x,int y){parent[root(x)]=root(y);}
};
struct Count {
    uint64_t closed=0, even=0;
    array<uint64_t,7> rank{};
    array<uint64_t,7> q3_by_rank{};
    uint64_t q1=0,q3=0;
};
vector<int> ports; vector<vector<int>> adj; vector<int> word; array<Count,9> stats{};

void inspect(int m){
    auto &s=stats[m]; ++s.closed;
    int h0=0, prev=0;
    array<int,6> degree{};
    DSU d;
    for(int t=0;t<m;t++){
        int h=ports[word[t]]|ports[word[t+1]];
        assert(__builtin_popcount((unsigned)h)==3);
        if(t==0) h0=h;
        else{
            unsigned entering=(unsigned)(h & ~prev), leaving=(unsigned)(prev & ~h);
            assert(__builtin_popcount(entering)==__builtin_popcount(leaving));
            assert(__builtin_popcount(entering)<=1);
            if(entering) d.join(__builtin_ctz(entering),__builtin_ctz(leaving));
        }
        for(int a=0;a<6;a++)degree[a]+=(h>>a)&1;
        prev=h;
    }
    int c=0; array<int,6> b{};
    for(int a=0;a<6;a++){
        if(d.root(a)==a) ++c;
        b[d.root(a)]+=(h0>>a)&1;
    }
    int g=0;for(int a=0;a<6;a++)g=gcd(g,b[a]);
    assert(g==1 || g==3);
    const int r=7-c;
    assert(r>=1&&r<=6);
    ++s.rank[r];
    if(g==3) {++s.q3;++s.q3_by_rank[r];} else ++s.q1;
    bool all_even=true;for(int a:degree)if(a&1)all_even=false;
    if(all_even){
        ++s.even;
        array<int,6> balance{};
        for(int a=0;a<6;a++)balance[d.root(a)]+=degree[a]/2 - (m/2)*((h0>>a)&1);
        for(int a:balance)assert(a==0);
    }
}
void walk(int depth,int length){
    if(depth==length){if(word.back()==0)inspect(length);return;}
    for(int n:adj[word.back()]){word.push_back(n);walk(depth+1,length);word.pop_back();}
}
int main(){
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)ports.push_back((1<<a)|(1<<b));
    adj.resize(ports.size());
    for(int i=0;i<(int)ports.size();i++)for(int j=0;j<(int)ports.size();j++)
        if(__builtin_popcount((unsigned)(ports[i]&ports[j]))==1)adj[i].push_back(j);
    for(int m=2;m<=8;m+=2){word={0};walk(0,m);}
    for(int m=2;m<=8;m+=2){
        auto &s=stats[m];
        assert(s.q1+s.q3==s.closed);
        cout<<"m="<<m<<" closed="<<s.closed<<" parity_even="<<s.even
            <<" q1="<<s.q1<<" q3="<<s.q3<<" rank_hist=[";
        for(int r=1;r<=6;r++)cout<<(r==1?"":",")<<s.rank[r];
        cout<<"] q3_by_rank=[";
        for(int r=1;r<=6;r++)cout<<(r==1?"":",")<<s.q3_by_rank[r];
        cout<<"]\n";
    }
    assert(stats[2].closed==8 && stats[4].closed==288 && stats[6].closed==17536 && stats[8].closed==1118720);
    assert(stats[2].even==8 && stats[4].even==168 && stats[6].even==4960 && stats[8].even==177536);
    cout<<"PASS\n";
}
