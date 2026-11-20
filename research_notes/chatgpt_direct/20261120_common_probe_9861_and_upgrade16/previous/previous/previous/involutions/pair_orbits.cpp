// Rebuild every moving orbit of a class of size at least eleven.
// A mask is always mapped point by point to avoid representation-dependent lookup tables.
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>

using Mask = __uint128_t;
using Word = uint64_t;
using Permutation = std::array<int,125>;

int first(Mask m) {
    return Word(m) ? __builtin_ctzll(Word(m)) : 64 + __builtin_ctzll(Word(m >> 64));
}
Mask image(Mask m, const Permutation& permutation) {
    Mask result = 0;
    for (; m; m &= m-1) result |= Mask(1) << permutation[first(m)];
    return result;
}
struct Hash {
    size_t operator()(Mask x) const {
        return Word(x) ^ (Word(x >> 64) * 0x9e3779b97f4a7c15ULL);
    }
};
struct Row {
    Mask points;
    int size, cost;
};
int translate(int x, int v) {
    return 25*((x/25+v/25)%5) + 5*((x/5%5+v/5%5)%5) + (x%5+v%5)%5;
}
int main(int argc,char** argv) {
    if (argc != 5) return 2;
    std::ifstream lin(argv[1]), seeds(argv[2]), mp(argv[3]);
    std::ofstream out(argv[4]);
    Permutation involution;
    for (int& p : involution) mp >> p;
    std::vector<Permutation> linear(96), translations(125);
    for (auto& h : linear) for (int& p : h) lin >> p;
    for (int v=0; v<125; ++v)
        for (int p=0; p<125; ++p) translations[v][p]=translate(p,v);
    assert(mp && lin && seeds && out);
    std::unordered_map<Mask,Row,Hash> bank;
    std::map<int,int> minima;
    int size,cost;
    while (seeds >> size >> cost) {
        Mask seed=0;
        for (int i=0,p; i<size; ++i) {
            seeds >> p;
            seed |= Mask(1) << p;
        }
        // No affine representative removal is needed at this scale.
        // Applying all 12,000 maps to each enumerated seed gives surjectivity directly.
        for (auto& h : linear) {
            Mask shape=image(seed,h);
            for (auto& t : translations) {
                Mask row=image(shape,t), mate=image(row,involution);
                if (row & mate) continue;
                if (!minima.count(size) || minima[size]>cost) minima[size]=cost;
                Mask support = row | mate;
                auto it=bank.find(support);
                if (it==bank.end() || it->second.cost>cost) bank[support]={row,size,cost};
            }
        }
    }
    for (auto [q,row] : bank) {
        out << row.size << " 0 " << row.cost << " " << Word(row.points) << " " << Word(row.points>>64) << "\n";
    }
    for (auto [s,c] : minima) std::cout << s << " " << c << "\n";
}
