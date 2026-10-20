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

bool connectedv(const vector<P>&v){
    if(v.empty()) return false; auto occ=pointset(v); unordered_set<uint32_t> seen; vector<P> st; st.push_back(v[0]); seen.insert(pack(v[0]));
    while(!st.empty()){P p=st.back();st.pop_back();for(auto d:D){P q=addp(p,d);auto k=pack(q);if(occ.count(k)&&seen.insert(k).second)st.push_back(q);}}
    return seen.size()==v.size();
}
vector<P> frontier(const vector<P>&v){auto occ=pointset(v); unordered_set<uint32_t> seen; vector<P>f; for(auto p:v)for(auto d:D){P z=addp(p,d);auto k=pack(z); if(!occ.count(k)&&seen.insert(k).second)f.push_back(z);} return f;}
long long energy(const vector<P>&v){long long sq=0;P S{0,0};for(auto p:v){sq+=Q(p);S.a+=p.a;S.b+=p.b;}return (long long)v.size()*sq-Q(S);}
int pedge(const vector<P>&v){auto occ=pointset(v);int z=0;for(auto p:v)for(auto d:D)if(!occ.count(pack(addp(p,d))))z++;return z;}
string hexkey(const string&s){static const char*h="0123456789abcdef";string o;o.reserve(2*s.size());for(unsigned char c:s){o.push_back(h[c>>4]);o.push_back(h[c&15]);}return o;}
string raw_norm(const vector<P>&v){return encode_norm(v);} // orientation kept, translation removed

struct Succs{int t0=-1,t1=-1,t2=-1;};

bool d2_has_improvement(const vector<P>&v,const vector<string>&valid,long long G){
    int n=v.size(); auto occ=pointset(v); P S{0,0}; for(auto p:v){S.a+=p.a;S.b+=p.b;}
    for(int ui=0;ui<n;ui++){
        P u=v[ui]; bool bd=false;for(auto d:D)if(!occ.count(pack(addp(u,d)))){bd=true;break;} if(!bd)continue;
        vector<P> rem;rem.reserve(n-1);for(int j=0;j<n;j++)if(j!=ui)rem.push_back(v[j]);
        auto F=frontier(rem);
        for(auto vv:F){if(vv==u)continue; if(occ.count(pack(vv)))continue; P dd=subp(vv,u); long long delta=(long long)n*(Q(vv)-Q(u))-(L(S,dd)+Q(dd)); if(delta>=0)continue;
            auto cp=rem;cp.push_back(vv); string ck=canon(cp); if(binary_search(valid.begin(),valid.end(),ck)) return true;
        }
    }
    return false;
}

string t2_terminal_raw(string rawkey){
    for(int steps=0;steps<10000;steps++){
        auto v=decode(rawkey);int n=v.size();auto occ=pointset(v);P S{0,0};for(auto p:v){S.a+=p.a;S.b+=p.b;}
        struct RM{long long delta;int ui;P u,vv;};vector<RM>rms;rms.reserve(n*4);
        for(int ui=0;ui<n;ui++){P u=v[ui];bool bd=false;for(auto d:D)if(!occ.count(pack(addp(u,d)))){bd=true;break;}if(!bd)continue;for(auto d:D){P vv=addp(u,d);if(occ.count(pack(vv)))continue;int touch=0;for(auto d2:D){P q=addp(vv,d2);if(q==u)continue;if(occ.count(pack(q)))touch++;}if(touch==0)continue;P dd=subp(vv,u);long long delta=(long long)n*(Q(vv)-Q(u))-(L(S,dd)+Q(dd));if(delta<0)rms.push_back({delta,ui,u,vv});}}
        sort(rms.begin(),rms.end(),[](const RM&x,const RM&y){if(x.delta!=y.delta)return x.delta<y.delta;if(x.u<y.u)return true;if(y.u<x.u)return false;return x.vv<y.vv;});
        bool found=false;vector<P>chosen;size_t pos=0;
        while(pos<rms.size()&&!found){size_t end=pos+1;while(end<rms.size()&&rms[end].delta==rms[pos].delta)end++;for(size_t j=pos;j<end;j++){auto&m=rms[j];vector<P>cp=v;cp[m.ui]=m.vv;string nr=raw_norm(cp);if(nr==rawkey)continue;if(!connectedv(cp)||!holefree(cp))continue;chosen=std::move(cp);found=true;break;}if(!found)pos=end;}
        if(!found)return canon(v);
        rawkey=raw_norm(chosen);
    }
    throw runtime_error("t2 max steps");
}

void analyze(int n,unordered_set<string>&all,ofstream&out,bool release_all=false){
    auto t0=chrono::steady_clock::now();vector<string>valid;valid.reserve(all.size());for(auto const&k:all)if(holefree(decode(k)))valid.push_back(k);sort(valid.begin(),valid.end());if(release_all){all.clear();all.rehash(0);}vector<string>terms(valid.size());
    #pragma omp parallel for schedule(dynamic,512)
    for(int i=0;i<(int)valid.size();i++)terms[i]=t2_terminal_raw(valid[i]);
    unordered_map<string,long long>bas;for(auto &k:terms)bas[k]++;vector<pair<string,long long>>z(bas.begin(),bas.end());sort(z.begin(),z.end());
    double sec=chrono::duration<double>(chrono::steady_clock::now()-t0).count();out<<"SUMMARY\t"<<n<<"\t"<<valid.size()<<"\t"<<z.size()<<"\t"<<sec<<"\n";for(auto &[k,c]:z)out<<"BASIN\t"<<n<<"\tT2_ORIENTATION_MOVE_LEX\t"<<hexkey(k)<<"\t"<<c<<"\n";out.flush();cerr<<"T2 n="<<n<<" valid="<<valid.size()<<" basins="<<z.size()<<" sec="<<sec<<"\n"<<flush;
}

int main(int argc,char**argv){int maxn=12;if(argc>1)maxn=stoi(argv[1]);string outpath=argc>2?argv[2]:"r055_exhaustive.tsv";ofstream out(outpath);out<<"# R055 exhaustive exact analysis\n";unordered_set<string>cur,nxt;cur.insert(string("\0\0",2));analyze(1,cur,out,maxn==1);if(maxn==1)return 0;for(int n=2;n<=maxn;n++){auto t=chrono::steady_clock::now();nxt.clear();nxt.reserve(cur.size()*5);for(auto const&key:cur){auto v=decode(key);auto f=frontier(v);for(auto z:f){auto w=v;w.push_back(z);nxt.insert(canon(w));}}cerr<<"generated n="<<n<<" total="<<nxt.size()<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n"<<flush;analyze(n,nxt,out,n==maxn);if(n==maxn)break;cur.swap(nxt);} }
