from storages.backends.azure_storage import AzureStorage
import os

if 'WEBSITE_HOSTNAME' in os.environ: 
    azure_storage_blob = os.environ['AZURE_STORAGE_BLOB']
    azure_storage_blob_parametros = {parte.split(' = ')[0]:parte.split(' = ')[1] for parte in azure_storage_blob.split('  ')}
else:
    azure_storage_blob_parametros = {'account_name':os.environ.get('ACCOUNT_NAME'),
                                     'container_name':os.environ.get('CONTAINER_NAME'),
                                     'account_key':os.environ.get('ACCOUNT_KEY')}
    
class PublicAzureStaticStorage(AzureStorage):
    account_name = azure_storage_blob_parametros['account_name']
    account_key = azure_storage_blob_parametros['account_key']
    azure_container = azure_storage_blob_parametros['container_name']
    location = 'static/'  # ubicación dentro del contenedor
    expiration_secs = None

# Configuración para los archivos de media
class PublicAzureMediaStorage(AzureStorage):
    account_name = azure_storage_blob_parametros['account_name']
    account_key = azure_storage_blob_parametros['account_key']
    azure_container = azure_storage_blob_parametros['container_name']
    location = 'media/'  # ubicación dentro del contenedor
    expiration_secs = None