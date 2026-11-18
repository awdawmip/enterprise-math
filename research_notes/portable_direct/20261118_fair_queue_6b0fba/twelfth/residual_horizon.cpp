// Independent scalar finite-volume stress check. No timing or solver speed claim.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using word = std::uint32_t;
using wide = std::int64_t;

struct State {
    std::vector<word> q, r, next, flux;
    std::vector<wide> cumulative;
    explicit State(const std::vector<word>& init)
        : q(init), r(q.size()), next(q.size()), flux(q.size()), cumulative(q.size()) {}
    void update() {
        for (std::size_t i=0; i<q.size(); ++i) {
            const word low=(q[i]&7u)+r[i];
            flux[i]=(q[i]>>3)+(low>>3);
            r[i]=low&7u;
            cumulative[i]+=flux[i];
        }
        word preceding=flux.back();
        for (std::size_t i=0; i<q.size(); ++i) {
            next[i]=(q[i]-flux[i])+preceding;
            preceding=flux[i];
        }
        q.swap(next);
    }
};

void check(int n,int horizon,bool sharp,int budget) {
    std::vector<word> initial(n);
    for (int i=0;i<n;++i)
        initial[i]=sharp ? (i>=n/4 && i<n/2 ? 131073u : 3u)
                         : static_cast<word>(32768+std::min(i,n-i)*23+((i*17)%13));
    State ref(initial), test(initial);
    int spent=0;
    wide field=0,face=0,region=0,discarded=0,inspected=0;
    for(int t=1;t<=horizon;++t) {
        ref.update();test.update();
        if(spent<budget && t%3!=0) {
            bool changed=false;
            for(int i=0;i<n;++i) {
                ++inspected;
                if((i+t)%3!=0 && test.r[i]>0 && test.r[i]<=static_cast<word>(1+t%7)) {
                    discarded+=test.r[i];test.r[i]=0;changed=true;
                }
            }
            spent+=changed;
        }
        // Every step is still run; inspect the long trajectories at predefined cuts.
        if(t<=10 || t%512==0 || t==horizon) {
            wide low=spent,high=0,mass=0,initial_mass=0,reference_mass=0;
            wide prev=ref.cumulative.back()-test.cumulative.back();
            for(int i=0;i<n;++i) {
                const wide flux=ref.cumulative[i]-test.cumulative[i];
                const wide delta=static_cast<wide>(ref.q[i])-test.q[i];
                if(flux<0 || flux>spent || delta!=prev-flux) std::abort();
                low=std::min(low,flux); high=std::max(high,flux);
                field=std::max(field,static_cast<wide>(std::llabs(delta)));
                prev=flux;mass+=test.q[i];reference_mass+=ref.q[i];initial_mass+=initial[i];
            }
            if(mass!=initial_mass || reference_mass!=mass) std::abort();
            face=std::max(face,high);region=std::max(region,high-low);
        }
    }
    std::cout<<"{\"n\":"<<n<<",\"T\":"<<horizon<<",\"sharp\":"<<(sharp?"true":"false")
             <<",\"budget\":"<<budget<<",\"spent\":"<<spent<<",\"register_units_discarded\":"<<discarded
             <<",\"activation_face_tests\":"<<inspected<<",\"checkpoint_max_field\":"<<field
             <<",\"checkpoint_max_cumulative_face\":"<<face<<",\"checkpoint_max_region\":"<<region<<"}";
}

int main() {
    std::cout<<"[\n";
    bool first=true;
    for(const auto& item:std::array<std::array<int,3>,4>{{
            {512,4096,0},{8192,4096,1},{8192,65536,1},{512,8192,1}}}) {
        for(int budget: {0,1,3}) {
            if(!first)std::cout<<",\n";
            first=false;check(item[0],item[1],item[2]!=0,budget);
        }
    }
    std::cout<<"\n]\n";
}
