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


EDUCATION_VERBOSE_NAME_TO_VALUE = {i[1]: i[0] for i in EDUCATION_CHOICES}


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


class JobDirection:
    JAVA = 1
    PYTHON = 2
    PHP = 3
    FRONT_END = 4
    PRODUCT_MANAGER = 5
    SOFTWARE_TEST = 6
    SOFTWARE_IMPLEMENTATION = 7
    UI_DESIGN = 8
    INTERNET_MARKETING = 9
    ALGORITHM = 10
    BLOCKCHAIN = 11
    BIG_DATA = 12
    CLOUD_COMPUTING = 13
    MOBILE_DEVELOPMENT = 14
    GAME_DEVELOPMENT = 15
    EMBEDDED_DEVELOPMENT = 16
    OPERATIONS_ENGINEER = 17
    GOLANG = 18


JOB_DIRECTION_TO_VERBOSE_NAME = {
    JobDirection.JAVA: 'JAVA开发',
    JobDirection.PYTHON: 'Python开发',
    JobDirection.PHP: 'PHP开发',
    JobDirection.FRONT_END: '前端开发',
    JobDirection.PRODUCT_MANAGER: '产品经理',
    JobDirection.SOFTWARE_TEST: '软件测试',
    JobDirection.SOFTWARE_IMPLEMENTATION: '软件实施',
    JobDirection.UI_DESIGN: 'UI设计',
    JobDirection.INTERNET_MARKETING: '互联网营销',
    JobDirection.ALGORITHM: '算法工程师',
    JobDirection.BLOCKCHAIN: '区块链',
    JobDirection.BIG_DATA: '大数据',
    JobDirection.CLOUD_COMPUTING: '云计算',
    JobDirection.MOBILE_DEVELOPMENT: '移动端开发',
    JobDirection.GAME_DEVELOPMENT: '游戏开发',
    JobDirection.EMBEDDED_DEVELOPMENT: '嵌入式开发',
    JobDirection.OPERATIONS_ENGINEER: '运维工程师',
    JobDirection.GOLANG: 'golang开发',
}


JOB_DIRECTION_CHOICES = (
    (JobDirection.JAVA, 'JAVA开发'),
    (JobDirection.PYTHON, 'Python开发'),
    (JobDirection.PHP, 'PHP开发'),
    (JobDirection.FRONT_END, '前端开发'),
    (JobDirection.PRODUCT_MANAGER, '产品经理'),
    (JobDirection.SOFTWARE_TEST, '软件测试'),
    (JobDirection.SOFTWARE_IMPLEMENTATION, '软件实施'),
    (JobDirection.UI_DESIGN, 'UI设计'),
    (JobDirection.INTERNET_MARKETING, '互联网营销'),
    (JobDirection.ALGORITHM, '算法工程师'),
    (JobDirection.BLOCKCHAIN, '区块链'),
    (JobDirection.BIG_DATA, '大数据'),
    (JobDirection.CLOUD_COMPUTING, '云计算'),
    (JobDirection.MOBILE_DEVELOPMENT, '移动端开发'),
    (JobDirection.GAME_DEVELOPMENT, '游戏开发'),
    (JobDirection.EMBEDDED_DEVELOPMENT, '嵌入式开发'),
    (JobDirection.OPERATIONS_ENGINEER, '运维工程师'),
    (JobDirection.GOLANG, 'golang开发'),
)


VERBOSE_NAME_TO_JOB_DIRECTION = {value: key for key, value in JOB_DIRECTION_TO_VERBOSE_NAME.items()}


class AnalysisType:
    JOB_DIRECTION = 1
    SKILL_LABEL = 2
    WELFARE_LABEL = 3
