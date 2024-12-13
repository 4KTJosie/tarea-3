import mongoengine

# Conectar a la base de datos MongoDB
# Reemplaza 'localhost' con tu servidor MongoDB si es necesario
mongoengine.connect('libro_de_recetas', host='localhost', port=27017)

# Definir el modelo de receta utilizando MongoDB (MongoEngine)
class Receta(mongoengine.Document):
    nombre = mongoengine.StringField(required=True)
    ingredientes = mongoengine.StringField(required=True)
    pasos = mongoengine.StringField(required=True)

# Función para agregar una receta
def agregar_receta():
    nombre = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes (separados por comas): ")
    pasos = input("Pasos: ")
    
    # Crear una nueva receta
    receta = Receta(nombre=nombre, ingredientes=ingredientes, pasos=pasos)
    receta.save()
    print("Receta agregada con éxito.")

# Función para actualizar una receta existente
def actualizar_receta():
    ver_recetas()
    receta_id = input("ID de la receta a actualizar: ")
    
    # Buscar receta por ID
    receta = Receta.objects(id=receta_id).first()

    if receta:
        nombre = input(f"Nuevo nombre de la receta (actual: {receta.nombre}): ")
        ingredientes = input(f"Nuevos ingredientes (actual: {receta.ingredientes}): ")
        pasos = input(f"Nuevos pasos (actual: {receta.pasos}): ")

        if nombre:
            receta.nombre = nombre
        if ingredientes:
            receta.ingredientes = ingredientes
        if pasos:
            receta.pasos = pasos

        receta.save()
        print("Receta actualizada con éxito.")
    else:
        print("Receta no encontrada.")

# Función para eliminar una receta existente
def eliminar_receta():
    ver_recetas()
    receta_id = input("ID de la receta a eliminar: ")

    # Buscar receta por ID
    receta = Receta.objects(id=receta_id).first()

    if receta:
        receta.delete()
        print("Receta eliminada con éxito.")
    else:
        print("Receta no encontrada.")

# Función para ver el listado de recetas
def ver_recetas():
    recetas = Receta.objects()  # Obtener todas las recetas
    print("\nListado de recetas:")
    for receta in recetas:
        print(f"ID: {receta.id}, Nombre: {receta.nombre}")
    print()

# Función para buscar ingredientes y pasos de una receta
def buscar_receta():
    nombre = input("Nombre de la receta a buscar: ")

    # Buscar receta por nombre
    receta = Receta.objects(nombre=nombre).first()

    if receta:
        print("\nIngredientes:", receta.ingredientes)
        print("Pasos:", receta.pasos)
    else:
        print("Receta no encontrada.")

# Menú principal
def menu():
    while True:
        print("\n--- Libro de Recetas ---")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta existente")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_receta()
        elif opcion == '2':
            actualizar_receta()
        elif opcion == '3':
            eliminar_receta()
        elif opcion == '4':
            ver_recetas()
        elif opcion == '5':
            buscar_receta()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    menu()