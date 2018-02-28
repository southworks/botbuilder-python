import json
import asyncio
import requests


class QnAMaker(object):
    def __init__(self, options, http_client):
        self.__qnaMakerServiceEndpoint = 'https://westus.api.cognitive.microsoft.com/qnamaker/v3.0/knowledgebases/'
        self.__json_mime_type = 'application/json'
        self.__api_management_header = 'Ocp-Apim-Subscription-Key'
        
        self.__http_client = http_client or False
        if not self.__http_client:
            raise TypeError('HTTP Client failed')
        self.__options = options or False
        if not self.__options:
            raise TypeError('Options config error')

        self.__answerUrl = "%s%s/generateanswer" % (self.__qnaMakerServiceEndpoint,options.knowledge_base_id)

        if self.__options.ScoreThreshold == 0:
            self.__options.ScoreThreshold = 0.3  # Note - SHOULD BE 0.3F 'FLOAT'
        
        if self.__options.Top == 0:
            self.__options.Top = 1
        
        if self.__options.StrictFilters is None:
            self.__options.StrictFilters = MetaData()

        if self.__options.MetadataBoost is None:
            self.__options.MetadataBoost = MetaData()

    async def get_answers(self, question):        # HTTP call
        headers = {
            self.__api_management_header: self.__options.subscription_key,
            "Content-Type": self.__json_mime_type
        }
        
        payload = json.dumps({
            "question": question
        })
        # POST request to QnA Service
        content = requests.post(self.__answerUrl, headers=headers, data=payload)
        return content.json()


class QnAMakerOptions(object):
    def __init__(self, subscription_key, knowledge_base_id, score_threshold, top, strict_filters, metadata_boost):
        self.subscription_key = subscription_key
        self.knowledge_base_id = knowledge_base_id
        self.score_threshold = score_threshold
        self.top = top
        self.strict_filters = strict_filters
        self.metadata_boost = metadata_boost


class MetaData(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class QueryResult(object):
    def __init__(self, questions, answer, score, metadata, source, qna_id):
        self.questions = questions
        self.answer = answer
        self.score = score
        self.metadata = metadata
        self.source = source
        self.qna_id = qna_id


class QueryResults(object):
    def __init__(self, answers):
        self.__answers = answers
