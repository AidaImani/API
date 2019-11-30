from rest_framework import serializers
from .models import Messages
from .models import Conversation


class AddMassageSerializer(serializers.Serializer):
    conversation = serializers.IntegerField()
    text = serializers.CharField(
        max_length=100,
        allow_blank=False)

    def create(self, validated_data):
        c = Conversation.objects.get(
            id=validated_data['conversation'])
        m = Messages(
            text=validated_data['text'],
            sender=self.context['user'],
            conversation=c,
        )
        m.save()
        return m


class UpdateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = ["id", "text"]


class ListOfMassageSerializer(serializers.Serializer):
    conversation_id = serializers.IntegerField


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
