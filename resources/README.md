## `original/acdc-lite_bundled_schema.json`
This is an extract from the ACDC project schema, containing only program,
project, subject and sample nodes, plus terms and definitions. It is in the
format `"<node>.yaml": { }` where the individual schema files are the top
level values.

## `original/cdis_bundled_schema.json`
This is the example schema from the Gen3 project, obtainable from the URL
https://s3.amazonaws.com/dictionary-artifacts/datadictionary/develop/schema.json.
It is also in the format `"<node>.yaml": { }` where the individual schema files
are the top level values.

## `original/json`

* These Gen3 node models are in JSON format but the name of the key in the
  original data is, incongrously, '<node>.yaml'

## `original/yaml`

* `dictionaryutils` is used to load and resolve the YAML schema files to
  create resolved schema, then dump it to file in JSON format.

## `inferred_linkml`

`terms_slots.yaml`: LinkML inferred from `_terms.yaml`.
NB: apart from file-related things like md5sum I don't think many of these are
actually used in the schema. 

`shared_definitions.yaml`: LinkML inferred from `_definitions.yaml`.
Note that a mixin class is used to define ubiquitous properties.

`program_model.yaml`: LinkML inferred from `program.yaml`. Note that `range`
of `id` is `UUID` which is defined in the imported `shared_definitions.yaml`.

`project_model.yaml`, `subject_model.yaml`, `sample_model.yaml` are all
all similarly inferred from the original Gen3 node model YAML files.
