mongo-connector-solr-doc-manager
==================================

Solr Doc Manager for the mongo-connector tool

Usage
-----

Install via::

    python setup.py install

Start the mongo connector with::

    mongo-connector -df solr_doc_manager    

Alternatively, if you download this module, you can 
start the connector with::

    mongo-connector -d <path_to>/solr_doc_manager.py

Solr Specific Instructions
--------------------------

For Solr, you need to define a schema that provides field definitions.
The included schema.xml includes field definitions for the 'name', '_ts',
'ns', and '_id' fields.
The provided schema.xml is meant more for testing the Solr Doc Manager and
the solr instance, but can be used as a starting point for those unfamiliar
with Solr.
The schema also sets the '_id' field to be the unique key through the line

    <uniqueKey>_id</uniqueKey>

Solr does not require all fields to be present, unless a field's 
required attribute is True.
However, the schema must have a line defining every field that may be present
in a document field.

An example field definition would look like so:

    <field name='_ts' type="long" indexed="true" stored="true"/>
    <field name='_id' type="string" indexed="true" stored="true"/>
    <field name='ns' type="string" indexed="true" stored="true"/>


Notes
-----

Previously this was included as part of the mongo-connector package.
The purpose of the separation is to encourage users to install plugins
for mongo-connector with pip as opposed to passing in source files.
However, it is still possible to do that with this module (see usage).
