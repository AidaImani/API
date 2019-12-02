from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddMassageSerializer, UpdateMessageSerializer, ListOfMassageSerializer, MassageSerializer, \
    ConversationSerializer,MakeConversationSerializer
from .models import Messages, Conversation
from django.contrib.auth.models import User



class Add_massage(APIView):
    def post(self, request):
        massage = AddMassageSerializer(data=request.POST,
                                       context={'user': request.user})
        if massage.is_valid():
            massage.save()
            return Response({'text': 'your massage saved'})

        else:
            return Response({'text': 'please enter valid data'})

    def put(self, request):
        u_massage = UpdateMessageSerializer(data=request.data,
                                            instance=Messages.objects.get(id=request.data['id']),)
        if u_massage.is_valid():
            u_massage.save()
            return Response({'text': 'your massage updated'})
        else:
            return Response({'text': 'please enter valid data'})

    def get(self, request):
        s = ListOfMassageSerializer(data=request.GET)
        if s.is_valid():
            c = Conversation.objects.get(
                id=request.GET['conversation_id']
            )
            messages = Messages.objects.filter(
                conversation=c
            )
            list_of_massage = []
            for massage in messages:
                m = MassageSerializer(massage)
                m = m.data
                list_of_massage.append(m)
            return Response(list_of_massage)
        else:
            return Response({'text': 'please enter valid data'})


class Conversations(APIView):
    def get(self, request):
        conv = Conversation.objects.all()
        conv = ConversationSerializer(conv, many=True)
        return Response(conv.data)

    def post(self, request):
        conversation = MakeConversationSerializer(data=request.POST)
        print(request.POST['members'])
        if conversation.is_valid():
            conversation.save()
            return Response({'text': 'your conversation created'})
        else:
            return Response({'text': 'please enter valid data'})

    # def post(self, request):
    #     conv_id = IdConversationSerializer(data=request.POST)
    #     if conv_id.is_valid():
    #         conv = Conversation.objects.get(id=request.POST['id'])
    #         conv = ConversationSerializer(conv)
    #         return Response(conv.data)
