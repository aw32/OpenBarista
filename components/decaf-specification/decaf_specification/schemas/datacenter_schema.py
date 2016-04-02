__author__ = 'sdjoum'
# Copyright 2016 DECaF Project Group
# This file is part of the DECaF project and originally derives from OpenMANO
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import basic_schema as bs


datacenter_schema_properties={
                "name": bs.name_schema,
                "description": bs.description_schema,
                "type": {"type":"string","enum":["openvim","openstack"]},
                "vim_url": bs.description_schema,
                "vim_url_admin": bs.description_schema,
            }

datacenter_schema = {
    "title":"datacenter information schema",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type":"object",
    "properties":{
        "datacenter":{
            "type":"object",
            "properties":datacenter_schema_properties,
            "required": ["name", "vim_url"],
            "additionalProperties": True
        }
    },
    "required": ["datacenter"],
    "additionalProperties": False
}


datacenter_edit_schema = {
    "title":"datacenter edit nformation schema",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type":"object",
    "properties":{
        "datacenter":{
            "type":"object",
            "properties":datacenter_schema_properties,
            "additionalProperties": False
        }
    },
    "required": ["datacenter"],
    "additionalProperties": False
}

datacenter_action_schema = {
    "title":"datacenter action information schema",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type":"object",
    "properties":{
        "net-update":{"type":"null",},
        "net-edit":{
            "type":"object",
            "properties":{
                "net": bs.name_schema,  #name or uuid of net to change
                "name": bs.name_schema,
                "description": bs.description_schema,
                "shared": {"type": "boolean"}
            },
            "minProperties": 1,
            "additionalProperties": False
        },
        "net-delete":{
            "type":"object",
            "properties":{
                "net": bs.name_schema,  #name or uuid of net to change
            },
            "required": ["net"],
            "additionalProperties": False
        }

    },
    "minProperties": 1,
    "maxProperties": 1,
    "additionalProperties": False
}


datacenter_associate_schema={
    "title":"datacenter associate information schema",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type":"object",
    "properties":{
        "datacenter":{
            "type":"object",
            "properties":{
                "vim_tenant": bs.id_schema,
                "vim_tenant_name": bs.name_schema,
            },
#            "required": ["vim_tenant"],
            "additionalProperties": True
        }
    },
    "required": ["datacenter"],
    "additionalProperties": False
}