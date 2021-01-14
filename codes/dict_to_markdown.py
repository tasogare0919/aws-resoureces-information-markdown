import pandas as pd

def dict_to_markdown(dc, title="TOP", depth=1, format="md"):

    # format(md or org)
    head_str = "*" if format == "org" else "#"

    # データ変換
    items = []
    if type(dc) == dict:
        items = dc.items()
    elif type(dc) == list:
        items = [("#{}".format(i+1),v)for i, v in enumerate(dc)]

    # 表示可能アイテムと表示不可能アイテムに分類
    displayable = [(k,v) for k,v in items if type(v) not in [dict, list]]
    not_displayable = [(k,v) for k, v in items if type(v) in [dict, list]]

    #　見出しを表示
    print("{} {}".format(head_str * depth, title))

    #表示可能アイテムを表示
    if displayable:
        print(pd.DataFrame(displayable,columns=["key", "value"]).to_markdown(index=False))

    #表示不可能アイテムをパース
    for k, v in not_displayable:
        dict_to_markdown(v, title=k, depth=depth+1, format=format)