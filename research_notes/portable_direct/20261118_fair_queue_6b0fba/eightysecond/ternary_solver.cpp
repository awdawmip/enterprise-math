// Portable exact finite multiset enumeration. Both modes read their integer data on stdin.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
#include <vector>

using Row = std::array<unsigned, 6>;
using Key = std::uint64_t;
struct Atom { int cost; Row value; };
struct Query { int id, left, right; Row offset; };

Key pack(const Row& value, const Row& mod, int length) {
    Key key = 0;
    for (int j = 0; j < length; ++j) key = key * mod[j] + value[j];
    return key;
}

Row plus(const Row& a, const Row& b, const Row& mod) {
    Row sum{};
    for (int j = 0; j < 6; ++j) {
        sum[j] = a[j] + b[j];
        if (sum[j] >= mod[j]) sum[j] -= mod[j];
    }
    return sum;
}

Row minus(const Row& a, const Row& b, const Row& mod) {
    Row diff{};
    for (int j = 0; j < 6; ++j) diff[j] = (a[j] + mod[j] - b[j]) % mod[j];
    return diff;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int mode, count, budget, omitted, nqueries;
    std::cin >> mode >> count >> budget >> omitted >> nqueries;
    Row mod;
    for (auto& x : mod) std::cin >> x;
    std::vector<Atom> atoms(count);
    for (auto& atom : atoms) {
        int d;
        std::cin >> d;
        atom.cost = d - 1;
        for (auto& x : atom.value) std::cin >> x;
    }
    // At each node the next atom has index no smaller than the preceding one.
    // The tail is in increasing cost order, so all affordable multisets occur exactly once.
    std::vector<unsigned char> digits(count);
    auto visit = [&](auto&& self, auto& emit, int first, int spent, Row value) -> void {
        emit(spent, value);
        for (int i = first; i < count && spent + atoms[i].cost <= budget; ++i) {
            ++digits[i];
            self(self, emit, i, spent + atoms[i].cost, plus(value, atoms[i].value, mod));
            --digits[i];
        }
    };
    if (mode == 0) {
        std::vector<Key> keys, repeated;
        auto collect = [&](int, Row value) { keys.push_back(pack(value, mod, 6)); };
        visit(visit, collect, 0, 0, Row{});
        std::sort(keys.begin(), keys.end());
        int distinct = 0;
        for (std::size_t i = 0; i < keys.size();) {
            std::size_t j = i + 1;
            while (j < keys.size() && keys[i] == keys[j]) ++j;
            if (j > i+1) repeated.push_back(keys[i]);
            ++distinct;
            i = j;
        }
        std::cout << keys.size() << ' ' << distinct << ' ' << repeated.size() << '\n';
        std::vector<Key>().swap(keys);
        struct Member { int spent; std::vector<unsigned char> digits; };
        std::map<Key, std::vector<Member>> members;
        auto collect_repeated = [&](int spent, Row value) {
            Key key = pack(value, mod, 6);
            if (std::binary_search(repeated.begin(), repeated.end(), key))
                members[key].push_back({spent, digits});
        };
        visit(visit, collect_repeated, 0, 0, Row{});
        int total_pairs = 0, disjoint = 0;
        for (const auto& group : members) {
            const auto& items = group.second;
            for (std::size_t i = 0; i < items.size(); ++i) {
                for (std::size_t j = i+1; j < items.size(); ++j) {
                    const auto& a = items[i]; const auto& b = items[j];
                    ++total_pairs;
                    bool overlap = false;
                    for (int t = 0; t < count; ++t)
                        if (a.digits[t] && b.digits[t]) { overlap = true; break; }
                    if (overlap) continue;
                    ++disjoint;
                    std::cout << budget-a.spent << ' ' << budget-b.spent;
                    for (const auto* side : {&a,&b}) {
                        for (auto v : side->digits) std::cout << ' ' << static_cast<int>(v);
                    }
                    std::cout << '\n';
                }
            }
        }
        std::cout << total_pairs << ' ' << disjoint << '\n';
        return 0;
    }

    std::vector<Query> queries(nqueries);
    for (auto& q : queries) {
        std::cin >> q.id >> q.left >> q.right;
        for (auto& x : q.offset) std::cin >> x;
    }
    int free_rows = 6 - omitted;
    struct Item { Key key; Row value; int spent; };
    std::vector<Key> ways(budget + 1);
    ways[0] = 1;
    for (int i=omitted; i<count; ++i)
        for (int n=atoms[i].cost; n<=budget; ++n) ways[n] += ways[n-atoms[i].cost];
    std::size_t total = 0;
    for (Key c : ways) total += c;
    std::vector<Item> items;
    items.reserve(total);
    auto emit = [&](int spent, Row value) { items.push_back({pack(value,mod,free_rows),value,spent}); };
    visit(visit,emit,omitted,0,Row{});
    if (total!=items.size()) return 1;
    std::sort(items.begin(),items.end(),[](const Item& a,const Item& b){return a.key<b.key;});
    std::cout << total << '\n';
    for (const auto& q : queries) {
        bool found = false;
        for (const auto& left : items) {
            if (left.spent>q.left) continue;
            Row right_value=minus(left.value,q.offset,mod);
            Key key=pack(right_value,mod,free_rows);
            auto it=std::lower_bound(items.begin(),items.end(),key,
                                      [](const Item& a,Key b){return a.key<b;});
            for (; it!=items.end() && it->key==key; ++it) {
                if (it->spent>q.right) continue;
                Row needed=minus(plus(q.offset,it->value,mod),left.value,mod);
                // Recover signed pivot multiplicities from the shortest modulus upwards.
                auto restore = [&](auto&& self,int t,int left_money,int right_money,Row residual)->bool {
                    if (t<0) return true;
                    int j=5-t, cost=atoms[t].cost;
                    int low=-(right_money/cost), high=left_money/cost;
                    int modulus=mod[j], first=residual[j];
                    first -= ((first-low)/modulus)*modulus; // low<=0<=the original first
                    for (int z=first; z<=high; z+=modulus) {
                        Row next=residual;
                        for (int u=j+1;u<6;++u) {
                            std::int64_t value=std::int64_t(z)*atoms[t].value[u];
                            next[u]=(std::int64_t(residual[u])-value%mod[u]+mod[u])%mod[u];
                        }
                        if(self(self,t-1,left_money-std::max(z,0)*cost,
                                right_money-std::max(-z,0)*cost,next)) return true;
                    }
                    return false;
                };
                if (restore(restore,omitted-1,q.left-left.spent,q.right-it->spent,needed)) {
                    found=true;
                    break;
                }
            }
            if (found) break;
        }
        std::cout << q.id << ' ' << found << '\n';
    }
}
