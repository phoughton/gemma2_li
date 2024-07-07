from llama_index.llms.ollama import Ollama
llm = Ollama(model="gemma2",
             base_url="http://host.docker.internal:11434",
             read_timeout=100)
response = llm.complete("Generate without comment the JSON for a full list of months in a year")
print(response)
