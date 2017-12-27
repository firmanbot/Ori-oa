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
        text_message = TextSendMessage(text=jwbn)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "Idl " in event.message.text:
        skss = event.message.text.replace('Idl ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Advent Stage":
        text_message = TextSendMessage(text='Coming soon')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "R":
        text_message = TextSendMessage(text='Viewlastseen')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Rs":
        text_message = TextSendMessage(text='Setlastpoint')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Dtbs Rangers":
        text_message = TextSendMessage(text='Coming soon')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Screen Recorder":
        text_message = TextSendMessage(text='Coming soon')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Emulator Android PC":
        text_message = TextSendMessage(text='Coming soon')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Keyword":    
        carousel_template_message = TemplateSendMessage(
            alt_text='Keyword Grup モの Rangers',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/qXBF4Xi.jpg',
                        title='モの keyword (Page 1)',
                        text='Keyword seputar grup モの Rangers',
                        actions=[
                            MessageTemplateAction(
                                label='Rules',
                                text='Rules'
                            ),
                            MessageTemplateAction(
                                label='Pengurus',
                                text='Pengurus'
                            ),
                            MessageTemplateAction(
                                label='Next Page'
                                text='Nxt Info'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/czohXnH.jpg',
                        title='About Line Rangers (Page 1)',
                        text='Info Line Rangers.',
                        actions=[
                            MessageTemplateAction(
                                label='Dtbs Rangers',
                                text='Dtbs Rangers'
                            ),
                            MessageTemplateAction(
                                label='Advent Stage',
                                text='Advent Stage'
                            ),
                            MessageTemplateAction(
                                label='Next Page',
                                text='Next Rgr'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/vpnKDDJ.jpg',
                        title='Tool :',
                        text='Apk yang disarankan bagi anda.',
                        actions=[
                            MessageTemplateAction(
                                label='Apk Clone',
                                text='App clone'
                            ),
                            MessageTemplateAction(
                                label='Screen Recorder',
                                text='Screen Recorder'
                            ),
                            MessageTemplateAction(
                                label='Emulator Android PC',
                                text='Emulator Android PC'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
        return 0
    if event.message.text == "Gears":
        buttons_template = TemplateSendMessage(
            alt_text='Gears Info',
            template=ButtonsTemplate(
                title='Gears Info',
                text='Klik salah satu menu dibawah ini.',
                thumbnail_image_url='https://imgur.com/k54UZcw.jpg',
                actions=[
                    URITemplateAction(
                        label='Gear Free/PVP/RAID',
                        uri='http://eo.moherbil.com/index.php?p=gears_free'
                    ),
                    URITemplateAction(
                        label='Gear ATK Range',
                        uri='http://eo.moherbil.com/index.php?p=gears_atkrange'
                    ),
                    URITemplateAction(
                        label='Gear Spam',
                        uri='http://eo.moherbil.com/index.php?p=gears_spam'
                    ),
                    URITemplateAction(
                        label='Gear Megaman',
                        uri='http://eo.moherbil.com/index.php?p=gears_ro'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Nxt info":
        buttons_template = TemplateSendMessage(
            alt_text='',
            template=ButtonsTemplate(
                title='モの keyword (Page 2)',
                text='Klik salah satu menu dibawah ini.',
                thumbnail_image_url='https://imgur.com/qXBF4Xi.jpg',
                actions=[
                    URITemplateAction(
                        label='Data Member',
                        uri='https://docs.google.com/spreadsheets/d/1ocqbpQHl65WbpSGHRxpYyciwa0S8UrOqMrKr3zw1FX4'
                    ),
                    MessageTemplateAction(
                        label='Guild Eo',
                        text='Guild eo'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Next Rgr":
        buttons_template = TemplateSendMessage(
            alt_text='About Rangers',
            template=ButtonsTemplate(
                title='About Line Rangers (Page 2)',
                text='Keyword ini akan menampilkan seputar Line Rangers.',
                thumbnail_image_url='https://imgur.com/czohXnH.jpg',
                actions=[
                    URITemplateAction(
                        label='Farm Leonard Point',
                        uri='https://docs.google.com/spreadsheets/d/1ocqbpQHl65WbpSGHRxpYyciwa0S8UrOqMrKr3zw1FX4'
                    ),
                    MessageTemplateAction(
                        label='Gears',
                        text='Gears'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "App clone":
        buttons_template = TemplateSendMessage(
            alt_text='App clone',
            template=ButtonsTemplate(
                title='Aplikasi clone',
                text='Klik salah satu menu dibawah ini.',
                thumbnail_image_url='https://imgur.com/Hbv4GWl.jpg',
                actions=[
                    URITemplateAction(
                        label='Parallel Space',
                        uri='https://play.google.com/store/apps/details?id=com.lbe.parallel.intl'
                    ),
                    URITemplateAction(
                        label='APP Cloner',
                        uri='https://play.google.com/store/apps/details?id=com.applisto.appcloner'
                    ),
                    URITemplateAction(
                        label='2Accounts',
                        uri='https://play.google.com/store/apps/details?id=com.excelliance.multiaccount'
                    ),
                    URITemplateAction(
                        label='Multi clone',
                        uri='https://play.google.com/store/apps/details?id=com.jumobile.multiapp'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Rules":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/uJFKjcs.jpg',
            alt_text='Rules Grup Evolved Rangers',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='Dibaca ya bukan di klik gambarnya',
                    area=ImagemapArea(
                        x=1, y=0, width=10, height=10
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
        return 0
    if event.message.text == "Sep 17":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/nsdrTRo.jpg',
            alt_text='Rangers Update September 2017',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='Dibaca ya bukan di klik gambarnya',
                    area=ImagemapArea(
                        x=1, y=0, width=10, height=10
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
        return 0
    if event.message.text == "Sep 16":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/tnfYdLa.jpg',
            alt_text='Rangers Update September 2016',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='Dibaca ya bukan di klik gambarnya',
                    area=ImagemapArea(
                        x=1, y=0, width=10, height=10
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
        return 0
    if event.message.text == "Pengurus":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/4Kn4DKS.jpg',
            alt_text='Pengurus Grup Evolved Rangers',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='Dibaca ya bukan di klik gambarnya',
                    area=ImagemapArea(
                        x=1, y=0, width=10, height=10
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
        return 0
    if event.message.text == "正妹":
        buttons_template = TemplateSendMessage(
            alt_text='正妹 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qKkE2bj.jpg',
                actions=[
                    MessageTemplateAction(
                        label='PTT 表特版 近期大於 10 推的文章',
                        text='PTT 表特版 近期大於 10 推的文章'
                    ),
                    MessageTemplateAction(
                        label='來張 imgur 正妹圖片',
                        text='來張 imgur 正妹圖片'
                    ),
                    MessageTemplateAction(
                        label='隨便來張正妹圖片',
                        text='隨便來張正妹圖片'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0


if __name__ == '__main__':
    app.run()
