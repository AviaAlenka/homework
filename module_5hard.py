class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        pass


class Video:
    def __init__ (self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        pass


class UrTube:
    def __init__ (self, adult_mode, videos, current_user):
        self.adult_mode = adult_mode
        self.videos = videos
        self.current_user = current_user
        pass


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)