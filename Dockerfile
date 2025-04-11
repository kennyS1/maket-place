# 使用官方 Python 镜像作为基础
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 运行数据库迁移
RUN python manage.py migrate

# 启动服务
CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
