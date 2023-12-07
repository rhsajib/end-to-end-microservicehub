import json
import requests
from django.conf import settings

# https://dashboard.pspdfkit.com/api/playground/
def convert(content):
    instructions = {
        'parts': [
            {
            'file': 'document'
            }
        ]
    }

    response = requests.request(
        'POST',
        'https://api.pspdfkit.com/build',
        headers = {
            'Authorization': f'Bearer {settings.TEXT_TO_PDF_API_TOKEN}'
        },

        files = {
            'document': ('document.docx', content)
        },

        data = {
            'instructions': json.dumps(instructions)
        },
        stream = True
    )

    if response.ok:
        # with open('result.pdf', 'wb') as fd:
        #     for chunk in response.iter_content(chunk_size=8096):
        #         fd.write(chunk)

        return response.content
        
    else:
        print(response.text)