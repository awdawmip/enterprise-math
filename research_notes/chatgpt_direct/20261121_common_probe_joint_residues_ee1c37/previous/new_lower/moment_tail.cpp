// Compare one exact residual-cover problem with and without the joint moment.
#define main complete_profile_main
#include "front_moments.cpp"
#undef main
int main(int argc, char** argv) {
    if (argc != 3) return 2;
    ifstream db(argv[1], ios::binary);
    struct Row { uint64_t lo,hi; unsigned cost,size; } row;
    Type t; t.sz=10; t.price=744;
    while (db.read(reinterpret_cast<char*>(&row), sizeof(row))) {
        if ((row.size&255)!=10 || row.cost!=744) continue;
        M m=M(row.lo)|(M(row.hi)<<64);
        t.all.push_back(m);
        if (row.size>=256) t.reps.push_back(m);
    }
    types.push_back(std::move(t));
    for (int i=0; i<125; ++i) {
        M bit=M(1)<<i; slices[i/25]|=bit; slices[5+i/5%5]|=bit; slices[10+i%5]|=bit;
    }
    init_mixed_moments(); prepare_bounds(); init_shapes();
    multi_id[{}]=0; multis.push_back({}); reachable.push_back({0});
    actual_ids={0}; abs_lo.resize(1); abs_hi.resize(1);
    abs_lo[0].fill(2); abs_hi[0].fill(2);
    level_bound[0]={shape_max[0]};
    mixed_enabled=stoi(argv[2]);
    uint64_t lo,hi; int count;
    while (cin>>lo>>hi>>count) {
        const M free=M(lo)|(M(hi)<<64);
        vector<int> counts={count}; Pools pool(1);
        for (M m:types[0].all) if ((m&free)==m) pool[0].push_back(m);
        for (int i=0;i<125;++i) bound_at[count][i]=count*shape_max[0][i];
        nodes=0; mixed_tested=0; mixed_rejected=0;
        bool marginal_pass=exact_margins(free,counts);
        bool answer=solve(free,count,counts,pool);
        cout<<count<<' '<<pool[0].size()<<' '<<marginal_pass<<' '<<nodes<<' '
            <<answer<<' '<<mixed_tested<<' '<<mixed_rejected<<'\n';
    }
}
