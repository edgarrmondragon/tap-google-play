"""GooglePlay Authentication."""


from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


# The SingletonMeta metaclass makes your streams reuse the same authenticator instance.
# If this behaviour interferes with your use-case, you can remove the metaclass.
class GooglePlayAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for GooglePlay."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the GooglePlay API."""
        return {
            'client_id': self.config["client_id"],
            'client_secret': self.config["client_secret"],
            'refresh_token': self.config["refresh_token"],
            'grant_type': 'refresh_token',
        }

    @classmethod
    def create_for_stream(cls, stream) -> "GooglePlayAuthenticator":
        return cls(
            stream=stream,
            auth_endpoint="https://accounts.google.com/o/oauth2/token",
            oauth_scopes="TODO: OAuth Scopes",
        )
