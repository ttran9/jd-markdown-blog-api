- Markdown Blog API Notes:

- Section 3, Video 7:
  - create a posts application
    - python manage.py startapp posts.
  - for our Post model keep in mind our content is stored as just raw text. supporting markdown will be completely taken care of in the front end (so our React app).
  - For the thumbnail the "upload_to" is just the handler and inside of that function when we reference "instance.user" that is just so we can grab the user associated with the image.