ML model testing
===========================

Complete code (including a trained model) to deploy and inference a machine learning model (built on the iris dataset) using Docker and Flask.

1. With terminal navigate to the root of this repository
--------------------------------------------------------

2. Build docker image
---------------------
.. code-block::

    docker build -t image_name .

3. Run container
----------------
.. code-block::

    docker run --name container_name -p 5000:5000 image_name

4. Output will contain
----------------------

Use this url in chrome to see the model frontend;