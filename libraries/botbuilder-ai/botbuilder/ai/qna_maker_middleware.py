from botbuilder.core import MiddleWare, IntentRecognizerMiddleware
from botbuilder.ai import QnAMaker

class QnaMakerMiddleware(MiddleWare):
    def __init__(self, options=None):
        self.__options = options or None
        if self.__options is None:
            raise TypeError('Invalid QnaMaker Config')
        self.__qna_maker = QnAMaker(self.__options)

    pass