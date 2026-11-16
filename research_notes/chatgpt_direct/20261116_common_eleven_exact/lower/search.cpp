// Exact cover of 125 histories with a prescribed multiset of class types.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>

using Mask = __uint128_t;
constexpr Mask full = (Mask(1) << 125) - 1;
struct Class {
    Mask mask;
    std::vector<int> points;
};
struct Type {
    int size, cost;
    std::vector<int> ids, representatives;
};
using Pools = std::vector<std::vector<int>>;
std::vector<Type> types;
std::vector<Class> classes;
std::uint64_t nodes;

int first(Mask mask) {
    auto low = static_cast<std::uint64_t>(mask);
    return low ? __builtin_ctzll(low) : 64 + __builtin_ctzll(static_cast<std::uint64_t>(mask >> 64));
}

bool cover(Mask free, int left, std::vector<int>& needed, const Pools& pool) {
    ++nodes;
    if (!left) return free == 0;
    if (left == 1) {
        for (std::size_t t = 0; t < types.size(); ++t) {
            if (!needed[t]) continue;
            for (int id : pool[t]) if (classes[id].mask == free) return true;
        }
        return false;
    }

    Pools options(types.size());
    int counts[125]{};
    int pivot_type = -1, pivot_point = -1, minimum = std::numeric_limits<int>::max();
    for (int t = 0; t < static_cast<int>(types.size()); ++t) {
        if (!needed[t]) continue;
        for (int id : pool[t]) {
            if ((classes[id].mask & free) != classes[id].mask) continue;
            options[t].push_back(id);
            for (int p : classes[id].points) ++counts[p];
        }
        int available = options[t].size();
        if (available < needed[t]) return false;
        if (available < minimum) {
            minimum = available;
            pivot_type = t;
        }
    }
    for (Mask bits = free; bits; bits &= bits - 1) {
        int p = first(bits);
        if (!counts[p]) return false;
        if (counts[p] < minimum) {
            minimum = counts[p];
            pivot_point = p;
            pivot_type = -1;
        }
    }

    for (int t = 0; t < static_cast<int>(types.size()); ++t) {
        if (!needed[t] || (pivot_type >= 0 && pivot_type != t)) continue;
        --needed[t];
        for (std::size_t i = 0; i < options[t].size(); ++i) {
            int id = options[t][i];
            if (pivot_type < 0 && !((classes[id].mask >> pivot_point) & 1)) continue;
            // At a type pivot, take the least ID of this type in the completion.
            // A point pivot fixes the unique class containing the chosen point.
            if (pivot_type >= 0 && needed[t]) {
                auto saved = std::move(options[t]);
                options[t].assign(saved.begin() + i + 1, saved.end());
                bool found = cover(free ^ classes[id].mask, left - 1, needed, options);
                options[t] = std::move(saved);
                if (found) return true;
            } else if (cover(free ^ classes[id].mask, left - 1, needed, options)) {
                return true;
            }
        }
        ++needed[t];
    }
    return false;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    std::ifstream database(argv[1]);
    int n;
    if (!(database >> n)) return 3;
    types.resize(n);
    for (auto& type : types) {
        int total;
        database >> type.size >> type.cost >> total;
        for (int j = 0; j < total; ++j) {
            int rep;
            std::uint64_t low, high;
            database >> low >> high >> rep;
            Mask mask = (Mask(high) << 64) | low;
            int id = classes.size();
            classes.push_back({mask, {}});
            for (Mask b = mask; b; b &= b - 1) classes.back().points.push_back(first(b));
            type.ids.push_back(id);
            if (rep) type.representatives.push_back(id);
        }
    }
    int cost;
    while (std::cin >> cost) {
        std::vector<int> needed(n);
        Pools pool(n);
        int left = 0, first_type = -1;
        for (int t = 0; t < n; ++t) {
            std::cin >> needed[t];
            left += needed[t];
            if (!needed[t]) continue;
            pool[t] = types[t].ids;
            auto order = [&](int i) {
                return std::make_pair(types[i].representatives.size(), types[i].ids.size());
            };
            if (first_type < 0 || order(t) < order(first_type)) first_type = t;
        }
        nodes = 0;
        bool found = false;
        --needed[first_type];
        for (int id : types[first_type].representatives) {
            if (cover(full ^ classes[id].mask, left - 1, needed, pool)) {
                found = true;
                break;
            }
        }
        std::cout << cost << " " << nodes << " " << found << std::endl;
    }
}
