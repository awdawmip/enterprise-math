#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <climits>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
using namespace std;
struct P{int a,b; bool operator==(P const&o)const{return a==o.a&&b==o.b;} bool operator<(P const&o)const{return a<o.a||(a==o.a&&b<o.b);} };
static const array<P,6> D={P{1,0},P{0,1},P{-1,1},P{-1,0},P{0,-1},P{1,-1}};
P addp(P x,P y){return {x.a+y.a,x.b+y.b};}
P subp(P x,P y){return {x.a-y.a,x.b-y.b};}
int Q(P p){return p.a*p.a+p.a*p.b+p.b*p.b;}
int L(P p,P q){return 2*p.a*q.a+p.a*q.b+p.b*q.a+2*p.b*q.b;}
P rot(P p){return {-p.b,p.a+p.b};}
P refl(P p){return {p.a+p.b,-p.b};}
P trans(P p,int idx){if(idx>=6)p=refl(p); for(int k=0;k<idx%6;k++)p=rot(p); return p;}
vector<P> decode(const string&s){vector<P> v; v.reserve(s.size()/2); for(size_t i=0;i<s.size();i+=2)v.push_back({(unsigned char)s[i],(unsigned char)s[i+1]}); return v;}
string encode_norm(vector<P> v){int ma=1000,mb=1000; for(auto p:v){ma=min(ma,p.a);mb=min(mb,p.b);} for(auto &p:v){p.a-=ma;p.b-=mb;} sort(v.begin(),v.end()); string s; s.resize(2*v.size()); for(size_t i=0;i<v.size();i++){s[2*i]=(char)v[i].a;s[2*i+1]=(char)v[i].b;} return s;}
string canon(const vector<P>&v){string best; bool first=true; vector<P>w(v.size()); for(int t=0;t<12;t++){for(size_t i=0;i<v.size();i++)w[i]=trans(v[i],t); string s=encode_norm(w); if(first||s<best){best=s;first=false;}} return best;}
uint32_t pack(P p){return (uint32_t)(p.a+64)<<16 | (uint16_t)(p.b+64);}
unordered_set<uint32_t> pointset(const vector<P>&v){unordered_set<uint32_t>s; s.reserve(v.size()*3); for(auto p:v)s.insert(pack(p)); return s;}
bool holefree(const vector<P>&v){auto occ=pointset(v); int amin=99,amax=-99,bmin=99,bmax=-99; for(auto p:v){amin=min(amin,p.a);amax=max(amax,p.a);bmin=min(bmin,p.b);bmax=max(bmax,p.b);} int A0=amin-1,A1=amax+1,B0=bmin-1,B1=bmax+1; unordered_set<uint32_t> ext; queue<P>q; auto seed=[&](P p){auto k=pack(p);if(!occ.count(k)&&ext.insert(k).second)q.push(p);}; for(int a=A0;a<=A1;a++){seed({a,B0});seed({a,B1});}for(int b=B0;b<=B1;b++){seed({A0,b});seed({A1,b});}while(!q.empty()){P p=q.front();q.pop();for(auto d:D){P z=addp(p,d);if(z.a<A0||z.a>A1||z.b<B0||z.b>B1)continue;auto k=pack(z);if(!occ.count(k)&&ext.insert(k).second)q.push(z);}}for(int a=amin;a<=amax;a++)for(int b=bmin;b<=bmax;b++){auto k=pack({a,b});if(!occ.count(k)&&!ext.count(k))return false;}return true;}
vector<P> frontier(const vector<P>&v){auto occ=pointset(v); unordered_set<uint32_t> seen; vector<P>f; for(auto p:v)for(auto d:D){P z=addp(p,d);auto k=pack(z); if(!occ.count(k)&&seen.insert(k).second)f.push_back(z);} return f;}
long long energy(const vector<P>&v){long long sq=0;P S{0,0};for(auto p:v){sq+=Q(p);S.a+=p.a;S.b+=p.b;}return (long long)v.size()*sq-Q(S);}
int pedge(const vector<P>&v){auto occ=pointset(v);int z=0;for(auto p:v)for(auto d:D)if(!occ.count(pack(addp(p,d))))z++;return z;}
string hexkey(const string&s){static const char*h="0123456789abcdef";string o;o.reserve(2*s.size());for(unsigned char c:s){o.push_back(h[c>>4]);o.push_back(h[c&15]);}return o;}
string raw_norm(const vector<P>&v){return encode_norm(v);} // orientation kept, translation removed

