import json
import random
import re
from http import HTTPStatus
from dashscope import Generation  # 建议dashscope SDK 的版本 >= 1.14.0
import dashscope

import jsonkeyreplace

dashscope.api_key = 'sk-dfc5d20c4dcd4463b2922f912d621415'
SCHEMA_INFO = '提取出组织机构，业务部门，出差人，出差城市，出发城市，出发日期，返回日期，出差事由 的信息并只返回json数据'
REPLACEMENTS = {
    "组织机构":"comp",
    "业务部门":"dep",
    "出差人":"user",
    "出发日期":"startDate",
    "返回日期":"endDate",
    "出发城市":"startCity",
    "出差城市":"endCity",
    "出差事由":"reason"
}
def call_with_messages(text):
    messages = [{'role': 'user', 'content': text + " " +SCHEMA_INFO}]
    json_pattern = r'({.*?})'
    result = ''

    response = Generation.call(model="qwen-max",
                               messages=messages,
                               # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
                               seed=random.randint(1, 10000),
                               # 将输出设置为"message"格式
                               result_format='message')
    if response.status_code == HTTPStatus.OK:
        res_result=response.output.choices[0]['message']['content']
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
    match = re.search(json_pattern,res_result,re.DOTALL)
    if match:
        json_string = match.group(1)
        try:
            result = json.loads(json_string)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("No JSON found in the text.")
    print(result)

    return  jsonkeyreplace.batch_replace_keys(result,REPLACEMENTS)
    # return  result

if __name__ == '__main__':
    print(call_with_messages("明天与财务处%20张三前往西安、成都参加集团公司组织的会议培训，计划%204月20日返回"))