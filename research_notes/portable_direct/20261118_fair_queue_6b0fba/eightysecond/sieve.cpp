// Classify affordable denominator multisets by exact finite residue tuples.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <vector>

using Key = std::uint64_t;
using Residues = std::array<Key, 6>;
using Counts = std::vector<unsigned char>;

class BudgetLayer {
    int budget{}, size{};
    Key expected{};
    Residues moduli{};
    std::vector<int> denominators;
    std::vector<Residues> columns;
    std::vector<Key> keys, repeated;
    std::unordered_map<Key, Counts> first_in_class;
    Counts counts, ambiguous;
    bool compare = false;

    void record(const Residues& residues) {
        Key key = 0;
        for (int j = 0; j < 6; ++j)
            key = key * moduli[j] + residues[j];
        if (!compare) {
            keys.push_back(key);
            return;
        }
        if (!std::binary_search(repeated.begin(), repeated.end(), key)) return;
        auto [it, inserted] = first_in_class.try_emplace(key, counts);
        if (!inserted)
            for (int i = 0; i < size; ++i)
                if (it->second[i] != counts[i]) ambiguous[i] = 1;
    }

    void visit(int start, int remaining, const Residues& residues) {
        record(residues);
        for (int i = start; i < size && denominators[i]-1 <= remaining; ++i) {
            Residues next;
            for (int j = 0; j < 6; ++j) {
                next[j] = residues[j] + columns[i][j];
                if (next[j] >= moduli[j]) next[j] -= moduli[j];
            }
            ++counts[i];
            visit(i, remaining - (denominators[i]-1), next);
            --counts[i];
        }
    }

public:
    void run() {
        std::cin >> budget >> size >> expected;
        for (Key& m : moduli) std::cin >> m;
        denominators.resize(size);
        columns.resize(size);
        counts.resize(size);
        ambiguous.resize(size);
        for (int i = 0; i < size; ++i) {
            std::cin >> denominators[i];
            for (Key& a : columns[i]) std::cin >> a;
            if (budget / (denominators[i]-1) > 255)
                throw std::runtime_error("multiplicity exceeds encoding");
        }
        keys.reserve(expected);
        visit(0, budget, Residues{});
        if (keys.size() != expected) throw std::runtime_error("partition count mismatch");
        std::sort(keys.begin(), keys.end());
        Key distinct = 0;
        for (std::size_t i = 0; i < keys.size();) {
            std::size_t end = i+1;
            while (end < keys.size() && keys[end] == keys[i]) ++end;
            if (end-i > 1) repeated.push_back(keys[i]);
            ++distinct;
            i = end;
        }
        std::vector<Key>().swap(keys);
        if (!repeated.empty()) {
            compare = true;
            visit(0, budget, Residues{});
        }
        std::cout << expected << " " << distinct << " " << repeated.size() << "\n";
        for (int i = 0; i < size; ++i)
            if (ambiguous[i]) std::cout << denominators[i] << " ";
        std::cout << "\n";
    }
};

int main() {
    BudgetLayer layer;
    layer.run();
}
