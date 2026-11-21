#include <array>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <stdexcept>
using namespace std;
constexpr int excMin[14]={0,0,12,36,72,120,201,292,419,557,744,1008,1244,99999};

int defect_budget=0;
array<vector<pair<int,int>>,14> defect_options;
unordered_map<unsigned,vector<int>> defect_memo;
long long capacity_tests=0,capacity_prunes=0;
void load_defect_options(const string& path,int budget){
  defect_budget=budget;defect_memo.clear();for(auto&v:defect_options)v.clear();
  ifstream file(path);if(!file)throw logic_error("missing complete cost-defect options");
  int size,cost,bound;
  while(file>>size>>cost>>bound){
    if(size<8||size>12||cost<excMin[size]||bound<0||bound>3*(size-2))throw logic_error("bad cost-defect option");
    int extra=cost-excMin[size];if(extra<=budget)defect_options[size].push_back({extra,bound});
  }
}
const vector<int>& defect_capacity(unsigned key){
  auto known=defect_memo.find(key);if(known!=defect_memo.end())return known->second;
  vector<int> result(defect_budget+1,key?-100000:0);
  if(key){int axis=0;while(((key>>(4*axis))&15)==0)++axis;
    const auto& previous=defect_capacity(key-(1u<<(4*axis)));
    for(auto [extra,bound]:defect_options[axis+8])for(int budget=extra;budget<=defect_budget;budget++)
      result[budget]=max(result[budget],previous[budget-extra]+bound);
  }
  return defect_memo.emplace(key,move(result)).first->second;
}

int main(int argc,char**argv){
  load_defect_options(argv[1],155);ifstream file(argv[2]);array<int,5>count{};long long tests=0;
  while(file>>count[0]){for(int i=1;i<5;i++)file>>count[i];int budget,expected;file>>budget>>expected;
    unsigned key=0;for(int i=0;i<5;i++){if(count[i]<0||count[i]>12)return 2;key|=unsigned(count[i])<<(4*i);}
    if(budget<0||budget>155||defect_capacity(key)[budget]!=expected)return 3;++tests;
  }
  cout<<tests<<"\n";
}
