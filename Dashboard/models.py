from django.db import models


# 自动生成sql语句
# app名_类名小写
"""
create table dashboard_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)
"""


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

    # class Department(models.Model):
    #     title = models.CharField(verbose_name="标题", max_length=32)
    # 无约束的
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 有约束的, -to:与哪张表关联，-to_filed:与表中的哪一列关联
    # 写的字段名是depart数据库中是depart_id
    # depart_id字段的值只能是Department已有的id
    # 级联删除：Department表删除某个部门，depart指定部门也会被删除
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE())
    # 置空
    # depart = models.ForeignKey(to="Department", to_fields="id", null=True, blank=True, on_delete=models.SET_NULL())

    # 在django中做的约束
    # 只能1或者2
    # gender_choices = (
    #     (1, "男"),
    #     (2, "女"),
    # )
    # gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

# 新建数据
# UserInfo.objects.create(name="v_hlhllu", password="123456", age="30")

# 删除数据
# row_obj = UserInfo.objects.filter(id=1).first()
# print(row_obj.id, row_obj.name)
# row_obj.delete()
# data_list = UserInfo.objects.all()
# for data in data_list:
#     print(data.id, data.name, data.password, data.age)
# data_list.delete()

# 更新数据
# UserInfo.objects.all().update(age=18)
# UserInfo.objects.filter(name="v_hlhllu").update(age=18)
