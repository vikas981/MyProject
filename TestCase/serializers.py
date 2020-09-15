from rest_framework import serializers
from .models import *


class TestcasedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcasedetail
        fields = "__all__"


class TestcaseSerializer(serializers.ModelSerializer):
    testcase = TestcasedetailSerializer(many=True, read_only=True)

    class Meta:
        model = Testcase
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    client = TestcaseSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = "__all__"


class ModulSerializer(serializers.ModelSerializer):
    module = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = "__all__"
