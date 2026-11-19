// Exact independent full-row a-enumeration for i=0 mixed named XOR witnesses.
// Emits sorted uint64 little-endian pair IDs; C++17, exact arithmetic only.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;
static constexpr uint64_t N=1ULL<<32;
static constexpr int LO=262145,HI=524287,M=131072;
long long egcd(long long a,long long b,long long &x,long long &y){
    if(!b){x=1;y=0;return a;}
    long long u,v,g=egcd(b,a%b,u,v);x=v;y=u-(a/b)*v;return g;
}
int inverse_mod(int a,int b){
    long long x,y,g=egcd(a,b,x,y);
    if(g!=1)return -1;
    x%=b;if(x<0)x+=b;return (int)x;
}
uint64_t idx(int a,int b){return uint64_t((a-LO)/2)*M+(b-LO)/2;}
int main(int argc,char**argv){
    if(argc!=2){cerr<<"usage: program sorted-pair-ids.bin\n";return 2;}
    vector<uint8_t> special(M,0);
    for(int b=LO;b<=HI;b+=2){
        int r=2%b;
        for(int d=1;d<32;d++){
            if(r==1||r==b-1){special[(b-LO)/2]=1;break;}
            r=int((2LL*r)%b);
        }
    }
    auto outside=[&](int a,int b)->bool{
        if(uint64_t(b)<33*((N+a-1)/a)||uint64_t(a)<33*((N+b-1)/b))return false;
        if((uint64_t(a)/gcd(a,b))*b<N)return false;
        return !special[(b-LO)/2];
    };
    unordered_set<uint64_t> cert,edge;
    uint64_t parameter=0;
    for(int b=400001;b<=400127;b+=2){
        for(int a=LO;a<=HI;a+=2){
            int inv=inverse_mod(a,b);
            if(inv<0)continue;
            uint64_t km=inv,kp=b-inv;
            bool minus=km*a<N && ((km*a-1)%b==0);
            bool plus=kp*a+1<N && ((kp*a+1)%b==0);
            if(!minus&&!plus)continue;
            parameter+=minus+plus;
            edge.insert(idx(a,b));edge.insert(idx(b,a));
            if(outside(a,b))cert.insert(idx(a,b));
            if(outside(b,a))cert.insert(idx(b,a));
        }
    }
    vector<uint64_t> sorted(cert.begin(),cert.end());
    sort(sorted.begin(),sorted.end());
    ofstream f(argv[1],ios::binary);
    for(auto z:sorted){for(int j=0;j<8;j++){char c=char((z>>(8*j))&255);f.write(&c,1);}}
    cerr<<"parameter="<<parameter<<" edge="<<edge.size()<<" cert="<<sorted.size()<<"\n";
    if(parameter!=386923 || edge.size()!=773724 || sorted.size()!=437560)return 3;
    if(!f)return 4;
}
