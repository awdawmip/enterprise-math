// Exhaust legal message classes and their bipartitions after affine normalization.
// The traversal and native menu input format follow previous/previous/previous/previous/curve/class_minima.cpp.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <stdexcept>

using Mask = __uint128_t;  // 125 histories
using ReadMask = std::array<std::uint64_t, 4>;  // 250 menu and transformation choices
using Forbidden = std::array<Mask, 125>;
constexpr Mask one = 1;
constexpr int n = 125;

Forbidden bad[n];
ReadMask observation[n][n];
long long visits[n + 1]{};

int selected[n];

constexpr int minima[] = {0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
struct Example {
    int value;
    int id[13]{};
    int left{};
    void save(int v, int size, int side) {
        value=v;
        std::copy(selected,selected+size,id);
        left=side;
    }
};
Example max_gain[14], min_fine[14];
long long examined[14]{}, splits_checked[14]{};
ReadMask half_menu[2][13][128]{};
int tailLower[14]{}, capCoarse=100000,lowerCoarse=0;
bool minimum_only=false;
void price_splits(int size,int cost) {
    if (minimum_only && cost!=minima[size]) return;
    if (cost+tailLower[size]>capCoarse) return;
    int tail=std::max(tailLower[size],lowerCoarse-cost);
    int lower=100000;
    for(int i=1;i<size;i++) lower=std::min(lower,minima[i]+minima[size-i]);
    if(cost-lower<=max_gain[size].value && lower+tail>=min_fine[size].value) return;
    ++examined[size];
    int first_size=size/2;
    int lengths[2]={first_size,size-first_size};
    for(int h=0;h<2;h++) {
        int offset=h?first_size:0;
        for(int x=0;x<size;x++) {
            auto &tab=half_menu[h][x];
            for(int mask=1;mask<(1<<lengths[h]);mask++) {
                int added=__builtin_ctz((unsigned)mask)+offset;
                auto o=observation[selected[x]][selected[added]];
                for(int w=0;w<4;w++) tab[mask][w]=tab[mask&(mask-1)][w]|o[w];
            }
        }
    }
    int all=(1<<size)-1, low_bits=(1<<first_size)-1;
    for(int left=1;left<all;left+=2) {
        int a=__builtin_popcount((unsigned)left),bound=minima[a]+minima[size-a];
        if(cost-bound<=max_gain[size].value && bound+tail>=min_fine[size].value) continue;
        int fine=0;
        ++splits_checked[size];
        for(int x=0;x<size;x++) {
            int own=(left&(1<<x))?left:all^left;
            const auto &p=half_menu[0][x][own&low_bits];
            const auto &q=half_menu[1][x][own>>first_size];
            for(int w=0;w<4;w++) fine+=__builtin_popcountll(p[w]|q[w]);
        }
        if(cost-fine>max_gain[size].value) max_gain[size].save(cost-fine,size,left);
        if(fine+tail<min_fine[size].value) min_fine[size].save(fine+tail,size,left);
    }
}


int first(Mask bits) {
    const auto low = static_cast<std::uint64_t>(bits);
    if (low) return __builtin_ctzll(low);
    return 64 + __builtin_ctzll(static_cast<std::uint64_t>(bits >> 64));
}

void enumerate(int size, Mask candidates, const Forbidden &forbidden,
               const ReadMask *masks, int cost) {
    if (size >= 14) throw std::runtime_error("found an admissible class of size at least 14");
    ++visits[size];
    price_splits(size, cost);
    while (candidates) {
        const int v = first(candidates);
        candidates &= candidates - 1;
        ReadMask next_masks[n], new_row{};
        int next_cost = cost;
        for (int j = 0; j < size; ++j) {
            for (int h = 0; h < 4; ++h) {
                auto pair = observation[v][selected[j]][h];
                auto old = masks[j][h];
                next_masks[j][h] = old | pair;
                next_cost += __builtin_popcountll(pair & ~old);
                new_row[h] |= pair;
            }
        }
        for (auto word : new_row) next_cost += __builtin_popcountll(word);
        next_masks[size] = new_row;
        selected[size] = v;
        Mask remaining = candidates & ~forbidden[v];
        Forbidden next_forbidden;
        for (Mask todo = remaining; todo; todo &= todo - 1) {
            int j = first(todo);
            next_forbidden[j] = forbidden[j] | bad[j][v];
        }
        enumerate(size + 1, remaining, next_forbidden, next_masks, next_cost);
    }
}

int canonical_second(int v) {
    std::array<int, 3> coords{v / 25, (v / 5) % 5, v % 5};
    std::sort(coords.begin(), coords.end());
    int best_id = n;
    do {
        for (int scale : {1, 2}) {
            for (int signs = 0; signs < 8; ++signs) {
                int id = 0;
                for (int j = 0; j < 3; ++j) {
                    int s = ((signs >> j) & 1) ? 5 - scale : scale;
                    id = 5 * id + (coords[j] * s) % 5;
                }
                best_id = std::min(best_id, id);
            }
        }
    } while (std::next_permutation(coords.begin(), coords.end()));
    return best_id;
}

int main(int argc, char **argv) {
    if (argc != 3) return 2;
    std::string mode=argv[2];
    minimum_only=(mode=="minimum");
    if (mode=="joint") {
        if (!(std::cin>>capCoarse>>lowerCoarse)) return 2;
        for(int &v:tailLower) if(!(std::cin>>v)) return 2;
    } else if(mode!="all"&&!minimum_only) return 2;
    std::ifstream in(argv[1], std::ios::binary);
    if (!in.read(reinterpret_cast<char *>(observation), sizeof(observation))) return 3;
    for(auto &r:min_fine) r.value=100000;
    std::array<unsigned char, 3> edge;
    int n_edges = 0;
    while (in.read(reinterpret_cast<char *>(edge.data()), edge.size())) {
        ++n_edges;
        do {
            bad[edge[0]][edge[1]] |= one << edge[2];
        } while (std::next_permutation(edge.begin(), edge.end()));
    }
    assert(n_edges == 47000);

    for (int v = 1; v < n; ++v) {
        if (canonical_second(v) != v) continue;
        selected[0] = 0;
        selected[1] = v;
        Mask remaining = ((one << n) - 1) & ~((one << (v + 1)) - 1) & ~bad[0][v];
        Forbidden forbidden;
        for (int j = 0; j < n; ++j) forbidden[j] = bad[0][j] | bad[v][j];
        ReadMask masks[2]{observation[0][v], observation[0][v]};
        int cost = 0;
        for (auto word : masks[0]) cost += 2 * __builtin_popcountll(word);
        enumerate(2, remaining, forbidden, masks, cost);
    }
    for (int k = 2; k <= n; ++k) {
        if (!visits[k]) continue;
        std::cout << k << " " << visits[k] << " " << examined[k] << " " << splits_checked[k];
        for(auto r:{max_gain[k],min_fine[k]}) {
            std::cout<<" "<<r.value<<" "<<r.left;
            for(int j=0;j<k;j++) std::cout<<" "<<r.id[j];
        }
        std::cout<<"\n";
    }
}
