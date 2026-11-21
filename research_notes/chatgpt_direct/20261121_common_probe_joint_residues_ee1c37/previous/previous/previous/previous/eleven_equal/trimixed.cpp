#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using U=uint64_t;struct Row{U q;int c,s,d;};const U eye=19808391266305,full=(U(1)<<45)-1;const int INF=1000000;int pc(U q){return __builtin_popcountll(q);}
std::vector<Row>fixed;std::vector<int>by[45],path;std::vector<std::pair<int,U>> mobile[14];std::unordered_map<U,int>mapcost;int lower[12][46][6][4];int ar,shard,shards,best=11293;U moved[2];long long nodes=0,mobile_queries=0;bool found=false;std::unordered_map<U,int>memo[12];
void success(int c){found=true;std::cout<<"hit "<<c;for(int i:path)std::cout<<" f"<<fixed[i].q;for(int i=0;i<ar;i++)std::cout<<" m"<<moved[i];std::cout<<std::endl;}
void finish(U free,int n,int cost){if(ar==0){if(!n)success(cost);return;}if(ar==1){auto iter=mapcost.find(free);if(iter!=mapcost.end()&&cost+3*iter->second<best){moved[0]=free;success(cost+3*iter->second);}return;}
 for(int s=9;s<=12;s++){int t=n-s;if(t<s||t>12)continue;int cap=(best-1-cost)/3-mobile[t][0].first;
 for(auto [c,q]:mobile[s]){if(c>cap)break;if(q&~free)continue;++mobile_queries;auto it=mapcost.find(free^q);if(it==mapcost.end()||cost+3*(it->second+c)>=best)continue;moved[0]=q;moved[1]=free^q;success(cost+3*(it->second+c));return;}}}
void solve(U free,int count,int cost,int id,int big){if(found)return;++nodes;int n=pc(free),d=pc(free&eye);if(cost+lower[count][n][d][ar]>=best)return;if(!count){if(!d)finish(free,n,cost);return;}
 U key=free|(U(big)<<45);auto it=memo[count].find(key);if(it!=memo[count].end() && it->second<=cost)return;if(memo[count].size()<1000000)memo[count][key]=cost;
 int pivot=-1,least=100000;if(d){for(U bits=free&eye;bits;bits&=bits-1){int k=__builtin_ctzll(bits),remain=0;for(int i:by[k]){auto&r=fixed[i];if((r.q&~free)==0&&cost+r.c+lower[count-1][n-pc(r.q)][d-r.d][ar]<best)remain++;if(remain>=least)break;}if(remain<least){pivot=k;least=remain;if(!least)return;}}}
 static std::vector<int> all; if(all.empty())for(int i=0;i<fixed.size();i++)all.push_back(i);
 const auto &opts=pivot<0?all:by[pivot];int branch=0;for(int ix:opts){auto&r=fixed[ix];if(big+(r.s==13)>2)continue;if(r.q&~free)continue;if(cost+r.c+lower[count-1][n-pc(r.q)][d-r.d][ar]>=best)continue;if(id==0 && branch++%shards!=shard)continue;path.push_back(ix);solve(free^r.q,count-1,cost+r.c,id+1,big+(r.s==13));path.pop_back();if(found)return;}}
int main(int argc,char**argv){std::ifstream f(argv[1]),m(argv[2]);ar=std::stoi(argv[3]);shard=std::stoi(argv[4]);shards=std::stoi(argv[5]);U q,l,h;int c;while(f>>q>>c){int d=pc(q&eye);fixed.push_back({q,c,3*pc(q)-2*d,d});}while(m>>q>>c>>l>>h){mapcost[q]=c;mobile[pc(q)].push_back({c,q});}for(auto&v:mobile)std::sort(v.begin(),v.end());std::sort(fixed.begin(),fixed.end(),[](auto&a,auto&b){return a.c-186*a.s<b.c-186*b.s;});for(int j=0;j<fixed.size();j++)for(U b=fixed[j].q&eye;b;b&=b-1)by[__builtin_ctzll(b)].push_back(j);
 int fm[10][6];for(auto&x:fm)for(auto &v:x)v=INF;for(auto&r:fixed){int&v=fm[pc(r.q)][r.d];v=std::min(v,r.c);}for(auto&a:lower)for(auto&b:a)for(auto&c:b)for(auto&v:c)v=INF;lower[0][0][0][0]=0;
 for(int t=1;t<4;t++)for(int n=0;n<=45;n++)for(int s=9;s<=12&&s<=n;s++)lower[0][n][0][t]=std::min(lower[0][n][0][t],lower[0][n-s][0][t-1]+3*mobile[s][0].first);
 for(int k=1;k<=11;k++)for(int n=1;n<=45;n++)for(int d=0;d<=5;d++)for(int t=0;t<4;t++)for(int s=1;s<10&&s<=n;s++)for(int e=0;e<=d;e++)lower[k][n][d][t]=std::min(lower[k][n][d][t],lower[k-1][n-s][d-e][t]+fm[s][e]);
 solve(full,11-3*ar,0,0,0);std::cerr<<shard<<" nodes "<<nodes<<" query "<<mobile_queries<<" found "<<found<<'\n';
}
