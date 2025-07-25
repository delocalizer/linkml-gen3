
from linkml_runtime.utils.schemaview import SchemaView
import yaml

# Load the LinkML schema
sv = SchemaView("resources/inferred_linkml/program_model.yaml")
cls = sv.get_class("program")

# Extract class-level annotations
annotations = {k: str(v.value) for k, v in (cls.annotations or {}).items()}

# parse systemProperties as list
sp_raw = annotations.get("systemProperties", "")
system_props = [x.strip() for x in sp_raw.split(",") if x.strip()] if isinstance(sp_raw, str) else []

# Prepare base Gen3 schema structure
gen3_schema = {
    "id": str(cls.name),
    "category": annotations.get("category", str(cls.name)),
    "submittable": annotations.get("submittable", "true").lower() == "true",
    "systemProperties": system_props,
    "description": str(cls.description) if cls.description else "",
    "properties": {},
    "required": [],
}

# hackfornow known references for $ref-style mapping
ref_map = {
    "UUID": "_definitions.yaml#/UUID",
    "type": "_definitions.yaml#/type",
    "project_id": "_definitions.yaml#/project_id",
    "created_datetime": "_definitions.yaml#/datetime",
    "updated_datetime": "_definitions.yaml#/datetime",
    "state": "_definitions.yaml#/state"
}

# Resolve full set of slots (including mixins)
all_slots = sv.class_induced_slots(str(cls.name))

# Fill out properties and required
for slot in all_slots:
    slot_name = str(slot.name)
    range_str = str(slot.range) if slot.range else "string"
    prop = {}

    if range_str in ref_map:
        prop["$ref"] = ref_map[range_str]
    else:
        prop["type"] = range_str

    if slot.description:
        prop["description"] = str(slot.description)

    gen3_schema["properties"][slot_name] = prop

    if slot.required:
        gen3_schema["required"].append(slot_name)

# Output file
with open("gen3_program.yaml", "w") as f:
    yaml.dump(gen3_schema, f, sort_keys=False)
