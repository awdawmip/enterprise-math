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

constexpr int gain=960;
int runner=900;
constexpr int minima[]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
ReadMask pre[2][12][64]{};
void price_splits(int size,int cost){
 if(size!=12)return;
 for(int half=0;half<2;half++)for(int i=0;i<12;i++)for(int sub=1;sub<64;sub++){
  auto val=observation[selected[i]][selected[6*half+__builtin_ctz((unsigned)sub)]];
  for(int j=0;j<4;j++)pre[half][i][sub][j]=pre[half][i][sub&(sub-1)][j]|val[j];
 }
 for(int subset=1;subset<4095;subset+=2){
  int k=__builtin_popcount((unsigned)subset);
  if(cost-minima[k]-minima[size-k]<gain && cost-minima[k]-minima[size-k]<=runner)continue;
  int fine=0;
  for(int i=0;i<12;i++){int mask=(subset>>i)&1?subset:4095^subset;
   for(int j=0;j<4;j++)fine+=__builtin_popcountll(pre[0][i][mask&63][j]|pre[1][i][mask>>6][j]);
  }
  if(cost-fine<gain)runner=std::max(runner,cost-fine);
  if(cost-fine>gain)throw std::runtime_error("larger gain");
  if(cost-fine==gain){std::cout<<cost<<" "<<subset;for(int i=0;i<12;i++)std::cout<<" "<<selected[i];std::cout<<"\n";}
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
    if(argc!=2)return 2;
    std::ifstream in(argv[1], std::ios::binary);
    if (!in.read(reinterpret_cast<char *>(observation), sizeof(observation))) return 3;

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
    std::cerr<<visits[12]<<" "<<runner<<"\n";
}
