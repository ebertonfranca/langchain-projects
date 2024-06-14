from urllib import response
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPEN_API_KEY")

def generate_company_name():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=openai_api_key
    )

    company_name = llm.invoke(
        [SystemMessage(
            
            content="Você é um assistente IA que sempre responde em Português do Brasil"
            ),

        HumanMessage(
            content="Gere 5 ideias de nomes para empresas no segmento Pets"
        ),
        ]
    )
    return company_name

if __name__ == "__main__":
    print("\n" + "=" * 30)
    print(generate_company_name())
    print("=" * 30)
   

