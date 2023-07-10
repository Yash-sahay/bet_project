

from rest_framework import serializers


class superagentSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()
    mobile_no = serializers.CharField()
    super_agent_limit = serializers.CharField(default='')
    super_agent_share = serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')


class agentSerializer(serializers.Serializer):
    super_agent = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()
    mobile_no = serializers.CharField(default='')
    agent_limit = serializers.CharField(default='')
    agent_share=serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')


class clientSerializer(serializers.Serializer):
    agent_master = serializers.CharField()
    username = serializers.CharField()
    mobile_no = serializers.CharField()
    password = serializers.CharField()
    client_limit = serializers.CharField()
    match_commission = serializers.CharField()
    session_commission = serializers.CharField()


class updateuserSerializer(serializers.Serializer):
    
    current_limit = serializers.CharField()

    