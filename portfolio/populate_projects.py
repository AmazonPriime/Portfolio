import os, django, requests, json
from datetime import datetime
from dateutil.parser import parse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from projects.models import Project

def populate():
    repositories = get_repositories()
    projects = Project.objects.all()
    for repository in repositories:
        name = repository['name']
        project = Project.objects.get_or_create(name = name)[0]
        if repository['description']:
            project.description = repository['description']
        else:
            project.description = "No description."
        project.language = repository['language']
        project.url = repository['html_url']
        project.date_created = parse(repository['created_at'])
        project.date_updated = parse(repository['updated_at'])
        project.save()

def get_repositories():
    response = requests.get("https://api.github.com/users/AmazonPriime/repos")
    return json.loads(response.content)

if __name__ == '__main__':
    populate()
