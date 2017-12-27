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
    if event.message.text == "R":
        text_message = TextSendMessage(text='Viewlastseen')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Rs":
        text_message = TextSendMessage(text='Setlastpoint')
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
                    MessageTemplateAction(
                        label='Guild',
                        text='Guild ori'
                    ),
                    MessageTemplateAction(
                        label='Pengurus',
                        text='Pengurus ori'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Pengurus ori":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/6rXwN9P.jpg',
            alt_text='Pengurus ØRI',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='http://line.me/R/ti/p/~ardianwrz',
                    area=ImagemapArea(
                        x=1040, y=1040, width=260, height=260
                    )
                ),
                URIImagemapAction(
                    link_uri='http://line.me/R/ti/p/~hinz85',
                    area=ImagemapArea(
                        x=0, y=1040, width=260, height=260
                    )
                ),
                URIImagemapAction(
                    link_uri='http://line.me/R/ti/p/~jeremiviki18',
                    area=ImagemapArea(
                        x=260, y=1040, width=260, height=260
                    )
                ),
                URIImagemapAction(
                    link_uri='http://line.me/R/ti/p/~ultraleonard',
                    area=ImagemapArea(
                        x=520, y=1040, width=260, height=260
                    )
                ),
                URIImagemapAction(
                    link_uri='http://line.me/R/ti/p/~denz_1717',
                    area=ImagemapArea(
                        x=260, y=780, width=260, height=260
                    )
                ),
                URIImagemapAction(
                    link_uri='http://line.me/R/ti/p/~zavielpratama',
                    area=ImagemapArea(
                        x=520, y=780, width=260, height=260
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
        return 0
    if event.message.text == "Guild ori":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/8lIaC0N.jpg',
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
