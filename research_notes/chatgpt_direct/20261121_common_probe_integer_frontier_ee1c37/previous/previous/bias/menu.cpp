// Enumerate native legal message classes through the origin. Common scaling
// may swap the two actions, so record the absolute difference of their prices.
#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>

using HistorySet = __uint128_t;
using Words = std::array<std::uint64_t, 4>;
using Forbidden = std::array<HistorySet, 125>;
constexpr HistorySet one = 1;
constexpr std::uint64_t lower61 = (std::uint64_t(1) << 61) - 1;
Forbidden forbidden_pair[125];
Words menus[125][125];
std::uint32_t anchored_mothers[125]{};
int maximum_difference[14][2][3251];
int chosen[14];
long long nodes[14]{};

int first(HistorySet m) {
    auto low = static_cast<std::uint64_t>(m);
    return low ? std::countr_zero(low) : 64 + std::countr_zero(static_cast<std::uint64_t>(m >> 64));
}

int canonical_second(int v) {
    std::array<int,3> coords{v/25,v/5%5,v%5};
    std::sort(coords.begin(),coords.end());
    int best = 125;
    do {
        for (int scale : {1,2}) for (int signs=0; signs<8; ++signs) {
            int id=0;
            for (int j=0;j<3;++j) {
                int a=(signs>>j&1) ? 5-scale : scale;
                id=5*id+(a*coords[j])%5;
            }
            best=std::min(best,id);
        }
    } while(std::next_permutation(coords.begin(),coords.end()));
    return best;
}

void update(const Words& added, int& identity, int& doubling) {
    identity += std::popcount(added[0]) + std::popcount(added[1]&lower61);
    doubling += std::popcount(added[1]&~lower61) + std::popcount(added[2]) + std::popcount(added[3]);
}

void scan(int size, HistorySet candidates, const Forbidden& forbidden,
          const Words* masks, int identity, int doubling, std::uint32_t parents) {
    assert(size <= 13);
    ++nodes[size];
    auto& entry=maximum_difference[size][parents!=0][identity+doubling];
    entry=std::max(entry,std::abs(identity-doubling));
    while(candidates) {
        int x=first(candidates);
        candidates &= candidates-1;
        int next_i=identity,next_d=doubling;
        Words next_masks[14],new_mask{};
        for(int j=0;j<size;++j) {
            Words added;
            for(int k=0;k<4;++k) {
                auto p=menus[x][chosen[j]][k];
                new_mask[k] |= p;
                added[k]=p&~masks[j][k];
                next_masks[j][k]=p|masks[j][k];
            }
            update(added,next_i,next_d);
        }
        next_masks[size]=new_mask;
        update(new_mask,next_i,next_d);
        chosen[size]=x;
        auto available=candidates&~forbidden[x];
        Forbidden next_forbidden;
        for(auto todo=available;todo;todo&=todo-1) {
            int y=first(todo);
            next_forbidden[y]=forbidden[y]|forbidden_pair[x][y];
        }
        scan(size+1,available,next_forbidden,next_masks,next_i,next_d,parents&anchored_mothers[x]);
    }
}

int main(int argc,char** argv) {
    assert(argc==3);
    std::ifstream input(argv[1],std::ios::binary), mother_input(argv[2]);
    assert(input.read(reinterpret_cast<char*>(menus),sizeof(menus)));
    std::array<unsigned char,3> tri;
    int edges=0, anchored=0;
    while(input.read(reinterpret_cast<char*>(tri.data()),3)) {
        ++edges;
        do {forbidden_pair[tri[0]][tri[1]] |= one << tri[2];} while(std::next_permutation(tri.begin(),tri.end()));
    }
    assert(edges==47000);
    for(int t=0;t<250;++t) {
        std::uint64_t l,h;
        assert(mother_input>>l>>h);
        if(!(l&1)) continue;
        auto m=(HistorySet(h)<<64)|l;
        for(auto bits=m;bits;bits&=bits-1) anchored_mothers[first(bits)] |= std::uint32_t(1)<<anchored;
        ++anchored;
    }
    assert(anchored==26);
    for(auto& slab:maximum_difference) for(auto& row:slab) std::fill(std::begin(row),std::end(row),-1);
    maximum_difference[1][1][0]=0;
    for(int v=1;v<125;++v) if(canonical_second(v)==v) {
        chosen[0]=0;chosen[1]=v;
        auto remaining=((one<<125)-1)&~((one<<(v+1))-1)&~forbidden_pair[0][v];
        Forbidden blocked;
        for(int j=0;j<125;++j) blocked[j]=forbidden_pair[0][j]|forbidden_pair[v][j];
        Words masks[2]{menus[0][v],menus[0][v]};
        int i=0,d=0;update(masks[0],i,d);
        scan(2,remaining,blocked,masks,2*i,2*d,anchored_mothers[v]);
    }
    for(int s=1;s<=13;++s) {
        std::cerr<<s<<" "<<nodes[s]<<"\n";
        for(int e=0;e<2;++e) for(int c=0;c<=3250;++c)
            if(maximum_difference[s][e][c]>=0) std::cout<<s<<" "<<e<<" "<<c<<" "<<maximum_difference[s][e][c]<<"\n";
    }
}
