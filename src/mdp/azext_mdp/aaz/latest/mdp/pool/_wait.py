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
    "mdp pool wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devopsinfrastructure/pools/{}", "2023-12-13-preview"],
        ]
    }

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
        _args_schema.pool_name = AAZStrArg(
            options=["-n", "--name", "--pool-name"],
            help="Name of the pool. It needs to be globally unique.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-.]*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PoolsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class PoolsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOpsInfrastructure/pools/{poolName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "poolName", self.ctx.args.pool_name,
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
                    "api-version", "2023-12-13-preview",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.agent_profile = AAZObjectType(
                serialized_name="agentProfile",
                flags={"required": True},
            )
            properties.dev_center_project_resource_id = AAZStrType(
                serialized_name="devCenterProjectResourceId",
                flags={"required": True},
            )
            properties.fabric_profile = AAZObjectType(
                serialized_name="fabricProfile",
                flags={"required": True},
            )
            properties.maximum_concurrency = AAZIntType(
                serialized_name="maximumConcurrency",
                flags={"required": True},
            )
            properties.organization_profile = AAZObjectType(
                serialized_name="organizationProfile",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            agent_profile = cls._schema_on_200.properties.agent_profile
            agent_profile.kind = AAZStrType(
                flags={"required": True},
            )
            agent_profile.resource_predictions = AAZObjectType(
                serialized_name="resourcePredictions",
            )

            disc_stateful = cls._schema_on_200.properties.agent_profile.discriminate_by("kind", "Stateful")
            disc_stateful.max_agent_lifetime = AAZStrType(
                serialized_name="maxAgentLifetime",
                flags={"required": True},
            )

            fabric_profile = cls._schema_on_200.properties.fabric_profile
            fabric_profile.kind = AAZStrType(
                flags={"required": True},
            )

            disc_vmss = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss")
            disc_vmss.images = AAZListType(
                flags={"required": True},
            )
            disc_vmss.network_profile = AAZObjectType(
                serialized_name="networkProfile",
            )
            disc_vmss.os_profile = AAZObjectType(
                serialized_name="osProfile",
            )
            disc_vmss.sku = AAZObjectType(
                flags={"required": True},
            )
            disc_vmss.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
            )

            images = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").images
            images.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").images.Element
            _element.aliases = AAZListType()
            _element.buffer = AAZStrType()
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"required": True},
            )

            aliases = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").images.Element.aliases
            aliases.Element = AAZStrType()

            network_profile = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").network_profile
            network_profile.subnet_id = AAZStrType(
                serialized_name="subnetId",
                flags={"required": True},
            )

            os_profile = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").os_profile
            os_profile.logon_type = AAZStrType(
                serialized_name="logonType",
            )
            os_profile.secrets_management_settings = AAZObjectType(
                serialized_name="secretsManagementSettings",
            )

            secrets_management_settings = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").os_profile.secrets_management_settings
            secrets_management_settings.certificate_store_location = AAZStrType(
                serialized_name="certificateStoreLocation",
            )
            secrets_management_settings.key_exportable = AAZBoolType(
                serialized_name="keyExportable",
                flags={"required": True},
            )
            secrets_management_settings.observed_certificates = AAZListType(
                serialized_name="observedCertificates",
                flags={"required": True},
            )

            observed_certificates = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").os_profile.secrets_management_settings.observed_certificates
            observed_certificates.Element = AAZStrType()

            sku = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").sku
            sku.name = AAZStrType(
                flags={"required": True},
            )

            storage_profile = cls._schema_on_200.properties.fabric_profile.discriminate_by("kind", "Vmss").storage_profile
            storage_profile.os_disk_storage_account_type = AAZStrType(
                serialized_name="osDiskStorageAccountType",
            )

            organization_profile = cls._schema_on_200.properties.organization_profile
            organization_profile.kind = AAZStrType(
                flags={"required": True},
            )

            disc_azure_dev_ops = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "AzureDevOps")
            disc_azure_dev_ops.organizations = AAZListType(
                flags={"required": True},
            )
            disc_azure_dev_ops.permission_profile = AAZObjectType(
                serialized_name="permissionProfile",
            )

            organizations = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "AzureDevOps").organizations
            organizations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "AzureDevOps").organizations.Element
            _element.parallelism = AAZIntType()
            _element.projects = AAZListType()
            _element.url = AAZStrType(
                flags={"required": True},
            )

            projects = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "AzureDevOps").organizations.Element.projects
            projects.Element = AAZStrType()

            permission_profile = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "AzureDevOps").permission_profile
            permission_profile.groups = AAZListType()
            permission_profile.kind = AAZStrType(
                flags={"required": True},
            )
            permission_profile.users = AAZListType()

            groups = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "AzureDevOps").permission_profile.groups
            groups.Element = AAZStrType()

            users = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "AzureDevOps").permission_profile.users
            users.Element = AAZStrType()

            disc_git_hub = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "GitHub")
            disc_git_hub.organizations = AAZListType(
                flags={"required": True},
            )

            organizations = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "GitHub").organizations
            organizations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "GitHub").organizations.Element
            _element.repositories = AAZListType()
            _element.url = AAZStrType(
                flags={"required": True},
            )

            repositories = cls._schema_on_200.properties.organization_profile.discriminate_by("kind", "GitHub").organizations.Element.repositories
            repositories.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""


__all__ = ["Wait"]