# 地点：西安
# 姓名：雷兆江
# 时间：2022/10/7 13:47
import json
import random

from Student import Student

json_path = '../data/students.json'


def get_student_list():
    lastnames = ["雷", "付", "张", "樊", "信", "刘", "李", "赵", "田", "白"]
    firstname_1 = ["化", "江", "国", "娟", "蕾", "花", "婷", "平", "和", "海"]
    firstname_2 = ["化", "江", "国", "娟", "蕾", "花", "婷", "平", "和", "海"]
    student_list = list()
    n = 0

    while n < 10000:
        full_name = lastnames[random.randint(0, 9)] + firstname_1[random.randint(0, 9)] + firstname_2[
            random.randint(0, 9)]
        english = random.randint(0, 9)
        python = random.randint(0, 9)
        java = random.randint(0, 9)
        student = Student(n, full_name, english, python, java)
        student_list.append(student)
        n += 1
    return student_list


def insert():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    with open(json_path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()

        for item in lines:
            print(item)
            stu = json.loads(item, object_hook=Student)
            print(type(stu))


def total():
    with open(json_path, 'r') as fp:
        print("学生总数：" + str(fp.readlines().__len__()))


def show():
    with open(json_path, 'r') as fp:
        for line in fp.readlines():
            print(line)


def search():
    pass


def main():
    while True:
        menu()
        choice = int(input("请选择"))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定您要退出吗？y/n')
                if answer == 'n' or answer == 'N':
                    print("谢谢您的使用！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
                pass
            elif choice == 2:
                search()
                pass
            elif choice == 3:
                delete()
                pass
            elif choice == 4:
                modify()
                pass
            elif choice == 5:
                sort()
                pass
            elif choice == 6:
                total()
                pass
            elif choice == 7:
                show()
                pass


def menu():
    print("=====================================学生信息管理系统=========================================")
    print("========================================功能菜单=============================================")
    print("\t\t\t\t\t\t\t\t1、录入学生信息")
    print("\t\t\t\t\t\t\t\t2、查找学生信息")
    print("\t\t\t\t\t\t\t\t3、删除学生信息")
    print("\t\t\t\t\t\t\t\t4、修改学生信息")
    print("\t\t\t\t\t\t\t\t5、排序学生信息")
    print("\t\t\t\t\t\t\t\t6、统计学生总数")
    print("\t\t\t\t\t\t\t\t7、显示所有信息")
    print("\t\t\t\t\t\t\t\t0、退出")


def write_student_list_to_file():
    stu_lst = get_student_list()
    fp = open(json_path, 'a+')
    for stu in stu_lst:
        print(stu.__str__(), file=fp)
    fp.close()


if __name__ == '__main__':
    # show()
    sort()
