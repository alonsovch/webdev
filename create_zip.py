import os
import zipfile

def zip_project():
    # Directorio raíz del proyecto
    root_dir = 'webdev'

    # Nombre del archivo ZIP
    zip_filename = 'webdev.zip'

    # Archivos y carpetas a excluir del ZIP
    excluded_items = ['create_zip.py', '__pycache__', '.vscode', 'venv']

    # Abrir el archivo ZIP para escritura
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Recorrer todos los archivos y carpetas en el directorio raíz
        for root, dirs, files in os.walk(root_dir):
            for name in files + dirs:
                # Verificar si el archivo o carpeta está en la lista de exclusiones
                if name not in excluded_items:
                    # Ruta completa del archivo o carpeta
                    path = os.path.join(root, name)
                    # Ruta relativa del archivo o carpeta en el ZIP
                    relpath = os.path.relpath(path, root_dir)
                    # Agregar el archivo o carpeta al ZIP
                    zipf.write(path, relpath)

    print(f'El archivo ZIP "{zip_filename}" ha sido creado correctamente.')

if __name__ == '__main__':
    zip_project()
