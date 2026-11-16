// Count every unordered six-class partition of a 60-point residual.
// Inputs are generated from all 250 public situations by saturated_cases.py.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <vector>

using Mask = std::uint64_t;
using Observation = std::array<Mask,4>;
constexpr int size = 60;
constexpr Mask universe = (Mask(1) << size) - 1;
std::array<std::array<Mask,size>,size> forbidden{};
std::array<std::array<Observation,125>,125> ambiguity{};
std::array<int,size> point{};
std::array<std::vector<Mask>,14> groups;
std::array<std::array<std::vector<Mask>,size>,14> containing;
std::map<int,unsigned long long> cost_histogram;
std::array<Mask,6> partition{};
std::uint64_t nodes=0;
std::ofstream solutions;

int count(Mask s) {return __builtin_popcountll(s);}
int first(Mask s) {return __builtin_ctzll(s);}

int price(Mask group) {
    int total=0;
    for(Mask xs=group;xs;xs&=xs-1) {
        Observation conditions{};
        for(Mask ys=group;ys;ys&=ys-1) {
            const auto &pair=ambiguity[point[first(xs)]][point[first(ys)]];
            for(int b=0;b<4;b++) conditions[b]|=pair[b];
        }
        for(auto word:conditions) total+=count(word);
    }
    return total;
}

bool legal(Mask group) {
    for(Mask xs=group;xs;xs&=xs-1)
        for(Mask ys=xs&(xs-1);ys;ys&=ys-1)
            if (forbidden[first(xs)][first(ys)] & group) return false;
    return true;
}

void enumerate(Mask picked, Mask candidates, const std::array<Mask,size>& blocked) {
    const int n=count(picked);
    if(n>13) throw std::runtime_error("unexpected 14-point class");
    if(n>=8){
        groups[n].push_back(picked);
        for(Mask xs=picked;xs;xs&=xs-1) containing[n][first(xs)].push_back(picked);
    }
    while(candidates && n+count(candidates)>=8) {
        const int j=first(candidates);
        candidates&=candidates-1;
        const Mask remain=candidates & ~blocked[j];
        std::array<Mask,size> next{};
        for(Mask xs=remain;xs;xs&=xs-1) {
            int i=first(xs);next[i]=blocked[i]|forbidden[i][j];
        }
        enumerate(picked | (Mask(1)<<j),remain,next);
    }
}

template<class Callback>
void small_groups(Mask points,int need,Mask selected,Callback& visit) {
    if(need==0){if(legal(selected))visit(selected);return;}
    while(count(points)>=need){Mask bit=points&-points;points-=bit;small_groups(points,need-1,selected|bit,visit);}
}

void partition_remaining(Mask remaining,int slots,int max_size,Mask last) {
    ++nodes;
    const int n=count(remaining);
    if(slots==1) {
        if(n<1 || n>max_size || (n==max_size && remaining<=last) || !legal(remaining))return;
        partition[5]=remaining;
        int total=0;for(auto g:partition) total+=price(g);
        ++cost_histogram[total];
        if(solutions.is_open()) { for(auto g:partition) solutions<<g<<' '; solutions<<'\n'; }
        return;
    }
    const int min_size=(n+slots-1)/slots;
    for(int s=std::min(max_size,n-slots+1);s>=min_size;--s) {
        Mask previous = s==max_size ? last : 0;
        const bool forced_equal = slots*s==n;
        int pivot=first(remaining);
        if(forced_equal && s>=8) for(Mask xs=remaining;xs;xs&=xs-1){
            int i=first(xs);if(containing[s][i].size()<containing[s][pivot].size())pivot=i;
        }
        auto visit=[&](Mask g) {
            if(g<=previous || (g&remaining)!=g || (forced_equal && !(g&(Mask(1)<<pivot))))return;
            partition[6-slots]=g;
            partition_remaining(remaining^g,slots-1,s,forced_equal?previous:g);
        };
        if(s<8) small_groups(remaining,s,0,visit);
        else {const auto &list=forced_equal?containing[s][pivot]:groups[s];for(auto g:list)visit(g);}
    }
}

int main(int argc,char**argv){
    if(argc!=3 && argc!=4)return 1;
    if(argc==4)solutions.open(argv[3]);
    std::ifstream edges(argv[1],std::ios::binary), points(argv[2]);
    if(!edges.read(reinterpret_cast<char*>(ambiguity.data()),sizeof(ambiguity)))return 2;
    std::array<int,125> local;local.fill(-1);
    for(int j=0;j<size;j++) {if(!(points>>point[j]))return 3;local[point[j]]=j;}
    unsigned char triple[3];
    while(edges.read(reinterpret_cast<char*>(triple),3)){
        const int a=local[triple[0]],b=local[triple[1]],c=local[triple[2]];
        if(a<0||b<0||c<0)continue;
        for(auto t: {std::array<int,3>{a,b,c},{a,c,b},{b,a,c},{b,c,a},{c,a,b},{c,b,a}})
            forbidden[t[0]][t[1]] |= Mask(1)<<t[2];
    }
    std::array<Mask,size> empty{};enumerate(0,universe,empty);
    partition_remaining(universe,6,13,0);
    std::cout<<nodes<<'\n';for(auto [cost,number]:cost_histogram)std::cout<<cost<<' '<<number<<'\n';
}
