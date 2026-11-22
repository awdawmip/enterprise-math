// R762IT: exact nine-support connectivity-essential family and S6 orbit census.
// g++ -O2 -std=c++17 R762IT_NINE_TRIANGLE_ORBITS.cpp -o r762it && ./r762it
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
using namespace std;

int port_id[6][6];
array<array<int,3>,20> support_ports;
array<array<int,3>,20> support_axes;

uint64_t partition(uint32_t subset) {
    int parent[15]; iota(parent,parent+15,0);
    auto root = [&](int x) {while(parent[x]!=x) x=parent[x]; return x;};
    for(int j=0;j<20;j++) if((subset>>j)&1) {
        auto t=support_ports[j];
        parent[root(t[0])]=root(t[1]);
        parent[root(t[0])]=root(t[2]);
    }
    int id[15];fill(id,id+15,-1);
    uint64_t partition_bits=0;int count=0;
    for(int v=0;v<15;v++){
        int r=root(v);
        if(id[r]<0) id[r]=count++;
        partition_bits|=uint64_t(id[r])<<(4*v);
    }
    return partition_bits;
}

int main(){
    int p=0,t=0;
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)port_id[a][b]=port_id[b][a]=p++;
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)for(int c=b+1;c<6;c++){
        support_axes[t]={a,b,c};
        support_ports[t]={port_id[a][b],port_id[a][c],port_id[b][c]};t++;
    }
    set<uint32_t> essential;
    int families=0;
    for(uint32_t mask=0;mask<(1u<<20);mask++){
        if(__builtin_popcount(mask)!=9)continue;
        families++;
        auto before=partition(mask);bool allessential=true;
        for(int j=0;j<20;j++)if((mask>>j)&1){
            if(partition(mask^(1u<<j))==before){allessential=false;break;}
        }
        if(allessential) essential.insert(mask);
    }
    assert(families==167960 && essential.size()==240);
    int index[6][6][6]={};
    for(int j=0;j<20;j++){
        auto s=support_axes[j];index[s[0]][s[1]][s[2]]=j;
    }
    auto orbit=[&](uint32_t representative){
        set<uint32_t> result;
        array<int,6> perm={0,1,2,3,4,5};
        do{
            uint32_t image=0;
            for(int j=0;j<20;j++)if((representative>>j)&1){
                auto a=support_axes[j];
                array<int,3> b={perm[a[0]],perm[a[1]],perm[a[2]]};
                sort(b.begin(),b.end());
                image|=1u<<index[b[0]][b[1]][b[2]];
            }
            result.insert(image);
        }while(next_permutation(perm.begin(),perm.end()));
        return result;
    };
    auto O1=orbit(967489),O2=orbit(971528);
    assert(O1.size()==180 && O2.size()==60);
    set<uint32_t> combined=O1;combined.insert(O2.begin(),O2.end());
    assert(combined==essential);
    int axisstar=0;
    for(auto mask:essential){
        bool isstar=false;
        for(int a=0;a<6;a++){
            uint32_t starmask=0;
            for(int j=0;j<20;j++){
                auto s=support_axes[j];
                if(s[0]==a||s[1]==a||s[2]==a)starmask|=1u<<j;
            }
            if((mask&starmask)==mask)isstar=true;
        }
        if(isstar)axisstar++;
    }
    assert(axisstar==60);
    cout<<"PASS R762IT families="<<families<<" all-essential9="<<essential.size()
        <<" S6-orbit-sizes="<<O1.size()<<","<<O2.size()
        <<" star-nine-subsets="<<axisstar<<"\n";
}
