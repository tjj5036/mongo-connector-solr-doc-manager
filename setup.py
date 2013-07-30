from setuptools import setup
import sys

setup(name='mongo-connector-solr-doc-manager',
      version='1.0.0',
      maintainer='10gen',
      description='Elastic plugin for mongo-connector',
      platforms=['any'],
      author='10gen labs',
      author_email='tyler.jones@10gen.com',
      url='https://github.com/10gen-labs/',
      py_modules=['solr_doc_manager'],
      install_requires=['pysolr >= 3.1.0'],
      license='OSI Approved :: Apache Software License',
      keywords='mongo-connector',
      entry_points={
          'mongo_connector_plugins': 
            ['solr_doc_manager = solr_doc_manager:DocManager']},
      )
