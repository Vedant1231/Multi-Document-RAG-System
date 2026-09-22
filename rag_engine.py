import os
from dotenv import load_dotenv
print("1. Starting...")
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# 1. Set your Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# 2. Automatically locate files inside the script's folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(BASE_DIR, "sample.pdf")
db_path = os.path.join(BASE_DIR, "chroma_db")

# 3. Load the document
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"Place your 'sample.pdf' inside: {BASE_DIR}")
print("2. Loading PDF...")
loader = PyPDFLoader(pdf_path)
docs = loader.load()

# 4. Chunk the document into manageable pieces
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
splits = text_splitter.split_documents(docs)

# 5. Embed text locally on your CPU (100% free via Hugging Face)
print("3. Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 6. Store in local Chroma vector database
print("4. Creating Chroma database...")
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=embeddings, 
    persist_directory=db_path
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 7. Initialize Groq Llama 3
print("5. Initializing LLM...")
llm = ChatGroq(model_name="openai/gpt-oss-20b", temperature=0)

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer the question using strictly the following context:

{context}

Question: {question}
""")

# 8. Query execution via LCEL pipeline
print("6. Ready!")
print("\n=== PDF Knowledge Base Ready (Type 'exit' to quit) ===")
while True:
    query = input("\nAsk a question: ")
    if query.lower().strip() in ["exit", "quit"]:
        break
    if not query.strip():
        continue

    # Retrieve relevant context
    retrieved_docs = retriever.invoke(query)
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

    # Generate answer
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"context": context_text, "question": query})

    print(f"\nAnswer:\n{answer}")