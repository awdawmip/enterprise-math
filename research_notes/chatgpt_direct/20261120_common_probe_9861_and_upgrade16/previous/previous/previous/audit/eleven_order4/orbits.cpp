#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using Mask=__uint128_t;using U=uint64_t;
struct Hash{size_t operator()(Mask m)const{return U(m)^((U(m>>64)+0x9e3779b97f4a7c15ULL)*0xbf58476d1ce4e5b9ULL);}};
int pc(Mask m){return __builtin_popcountll(U(m))+__builtin_popcountll(U(m>>64));}
int bit(Mask m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
struct Map{std::array<int,125> p;std::array<std::array<Mask,256>,16> tab{};void make(){for(int j=0;j<16;j++)for(int b=1;b<256;b++){int pos=8*j+__builtin_ctz(b);tab[j][b]=tab[j][b&(b-1)]|(pos<125?Mask(1)<<p[pos]:0);}}Mask apply(Mask m)const{Mask r=0;for(int j=0;m;j++,m>>=8)r|=tab[j][(unsigned char)m];return r;}};
int plus(int x,int t){return 25*((x/25+t/25)%5)+5*((x/5%5+t/5%5)%5)+(x%5+t%5)%5;}
int neg(int i){return 25*((5-i/25)%5)+5*((5-i/5%5)%5)+(5-i%5)%5;}
struct Row{int c;Mask m;};
int main(int argc,char**argv){
 if(argc<6)return 2;int id=atoi(argv[4]);std::ifstream lm(argv[1]),rm(argv[2]),sf(argv[3]);std::vector<Map> linear(96),tr(125);for(auto &g:linear){for(auto &v:g.p)lm>>v;g.make();}for(int d=0;d<125;d++){for(int x=0;x<125;x++)tr[d].p[x]=plus(x,d);tr[d].make();}
 Map g;for(int j=0;j<=id;j++)for(auto &v:g.p)rm>>v;g.make();int index[125];std::fill(index,index+125,-1);int n=0;for(int x=0;x<125;x++)if(index[x]<0){int t=x;do{index[t]=n;t=g.p[t];}while(t!=x);++n;}assert(n==32);
 int caps[14]={0,0,0,0,0,0,0,0,0,0,8000,8000,8000,8000};std::unordered_set<Mask,Hash> seen;std::unordered_map<uint32_t,Row> best;
 int se=0,sh=0;std::string line;while(std::getline(sf,line)){std::istringstream st(line);int s,c;st>>s>>c;if(c>caps[s])continue;Mask m=0;for(int i=0,x;i<s;i++){st>>x;m|=Mask(1)<<x;}++se;if(seen.count(m))continue;std::unordered_set<Mask,Hash> rooted;
 for(auto&l:linear){auto r=l.apply(m);for(Mask t=r;t;t&=t-1)seen.insert(tr[neg(bit(t))].apply(r));rooted.insert(r);}++sh;
 for(Mask r:rooted)for(auto&t:tr){Mask v=t.apply(r),v1=g.apply(v);if(v&v1)continue;Mask v2=g.apply(v1);if(v&v2)continue;uint32_t q=0;for(Mask u=v;u;u&=u-1)q|=uint32_t(1)<<index[bit(u)];assert(__builtin_popcount(q)==s);if(!best.count(q)||best[q].c>c)best[q]={c,v};}
 }
 std::ofstream fs(argv[5]);std::vector<std::pair<uint32_t,Row>> out(best.begin(),best.end());std::sort(out.begin(),out.end(),[](auto&a,auto&b){return a.first<b.first;});for(auto &[q,x]:out)fs<<q<<' '<<x.c<<' '<<U(x.m)<<' '<<U(x.m>>64)<<'\n';std::cerr<<id<<' '<<n<<' '<<se<<' '<<sh<<' '<<out.size()<<'\n';
}
