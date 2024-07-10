import os
from dotenv import load_dotenv, find_dotenv

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
Scarlett Ingrid Johansson ( born November 22, 1984) is an American actress and singer. The world's highest-paid actress in 2018 and 2019, she has been featured multiple times on the Forbes Celebrity 100 list. Time named her one of the 100 most influential people in the world in 2021. Johansson's films have grossed over $15.4 billion worldwide, making her the highest-grossing box office female star of all time. She has received various accolades, including a British Academy Film Award, a Tony Award, and nominations for two Academy Awards and five Golden Globe Awards.

Johansson first appeared on stage in an off-Broadway play as a child actor. She made her film debut in the fantasy comedy North (1994) and gained early recognition for her roles in Manny & Lo (1996), The Horse Whisperer (1998), and Ghost World (2001). Her shift to adult roles came in 2003 with Lost in Translation, for which she won the BAFTA Award for Best Actress. She continued to gain praise for playing a 17th-century servant in Girl with a Pearl Earring (2003), a troubled teenager in A Love Song for Bobby Long (2004) and a seductress in Match Point (2005). The latter marked her first collaboration with Woody Allen, who later directed her in Scoop (2006) and Vicky Cristina Barcelona (2008). Johansson's other works of this period include The Prestige (2006) and the albums Anywhere I Lay My Head (2008) and Break Up (2009), both of which charted on the Billboard 200.

In 2010, Johansson debuted on Broadway in a revival of A View from the Bridge, which won her the Tony Award for Best Performance by a Featured Actress in a Play, and began portraying Black Widow in the Marvel Cinematic Universe film Iron Man 2. She reprised the role in eight films, leading up to her solo feature Black Widow (2021), gaining global stardom. During this period, Johansson starred in the science fiction films Her (2013), Under the Skin (2013) and Lucy (2014). She received two simultaneous Academy Award nominations—Best Actress and Best Supporting Actress—for the respective roles of an actress going through a divorce in the drama Marriage Story (2019) and a single mother in Nazi Germany in the satire Jojo Rabbit (2019), becoming one of the few actors to achieve this feat.

Labeled a sex symbol, Johansson has been referred to as one of the world's most attractive women by various media outlets. She is a prominent brand endorser and supports several charitable causes. Divorced from actor Ryan Reynolds and businessman Romain Dauriac, Johansson has been married to comedian Colin Jost since 2020. She has two children, one with Dauriac and another with Jost.


"""

if __name__ == "__main__":
    dotenv_path = find_dotenv()
    if not dotenv_path:
        raise FileNotFoundError("Could not find .env file")
    load_dotenv(dotenv_path)
    print(f"Loaded .env file from: {dotenv_path}")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    print("Hello Langchain")
    summary_template = """
    given information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    # llm = ChatOpenAI(temperature=0, model_name="gpt2")
    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)