

from rest_framework import serializers


class superagentSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()
    mobile_no = serializers.CharField()
    super_agent_limit = serializers.CharField(default='')
    super_agent_share = serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')


class agentSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()
    mobile_no = serializers.CharField(default='')
    agent_limit = serializers.CharField(default='')
    agent_share=serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')


class clientSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    username = serializers.CharField()
    mobile_no = serializers.CharField(default='')
    password = serializers.CharField()
    client_limit = serializers.CharField(default='')
    match_commission = serializers.CharField(default='')
    session_commission = serializers.CharField(default='')


class updateuserSerializer(serializers.Serializer):
    
    current_limit = serializers.CharField()

    