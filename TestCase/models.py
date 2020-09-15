from django.db import models


class Module(models.Model):
    module_name = models.CharField(max_length=30, primary_key=True)

    class Meta:
        verbose_name_plural = "module"

    def __str__(self):
        return self.module_name


class Client(models.Model):
    client_name = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='module')


class Testcase(models.Model):
    Test_Case_Id = models.CharField(max_length=50, primary_key=True)
    Test_Case_Description = models.CharField(max_length=1000)
    testcase_slug = models.CharField(max_length=20)
    client = models.ForeignKey(Client, related_name='client', on_delete=models.CASCADE)


class Testcasedetail(models.Model):
    STATUS = (
        ('Approved', 'Approved'),
        ('Disapproved', 'Disapproved')
    )
    Test_Step_Id = models.CharField(max_length=100, primary_key=True)
    Test_Step_Description = models.CharField(max_length=100)
    Keyword = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, null=True)
    testcase = models.ForeignKey(Testcase, related_name='testcase', on_delete=models.CASCADE)

    def __str__(self):
        return self.Test_Step_Id
