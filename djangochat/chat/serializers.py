from rest_framework import serializers
from chat.models import Messages, Conversations
from users.models import Users
from django.core.exceptions import ObjectDoesNotExist


class RequestChatSerializer(serializers.Serializer):
    token = serializers.IntegerField(
        required=True
    )
    text = serializers.CharField()
    conversation_id = serializers.IntegerField(
        min_value=1)
    
    def validate(self, data):
        try:
            Users.objects.get(
                token=validated_data['token'])
        except ObjectDoesNotExist:
            raise serializers.ValidataionError(
                'Error'
            )
        return data

    def create(self, validated_data):
        u = Users.objects.get(
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

