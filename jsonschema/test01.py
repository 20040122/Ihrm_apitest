# 1.导入jsonschema模块
import jsonschema
# 2.定义校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type": "integer"},
        "message": {"type": "string"}
    },
    "required": ["success", "code", "message"]
}
# 3.定义待校验的数据
data={
    "success": True,
    "code": 10000,
    "message": "操作成功！"
}
# 4.调用validate()方法进行校验
result=jsonschema.validate(instance=data,schema=schema)
print(result)