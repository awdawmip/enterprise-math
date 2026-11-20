#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector>
using Mask = std::uint32_t;
struct Part { Mask mask; int labels; };
int size(Mask m) { return __builtin_popcount(m); }
std::vector<Part> small, origins;
std::vector<int> at[32];
std::vector<Mask> large[14];
std::unordered_set<Mask> available;
long long nodes;
bool solve_small(Mask free, int labels) {
    ++nodes;
    if (!labels) return !free;
    if (!free || 4*size(free)>12*labels) return false;
    int pivot=-1, fewest=100000;
    for (Mask b=free; b; b&=b-1) {
        int bit=__builtin_ctz(b), count=0;
        for (int i:at[bit]) {
            Part row=small[i];
            if (row.labels<=labels && !(row.mask&~free) &&
                4*(size(free)-size(row.mask))<=12*(labels-row.labels)) ++count;
            if (count>=fewest) break;
        }
        if (!count) return false;
        if (count<fewest) { fewest=count; pivot=bit; }
    }
    for(int i:at[pivot]) {
        Part row=small[i];
        if (row.labels<=labels && !(row.mask&~free) && solve_small(free^row.mask,labels-row.labels)) return true;
    }
    return false;
}
int main(int argc,char**argv) {
    if (argc!=4) return 2;
    for (int j=1;j<=3;++j) {
        std::ifstream file(argv[j]);Mask q;int cost;std::uint64_t lo,hi;
        while (file>>q>>cost) {
            if (j>1) file>>lo>>hi;
            if (q&1) { if (j!=1) return 3; origins.push_back({q,1}); }
            else if (j<3) small.push_back({q,j});
            else { large[size(q)].push_back(q); available.insert(q); }
        }
    }
    for(int j=0;j<(int)small.size();j++) {
        auto r=small[j];
        if (4*size(r.mask)>12*r.labels) return 4;
        for(Mask b=r.mask;b;b&=b-1) at[__builtin_ctz(b)].push_back(j);
    }
    // Without a free four-label orbit, all eleven classes are fixed or paired.
    bool found=false;nodes=0;
    for(auto first:origins) found |= solve_small(~first.mask,10);
    long long zero=nodes,one_residuals=0;nodes=0;
    // The seven small labels occupy at most 13+6*12=85 points,
    // so the one remaining free representative must have size >=10.
    for (int s=10;s<=13;s++) for (Mask q:large[s]) for(auto a:origins) {
        if (q&a.mask) continue;
        Mask rest=~(q|a.mask);
        if (4*size(rest)>72) continue;
        ++one_residuals;found |= solve_small(rest,6);
    }
    long long one=nodes,two_shapes=0,two_options=0;int min_two_rest=32;
    for (auto first:origins) {
        for(int i=0;i<(int)small.size();i++) {
            auto a=small[i];if(a.mask&first.mask)continue;
            auto pair_check=[&](Mask free) {
                int n=size(free);min_two_rest=std::min(min_two_rest,n);
                if(n<23){std::cerr<<"two-list bound invalid";std::exit(5);}++two_shapes;
                for(int s=10;s<=13;s++) {
                    int t=n-s;if(t<s||t>13)continue;
                    for(Mask row:large[t]) {
                        if(row&~free)continue;++two_options;
                        if(available.count(free^row))found=true;
                    }
                }
            };
            if(a.labels==2)pair_check(~(first.mask|a.mask));
            else for(int j=i+1;j<(int)small.size();j++) {
                auto b=small[j];if (b.labels==1 && !(b.mask&(a.mask|first.mask)))pair_check(~(first.mask|a.mask|b.mask));
            }
        }
    }
    std::cout<<zero<<' '<<one<<' '<<one_residuals<<' '<<two_shapes<<' '<<two_options<<' '<<min_two_rest<<' '<<found<<'\n';
}
