#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
struct Term {int32_t v; int8_t i,j,s;};
struct Hit {uint64_t id; uint8_t m; int16_t t; uint8_t i,j,I,J;};
int main() {
    const int L=262145, U=524287, M=131072;
    vector<Term> terms;terms.reserve(722);
    for(int i=0;i<19;i++)for(int j=0;j<19;j++)for(int s: {-1,1})
        terms.push_back({(1<<i)-s*(1<<j),(int8_t)i,(int8_t)j,(int8_t)s});
    array<uint64_t,7> raw{}, offraw{};
    vector<Hit> hits; hits.reserve(12000);
    for(int m=0;m<=6;m++)for(int t=1;t<=42;t++) {
        int T=t+m;if(T>46)continue;
        int d=2*t-21*m;if(!d)continue;
        for(const Term &x:terms)for(const Term &y:terms) {
            int64_t na=int64_t(t)*y.v-int64_t(T)*x.v;
            int64_t nb=21LL*y.v-23LL*x.v;
            if(na%d || nb%d)continue;
            int64_t a=na/d,b=nb/d;
            if(a<L || a>U || b<L || b>U || !(a&1) || !(b&1))continue;
            int64_t ka=21*a,la=23*a;
            if((1-2*((ka>>x.j)&1))!=x.s || (1-2*((la>>y.j)&1))!=y.s)continue;
            int64_t left1=(ka^(1LL<<x.j))-(1LL<<x.i);
            int64_t left2=(la^(1LL<<y.j))-(1LL<<y.i);
            if(left1!=t*b || left2!=T*b || left1<=0 || left2<=0 || left1>= (1LL<<32) || left2>= (1LL<<32))continue;
            raw[m]++;if(a!=b)offraw[m]++;
            uint64_t id=(uint64_t((a-L)/2)*M+(b-L)/2);
            hits.push_back({id,(uint8_t)m,(int16_t)t,(uint8_t)x.i,(uint8_t)x.j,(uint8_t)y.i,(uint8_t)y.j});
        }
    }
    sort(hits.begin(),hits.end(),[](const Hit&a,const Hit&b){return a.id<b.id || (a.id==b.id && a.m<b.m);});
    array<uint64_t,7> distinct_by_m{}, unique_to_m{}, overlap_m{};
    array<uint64_t,128> m_mask_hist{};
    uint64_t distinct=0,offdistinct=0,diag=0,lt=0,gt=0, multi=0;
    uint64_t firstnon=0;uint64_t lastnon=0;
    ofstream offout("PREFIX955_NONDIAGONAL_IDS.bin",ios::binary);
    ofstream jointout("PREFIX955_W21_W23_INTERSECTION_IDS.bin",ios::binary);
    for(size_t i=0;i<hits.size();) {
        size_t j=i;uint64_t id=hits[i].id;unsigned mask=0;
        while(j<hits.size()&&hits[j].id==id){mask|=1u<<hits[j].m;j++;}
        m_mask_hist[mask]++;distinct++;if(mask&(mask-1)){ multi++;cout<<"MULTI_M a,b="<<(L+2*(id/M))<<","<<(L+2*(id%M))<<" mask="<<mask<<"\n";}
        int a=int(id/M)*2+L,b=int(id%M)*2+L;
        if(a!=b){offout.write(reinterpret_cast<const char*>(&id),8); offdistinct++;if(a<b)lt++;else gt++;if(!firstnon)firstnon=id;lastnon=id;}
        else diag++;
        for(int m=0;m<7;m++)if(mask&(1u<<m)){distinct_by_m[m]++;if(!(mask&(mask-1)))unique_to_m[m]++;else overlap_m[m]++;}
        i=j;
    }
    vector<uint64_t> full;full.reserve(137274);
    for(int a=L;a<=U;a+=2){if(a==274627)continue;uint64_t id=uint64_t((a-L)/2)*M+(a-L)/2;full.push_back(id);}
    for(size_t i=0;i<hits.size();){auto id=hits[i].id;if((id/M)!=(id%M))full.push_back(id);while(i<hits.size() && hits[i].id==id)i++;}
    sort(full.begin(),full.end());for(auto id:full)jointout.write(reinterpret_cast<const char*>(&id),8);
    offout.close();jointout.close();
    cout<<"RAW ";for(auto v:raw)cout<<v<<" ";cout<<"\nOFFRAW ";for(auto v:offraw)cout<<v<<" ";
    cout<<"\nDISTINCT_BY_M ";for(auto v:distinct_by_m)cout<<v<<" ";
    cout<<"\nUNIQUE_TO_M ";for(auto v:unique_to_m)cout<<v<<" ";
    cout<<"\nOVERLAP_M ";for(auto v:overlap_m)cout<<v<<" ";
    cout<<"\nTOTAL raw="<<hits.size()<<" distinct="<<distinct<<" off="<<offdistinct<<" diag="<<diag<<" a_lt_b="<<lt<<" a_gt_b="<<gt<<" multiple_m="<<multi<<"\n";
    cout<<"MASK_HIST ";for(size_t mask=1;mask<m_mask_hist.size();mask++)if(m_mask_hist[mask])cout<<mask<<":"<<m_mask_hist[mask]<<" ";cout<<"\n";
    auto print_id=[&](uint64_t id){cout<<"("<<L+2*(id/M)<<","<<L+2*(id%M)<<")";};
    cout<<"first_offdiag=";print_id(firstnon);cout<<" last_offdiag=";print_id(lastnon);cout<<"\n";
    cout<<"EXAMPLES\n";size_t cnt=0;for(const auto&h:hits){auto a=L+2*(h.id/M),b=L+2*(h.id%M);if(a==b)continue;cout<<a<<" "<<b<<" m="<<int(h.m)<<" t="<<h.t<<" i,j,I,J="<<int(h.i)<<","<<int(h.j)<<","<<int(h.I)<<","<<int(h.J)<<"\n";if(++cnt>=8)break;}
}
