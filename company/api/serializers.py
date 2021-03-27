from rest_framework import serializers

from company.models import JobPosition, Label, Company


class LabelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'name', 'label_type')


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')


class JobPositionListSerializer(serializers.ModelSerializer):
    welfare_label = serializers.ListField(child=LabelListSerializer(), source='welfare_label.all')
    skill_label = serializers.ListField(child=LabelListSerializer(), source='skill_label.all')
    education = serializers.CharField(source='get_education_display')
    company = CompanyDetailSerializer()
    work_experience = serializers.CharField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = JobPosition
        fields = (
            'id', 'name', 'location', 'salary', 'welfare_label', 'skill_label', 'education', 'company',
            'work_experience',
        )

    def get_location(self, obj: JobPosition):
        location_list = list()
        if obj.location:
            location_list = obj.location.split('-')
        location_list = [i for i in location_list if i]
        return '-'.join(location_list)
