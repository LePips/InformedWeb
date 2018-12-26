# InformedWeb

Django web server to communicate with Firebase.

Nothing will be stored in the Django database, this is only for communication
with Firebase to easily view, add, and delete data.

Eventually this will be hosted online so that tampering is prevented.

### Installation

Written for Python 3.7.1 and Django 2.1.4

You might want to create a python virtual environment before installing.

Download repo and to install all required dependencies, execute:

`sh InstallDependencies.sh`

This will also update pip if not updated to the latest version.

To communicate with Firebase, you must be given a private key from the Firebase console.
- Move your given `.json` key to the main project directory.

### Fabfile

Instead of using the `python manage.py runserver 8080` command, there is
an available fabfile.py to shorten commands and increase functionality
with only `fab start`

### Style

Following (at least trying to) Pep8
https://www.python.org/dev/peps/pep-0008/

# JSON

Below is the specifications of the structure that the JSON sent to and
from Firebase should be structured. More to come.

### Election
```
{
    "id": "660c2206",
    "title": "2000 Presidential Election",
    "category": "national",
    "coverImageUrl": "image.jpg",
    "role": 4325,
    "candidates": [
        "hjk5432",
        "432kja"
    ],
    "sections": [
        {
            "title": "description",
            "references": [
                "dragomax2000, hillo2343, runningrenob"
            ],
            "content": "Velit occaecat tempor nostrud et culpa irure mollit commodo elit fugiat ex. Ullamco nisi quis ea elit sint nostrud proident labore eiusmod aute incididunt labore do."
        }
    ]
}
