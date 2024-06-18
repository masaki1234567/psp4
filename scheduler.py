#時間割別課題管理プログラム「scheduler」

#User（ユーザー）クラスはユーザー名、メールアドレスを持つ
class User:
    def __init__(self, name, mailaddress):
        self.name = name
        self.mailaddress = mailaddress

#Schedule（時間割）クラスは授業名、曜日、何限目、色を持つ
class Schedule:
    def __init__(self, name, dayofweek, time, color):
        self.name = name
        self.dayofweek = dayofweek
        self.time = time
        self.time = color

#Homework（課題）クラスは名前、説明文、締め切り、進捗情報を持つ
class Homework:
    def __init__(self, name, description, deadline, progress):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.progress = progress

#Mail（メール）クラスは名前、メールアドレス、文章を持つ
class Mail:
    def __init__(self, name, mailaddress, text):
        self.name = name
        self.mailaddress = mailaddress
        self.text = text

#Reset（リセット）クラスは確認を持つ
class Reset:
    def __init__(self, confirm = False):
        self.confirm = confirm
        


