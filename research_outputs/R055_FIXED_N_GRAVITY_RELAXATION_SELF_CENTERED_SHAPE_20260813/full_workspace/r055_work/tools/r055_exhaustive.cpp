#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
using namespace std;
struct P{int a,b; bool operator==(P const&o)const{return a==o.a&&b==o.b;} bool operator<(P const&o)const{return a<o.a||(a==o.a&&b<o.b);} };
static const array<P,6> D={P{1,0},P{0,1},P{-1,1},P{-1,0},P{0,-1},P{1,-1}};
P addp(P x,P y){return {x.a+y.a,x.b+y.b};}
P rot(P p){return {-p.b,p.a+p.b};}
P refl(P p){return {p.a+p.b,-p.b};}
P trans(P p,int idx){if(idx>=6)p=refl(p); for(int k=0;k<idx%6;k++)p=rot(p); return p;}
vector<P> decode(const string&s){vector<P> v; v.reserve(s.size()/2); for(size_t i=0;i<s.size();i+=2)v.push_back({(unsigned char)s[i],(unsigned char)s[i+1]}); return v;}
string encode_norm(vector<P> v){int ma=1000,mb=1000; for(auto p:v){ma=min(ma,p.a);mb=min(mb,p.b);} for(auto &p:v){p.a-=ma;p.b-=mb;} sort(v.begin(),v.end()); string s; s.resize(2*v.size()); for(size_t i=0;i<v.size();i++){if(v[i].a<0||v[i].a>250||v[i].b<0||v[i].b>250) abort(); s[2*i]=(char)v[i].a;s[2*i+1]=(char)v[i].b;} return s;}
string canon(const vector<P>&v){string best; bool first=true; vector<P>w; w.resize(v.size()); for(int t=0;t<12;t++){for(size_t i=0;i<v.size();i++)w[i]=trans(v[i],t); string s=encode_norm(w); if(first||s<best){best=s;first=false;}} return best;}
uint32_t pack(P p){return (uint32_t)(p.a+64)<<16 | (uint16_t)(p.b+64);}
unordered_set<uint32_t> pointset(const vector<P>&v){unordered_set<uint32_t>s; s.reserve(v.size()*2); for(auto p:v)s.insert(pack(p)); return s;}
bool holefree(const vector<P>&v){auto occ=pointset(v); int amin=99,amax=-99,bmin=99,bmax=-99; for(auto p:v){amin=min(amin,p.a);amax=max(amax,p.a);bmin=min(bmin,p.b);bmax=max(bmax,p.b);} int A0=amin-1,A1=amax+1,B0=bmin-1,B1=bmax+1; unordered_set<uint32_t> ext; queue<P>q; auto seed=[&](P p){auto k=pack(p);if(!occ.count(k)&&ext.insert(k).second)q.push(p);}; for(int a=A0;a<=A1;a++){seed({a,B0});seed({a,B1});}for(int b=B0;b<=B1;b++){seed({A0,b});seed({A1,b});}while(!q.empty()){P p=q.front();q.pop();for(auto d:D){P z=addp(p,d);if(z.a<A0||z.a>A1||z.b<B0||z.b>B1)continue;auto k=pack(z);if(!occ.count(k)&&ext.insert(k).second)q.push(z);}}for(int a=amin;a<=amax;a++)for(int b=bmin;b<=bmax;b++){auto k=pack({a,b});if(!occ.count(k)&&!ext.count(k))return false;}return true;}
vector<P> frontier(const vector<P>&v){auto occ=pointset(v); unordered_set<uint32_t> seen; vector<P>f; for(auto p:v)for(auto d:D){P z=addp(p,d);auto k=pack(z); if(!occ.count(k)&&seen.insert(k).second)f.push_back(z);} return f;}
int main(int argc,char**argv){int maxn=12;if(argc>1)maxn=stoi(argv[1]);unordered_set<string> cur,nxt;cur.insert(string("\0\0",2));cout<<1<<" "<<cur.size()<<" 1\n"<<flush;for(int n=2;n<=maxn;n++){auto t=chrono::steady_clock::now();nxt.clear();nxt.reserve(cur.size()*5);for(auto const&key:cur){auto v=decode(key);auto f=frontier(v);for(auto z:f){auto w=v;w.push_back(z);nxt.insert(canon(w));}}size_t hf=0;for(auto const&key:nxt)if(holefree(decode(key)))hf++;double sec=chrono::duration<double>(chrono::steady_clock::now()-t).count();cout<<n<<" "<<nxt.size()<<" "<<hf<<" "<<sec<<"\n"<<flush;cur.swap(nxt);} }
