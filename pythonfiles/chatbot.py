from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"
reader = PdfReader('assets/AC.pdf')
raw_text = ''

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

texts = text_splitter.split_text(raw_text)
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts, embeddings)
chain = load_qa_chain(OpenAI(), chain_type="stuff")


def process_query(query):
    query.lower()
    if "hi" == query or "hello" == query:
        return "Hi. How can i help you?"
    docs = docsearch.similarity_search(query)
    result = chain.run(input_documents=docs, question=query)
    return result
