#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstdint>
#include <string>
using U=uint64_t;struct Row{U q,l,h;int c;};constexpr U all=(U(1)<<45)-1;
int pc(U x){return __builtin_popcountll(x);}int main(int argc,char**argv){int shard=atoi(argv[3]),step=atoi(argv[4]);std::ifstream f(argv[1]),jobs(argv[2]);std::vector<Row>rows[14];std::unordered_map<U,Row>lookup;lookup.reserve(3000000);int c;U q,l,h;while(f>>q>>c>>l>>h){Row r={q,l,h,c};rows[pc(q)].push_back(r);lookup[q]=r;}
 for(auto&v:rows)std::sort(v.begin(),v.end(),[](auto &a,auto &b){return a.c<b.c;});U used,a,b;int ix=0;while(jobs>>used>>c>>a>>b){if(ix++%step!=shard)continue;int cap=(11292-c)/3,n=45-pc(used),scans=0;U free=all^used;
 for(int s=9;s<=12;s++)for(int t=s;t<=12;t++){int u=n-s-t;if(u<t||u>12)continue;std::vector<Row>v[2];int sz[3]={s,t,u};for(int j=0;j<2;j++){auto &list=rows[sz[j]];int slack=cap-rows[sz[j^1]][0].c-rows[u][0].c;
 for(auto &x:list){if(x.c>slack)break;if(!(x.q&used))v[j].push_back(x);}}
 for(auto &x:v[0]){for(auto&y:v[1]){if(x.c+y.c+rows[u][0].c>cap)break;if((x.q&y.q)||(s==t&&x.q>y.q))continue;auto z=lookup.find(free^x.q^y.q);if(z==lookup.end()||x.c+y.c+z->second.c>cap)continue;std::cout<<"hit "<<ix-1<<' '<<c+3*(x.c+y.c+z->second.c)<<' '<<a<<' '<<b<<' '<<x.l<<' '<<x.h<<' '<<y.l<<' '<<y.h<<' '<<z->second.l<<' '<<z->second.h<<std::endl;return 0;}}}
 if(ix%100==shard+1)std::cerr<<ix<<std::endl;
 }std::cerr<<"done "<<ix<<std::endl;}
