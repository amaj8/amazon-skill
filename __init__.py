from mycroft import MycroftSkill, intent_file_handler


class Amazon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('amazon.intent')
    def handle_amazon(self, message):
        self.speak_dialog('amazon')


def create_skill():
    return Amazon()

