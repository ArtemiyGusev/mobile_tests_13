import allure
import requests
from allure_commons.types import AttachmentType
from config import settings


def get_url_video(session_id: str):
    session = requests.Session()
    session.auth = (settings.usrName, settings.accessKey)
    response = session.get(
        f'{settings.browserStackApi}{session_id}.json')
    return response.json().get('automation_session').get('video_url')


def add_video(session_id: str, name: str):
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + get_url_video(session_id) \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, name, AttachmentType.HTML, '.html')
