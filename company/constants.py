class CompanySize:
    RANGE_0_TO_20 = 1
    RANGE_20_TO_99 = 2
    RANGE_100_TO_499 = 3
    RANGE_500_TO_999 = 4
    RANGE_1000_TO_9999 = 5
    GT_10000 = 6


COMPANY_SIZE_CHOICES = (
    (CompanySize.RANGE_0_TO_20, '0-20'),
    (CompanySize.RANGE_20_TO_99, '20-99'),
    (CompanySize.RANGE_100_TO_499, '100-499'),
    (CompanySize.RANGE_500_TO_999, '500-999'),
    (CompanySize.RANGE_1000_TO_9999, '1000-9999'),
    (CompanySize.GT_10000, '>10000'),
)


class Education:
    OTHER = 1
    JUNIOR_COLLEGE = 2
    UNDERGRADUATE = 3
    MASTER_DEGREE = 4
    PHD = 5


EDUCATION_CHOICES = (
    (Education.OTHER, '其他'),
    (Education.JUNIOR_COLLEGE, '大专'),
    (Education.UNDERGRADUATE, '本科'),
    (Education.MASTER_DEGREE, '硕士'),
    (Education.PHD, '博士'),
)


class RecruitmentStatus:
    HIRING = 1
    STOP_HIRING = 2


RECRUITMENT_STATUS_CHOICES = (
    (RecruitmentStatus.HIRING, '招聘中'),
    (RecruitmentStatus.STOP_HIRING, '停止招聘'),
)


class LabelType:
    SKILL = 1
    WELFARE = 2


LABEL_TYPE_CHOICES = (
    (LabelType.SKILL, '技能'),
    (LabelType.WELFARE, '福利')
)
