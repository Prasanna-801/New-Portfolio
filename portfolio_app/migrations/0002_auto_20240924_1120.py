from django.db import migrations

def create_projects(apps, schema_editor):
    Project = apps.get_model('portfolio_app', 'Project')  # Replace 'portfolio_app' with your app name
    Project.objects.create(
        title='My First Project',
        description='This is a description of my first project.',
        image='project_images/your_image.jpg',  # Ensure this path is correct
        github_link='https://github.com/your_github_link',
        live_demo='https://your_live_demo_link.com'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),  # Replace with your last migration file
    ]

    operations = [
        migrations.RunPython(create_projects),
    ]
