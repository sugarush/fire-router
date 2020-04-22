About
=====

Sugar Router provides a simple, asynchronous router class.

Installation
------------

Suagr Router can be installed with `pip`.

``pip install git+https://github.com/sugarush/sugar-router@master``

Usage
-----

.. code-block:: python

  from sugar_router import Router

  router = Router(methods=['get'])

  @router.get('/v1/endpoint')
  async def endpoint(data):
    print(data)

  @router.get('/v1/endpoint/<id>')
  async def endpoint(data, id):
    print(data, id)

  # Triggers the first handler.
  await router.emit('get', '/v1/endpoint', { 'some': 'data' })

  # Triggers the second handler.
  await router.emit('get', '/v1/endpoint/some-id', { 'more': 'data' })
