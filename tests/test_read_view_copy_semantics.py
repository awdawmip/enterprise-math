from copy import deepcopy
from control_plane.research_read_view import _copy_read,read_view,reuse_read


def test_nested_containers_are_independent_and_shared_aliases_remain_shared():
    shared={'values':[1,None,'proof']}
    original={'first':shared,'second':shared,'tuple':(shared,3)}
    value=_copy_read(original)
    assert value==deepcopy(original)
    assert value['first'] is value['second'] is value['tuple'][0]
    value['first']['values'].append('changed')
    assert original['first']['values']==[1,None,'proof']


def test_dict_list_and_tuple_cycles_match_deepcopy():
    original={};original['self']=original
    value=_copy_read(original)
    assert value is value['self'] and value is not original
    child=[];cycle=(child,);child.append(cycle)
    value=_copy_read(cycle)
    assert value[0][0] is value and value is not cycle


def test_custom_mutable_objects_keep_their_original_deepcopy_protocol():
    class Mutable:
        def __init__(self,values):self.values=values
        def __deepcopy__(self,memo):
            result=Mutable(deepcopy(self.values,memo));memo[id(self)]=result;return result
    item=Mutable(['original']);value=_copy_read({'item':item})
    value['item'].values.append('changed')
    assert item.values==['original']


def test_cache_does_not_share_mutable_result_with_first_or_later_caller(tmp_path):
    original={'a':[1]}
    with read_view(tmp_path):
        first=reuse_read(tmp_path,'copy',(),lambda:original)
        first['a'].append(2)
        second=reuse_read(tmp_path,'copy',(),lambda:None)
        assert second=={'a':[1]}
        second['a'].append(3)
        assert reuse_read(tmp_path,'copy',(),lambda:None)=={'a':[1]}
