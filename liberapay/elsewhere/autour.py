from __future__ import absolute_import, division, print_function, unicode_literals

from liberapay.elsewhere._base import PlatformOAuth2
from liberapay.elsewhere._exceptions import CantReadMembership
from liberapay.elsewhere._extractors import key
from liberapay.elsewhere._paginators import header_links_paginator


class Autour(PlatformOAuth2):

    # Platform attributes
    name = 'autour'
    display_name = 'Autour.com'
    account_url = 'https://autour.com/{user_name}'
    allows_team_connect = True

    # Auth attributes
    auth_url = 'https://api.autour.com/oauth2'
    access_token_url = 'https://api.autour.com/oauth2/access_token'
    oauth_email_scope = 'user:email'
    oauth_default_scope = ['read:org']

    # API attributes
    api_format = 'json'
    api_paginator = header_links_paginator()
    api_url = 'https://api.autour.com'
    api_app_auth_params = 'client_id={api_key}&client_secret={api_secret}'
    api_friends_path = '/friends/{user_name}'
    api_user_info_path = '/users/{user_name}'
    api_user_name_info_path = '/users/{user_name}'
    api_user_self_info_path = '/oauth2/verify_credentials'
    api_team_members_path = '/orgs/{user_name}/public_members'
    api_friends_path = '/users/{user_id}/following'
    ratelimit_headers_prefix = 'x-ratelimit-'

    # User info extractors
    x_user_id = key('id')
    x_user_name = key('login')
    x_display_name = key('name')
    x_email = key('email')
    x_gravatar_id = key('gravatar_id')
    x_avatar_url = key('avatar_url')
    x_is_team = key('type', clean=lambda t: t.lower() == 'organization')


    


    
