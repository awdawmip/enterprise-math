// Exhaust all completions of one disjoint pair of cost-1104 twelve-point rows.
// Input rows are from the complete native one-probe class census.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

using Mask = __uint128_t;
using Word = std::uint64_t;
constexpr Mask SPACE = (Mask(1) << 125) - 1;
std::array<Mask,15> slices{};
std::uint64_t nodes;

int first(Mask mask) {
    Word low=static_cast<Word>(mask);
    return low ? __builtin_ctzll(low) : 64 + __builtin_ctzll(static_cast<Word>(mask >> 64));
}
int count(Mask mask) {
    return __builtin_popcountll(static_cast<Word>(mask)) + __builtin_popcountll(static_cast<Word>(mask >> 64));
}
struct Row {
    Mask mask;
    bool nine;
    std::array<int,3> singleton{};
};
std::vector<Row> rows;
bool search(Mask free, int nines, int tens, const std::vector<int>& pool) {
    ++nodes;
    if (!free) return nines == 0 && tens == 0;
    std::array<int,15> needed{}, donors{};
    std::array<int,125> frequencies{};
    for (int j=0; j<15; ++j) {
        needed[j] = 2*(nines+tens) - count(free & slices[j]);
        if (needed[j] < 0 || needed[j] > nines) return false;
    }
    std::vector<int> admissible;
    Mask covered=0;
    int ten_options=0;
    for (int k:pool) {
        const Row& row=rows[k];
        if ((row.mask & free) != row.mask || (row.nine ? nines : tens) == 0) continue;
        if (row.nine) {
            bool possible=true;
            for (int j=0; j<15; ++j) {
                bool singleton=(row.singleton[j/5] == j);
                if ((singleton && needed[j]==0) || (!singleton && needed[j]==nines)) possible=false;
            }
            if (!possible) continue;
            for (int j:row.singleton) ++donors[j];
        } else {
            ++ten_options;
        }
        admissible.push_back(k);
        covered |= row.mask;
        for (Mask m=row.mask; m; m &= m-1) ++frequencies[first(m)];
    }
    if (covered != free) return false;
    int pivot=-1, fewest=1000000;
    for (Mask m=free; m; m &= m-1) {
        int p=first(m);
        if (frequencies[p] < fewest) {fewest=frequencies[p]; pivot=p;}
    }
    // A slice with demand one is another exact-one constraint, as is the last ten-row.
    for (int j=0;j<15;++j) {
        if (donors[j] < needed[j]) return false;
        if (needed[j] == 1 && donors[j] < fewest) {fewest=donors[j]; pivot=125+j;}
    }
    if (tens == 1 && ten_options < fewest) pivot=140;
    for (int k:admissible) {
        const Row& row=rows[k];
        if (pivot < 125 && !(row.mask & (Mask(1)<<pivot))) continue;
        if (pivot >= 125 && pivot < 140 &&
            (!row.nine || row.singleton[(pivot-125)/5] != pivot-125)) continue;
        if (pivot == 140 && row.nine) continue;
        if (search(free ^ row.mask, nines-row.nine, tens-!row.nine, admissible)) return true;
    }
    return false;
}

int main(int argc,char**argv) {
    std::ifstream input(argv[1]);
    int types;
    input >> types;
    for (int p=0;p<125;++p) {
        Mask point=Mask(1)<<p;
        slices[p/25] |= point;
        slices[5+p/5%5] |= point;
        slices[10+p%5] |= point;
    }
    while (types--) {
        int size,price,number;
        input >> size >> price >> number;
        while (number--) {
            Word low,high;
            input >> low >> high;
            if (price != 557 && price != 744) continue;
            if (argc > 3 && price == 744) continue;
            Row row{(Mask(high)<<64)|low,size==9,{}};
            if (row.nine) for (int j=0;j<15;++j)
                if (count(row.mask & slices[j]) == 1) row.singleton[j/5]=j;
            rows.push_back(row);
        }
    }
    std::ifstream anchors(argv[2]);
    Word lo,hi,ll,hh;
    while (anchors>>lo>>hi>>ll>>hh) {
        Mask used=(Mask(hi)<<64)|lo|(Mask(hh)<<64)|ll;
        std::vector<int> pool;
        for (int i=0;i<static_cast<int>(rows.size());++i) if (!(rows[i].mask&used)) pool.push_back(i);
        nodes=0;
        bool found=search(SPACE^used,argc>3?11:9,argc>3?0:2,pool);
        std::cout << pool.size() << ' ' << nodes << ' ' << found << std::endl;
    }
}
