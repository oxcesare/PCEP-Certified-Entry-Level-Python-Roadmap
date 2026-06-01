# En Python, esto es polimorfismo puro sin interfaces:
class LlamaStrategy:
    def generar_respuesta(self, prompt): return "Respuesta Llama"

class MistralStrategy:
    def generar_respuesta(self, prompt): return "Respuesta Mistral"

def interactuar(modelo, prompt):
    # No importa el tipo, solo que el método exista en tiempo de ejecución
    print(modelo.generar_respuesta(prompt))