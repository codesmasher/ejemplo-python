import debugpy

debugpy.listen(("0.0.0.0", 5678))
print("Esperando a que el debugger se conecte...")
debugpy.wait_for_client()

print("¡Hola desde Docker con debugging!")
