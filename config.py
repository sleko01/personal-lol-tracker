class APIFetcher:
    api_key = 'RGAPI-ec6c5f59-cbe1-422b-b90b-df7e748a12c5'
    puuid = 'vRcJBT69hPYI4W5NnxWnDsKY-bI0e1Dih7gTAx5KHzGkZtIJXQ9wjxAWMTTTzrIkF-87544a9GCAvA'

    # api_key and puuid are class attributes since they are used everywhere

    @staticmethod
    def get_api_key():
        return APIFetcher.api_key

    @staticmethod
    def get_puuid():
        return APIFetcher.puuid

    @staticmethod
    def set_puuid(new_puuid):
        APIFetcher.puuid = new_puuid
