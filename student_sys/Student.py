# 地点：西安
# 姓名：雷兆江
# 时间：2022/10/7 14:15
class Student:
    def __init__(self, sid, name, english, python, java):
        super().__init__()
        self.sid = sid
        self.name = name
        self.english = english
        self.python = python
        self.java = java

    def __str__(self):
        return f"""{{ "id": {self.id}, "name": "{self.name}", "english": {self.english}, "python": {self.python}, "java": {self.java} }}"""
