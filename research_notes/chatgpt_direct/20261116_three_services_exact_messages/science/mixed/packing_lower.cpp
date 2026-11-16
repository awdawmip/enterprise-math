// Exclude an eleven-class partition after choosing four to six size-12 classes.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using Mask = __uint128_t;
using Indices = std::vector<int>;
std::vector<Mask> twelve, eleven;
std::array<long long, 7> packings{}, survivors{};

int population(Mask mask) {
    return __builtin_popcountll(static_cast<std::uint64_t>(mask))
         + __builtin_popcountll(static_cast<std::uint64_t>(mask >> 64));
}

int first_bit(Mask mask) {
    auto low = static_cast<std::uint64_t>(mask);
    return low ? __builtin_ctzll(low) : 64 + __builtin_ctzll(static_cast<std::uint64_t>(mask >> 64));
}

Indices disjoint_from(const Indices &candidates, std::size_t begin,
                      const std::vector<Mask> &classes, Mask chosen) {
    Indices result;
    for (std::size_t i = begin; i < candidates.size(); ++i) {
        int j = candidates[i];
        if (!(classes[j] & chosen)) result.push_back(j);
    }
    return result;
}

// Classes containing a common point form one group, of which at most one can be selected.
bool enough_groups(const Indices &pool, int need) {
    std::vector<Mask> left;
    for (int j : pool) left.push_back(eleven[j]);
    for (int k = 0; k < need; ++k) {
        if (left.empty()) return false;
        std::array<int, 125> frequency{};
        for (Mask mask : left)
            for (Mask m = mask; m; m &= m - 1) ++frequency[first_bit(m)];
        const auto pos = std::max_element(frequency.begin(), frequency.end()) - frequency.begin();
        Mask bit = Mask(1) << pos;
        left.erase(std::remove_if(left.begin(), left.end(),
                                 [bit](Mask row){return (row & bit) != 0;}), left.end());
    }
    return true;
}

bool pack_eleven(const Indices &pool, int need) {
    if (need == 0) return true;
    if (int(pool.size()) < need || !enough_groups(pool, need)) return false;
    for (std::size_t k = 0; k + need <= pool.size(); ++k) {
        const auto tail = disjoint_from(pool, k + 1, eleven, eleven[pool[k]]);
        if (pack_eleven(tail, need - 1)) return true;
    }
    return false;
}

void choose_twelve(int depth, const Indices &remaining, const Indices &small) {
    ++packings[depth];
    if (depth >= 4 && pack_eleven(small, 15 - 2*depth)) ++survivors[depth];
    if (depth == 6) {
        if (!remaining.empty()) throw std::runtime_error("Found seven disjoint size-12 classes");
        return;
    }
    for (std::size_t k=0; k < remaining.size(); ++k) {
        Mask row = twelve[remaining[k]];
        const auto children = disjoint_from(remaining, k+1, twelve, row);
        if (depth+1+children.size() < 4) continue;
        choose_twelve(depth+1, children, disjoint_from(small, 0, eleven, row));
    }
}

int main(int argc, char **argv) {
    if (argc != 3) return 1;
    std::ifstream in(argv[1]), seeds(argv[2]);
    if (!in || !seeds) return 2;
    std::string decimal;
    while (in >> decimal) {
        Mask row=0;
        for (char c : decimal) row=10*row + c-'0';
        if (population(row)==12) twelve.push_back(row);
        else if (population(row)==11) eleven.push_back(row);
        else return 3;
    }
    int seed;
    while (seeds >> seed) {
        const Mask chosen=twelve.at(seed);
        Indices big, small;
        for (std::size_t i=0; i<twelve.size(); ++i) if (!(chosen & twelve[i])) big.push_back(i);
        for (std::size_t i=0; i<eleven.size(); ++i) if (!(chosen & eleven[i])) small.push_back(i);
        choose_twelve(1, big, small);
    }
    for (int d=4; d<=6; ++d) std::cout << d << ' ' << packings[d] << ' ' << survivors[d] << '\n';
}
