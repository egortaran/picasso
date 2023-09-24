import mimetypes

from celery import shared_task
from .models import File

# Only for this types: https://www.iana.org/assignments/media-types/media-types.xhtml
handlers = {
    'text': 'handle_text',
    'application': 'handle_application',
    'audio': 'handle_audio',
    'example': 'handle_example',
    'image': 'handle_image',
    'message': 'handle_message',
    'model': 'handle_model',
    'multipart': 'handle_multipart',
    'video': 'handle_video',
}


@shared_task()
def process_file(file_id):
    file_instance = File.objects.get(id=file_id)
    file_path = file_instance.file.path

    type_info = mimetypes.guess_type(file_path)
    if type_info[0]:
        type_info = type_info[0].split('/')[0]

    handler = handlers.get(type_info)
    if handler:
        print(handler)  # ToDo Change to def

        file_instance.processed = True
        file_instance.save()
