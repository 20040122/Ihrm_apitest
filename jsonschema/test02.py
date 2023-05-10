# properties嵌套使用
import jsonschema

schema = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"}
            }
        }
    },
        "required": ["success", "code", "message", "data"]
}

data = {
    "success": True,
    "code": 10000,
    "message": "操作成功！",
    "data": {
        "name": "张三",
        "age": 18,
    }
}

result = jsonschema.validate(instance=data, schema=schema)
print(result)