# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "logic integration-account partner update",
)
class Update(AAZCommand):
    """Update an integration account partner.

    :example: Update partner
        az logic integration-account partner update -g rg -n partner --integration-account-name name --content '{b2b:{businessIdentities:[{qualifier:CC,value:DD}]}}'
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/partners/{}", "2019-05-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.integration_account_name = AAZStrArg(
            options=["--integration-account-name"],
            help="The integration account name.",
            required=True,
            id_part="name",
        )
        _args_schema.partner_name = AAZStrArg(
            options=["-n", "--name", "--partner-name"],
            help="The integration account partner name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Partner"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Partner",
            help="The resource location.",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Partner",
            help="The resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.content = AAZObjectArg(
            options=["--content"],
            arg_group="Properties",
            help="The partner content.",
        )
        _args_schema.metadata = AAZFreeFormDictArg(
            options=["--metadata"],
            arg_group="Properties",
            help="The metadata.",
            nullable=True,
            blank={},
        )
        _args_schema.partner_type = AAZStrArg(
            options=["--partner-type"],
            arg_group="Properties",
            help="The partner type.",
            enum={"B2B": "B2B", "NotSpecified": "NotSpecified"},
        )

        content = cls._args_schema.content
        content.b2b = AAZObjectArg(
            options=["b2b"],
            help="The B2B partner content.",
            nullable=True,
        )

        b2b = cls._args_schema.content.b2b
        b2b.business_identities = AAZListArg(
            options=["business-identities"],
            help="The list of partner business identities.",
            nullable=True,
        )

        business_identities = cls._args_schema.content.b2b.business_identities
        business_identities.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.content.b2b.business_identities.Element
        _element.qualifier = AAZStrArg(
            options=["qualifier"],
            help="The business identity qualifier e.g. as2identity, ZZ, ZZZ, 31, 32",
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The user defined business identity value.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountPartnersGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.IntegrationAccountPartnersCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IntegrationAccountPartnersGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "partnerName", self.ctx.args.partner_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_integration_account_partner_read(cls._schema_on_200)

            return cls._schema_on_200

    class IntegrationAccountPartnersCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "partnerName", self.ctx.args.partner_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_integration_account_partner_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("content", AAZObjectType, ".content", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("metadata", AAZFreeFormDictType, ".metadata")
                properties.set_prop("partnerType", AAZStrType, ".partner_type", typ_kwargs={"flags": {"required": True}})

            content = _builder.get(".properties.content")
            if content is not None:
                content.set_prop("b2b", AAZObjectType, ".b2b")

            b2b = _builder.get(".properties.content.b2b")
            if b2b is not None:
                b2b.set_prop("businessIdentities", AAZListType, ".business_identities")

            business_identities = _builder.get(".properties.content.b2b.businessIdentities")
            if business_identities is not None:
                business_identities.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.content.b2b.businessIdentities[]")
            if _elements is not None:
                _elements.set_prop("qualifier", AAZStrType, ".qualifier", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})

            metadata = _builder.get(".properties.metadata")
            if metadata is not None:
                metadata.set_anytype_elements(".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_integration_account_partner_read = None

    @classmethod
    def _build_schema_integration_account_partner_read(cls, _schema):
        if cls._schema_integration_account_partner_read is not None:
            _schema.id = cls._schema_integration_account_partner_read.id
            _schema.location = cls._schema_integration_account_partner_read.location
            _schema.name = cls._schema_integration_account_partner_read.name
            _schema.properties = cls._schema_integration_account_partner_read.properties
            _schema.tags = cls._schema_integration_account_partner_read.tags
            _schema.type = cls._schema_integration_account_partner_read.type
            return

        cls._schema_integration_account_partner_read = _schema_integration_account_partner_read = AAZObjectType()

        integration_account_partner_read = _schema_integration_account_partner_read
        integration_account_partner_read.id = AAZStrType(
            flags={"read_only": True},
        )
        integration_account_partner_read.location = AAZStrType()
        integration_account_partner_read.name = AAZStrType(
            flags={"read_only": True},
        )
        integration_account_partner_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        integration_account_partner_read.tags = AAZDictType()
        integration_account_partner_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_integration_account_partner_read.properties
        properties.changed_time = AAZStrType(
            serialized_name="changedTime",
            flags={"read_only": True},
        )
        properties.content = AAZObjectType(
            flags={"required": True},
        )
        properties.created_time = AAZStrType(
            serialized_name="createdTime",
            flags={"read_only": True},
        )
        properties.metadata = AAZFreeFormDictType()
        properties.partner_type = AAZStrType(
            serialized_name="partnerType",
            flags={"required": True},
        )

        content = _schema_integration_account_partner_read.properties.content
        content.b2b = AAZObjectType()

        b2b = _schema_integration_account_partner_read.properties.content.b2b
        b2b.business_identities = AAZListType(
            serialized_name="businessIdentities",
        )

        business_identities = _schema_integration_account_partner_read.properties.content.b2b.business_identities
        business_identities.Element = AAZObjectType()

        _element = _schema_integration_account_partner_read.properties.content.b2b.business_identities.Element
        _element.qualifier = AAZStrType(
            flags={"required": True},
        )
        _element.value = AAZStrType(
            flags={"required": True},
        )

        tags = _schema_integration_account_partner_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_integration_account_partner_read.id
        _schema.location = cls._schema_integration_account_partner_read.location
        _schema.name = cls._schema_integration_account_partner_read.name
        _schema.properties = cls._schema_integration_account_partner_read.properties
        _schema.tags = cls._schema_integration_account_partner_read.tags
        _schema.type = cls._schema_integration_account_partner_read.type


__all__ = ["Update"]