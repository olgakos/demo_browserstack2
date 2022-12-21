import allure
from allure_commons.types import AttachmentType

def add_video(browser):
    video_url = (
       f"https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.eu-west-1/"
       f"{browser.driver.session_id}/video-" + browser.driver.session_id + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        body=html,
        name='video_' + browser.driver.session_id,
        attachment_type=AttachmentType.HTML,
        extension='.html',
    )