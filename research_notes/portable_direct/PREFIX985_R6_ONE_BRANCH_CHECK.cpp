// PREFIX-985: exact four-phase signed-source observer census, <=1 branching phase.
// Original source equation; all odd start states; all 0/1-double-port words.
#include <bits/stdc++.h>
using namespace std;
struct Port {int j,mask;};
struct R {int c; vector<Port> ports;};
vector<R> dictionary(int p) {
    map<int,map<int,int>> raw;
    for(int i=0;i<p;i++) for(int j=1;j<p;j++) for(int s:{-1,1}) {
        int c=(1<<i)-s*(1<<j);
        if(c) raw[c][j] |= (s<0?2:1);
    }
    vector<R> v;
    for(auto &[c,ports]:raw){ R r{c,{}}; for(auto &[j,m]:ports)r.ports.push_back({j,m}); v.push_back(r);}
    return v;
}
int path_len(const array<const R*,4>& w, int phase, int x, int steps) {
    if(steps==8)return 8;
    int best=steps;
    for(auto [j,mask]:w[phase]->ports) if(mask & (1<<((x>>j)&1)))
        best=max(best,path_len(w,(phase+1)&3,x^(1<<j),steps+1));
    return best;
}
int main(int argc,char**argv){
    int p=stoi(argv[1]);
    auto all=dictionary(p);
    vector<const R*> single,branch;
    for(auto &r:all)(r.ports.size()==1?single:branch).push_back(&r);
    uint64_t count=0, cyclic=0, finite=0, no4=0;
    int maxfinite=0;array<int,4> wit{};int witx=0;
    array<const R*,4> w;
    auto process=[&](){
        count++;
        bool reaches8=false, has4=false;int localmax=0,localx=0;
        for(int x=1;x<(1<<p);x+=2){
            function<void(int,int)> loop4=[&](int step,int z){
                if(step==4){if(z==x)has4=true;return;}
                for(auto [j,m]:w[step]->ports) if(m & (1<<((z>>j)&1)))loop4(step+1,z^(1<<j));
            };
            loop4(0,x);
            int len=path_len(w,0,x,0);
            if(len>localmax){localmax=len;localx=x;}
            if(len==8)reaches8=true;
        }
        if(reaches8){cyclic++;if(!has4)no4++;}
        else {finite++;if(localmax>maxfinite){maxfinite=localmax;witx=localx;for(int k=0;k<4;k++)wit[k]=w[k]->c;}}
    };
    for(auto *a:single)for(auto *b:single)for(auto *c:single)for(auto *d:single){w={a,b,c,d};process();}
    for(int j=0;j<4;j++){
        for(auto *z:branch)for(auto *a:single)for(auto *b:single)for(auto *c:single){
            int h=0;for(int k=0;k<4;k++)w[k]=(k==j?z:(h==0?a:h==1?b:c)),h+=(k!=j);
            process();
        }
    }
    cout<<"{\"p\":"<<p<<",\"residuals\":"<<all.size()<<",\"single\":"<<single.size()
        <<",\"double\":"<<branch.size()<<",\"words\":"<<count<<",\"cycle_witnesses\":"
        <<cyclic<<",\"finite\":"<<finite<<",\"8_without_4\":"<<no4
        <<",\"max_finite\":"<<maxfinite<<",\"max_word\":["
        <<wit[0]<<","<<wit[1]<<","<<wit[2]<<","<<wit[3]<<"],\"start\":"<<witx<<"}\n";
}
