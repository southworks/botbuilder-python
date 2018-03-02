import json
import requests


class QnAMaker(object):
    def __init__(self, options):
        self.__qnaMakerServiceEndpoint = 'https://westus.api.cognitive.microsoft.com/qnamaker/v3.0/knowledgebases/'
        self.__json_mime_type = 'application/json'
        self.__api_management_header = 'Ocp-Apim-Subscription-Key'

        self.__options = options or False
        if not self.__options:
            raise TypeError('Options config error')

        self.__answerUrl = "%s%s/generateanswer" % (self.__qnaMakerServiceEndpoint, options["knowledge_base_id"])

        if self.__options.get("score_threshold", None) is None:
            self.__options["score_threshold"] = 0.3  # Note - SHOULD BE 0.3F 'FLOAT'
        
        if self.__options.get("top", None) is None or 0:
            self.__options["top"] = 1
        
        if self.__options.get("strict_filters", None) is None:
            self.__options["strict_filters"] = MetaData()

        if self.__options.get("meta_data_boost", None) is None:
            self.__options["meta_data_boost"] = MetaData()

    def get_answers(self, question):        # HTTP call
        headers = {
            self.__api_management_header: self.__options["subscription_key"],
            "Content-Type": self.__json_mime_type
        }
        
        payload = json.dumps({
            "question": question
        })
        # POST request to QnA Service
        content = requests.post(self.__answerUrl, headers=headers, data=payload).json()
        qna_result = QnaMakerResult(content)
        return qna_result


class QnAMakerOptions(object):
    def __init__(self, subscription_key, knowledge_base_id, score_threshold, top, strict_filters, metadata_boost):
        self.subscription_key = subscription_key
        self.knowledge_base_id = knowledge_base_id
        self.score_threshold = score_threshold
        self.top = top
        self.strict_filters = strict_filters
        self.metadata_boost = metadata_boost


class MetaData(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value


class QnaMakerResult(object):
    def __init__(self, qna_response=None, metadata=None, source=None, qna_id=None):
        self.__dict__ = qna_response
        self.question = self.__dict__['answers'][0]['questions'][0]
        self.answer = self.__dict__['answers'][0]['answer']
        self.score = self.__dict__['answers'][0]['score']
        self.metadata = metadata
        self.source = source
        self.qna_id = qna_id



