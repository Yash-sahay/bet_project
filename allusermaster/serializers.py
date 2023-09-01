

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


class MasterSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    mobile_no = serializers.CharField()
    master_limit = serializers.CharField(default='')
    master_share = serializers.CharField(default='')
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


# update serializers-----------------

class updatemasterSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    mobile_no = serializers.CharField()
    master_limit = serializers.CharField(default='')
    master_share = serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')





class updatesuperagentSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    mobile_no = serializers.CharField()
    super_agent_limit = serializers.CharField(default='')
    super_agent_share = serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')



class updateagentSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    mobile_no = serializers.CharField(default='')
    agent_limit = serializers.CharField(default='')
    agent_share=serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')
    

class updateclientSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    mobile_no = serializers.CharField(default='')
    client_limit = serializers.CharField(default='')
    match_commission=serializers.CharField(default='')
    session_commission=serializers.CharField(default='')