from django.shortcuts import render
from phonebook.models import Contact
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

def phones(request):
    contacts = Contact.objects.all()
    return render(request, "phones.html", {"contacts": contacts})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contactList.html', {'contacts': contacts})

def user_online(user_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_add)('online_users', str(user_id))

def user_offline(user_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_discard)('online_users', str(user_id))

def online_users(request):
    if request.user.is_superuser:
        channel_layer = get_channel_layer()
        online_users = async_to_sync(channel_layer.group_channels)('online_users')
        return JsonResponse({'online_users_count': len(online_users)})
    else:
        return JsonResponse({'error': 'Only superuser can access this endpoint'}, status=403)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_auth_token(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})
