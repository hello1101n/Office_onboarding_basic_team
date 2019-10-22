from dialog_bot_sdk.bot import DialogBot
from pymongo import MongoClient
import grpc

# Utils
client = MongoClient(port=27017)
db = client.onboarding


def on_msg(*params):
    print('on msg', params)
    bot.messaging.send_message(
        params[0].peer, 'Hello user')


# Add data to db
def add_user_to_admins(id):
    db.reviews.insert_one({
        'name': 'Office-manager',
        'id': id
    })


# Main fun
def main(*params):
    on_msg(*params)
    i = 0
    j = 0
    if i == 0:
        j = 1
        add_user_to_admins(params[0].peer.id)
    if j == 1:
        bot.messaging.send_message(
            params[0].peer, 'You are office manager!')


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        # bot endpoint (specify different endpoint if you want to connect to your on-premise environment)
        'hackathon-mob.transmit.im',
        grpc.ssl_channel_credentials(),  # SSL credentials (empty by default!)
        '4a3a998e50c55e13fb4ef9a52a224303602da6af',  # bot token
        verbose=False  # optional parameter, when it's True bot prints info about the called methods, False by default
    )

# work like return , block code after, if want to use code after, use async vers
bot.messaging.on_message(main)