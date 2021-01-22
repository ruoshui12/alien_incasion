# -*- coding =utf-8 -*-
# @Time : 2021/1/14 14:28
# @Author :Mr
# @File :bullet.py
# @Software :PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        """super(Bullet, self).__init__()
        其实这个是关于python2.x和python3.x的区别，这个是python2.x的表达,等价于python3.x中的super().__init__()。
        Bullet的父类是Sprite，super(Bullet, self)首先找到Bullet的父类（就是类Sprite），然后把类Bullet
        的对象转换为类Sprite的对象。  """
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
