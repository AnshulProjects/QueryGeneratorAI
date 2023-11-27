import openai
class QueryGenerator:

    '''
    Initlizes QueryGenerator

    input : 
        api_key : use OpenAi API key 
    '''
    def __init__(self,api_key):
        openai.api_key = api_key


    '''
    This function generate the query

    query:str: what you want to query from database(s).

    schemas:list:All layouts for all databases mentioned.

    context:str:description of all tables in plain English (Be as descriptive as possible, mention and describe all tables present).

    language:str:defaut is Pandas. This is langauge that the query should be in.

    write_to_file:boolean:default is false. Writes query to file if True.
    
    '''
    def query(self,query,schemas,context,language = "Pandas",write_to_file = False):
        formatted_prompt = f"given info from the following schema(s): {[str(schemas)]} , with the given context {context},  write a query for the following prompt: {query} , write the query in {language}. print out only the query, nothing else"
        try:
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[ 
                {"role": "assistant", "content": formatted_prompt},
                ],
            )

            if(write_to_file):
                query_file = open("query.txt", "W")
                query_file.write(response["choices"][0]["message"]["content"])
                query_file.close()


            return response["choices"][0]["message"]["content"]
        
        except Exception as error:
            
            return f"ERROR WITH GENERATING QUERY: {error}"



        