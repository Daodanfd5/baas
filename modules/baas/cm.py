
from common import image

x = {
    'notice': (610, 146, 640, 175)
}


def close_notice(self):
    """
    关闭通知
    @param self:
    """
    if image.compare_image(self, 'cm_notice', 3):
        self.d.click(888, 160)
