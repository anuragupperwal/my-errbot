from errbot import BotPlugin, botcmd
import json
from notice import notice_fetcher, cse, ece, me, bt
from chatt import chatter


class Example(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        return 'It **works** !'  # This string format is markdown.

    @botcmd
    def friday(self, msg, args):    #   Tells about friday
        return 'Hola! I am your friend Friday the bot. Anurag is my creator. I have been brought into existence to ease out your tasks. Here I can provide you the latest notices on UIET, KUK website and give you the easy access to check your result. I can provide you all the handwritten and printed notes of all branches and all years. Currently I am being educataed so some resources might not be available, but they will be soon. CHEERS! :)'


    @botcmd     
    def notice(self, msg, args):    #  To get all the notices
        return notice_fetcher()

    @botcmd
    def cse_notice(self, msg, args):    #   to get CSE Notices
        yield "All CSE notices: \n\n"
        yield cse()

    @botcmd
    def ece_notice(self, msg, args):    #   to get ECE Notices
        yield "All ECE notices: \n\n"
        yield ece()

    @botcmd
    def me_notice(self, msg, args):    #    to get ME Notices
        yield "All ME notices: \n\n"
        yield me()

    @botcmd
    def bt_notice(self, msg, args):    #    to get BT Notices
        yield "All BT notices: \n\n"
        yield bt()

    @botcmd
    def chem_notes(self, msg, args):    #   to get chemistry notes
        link = 'https://drive.google.com/open?id=1qd0cevrsSZtvoBUmVQLr1kuyFiKw8inf'
        yield 'Kindly download CHEMISTRY notes from this link: ' 
        yield link

    @botcmd
    def et_notes(self, msg, args):    #     to get chemistry notes
        link = 'https://drive.google.com/open?id=13goyh3f1ut56oQG2Ip36Jhdts2s6jbA4'
        yield 'Kindly download ET notes from this link: ' 
        yield link

    @botcmd
    def bio_notes(self, msg, args):    #    to get chemistry notes
        link = 'https://drive.google.com/open?id=1dXCav7-56bl0bUd9VSE1KFUheU5s8wi8'
        yield 'Kindly download BIOLOGY notes from this link: ' 
        yield link
    
    @botcmd
    def phy_notes(self, msg, args):    #    to get chemistry notes
        link = 'https://drive.google.com/open?id=1u7tfh6qKzakTonUupwfuefCFTmK2EMRE'
        yield 'Kindly download PHYSICS notes from this link: ' 
        yield link



    @botcmd     
    def result(self, msg, args):    #   To get all the notices
        
        f = open('./plugins/err-example/data.json')
        data = json.load(f)
        
        for i in data["result"]:
            return ('> Your' + (i['Title']) + ' is: \n' + i['Link'])

        f.close()

    @botcmd 
    def chat(self, msg, args):  #   to chat with the user
        chatter()
        


    