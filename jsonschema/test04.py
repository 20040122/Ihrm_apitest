# pattern关键字的使用
# 1.导入jsonschema模块
import jsonschema
# 2.定义校验规则
schema = {
    "type": "object",
    "properties": {
        "mobile": {"pattern":"^[0-9]{11}$"},
        "message": {"pattern":"^操"},
        "message": {"pattern":"！$"}

    },
    "required": ["mobile", "message"]
}
# 3.定义待校验的数据
data={
    "mobile": 13000000002,
    "message": "操作成功！"
}
# 4.调用validate()方法进行校验
result=jsonschema.validate(instance=data,schema=schema)
print(result)