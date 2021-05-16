# interestingly, we have the option of getting top clips by channel
# and top clips by game (or just top clips)
# i think the just chatting clips may be just as lucrative in some cases
# perhaps the best options are to return the top five from each category, and then
# sort the top 5 among them? by viewcount
# furthermore, the trending parameter exists - as clips may be sorted by their popularity
# or viewcount - trending associates with popularity, but not sure how this is measured.
# So, in sum, the categories are:
# from all channels in channel list - which may well be 30 individual channels, plus e-sports clips:
#   -just chatting - top 3 trending, top 3 viewcount (remove overlap?), by day
#   -Valorant - top 3 trending, top 3 viewcount (remove overlap?), by day
#   -top 1 popular clip of the week, by viewcount/trending.
#   -top 1 popular clip of the month, by viewcount.
# so a max of 6 clips, most likely 4-5.
# already uploaded clips must be filtered out as well.
# then, from these 150ish clips, lets say 6 must be determined, per day.
# how??? this has to account for the channels size - ie tenz channel gets higher avg views than sick, so
# if sick hits an insane clip, his viewcount will be higher proportionally, but lower numbers wise
#
# it may also be easy to just - you know - take the top 10 trending valorant clips per day. and upload them.
# whatever im going to bed. FIXED: all setup bullshit?
# TODO: finalize the getting system. determine the clip choosing systems and whatnot.

from twitch import TwitchClient

DAVID_API_KEY = 'pueal2dnr8k6odwu91y7ve7se449on'
GAME = "Valorant"

ClIP_NUMBER = 3
PERIOD = "day"
channel_list = []
clip_list = []


def getClipsByChannel(channels):
    client = TwitchClient(client_id=DAVID_API_KEY)
    for channel in channels:
        client.clips.get_top(channel=channel, game=GAME, limit=ClIP_NUMBER, period=PERIOD)
        client.clips.get_top(channel=channel, game=GAME, limit=ClIP_NUMBER, period=PERIOD)


if __name__ == "__main__":
    getClipsByChannel(channel_list)
    print("The following clips have been downloaded:")
