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
    elif "Siapakah " in event.message.text:
        jawan = ('Orang yang suka gosip kak...','Orang yang suka ngalong kak...','dia jones lho, temenin gih...','Orang yang baik dan tidak sombong kak...','Orang yang suka baperan kak...','Dia sultan lho...','Dia yang kemarin nabrak tiang listrik...')
        dsa = random.choice(jawan)
        text_message = TextSendMessage(text=dsa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Makanan":
        quor = ('https://imgur.com/Gl0lcYB.jpg','https://imgur.com/1Sae11M.jpg','https://imgur.com/ZuChLoV.jpg','https://imgur.com/miHQFHT.jpg','https://imgur.com/lhR1aW3.jpg','https://imgur.com/qf6gwYQ.jpg','https://imgur.com/3nbHyTw.jpg','https://imgur.com/wq83igW.jpg')
        jwbr = random.choice(quor)
        image_message = ImageSendMessage(
            original_content_url=jwbr,
            preview_image_url=jwbr
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        return 0
    elif "/lr" in event.message.text:
        text_message = TextSendMessage(text='Gak ada po disini\nLewat personal chat aja ya...\nNih kontaknya\nhttp://line.me/R/ti/p/~@qik6373h\nhttp://line.me/R/ti/p/~@qik6373h')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "Kapan " in event.message.text:
        quo = ('Hari ini','Besok','Lusa','Minggu depan','Sebulan lagi','Setahun lagi','Tanya langsung ke orangnya...')
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
    if event.message.text == "Key":
        buttons_template = TemplateSendMessage(
            alt_text='Key ØRI',
            template=ButtonsTemplate(
                title='Key ØRI',
                text='Pilih salah satu menu dibawah ini',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    MessageTemplateAction(
                        label='About ORI',
                        text='ORI grup'
                    ),
                    MessageTemplateAction(
                        label='Hiburan',
                        text='Hiburan'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "ORI grup":
        buttons_template = TemplateSendMessage(
            alt_text='About ORI',
            template=ButtonsTemplate(
                title='About ORI',
                text='Pilih salah satu menu dibawah ini',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Pengurus',
                        text='Pengurus'
                    ),
                    MessageTemplateAction(
                        label='Rules',
                        text='Rules'
                    ),
                    MessageTemplateAction(
                        label='Guild',
                        text='Guild'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Hiburan":
        buttons_template = TemplateSendMessage(
            alt_text='Hiburan',
            template=ButtonsTemplate(
                title='Hiburan',
                text='Pilih salah satu menu dibawah ini',
                thumbnail_image_url='https://imgur.com/RBDkN79.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Kerang ajaib',
                        text='Kerajib'
                    ),
                    MessageTemplateAction(
                        label='Penjwb Pertanyaan',
                        text='Rules satuan'
                    ),
                    MessageTemplateAction(
                        label='Foto makanan',
                        text='Makanan'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Rules":
        buttons_template = TemplateSendMessage(
            alt_text='Rules ØRI',
            template=ButtonsTemplate(
                title='Rules ØRI',
                text='Dalam versi apa?',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Versi satuan',
                        text='Rules satuan'
                    ),
                    URITemplateAction(
                        label='Versi full',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151442807704026737'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Pengurus":
        buttons_template = TemplateSendMessage(
            alt_text='Pengurus ØRI',
            template=ButtonsTemplate(
                title='Pengurus ØRI',
                text='Pengen tau? klik menu dibawah ini',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    URITemplateAction(
                        label='Info',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151442178104024988'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Guild":
        buttons_template = TemplateSendMessage(
            alt_text='Guild ØRI',
            template=ButtonsTemplate(
                title='Guild ØRI',
                text='Gak punya guild? join aja...',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    URITemplateAction(
                        label='Info',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151441933104021159'
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
                title='isi data dinote grup.diberi wkt 1x24 jam',
                text='lewat dari wkt yg di tentukan akan di kick',
                thumbnail_image_url='https://imgur.com/8wsvtGU.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Dapatkan form',
                        text='Minta form dong min...'
                    ),
                    URITemplateAction(
                        label='Dibaca juga Rulesnya',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151442807704026737'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0


if __name__ == '__main__':
    app.run()
