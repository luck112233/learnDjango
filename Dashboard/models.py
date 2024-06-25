from django.db import models


class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)


class UserInfo(models.Model):
    # 自动生成sql语句（app名_类名小写）
    # create table dashboard_userinfo(
    #     id bigint auto_increment primary key,
    #     name varchar(32),
    #     password varchar(64),
    #     age int
    # )
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    # 可以为空
    # data = models.IntegerField(null=True, blank=True)
    # 数字长度为10，小数位为2
    account = models.DecimalField(verbose_name="账户余额", default=0, max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(verbose_name="入职时间")
    # 无约束的
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 有约束的, -to:与哪张表关联，-to_filed:与哪一列关联，depart_id字段的值只能是Department已有的id
    # django自动给dpart加上_id，所以最终字段名是depart_id
    # 级联删除：Department表删除某个部门，UserInfo表指定部门下的用户也会被删除
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE)
    # 置空：Department表删除某个部门，UserInfo表指定部门下的用户部门置空
    depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    # django给的约束，只能1或者2
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


