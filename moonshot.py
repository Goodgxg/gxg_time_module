import json
import re
from time import sleep

from openai import OpenAI

import jsonkeyreplace

client = OpenAI(
    api_key="sk-1idpN3Em0QVPIvV4md8KnxNdEzsKSzxmDbIZZgjprER4Et1D",
    base_url="https://api.moonshot.cn/v1",
)
SCHEMA_INFO = "提取出 组织机构，业务部门，人员，出差城市，出发城市，出发日期，返回日期，出差事由 并返回只有一个大括号的json数据"
REPLACEMENTS = {
    "组织机构": "comp",
    "业务部门": "dep",
    "人员": "user",
    "出发日期": "startDate",
    "返回日期": "endDate",
    "出发城市": "startCity",
    "出差城市": "endCity",
    "出差事由": "reason"
}


def moonshot_get_resul(text):
    # json_pattern = r'\{.*?\}'
    json_pattern = r'({.*?})'
    result = ''
    sleep(3)
    completion = client.chat.completions.create(
        model="moonshot-v1-128k",
        messages=[
            {"role": "system",
             "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
            {"role": "user", "content": text + " " + SCHEMA_INFO}
        ],
        temperature=0.1,
    )

    res_result = completion.choices[0].message.content
    match = re.search(json_pattern, res_result, re.DOTALL)
    # match = re.findall(json_pattern,res_result)
    if match:
        json_string = match.group(1)
        try:
            result = json.loads(json_string)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("No JSON found in the text.")
    print(res_result)
    print(result)
    print(jsonkeyreplace.batch_replace_keys(result,REPLACEMENTS))
    return jsonkeyreplace.batch_replace_keys(result,REPLACEMENTS)


print(moonshot_get_resul("本人张三申请明天去成都进行出差，与大集中erp项目进行沟通，大约对接一周左右返回。同行人为财务处王德锋和办公室李四"))
