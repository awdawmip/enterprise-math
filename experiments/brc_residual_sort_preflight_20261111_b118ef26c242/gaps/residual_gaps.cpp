#include "build/frozen_phase5.hpp"
#include <map>

namespace diagnostic {
struct Cut { u64 empty; std::size_t after; };
struct Span {
    u64 low{}, high{};
    std::size_t occurrences{};
    void add(u64 x) {
        if(!occurrences) low=high=x;
        else {low=std::min(low,x); high=std::max(high,x);}
        ++occurrences;
    }
};
std::string decimal(u128 x) {
    std::string out;
    do {out.push_back(char('0'+unsigned(x%10))); x/=10;} while(x);
    std::reverse(out.begin(),out.end());
    return out;
}
std::vector<Cut> two_largest(const std::vector<u64>& v) {
    std::vector<Cut> best;
    for(std::size_t j=1;j<v.size();++j) if(v[j]!=v[j-1]) {
        Cut c{v[j]-v[j-1]-1,j};
        if(best.size()==2 && c.empty<=best.back().empty) continue;
        auto it=std::find_if(best.begin(),best.end(),[&](Cut b){return c.empty>b.empty;});
        best.insert(it,c);
        if(best.size()>2) best.pop_back();
    }
    return best;
}
std::vector<Span> partition(const std::vector<u64>& sorted,const std::vector<Cut>& cuts,unsigned k) {
    std::vector<std::size_t> stops;
    for(unsigned i=0;i+1<k && i<cuts.size();++i) stops.push_back(cuts[i].after);
    std::sort(stops.begin(),stops.end());
    stops.push_back(sorted.size());
    std::vector<Span> segments;
    std::size_t begin=0;
    for(std::size_t stop:stops) {
        segments.push_back({sorted[begin],sorted[stop-1],stop-begin});
        begin=stop;
    }
    return segments;
}
void inspect(const pilot_bench::Case& c, unsigned bank, const char* stage,
             std::ofstream& arrays,std::ofstream& spans) {
    const auto v=pilot_bench::make_input(c,bank);
    const auto n=v.size();
    auto model=brc_sampled_detail::learn_sampled<1024,false>(v,nullptr);
    const auto bounds=std::minmax_element(model.sample.begin(),model.sample.end());
    const u64 lo=*bounds.first, hi=*bounds.second;
    const auto root_budget=brc_sampled_detail::cell_budget(n);
    AdaptiveNodeStats adaptive;SelectionNodeStats selection;CertifiedNodeStats certified;
    brc_robust_detail::select_compact_layout<false>(model,lo,hi,model.sample.size(),
                                                     root_budget,false,nullptr,&adaptive.core);
    require(brc_certified_detail::select_certified_gap<false>(model,root_budget,nullptr,
                        adaptive,selection,certified,lo,hi),"frozen model was not selected");
    brc_sampled_detail::assign_offsets(model.buckets);
    std::vector<std::size_t> counts(std::size_t(model.cells),0);
    std::vector<u64> residual;
    SampleStats scan;
    require(brc_sampled_detail::count_sampled<true>(v,model.grid,model.buckets,counts,residual,
            brc_sampled_detail::recursive_spill_budget(n),&scan),"root failed contraction");
    require(scan.processed==n && !residual.empty(),"incomplete root scan");
    std::size_t t=0;
    for(u64 x:v) if(!brc_probe::covered(x,model)) {
        require(t<residual.size() && x==residual[t],"residual order or multiplicity mismatch");++t;
    }
    require(t==residual.size(),"residual not conserved");
    // Ground the three known generator labels, independently of the interval optimizer.
    const u64 source_origin=*std::min_element(v.begin(),v.end()) & ~((u64(1)<<20)-1);
    constexpr u64 gen_width[]={297110,246800,246800};
    std::array<std::size_t,3> source_mass{};
    std::map<u64,Span> coarse;
    for(u64 x:residual) {
        const u64 g=(x-source_origin)>>28;
        require(g<3 && x-(source_origin+(g<<28))<gen_width[g],"source label inconsistent");
        ++source_mass[g];
        coarse[x>>model.grid.shift].add(x);
    }
    u128 coarse_width=0;
    for(const auto& [q,span]:coarse) coarse_width+=u128(span.high)-span.low+1;
    const auto s=residual.size();
    const auto budget=std::min<std::size_t>(s,COUNTER_CAP);
    // Independent constructive check. All counter ranges are fixed before
    // sorting the reference residual for the gap optimum.
    std::map<u64,std::vector<std::size_t>> by_prefix;
    if(coarse_width<=budget) {
        for(const auto& [prefix,span]:coarse)
            by_prefix[prefix].resize(std::size_t(u128(span.high)-span.low+1));
        for(u64 x:residual) {
            const auto prefix=x>>model.grid.shift;
            ++by_prefix.at(prefix)[std::size_t(x-coarse.at(prefix).low)];
        }
    }
    std::sort(residual.begin(),residual.end());
    if(coarse_width<=budget) {
        std::size_t emitted=0;
        for(const auto& [prefix,histogram]:by_prefix) {
            const u64 first=coarse.at(prefix).low;
            for(std::size_t j=0;j<histogram.size();++j)
                for(std::size_t copies=0;copies<histogram[j];++copies) {
                    require(emitted<s && residual[emitted]==first+j,
                            "ordered prefix histogram emit mismatch");
                    ++emitted;
                }
        }
        require(emitted==s,"prefix histogram output length mismatch");
    }
    const auto cuts=two_largest(residual);
    const u128 w1=u128(residual.back())-residual.front()+1;
    for(unsigned k=1;k<=3;++k) {
        const auto segments=partition(residual,cuts,k);
        u128 width=0;
        std::size_t most=0, mass=0;
        for(std::size_t j=0;j<segments.size();++j) {
            const auto& seg=segments[j];
            const u128 w=u128(seg.high)-seg.low+1;
            width+=w;mass+=seg.occurrences;most=std::max(most,seg.occurrences);
            spans<<stage<<','<<bank<<','<<k<<','<<j+1<<','<<seg.low<<','<<seg.high<<','
                 <<decimal(w)<<','<<seg.occurrences<<'\n';
        }
        u128 formula=w1;
        for(unsigned i=0;i+1<k && i<cuts.size();++i) formula-=cuts[i].empty;
        require(width==formula && mass==s, "gap identity or multiplicity failed");
        arrays<<stage<<','<<bank<<','<<n<<','<<decimal(model.cells)<<','<<model.grid.shift<<','<<s
              <<','<<budget<<','<<k<<','<<decimal(width)<<','<<(width<=budget)<<','<<most<<','<<s-most
              <<','<<source_mass[0]<<','<<source_mass[1]<<','<<source_mass[2]<<','<<coarse.size()
              <<','<<decimal(coarse_width)<<','<<(coarse_width<=budget)<<'\n';
    }
}
}
int main(int argc,char** argv) {
    try {
        if(argc!=2) throw std::runtime_error("usage: residual_gaps output_directory");
        const auto where=std::filesystem::path(argv[1]);
        std::filesystem::create_directories(where);
        std::ofstream arrays(where/"arrays.csv"),spans(where/"intervals.csv");
        require(bool(arrays)&&bool(spans),"cannot write output");
        arrays<<"stage,bank,parent_n,parent_cells,parent_grid_shift,residual_n,budget,k,width,fits_budget,largest_segment_occurrences,outside_largest_segment,source_A,source_B,source_C,parent_grid_occupied_bins,parent_grid_sum_hulls,parent_grid_fits\n";
        spans<<"stage,bank,k,interval,low,high,width,occurrences\n";
        for(auto& c:pilot_bench::plan) {
            if(c.kind==pilot_bench::Family::known_million)
                for(unsigned b=0;b<8;++b) diagnostic::inspect(c,b,"known4",arrays,spans);
            if(c.kind==pilot_bench::Family::new_million) {
                for(unsigned b=0;b<8;++b) diagnostic::inspect(c,b,"fresh5",arrays,spans);
                for(unsigned b=32;b<40;++b) diagnostic::inspect(c,b,"fresh6",arrays,spans);
            }
        }
    } catch(const std::exception& e) {std::cerr<<e.what()<<'\n';return 1;}
}