struct Succs{int t0=-1,t1=-1,t2=-1;};

bool d2_has_improvement(const vector<P>&v,const unordered_map<string,int>&idx,long long G){
    int n=v.size(); auto occ=pointset(v); P S{0,0}; for(auto p:v){S.a+=p.a;S.b+=p.b;}
    for(int ui=0;ui<n;ui++){
        P u=v[ui]; bool bd=false;for(auto d:D)if(!occ.count(pack(addp(u,d)))){bd=true;break;} if(!bd)continue;
        vector<P> rem;rem.reserve(n-1);for(int j=0;j<n;j++)if(j!=ui)rem.push_back(v[j]);
        auto F=frontier(rem);
        for(auto vv:F){if(vv==u)continue; if(occ.count(pack(vv)))continue; P dd=subp(vv,u); long long delta=(long long)n*(Q(vv)-Q(u))-(L(S,dd)+Q(dd)); if(delta>=0)continue;
            auto cp=rem;cp.push_back(vv); string ck=canon(cp); if(idx.find(ck)!=idx.end()) return true;
        }
    }
    return false;
}

void analyze(int n,const unordered_set<string>&all,ofstream&out){
    auto t0=chrono::steady_clock::now();
    vector<string> valid;valid.reserve(all.size());for(auto const&k:all)if(holefree(decode(k)))valid.push_back(k);sort(valid.begin(),valid.end()); cerr<<" phase filter "<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n"<<flush;
    unordered_map<string,int> idx;idx.reserve(valid.size()*1.3);for(int i=0;i<(int)valid.size();i++)idx.emplace(valid[i],i);
    vector<long long> G(valid.size());vector<int>Pedge(valid.size());long long gmin=LLONG_MAX;int pmin=INT_MAX;
    for(int i=0;i<(int)valid.size();i++){auto v=decode(valid[i]);G[i]=energy(v);Pedge[i]=pedge(v);gmin=min(gmin,G[i]);pmin=min(pmin,Pedge[i]);}
    vector<int> gmins,pmins;for(int i=0;i<(int)valid.size();i++){if(G[i]==gmin)gmins.push_back(i);if(Pedge[i]==pmin)pmins.push_back(i);} cerr<<" phase metrics "<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n"<<flush;
    vector<Succs> succ(valid.size()); vector<int> locals;locals.reserve(1024);
    vector<unsigned char> islocal(valid.size(),0);
    #pragma omp parallel for schedule(dynamic,4096)
    for(int i=0;i<(int)valid.size();i++){
        auto v=decode(valid[i]);auto occ=pointset(v);P S{0,0};for(auto p:v){S.a+=p.a;S.b+=p.b;}
        long long bestDelta=0; bool have=false; string bestMin,bestMax,bestT2; P bestU{999,999},bestV{999,999};
        for(int ui=0;ui<n;ui++){
            P u=v[ui]; bool bd=false;for(auto d:D)if(!occ.count(pack(addp(u,d)))){bd=true;break;} if(!bd)continue;
            for(auto d:D){P vv=addp(u,d);if(occ.count(pack(vv)))continue;
                int touch=0;for(auto d2:D){P q=addp(vv,d2);if(q==u)continue;if(occ.count(pack(q)))touch++;} if(touch==0)continue;
                P dd=subp(vv,u); long long delta=(long long)n*(Q(vv)-Q(u))-(L(S,dd)+Q(dd)); if(delta>=0)continue;
                vector<P> cp=v;cp[ui]=vv;
                string raw=raw_norm(cp); if(raw==valid[i])continue; // pure translation only in current canonical orientation
                string ck=canon(cp);auto it=idx.find(ck);if(it==idx.end())continue;
                if(!have||delta<bestDelta){have=true;bestDelta=delta;bestMin=bestMax=ck;bestU=u;bestV=vv;bestT2=ck;}
                else if(delta==bestDelta){if(ck<bestMin)bestMin=ck;if(ck>bestMax)bestMax=ck;if(make_pair(u,vv)<make_pair(bestU,bestV)){bestU=u;bestV=vv;bestT2=ck;}}
            }
        }
        if(!have)islocal[i]=1;else{succ[i].t0=idx.at(bestMin);succ[i].t1=idx.at(bestMax);succ[i].t2=idx.at(bestT2);}
    }
    for(int i=0;i<(int)valid.size();i++) if(islocal[i]) locals.push_back(i); cerr<<" phase d1 locals="<<locals.size()<<" t="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n"<<flush;
    vector<char>d2min(valid.size(),0);int localNotD2=0;for(int i:locals){bool imp=d2_has_improvement(decode(valid[i]),idx,G[i]);d2min[i]=!imp;if(imp)localNotD2++;}
    cerr<<" phase d2 t="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n"<<flush;
    auto roots=[&](int which){vector<int> memo(valid.size(),-2);for(int i=0;i<(int)valid.size();i++){int cur=i;vector<int>path;while(memo[cur]==-2){path.push_back(cur);int nx=(which==0?succ[cur].t0:which==1?succ[cur].t1:succ[cur].t2);if(nx<0){memo[cur]=cur;break;}cur=nx;}int root=memo[cur];for(auto it=path.rbegin();it!=path.rend();++it){memo[*it]=root;} }return memo;};
    vector<unordered_map<int,long long>> bas(3);for(int w=0;w<3;w++){auto m=roots(w);for(int r:m)bas[w][r]++;}
    cerr<<" phase basins t="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n"<<flush;
    int overlap=0;unordered_set<int>ps(pmins.begin(),pmins.end());for(int x:gmins)if(ps.count(x))overlap++;
    double sec=chrono::duration<double>(chrono::steady_clock::now()-t0).count();
    out<<"SUMMARY\t"<<n<<"\t"<<all.size()<<"\t"<<valid.size()<<"\t"<<gmin<<"\t"<<gmins.size()<<"\t"<<pmin<<"\t"<<pmins.size()<<"\t"<<overlap<<"\t"<<locals.size()<<"\t"<<localNotD2<<"\t"<<fixed<<setprecision(6)<<sec<<"\n";
    for(int i:gmins)out<<"GMIN\t"<<n<<"\t"<<hexkey(valid[i])<<"\n";
    for(int i:pmins)out<<"PMIN\t"<<n<<"\t"<<hexkey(valid[i])<<"\n";
    for(int i:locals)out<<"LOCAL\t"<<n<<"\t"<<hexkey(valid[i])<<"\t"<<(d2min[i]?1:0)<<"\t"<<G[i]<<"\n";
    const char*tn[3]={"T0_CANONICAL_MIN","T1_CANONICAL_MAX","T2_ORIENTATION_MOVE_LEX"};
    for(int w=0;w<3;w++){vector<pair<int,long long>>z(bas[w].begin(),bas[w].end());sort(z.begin(),z.end(),[&](auto x,auto y){return valid[x.first]<valid[y.first];});for(auto [r,c]:z)out<<"BASIN\t"<<n<<"\t"<<tn[w]<<"\t"<<hexkey(valid[r])<<"\t"<<c<<"\n";}
    out.flush(); cerr<<"analyzed n="<<n<<" valid="<<valid.size()<<" local="<<locals.size()<<" sec="<<sec<<"\n"<<flush;
}

int main(int argc,char**argv){int maxn=12;if(argc>1)maxn=stoi(argv[1]);string outpath=argc>2?argv[2]:"r055_exhaustive.tsv";ofstream out(outpath);out<<"# R055 exhaustive exact analysis\n";unordered_set<string>cur,nxt;cur.insert(string("\0\0",2));analyze(1,cur,out);for(int n=2;n<=maxn;n++){auto t=chrono::steady_clock::now();nxt.clear();nxt.reserve(cur.size()*5);for(auto const&key:cur){auto v=decode(key);auto f=frontier(v);for(auto z:f){auto w=v;w.push_back(z);nxt.insert(canon(w));}}cerr<<"generated n="<<n<<" total="<<nxt.size()<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n"<<flush;analyze(n,nxt,out);cur.swap(nxt);} }
