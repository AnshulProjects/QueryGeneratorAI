# Query Generator

This is a Python-based application that generates a query for almost any Language format.

I used the OpenAI completion API to achieve this. I also have a user interface to support the application


## Prompt 

This the prompt I engineered to get reliable queries. I thought it needed to include the database schemas. It also needed deep and though context for the LLM to understand the data. This is then followed by user query and programing langauge

```
"given info from the following schema(s): ___________ , with the given context ___________,  write a query for the following prompt: ___________ , write the query in ___________. print out only the query, nothing else"

```


### Example Use

```python
from QueryGenerator import QueryGenerator

generator = QueryGenerator("API_KEY")

generator.query("Query",["Schemas of all tables"],"Describtion of dataset as detailed as possible", "Langauge to write query in - default, Pandas")

#This call writes to file called query.txt
generator.query("Query",["Schemas of all tables"],"Describtion of dataset as detailed as possible", "Langauge to write query in - default, Pandas", True)


```

#### Before Use
```
$ pip install -r requirements.txt
```