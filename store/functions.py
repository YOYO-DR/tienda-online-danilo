#azure blob storage
import uuid
from azure.storage.blob import BlockBlobService
from azure.storage.blob.models import ContentSettings
import os

def subirAzureBlobs(self,tipo_a):
  # si esta en un server o subido, se ejecuta el llamado a la config del storage, de lo contrario, le paso los locales
  if 'WEBSITE_HOSTNAME' in os.environ: 
    azure_storage_blob = os.environ['AZURE_STORAGE_BLOB']
    azure_storage_blob_parametros = {parte.split('=')[0]:parte.split('=')[1] for parte in azure_storage_blob.split(' ')}
  else:
    azure_storage_blob_parametros = {'account_name':os.environ.get('ACCOUNT_NAME'),
                                     'container_name':os.environ.get('CONTAINER_NAME'),
                                     'account_key':os.environ.get('ACCOUNT_KEY')}
  tipo_archivo = tipo_a
  name = self.photo.name
  extension = name.split('.')[-1] #lo parto en puntos, pero obtengo el ultimo el cual se obtiene con -1
  account_name = azure_storage_blob_parametros['account_name']
  container_name = azure_storage_blob_parametros['container_name']
  account_key=azure_storage_blob_parametros['account_key']
  # Conectarse al servicio de blobs de Azure
  blob_service_client = BlockBlobService(account_name=account_name, account_key=account_key)
  # Generar un nombre único para el archivo
  filename = 'media/productos/'+str(uuid.uuid4()) + name
  # Subir el archivo al contenedor de Azure
  blob_service_client.create_blob_from_bytes(container_name=container_name, blob_name=filename, blob=self.photo.read(), content_settings=ContentSettings(content_type=tipo_archivo+'/'+extension, content_disposition='inline'))
  #############
  #content-type: https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types
  #image: image/gif, image/png, image/jpeg, image/bmp, image/webp
  #############
  # Guardar la URL del archivo en el modelo
  self.photo = filename