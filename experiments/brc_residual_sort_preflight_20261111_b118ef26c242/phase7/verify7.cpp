#define main preceding_verify7_entry
#include "pure_bench.cpp"
#undef main
#include "local_kernels.hpp"
#include "sampled_kernels.hpp"
#include "robust_kernels.hpp"
#include "adaptive_kernels.hpp"
#include "selection_kernels.hpp"
#include "certified_kernels.hpp"
#include "../phase5/probe.hpp"
#include "../phase6/child.hpp"
#include "parent_grid.hpp"
#include <set>

void expect(bool x) { if(!x) throw std::runtime_error("verification mismatch"); }
int main() {
    using brc_sampled_detail::Grid;
    const std::vector<std::pair<Grid,std::vector<u64>>> edges={
        {{0,0,2},{0,0,1,1}}, {{0,63,2},{0,0,MAX_VALUE,MAX_VALUE}},
        {{MAX_VALUE-1,0,2},{MAX_VALUE,MAX_VALUE-1,0}},
        {{0,0,1},{0,1}}, {{0,4,2},{0,15,16,31}}, {{0,63,2},{MAX_VALUE}},
        {{0,1,2},{}}, {{32,4,3},{34,32,35,34,46}}, {{32,4,3},{31,35,34,32}}};
    std::size_t local=0, full=0;
    auto check_local=[&](Grid grid,const std::vector<u64>& input) {
        auto v=input;
        ProbeRow row{};
        const bool ok=brc_inherited::count_with_parent_grid(v,grid,row);
        std::vector<std::set<u64>> sets(grid.bucket_count);
        bool possible=true;
        for(u64 x:input) {
            const u64 p=x>>grid.shift, first=grid.origin>>grid.shift;
            if(p<first || p-first>=sets.size()) {possible=false;continue;}
            sets[p-first].insert(x);
        }
        u128 slots=0;
        for(auto& s:sets) if(!s.empty()) slots+=u128(*s.rbegin())-*s.begin()+1;
        possible=possible && slots<=std::min<std::size_t>(COUNTER_CAP,input.size());
        expect(ok==possible);
        auto target=input;
        if(ok) std::sort(target.begin(),target.end());
        expect(target==v);
        ++local;
    };
    for(auto& [grid,a]:edges) check_local(grid,a);
    std::mt19937_64 rng(0x71371811);
    for(unsigned trial=0;trial<256;++trial) {
        const unsigned shift=rng()%12;
        const u64 block=u64(1)<<shift;
        Grid g{(rng()%6)*block,shift,unsigned(1+rng()%9)};
        std::vector<u64> a(1+rng()%300);
        for(auto& x:a) x=g.origin+(rng()%(g.bucket_count+1))*block+rng()%std::min<u64>(block,9);
        if(trial%2) for(auto& x:a) x=g.origin+(rng()%g.bucket_count)*block;
        check_local(g,a);
    }
    for(auto n:{0,1,100,256,257,16384,32767,32768,32769,65536,125000}) {
        for(unsigned family=0;family<7;++family) {
            std::vector<u64> a(n);
            for(auto& x:a) {
                auto k=rng();
                switch(family) {
                    case 0:x=k;break;
                    case 1:x=MAX_VALUE-k%100;break;
                    case 2:x=0;break;
                    case 3:x=(k%3)*(u64(1)<<32)+rng()%3000;break;
                    case 4:x=k%2?0:MAX_VALUE;break;
                    case 5:x=(k%3)*(u64(1)<<24)+rng()%30000;break;
                    default:x=k%7?rng()%199:k;break;
                }
            }
            auto expected=a;std::sort(expected.begin(),expected.end());
            ProbeStats stats;stats.rows.emplace_back();stats.rows[0].n=123456789;
            for(bool diag:{false,true}) {
                auto v=a;
                parent_grid_sort(v,198,diag?&stats:nullptr);
                expect(v==expected);++full;
            }
            expect(stats.rows[0].n==123456789);
        }
    }
    std::cout<<"local_span_oracles="<<local<<" full_output_checks="<<full<<" PASS\n";
}
