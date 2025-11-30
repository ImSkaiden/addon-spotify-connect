from librespot.core import Session
import logging


logging.basicConfig(level=logging.DEBUG)

session = Session.Builder() \
    .oauth(None) \
    .create()

access_token = session.tokens().get("streaming")
print("Access Token:", access_token)