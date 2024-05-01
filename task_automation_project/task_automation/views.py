# task_automation/views.py

from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request, 'task_automation/index.html')

def create_files(request):
    directory = os.path.join('task_automation', 'static', 'task_automation')
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Create text files
    for i in range(1, 4):
        with open(os.path.join(directory, f'file{i}.txt'), 'w') as file:
            file.write(f'Content of file {i}\n')

    # Concatenate files
    concatenated_content = ''
    for i in range(1, 4):
        with open(os.path.join(directory, f'file{i}.txt'), 'r') as file:
            concatenated_content += file.read() + '\n'

    # Write concatenated content to a new file
    with open(os.path.join(directory, 'concatenated.txt'), 'w') as file:
        file.write(concatenated_content)

    # Print concatenated content to console
    print(concatenated_content)

    return HttpResponse("Files created successfully.")
