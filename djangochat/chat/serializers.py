from rest_framework import serializers
from chat.models import Messages, Conversations
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RequestChatSerializer(serializers.Serializer):
    text = serializers.CharField()
    conversation_id = serializers.IntegerField(
        min_value=1)
    
    def validate(self, data):
        try:
            User.objects.get(
                token=data['token'])
        except ObjectDoesNotExist:
            raise serializers.Validat7ionError(
                'Error'
            )
        return data

    def create(self, validated_data):
        u = User.objects.get(
                token=validated_data['token'])
        c = Conversations.objects.get(
                id=validated_data['conversation_id'])
        m = Messages(
            conversation_id=c,
            text=validated_data['text'],
            date='2019-08-10',
            sender_id=u
        )
        m.save()
        return m

