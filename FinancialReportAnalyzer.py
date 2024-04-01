# Created by rishijeet at 31/03/24

from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
import os

global api_key
api_key = "sk-***s"


class FinancialReportAnalyzer(object):
    """
    Class to analyze the financial reports
    """
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = api_key

    def read_reports(self):
        loader = PyPDFLoader("reports/hdfc_bank_financial.pdf")
        self.docs = loader.load()

    def parse_doc(self):
        """
        parse the docs
        :return:
        """
        self.read_reports()
        chain = load_qa_chain(llm=OpenAI())
        query = "What's was the profit for 2024"
        response = chain.invoke({"input_documents" : self.docs, "question" : query})
        return response

if __name__ == '__main__':
    f = FinancialReportAnalyzer()
    print(f.parse_doc())
