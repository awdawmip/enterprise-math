#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using Mask=__uint128_t;using U=uint64_t;
int cnt(Mask x){return std::popcount(U(x))+std::popcount(U(x>>64));}
int bit(Mask x){return U(x)?std::countr_zero(U(x)):64+std::countr_zero(U(x>>64));}
constexpr Mask all=(Mask(1)<<125)-1;
Mask bad[125][125];
struct Row{Mask points=0,available=all;int size=0;};
std::array<Row,5> rows;
int colors;
long long steps=0;
bool solve(Mask free){
    ++steps;
    if(!free)return true;
    int n=cnt(free);
    for(int c=0;c<colors;c++)if(rows[c].size+cnt(rows[c].available&free)<n-12*(colors-1))return false;
    int best=colors+1,pivot=-1,score=-1;
    for(Mask d=free;d;d&=d-1){
        int p=bit(d),ways=0;
        for(int c=0;c<colors;c++) if((rows[c].available>>p)&1)++ways;
        if(!ways)return false;
        if(ways<best){pivot=p;best=ways;score=-1;}
    }
    for(int c=0;c<colors;c++){
        auto old=rows[c];Mask flag=Mask(1)<<pivot;
        if(old.available&flag){
            auto& r=rows[c];
            for(Mask d=old.points;d;d&=d-1)r.available&=~bad[pivot][bit(d)];
            r.points|=flag;
            if(++r.size==12)r.available=0;
            if(solve(free^flag))return true;
            r=old;
        }
        if(!old.size)break;
    }
    return false;
}
int main(int argc,char**argv){
    if(argc!=6)return 2;
    int k=std::stoi(argv[1]);colors=std::stoi(argv[2]);
    std::ifstream obs(argv[3],std::ios::binary);obs.seekg(125*125*32);
    unsigned char t[3];int triples=0;
    while(obs.read((char*)t,3)){++triples;for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(i!=j)bad[t[i]][t[j]]|=Mask(1)<<t[3-i-j];}
    if(triples!=47000)return 3;
    std::ifstream masks(argv[4]);std::array<Mask,250> parent;
    for(auto& a:parent){U l,h;masks>>l>>h;a=(Mask(h)<<64)|l;}
    std::ifstream records(argv[5]);std::string line;int cases=0;
    while(std::getline(records,line)){
        if(line.empty()||line[0]!='0')continue;
        std::istringstream input(line);Mask free=all;
        for(int j=0,i;j<k;j++){if(!(input>>i))return 4;free&=~parent[i];}
        ++cases;rows={};
        if(solve(free)){
            std::cout<<"found "<<line<<"\n";
            for(int c=0;c<colors;c++)std::cout<<U(rows[c].points)<<" "<<U(rows[c].points>>64)<<"\n";
            break;
        }
    }
    std::cout<<cases<<" "<<steps<<"\n";
}
