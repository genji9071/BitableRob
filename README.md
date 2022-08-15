# lark-bitable-sdk
飞书多维表格，关于记录增删改查相关的api

## 安装方法
    pip install lark-bitable-sdk

## 使用方法
    Auth(app_id="your_app_id", app_secret="your_app_secret")
    fetch_records("app_token", "table_id", field_names='["field_name"]', page_size=3)

## 一个例子
    test/__init__.py