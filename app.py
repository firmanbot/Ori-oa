import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
handler = WebhookHandler(config['line_bot']['Channel_Secret'])
client_id = config['imgur_api']['Client_ID']
client_secret = config['imgur_api']['Client_Secret']
album_id = config['imgur_api']['Album_ID']
API_Get_Image = config['other_api']['API_Get_Image']


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "Jones":
        quote = ('Udah takdir itu mah...','Yang barusan ngetik itu orangnya...')
        jwbn = random.choice(quote)
        text_message = TextSendMessage(text=jwbn)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "Apakah " in event.message.text:
        quo = ('Iya','Tidak','Gak tau')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "Idl " in event.message.text:
        skss = event.message.text.replace('Idl ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Keyword":
        buttons_template = TemplateSendMessage(
            alt_text='ØRI Keyword',
            template=ButtonsTemplate(
                title='ØRI Keyword',
                text='Klik salah satu menu dibawah ini.',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    URITemplateAction(
                        label='Guild',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151441933104021159'
                    ),
                    URITemplateAction(
                        label='Pengurus',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151442178104024988'
                    ),
                    URITemplateAction(
                        label='Rules',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151442807704026737'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Welcome":
        buttons_template = TemplateSendMessage(
            alt_text='Isi data diri',
            template=ButtonsTemplate(
                title='Data member ØRI',
                text='Silahkan mengisi form data member dengan klik menu dibawah ini',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Dapatkan form',
                        text='Minta form dong min...'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0


if __name__ == '__main__':
    app.run()
