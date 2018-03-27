#encoding:utf-8

# Some utils can be useful.
from utils import get_url


# Write here subreddit name. Like this one for /r/Damnthatsinteresting.
subreddit = 'Damnthatsinteresting'
# This is for your public telegram channel.
t_channel = '@r_Damnthatsinteresting'


def send_post(submission, r2t):
    what, url, ext = get_url(submission)

    # If this func returns:
    # False – it means that we will not send
    # this submission, let's move to the next.
    # True – everything is ok, we send the submission
    # None – we do not want to send anything this time,
    # let's just sleep.

    # Get all data from submission that we need
    title = submission.title
    link = submission.shortlink
    text = '{}\n{}'.format(title, link)

    if what == 'text':
        punchline = submission.selftext
        text = '{t}\n\n{p}\n\n{l}'.format(t=title, p=punchline, l=link)
        return r2t.send_text(text)
    elif what == 'other':
        base_url = submission.url
        text = '{t}\n{b}\n\n{l}'.format(t=title, b=base_url, l=link)
        return r2t.send_text(text)
    elif what == 'album':
        base_url = submission.url
        text = '{t}\n{b}\n\n{l}'.format(t=title, b=base_url, l=link)
        r2t.send_text(text)
        r2t.send_album(url)
        return True
    elif what in ('gif', 'img'):
        return r2t.send_gif_img(what, url, ext, text)
    else:
        return False
