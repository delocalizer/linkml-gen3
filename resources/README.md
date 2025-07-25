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
