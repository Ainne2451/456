from django.shortcuts import render
from studentsapp.models import student
from django.http import HttpResponse

import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler

logger = logging.getLogger("django")

"""
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)
"""
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('CxVO4fNcPJFe3hszmu//G4BnLFRyhwv2pByFcB6h48HeelcuweOrvwg2+VHahoocWQyKqMyFI+Px27xdcUTLSxI8qPNz9v2+16nC26iUgqvbjcj6Mbwe+tJ5sgcv4EvLNNg8vL7VYIF2zIUoA0/YHgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('339f6e2054c10bc8f4fd19e2277fd4c8')

line_bot_api.push_message('Uae6995ae4c73190deaa1d36b1c3f1a7b', TextSendMessage(text='你可以開始了'))
