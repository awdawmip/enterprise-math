// Test all sets of near-full classes of a given cardinality through a fixed parent.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>

using Mask = __uint128_t;
struct Option { Mask occupied; int full; int peripheral; };
std::array<Mask, 250> parents;
std::array<int, 250> centres;
std::vector<int> chosen;
int count_wanted;
long long parent_sets, feasible_sets, assignments;
bool attained[10][10]{};

int size(Mask m) {
    return __builtin_popcountll(std::uint64_t(m)) + __builtin_popcountll(std::uint64_t(m >> 64));
}

void choose_omissions(const std::vector<std::vector<Option>>& options, int j, Mask used,
                      int full_count, int peripheral) {
    if (j == count_wanted) {
        ++assignments;
        attained[full_count][peripheral] = true;
        return;
    }
    for (auto option : options[j])
        if (!(option.occupied & used))
            choose_omissions(options, j + 1, used | option.occupied, full_count + option.full,
                             peripheral + option.peripheral);
}

void complete_parent_set() {
    ++parent_sets;
    Mask seen = 0, overlap = 0;
    for (int id : chosen) {
        overlap |= seen & parents[id];
        seen |= parents[id];
    }
    std::vector<std::vector<Option>> options(count_wanted);
    for (int j = 0; j < count_wanted; ++j) {
        const int id = chosen[j];
        const Mask p = parents[id];
        const Mask core = p ^ (Mask(1) << centres[id]);
        auto& v = options[j];
        v.push_back({p & overlap, 1, 0});
        v.push_back({core & overlap, 0, 0});
        // Deleting a shared peripheral point changes its occupied mask.
        for (Mask t = core & overlap; t; t &= t - 1)
            v.push_back({(p ^ (t & -t)) & overlap, 0, 1});
        // All private peripheral points give the same feasibility and cost.
        if (core & ~overlap) v.push_back({p & overlap, 0, 1});
    }
    std::sort(options.begin(), options.end(), [](auto& a, auto& b){ return a.size() > b.size(); });
    const auto before = assignments;
    choose_omissions(options, 0, 0, 0, 0);
    if (before != assignments) {
        ++feasible_sets;
        if (count_wanted == 8) {
            for (int id : chosen) std::cout << id << ' ';
            std::cout << '\n';
        }
    }
}

void extend(const std::vector<int>& candidates, Mask used) {
    const int n = chosen.size(), needed = count_wanted - n;
    if (!needed) { complete_parent_set(); return; }
    for (int j = 0; j + needed <= int(candidates.size()); ++j) {
        const int id = candidates[j];
        Mask next_used = used | parents[id];
        // Each selected class can discard at most one point of its parent.
        // The union defect never decreases when a parent is added.
        if (13 * (n + 1) - size(next_used) > count_wanted) continue;
        std::vector<int> next;
        for (int l = j + 1; l < int(candidates.size()); ++l) {
            int p = candidates[l];
            if (13 * (n + 2) - size(next_used | parents[p]) <= count_wanted) next.push_back(p);
        }
        if (int(next.size()) < needed - 1) continue;
        chosen.push_back(id); extend(next, next_used); chosen.pop_back();
    }
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    count_wanted = std::stoi(argv[1]);
    std::ifstream f(argv[2]);
    std::uint64_t lo, hi;
    for (int i = 0; i < 250; ++i) {
        if (!(f >> lo >> hi >> centres[i])) return 3;
        parents[i] = (Mask(hi)<<64) | lo;
    }
    std::vector<int> candidates;
    for (int i = 1; i < 250; ++i) candidates.push_back(i);
    chosen = {0}; extend(candidates, parents[0]);
    std::cout << "counts " << parent_sets << ' ' << feasible_sets << '\n';
    for (int full = 0; full <= count_wanted; ++full)
        for (int peripheral = 0; peripheral <= count_wanted-full; ++peripheral)
            if (attained[full][peripheral]) std::cout << "support " << full << ' ' << peripheral << '\n';
}
