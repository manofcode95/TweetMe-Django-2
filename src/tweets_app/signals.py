from django import dispatch

hashtag_done=dispatch.Signal(providing_args=['hashtags'])