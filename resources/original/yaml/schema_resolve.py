import json
from dictionaryutils import DataDictionary

# root_dir: The directory to find YAML format schema files.
# Must have _settings, _terms, _definitions.yaml if these are used in $ref's.
dd = DataDictionary(root_dir='.', lazy=False)

# root and data_release keys are generated automatically - do we need them?
dd.schema.pop('root')
dd.schema.pop('data_release')

# write out the resolved schema
with open('resolved_schema.json', 'w') as fh:
    json.dump(dd.schema, fh)
