// Exact mixed-radix membership and multiplicity queries for a common dyadic layer.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>

using Word = std::uint64_t;
using Signature = std::array<Word, 6>;

struct Atom {
    int cost;
    Signature signature;
};
struct Query {
    int id, left_budget, right_budget;
    Signature difference;
};

class Layer {
    Signature moduli;
    std::vector<Atom> atoms;
    using Counts = std::vector<short>;
    Word encode(const Signature& s) const {
        Word key = 0;
        for (std::size_t j = 0; j < s.size(); ++j)
            key = key * moduli[j] + s[j];
        return key;
    }
    Signature add(const Signature& a, const Signature& b) const {
        Signature c;
        for (std::size_t j = 0; j < c.size(); ++j)
            c[j] = (a[j] + b[j]) % moduli[j];
        return c;
    }
    template<class Visitor>
    void multisets(std::size_t first, int left, const Signature& s,
                   Counts& word, Visitor& visit) const {
        visit(s, left, word);
        for (std::size_t j = first; j < atoms.size() && atoms[j].cost <= left; ++j) {
            ++word[j];
            multisets(j, left-atoms[j].cost, add(s, atoms[j].signature), word, visit);
            --word[j];
        }
    }
    // The DFS lists the current word before any of its longer extensions.
    Counts unrank(Word rank, int budget, const std::vector<std::vector<Word>>& sizes) const {
        Counts word(atoms.size());
        std::size_t first = 0;
        while (rank) {
            --rank;
            bool chosen = false;
            for (std::size_t j = first; j < atoms.size() && atoms[j].cost <= budget; ++j) {
                int residual = budget-atoms[j].cost;
                if (rank >= sizes[j][residual]) {
                    rank -= sizes[j][residual];
                } else {
                    ++word[j];
                    first = j;
                    budget = residual;
                    chosen = true;
                    break;
                }
            }
            assert(chosen);
        }
        return word;
    }

public:
    Layer(Signature mod, std::vector<Atom> input) : moduli(mod), atoms(input) {}
    void run(const std::vector<Query>& queries) const {
        int max_budget = 0;
        for (const Query& q : queries) max_budget = std::max(max_budget, q.right_budget);
        Word max_key = 1;
        for (Word m : moduli) {
            assert(m && max_key <= UINT64_MAX / m);
            max_key *= m;
        }
        assert(max_budget/atoms.front().cost < INT16_MAX);
        std::vector<std::vector<Word>> sizes(atoms.size()+1,
                                             std::vector<Word>(max_budget+1,1));
        for (int i = int(atoms.size())-1; i >= 0; --i)
            for (int b = 0; b <= max_budget; ++b)
                sizes[i][b] = sizes[i+1][b] + (b >= atoms[i].cost ? sizes[i][b-atoms[i].cost] : 0);

        struct Request { Word key; int id; Word rank; };
        std::vector<Request> requests;
        std::vector<Word> matches(queries.size()), tested(queries.size());
        std::vector<std::set<Counts>> differences(queries.size());
        Counts word(atoms.size());
        for (const Query& q : queries) {
            auto collect = [&](const Signature& s, int, const Counts&) {
                requests.push_back({encode(add(s,q.difference)),q.id,tested[q.id]++});
            };
            multisets(0,q.left_budget,{},word,collect);
            assert(tested[q.id]==sizes[0][q.left_budget]);
        }
        std::sort(requests.begin(),requests.end(),[](const Request& a,const Request& b) {
            return a.key < b.key;
        });
        Word visited = 0;
        auto match = [&](const Signature& s, int left, const Counts& rhs) {
            ++visited;
            Word key = encode(s);
            auto it = std::lower_bound(requests.begin(),requests.end(),key,
                [](const Request& item, Word target) { return item.key < target; });
            for (; it != requests.end() && it->key == key; ++it) {
                const Query& q = queries[it->id];
                if (max_budget-left > q.right_budget) continue;
                ++matches[q.id];
                Counts delta = unrank(it->rank,q.left_budget,sizes);
                for (std::size_t j = 0; j < delta.size(); ++j) delta[j] -= rhs[j];
                differences[q.id].insert(delta);
            }
        };
        multisets(0,max_budget,{},word,match);
        assert(visited==sizes[0][max_budget]);
        std::cout << max_budget << " " << visited << "\n";
        for (const Query& q : queries) {
            std::cout << q.id << " " << tested[q.id] << " " << matches[q.id] << " "
                      << differences[q.id].size() << "\n";
            for (const Counts& delta : differences[q.id]) {
                for (short x : delta) std::cout << x << " ";
                std::cout << "\n";
            }
        }
    }
};

int main() {
    int n, k;
    if (!(std::cin >> n >> k)) return 1;
    Signature mod;
    for (Word& m : mod) std::cin >> m;
    std::vector<Atom> atoms(n);
    for (Atom& atom : atoms) {
        int denominator;
        std::cin >> denominator;
        atom.cost = denominator - 1;
        for (Word& x : atom.signature) std::cin >> x;
    }
    std::vector<Query> queries(k);
    for (Query& q : queries) {
        std::cin >> q.id >> q.left_budget >> q.right_budget;
        for (Word& x : q.difference) std::cin >> x;
    }
    if (!std::cin) return 1;
    Layer(mod, atoms).run(queries);
}
