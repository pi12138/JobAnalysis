from django.db import models

# Create your models here.
from company.constants import (
    COMPANY_SIZE_CHOICES,
    CompanySize,
    EDUCATION_CHOICES,
    Education,
    RECRUITMENT_STATUS_CHOICES,
    RecruitmentStatus,
    LABEL_TYPE_CHOICES,
    LabelType,
)


class Company(models.Model):
    """
    公司
    """
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='公司名称')
    introduction = models.TextField(null=True, verbose_name='公司简介', blank=True)
    company_size = models.IntegerField(choices=COMPANY_SIZE_CHOICES, default=CompanySize.RANGE_0_TO_20, verbose_name='公司规模')
    Legal_person = models.CharField(max_length=255, null=True, verbose_name='法人', blank=True)
    date_of_establishment = models.DateField(verbose_name='成立时间')
    business_type = models.CharField(verbose_name='企业类型', null=True, blank=True)
    business_scope = models.TextField(verbose_name='经营范围', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='地址', null=True, blank=True)
    other_info = models.JSONField(default={}, null=True, verbose_name='其他信息', blank=True)


class JobPosition(models.Model):
    """
    工作岗位
    """
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位名称')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='工作地点')
    recruitment_status = models.IntegerField(choices=RECRUITMENT_STATUS_CHOICES, default=RecruitmentStatus.HIRING, verbose_name='招聘状态')
    welfare_label = models.ManyToManyField(to='Label', db_constraint=False, verbose_name='福利标签', related_name='welfare_label')
    salary = models.CharField(max_length=255, null=True, blank=True, verbose_name='薪水')
    work_experience = models.IntegerField(max_length=255, null=True, blank=True, verbose_name='工作经验')
    education = models.IntegerField(choices=EDUCATION_CHOICES, default=Education.OTHER, verbose_name='教育')
    recruiter = models.CharField(max_length=255, null=True, blank=True, verbose_name='照着')
    skill_label = models.ManyToManyField(to='Label', db_constraint=False, verbose_name='skill_label')
    job_description = models.TextField(null=True, blank=True, verbose_name="职位描述")
    company = models.ForeignKey(to=Company, db_constraint=False, on_delete=models.DO_NOTHING, verbose_name='公司')


class Label(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    label_type = models.IntegerField(choices=LABEL_TYPE_CHOICES, default=LabelType.SKILL)
