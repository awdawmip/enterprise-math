#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using U64 = std::uint64_t;
using U128 = __uint128_t;
constexpr U64 prime = (U64(1) << 61) - 1;

U64 add(U64 x, U64 y) {
    U64 s = x + y;
    return s < prime ? s : s - prime;
}
U64 mul(U64 x, U64 y) {
    U128 w = U128(x) * y;
    return add(U64(w) & prime, U64(w >> 61));
}
U64 inv(U64 x) {
    assert(x);
    U64 value = 1;
    for (U64 e = prime - 2; e; e >>= 1) {
        if (e & 1) value = mul(value, x);
        x = mul(x, x);
    }
    return value;
}

struct Edge {
    U64 b, c, d; // (0,b;c,d)
    bool decreasing;
};
struct Point { U64 x, y; };
struct Terminal {
    U64 a,b,c,d; // odds (a u+b)/(c u+d), increasing in the terminal input
};
using Layer = std::vector<std::vector<Edge>>;

class Census {
    const std::vector<Layer>& layers;
    const std::vector<Terminal>& tails;
    std::vector<U64> keys;
    static constexpr int batch_size = 1024;
    std::array<U64,batch_size> numerators, denominators, products;
    int pending=0;
    bool collect=false;
    U64 target=0;
    std::vector<int> path;
    std::vector<std::vector<int>> pending_paths;
    U64 enumeration_sum=0;
    std::vector<std::pair<U64,U64>> known;
    std::size_t tested=0;

    void flush() {
        if (!pending) return;
        U64 product=1;
        for (int i=0;i<pending;++i) {
            products[i]=product;
            product=mul(product,denominators[i]);
        }
        U64 inverse=inv(product);
        for (int i=pending-1;i>=0;--i) {
            U64 v=mul(numerators[i],mul(inverse,products[i]));
            inverse=mul(inverse,denominators[i]);
            if (collect) {
                if (v==target) {
                    std::cout << "collision_path";
                    for (int m:pending_paths[i]) std::cout << " " << m;
                    std::cout << "\n";
                }
            } else numerators[i]=v;
        }
        if (!collect) {
            for (int i=0;i<pending;++i) {
                if(tested<known.size() && keys.size()==known[tested].first) {
                    assert(numerators[i]==known[tested].second);
                    ++tested;
                }
                enumeration_sum=add(enumeration_sum,mul(keys.size()+1,numerators[i]));
                keys.push_back(numerators[i]);
            }
        }
        pending_paths.clear();
        pending=0;
    }

    void enumerate(int r,int c,Point u,Point v,bool flipped) {
        if (r==0) {
            const Terminal& t=tails[c];
            auto evaluate = [&](U64 a,U64 b,Point p) {return add(mul(a,p.x),mul(b,p.y));};
            U64 n=mul(evaluate(t.a,t.b,v),evaluate(t.c,t.d,u));
            U64 d=mul(evaluate(t.c,t.d,v),evaluate(t.a,t.b,u));
            if(flipped) std::swap(n,d);
            assert(n && d); // all reported fibers have a well-defined finite reduction
            numerators[pending]=n;
            denominators[pending]=d;
            if(collect) {
                pending_paths.push_back(path);
                pending_paths.back().push_back(c-2);
            }
            if(++pending==batch_size) flush();
            return;
        }
        for(int m=0;m<=c-2;++m) {
            const auto& edge=layers[r][c][m];
            auto advance=[&](Point p)->Point {
                return {mul(edge.b,p.y),add(mul(edge.c,p.x),mul(edge.d,p.y))};
            };
            if(collect) path.push_back(m);
            enumerate(r-1,c-m,advance(u),advance(v),flipped!=edge.decreasing);
            if(collect) path.pop_back();
        }
    }

    void run_family(int n,bool cut) {
        if(cut) enumerate(n,n+1,{0,1},{1,1},false);
        else for(int b0=0;b0<n;++b0) {
            if(collect) path.push_back(b0);
            enumerate(n-1,n+1-b0,{0,1},{1,1},false);
            if(collect) path.pop_back();
        }
        flush();
    }
public:
    Census(const std::vector<Layer>& edge_data,const std::vector<Terminal>& terminal_data):
        layers(edge_data),tails(terminal_data) {}
    std::vector<U64> run(int n,bool cut) {
        U64 count=1;
        for(int i=1;i<=n-1;++i) count=count*(n+i)/i;
        int reference_count;
        std::cin>>reference_count;
        for(int i=0;i<reference_count;++i) {
            U64 index,residue;
            std::cin>>index>>residue;
            known.emplace_back(index,residue);
        }
        keys.reserve(count);
        run_family(n,cut);
        assert(keys.size()==count && tested==known.size());
        std::sort(keys.begin(),keys.end());
        U64 repeated=0,first=0;
        for(size_t i=1;i<keys.size();++i) if(keys[i]==keys[i-1]) {
            if(!repeated) first=keys[i];
            ++repeated;
        }
        std::cout << (cut?"cut":"full") << " " << n << " " << count << " " << repeated
                  << " " << enumeration_sum << " " << keys.front() << " " << keys.back() << "\n" << std::flush;
        if(repeated) {
            target=first;
            collect=true;
            std::vector<U64>().swap(keys);
            run_family(n,cut);
        }
        return std::move(keys);
    }
};

int main() {
    int nmax;
    std::cin >> nmax;
    std::vector<Layer> layers(nmax+1,Layer(nmax+2));
    std::vector<Terminal> tails(nmax+2);
    for(int c=2;c<=nmax+1;++c) {
        auto& t=tails[c];
        std::cin>>t.a>>t.b>>t.c>>t.d;
    }
    for(int r=1;r<=nmax;++r) for(int c=2;c<=nmax+1;++c) {
        for(int m=0;m<=c-2;++m) {
            Edge e{};
            std::cin>>e.b>>e.c>>e.d>>e.decreasing;
            layers[r][c].push_back(e);
        }
    }
    // Each family is already sorted, so uniqueness across target scales only
    // needs a k-way merge, with one next element per scale in the heap.
    std::vector<std::vector<U64>> complete;
    auto check_joint = [&]() {
        if(complete.empty()) return;
        struct Cursor { U64 value; std::size_t row,col; };
        auto later=[](const Cursor& a,const Cursor& b) {return a.value>b.value;};
        std::priority_queue<Cursor,std::vector<Cursor>,decltype(later)> heap(later);
        for (std::size_t i=0;i<complete.size();++i) if(!complete[i].empty()) heap.push({complete[i][0],i,0});
        U64 total=0,previous=0,repeated=0;
        while(!heap.empty()) {
            auto item=heap.top();heap.pop();
            repeated+= (total && item.value==previous);
            previous=item.value;
            ++total;
            if(++item.col<complete[item.row].size()) {
                item.value=complete[item.row][item.col];
                heap.push(item);
            }
        }
        std::cout<<"joint "<<total<<" "<<repeated<<"\n"<<std::flush;
        complete.clear();
    };
    int n; std::string family;
    while(std::cin>>family>>n) {
        assert(n>=2 && n<=nmax);
        bool cut=family=="cut";
        if(cut) check_joint();
        auto sorted=Census(layers,tails).run(n,cut);
        if(!cut) complete.push_back(std::move(sorted));
  }
    check_joint();
}
