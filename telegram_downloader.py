import os
import argparse
from telethon.sync import TelegramClient, events

# ------------------------------------------------------------------ #
# To get API_ID & API HASH, create a new app in the following link:
# https://my.telegram.org/apps
# ------------------------------------------------------------------ #
API_ID = -1 # PLACE HERE THE API ID OF YOUR TELEGRAM APP
API_HASH = "" # PLACE HERE THE API HASH OF YOUR TELEGRAM APP


def download(videos_dir, group_id, limit):
    """
    Function that downloads the last "limit" videos from a Telegram group.
    To save disk space, the function deletes videos not present in group 
    messages.
    """

    # check if directory exists
    if not os.path.isdir(videos_dir):
        os.mkdir(videos_dir)
    videos_list = os.listdir(videos_dir)

    # create Telegram client
    with TelegramClient('RaspberryPi', API_ID, API_HASH) as client:

        # get the messages from the telegram group
        messages = client.get_messages(group_id, limit=limit)

        if len(messages) == 0:
            print('The group is empty. Nothing to download')
            os._exit(0)

        # get list of videos to download
        msg_videos_list = [
            msg.file.name for msg in messages
        ]

        # for each video in disk...
        for video_name in videos_list:

            # remove the video in disk that is not in the ones to download
            if video_name not in msg_videos_list:
                print('-' * 30)
                print('Removing {}'.format(video_name))
                print('-' * 30)
                os.remove(os.path.join(videos_dir, video_name))

        # for each message...
        for msg in messages:
            
            # if the file is not a video, skip
            if 'video' not in msg.file.mime_type:
                continue

            # get the message text
            file_name = msg.file.name
            file_path = os.path.join(videos_dir, file_name)

            if (not os.path.exists(file_path)):
                print('-' * 30)
                print('Downloading "{}"'.format(file_name))
                print('-' * 30)
                msg.download_media(file_path)
            else:
                print('"{}" already downloaded '.format(file_name))


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser(description='Telegram video downloader')
    parser.add_argument('-dir', '--directory', type=str)
    parser.add_argument('-gid', '--group-id', type=int)
    parser.add_argument('-lim', '--limit', type=int, default=5)
    args = vars(parser.parse_args())

    # Download the last "limit" videos into disk
    download(args['directory'], args['group_id'], args['limit'])