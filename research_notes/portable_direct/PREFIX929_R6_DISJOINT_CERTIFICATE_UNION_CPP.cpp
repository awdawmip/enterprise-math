// PREFIX-929: independently enumerate disjoint full-row/highband/reversed collision
// certificate domains, then subtract the exact prior B/Z/S and U coverage.
// Compile: g++ -O3 -std=c++17 PREFIX929_R6_DISJOINT_CERTIFICATE_UNION_CPP.cpp -o p929
// Run: ./p929 PREFIX928_R6_SORTED_PAIR_IDS.bin
// The external binary must match SHA256 15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using u64=uint64_t;
constexpr u64 N=1ULL<<32;
constexpr int NQ=131072,Q0=262145;
struct Stats {u64 domain=0,bzscount=0,ucount=0;};
vector<uint8_t> inL(NQ),inT(NQ),inS(NQ);
vector<int> L,T,D,S;
inline int idx(int a){return (a-Q0)/2;}
inline bool bzs(int a,int b){
    const u64 ca=(N+(u64)a-1)/a,cb=(N+(u64)b-1)/b;
    if((u64)b<33*ca||(u64)a<33*cb)return true;
    if(inS[idx(b)])return true;
    return (u64)(a/std::gcd(a,b))*b<N;
}
void add(Stats&s,int a,int b){
    ++s.domain;
    if(bzs(a,b))++s.bzscount;
}
int main(int argc,char**argv){
    if(argc!=2){cerr<<"usage: program PREFIX928_R6_SORTED_PAIR_IDS.bin\n";return 2;}
    for(int b=Q0;b<=524287;b+=2){
        int r=1;bool early=false,late=false;
        for(int d=1;d<=52;++d){
            r=(2LL*r)%b;bool hit=(r==1||r==b-1);
            if(hit&&d<=31)early=true;
            else if(hit)late=true;
        }
        if(early){S.push_back(b);inS[idx(b)]=1;}
        else if(late)D.push_back(b);
    }
    if(S.size()!=24||D.size()!=91)throw runtime_error("D or S count mismatch");
    const vector<int> E{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287};
    L=D;L.insert(L.end(),E.begin(),E.end());sort(L.begin(),L.end());
    L.erase(unique(L.begin(),L.end()),L.end());
    if(L.size()!=104)throw runtime_error("complete-row count mismatch");
    for(int b:L)inL[idx(b)]=1;
    for(int t=0;t<1024;++t){int b=Q0+2*((77081LL*t+12345)%NQ);T.push_back(b);inT[idx(b)]=1;}
    sort(T.begin(),T.end());T.erase(unique(T.begin(),T.end()),T.end());
    if(T.size()!=1024)throw runtime_error("highband seed count mismatch");
    Stats st[4];
    // First the entire second-port rows, then columns with their intersections removed.
    for(int b:L)for(int a=Q0;a<=524287;a+=2)add(st[0],a,b);
    for(int a:L)for(int b=Q0;b<=524287;b+=2)if(!inL[idx(b)])add(st[1],a,b);
    // Highband H and time reverse, excluding already counted complete stripes.
    for(int b:T){
        if(inL[idx(b)])continue;
        for(int a=500001;a<=524287;a+=2)if(!inL[idx(a)])add(st[2],a,b);
    }
    for(int a:T){
        if(inL[idx(a)])continue;
        for(int b=500001;b<=524287;b+=2){
            if(inL[idx(b)])continue;
            if(a>=500001&&inT[idx(b)])continue; // already represented in H
            add(st[3],a,b);
        }
    }
    // Stream the verified, sorted PREFIX928 U IDs once and verify that U excludes BZS.
    ifstream f(argv[1],ios::binary);
    if(!f)throw runtime_error("cannot open PREFIX928 ID binary");
    u64 id=0,prev=0,records=0;
    while(f.read((char*)&id,8)){
        if(records&&id<=prev)throw runtime_error("IDs not strictly increasing");
        prev=id;++records;
        int ai=(int)(id/NQ),bi=(int)(id%NQ);
        if(ai>=NQ)throw runtime_error("out-of-domain ID");
        int a=Q0+2*ai,b=Q0+2*bi;
        if(bzs(a,b))throw runtime_error("U intersects BZS");
        if(inL[bi])++st[0].ucount;
        else if(inL[ai])++st[1].ucount;
        else if(inT[bi]&&a>=500001)++st[2].ucount;
        else if(inT[ai]&&b>=500001)++st[3].ucount;
    }
    if(records!=5295478)throw runtime_error("source U record count mismatch");
    constexpr u64 PREVIOUS=7467804449;
    u64 dom=0,bzsco=0,ucount=0;
    const char* names[]={"complete_second_rows","complete_first_columns_except_overlap","highband_forward_excluding_stripes","highband_reverse_excluding_stripes_and_forward"};
    for(int i=0;i<4;++i){
        auto s=st[i];dom+=s.domain;bzsco+=s.bzscount;ucount+=s.ucount;
        cout<<names[i]<<" domain="<<s.domain<<" BZS="<<s.bzscount<<" U="<<s.ucount<<" increment="<<(s.domain-s.bzscount-s.ucount)<<"\n";
    }
    u64 delta=dom-bzsco-ucount;
    cout<<"D="<<D.size()<<" S="<<S.size()<<" L="<<L.size()<<" T="<<T.size()<<"\n";
    cout<<"total_domain="<<dom<<" BZS="<<bzsco<<" U="<<ucount<<" increment="<<delta<<"\n";
    cout<<"previous_union="<<PREVIOUS<<" new_union="<<PREVIOUS+delta<<" complement="<<(u64)NQ*NQ-PREVIOUS-delta<<"\n";
}
