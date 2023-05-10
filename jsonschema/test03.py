# const关键字的使用
import jsonschema

schema = {
    "type": "object",
    "properties": {
        "success": {"const": True},
        "code": {"const":10000},
        "message": {"const": "操作成功！"}
    },
    "required": ["success", "code", "message"]
}

data={
    "success": True,
    "code": 10000,
    "message": "操作成功！"
}

result=jsonschema.validate(instance=data,schema=schema)

print(result)