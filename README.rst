==============
file-processor
==============


.. image:: https://img.shields.io/pypi/v/file_processor.svg
        :target: https://pypi.python.org/pypi/file_processor

.. image:: https://img.shields.io/travis/amjadraza/file_processor.svg
        :target: https://travis-ci.com/amjadraza/file_processor

.. image:: https://readthedocs.org/projects/file-processor/badge/?version=latest
        :target: https://file-processor.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A project to processor files


* Free software: MIT license
* Documentation: https://file-processor.readthedocs.io.


Project Environment
-------------------

We create the project environment using below command.

``conda env create -f environment.yml -p ./venv``

Update the existing conda environment

``conda env update -f environment.yml -p ./venv``

Activate the environment

``conda activate ./venv``




Features
--------
This package is to read the text files using API.

Currently it supports below features

* An API to read the text files.
* Process the text file
* Notebooks with sanbox codes
* Package Documentation using Sphnix
* Other DevOps batteries

Run App using Python
---------------------
To develop/test, we can run the app using python with conda environment.

Test/run the using python with input arguments from project home directory

``python file_processor/main.py --file_name test_data/sample1.txt  --start_datetime 2000-01-01T17:25:49Z  --end_datetime 2000-01-06T06:27:36Z``

To set up the local development server using `FASTAPI` server

``uvicorn file_processor.API.main:app --reload``

Go to below link to test the App using `Docs`

```http://127.0.0.1:8000/docs```

To test the App using Postman, follow below link

```http://127.0.0.1:8000/process_file/```

Run Auto Tests
--------------------
We can run auto test of the functions for backend

use below commands

``python -m pytest tests/test_file_processor.py``


Run App using Docker
--------------------
This project includes `Dockerfile` to run the app in Docker container.

Build the docker container

``docker  build -t fileprocessor .``

Run the docker container

``docker run -d --name fp_app -p 80:80 fileprocessor``

Run the docker container using docker-compose

``docker-compose up``

Create Docs
------------
The documentation using Sphnix is already set it up.

Use below command to build from `.docs/` location

``make html``

TODO
----
* Streaming the text file
* Using Spark Streaming to read/process/store the files
* Load Balancer
* Host Docs
* Set up CI/CD


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
