import json

def read_schema(schema_path):
    # 读取schema
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    return schema

def add_args_to_schema(schema):
    # 为schema添加args
    # 原始的schema是一个树型结构，若该节点的value以“【NA】”结尾，则该节点有若干子节点，包含在children中
    # 若该节点的value不以“【NA】”结尾，则该节点为叶子节点，即事件类型，其value即为事件类型
    # 遍历schema，若该节点的value不以“【NA】”结尾，则将该节点的之前的路径和该节点的value组成的字符串作为事件类型，并加入args_list作为该事件类型的args
    # 返回new_schema, new_schema的格式为{event_type: [args]}
    args_list = ["主体", "对象", "时间", "地点"]
    new_schema = {}
    path = []
    def dfs(schema):
        if schema['value'].endswith('【NA】'):
            path.append(schema['value'][:-4])
            for child in schema['children']:
                dfs(child)
            path.pop()
        else:
            event_type = '_'.join(path + [schema['value']])
            new_schema[event_type] = args_list
    for con in schema:
        dfs(con)
    return new_schema


if __name__ == '__main__':
    schema = read_schema('data/raw/schema.json')
    new_schema = add_args_to_schema(schema)
    with open('data/schema.json', 'w') as f:
        json.dump(new_schema, f, ensure_ascii=False, indent=4)
    print("a")
    