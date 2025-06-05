"""
acl_extra_reg_fields Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs
)
from openedx.core.djangoapps.plugins.constants import ProjectType


class AclExtraRegFieldsConfig(AppConfig):
    """
    Configuration for the acl_extra_reg_fields Django application.
    """

    name = 'acl_extra_reg_fields'
    plugin_app = {
    # Configuration setting for Plugin URLs for this app.
    PluginURLs.CONFIG: {
        ProjectType.LMS: {
            # The namespace to provide to django's urls.include.
            PluginURLs.NAMESPACE: 'acl_extra_reg_fields',

            # The application namespace to provide to django's urls.include.
            # Optional; Defaults to None.
            PluginURLs.APP_NAME: 'acl_extra_reg_fields',

            # The regex to provide to django's urls.url.
            # Optional; Defaults to r''.
            PluginURLs.REGEX: r'^acl/',

            # The python path (relative to this app) to the URLs module to be plugged into the project.
            # Optional; Defaults to 'urls'.
            PluginURLs.RELATIVE_PATH: 'urls',
        },
        ProjectType.CMS: {
            # The namespace to provide to django's urls.include.
            PluginURLs.NAMESPACE: 'acl_extra_reg_fields',

            # The application namespace to provide to django's urls.include.
            # Optional; Defaults to None.
            PluginURLs.APP_NAME: 'acl_extra_reg_fields',

            # The regex to provide to django's urls.url.
            # Optional; Defaults to r''.
            PluginURLs.REGEX: r'',

            # The python path (relative to this app) to the URLs module to be plugged into the project.
            # Optional; Defaults to 'urls'.
            PluginURLs.RELATIVE_PATH: 'urls',
        },
    },
}