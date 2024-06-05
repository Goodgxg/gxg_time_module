import json


def batch_replace_keys(json_data, replacements):
    """
    批量替换JSON数据中的键名。

    参数:
    - json_data: 原始JSON数据，可以是字典或JSON字符串。
    - replacements: 映射字典，键为旧键名，值为新键名。

    返回:
    - 替换键名后的新JSON数据字典。

    replacements = {
    "name_old": "name",
    "age_old": "age"
}
    """
    # 如果传入的是JSON字符串，则先解析为字典
    if isinstance(json_data, str):
        json_data = json.loads(json_data)

    # 遍历映射表，执行键名替换
    for old_key, new_key in replacements.items():
        if old_key in json_data:
            json_data[new_key] = json_data.pop(old_key)

    return json_data