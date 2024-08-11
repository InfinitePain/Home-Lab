AUTHENTICATION_SOURCES = ['oauth2', 'internal']
OAUTH2_CONFIG = [
    {
        'OAUTH2_NAME': 'authentik',
        'OAUTH2_DISPLAY_NAME': 'Authentik',
        'OAUTH2_CLIENT_ID' : '<client-id>',
        'OAUTH2_CLIENT_SECRET' : '<client-secret>',
        'OAUTH2_TOKEN_URL': 'https://authentik.example.com/application/o/token/',
        'OAUTH2_AUTHORIZATION_URL': 'https://authentik.example.com/application/o/authorize/',
        'OAUTH2_SERVER_METADATA_URL': 'https://authentik.example.com/application/o/pgadmin-oauth-application/.well-known/openid-configuration',
        'OAUTH2_API_BASE_URL': 'https://authentik.example.com/',
        'OAUTH2_USERINFO_ENDPOINT': 'https://authentik.example.com/application/o/userinfo/',
        'OAUTH2_SCOPE': 'openid email profile',
        'OAUTH2_USERNAME_CLAIM': 'preferred_username',
        'OAUTH2_ICON': 'fa-expeditedssl',
        'OAUTH2_BUTTON_COLOR': '#fd4b2d',
        'OAUTH2_SSL_CERT_VERIFICATION': True,
        'OAUTH2_LOGOUT_URL': 'https://authentik.example.com/application/o/pgadmin-oauth-application/end-session/'
    }
]
OAUTH2_AUTO_CREATE_USER = True